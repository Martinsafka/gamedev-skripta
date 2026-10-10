# Breakdowny II: technika za vzhledem

Druhá řada rozborů velkých světů. [První](env-breakdowny.md) ukazovala, jak se světy staví z trim sheetů, instancí a vrstev špíny. Tahle se dívá na systémy, které za artisty dělají práci, kterou by ručně nezvládli: editor, ve kterém je i logika skládačka, spouštěče, které samy sypou prach a listí, a shadery, které předstírají celé místnosti. Všechny tři rozbory skládá tentýž kanál, hlavně z veřejných portfolií artistů, u Alan Wake 2 i z přednášky vývojáře; u 007 video zdroj enginové části neuvádí. Hry běží na vlastních enginech studií (Glacier, Northlight, Anvil), takže nejde o návody pro Unreal, ale o myšlenky, které se do něj dají přenést. Stavbu kitů a materiálů, na kterých tyhle světy stojí, rozebírají [Modulární kity](modularni-kity.md).

---

## 007 First Light: editor, ve kterém se všechno skládá z entit a nikdo nečeká

**Zdroj:** [How 007 First Light Is Built Inside the Editor](https://www.youtube.com/watch?v=T4JStuqxUPI) · [Next Level Game Art](https://www.youtube.com/channel/UCmPBLkozH1irLObN0Q3_aJw) · ~14 min, breakdown (Glacier Next, vlastní engine IO Interactive)

**Shrnutí:** IO Interactive staví 007 First Light ve vlastním enginu. Jeho filozofie je dát moc tvůrcům obsahu místo programátorů a nenechat je čekat. Všechno je entita, model, světlo i logický uzel. Entity se skládají do znovupoužitelných templatů a ty do vrstev scény (bricks), které se dají míchat a za běhu nahrávat. Hra se upravuje za běhu a nový build editoru přichází každých 15 až 30 minut. Háček: modularita tu nekončí u stěn. Skládačkou je i herní logika, takže artista postaví výbušný kanystr i s chováním a designér ho nasadí bez programátora.

### Rozpad myšlenky

**Iterace jako zásada.** Většina věcí jde upravit za hraní a změny se projeví okamžitě. Vývoj běží z jedné hlavní větve (trunk-based development), nový build vzniká zhruba po každých 10 až 15 odevzdáních. Nový editor tak přichází každých 15 až 30 minut, kdežto plný samostatný build trvá hodinu až hodinu a půl [(1:18)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=78s), [(2:04)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=124s).

**Entita, template, brick.** Entita je nejnižší úroveň: jeden model, jedno světlo nebo jeden logický uzel. Základní třída má jen asi 32 bajtů, takže se entity hodí i na věci, které nejsou vidět [(2:04)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=124s). Template je sbírka entit, která tvoří jeden znovupoužitelný asset, a jde upravit, aniž by se sahalo na zbytek hry. Brick je vrstva scény z templatů a entit: jedna nese jen geometrii místa, druhá gala večer, třetí Bondovu misi uvnitř galavečera. Vrstvy se míchají, takže gala jde vyměnit za jinou událost bez přestavby prostředí [(2:04)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=124s), [(2:52)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=172s). Velký level Hitmana, jako Bombaj, má přes dva miliony entit nahraných a simulovaných najednou. Úprava ale nestojí podle jejich počtu: editor spočítá graf závislostí a aktualizuje jen dotčené entity, obvykle pod 1 %. Pro 007 přibyly bloky jako v programovacím jazyce, tedy podmínky, řízení toku a iterátory, a zhruba 70 % entit je teď logika a jen 30 % modely a světla [(2:52)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=172s).

**Logika jako společný jazyk.** VFX artista a artista propů postavili template kanystru i s jeho logikou. Designérovi se líbil, navrhl jím naplnit kontejnery a dal ho do hry bez programátorů. Protože všechno interaguje, kanystr sám funguje s ostatními systémy [(3:38)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=218s). Level designer, AI programátor, environment artista i animátor používají tutéž uzlovou vrstvu, takže designér přečte, co postavil VFX artista, a příběhová sekvence může odpálit kanystr. Vývojáři ji popisují jako táborák, kolem kterého se týmy sejdou [(3:38)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=218s), [(4:25)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=265s).

**Editor zvlášť od hry.** Paměť a entity drží editor, ne hra. Když hra při úpravách spadne, nic se neztratí, stačí ji znovu spustit [(4:25)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=265s). Engine tvoří editor, runtime a resource server, takže umí hot reload a editor se připojí k několika běžícím hrám nebo konzolím najednou. Bricks jsou zároveň základ streamování: designéři je za běhu nahrávají a uvolňují z vizuálního skriptování [(4:25)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=265s), [(5:13)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=313s).

**Světlo.** Globální osvětlení je plně v reálném čase. Kombinuje screen-space průchod po pixelech se sondami ve stylu DDGI jako zálohou a softwarový ray tracing proti distance fields meshů [(6:46)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=406s), [(7:34)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=454s). Hardwarový ray tracing IO záměrně nepoužívá, aby jeden systém škáloval na všech platformách a artisti nechystali data pro dvě pipeline. Ve scéně galavečera je kolem 1 500 světel. Culling je zredukuje na 100 až 200 v záběru a pak ještě clustered lighting [(7:34)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=454s). Každé světlo má statickou stínovou mapu, pokud ji artista nevypne. Omezený počet dynamických stínů dostanou světla podle toho, kolik pixelů opravdu ovlivňují [(7:34)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=454s), [(8:21)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=501s).

**Smolder.** Nad objemovou mlhou ve froxelech a atmosférou je systém Smolder pro objemové efekty [(8:21)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=501s). Díky průhlednosti nezávislé na pořadí (order-independent transparency) se jeho objemy prolínají s průhlednými objekty i s jinou volumetrikou a částice z explozí se s nimi správně řadí. Osvětluje je každé světlo i globální osvětlení a vrhají stín [(9:08)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=548s). Měl to být jednorázový nástroj pro kouřovou pomůcku. Ve hře je jich nakonec přes 400 a jen úvodní cutscéna jich má kolem 30 [(9:08)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=548s). Billboardy se pořád hodí na vzdálené nebo velmi ostré efekty, objemy na všechno, čím může hráč projít [(9:56)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=596s).

**Houdini, i když ho engine moc neumí.** Integrace Houdini byla omezená, a tak tech artisti museli improvizovat [(0:04)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=4s), [(9:56)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=596s):
- karty mechu, které vertex shader škáluje podle vzdálenosti kamery a tím vyhladí přechod mezi LODy. Pivot škálování je uložený ve vertex color a rozmisťování volí co nejdelší karty, aby bylo co nejméně geometrie [(9:56)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=596s), [(10:43)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=643s),
- nástroj na decaly podél spline,
- destrukce s chováním na asset: monitor změní materiál a pustí efekt, stůl poskočí, drobnosti se roztříští a reaguje to i na srážky při přeskoku. Padající kusy jsou kvůli výkonu GPU částice [(11:04)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=664s),
- prostřelený barel s vodou: z děr teče a spustí se odpočet, dokud nevyteče [(11:50)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=710s).

**Co si vzít.** Modularita na všechno, nejen na stěny, a iterace, která nečeká [(12:41)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=761s). Takový engine nemáš, ale zpětnou vazbu si můžeš brát průběžně, ne až na konci. A když engine nástroj nemá, často se dá postavit nebo nafejkovat. I jednoduché nástroje se v portfoliu vyplatí a naučí věci, které se v komfortní zóně nenaučíš [(13:28)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=808s).

> **Pozn.:** Prostřelený barel má v knihovně indie protějšek: [barel, který teče](pasti-a-mechaniky.md#barel-ktery-tece-diry-jako-data-hladina-jako-jedno-cislo), postavený v Blueprintech. Oddělený proces editoru je proti Unrealu podstatný rozdíl. Play In Editor v UE běží ve stejném procesu jako editor, takže pád hry obvykle shodí i editor (to je naše poznámka, ne z videa). Scény s mnoha stínícími světly zlevňuje v Unrealu [MegaLights](../rejstrik.md#megalights), jinou cestou než cullingem: světla vzorkuje sdíleně. Video propaguje autorův kurz a partnerský web [(6:00)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=360s), [(11:50)](https://www.youtube.com/watch?v=T4JStuqxUPI&t=710s).

**Souvislosti:** [Rejstřík: Prefab](../rejstrik.md#prefab) · [Rejstřík: Trunk-based development](../rejstrik.md#trunk-based-development) · [Rejstřík: Hot reload](../rejstrik.md#hot-reload) · [Rejstřík: Order-independent transparency](../rejstrik.md#order-independent-transparency) · [Objemy přes EVDB](osvetleni.md#objemy-pres-evdb-mraky-a-mlha-jako-asset) *(volumetrika v UE)* · [MegaLights: rozpočet vzorků na pixel](megalights.md#rozpocet-vzorku-na-pixel-co-megalights-meni-a-co-za-to-platis) *(stovky světel v Unrealu)*

---

## Alan Wake 2: neviditelné systémy, které za artisty oživí les

**Zdroj:** [3 Invisible Systems Secretly Running Alan Wake 2](https://www.youtube.com/watch?v=zOlvns5pEZM) · [Next Level Game Art](https://www.youtube.com/channel/UCmPBLkozH1irLObN0Q3_aJw) · ~17 min, breakdown (engine Northlight, Remedy)

**Shrnutí:** Remedy v Alan Wake 2 nechává nudnou práci na systémech, které hráč nevidí:
- spouštěče na zemi samy podle povrchu sypou prach, listí a hmyz,
- stopy si pamatují, v čem hráč šlápl,
- vítr z jednoduchých „wind boxů" nad signed distance fields fouká jinak venku a jinak uvnitř, včetně auta.

Vegetaci rozpohybuje skinning na GPU s téměř 300 000 kostmi za snímek a hustou geometrii utáhne culling po meshletech. Háček: autor z toho nevyvozuje „nauč se mesh shadery". Podle něj má technologie artistovi vzít nudných 90 % práce, aby se mohl věnovat 10 %, na kterých záleží.

### Rozpad myšlenky

**Kity a podklady pro outsourcing.** Prostředí stojí na modulárních kitech jako u většiny dnešních her [(1:38)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=98s). Část dodalo outsourcingové studio: fasády, zadní strany budov, celé budovy, schodiště i kit rozbitého autobusu. Jeden z artistů musel kvůli kitu studovat tesařské konstrukce, protože nikdo neumí každý architektonický styl [(2:25)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=145s). Pro externí partnery připravil podrobnou dokumentaci: od blockoutu přes herní rozměry (gameplay metrics) až po kit dřevěné konstrukce a nábytku. Kity chatek vznikly zvenku i zevnitř [(2:25)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=145s), [(3:11)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=191s).

**Spouštěče na zemi.** VFX artista postavil nástroj na velké spouštěče na zemi. Ty v čase vrhají paprsky, zjistí, kde je zem a z jakého physical materialu, a podle toho spawnují prach, listí, trávu, hmyz nebo písek. Emitory se natáčejí podle směru větru [(0:04)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=4s), [(3:11)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=191s), [(3:58)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=238s). Podobné spouštěče na obloze sypou listí, ptáky a za deště kapky. Nový systém větru s částicemi nefungoval, a tak artista udělal efekty s různými rychlostmi, které se natáčejí a hýbou podle síly a směru větru [(4:22)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=262s).

**Stopy, které si pamatují.** Systémy stop jsou dva. Jeden řeší, na co hráč šlápne, přes správce kontaktních materiálů. Druhý řeší, co si hráč nese na botách: kdo šlápne do bláta a vejde dovnitř, nechává ještě pár kroků blátivé stopy. Stejně fungují krvavé a mokré stopy a decaly se kombinují, takže vznikne krev v blátě nebo mokrá hlína [(4:22)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=262s), [(5:08)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=308s).

**Vítr z krabic.** Systém větru stojí na signed distance fields. Wind boxy jsou primitiva, která skládají plynulé pole síly větru, a designéři jimi snadno odliší vnitřek a venek s plynulým přechodem bez stavů [(0:51)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=51s), [(6:34)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=394s). V jedoucím autě je pohyblivý wind box, který říká, že uvnitř nefouká [(6:34)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=394s).

**Les na kostech.** Vegetace je skinovaná, a to celá na GPU. V oblasti Cauldron Lake se každý snímek zpracuje skoro 300 000 kostí [(7:22)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=442s). Systém je „řízený artisty": bone shadery mají API, do kterého artisti píšou vlastní kód. Rozhýbat jde cokoli, vegetaci, předměty na vodě nebo kabely ve větru, a vegetace má rigy jako postavy [(0:51)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=51s), [(8:09)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=489s).

**Meshlety.** Meshlety jsou nízkoúrovňové stavební bloky virtualizované geometrie. Nanite je úplný systém postavený nad stejnými principy [(8:09)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=489s). V Alan Wake 2 má meshlet 64 trojúhelníků a 64 vrcholů a nese obalovou kouli a kužel normál pro culling [(8:56)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=536s). U skinované vegetace se obaly přepočítávají compute shaderem; na Xbox Series X to trvá pod 0,2 ms pro koule a pod 0,3 ms pro kužely [(9:42)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=582s). Ukázková scéna má 200 000 instancí, 4 miliony meshletů a kolem 200 milionů trojúhelníků. Culling proto jde ve stupních [(10:30)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=630s), [(11:17)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=677s):
1. pohledový jehlan,
2. příspěvek, tedy vyřazení objektů malých na obrazovce,
3. okluze,
4. totéž po jednotlivých meshletech, včetně kuželů normál.

**Mlha a průhlednost.** Všudypřítomná mlha stojí na přestavbě průhlednosti. Průhlednost nezávislá na pořadí, založená na momentech (MBOIT), se kreslí ve třech rozlišeních, takže mlha, průhledná geometrie a efekty se plynule prolínají [(12:24)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=744s), [(13:10)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=790s). Přidává se osvětlení průhledných ploch po pixelech, odrazy ovlivněné mlhou a přibližný vícenásobný rozptyl světla v mlze, který zlepšuje atmosféru [(13:10)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=790s), [(13:56)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=836s).

**Pod kapotou.** Northlight během vývoje přešel na datově orientovaný systém herních objektů (ECS). Ten zrychlil i iteraci na nástěnce s důkazy [(13:56)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=836s). Ovládání postavy stojí na voxelech, aby se postavy v těsných prostorech nezasekávaly. Na PC je ray tracing přímého světla a path tracing nepřímého [(14:42)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=882s).

**Lekce.** Každý z těch systémů existuje proto, aby artistovi ulehčil práci. Díky meshletům se nemusí trápit polygony každého propu, spouštěče za něj rozmístí listí a vegetace na kostech se hýbe sama [(15:29)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=929s). Základy, tedy kity, set dressing a vyprávění prostředím, zůstávají artistovi [(16:15)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=975s).

> **Pozn.:** Stopy, které si nesou předchozí povrch, zná knihovna z UE jako [stopy v decalech](footsteps.md#stopy-jako-decaly-nosis-s-sebou-predchozi-povrch). Výběr částic podle physical materialu staví v UE i [kroky přes Niagara Data Channel](footsteps.md#niagara-data-channel-castice-kroku-bez-stovky-systemu), s mapou povrch → efekt v data assetu. Jak Nanite rozhoduje o ceně geometrie v UE, rozebírá [Nanite do hloubky](nanite-do-hloubky.md) a datově orientovaný přístup [Mass a ECS](mass-ecs.md#entita-neni-actor-rozkladej-podle-pristupu-do-pameti-ne-podle-postavy). Video propaguje autorův kurz a partnerský web [(5:47)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=347s), [(12:24)](https://www.youtube.com/watch?v=zOlvns5pEZM&t=744s).

**Souvislosti:** [Rejstřík: Meshlet](../rejstrik.md#meshlet) · [Rejstřík: Occlusion culling](../rejstrik.md#occlusion-culling) · [Rejstřík: Order-independent transparency](../rejstrik.md#order-independent-transparency) · [Rejstřík: Set dressing](../rejstrik.md#set-dressing) · [Rejstřík: Mesh distance field](../rejstrik.md#mesh-distance-field)

---

## AC Black Flag Resynced: prodat iluzi, ne postavit skutečnost

**Zdroj:** [Tricks Behind AC Black Flag Resynced's Materials and Tech](https://www.youtube.com/watch?v=MF_wkqanBFI) · [Next Level Game Art](https://www.youtube.com/channel/UCmPBLkozH1irLObN0Q3_aJw) · ~11 min, breakdown (engine Anvil, Ubisoft Singapore)

**Shrnutí:** Remake Black Flag z roku 2026 je přehled triků, jak dát velkému světu bohatost bez unikátních textur a modelů:
- páry materiálů navržené tak, aby se do sebe prolínaly vertex paintem,
- sdílená knihovna obecných materiálů s vrstvami poškození a špíny,
- trim sheety a mesh decaly na lodích,
- kamenné zdi vyskládané fyzikální simulací v Houdini,
- falešné interiéry za okny.

Háček je v posledním bodě. Místnost za sklem neexistuje: shader ji promítne z textury, dodá jí hloubku parallaxem a každému oknu náhodnou variantu. Protože zná denní dobu, v noci se „rozsvítí".

### Rozpad myšlenky

**Páry materiálů.** V Havaně se materiály prolínají vertex paintem. Místo ručně umísťovaných prasklin, skvrn a mechu artisti staví páry materiálů navržené tak, aby do sebe přecházely přímo na meshi [(0:49)](https://www.youtube.com/watch?v=MF_wkqanBFI&t=49s), [(1:36)](https://www.youtube.com/watch?v=MF_wkqanBFI&t=96s). Stěna tak není jedna textura kamene, ale dva nebo tři materiály namalované do vertex colors. Každá budova dostane přirozenou variaci bez vlastní textury, a proto nic nevypadá zkopírovaně [(1:48)](https://www.youtube.com/watch?v=MF_wkqanBFI&t=108s). Na katedrálách se totéž dotahuje dál, protože po nich hráč šplhá a prolínání musí obstát zblízka [(2:14)](https://www.youtube.com/watch?v=MF_wkqanBFI&t=134s).

**Pevnosti a obecné materiály.** U pevností bylo zadání výslovné: mají působit pevněji a hrozivěji, jako by vydržely boční salvu. Těžší kámen, hlubší zvětrání a pocit hmoty ukazují, že remaster není jen vyšší rozlišení textur, ale nový výklad místa [(2:39)](https://www.youtube.com/watch?v=MF_wkqanBFI&t=159s). Pod tím vším leží obecné materiály, které nikdo nezmíní. Každá stěna, střecha i ulička stojí na sdílené knihovně, převrstvené poškozením, špínou, zatékáním a posunem odstínu. Stejný základ se tak čte jako tucet různých povrchů. Že si toho nikdo nevšimne, je přesně smysl [(3:25)](https://www.youtube.com/watch?v=MF_wkqanBFI&t=205s).

**Lodě.** Trim sheety mají univerzální rozložení, takže jde měnit materiály bez přestavby UV [(3:25)](https://www.youtube.com/watch?v=MF_wkqanBFI&t=205s). Bitevní poškození není modelované zvlášť pro každou loď, ale tvoří ho mesh decaly zapečené do jednoho sdíleného atlasu. Trim má zapečená zkosení hran stejně jako v The Last of Us [(4:11)](https://www.youtube.com/watch?v=MF_wkqanBFI&t=251s).

**Zdi ze simulace.** Procedurální opakování přímo ze Substance Designeru bývá až příliš dokonalé a opakující se. Artisti proto postavili pipeline v Houdini [(4:58)](https://www.youtube.com/watch?v=MF_wkqanBFI&t=298s):
1. zdi se vygenerují procedurálně,
2. fyzikální simulace kameny poskládá, jako by je někdo vršil rukama,
3. finální textura vznikne v Substance Designeru.

Zeď je pak nepravidelná přesně tak, jako skutečná zeď z 18. století. Pod mnoha assety jsou ručně sochané tvary, ze kterých se pečou normal mapy na herní verze [(4:58)](https://www.youtube.com/watch?v=MF_wkqanBFI&t=298s), [(5:44)](https://www.youtube.com/watch?v=MF_wkqanBFI&t=344s).

**Falešný interiér.** Vymodelovat interiér za každým oknem v hustém městě by stálo nehorázně moc, tisíce místností, do kterých nikdo nevejde [(6:31)](https://www.youtube.com/watch?v=MF_wkqanBFI&t=391s). Shader proto pracuje se dvěma UV kanály. Jeden simuluje sklo s lomem a neprůhledný rám, druhý promítne za sklo plochou mapu interiéru, která vytvoří iluzi hloubky [(6:31)](https://www.youtube.com/watch?v=MF_wkqanBFI&t=391s), [(7:18)](https://www.youtube.com/watch?v=MF_wkqanBFI&t=438s). Navrch přidává:
- parallax occlusion mapping, takže se místnost při pohybu kolem posouvá,
- world position offset, který každému oknu náhodně změní uspořádání a jas místnosti, aby se okna neopakovala,
- podporu denní doby, takže v noci falešné interiéry svítí [(7:18)](https://www.youtube.com/watch?v=MF_wkqanBFI&t=438s).

Technika vznikla ze zkušeností z Assassin's Creed Shadows a používá se skoro ve všech oblastech mapy. Je to zlaté pravidlo herního renderingu: nemusíš postavit skutečnou věc, musíš prodat iluzi [(8:04)](https://www.youtube.com/watch?v=MF_wkqanBFI&t=484s).

**Vlny u břehu.** Vlny u pobřeží vznikly od nuly. Houdini vygeneroval jejich textury a ve hře k nim přibyly částice spršky a mlhy na hřebeni a částice nárazu do skal, mol a lodí [(8:51)](https://www.youtube.com/watch?v=MF_wkqanBFI&t=531s). Těžké bylo, že hráč může plavat skoro kdekoli podél pobřeží. Vlny proto musely obstát v reálném čase z úrovně hladiny, za každého počasí a v přísném výkonovém rozpočtu. Nejlíp vypadající efekt bývá ten, který prošel nejtvrdší optimalizací [(8:51)](https://www.youtube.com/watch?v=MF_wkqanBFI&t=531s), [(9:37)](https://www.youtube.com/watch?v=MF_wkqanBFI&t=577s).

> **Pozn.:** Podobnou iluzi staví i [Beauclair z Witcher 3](modularni-kity.md#beauclair-500-mb-textur-na-cele-mesto-orientacni-body-clony-a-jeden-shader-na-ctvrt), kde parallax shader v okleštěných interiérech předstírá obsah z pár ploch, a [Resident Evil Requiem](levely-a-streaming.md#jak-to-dela-resident-evil-requiem), kde jsou interiéry oken parallax textury. Vrstvy prolnuté vertex colorem staví v UE [Nanite displacement](materialy.md#nanite-displacement-relief-malovany-vertex-colorem). Všechno v rozboru pochází z veřejných portfolií artistů, ne z marketingu [(0:49)](https://www.youtube.com/watch?v=MF_wkqanBFI&t=49s), [(10:23)](https://www.youtube.com/watch?v=MF_wkqanBFI&t=623s). Video zároveň propaguje autorův kurz a partnerský web [(5:44)](https://www.youtube.com/watch?v=MF_wkqanBFI&t=344s), [(9:37)](https://www.youtube.com/watch?v=MF_wkqanBFI&t=577s).

**Souvislosti:** [Rejstřík: Interior mapping](../rejstrik.md#interior-mapping) · [Rejstřík: Vertex painting](../rejstrik.md#vertex-painting) · [Rejstřík: Trim sheet](../rejstrik.md#trim-sheet) · [Rejstřík: Parallax occlusion mapping](../rejstrik.md#parallax-occlusion-mapping) · [TLOU: trim sheet](env-breakdowny.md#tlou-trim-sheet-ktery-nahradil-tisice-bake) · [Falešné okno v UE](materialy.md#falesne-okno-interior-cubemap-a-mistnost-nafocena-v-enginu) *(interior cubemap krok za krokem)*
