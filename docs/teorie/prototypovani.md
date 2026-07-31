# Prototypování a vertical slice

Mezi „mám nápad" a „dělám hru" leží dvě brány, které indie vývojáři rádi přeskakují — a průmysl ne: gameplay prototyp a vertical slice. Indie Game Clinic je vysvětluje na nejtěžším případu, jaký existuje: jak prototypovat city builder, jehož jádrem je komplexní ekonomika. A přidává metaforu pro všechno, co následuje po první bráně: vývoj jako spirála, po které se ke středu jede přes všechny části hry — ne rychlým pruhem té, která ti jde.

---

## Tři brány: gameplay prototyp → vertical slice → produkce

**Zdroj:** [Prototyping, Vertical Slices, and Planning a Complex Game](https://www.youtube.com/watch?v=atUsa3BE7t0) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · ~22 min, esej o procesu

**Shrnutí:** Průmyslový postup rané fáze vývoje má tvar trychtýře: **gameplay prototyp** ověří, že mechaniky fungují, **vertical slice** ověří, že z nich jde složit hra v cílové kvalitě, a teprve pak se otevírá **plná produkce** — sto levelů, dvacet nepřátel. Indie vývojáři často začnou „prostě stavět hru" a doufají — čímž největší sázku (měsíce výroby obsahu) uzavírají bez jediného testu.

### Rozpad myšlenky

**Gameplay prototyp** [(2:23)](https://www.youtube.com/watch?v=atUsa3BE7t0&t=143s) testuje interaktivní jádro a všechno, čím si nejsi jistý. Má být ošklivý [(4:36)](https://www.youtube.com/watch?v=atUsa3BE7t0&t=276s) — ze dvou důvodů: do hezkého se zamiluješ a přestaneš ho chtít měnit, a hráče krása oslepí [(5:25)](https://www.youtube.com/watch?v=atUsa3BE7t0&t=325s) — na mechaniku, kterou testuješ, pak nedostaneš férovou odpověď. Proto se jmenuje *gameplay* prototyp, ne prototyp hry [(5:39)](https://www.youtube.com/watch?v=atUsa3BE7t0&t=339s): art style (style guide / art bible), příběh a GDD se vyvíjejí paralelně jako samostatné úkoly.

**Vertical slice** [(0:50)](https://www.youtube.com/watch?v=atUsa3BE7t0&t=50s): výsek z časové osy hráčova zážitku — ne nutně začátek hry — v deklarované finální kvalitě [(1:11)](https://www.youtube.com/watch?v=atUsa3BE7t0&t=71s). Pět minut nebo hodina, podle žánru. Je to bod, kde se všechny paralelní linky poprvé potkají [(6:35)](https://www.youtube.com/watch?v=atUsa3BE7t0&t=395s): mechaniky z prototypu, art z bible, tón z příběhu. Otázka, na kterou odpovídá: když lidem ukážu reprezentativní půlhodinu [(6:48)](https://www.youtube.com/watch?v=atUsa3BE7t0&t=408s), nadchnou se? Teprve „ano" ospravedlňuje výrobu zbytku obsahu — všechno ostatní je hazard s měsíci práce.

> **Pozn.:** Pozor na terminologickou kolizi s [BiteMe přístupem](napad.md#prototyp-do-tydne-a-momentum-bar): tam prototyp *nemá* být šedý, protože testuje prodejnost a emoci. Rozpor je zdánlivý — jsou to dva různé testy. Ošklivý gameplay prototyp odpovídá na „funguje mechanika?", asset-packový vibe prototyp na „koupil by to někdo?". Průšvih je jen odpovídat si jedním testem na druhou otázku.

**Souvislosti:** [Vydání hry: vertikální a horizontální řez](vydani-hry.md#vertikalni-a-horizontalni-rez-jak-vybrat-co-do-dema-dat) *(co se z vertical slice stane, když ho ukazuješ zákazníkům)* · [Nápad: prototyp do týdne](napad.md#prototyp-do-tydne-a-momentum-bar) · [Postmortem ShantyTown: tři prototypy](postmortem-shantytown.md#vyber-projektu-tri-prototypy-tri-vahy) · [Zápisky: cut line](../zapisky/cut-line.md) *(slice přeložený do tvrdé definice na vlastním projektu)* · [Rejstřík: vertical slice](../rejstrik.md#vertical-slice) · [Hudba a zvuk: nástroje a game jam](../hudba/nastroje-zdarma-a-game-jam.md) *(vlastní hudba jako placeholder pro jam)*

---

## Standardy vs. inovace: co do slice patří

**Zdroj:** [Prototyping, Vertical Slices, and Planning a Complex Game](https://www.youtube.com/watch?v=atUsa3BE7t0) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · stejné video, jádro odpovědi

**Shrnutí:** Jak udělat vertical slice hry, kde „všechno souvisí se vším"? Rozděl každou plánovanou feature do dvou sloupců: **žánrové standardy** (co fanoušci žánru očekávají) a **inovace** (co máš jen ty). Slice stavěj zhruba ze 60 % standardů a 40 % inovací — protože slice pořád testuje *nápad*, a testovat jde jen to nové.

### Rozpad myšlenky

Dva sloupce [(9:14)](https://www.youtube.com/watch?v=atUsa3BE7t0&t=554s) na příkladu Frostpunku [(10:11)](https://www.youtube.com/watch?v=atUsa3BE7t0&t=611s): standardy — silnice, produkce surovin, zdraví kolonistů; inovace — teplo jako mechanická surovina s radiusem ohřívačů [(11:17)](https://www.youtube.com/watch?v=atUsa3BE7t0&t=677s), narativní výpravy. Extrémy selhávají v obou směrech: slice ze samých standardů netestuje nic — děláš „City Skylines, jen horší" [(12:37)](https://www.youtube.com/watch?v=atUsa3BE7t0&t=757s), a video je tu nemilosrdné: **hra bez jediné inovace nemá důvod vzniknout**. Obráceně slice ze samých inovací je nečitelný — hráč nemá za co uchopit žánr; přesně tím podle autora trpěl city builder The Hell [(21:27)](https://www.youtube.com/watch?v=atUsa3BE7t0&t=1287s): tolik novinek najednou, že nevěděl, co má dělat.

Poměr ~60/40 [(13:56)](https://www.youtube.com/watch?v=atUsa3BE7t0&t=836s) je vodítko, ne zákon. Dvě zpřesnění: **vynech, co je prokázané** — vodovodní systém city builderu [(14:27)](https://www.youtube.com/watch?v=atUsa3BE7t0&t=867s) funguje v deseti hrách před tebou, netestuje se a nikoho nenadchne; a **inovace ber z tématu** [(15:59)](https://www.youtube.com/watch?v=atUsa3BE7t0&t=959s) — Frostpunkovo teplo plyne ze steampunku v mrazu, mechaniky Pacific Drive z auta. Cvičení z videa: Prison Architect na Měsíci [(16:53)](https://www.youtube.com/watch?v=atUsa3BE7t0&t=1013s) — co nového z toho tématu *vyplývá* pro původní sadu mechanik? A poslední filtr je lidský: když inovacím z tvého slicu nikdo nefandí [(17:35)](https://www.youtube.com/watch?v=atUsa3BE7t0&t=1055s), vyměň je, dokud je to levné.

> **Pozn.:** Tohle je strukturovanější příbuzný [yoink & twist](napad.md#yoink-twist-lepsi-nebo-dost-jina): sloupec standardů = yoink, sloupec inovací = twist. A stejný test „vyplývá to z tématu?" používá ShantyTown ([účel jako soudce](postmortem-shantytown.md#hra-ti-rika-cim-chce-byt-ucel-jako-designovy-soudce)).

**Souvislosti:** [Nápad: yoink & twist](napad.md#yoink-twist-lepsi-nebo-dost-jina) · [Rejstřík: vertical slice](../rejstrik.md#vertical-slice) · [Rejstřík: hook](../rejstrik.md#hook)

---

## Ekonomiku si zahraj na papíře, než ji naprogramuješ

**Zdroj:** [Prototyping, Vertical Slices, and Planning a Complex Game](https://www.youtube.com/watch?v=atUsa3BE7t0) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · stejné video, závěr

**Shrnutí:** U systémových her (ekonomiky, strategie) existuje ještě levnější patro pod gameplay prototypem: balancovací spreadsheet, papírový prototyp, klidně desková verze hry. Ne proto, že je to rychlejší napsat — proto, že programátor a hráč jsou dva neslučitelné stavy mysli.

### Rozpad myšlenky

Video to pojmenovává přesně [(20:02)](https://www.youtube.com/watch?v=atUsa3BE7t0&t=1202s): když stavíš systém v enginu, přemýšlíš jako stavitel — struktura, závislosti, edge cases. Otázku „mám pět továren a tři farmy, co udělám *teď* a proč mě to baví?" si v tom stavu položit neumíš. Spreadsheet s čísly ekonomiky [(19:40)](https://www.youtube.com/watch?v=atUsa3BE7t0&t=1180s) nebo desková verze [(19:46)](https://www.youtube.com/watch?v=atUsa3BE7t0&t=1186s) tě přepnou do hráčské hlavy za odpoledne — a chyby balancu odhalené tam stojí guma a papír, ne refactoring.

Působí to jako ztráta času („vždyť se nedotýkám enginu!") a přesně proto se to přeskakuje — stejná psychologie jako u [world buildingu](produktivita.md#unik-k-snadne-tvorbe-world-building-a-dokonaly-toolset), jen obráceně: tady *užitečná* práce nevypadá jako práce.

**Souvislosti:** [Žrouti času](produktivita.md) · [Nápad: core DNA](napad.md#core-dna-a-ctyri-emoce) · [Markovovy řetězce: Monte Carlo](markovovy-retezce.md#monte-carlo-zahraj-to-tisickrat-misto-vypoctu) *(totéž s počítačem — balanc simulací)*

---

## Iterační spirála: ke středu nevede rychlý pruh

**Zdroj:** [GameDev as an Iterative Spiral](https://www.youtube.com/watch?v=9L6XX9kDQyA) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · ~12 min, metafora + vlastní projekt

**Shrnutí:** „Začít mechanikami, nebo tématem?" je špatná otázka — brilantní hry vznikly oběma cestami. Podstatné je, co následuje: ať začneš kdekoli, projdeš všemi ostatními částmi hry, a to opakovaně. Vývoj je spirála: ve středu leží dokonalá verze hry, která nikdy nemůže existovat, a blíž k ní se dostaneš jen tak, že objedeš celé kolo — art, kód, mechaniky, téma — znovu a znovu.

### Rozpad myšlenky

Kruh se dělí na části hry — poslouží [elemental tetrad](../rejstrik.md#elemental-tetrad) Jesseho Schella: estetika, mechaniky, technologie, příběh/téma [(0:48)](https://www.youtube.com/watch?v=9L6XX9kDQyA&t=48s). Ve středu spirály je platónský ideál tvé hry [(2:22)](https://www.youtube.com/watch?v=9L6XX9kDQyA&t=142s) — nedosažitelný („umění se nedokončuje, jen opouští"); každé kolo iterace tě přiblíží, a v nějakém bodě řekneš „to stačí" a vydáš [(3:09)](https://www.youtube.com/watch?v=9L6XX9kDQyA&t=189s). Proč spirála, a ne kruh: **na další patro se dostaneš jen objetím celého kola** [(3:09)](https://www.youtube.com/watch?v=9L6XX9kDQyA&t=189s).

Jak vypadá jedno kolo na jeho vlastním projektu (golem hra, viz [pivot](scope.md#pivot-kdyz-hra-nasla-jadro-jinde-nez-jsi-planoval)):

- **Technologie + art s nízkou laťkou, záměrně** [(3:56)](https://www.youtube.com/watch?v=9L6XX9kDQyA&t=236s): šablona projektu, 24×24px grid, sprity jedna barva + černá. „Vím, že umím lepší art — ale teď mě zajímá rychlá jízda po spirále." Nízké laťky v silných oblastech kupují rychlost iterace těm slabým.
- **Mechaniky**: room drafting z Blue Prince zkřížený s platformerem — protože v Terrarii ho baví *tvořit*, ale nebaví piplat jednotlivé bloky; drafting = tvoření v hrubých tazích [(4:42)](https://www.youtube.com/watch?v=9L6XX9kDQyA&t=282s).
- **Technologie podruhé**: fyzikální bugy + tisk před-renderovaných pokojů do mapy → knihovna z komunitního Discordu; chybějící zrcadlení pokojů → stal se testerem nové verze knihovny [(6:14)](https://www.youtube.com/watch?v=9L6XX9kDQyA&t=374s). (A překonaná „fobie z knihoven": nejde o pýchu, chce kódu rozumět.)
- **Téma**: proč postavený svět zase mizí? → efekt roztrhání levelu při teleportu domů — narativní ospravedlnění mechaniky, které si vyžádalo naučit se particle systém enginu [(7:48)](https://www.youtube.com/watch?v=9L6XX9kDQyA&t=468s).

Tři měsíce, asi pět kol [(8:34)](https://www.youtube.com/watch?v=9L6XX9kDQyA&t=514s) — a v každém kole se v každé oblasti něco nového naučil.

**Diagnóza her bez budoucnosti** [(8:34)](https://www.youtube.com/watch?v=9L6XX9kDQyA&t=514s): většina her, které autor recenzuje a „nemají budoucnost", vznikla opačně — autor má jednu dvě oblasti jako komfortní zónu a v té lajně se hrne ke středu: nádherné assety, které se nehýbou a mechaniky nechutnají; nebo skvělé mechaniky v nehratelně zabugované hře [(9:21)](https://www.youtube.com/watch?v=9L6XX9kDQyA&t=561s). Sólo vývojář je nejohroženější druh. Jenže dokonalá verze hry ve středu **není zabugovaná, má mechaniky, které sedí, téma, které dává smysl, a vypadá přitažlivě** — třeba minimalisticky, ale přitažlivě [(10:07)](https://www.youtube.com/watch?v=9L6XX9kDQyA&t=607s). Vlastní lajnou se k ní nepřiblížíš ani o milimetr.

Praktický korolár [(10:54)](https://www.youtube.com/watch?v=9L6XX9kDQyA&t=654s): máš-li oblast, které se bojíš a ignoruješ ji (placeholder assety, mdlé barvy), týden soustředěný jen na ni — art direction, paleta, shadery, ne „umět kreslit" — může hru posunout víc než měsíc v komfortní zóně. A tvrdý závěr [(11:40)](https://www.youtube.com/watch?v=9L6XX9kDQyA&t=700s): kdo se o některé části hry starat *nemíní* („bugy neřeším, víc neumím"), ať dělá jednodušší hru, která jeho dovednosti využije líp — aby hru chtěl někdo aspoň playtestovat, natož koupit, musí se jet po celé spirále.

> **Pozn.:** Tohle je jemnozrnný pohled dovnitř [tří bran](#tri-brany-gameplay-prototyp-vertical-slice-produkce): brány říkají, *kdy* smíš dál, spirála říká, *jak* se mezi nimi jede. A „komfortní lajna" je totéž, co [únik k snadné tvorbě](produktivita.md#unik-k-snadne-tvorbe-world-building-a-dokonaly-toolset) — jen viděná z ptačí perspektivy celého projektu.

**Souvislosti:** [Žrouti času: únik k snadné tvorbě](produktivita.md#unik-k-snadne-tvorbe-world-building-a-dokonaly-toolset) · [Sólo vývoj](solo-vyvoj.md) · [Scope: pivot](scope.md#pivot-kdyz-hra-nasla-jadro-jinde-nez-jsi-planoval) · [Rejstřík: elemental tetrad](../rejstrik.md#elemental-tetrad) · [Rejstřík: iterace](../rejstrik.md#iterace)

---

## Když GDD nestíhá: booleovské A/B a pilíře, které dovolí škrtat

**Zdroj:** [How This Game Dev Sold 1,000,000 Copies of His Game (In A WEEK)](https://www.youtube.com/watch?v=kodquYtxXd8) · [Thomas Brush](https://www.youtube.com/channel/UCuHVjteDW9tCb8QqMrtGvwQ) · ~77 min, rozhovor (spoluzakladatel Massive Monster)

**Shrnutí:** Na otázku *„naplánovali jste to v GDD?"* odpoví host *„proboha ne"* — a pak to celé hodinu zdůvodňuje způsobem, který není obhajobou chaosu. Jeho proces má dvě opory: **spor se neřeší diskuzí, ale tím, že se obě varianty naprogramují**, a **tři designové pilíře**, bez kterých by to celé neudrželo směr. Háček, který dělá rozdíl mezi tímhle a nekázní: **iterovat se dá jen tam, kde všichni vědí, kam se jde.**

### Rozpad myšlenky

**Proč u nich GDD nefungoval** [(25:45)](https://www.youtube.com/watch?v=kodquYtxXd8&t=1545s) — a je to konkrétní důvod, ne postoj: *„dělali jsme spoustu věcí, se kterými jsme se předtím nesetkali."* U metroidvanie se dá napsat dopředu, co bude, protože formát je známý. U hry, jejíž žánr ještě neexistoval, se nedalo. K tomu malý tým a takové tempo, že *„nápady byly zaříznuté dřív, než se o nich většina lidí dozvěděla."* Výslovně dodává, že proti GDD **nic nemá** a že pro vydavatele psali dokumenty kvůli financování.

**Co dělali místo toho: booleovské A/B** [(24:11)](https://www.youtube.com/watch?v=kodquYtxXd8&t=1451s). Když se přeli, jestli má sermon zvyšovat úroveň postavy, nebo dávat zlato, **udělali z toho boolean a zkusili obojí**. *„Došli jsme do bodu, kdy jsme si říkali: nemám čas ani energii se hádat. Dej to tam obojí a zkusíme to."* Z toho vznikla jejich formulace, která je celé myšlence jádrem: **„ať nám ta hra řekne, co chce být."**

**Dva nálezy, které přišly úplně na konci** a bez toho procesu by nevznikly:

- **Obětování stoupence zvedne úroveň postavy** [(22:37)](https://www.youtube.com/watch?v=kodquYtxXd8&t=1357s). Dřív dávalo zlato, jenže v pozdní hře už zlato nepotřebuješ, takže se oběť nevyplácela. Nová verze udělala něco jiného: **hráč to dělá pro vlastní prospěch** — a tím se stane spoluviníkem. *„Bylo to fantastické, když to šlo dovnitř."*
- **Sermony napojené na úrovně** — také až na konci, přestože je to celá smyčka hry.

**A ta podmínka, bez které je to jen chaos** [(29:36)](https://www.youtube.com/watch?v=kodquYtxXd8&t=1776s): **tři designové pilíře.** *„Každé rozhodnutí, které pak uděláš, musí posílit jeden nebo víc z nich. A když ne — i kdyby to byla skvělá funkce — musíš to vyhodit, protože to kalí vizi."* Zmiňuje, že tým God of War měl své tři pilíře vyvěšené v budově. Živá ukázka v rozhovoru: hostitel na místě zformuluje pilíře své hry jako **BioShock, ale Willy Wonka** · **gunplay jako Half-Life, ale měníš prostředí** · **příběh, který dojme** — a host to okamžitě otočí do praxe: *„nedáš tam piráty, protože nesedí do té Willy Wonka estetiky."*

**Vedlejší praxe, kterou stojí za to znát i s jejími náklady** [(30:23)](https://www.youtube.com/watch?v=kodquYtxXd8&t=1823s): *team sneaky boys* — když je něco potřeba a není to naplánované, **prostě to udělají a neřeknou o tom**. Logika je cynicky přesná: *„je víc práce to vyhodit, než to tam nechat."* Host to sám označí za *„velmi stresující pro všechny, kdo v tom týmu nejsou"* — zejména pro producenta.

**Vina za zahozenou práci** [(49:56)](https://www.youtube.com/watch?v=kodquYtxXd8&t=2996s) je v rozhovoru nejlidštější část: hostitel přiznává, že měsíc práce svého výtvarníka zahodil a týdny se z toho hryzal. Odpověď hosta je přirovnání k horolezci, který se probudí v ledovcové trhlině: *„musel jsem si vybrat doleva, nebo doprava — a nezáleželo na tom, jestli je to správně. Rozhodoval jsem se."* A rozvedení: **jednotlivé rozhodnutí obvykle není osudové, ale to, že někdo kormidluje, ano.** *„Lidi chtějí mít pocit, že tuhle loď někdo řídí."*

> **Pozn.:** Tenhle rozhovor by se dal snadno přečíst jako „GDD je zbytečný" — a to by byla špatná četba. Podstatné je, **co u nich tu funkci zastalo**: tři věty, které se vejdou na zeď, a pravidlo, že všechno ostatní se musí dát odvodit z nich. To je vlastně **komprimovaný GDD**, jen ve formě, kterou nikdo nemusí otevírat. Přesně to je i pointa [jedné stránky](gdd.md#jedna-stranka-format-rozhoduje-o-tom-jestli-to-nekdo-otevre): dokument, který se nečte, nefunguje; tři věty na zdi se čtou samy. Nejcennější přenositelná technika je ale **boolean místo hádky**: převádí názorový spor na měřitelný, a hlavně ho převádí na **něco levnějšího než diskuze** — což u malého týmu obvykle platí a u velkého ne. Vlastní výhrada k *team sneaky boys*: funguje to v týmu tří spoluzakladatelů se sdíleným podílem a **stejnou motivací**. V týmu se zaměstnanci a termíny je to tentýž postup s úplně jiným významem — obcházení plánování, ne iniciativa. Ta praxe se nedá odstřihnout od kontextu, ve kterém vznikla.

**Souvislosti:** [Iterační spirála](#iteracni-spirala-ke-stredu-nevede-rychly-pruh) · [Tři brány](#tri-brany-gameplay-prototyp-vertical-slice-produkce) · [GDD: jedna stránka](gdd.md#jedna-stranka-format-rozhoduje-o-tom-jestli-to-nekdo-otevre) · [Nápad: „X, ale Y"](napad.md#x-ale-y-hook-ktery-se-vejde-do-ctyr-slov) · [Rejstřík: Design pillars](../rejstrik.md#design-pillars) · [Rejstřík: A/B test](../rejstrik.md#ab-test)
