# Paměť, reference a instancování

Věci, které nesouvisejí s tím, jak scéna vypadá, a přesto rozhodují o tom, jak běží: **co všechno tvoje blueprinty táhnou do paměti** a jak to odložit, dokud to není potřeba, **kolik draw callů vyrobí opakující se geometrie** a hrst zásahů, které se dají udělat za odpoledne. Kapitola je záměrně praktická — zdroje jsou krátké tutoriály, ne přednášky, a hodnota je v tom, že jsou to věci, které se dělají špatně skoro všude.

Paměťovou stranu GPU řeší [Paměť GPU](gpu-pamet.md); architektonický základ pro první myšlenku je v [Komunikaci Blueprintů](komunikace-blueprintu.md#interface-nebo-dispatcher-a-kolik-doopravdy-stoji-cast).

---

## Size Map v režimu paměti: co drží tvůj blueprint

**Zdroj:** [How To Optimise Memory Usage In Your Unreal Engine 5 Game](https://www.youtube.com/watch?v=JWDnTDi_aLY) · [Matt Aspland](https://www.youtube.com/channel/UC8_RNwftEO4isrX2LJowcpg) · ~10 min, tutoriál

**Shrnutí:** Autor vezme nejjednodušší možný blueprint — sběratelný předmět, který po stisku klávesy nastaví jednu proměnnou a zmizí — a ukáže, že zabírá **111 MB paměti**. Ne kvůli meshi ani texturám, ale protože **castuje na postavu hráče**. Po dvou úpravách je z toho 1,7 MB. Háček, kvůli kterému to není jen tutoriálový trik: **ten předmět je ve hře stokrát.**

### Rozpad myšlenky

**Nástroj a jeho méně známý režim** [(0:48)](https://www.youtube.com/watch?v=JWDnTDi_aLY&t=48s): pravý klik na asset → **Size Map**, a v pravém horním rohu přepnout *size to display* z **disk size** na **memory size**. Diskovou velikost zná víc lidí (řeší velikost instalace), paměťová řekne, co se s tím assetem načte do RAM.

Čtení je vizuální a rychlé: **největší modrý blok je tvůj problém.** V ukázce je to postava hráče, a důvod je jednoduchý — *„tenhle blueprint referencuje BP_ThirdPersonCharacter, a protože ho referencuje, drží ho v paměti."* Dá se do toho zoomovat dál (postava → skeletal mesh → textury), takže Size Map je zároveň mapa, kde se dá dál škrtat.

**Kde ta reference vzniká** [(3:11)](https://www.youtube.com/watch?v=JWDnTDi_aLY&t=191s): u dvou cast uzlů. A oprava má dvě různé podoby podle toho, **k čemu ten cast slouží**:

1. **Cast jako ověření identity** („je to hráč, co se mě dotkl?") → nahradit uzlem **`==` proti `Get Player Character`**. *„Dělá to úplně totéž jako cast, ale nespotřebovává tu paměť."*
2. **Cast jako cesta k funkci nebo proměnné** na postavě → **Blueprint Interface**. Autor postaví `BPI_PlayerCharacter` s funkcí `Set Has Item`, přidá ji do class settings postavy, implementuje ji tam — a předmět pak volá zprávu, aniž by třídu postavy znal.

**Jak si ověřit, že jsi to doopravdy vyčistil** [(3:11)](https://www.youtube.com/watch?v=JWDnTDi_aLY&t=191s) je nejlepší praktický zvyk z celého videa: **Window → Find Results** a vyhledat jméno té třídy. Postup je pak mechanický — proklikat každý nález a odstranit ho, dokud se nevypíše *no results found*. U velkého blueprintu je to jediná rozumná cesta, protože cast se dá schovat kdekoli.

**Výsledek**: **111 MB → 1,7 MB**, a to, co v Size Mapu zbylo, je jen cube mesh, standardní makra a materiál. *„1,7 MB je velmi, velmi dobré."*

**A rozšíření, které se hodí znát**: Size Map funguje i na **složce** a na **celém projektu**. U celého projektu to chvíli trvá, ale je to způsob, jak najít největší žrouty naráz — v jeho prázdném projektu vyhrály materiály postavy, u kterých je jediná páka snížit rozlišení textur.

> **Pozn.:** Tenhle nález se v knihovně už objevil z jiné strany — [kolik doopravdy stojí cast](komunikace-blueprintu.md#interface-nebo-dispatcher-a-kolik-doopravdy-stoji-cast) říká totéž jazykem architektury. Tady je hodnota v tom, že je to **měřicí postup, ne princip**: Size Map → memory size → největší blok → Find Results → nula. Takový postup se dá dát juniorovi a dá se z něj udělat kontrola před odevzdáním. Za pozornost stojí i to rozdělení oprav podle **účelu castu**, protože rada „nepoužívej casty" je jinak nepoužitelná — polovina castů jsou ověření identity, a ta se řeší jednodušeji než interfacem. Vlastní výhrada k tomu příkladu: **111 MB v prázdném projektu je nafouknuté číslo**, protože ta postava s sebou táhne kompletní ukázkový obsah. V reálném projektu bude cast na hráče dražší v tom, že s ním přijde **všechno, co postava referencuje** — což je hůř předvídatelné a spíš horší, ne lepší. Táž logika platí i o patro výš, u [řetězů referencí, které z hlavního menu načtou 2,5 GB balíčků](profiling.md#cisla-se-kterymi-se-da-srovnavat).

**Souvislosti:** [Komunikace Blueprintů: kolik stojí cast](komunikace-blueprintu.md#interface-nebo-dispatcher-a-kolik-doopravdy-stoji-cast) · [Soft reference: načti, až když to hra potřebuje](#soft-reference-nacti-az-kdyz-to-hra-potrebuje) · [Interakce bez Event Ticku: volání bez castů](interakce-bez-event-ticku.md#blueprint-interface-volani-bez-castu) · [Principy architektury: tři principy škálovatelnosti](principy-architektury.md#tri-principy-skalovatelnosti-separace-volne-vazby-data) · [Profiling: čísla, se kterými se dá srovnávat](profiling.md#cisla-se-kterymi-se-da-srovnavat) · [Rejstřík: Hard reference](../rejstrik.md#hard-reference) · [Rejstřík: Size Map](../rejstrik.md#size-map) · [Rejstřík: Blueprint Interface](../rejstrik.md#blueprint-interface)

---

## Soft reference: načti, až když to hra potřebuje

**Zdroj:** [Stop Overusing Hard References (Do This Instead)](https://www.youtube.com/watch?v=OpotdQGOAYE) · [Unreal University](https://www.youtube.com/channel/UCQv4mwerZLQVe3wPbsMc-qw) · ~8 min, tutoriál · + [5 Ways To Optimise Your Game In Unreal Engine](https://www.youtube.com/watch?v=UAVz7WTARIk) · [Unreal University](https://www.youtube.com/channel/UCQv4mwerZLQVe3wPbsMc-qw) · ~17 min, listicle (úsek o asynchronním načítání)

**Shrnutí:** Tvrdá reference říká enginu „tohle potřebuju vždycky" a engine poslechne: asset se načte s blueprintem, i když se nikdy nepoužije. **[Soft reference](../rejstrik.md#soft-reference)** drží jen cestu a nenačte nic, dokud si o to hra neřekne — v ukázce tím blueprint, který spouští jeden efekt, klesne z 24,5 MB na 99 KB. Cena je o krok víc práce (asset se musí asynchronně načíst) a jedna zrádnost: **v editoru to funguje i bez načtení, protože asset už v paměti je** — rozbije se to až po restartu.

### Rozpad myšlenky

**Co se děje** [(0:49)](https://www.youtube.com/watch?v=OpotdQGOAYE&t=49s): přetáhneš do levelu blueprint, který tvrdě referencuje deset věcí, a do paměti jde všech deset — ať je hráč použije, nebo ne. V ukázce stačí jeden Niagara systém spouštěný overlapem: **24,5 MB** v Size Mapu, celé za ten efekt [(1:36)](https://www.youtube.com/watch?v=OpotdQGOAYE&t=96s). Druhé video přidává druhou polovinu ceny [(5:28)](https://www.youtube.com/watch?v=UAVz7WTARIk&t=328s): těžký asset s tvrdou referencí se načítá **naráz v okamžiku spawnu**, a to je škubnutí, které hráč vidí. Asynchronní načtení proběhne na pozadí, takže když asset přijde na řadu, v paměti už je.

**Jak na to** [(3:08)](https://www.youtube.com/watch?v=OpotdQGOAYE&t=188s): proměnnou přepnout na *Soft Object Reference* (pro třídy *Soft Class Reference*). Pak vzorec, který se opakuje všude: **`Is Valid?`** — je-li asset načtený, použij ho; není-li, **`Async Load Asset`** a pokračuj až z pinu *Completed* [(3:53)](https://www.youtube.com/watch?v=OpotdQGOAYE&t=233s), [(4:42)](https://www.youtube.com/watch?v=OpotdQGOAYE&t=282s). Výsledek: tentýž blueprint, totéž chování, **99 KB** [(5:29)](https://www.youtube.com/watch?v=OpotdQGOAYE&t=329s). Druhé video dojde k podobnému číslu z jiné strany — spawner částic z 21,8 MB na 11,8 KB [(7:02)](https://www.youtube.com/watch?v=UAVz7WTARIk&t=422s). Načíst se dá i předem, třeba v `BeginPlay`, aby ve chvíli potřeby nic nečekalo [(10:09)](https://www.youtube.com/watch?v=UAVz7WTARIk&t=609s).

**Past, kvůli které se tahle myšlenka vyplatí znát** [(7:48)](https://www.youtube.com/watch?v=UAVz7WTARIk&t=468s): po přepnutí na soft referenci efekt v editoru dál funguje — protože ho editor má načtený odjinud. Po restartu editoru se **nespawne nic**. Kdo testuje jen v rozběhnutém editoru, odhalí chybějící načtení až u někoho jiného nebo v zabaleném buildu.

**Kdy ano a kdy ne** [(6:17)](https://www.youtube.com/watch?v=OpotdQGOAYE&t=377s) — autor to sám označuje za svůj názor: co je potřeba **vždy a hned** (postava, hlavní mesh, UI, které se ukáže okamžitě), může zůstat tvrdé. Co je potřeba **až při konkrétní akci** (zvednutí zbraně, vstup do oblasti), je kandidát na soft referenci [(7:03)](https://www.youtube.com/watch?v=OpotdQGOAYE&t=423s). Totéž platí o velikosti projektu: v malém se s tvrdými referencemi projde, v rostoucím se začnou sčítat. Kontrolní nástroj je stejný jako v [předchozí myšlence](#size-map-v-rezimu-pameti-co-drzi-tvuj-blueprint) — Size Map v režimu paměti.

> **Pozn.:** Soft reference se v knihovně dosud objevovala jen jako jedno slovo v seznamu léků na [tvrdé reference](../rejstrik.md#hard-reference); tady je postup i cena. Obě videa přiznávají, že to **není výměna bez nákladů** — složitost se přesouvá z paměti do toku programu, protože načtení je asynchronní a všechno, co na asset čeká, musí čekat taky. Proto je jejich pravidlo („vždy potřebné tvrdě, podmíněné měkce") lepší než obecné „používej soft reference": rozhoduje se podle toho, **kdy** je asset potřeba, ne jak je velký. Škubnutí při spawnu patří do stejné rodiny jako [jitter, při kterém nespadne ani jeden snímek](frame-pacing.md#jitter-nespadne-ani-jeden-snimek-a-presto-to-skube): práce, která se neměla dělat v tom snímku, kdy se dělala. A asynchronní načítání má v knihovně dva starší sourozence — [level streaming místo Open Level](levely-a-streaming.md#open-level-zamrzne-hru-streaming-ji-drzi-zivou) a [async ukládání](ukladani.md#save-system-ktery-prezije-druhy-projekt-struktury-interface-a-async).

**Souvislosti:** [Size Map v režimu paměti](#size-map-v-rezimu-pameti-co-drzi-tvuj-blueprint) · [Komunikace Blueprintů: kolik stojí cast](komunikace-blueprintu.md#interface-nebo-dispatcher-a-kolik-doopravdy-stoji-cast) · [Levely a streaming](levely-a-streaming.md#open-level-zamrzne-hru-streaming-ji-drzi-zivou) · [Potrubí snímku: jitter](frame-pacing.md#jitter-nespadne-ani-jeden-snimek-a-presto-to-skube) · [Rejstřík: Soft reference](../rejstrik.md#soft-reference) · [Rejstřík: Hard reference](../rejstrik.md#hard-reference) · [Rejstřík: Size Map](../rejstrik.md#size-map)

---

## ISM, HISM a merge: draw cally podle geometrie

**Zdroj:** [Optimization UE5 — The Power of Instanced Static Meshes with Efficient Materials](https://www.youtube.com/watch?v=S7lJnSeL41M) · [PolySphere 3D](https://www.youtube.com/channel/UCBlzcvb5sKveHZdTmOZNgnQ) · ~6 min, výklad · + [How to Quickly Optimize Your Scene in Unreal Engine 5 Using ISM/HISM](https://www.youtube.com/watch?v=lZegK5ussdU) · [Sergey Maryshev](https://www.youtube.com/channel/UCVAdTnZgQ40jpKzC0-_RPAQ) · ~3 min, výklad

**Shrnutí:** Dvě krátká videa o téže věci, a dohromady dávají to, co ani jedno samo: **instancování šetří draw cally jen tehdy, když je geometrie i materiál naprosto shodná** — a druhá polovina úspěchu je ve **materiálu**, protože variace se dělají v jednom materiálu, ne dvaceti. Háček, který obě videa říkají nahlas a stojí za zapamatování: **máš-li zapnutý Nanite, tohle nepotřebuješ.**

### Rozpad myšlenky

**Základ a jeho hranice** [(0:48)](https://www.youtube.com/watch?v=lZegK5ussdU&t=48s): jeden barel = jeden draw call, pět kopií = pět draw callů, pět instancí v ISM = **jeden**. A pořád se dá s každou instancí pracovat zvlášť. Pak přijde ta hranice, kterou si lidé pletou: **barel a bedna se nesloučí ani se stejným materiálem**, protože *„ISM funguje jen s objekty, které mají naprosto identickou geometrii."*

**Co dělat, když geometrie shodná není**: **Merge Actors** — vyrobí nový mesh se společným materiálem, takže se všechno vykreslí jedním callem. Poctivé zhodnocení: *„je to dost hrubá metoda, ale jsou-li objekty blízko sebe, může být velmi efektivní."* (A pozor na to, co k tomu dodává [kritika slučování](nanite-do-hloubky.md#spor-o-nanite-co-tvrdi-kritika-a-co-z-toho-plati): slučování v Unrealu slučuje i LOD logiku.)

**ISM proti HISM** je rozhodnutí o **rozložení v prostoru**:

| | pro co | proč |
|---|---|---|
| **ISM** | modulární stavba blízko sebe — stěny, podlahy, stropy | 100 segmentů stěny = jeden objekt |
| **HISM** | objekty rozeseté po velké ploše — stromy u ulice | **podporuje LODy**, takže se v dálce ubere i geometrie |

**A past, která z instancování udělá zhoršení** [(2:22)](https://www.youtube.com/watch?v=lZegK5ussdU&t=142s): sloučíš-li **všechny** stromy včetně těch za budovami, *„budou se pořád vykreslovat, i když je kamera nevidí."* Instance se totiž cullují jako jeden celek. U malého počtu je to jedno, u velkého ne — takže se musí **plánovat dopředu, co se s čím sloučí**.

**Tři cesty, jak instance vyrobit** [(0:48)](https://www.youtube.com/watch?v=S7lJnSeL41M&t=48s):

1. **Packed Level Actor** — vybrat aktéry, pravý klik → Level → Create Packed Level Actor.
2. **Harvest Instances** v modeling mode (XForm → *non-hierarchical ISM*, zapnout *single actor* a *include single instances*).
3. **Blueprint** — v construction scriptu pole transformů a uzel *Add Instances*.

**Druhá polovina, na které to stojí nebo padá** [(2:35)](https://www.youtube.com/watch?v=S7lJnSeL41M&t=155s): *„všechny instance musí mít shodné vlastnosti, včetně materiálů."* Takže má-li být scéna rozmanitá **a** instancovaná, musí variace vzniknout **v jednom materiálu**:

- **Náhodná variace z pozice instance** — uzly, které dávají číslo mezi 0 a 1, přivedené na *hue* posun. *„A nejlepší na tom je, že je to všechno tentýž materiál na jednom ISM, i když to vypadá tak různě."* Autor to rozvádí až na tři nezávislé náhodné hodnoty.
- **Per-instance custom data** — pole vstupů, které se dají nastavit **pro každou instanci zvlášť** (a je potřeba nastavit *Num Custom Data Floats*). Autor tím dělá variace okenních materiálů v městské scéně.

**A výhrada, která tuhle myšlenku zasazuje do doby** [(2:22)](https://www.youtube.com/watch?v=lZegK5ussdU&t=142s): *„máš-li na objektech zapnutý Nanite, není důvod ISM používat — Nanite má vlastní cullovací systém."* Druhé video k tomu přidává upozornění, které je věcné a ne úplně nezpochybnitelné: Nanite *„vyžaduje skutečně výkonnou a moderní grafickou kartu"* — jinak nepoběží dobře.

> **Pozn.:** Nejcennější je tady spojení dvou věcí, které se obvykle učí odděleně: **instancování je bezcenné bez materiálové disciplíny.** Kdo si sloučí dvě stě kamenů do ISM a pak jim dá dvacet materiálových instancí, aby nebyly stejné, si výhodu sám zruší — a je to táž věta jako [cena rozmanitosti u raster binů](rozpocet-snimku.md#view-modes-kde-se-ztraci-nez-otevres-profiler). Za pozornost stojí i to, jak **stará** tahle technika je a že je pořád aktuální: dokud existují platformy, kde se Nanite nedá zapnout, existují i dvě různé pipeline — a rozhodnutí mezi nimi se dělá jednou, na začátku, spolu s [volbou cílového framerate](rozpocet-snimku.md#prvnich-1666-ms-se-rozdava-v-cl1). Vlastní výhrada k té pasti se stromy: neřeší se jen plánováním, ale i **velikostí shluků** — deset HISM po padesáti stromech se culluje lépe než jeden po pěti stech, protože culling má co zahodit.

**Souvislosti:** [Optimalizace: proč jsou levely pomalé](optimalizace.md#proc-jsou-levely-pomale-od-instanci-po-data-layers) *(tatáž cesta o patro dál, po data layers)* · [Instanced Actors](instanced-actors.md#swap-podle-vzdalenosti-setup-pres-data-registry) · [Nanite do hloubky: cluster culling](nanite-do-hloubky.md#overdraw-se-autoruje-ne-opravuje) · [Materiály: master material](materialy.md#master-material-pet-textur-nema-mit-kazdy-mesh) · [Rejstřík: ISM](../rejstrik.md#ism) · [Rejstřík: Packed Level Actor](../rejstrik.md#packed-level-actor) · [Rejstřík: Per-instance custom data](../rejstrik.md#per-instance-custom-data) · [Rejstřík: Draw call](../rejstrik.md#draw-call) · [Bojovka: ISM, které ztratí culling](gpu-pruchod.md#bojovka-pro-desetilety-hardware-rozpocet-po-castech-a-co-se-v-nem-naslo) *(když instancování vyjde dráž)*

---

## Drobky: šest zásahů na jedno odpoledne

**Zdroj:** [Unreal Engine Performance Optimization Tips](https://www.youtube.com/watch?v=V8NnLnBQFIg) · [Unreal University](https://www.youtube.com/channel/UCQv4mwerZLQVe3wPbsMc-qw) · ~8 min · + [Triple Your FPS With These 5 Lighting Optimization Tips](https://www.youtube.com/watch?v=MLS96wgSMk4) · [MelvinTang Games](https://www.youtube.com/channel/UCoseMmvZqeCgrj4ZwKBHOAA) · ~7 min · + [Geometry Optimization In a Few Clicks](https://www.youtube.com/watch?v=h6uLdQmwc7c) · [Unreal ArchWizard](https://www.youtube.com/channel/UCyJRsafskBTJ4hw8GRFfVRg) · ~2 min · + [I Reduced My UE5 Game Size By 70%](https://www.youtube.com/watch?v=qlPqwTAmQ5E) · [Matt Aspland](https://www.youtube.com/channel/UC8_RNwftEO4isrX2LJowcpg) · short · + [5 Ways To Optimise Your Game In Unreal Engine](https://www.youtube.com/watch?v=UAVz7WTARIk) · [Unreal University](https://www.youtube.com/channel/UCQv4mwerZLQVe3wPbsMc-qw) · ~17 min (doplněk k texturám a nastavení)

**Shrnutí:** Čtyři krátká videa, ze kterých se dohromady dá vytáhnout šest zásahů, které se vejdou do odpoledne a nevyžadují měřicí aparát. Nejsou to velké myšlenky — je to seznam věcí, které se dělají špatně, protože je nikdo neřekl. Háček u dvou z nich: **jedna podmínka, kterou nesplníš, celý mechanismus tiše vypne.**

### Rozpad myšlenky

**1. Mip mapy potřebují mocninu dvou** [(3:39)](https://www.youtube.com/watch?v=V8NnLnBQFIg&t=219s) — a tohle je ta tichá podmínka, kterou se vyplatí znát: *„Unreal negeneruje mip mapu pro texturu, která nemá poměr v mocnině dvou."* Textura 512×1024 mipy dostane, textura 321×431 **nedostane žádné** — takže se pořád vzorkuje v plném rozlišení a všechny rady o mip biasu jsou u ní bez účinku. Praktický důsledek: rozměry textur nejsou estetická volba. A kde v textuře začít škrtat, ukáže Size Map postavy: v jiné ukázce Unreal University tvořily textury většinu ze 183 MB a největší položkou byla **normál mapa** (nese nejvíc detailu) — 21 MB ve 4K. `Maximum Texture Size` 2048 ji srazí na zhruba 5 MB a u modelu, který hráč nevidí zblízka, nepoznáš rozdíl ani při 512 [(1:35)](https://www.youtube.com/watch?v=UAVz7WTARIk&t=95s), [(3:08)](https://www.youtube.com/watch?v=UAVz7WTARIk&t=188s).

**2. AutoLOD v modeling mode** [(0:01)](https://www.youtube.com/watch?v=h6uLdQmwc7c&t=1s) je nejlepší poměr času k výsledku v celé kapitole. Modeling mode → **AutoLOD**, v *simplification* přepnout na **triangle count**, zadat cíl a rozlišení pečené textury. Autor tím udělá z **milionového** kamene z Megascans **pětitisícový** a z něj nový asset ve stejné složce. Výsledek na disku: **0,1 MB proti 10 MB** — a ze vzdálenosti, ze které se to v levelu vidí, není rozdíl poznat. (Vyžaduje zapnutý plugin *Modeling*.)

**3. Draw distance na světlech**, na které narazily obě lightingová videa nezávisle [(3:15)](https://www.youtube.com/watch?v=MLS96wgSMk4&t=195s): v sekci *Performance* na světle je **max draw distance** a **max distance fade range**. Za tou vzdáleností se světlo přestane vykreslovat úplně; fade range zajistí, že to hráč nechytí. Jedno světlo tím nezachráníš — smysl to dává **u stovky světel ve městě**. Táž rada je i v [průchodu Toma Loomana](gpu-pruchod.md#hodina-v-cizi-scene-co-se-najde-kdyz-se-hleda), včetně jeho výchozího čísla 750 pro fade.

**4. Mobilita světla jako první rozhodnutí** [(1:33)](https://www.youtube.com/watch?v=MLS96wgSMk4&t=93s): *movable* se počítá za běhu a je nejdražší — patří baterce, světlu na postavě nebo na autě. Všechno ostatní má být *static* nebo *stationary*. Zní to banálně a je to jedna z nejčastějších chyb v cizích scénách.

**5. MegaLights jako jedno zaškrtnutí** [(4:50)](https://www.youtube.com/watch?v=MLS96wgSMk4&t=290s). V hustě osvětlené městské scéně (mega pack, RTX 4080, cinematic scalability) autor naměřil **19–20 FPS**; po zapnutí MegaLights v post-process volume s nekonečným rozsahem **57–60 FPS**. Trojnásobek za jedno pole — s tím, že jde o funkci z 5.5, která [v knihovně už má svůj kontext](osvetleni.md#malovat-svetlem-scena-slozena-z-falesnych-svetel), a s výhradou z [průchodu ukázkovou scénou](gpu-pruchod.md#hodina-v-cizi-scene-co-se-najde-kdyz-se-hleda): mění, jak se čtou statistiky světel, takže se při měření občas hodí vypnout.

**6. Balíček o 70 % menší** [(0:02)](https://www.youtube.com/watch?v=qlPqwTAmQ5E&t=2s) — čtyři pole v nastavení packagingu: **create compressed cooked packages**, **cook only maps** se seznamem map, **exclude editor content when cooking** a seznam adresářů, které se nemají cookovat nikdy. Netýká se to výkonu, ale velikosti instalace, a je to jediné místo v kapitole, kde se dá čekat dvouciferné procento zdarma.

**Bonus, který nepatří k výkonu, ale k dobrým návykům** [(6:44)](https://www.youtube.com/watch?v=V8NnLnBQFIg&t=404s): **dej hráči nastavení kvality a rozlišení.** Autor to formuluje prostě — lidé mají různě silné počítače a mají mít možnost si to srovnat sami. Druhé video Unreal University ji ze svých pěti rad označuje za tu nejdůležitější, protože se týká každého hráče na slabším stroji [(14:06)](https://www.youtube.com/watch?v=UAVz7WTARIk&t=846s). Je to druhá strana [rozpočtu, který na PC ovládá hráč](rozpocet-snimku.md#rozpocet-je-penezenka-ne-cil).

> **Pozn.:** Z téhle sbírky je zdaleka nejcennější **položka o mipách**, protože je to **tichá podmínka**: nic se nerozbije, nic nevypíše varování, jen jeden optimalizační mechanismus u té textury neexistuje. Takových podmínek je v enginech víc (fallback mesh bez nastavených LODů, [device profil, který si engine sám nevybere](rozpocet-snimku.md#prvnich-1666-ms-se-rozdava-v-cl1)) a spojuje je jedna vlastnost: **selžou mlčky**. Vyplatí se je proto sbírat do kontrolního seznamu, ne se je snažit pamatovat. Ke zbytku patří jedna společná výhrada: tři ze čtyř zdrojů slibují v titulku zdvojnásobení nebo ztrojnásobení FPS, a to číslo je vždycky z **jedné konkrétní scény, kde byla ta jedna věc extrémně špatně**. Ve scéně, kde světla nejsou úzké hrdlo, ti MegaLights nedají nic — takže i tady platí, že se nejdřív [měří](profiling.md#rozhodovaci-strom-stat-unit-rekne-kterym-nastrojem-pokracovat).

**Souvislosti:** [Textury a DLSS: right-size](textury-a-dlss.md#right-size-ne-vsechno-si-zaslouzi-4k) · [Osvětlení: malovat světlem](osvetleni.md#malovat-svetlem-scena-slozena-z-falesnych-svetel) · [Optimalizační průchod](gpu-pruchod.md#hodina-v-cizi-scene-co-se-najde-kdyz-se-hleda) · [Karta selhání: packaging](../zapisky/karta-selhani-packaging.md) · [Rejstřík: Mip mapa](../rejstrik.md#mip-mapa) · [Rejstřík: MegaLights](../rejstrik.md#megalights) · [Rejstřík: Cook](../rejstrik.md#cook)
