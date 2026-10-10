# Chaos: destrukce a látky

Chaos je fyzikální engine Unrealu. Kapitola z něj bere dvě oblasti, které knihovna zatím neměla: destrukci ve velkém a látku jako samostatný asset. Destrukce stojí na tom, jak Epic stavěl LEGO Fortnite: otevřený svět, ve kterém kterýkoli hráč rozbije cokoli, od drobností po celé budovy, a to v multiplayeru. Látku popisuje nová pipeline přes Dataflow graf, doplněná postupem z 5.8. Pozor na verzi: přednáška, na které kapitola stojí, je z UE 5.4 (2024) a řada popsaných nástrojů tehdy byla experimentální nebo v betě. Ragdoll a fyzikální postavy jsou v kapitole [Ragdoll](ragdoll.md), lana v [Kabelech a lanech](lana-kabely.md), plavání ve [Vodě](voda-a-buoyancy.md) a nahlížení do fyzikální scény v [Ladění](debugging.md#chaos-visual-debugger-zevnitr-faze-solveru-kontakty-a-klient-vedle-serveru).

---

## Budova, kterou rozbije kdokoli: graf spojení na serveru, cluster union ve fyzice

**Zdroj:** [Using Chaos Physics for Large-Scale and High-Fidelity Scenes | Unreal Fest 2024](https://www.youtube.com/watch?v=uCYGFdEWyZw) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~51 min, přednáška (vedoucí fyzikální programátor Epicu; UE 5.4)

**Shrnutí:** LEGO Fortnite potřeboval otevřený síťový svět, ve kterém může kterýkoli hráč rozbít jakýkoli simulovaný objekt. Práce se dělí do tří vrstev. Assety se lámou nedestruktivně v Dataflow grafu. Gameplay vrstva drží graf spojení: co je s čím spojené a co drží zem. A fyzika slepí spojené kusy do jednoho tělesa, cluster unionu, který umí prasknout jen v jednom místě. Háček: graf spojení je herní systém, ne fyzika. Kusy ve fyzice spojí teprve cluster union.

### Rozpad myšlenky

**Výchozí situace.** Velký otevřený svět, víc klientů v síti a destrukce od drobných předmětů po celé dynamické budovy, se kterými může každý hráč cokoli udělat [(0:52)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=52s). Z toho plynou čtyři úkoly [(1:40)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=100s):
- opakovatelná výroba spousty rozbitných assetů,
- jejich spojování do větších staveb i se světem,
- škálování, protože se hýbou tisíce kusů,
- síť, ve které na simulaci sahá víc hráčů najednou.

**Geometry Collection.** Asset, který drží rozbitný objekt: sada fyzikálních těles, která se aktualizují a kreslí společně a lehce, každý kus pevně skinovaný. Úrovně clusteringu seskupují kusy do větších hmot pro simulaci [(1:40)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=100s).

**Lámání v Dataflow.** Nástroje na fraktury jsou uzly v grafu, který jde opakovaně pouštět na mnoho assetů [(2:27)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=147s). Graf umí shlukovat kusy podle úrovně, počtu nebo hustoty, generovat konvexní obaly a mít výjimky pro zvláštní případy. Příkladem jsou dveře, které si drží tvar, aby jimi hráči prošli. Utility blueprint pak graf spustí nad sadou assetů a vydá hotovou geometry collection i blueprint aktéra připraveného k přetažení do levelu. Dataflow pro destrukci byl v 5.4 experimentální [(3:14)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=194s).

**Graf spojení jen na serveru.** Spojení mezi aktéry spravuje komponenta a systém connectivity graph. Klíčové rozhodnutí bylo udělat destrukci serverově autoritativní: spojení sleduje jen server a klient je vůbec nezná [(3:14)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=194s). Graf je neorientovaný, takže se v něm rychle najdou spojené objekty, jejich ostrovy a to, jestli je něco drží u země, nebo už má padat dynamicky [(4:00)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=240s).

**Cluster union ve fyzice.** Graf řekne, co má být spojené, ale nic nespojí. To dělá komponenta cluster union, která z víc geometry collections udělá jedno fyzikální těleso a rozhoduje, které vnitřní částice patří do kterého unionu [(4:00)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=240s). Umí částečnou destrukci: poškození rozbije jedno místo a zbytek zůstane připojený [(4:47)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=287s). Nahrazuje starší cluster groups, které šly snadno nastavit v editoru, ale neměly jednoduchý způsob, jak kusy seskupovat dynamicky za běhu.

**Co hráč postaví, musí i plavat.** Hra se odehrává na ostrově s řekami, jezery a oceánem a buoyancy musí unést cokoli, co hráči postaví [(10:19)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=619s). Projekt běží s asynchronní fyzikou, takže výpočet musí běžet na fyzikálním vlákně. Collision modifier ve fázi midphase ohlásí objekty, které protínají vodní objem. Jejich bounds se pak postupně dělí do hierarchie, až vznikne odhad ponořeného objemu, jeho těžiště a plochy pod vodou. Objem s těžištěm dají vztlak, plocha odpor a proud, takže loď postavená na řece pluje k jezeru [(11:06)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=666s). Plugin Buoyancy je v 5.4 a funguje s jakoukoli rigid částicí: geometry collection, cluster unionem i obyčejným static meshem [(11:58)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=718s).

> **Pozn.:** Rozdělení na herní graf a fyzikální union je přenositelné i mimo multiplayer. Otázka „drží to ještě?" je herní pravidlo, ne fyzikální výpočet, a proto se dá ladit, debugovat i ukládat zvlášť. Serverová autorita je naopak výslovně rozhodnutí kvůli konzistentnějšímu světu, ne vlastnost systému. Přednáška je z 5.4 a jak daleko se Dataflow pro destrukci od té doby posunul, knihovna zatím nemá z čeho říct. Starší cesty k plavání (pontoony, physical material v 5.7) jsou ve [Vodě](voda-a-buoyancy.md#buoyancy-v-57-physical-material-misto-pontoonu).

**Souvislosti:** [Rejstřík: Geometry Collection](../rejstrik.md#geometry-collection) · [Rejstřík: Cluster Union](../rejstrik.md#cluster-union) · [Rejstřík: Dataflow](../rejstrik.md#dataflow) · [Voda a buoyancy](voda-a-buoyancy.md)

---

## Destrukce, kterou procesor unese: konvexy, debris, sdílené instance a strop zlomů

**Zdroj:** [Using Chaos Physics for Large-Scale and High-Fidelity Scenes | Unreal Fest 2024](https://www.youtube.com/watch?v=uCYGFdEWyZw) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~51 min, přednáška (vedoucí fyzikální programátor Epicu; UE 5.4)

**Shrnutí:** Velká destrukce bere výkon čtyřmi cestami:
- kontakty, třeba když budova leží na terénu,
- vykreslování, protože každá geometry collection má vlastní scene proxy,
- paměť částic,
- špička ve chvíli výbuchu.

Na každou má LEGO Fortnite jinou páku. Cluster union se postupně zabalí do konvexních obalů, které slouží jen simulaci. Opakované kusy se kreslí jako sdílené instance a odlomené drobky se stanou debris bez vlivu na hru. A počet zlomů za snímek má strop. Háček: strop zlomů mění chování a víc kusů dopadne na zem vcelku. Je to cena za to, že fyzikální vlákno nedostane nerozumnou dávku najednou.

### Rozpad myšlenky

**Kontakty.** Velká dynamická budova, která dopadne na height field, vyrobí spoustu kontaktů a broad a mid phase vydají spoustu párů k testování [(4:47)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=287s). Cluster union se proto postupně zjednodušuje: zabalí se do konvexního obalu, který slouží jen simulaci. Postava, která budovou probíhá, se dál ptá skutečné geometrie, ta je jen vyřazená ze simulace [(5:33)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=333s). V ukázce se ze čtrnácti kvádrů stane sedm, pak čtyři a nakonec jediný konvex. Kdy přestat, rozhoduje heuristika objemu: když by se obal od tvaru odchýlil příliš, zjednodušování skončí. S výchozím nastavením by ukázka skončila zhruba ve třetím kroku [(6:20)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=380s).

**Vykreslování.** Každá geometry collection se kreslí sama, protože při náhodné fraktuře je každý kus jedinečný a potřebuje vlastní vertex data [(6:20)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=380s). Často to ale neplatí. Sud má stejné víko a dno a dvacet až třicet stejných dužin [(7:07)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=427s). ISM pooling proto dovolí víc collections sdílet pole kusů a kreslit je jako instance. A když se tentýž asset ve scéně opakuje mnohokrát, nerozbitý kořenový mesh se zhroutí do jedné instance a všechny výskyty se vykreslí najednou [(7:55)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=475s).

**Debris.** Drobné kusy, které se při velké destrukci odlomí, jsou listy grafu bez dalšího spojení [(8:43)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=523s). Jako debris už nemají vliv na hru a nesmějí tlačit jiná dynamická tělesa. Vypadnou z vnější akcelerační struktury, takže je mimo fyzikální vlákno nenajde žádný scene query, a ušetří se dotazy i aktualizace. Při srážce s čímkoli, co debris není, se druhé těleso bere jako nekonečně těžké, kdežto dva kusy debris se od sebe odrazí normálně [(9:30)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=570s). V LEGO Fortnite běžel debris jen na klientovi [(9:30)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=570s).

**Paměť.** Částice fyzikální scény jsou uložené jako struct of arrays a řada vlastností se ukládala s vyšší přesností, než potřebovala. Zúžení ušetřilo zhruba 144 bajtů na každou částici [(37:44)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=2264s), [(38:31)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=2311s). Geometry collection má neměnnou rest collection uloženou v assetu a za běhu z ní dynamickou kopii. Z té zmizela data, která byla zdvojená nebo neměnná [(39:18)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=2358s), [(40:06)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=2406s). Řídká pole se stlačí: asset s tisícem částic, ze kterých se simuluje sto shluků, už nenese prázdné místo [(41:41)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=2501s). A částice se nemusí vytvářet předem, ale až ve chvíli zlomu. Svět plný rozbitných objektů tak potřebuje méně paměti, cena se ale přesune do okamžiku fraktury [(42:27)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=2547s), [(43:13)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=2593s).

**Špička výbuchu.** Exploze rozloží napětí do částic v dosahu a model zlomů aktivuje všechno, co je nad limitem. U velkých staveb z mnoha dílů to znamená obrovské množství zlomů v jednom snímku [(43:13)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=2593s), [(44:00)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=2640s). Řešením je strop. Za snímek se zpracuje jen daný počet zlomů a zbytek se odloží do dalších snímků. Co přeteče i limit odložených, se zahodí, dokud to hra znovu nenapne. Obojí řídí konzolové proměnné [(44:46)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=2686s). Chování se tím změní: víc kusů dopadne na zem vcelku a některé se rozbijí až tam. Při 60 snímcích za sekundu a stropu tři zlomy na snímek se zpracuje 180 částic za sekundu a cena se rozloží do mnoha snímků [(45:32)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=2732s).

**Události.** Callback na každý zásah zvlášť (Simulation Generates Hit Events) je při destrukci drahý: skok přes virtuální rozhraní a často až do Blueprintu, jen aby se události posbíraly třeba pro zvuk [(47:52)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=2872s), [(48:38)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=2918s). Event Relay vedle toho nabízí delegáty po typech událostí, které dostanou celý buffer najednou. LEGO Fortnite přes něj centralizoval zásahy a zlomy pro audio [(49:25)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=2965s). Starý způsob zůstává: když potřebuješ jen, aby trefený aktér věděl, že ho něco trefilo, stačí.

> **Pozn.:** Všechny páky sdílejí jednu myšlenku: **simulace nemusí vidět to, co vidí hráč.** Obal místo budovy, debris místo plnohodnotných těles, instance místo jedinečných kusů. Strop zlomů je stejný tah jako [strop instancí u Niagary](niagara-vykon.md#effect-type-jeden-asset-ktery-rozhoduje-o-vsem) nebo dvacet aktivních nepřátel v [AI ve velkém](ai-ve-velkem.md#velky-nepritel-na-malem-agentovi-offset-cesty-ktery-nevyjede-z-navigace): nejdřív omezit, kolik práce smí přijít najednou. Proč pomáhá struct of arrays, vysvětluje [Mass a ECS](mass-ecs.md#proc-objekty-zpomaluji-pamet-kterou-nactes-a-zahodis). Strop zlomů je navíc zároveň designové rozhodnutí. Přednášející říká, že se nastaví podle toho, kolik destrukce najednou je pro projekt rozumné.

**Souvislosti:** [Rejstřík: Geometry Collection](../rejstrik.md#geometry-collection) · [Rejstřík: ISM](../rejstrik.md#ism) · [Rejstřík: Data-oriented design](../rejstrik.md#data-oriented-design) · [Optimalizační průchod: Chaos Visual Debugger](gpu-pruchod.md#chaos-visual-debugger-rentgen-fyziky) *(jak kolizní geometrie vypadá v reálné hře)*

---

## Rozbití v multiplayeru: predictive interpolation místo predikce

**Zdroj:** [Using Chaos Physics for Large-Scale and High-Fidelity Scenes | Unreal Fest 2024](https://www.youtube.com/watch?v=uCYGFdEWyZw) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~51 min, přednáška (vedoucí fyzikální programátor Epicu; UE 5.4) ·
[A Dive Into Networked Physics-Based Character Movement | Unreal Fest Stockholm 2025](https://www.youtube.com/watch?v=_jRLlTDqoGI) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~41 min, přednáška (fyzikální tým Epicu; úsek o plánech)

**Shrnutí:** Destrukce v LEGO Fortnite je serverově autoritativní. Lámat smí jen server; klient objekty simuluje, ale rozbije je, až když mu to server řekne. Při obyčejné replikaci by klient zlom propásl: předmět se odrazí od zdi a o chvíli později se zeď rozpadne. Predikce se může splést a dodatečná oprava nemá k čemu se vrátit, protože debris na serveru neexistuje. Řešením je predictive interpolation. Klient míří na stav zhruba o polovinu doby odezvy za serverem, takže zprávy o zlomech dorazí skoro načas. Háček: rozdíl se dorovnává rychlostí, ne přepsáním polohy, takže tvrdé skoky přijdou jen při velkém rozjetí.

### Rozpad myšlenky

**Problém.** Klient má simulaci, ale bez zlomů. Když se něco odrazí od rozbitného objektu dřív, než klient dostane zprávu o zlomu, uvidí odraz a teprve pak rozpad [(11:58)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=718s). Dodatečně opravit už postavený objekt by bylo velmi obtížné, a protože debris na serveru není, chybí cílový stav, ke kterému se vracet. Zbýval by rollback a resimulace. Predikce zlomů by problém neřešila, protože i ona se může splést a pak by se stejně muselo vracet [(12:44)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=764s).

**Mechanismus.** Klient cílí na stav, který je zhruba o polovinu doby odezvy za serverem. Zprávy o zlomech pak přicházejí přesně, nebo skoro přesně ve chvíli, kdy jsou potřeba [(12:44)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=764s). Dorovnání polohy probíhá ve čtyřech krocích [(13:31)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=811s), [(14:19)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=859s):
1. Rozdíl poloh se vydělí dobou odezvy. Vyjde rychlost, která by mezeru zavřela za jednu odezvu.
2. Přičte se k ní rozdíl rychlostí a vznikne cílová rychlost, se kterou by se klient srovnal naplno, a tedy tvrdě.
3. Cílová rychlost se zmenší, aby se k cíli blížil bez přestřelení.
4. Výsledek se přičte k současné rychlosti.

Mezi zprávami ze serveru se cíl extrapoluje po jeho rychlosti o krok fyziky a s další zprávou se nahradí [(15:05)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=905s). Protože se pracuje s rychlostmi a polohy se přímo nepřepisují, tvrdé skoky přijdou jen při velkém rozjetí. Rotace a úhlová rychlost se řeší stejně. Zapíná se v nastavení physics replication aktéra volbou Predictive Interpolation [(15:05)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=905s).

**Kam to míří.** O rok později fyzikální tým popisuje predictive interpolation jako levnější z obou režimů replikace. Běží v interpolované časové ose s trochou predikce kolem ní a používá ho LEGO Fortnite [(38:39)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=2319s). Plánem je replikační LOD: vzdálené objekty v predictive interpolation, a co se přiblíží k hráči, přejde do resimulace, aby s tím hráč mohl přímo interagovat. Přechod byl tehdy ještě experimentální [(39:25)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=2365s).

> **Pozn.:** Tohle je druhá polovina obrazu, jehož první polovinu najdeš v [síťové fyzice postav](mover.md#sitova-fyzika-zevnitr-snimky-misto-casu-resimulace-a-input-decay). Resimulace drží vlastní postavu a to, na co hráč sahá, ve stejné časové ose se serverem, za cenu rewindu a přehrávání. Predictive interpolation nechá svět mírně pozadu, a zato levně a bez rewindu. Který režim kde použít, rozhoduje vzdálenost od hráče a to, jestli s věcí přímo interaguje. A že síťová fyzika umí být zrádná i pro Epic, ukazuje [ragdoll v GASP](ragdoll.md#ragdoll-ktery-se-chrani-pozy-z-animace-sila-z-krivek-a-cas-do-dopadu), který se do sítě kvůli zpětné vazbě s korekcemi kapsle nedostal.

**Souvislosti:** [Rejstřík: Predictive interpolation](../rejstrik.md#predictive-interpolation) · [Rejstřík: Resimulation](../rejstrik.md#resimulation) · [Mover: dvě síťové větve](mover.md#proc-mover-existuje-modularita-vstupy-a-dve-sitove-vetve)

---

## Látka jako samostatný asset: Chaos Cloth přes Dataflow

**Zdroj:** [Using Chaos Physics for Large-Scale and High-Fidelity Scenes | Unreal Fest 2024](https://www.youtube.com/watch?v=uCYGFdEWyZw) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~51 min, přednáška (úsek o látkách; UE 5.4) ·
[Unreal Engine 5.8's NEW Cloth Physics System | Chaos Cloth Dataflow Tutorial](https://www.youtube.com/watch?v=6XDPQX-i0AQ) · [Pixelart Animation](https://www.youtube.com/channel/UCsuscoE2BG29RHfMYainuzw) · ~8 min, tutoriál (UE 5.8, díl 1)

**Shrnutí:** Dřív data látky bydlela ve skeletal meshi: v záložce jeho editoru a v jeho kreslení. Nová pipeline z nich dělá samostatný cloth asset, který vzniká v Dataflow grafu. Graf má tyto kroky:
- import, i ze static meshe nebo z Marvelous Designeru přes USD,
- přenos skin weights z postavy,
- namalované mapy (Max Distance, Backstop),
- konfigurace solveru,
- physics asset jako kolize.

Háček: protože je to nedestruktivní graf, jde z jednoho základního meshe vyrobit látku pro víc postav a nechat stroj vygenerovat simulační LODy. Ruční práce zůstane jen tam, kde je vidět.

### Rozpad myšlenky

**Proč samostatný asset.** Epic stavěl pipeline pro demo Talisman (GDC 2024), kde nosí MetaHuman velmi kvalitní simulované oblečení v UEFN [(15:05)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=905s), [(15:52)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=952s). Do té doby musela data látky žít ve skeletal meshi. Teď mají skeletal mesh i clothing komponenta společného předka, Skinned Mesh Component, takže se sdílí jen to, co dává smysl, a nové funkce pro látky nesahají do skeletal meshů [(16:38)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=998s).

**Graf.** Na vstupu mohou být i static meshe, skeletal meshe už nejsou podmínkou [(18:57)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=1137s). Uzel Transfer Skin Weights dopočítá skinning z postavy, buď podle nejbližšího bodu, nebo inpaintingem. Jeden základní mesh tak může dostat skinning a látku pro celou řadu postav [(19:43)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=1183s). Namalované weight mapy pak jdou do dvou konfigurací:
- **Max Distance** určuje, které vrcholy simulují a jak daleko se smějí vzdálit od skinované polohy [(17:24)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=1044s).
- **Backstop** je levný test koulí pro každou částici, aby látka nepřelezla zpátky přes skinovaný povrch a nezapadla do těla [(20:30)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=1230s).

Každé nastavení solveru je v grafu uzel. Physics asset dodá kolize a koncový uzel všechno zapíše do cloth assetu.

**Nástroj.** Panel viewer ukazuje 2D střihy a dovoluje malovat na 3D mesh. Vedle je náhled s animací, simulačním meshem, statistikami a kolizními vrstvami [(17:24)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=1044s), [(18:11)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=1091s).

**Z DCC do hry.** Uzel pro import USD dovoluje převzít látku z Marvelous Designeru: parametry simulace se uloží s meshem a poslouží jako základ konfigurace v Unrealu. V 5.4 to bylo v betě [(21:16)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=1276s), [(22:03)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=1323s). Ve hře pak stačí Chaos Cloth komponenta, která ukazuje na cloth asset. Je-li jejím rodičem skeletal mesh, skinovaná část látky jde s jeho animací [(22:49)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=1369s).

**Rozpočty.** Kapitánova bunda v demu je simulovaná celá, s kinematickým colliderem těla pod ní [(23:35)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=1415s). Nejvyšší LOD má ručně laděný mesh i simulaci s cílem zhruba 30 aktualizací za sekundu, nižší LODy 40 až 60. Konfigurace se dají mít zvlášť pro cutscény a gameplay i pro jednotlivé platformy [(24:22)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=1462s). Uzel Remesh vyrobí méně detailní mesh podle cílového procenta vrcholů, pro render, pro simulaci nebo pro obojí. U kapitána byly LODy renderu ruční a simulační LODy generované [(25:09)](https://www.youtube.com/watch?v=uCYGFdEWyZw&t=1509s).

**Postup v 5.8.** Tutoriál ukazuje cestu se skeletal meshem:
1. Oblečení se v Mayi naváže na skelet MetaHumana a skin weights se zkopírují z těla na každý kus [(0:02)](https://www.youtube.com/watch?v=6XDPQX-i0AQ&t=2s), [(0:48)](https://www.youtube.com/watch?v=6XDPQX-i0AQ&t=48s).
2. Každý kus se vyexportuje i s kostrou [(1:28)](https://www.youtube.com/watch?v=6XDPQX-i0AQ&t=88s) a importuje jako skeletal mesh s geometrií a skin weights, bez animací [(2:17)](https://www.youtube.com/watch?v=6XDPQX-i0AQ&t=137s).
3. Cloth asset se založí s volbou Skeletal Mesh, čímž se otevře Dataflow graf s výchozími uzly. V uzlu Set Physics Asset se nastaví physics asset MetaHumana, aby látka věděla, o které tělo se opírá [(3:04)](https://www.youtube.com/watch?v=6XDPQX-i0AQ&t=184s).
4. Mapa Max Distance se maluje objemovým štětcem. Černá (0) je přišitá k tělu a nástrojem relax se hrany vyhladí do plynulého přechodu, což autor považuje za klíčové pro uvěřitelnou simulaci [(4:04)](https://www.youtube.com/watch?v=6XDPQX-i0AQ&t=244s), [(5:01)](https://www.youtube.com/watch?v=6XDPQX-i0AQ&t=301s).
5. V blueprintu postavy přibude pod tělo Chaos Cloth komponenta s override physics assetu [(5:47)](https://www.youtube.com/watch?v=6XDPQX-i0AQ&t=347s).
6. V sequenceru se k ní přidá stopa pro simulaci v editoru a látka se rozhýbe přímo ve viewportu [(6:32)](https://www.youtube.com/watch?v=6XDPQX-i0AQ&t=392s), [(7:20)](https://www.youtube.com/watch?v=6XDPQX-i0AQ&t=440s).

> **Pozn.:** Variantu se static meshem a přenosem skin weights přímo v grafu ukazuje už [Chaos Cloth v kapitole MetaHuman](metahuman.md#chaos-cloth-sukne-ktera-se-hybe) (5.6). Ke skin weights tedy vedou dvě cesty: v DCC nástroji, nebo uzlem v grafu. Tutoriál z 5.8 na začátku slibuje víc kusů oblečení najednou, ale ukáže jen bundu; ostatní vrstvy a vnitřní prolínání odkládá do druhého dílu [(7:20)](https://www.youtube.com/watch?v=6XDPQX-i0AQ&t=440s). Přednáška je z 5.4 a některé části pipeline v ní byly v betě. U čísel z dema platí, že jsou z prezentačního dema, ne z hry s davem postav.

**Souvislosti:** [Rejstřík: Chaos Cloth](../rejstrik.md#chaos-cloth) · [Rejstřík: Dataflow](../rejstrik.md#dataflow) · [Rejstřík: Physics Asset](../rejstrik.md#physics-asset) · [Rig, který se přenese: Dataflow přenos atributů](animace-nastroje.md#rig-ktery-se-prenese-controly-na-kuzi-moduly-a-tvary-bez-navratu-k-riggerovi) *(týž graf v riggingu)*
