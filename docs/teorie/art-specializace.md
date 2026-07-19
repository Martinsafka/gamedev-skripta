# Art, který se hýbe: tech art, animace, VFX a UI

Druhá polovina Riotí série „So You Wanna Make Games??" popisuje čtyři řemesla, která mají společné to, že jejich výsledek **nejde posoudit na statickém obrázku**: technický art (bez něj se model nepohne), animace, vizuální efekty a uživatelské rozhraní. Pro sólo vývojáře jsou to zároveň čtyři nejčastěji podceňované položky rozpočtu — protože je nevidíš, dokud nechybí.

Předchozí řemesla — principy artu, concept, postavy, prostředí — jsou v [pipeline kapitole](art-pipeline.md).

---

## Tech art: most mezi artem a kódem

**Zdroj:** [So You Wanna Make Games?? | Episode 5: Technical Art](https://www.youtube.com/watch?v=kr7XYXMM7-U) · [Riot Games](https://www.youtube.com/channel/UCJEGvSZnQ1pkVfHO8s5G8hA) · ~13 min

**Shrnutí:** Technický artista je člověk, který umí obojí — art i kód — a jeho jediná definice zní: **optimalizovat způsob, jakým art vzniká a dostává se do hry.** Prakticky to znamená čtyři světy: rozhýbat modely (rigging), stavět nástroje pro ostatní artisty, držet pořádek v souborech a verzování, a psát shadery a simulace. Pro sólo vývojáře je to zpráva nepříjemná i užitečná: tuhle roli děláš taky, i když jsi o ní nevěděl.

### Rozpad myšlenky

Video otevírá výčtem, který má být vtipný a je hlavně přesný [(0:52)](https://www.youtube.com/watch?v=kr7XYXMM7-U&t=52s): nástroje pro artisty, optimalizace tvorby, export, implementace, příprava postav pro animaci, struktura souborů, podpora verzování, automatizace — a k tomu modelování, animace, efekty, rozhraní, shadery a světla. Když se moderátor brání („to je moc na jednu práci"), přijde ta definice: **náš úkol je optimalizovat, jak art vzniká a jak se dostane do hry**. Doprovodná poznámka je pro čtenáře, který přemýšlí o kariéře, možná nejcennější věta dílu [(0:52)](https://www.youtube.com/watch?v=kr7XYXMM7-U&t=52s): **všechny týmy, ve kterých autor byl, chtěly najmout víc tech artistů.**

**Rigging** [(1:38)](https://www.youtube.com/watch?v=kr7XYXMM7-U&t=98s) řeší problém, který si nikdo neuvědomí, dokud ho nepotká: model od character artisty je zamrzlý v pozici, ve které vznikl — **„vypadá jako socha"**. Tech artista do něj vloží kostru, pak **maluje váhy** jednotlivých kostí [(2:26)](https://www.youtube.com/watch?v=kr7XYXMM7-U&t=146s), tedy určuje, kolik které kosti patří která část meshe. Video zdůrazňuje, že to **není mechanická práce, ale docela umělecká** — cílem je deformace, která vypadá přirozeně, ne „divné výsledky". A protože kostí je moc a animátorovi by se s nimi pracovalo mizerně, staví se nad ně **ovladače** [(2:43)](https://www.youtube.com/watch?v=kr7XYXMM7-U&t=163s), které s nimi hýbou jednoduše a intuitivně — video pro ně používá obraz **provázků loutky v divadle**. Na téhle vrstvě se řeší i nenápadné problémy typu „udrž chodidlo na zemi, když se hýbe zbytek těla" — nebo naopak přepni chování tak, aby chodidlo tělo následovalo, jako při plavání.

**Nástroje a jedna otázka, která je řídí** [(3:30)](https://www.youtube.com/watch?v=kr7XYXMM7-U&t=210s). Artisté mají „velmi nuancované a excentrické požadavky" a tech artista je překládá do úprav softwaru. Klíčové je, že požadavek nebere doslova — **ptá se „co se vlastně snažíš udělat?"** [(3:30)](https://www.youtube.com/watch?v=kr7XYXMM7-U&t=210s). Příklad z videa to vysvětluje líp než definice [(4:16)](https://www.youtube.com/watch?v=kr7XYXMM7-U&t=256s): artista chce nástroj, který v levelu skryje vodu a rostliny — protože potřebuje spočítat ryby na mapě. Tech artista místo toho udělá nástroj, který **rovnou vypíše počet ryb**. Stejná logika stojí za redukcí kliků [(4:16)](https://www.youtube.com/watch?v=kr7XYXMM7-U&t=256s): implementace assetu má spoustu kroků a „jeden klik nezní jako moc, dokud nemusíš klikat na tentýž dialog celý den".

**Pořádek jako disciplína** [(5:03)](https://www.youtube.com/watch?v=kr7XYXMM7-U&t=303s): největší organizační problém je, že spoustu souborů edituje spousta lidí najednou. Verzovací systém drží historii a autory změn — a hlavně **řekne, jestli na tomtéž souboru někdo pracuje**. Tech artisti kolem něj staví nástroje, aby to artisty netrápilo. Podobně **pojmenovací konvence a struktura složek** [(6:36)](https://www.youtube.com/watch?v=kr7XYXMM7-U&t=396s): pojmenovat soubor je triviální, dokud jich nemáš **tisíce až statisíce**.

A **shadery jako kreativní nástroj**, ne jen materiálová kuchyně [(7:26)](https://www.youtube.com/watch?v=kr7XYXMM7-U&t=446s): navázání barvy vrcholů na výšku umožní **malovat terén extrémně rychle**, strmé části hory se můžou **automaticky proměnit v bahno nebo skálu**, a **zablokováním směru světla ve shaderu** vznikne kreslený vzhled ve stylu Breath of the Wild [(8:13)](https://www.youtube.com/watch?v=kr7XYXMM7-U&t=493s). Poslední doména jsou **simulace** [(9:02)](https://www.youtube.com/watch?v=kr7XYXMM7-U&t=542s): matematika pro chování látky, vlasů, vody, bahna či lávy.

> **Pozn.:** Rada „uč se principy programování, ne syntaxi jednoho jazyka" [(10:34)](https://www.youtube.com/watch?v=kr7XYXMM7-U&t=634s) je totéž, co říká [kolik kódu na start](co-se-ucit.md), jen z druhé strany profese. A přiznaná nejtěžší část práce — **neustálé přepínání kontextu** mezi animátorem, modelářem a inženýrem [(11:20)](https://www.youtube.com/watch?v=kr7XYXMM7-U&t=680s) — je přesně to, co sólo vývojář dělá každý den, aniž by to někdo nazval profesním rizikem.

**Souvislosti:** [Organizace projektu v UE](../praxe/organizace-projektu.md#content-browser-podle-epicu-feature-foldery-developers-a-redirectory) *(naming a struktura z praktické strany)* · [Materiály: master material](../praxe/materialy.md#master-material-pet-textur-nema-mit-kazdy-mesh) · [Toon shading v UE](../praxe/materialy.md#toon-shading-pasy-svetla-v-58) *(zablokované světlo v praxi)* · [Rejstřík: version control](../rejstrik.md#version-control) · [Rejstřík: rigging](../rejstrik.md#rigging)

---

## Animace: čitelnost, váha a osobnost

**Zdroj:** [So You Wanna Make Games?? | Episode 6: Character Animation](https://www.youtube.com/watch?v=VmNUAX2V8JQ) · [Riot Games](https://www.youtube.com/channel/UCJEGvSZnQ1pkVfHO8s5G8hA) · ~13 min

**Shrnutí:** Herní animace má tři cíle v přesném pořadí důležitosti: **jasně sdělit akci**, vytvořit **uvěřitelný pohyb** a teprve pak přidat **osobnost**. Řemeslně to stojí na dvou věcech, které se dají naučit bez talentu — čitelná linie pózy a správně rozložená váha — a na jednom návyku, který vypadá směšně a funguje: **zahraj si pohyb sám**.

### Rozpad myšlenky

Pořadí cílů není libovolné [(0:57)](https://www.youtube.com/watch?v=VmNUAX2V8JQ&t=57s). **Čitelnost akce** je první, protože animace ve hře nese herní informaci: úder je nejlepší příklad — **animace je to, co hráči oznamuje přicházející útok**, a bývá to jedna z nejdůležitějších informací v celém souboji [(1:44)](https://www.youtube.com/watch?v=VmNUAX2V8JQ&t=104s). **Uvěřitelnost** je druhá a nejde o realismus: ať je hra jakkoli stylizovaná, **konzistentní pohyb a fyzika umožňují hráči předvídat**, jak akce dopadnou. A protože pohyb nese i emoci, obří postava pohybující se s odpovídající vahou sděluje měřítko a budí strach [(2:31)](https://www.youtube.com/watch?v=VmNUAX2V8JQ&t=151s). **Osobnost** je třetí a video ji formuluje jako hereckou otázku [(2:31)](https://www.youtube.com/watch?v=VmNUAX2V8JQ&t=151s): nestačí „ať běží" — ptáš se, **jak by běžela právě tahle postava**.

Příprava má vlastní zvyk [(3:16)](https://www.youtube.com/watch?v=VmNUAX2V8JQ&t=196s): animátoři kreslí a hledají reference, ale nejlepší je **pohyb si vyzkoušet na vlastním těle** — „udělat ze sebe blázna" je nejrychlejší způsob, jak referenci získat. Video z toho dělá parodii na přírodopisný dokument, ve které se kolegové v kanceláři nahrávají na telefon, jak si zavazují botu nebo nacvičují smrtelnou animaci ve dvou [(4:04)](https://www.youtube.com/watch?v=VmNUAX2V8JQ&t=244s).

Řemeslné jádro jsou pózy [(4:54)](https://www.youtube.com/watch?v=VmNUAX2V8JQ&t=294s), protože animace je jejich série:

- **Line of action** [(4:54)](https://www.youtube.com/watch?v=VmNUAX2V8JQ&t=294s): pomyslná linie procházející pózou. Chceš ji **rovnou a čitelnou**, s částmi těla, které ji následují; **zlomená nebo komplikovaná linie ničí účel pózy** a pohyb se hůř čte.
- **Těžiště** [(5:47)](https://www.youtube.com/watch?v=VmNUAX2V8JQ&t=347s): musí padat nad chodidla — pokud zrovna nechceš ukázat, že postava dostala kopanec do hlavy. Póza současně sděluje **váhu předmětu**: čím blíž k těžišti ho postava drží, tím těžší působí — tentýž míč tak vypadá jako balonek, nebo jako bowlingová koule.
- **Osobnost přes adjektiva** [(6:33)](https://www.youtube.com/watch?v=VmNUAX2V8JQ&t=393s): postup, který jde okopírovat bez animátorského talentu. Vezmi adjektiva, která postavu popisují, a přelož je do těla — „těžký" znamená širší postoj a zvýrazněné svaly; „vzdorný a hrdý" znamená bradu nahoru a hruď vpřed; **urozený původ dodá šála zvednutá vánkem**. Video přitom přiznává, že první pokus přestřelili a museli couvnout.

Fyzika se pak dělá dvěma triky, které video ukazuje na skákajícím míči [(7:21)](https://www.youtube.com/watch?v=VmNUAX2V8JQ&t=441s): **easing** — rozestupy mezi pózami se u vrcholu zmenšují, protože gravitace zpomaluje pohyb, a rovnoměrné rozestupy proto vypadají mrtvě; a **squash & stretch** [(8:07)](https://www.youtube.com/watch?v=VmNUAX2V8JQ&t=487s) — protažení při rychlém pohybu dělá setrvačnost, stlačení při dopadu dělá náraz.

Poslední vrstva je systémová a bývá pro nováčky největší překvapení [(8:54)](https://www.youtube.com/watch?v=VmNUAX2V8JQ&t=534s): ve hře **nejde předvídat, která animace se kdy přehraje**, takže postava je kolekcí **stovek až tisíců animací, které se prolínají, přerušují a blendují**. Nástroj, kterým se to řídí, je **state machine** [(9:42)](https://www.youtube.com/watch?v=VmNUAX2V8JQ&t=582s): řeší přechody mezi chůzí, klusem a během podle rychlosti, změny míření podle myši, hledání úchytu při šplhání — a v Riotím výčtu i „zdvořilé zavření dveří před přestřelkou".

> **Pozn.:** Nejlepší rada dílu je proti intuici začátečníka [(11:17)](https://www.youtube.com/watch?v=VmNUAX2V8JQ&t=677s): autor chtěl animovat salta a útoky, aby ukázal, jak je dobrý, ale **„animování složitých pohybů se nerovná dobré animaci"**. Učitel mu místo toho zadal skákající míč — a pak **těžký míč, lehký míč, ohnivý míč, veselý míč, smutný míč**. Je to přesně tentýž princip jako [padesát návrhů jedné hole](art-pipeline.md#closing-doors-jak-iterovat-aniz-bys-chodil-dokola) u concept artu: variace na jednoduchém zadání odhalí slabiny rychleji než jeden ambiciózní kus.

**Souvislosti:** [AnimBP v UE: state machine a blend space](../praxe/animace-nastroje.md#animbp-od-nuly-state-machine-tridilny-skok-a-blend-space) *(tentýž nástroj v enginu)* · [Game feel: souboj a rytmus](game-feel.md#souboj-dela-zabavnym-pohyb-nepratel-ne-jejich-statistiky) · [Rejstřík: state machine](../rejstrik.md#state-machine) · [Rejstřík: squash & stretch](../rejstrik.md#squash-stretch) · [Rejstřík: line of action](../rejstrik.md#line-of-action)

---

## VFX: primární, sekundární, terciární — a rozpočet na okázalost

**Zdroj:** [So You Wanna Make Games?? | Episode 7: Game VFX](https://www.youtube.com/watch?v=3QKK2o5rWSQ) · [Riot Games](https://www.youtube.com/channel/UCJEGvSZnQ1pkVfHO8s5G8hA) · ~12 min

**Shrnutí:** Efekt se skládá ze tří vrstev podle pořadí, ve kterém je oko čte: **primární** (to hlavní, co přitáhne pohled), **sekundární** (detaily prodávající téma) a **terciární** (drobnosti, kterých musí být málo). A protože role VFX je sdělovat herní systém, platí tvrdý rozpočet na okázalost: **když je epický každý efekt, není epický žádný.**

### Rozpad myšlenky

Nejdřív omezení, které celé řemeslo tvaruje [(0:59)](https://www.youtube.com/watch?v=3QKK2o5rWSQ&t=59s): herní efekty běží **v reálném čase**, takže musí být řádově efektivnější než filmové, které se renderují dopředu. A hned poctivé přiznání [(0:59)](https://www.youtube.com/watch?v=3QKK2o5rWSQ&t=59s): **standardní postup neexistuje** — tentýž efekt jde udělat spritem otočeným ke kameře, meshem nebo trailem; „záleží na hotovém efektu, ne na cestě". Technický základ je **particle system** [(1:45)](https://www.youtube.com/watch?v=3QKK2o5rWSQ&t=105s): emitter je neviditelný bod, který vystřeluje sprity a modely, a jeho nastavení zvládne jak proud vody reagující na gravitaci, tak jeden nehybný obrázek.

Anatomii vrstev video ukazuje na ohnivé kouli [(2:31)](https://www.youtube.com/watch?v=3QKK2o5rWSQ&t=151s):

- **Primární** je hlava koule — první, co uvidíš, takže musí strhnout pozornost: zářivá textura nebo prvek otočený ke kameře, kolem toho půlkulový mesh s animovanou ohnivou texturou, která dodá dojem pohybu a intenzity.
- **Sekundární** jsou tematické detaily, které myšlenku ohně „prodávají" — pruh vycházející z vršku s texturou běžící po délce, tedy ohon [(3:18)](https://www.youtube.com/watch?v=3QKK2o5rWSQ&t=198s).
- **Terciární** jsou jiskry [(3:18)](https://www.youtube.com/watch?v=3QKK2o5rWSQ&t=198s) — a tady je pointa: jsou vizuálně nejméně důležité, takže **jich nesmí být moc, jinak ukradnou fokus a rozbijí čitelnost efektu**.

Z toho plyne hlavní disciplína oboru [(4:05)](https://www.youtube.com/watch?v=3QKK2o5rWSQ&t=245s): je svůdné udělat každý efekt velký a blyštivý, ale **úkolem VFX je sdělovat herní systém**, a to jde jen kontrastem. Nástroje, kterými se kontrast v efektech dělá:

- **Shape language** [(4:52)](https://www.youtube.com/watch?v=3QKK2o5rWSQ&t=292s), tedy standardizace tvarů pro významy napříč celou hrou. Ve hře se stovkami efektů je to nutnost: **plus znamená zdraví, kruh štít, špičaté tvary poškození**. A klíčová vlastnost — **když jsou barvy podobné, tvar je jediné, co efekty rozliší** [(5:39)](https://www.youtube.com/watch?v=3QKK2o5rWSQ&t=339s).
- **Barva** [(6:09)](https://www.youtube.com/watch?v=3QKK2o5rWSQ&t=369s), u které video přiznává, že často není zřejmá („jakou barvu má vítr?"). Slouží k rozlišení týmů (červené a zelené lasery ve Star Wars), typu poškození (živly v Magicka 2) i k emočnímu tónu (přesycený oheň v Mad Max). Praktický trik pro hry s mnoha efekty [(6:59)](https://www.youtube.com/watch?v=3QKK2o5rWSQ&t=419s): **barvu efektu drž analogickou k barvě postavy**, aby hráč okamžitě poznal, kdo kouzlí.
- **Timing** [(6:59)](https://www.youtube.com/watch?v=3QKK2o5rWSQ&t=419s): exploze je kruh rostoucí k maximu, ale **lineární růst je mrtvý**. Rytmus vzniká změnou rychlosti — prudký start a zpomalení u vrcholu — a přidat se dá i **před** výbuch, jako anticipace [(7:47)](https://www.youtube.com/watch?v=3QKK2o5rWSQ&t=467s).

Rada, kterou dostane každý, kdo se ptá, jak se rytmus efektů učí, je nečekaně fyzická [(9:21)](https://www.youtube.com/watch?v=3QKK2o5rWSQ&t=561s): **vezmi kámen, jdi k tichému jezeru a házej ho do vody** — ta vteřina, než něco dopadne a šplouchne, je podle autora „epický a fundamentální moment akce a rytmu, který se používá ve všech explozích".

> **Pozn.:** Obor nemá skoro žádné formální vzdělávání, a video to řeší otevřeně: **spoj se s komunitou** (fórum RealtimeVFX, Discord, Facebook) a prostuduj ručně kreslenou klasiku *Elemental Magic* od Josepha Gillanda [(10:07)](https://www.youtube.com/watch?v=3QKK2o5rWSQ&t=607s). Za zmínku stojí i historka, že autora na prvním pohovoru okamžitě odmítli a nechápal proč — v sérii, která je jinak náborovým materiálem velkého studia, je to nezvykle upřímné.

**Souvislosti:** [Game feel: katalog juice](game-feel.md#katalog-juice-deset-detailu-ktere-prodavaji-tutez-mechaniku) *(tytéž principy mimo částicové systémy)* · [Art pipeline: hierarchie kontrastem](art-pipeline.md#vizualni-hierarchie-fokus-vznika-ubranim-ne-pridanim) · [Praxe: VFX textury](../praxe/materialy.md#vfx-textury-nedelat-je-a-kdyz-uz-tak-v-krite) *(kde je vzít a čím je vyrobit)* · [Rejstřík: shape language](../rejstrik.md#shape-language) · [Rejstřík: particle system](../rejstrik.md#particle-system)

---

## UI a UX: ekosystém pravidel a pět cílů pohybu

**Zdroj:** [So You Wanna Make Games?? | Episode 9: User Interface Design](https://www.youtube.com/watch?v=sc3h5JXtIzw) · [Riot Games](https://www.youtube.com/channel/UCJEGvSZnQ1pkVfHO8s5G8hA) · ~12 min

**Shrnutí:** UX je **informační architektura** — kde informace bydlí a kolika kroky se k nim hráč dostane; UI je její vizuální provedení. Dobré rozhraní se přitom nedělá po obrazovkách, ale jako **ekosystém pravidel** (co znamená která barva, tvar a pozice) — a jeho pohyb má pět měřitelných cílů, ne „aby to bylo hezké".

### Rozpad myšlenky

Rozdíl obou zkratek [(1:03)](https://www.youtube.com/watch?v=sc3h5JXtIzw&t=63s): **UX** je celá informační architektura hry — kde jsou informace uložené a jak se k nim hráč dostane; **UI** jsou konkrétní vizuální prvky. V praxi jde **UX designér první**: stará se, aby hráč získal, co potřebuje, **s co nejmenším počtem nutných akcí**, a mapuje cestu, kterou hráč prochází. UI designér tu cestu bere a staví vizuál, ideálně tak, aby ji ještě zpřehlednil [(1:49)](https://www.youtube.com/watch?v=sc3h5JXtIzw&t=109s). U malých týmů je to jedna role — a právě proto se vyplatí ta dvě zadání držet oddělená v hlavě.

Základ řemesla je obecný **vizuální design**, jehož jádro video shrnuje jednou větou [(2:36)](https://www.youtube.com/watch?v=sc3h5JXtIzw&t=156s): **prezentovat komplexní informace tak jednoduše, aby jim publikum intuitivně rozumělo a mohlo podle nich jednat**. Z toho plyne, proč je nutné znát publikum [(2:36)](https://www.youtube.com/watch?v=sc3h5JXtIzw&t=156s): kde a jak bude rozhraní používat, jaké informace hledá a kdy. Rozdíl mezi PC, mobilem a konzolí mění všechno — video to ukazuje na dvou verzích téže hry [(3:22)](https://www.youtube.com/watch?v=sc3h5JXtIzw&t=202s). Objem UI navíc určuje žánr [(3:31)](https://www.youtube.com/watch?v=sc3h5JXtIzw&t=211s): karetní hra je **„z 90 % UI"**, strategie a simulace potřebují zpřístupnit hory dat, zatímco narativní hra si vystačí s minimem. A samotné UI je mnohem víc než HUD [(4:18)](https://www.youtube.com/watch?v=sc3h5JXtIzw&t=258s) — mapy, výběr postav, inventář, skill tree, questovní okna.

**Ekosystém místo obrazovek** [(4:18)](https://www.youtube.com/watch?v=sc3h5JXtIzw&t=258s) je hlavní teze dílu: „jsme zodpovědní za ekosystém celé hry", takže **musí existovat pravidla pro význam barev, textu a pozic** — a všechno ovlivňuje všechno. Riot to dokládá vlastním redesignem klienta [(5:04)](https://www.youtube.com/watch?v=sc3h5JXtIzw&t=304s): začali **definováním jádrové tematiky** a teprve z ní odvodili konkrétní pravidla pro typografii, ikonografii, barvu, tvarosloví a animaci.

**Layout** [(5:51)](https://www.youtube.com/watch?v=sc3h5JXtIzw&t=351s) je pak „puzzle", které rozhoduje o dvou věcech: co si hráč s čím spojí a jak rychle to přečte. Mozek dělá asociace podle **blízkosti** — pruh vedle jména nepřítele čteme jako jeho zdraví, počítadlo vedle pruhu jako postup k dalšímu levelu. Že rychlost není teoretická, dokládá vložený záběr turnajového komentáře [(6:37)](https://www.youtube.com/watch?v=sc3h5JXtIzw&t=397s), kde se kritické informace čtou v setinách.

Poslední vrstva je pohyb — **motion graphics** [(7:10)](https://www.youtube.com/watch?v=sc3h5JXtIzw&t=430s). Vztah k vizuálnímu designu je definovaný elegantně: **„vizuální design cílí na sdělení, kterému je jasně rozuměno; motion na sdělení, které je jasně cítit."** A hned s pojistkou proti záměně polish za design [(7:56)](https://www.youtube.com/watch?v=sc3h5JXtIzw&t=476s): **špatný design nevyleštíš do funkčnosti** — proces staví funkci a zážitek první, art je má doplňovat. Pohyb má proto **pět cílů** [(8:22)](https://www.youtube.com/watch?v=sc3h5JXtIzw&t=502s), které fungují jako checklist:

1. **Responsiveness** — interakce jsou rychlé, klikání působí plynule a bez námahy.
2. **Intention** — pohyb vede fokus ke klíčovým akcím a cestám.
3. **Awareness** — prvky reagují ze své pozice, takže je vidět, odkud co přišlo.
4. **Consistency** — stejné typy prvků sdílejí stejné pohybové vzorce, takže chování je předvídatelné.
5. **Physical intuition** — pohyb respektuje síly jako tření a měřítko a sedí ke značce hry; příkladem je kniha v Enter the Gungeon, kterou **otevírá kulka** [(9:09)](https://www.youtube.com/watch?v=sc3h5JXtIzw&t=549s).

> **Pozn.:** Nejlepší rada dílu míří na samouky, kteří „neumí UI" [(10:41)](https://www.youtube.com/watch?v=sc3h5JXtIzw&t=641s): jeden z autorů **vzal svoje oblíbené hry a překreslil jejich HUDy a menu** — nebylo to dokonalé, ale naučil se tím řemeslo, protože kopírování cizího řešení nutí pochopit jeho logiku. Rámuje to větou, kterou stojí za to si nechat: **rozdíl mezi tebou a lidmi, které obdivuješ, je čas a úsilí, ne magický talent** — a „skutečné umění je vědět, které chyby si nechat".

**Souvislosti:** [První dojem: menu, které žije](prvni-dojem.md#splash-prazdna-scena-a-menu-ktere-zije) · [První projekty: hra, která je jen interface](prvni-projekty.md#hra-ktera-je-jen-interface-virtualni-mazlicek) · [Typografie: pravidlo dvou fontů](typografie.md#pravidlo-dvou-fontu-a-vizualni-jazyk-textu) *(tatáž logika pravidel, aplikovaná na písmo)* · [Rejstřík: UX](../rejstrik.md#ux) · [Rejstřík: HUD](../rejstrik.md#hud)
