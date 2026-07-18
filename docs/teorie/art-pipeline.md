# Herní art: tři úkoly, pipeline a spolupráce

Riot Games natočil v roce 2018 desetidílnou sérii „So You Wanna Make Games??" — průvodce pro lidi, kteří umí kreslit a chtěli by dělat hry. Je to vzácný typ zdroje: profesionálové z velkého studia popisují **řemesla, ne nástroje**, takže drtivá většina obsahu platí dodnes a mimo Riot. Tahle kapitola bere první polovinu série — principy artu, concept art, character art a environment art — a přidává její poslední díl, který artistům vysvětluje design.

Zbylá řemesla (tech art, animace, VFX, UI) mají [vlastní kapitolu](art-specializace.md); díl o zvuku žije v [sound designu](../hudba/sound-design-ve-hre.md#tri-ukoly-herniho-zvuku).

---

## Art má tři úkoly: clarity, satisfaction, style

**Zdroj:** [So You Wanna Make Games?? | Episode 1: Intro to Game Art](https://www.youtube.com/watch?v=RqRoXLLwJ8g) · [Riot Games](https://www.youtube.com/channel/UCJEGvSZnQ1pkVfHO8s5G8hA) · ~11 min, úvod série

**Shrnutí:** Art ve hře není hezký obal kolem mechanik. Má tři konkrétní úkoly: **clarity** (hráč musí okamžitě vědět, co se děje), **satisfaction** (akce musí být responzivní a uspokojivé) a **style** (vizuál nese emoční tón a odlišuje jinak podobné hry). Tenhle trojlístek je současně zadání pro artistu a checklist pro kohokoli, kdo si art kupuje nebo objednává.

### Rozpad myšlenky

Definice na začátek [(1:39)](https://www.youtube.com/watch?v=RqRoXLLwJ8g&t=99s): art je **všechno, co ve hře vidíš a slyšíš** — postavy, nepřátelé, efekty, prostředí, UI, animace i zvuk. Z toho plyne, proč se role nedá odbýt estetikou: kdyby art dělal jen krásu, hra by bez něj byla ošklivá, ale hratelná. Takhle je bez něj nehratelná.

**Clarity** [(2:26)](https://www.youtube.com/watch?v=RqRoXLLwJ8g&t=146s) je informační úkol: kudy jít, kde jsem, kdo je spojenec a kdo nepřítel, kolik mi zbývá zdraví. Těžké to je proto, že hra sype kritické informace **v extrémně krátkém čase** — video si servíruje vlastní hru jako důkaz („byl jsi někdy v team fightu v League of Legends?"). **Satisfaction** [(3:00)](https://www.youtube.com/watch?v=RqRoXLLwJ8g&t=180s) je zpětnovazební úkol: okamžitá odezva na stisk tlačítka, dobrý pocit z úspěchu a nepříjemný ze selhání; nese ho hit pause, ceremonie po výhře, plynulé momentum i obyčejné skákání. **Style** [(3:46)](https://www.youtube.com/watch?v=RqRoXLLwJ8g&t=226s) je emoční úkol — a video ho dokládá nejlepším možným experimentem: PUBG a Fortnite mají **velmi podobný gameplay a úplně jiný pocit**. Fortnite má víc barev a přehnané proporce, takže působí odlehčeně; PUBG má tlumenou paletu, reálné zbraně a prostředí, takže působí vážně. Stejná pravidla, jiná emoce — rozdíl dělá výhradně art.

Hranice trojlístku je v tom, že se úkoly perou: maximální clarity vede k plochému čitelnému vizuálu bez atmosféry, maximální style k nádheře, ve které hráč nepozná nepřítele. Video na tenhle konflikt odpovídá pořadím — clarity a satisfaction jsou povinnosti, style je volba, která je má obsloužit, ne přebít.

> **Pozn.:** Trojice je podezřele blízká [třem úkolům herního zvuku](../hudba/sound-design-ve-hre.md#tri-ukoly-herniho-zvuku) (cues, feedback, emoce) z osmého dílu téže série — a to není náhoda: je to jeden studiový rámec aplikovaný na dva smysly. Kdo si ho osvojí, umí se u každého assetu zeptat „který ze tří úkolů tenhle kus plní?" — a poznat ten, který neplní žádný.

**Souvislosti:** [Základy: engagement a appeal](zaklady.md#engagement-drzi-hrace-ve-hre-appeal-ho-k-ni-privede) · [Game feel: katalog juice](game-feel.md#katalog-juice-deset-detailu-ktere-prodavaji-tutez-mechaniku) *(satisfaction rozepsaná do konkrétních triků)* · [Sound design: tři úkoly zvuku](../hudba/sound-design-ve-hre.md#tri-ukoly-herniho-zvuku) · [Rejstřík: game feel](../rejstrik.md#game-feel)

---

## Vizuální hierarchie: fokus vzniká ubráním, ne přidáním

**Zdroj:** [So You Wanna Make Games?? | Episode 1: Intro to Game Art](https://www.youtube.com/watch?v=RqRoXLLwJ8g) · [Riot Games](https://www.youtube.com/channel/UCJEGvSZnQ1pkVfHO8s5G8hA) · druhá půlka dílu

**Shrnutí:** Hra má tisíce kusů artu, které se navzájem perou o pozornost. Nástroj, kterým se to řeší, je **vizuální hierarchie**: nejdůležitější informace musí být nejsnáze vidět. A jediná páka, kterou se hierarchie dělá, je **kontrast** — v tvaru, velikosti, barvě, saturaci i míře detailu. Klíčový a kontraintuitivní důsledek: fokus se nevyrábí zvýrazněním jednoho místa, ale **potlačením všech ostatních**.

### Rozpad myšlenky

Video formuluje princip nezvykle radikálně [(4:33)](https://www.youtube.com/watch?v=RqRoXLLwJ8g&t=273s): „doslova všechno, co jako artisti děláme, se dá popsat jako práce s kontrastem" — a to platí i pro zvuk, hudbu a vyprávění. Ukázka je šachovnice [(5:20)](https://www.youtube.com/watch?v=RqRoXLLwJ8g&t=320s): každé pole je černé nebo bílé, kontrast je všude stejný, a proto oko nemá kde přistát. Chceš-li fokus na prostřední pole, **musíš snížit kontrast všech ostatních polí**. Tohle je nejcennější věta celé série pro sólo vývojáře: když ti scéna „nefunguje", odpověď málokdy zní přidej efekt — obvykle zní **ubeř všude jinde**.

Konkrétní páky, kterými se kontrast dělá:

- **Tvar a silueta** [(6:06)](https://www.youtube.com/watch?v=RqRoXLLwJ8g&t=366s): odlišné tvary tvoří body kontrastu a čitelné siluety; tvary navíc fungují jako **šipky** — ukazují, kam se dívat a co je nebezpečné.
- **Velikost** [(6:06)](https://www.youtube.com/watch?v=RqRoXLLwJ8g&t=366s): pouhou změnou velikosti sdělíš, který nepřítel je nejdůležitější.
- **Barva** [(6:53)](https://www.youtube.com/watch?v=RqRoXLLwJ8g&t=413s): ostrý barevný kontrast pro to, co se musí vidět — nepřátelé v Superhot, místa ke skoku v Mirror's Edge.
- **Detail** [(7:44)](https://www.youtube.com/watch?v=RqRoXLLwJ8g&t=464s) — a tenhle bod je nejméně samozřejmý. V době kopírování a vkládání je svůdné nacpat detail všude, jenže tím se hierarchie ničí. Střídání **klidných ploch a míst s vysokým detailem** je plnohodnotný kontrastní nástroj (Journey, INSIDE). Nefunguje to jen ve stylizovaných hrách: realistické tituly dělají totéž **atmosférickou perspektivou** — detail klesá se vzdáleností (Uncharted, God of War), což vede oko a vyrábí hloubku.

Praktický důsledek pro člověka, který art nedělá, ale nakupuje: asset pack sám o sobě žádnou hierarchii nemá. Když do scény nasypeš deset stejně detailních modelů, hráč nepozná, který z nich je interaktivní — a to není problém kvality assetů, ale chybějícího kontrastu.

> **Pozn.:** Tohle je výtvarná strana téhož jevu, který [vizuální komunikace](vizualni-komunikace.md#gestalt-a-vizualni-hierarchie-mozek-cte-cely-obraz) popisuje z psychologické strany (gestalt) — Riot ukazuje *páky*, Indie Game Clinic *proč na ně mozek reaguje*. A stejný princip v prostoru řeší [landmark napřed](prostor-a-hranice.md#jeskyne-ktera-se-hraje-landmark-napred-detail-nakonec): dominanta funguje jen tehdy, když okolí ustoupí.

**Souvislosti:** [Vizuální komunikace: gestalt](vizualni-komunikace.md#gestalt-a-vizualni-hierarchie-mozek-cte-cely-obraz) · [Prostor a hranice: landmark napřed](prostor-a-hranice.md#jeskyne-ktera-se-hraje-landmark-napred-detail-nakonec) · [Kamera: hranice, které umí lhát](kamera.md#kamera-metroidvanie-hranice-ktere-umi-lhat) · [Rejstřík: silueta](../rejstrik.md#silueta) · [Rejstřík: vizuální hierarchie](../rejstrik.md#vizualni-hierarchie)

---

## Concept artist řeší problémy, nekreslí obrázky

**Zdroj:** [So You Wanna Make Games?? | Episode 2: Concept Art](https://www.youtube.com/watch?v=FqX-UMVTLHI) · [Riot Games](https://www.youtube.com/channel/UCJEGvSZnQ1pkVfHO8s5G8hA) · ~13 min

**Shrnutí:** Concept art není disciplína krásných detailních maleb — je to **vizuální řešení problémů**, ve kterém jsou kresba a malba jen komunikačním nástrojem. Z toho plyne celý pracovní režim: napřed vědět, co řeším, pak si nastavit omezení, pak rešerše a moodboard, a teprve potom kreslit — rychle, volně a bez zamilovanosti do jednotlivých kusů.

### Rozpad myšlenky

Video otevírá parodií na představu „kresba tak nádherná, že otřese základy…" a hned ji utne [(0:02)](https://www.youtube.com/watch?v=FqX-UMVTLHI&t=2s): úkolem concept artisty je **pomáhat týmu řešit problémy návrhem vizuálních řešení**. Mnemotechnika, kterou k tomu dává, je „ABC — always be solving" [(1:12)](https://www.youtube.com/watch?v=FqX-UMVTLHI&t=72s): nakreslit něco cool nemusí tým posunout k jeho cílům.

**Omezení nejsou překážka, ale nástroj proti nekonečnému točení** [(1:59)](https://www.youtube.com/watch?v=FqX-UMVTLHI&t=119s). Video jmenuje tři zdroje: **tematická** omezení (lore, setting, tón — dubstepová zbraň je skvělá do Saints Row a nemožná jinde), **perspektiva** (návrh pro první osobu řeší jiné věci než pro třetí osobu nebo top-down) a — nejzajímavěji — **pravidla a mechaniky** [(2:45)](https://www.youtube.com/watch?v=FqX-UMVTLHI&t=165s). Když má schopnost přitáhnout nepřítele k sobě, je to concept artist, kdo vymýšlí, jak to vypadá; a i **počet životů postavy** je vstup do designu, protože křehká postava musí vypadat křehce.

Pak přijde krok, který nováčci vynechávají: **rešerše a moodboard před kreslením** [(2:45)](https://www.youtube.com/watch?v=FqX-UMVTLHI&t=165s). Děláš hru na horách? Sbírej fotky hor, klidně tam jeď. Důvod není inspirace, ale ekonomika [(3:33)](https://www.youtube.com/watch?v=FqX-UMVTLHI&t=213s): moodboard ti dá **zpětnou vazbu týmu s minimem odvedené práce** — je to gut-check směru dřív, než do něj investuješ týdny. Moodboard smí obsahovat i krátké deskriptory, kterým se říká **pillars**; a naopak **příliš obecný nebo roztříštěný moodboard vede ke zmatku a pivotům později**.

Samotné kreslení má dva návyky, které stojí za převzetí i mimo art:

- **Originalita jako cíl paralyzuje** [(4:19)](https://www.youtube.com/watch?v=FqX-UMVTLHI&t=259s). Honba za „něčím, co tu ještě nebylo" zastaví experimentování; místo toho zkoušej hodně věcí a **nebuď na svou práci navázaný**.
- **Drawing for ideation** [(4:19)](https://www.youtube.com/watch?v=FqX-UMVTLHI&t=259s): kresli rychle a volně. Pořád to vyžaduje silné základy, ale cílem není vyrenderovaný obraz — cílem je **dostat esenci nápadu před tým**, a k tomu často stačí skica. Živá ukázka to potvrzuje [(5:05)](https://www.youtube.com/watch?v=FqX-UMVTLHI&t=305s): zadání „čarodějova hůl s prastarým krystalem", pět artistů, každý jiným směrem — jeden staví tvary krystalů na bonbonech z dětství a vymyslí „candy-mancera".
- **Two-tone approach** [(6:42)](https://www.youtube.com/watch?v=FqX-UMVTLHI&t=402s): skicování jen ve dvou tónech. Není to estetická volba, ale **omezení, které ti zabrání utopit se v detailech** a drží pozornost na velkých grafických tvarech.

Proč tenhle režim vůbec existuje, shrnuje jedna věta [(6:42)](https://www.youtube.com/watch?v=FqX-UMVTLHI&t=402s): **concept artist jde v pipeline první, protože velké změny jsou v rychlých kresbách levné** — ve vyleštěném artu už ne. Pracovní předpoklad tedy zní: to, na čem právě dělám, se může kdykoli zásadně změnit.

> **Pozn.:** Vztah omezení a nápadu je tu obrácený stejně jako v [designu z omezení](scope.md#design-by-constraint-krabice-napred-napad-dovnitr): napřed krabice, pak obsah. A logika „levné změny první" je vizuální dvojče [tří bran prototypování](prototypovani.md#tri-brany-gameplay-prototyp-vertical-slice-produkce) — v obou případech se nejdřív ověřuje to, co jde ještě zahodit bez bolesti.

**Souvislosti:** [Scope: design by constraint](scope.md#design-by-constraint-krabice-napred-napad-dovnitr) · [Prototypování: tři brány](prototypovani.md#tri-brany-gameplay-prototyp-vertical-slice-produkce) · [GDD: pilíře a publikum](gdd.md#od-sirokeho-ke-konkretnimu-pilire-publikum-jadro) *(moodboard jako předstupeň art bible)* · [Rejstřík: moodboard](../rejstrik.md#moodboard) · [Rejstřík: art bible](../rejstrik.md#art-bible)

---

## Closing doors: jak iterovat, aniž bys chodil dokola

**Zdroj:** [So You Wanna Make Games?? | Episode 2: Concept Art](https://www.youtube.com/watch?v=FqX-UMVTLHI) · [Riot Games](https://www.youtube.com/channel/UCJEGvSZnQ1pkVfHO8s5G8hA) · druhá půlka dílu

**Shrnutí:** Iterace bez struktury se točí v kruhu: tým se vrací k zamítnutým nápadům, feedback je rozplizlý a nikdo neví, jestli se blížíme k rozhodnutí. Riot na to má postup **closing doors** — od širokého k úzkému, s pravidlem, že zavřené dveře se znovu neotevírají — a tři návyky kolem feedbacku, které fungují v jakékoli tvůrčí spolupráci, nejen v artu.

### Rozpad myšlenky

**Closing doors** [(7:28)](https://www.youtube.com/watch?v=FqX-UMVTLHI&t=448s) funguje takhle: předlož týmu **široký set nápadů**, v každém cyklu **zavři, co nefungovalo, a rozviň, co zaujalo**. Každá iterace je tím užší a přesnější. Celá metoda stojí a padá s jedním sebeovládáním, které video pojmenovává výslovně: **odolat nutkání otevírat zavřené dveře**. Bez toho pravidla je „iterace" jen procházení stejného prostoru dokola — a přesně tak vypadá projekt, který se každé tři měsíce potichu promění v jinou hru.

Feedback pak drží tři návyky:

- **Ptej se konkrétně a z perspektivy cíle** [(8:14)](https://www.youtube.com/watch?v=FqX-UMVTLHI&t=494s). Otázka „líbí se ti to?" vrátí názory na všechno možné. Otázka **„která z nich působí nejděsivěji?"** vrátí data k rozhodnutí, které právě děláš.
- **Žádná velká odhalení** [(8:14)](https://www.youtube.com/watch?v=FqX-UMVTLHI&t=494s). Ukazuj brzy a často: má-li se něco změnit, je to nejlevnější dnes.
- **Prezentuj práci, jako by ti na ní záleželo** [(8:14)](https://www.youtube.com/watch?v=FqX-UMVTLHI&t=494s). Concept artist je pro tým často zdroj nadšení — a video to demonstruje pasáží, kde autor s viditelnou radostí líčí Dariuse s motorovou sekerou a jetpackem. Sdělení je střízlivější, než se zdá: **stejná kresba prezentovaná unaveně a prezentovaná se zápalem nedostane stejnou zpětnou vazbu.**

A dvě rady z konce dílu, které míří přesně na samouka [(10:34)](https://www.youtube.com/watch?v=FqX-UMVTLHI&t=634s): **udělej list padesáti až sta variant jedné věci** (padesát holí — magická? steampunková? nekromantská?), protože kvantita učí rychleji než leštění jednoho kusu; a **abys mohl design posunout, musíš rozumět jeho historii** — než autor navrhl novou verzi postavy „blade dancer", musel nejdřív pochopit, co ten archetyp vůbec znamená. Poslední věta dílu je nejostřejší [(12:08)](https://www.youtube.com/watch?v=FqX-UMVTLHI&t=728s): **nejlepší práce míří na velmi konkrétní publikum** — nechceš, aby všem bylo „ok", chceš, aby tvoje cílovka explodovala nadšením, i za cenu, že si někdo jiný přijde s vidlemi.

> **Pozn.:** „Ptej se na cíl, ne na dojem" je tentýž sval jako [čti chování, ne slova](playtesting.md#moderovany-playtest-divej-se-co-delaji-ne-co-rikaji) v playtestu a [čti problém za návrhem](rady-z-praxe.md#kompilace-od-profiku-cti-problem-za-navrhem-ukazuj-brzy-ozen-se-s-hrou) v radách z praxe. Tři nezávislé zdroje, jedna dovednost: **překládat cizí reakce na rozhodnutí, které máš udělat.**

**Souvislosti:** [Playtesting: moderovaný test](playtesting.md#moderovany-playtest-divej-se-co-delaji-ne-co-rikaji) · [Rady z praxe: čti problém za návrhem](rady-z-praxe.md#kompilace-od-profiku-cti-problem-za-navrhem-ukazuj-brzy-ozen-se-s-hrou) · [Začátky: sdílení práce jako nástroj učení](zacatky-bez-zkusenosti.md#sdileni-prace-neni-marketing-je-to-nastroj-uceni) · [Rejstřík: closing doors](../rejstrik.md#closing-doors)

---

## Character art: od proxy k modelu, který jde animovat

**Zdroj:** [So You Wanna Make Games?? | Episode 3: Character Art](https://www.youtube.com/watch?v=PfpE5dNTWeI) · [Riot Games](https://www.youtube.com/channel/UCJEGvSZnQ1pkVfHO8s5G8hA) · ~12 min

**Shrnutí:** Postava se nevyrábí od detailu k celku, ale opačně: **proxy model** ověří proporce a siluetu ve hře, teprve pak přijde high-poly sochání, optimalizace a přenos detailů texturami. Nejtěžší disciplína přitom není software — je to **výběr ikonických prvků**, které postavu udrží čitelnou, i když je na obrazovce malá jako palec.

### Rozpad myšlenky

Zadání téhle role video formuluje nečekaně [(1:09)](https://www.youtube.com/watch?v=PfpE5dNTWeI&t=69s): nejtěžší je **zachytit fantazii postavy, i když je postava na obrazovce titěrná, vidíš ji jen shora, míhá se v pohybu — nebo z ní vidíš jenom ruce**. Odtud plyne technika ikonických prvků [(1:55)](https://www.youtube.com/watch?v=PfpE5dNTWeI&t=115s): u Garena z League of Legends jsou to **meč, nárameníky a šála**, a herní model je na tyhle tři věci zjednodušený, protože ve skutečné velikosti víc nepřečteš. Nebezpečí je dvojí a video ho pojmenovává férově: můžeš při zjednodušování **ztratit esenci**, nebo si **vybrat špatné prvky** — Garen zredukovaný na boty, ruce a vlasy je pořád zjednodušený, jen k nepoznání. Proto character artist pracuje těsně s concept artistou: concept je **cíl, na který se míří**, a v 3D se jeho ikonické kvality mají zachytit a **pokud možno ještě zesílit**.

Pipeline sama má jasnou logiku „nejdřív to, co se nejhůř opravuje":

1. **Proxy model** [(2:42)](https://www.youtube.com/watch?v=PfpE5dNTWeI&t=162s) — velké bloky tvarů a barev. Slouží ke kontrole **proporcí a siluety co nejdřív**, a hlavně se hodnotí **ve hře**, ne v modelovacím programu, protože teprve tam má postava svou skutečnou velikost.
2. **High-poly sculpt** [(3:29)](https://www.youtube.com/watch?v=PfpE5dNTWeI&t=209s) v sochacím programu typu ZBrush; video k tomu přidává upřímný vtip — záběry jsou zrychlené, a pak ukáže, jak sochání vypadá v reálném čase.
3. **Low-poly mesh** [(4:22)](https://www.youtube.com/watch?v=PfpE5dNTWeI&t=262s), protože engine počítá polygony v reálném čase a miliony jich neunese.
4. **UV mapa a bake** [(4:58)](https://www.youtube.com/watch?v=PfpE5dNTWeI&t=298s): rozbalení modelu do plochy — video používá obraz **složené krabice nebo oloupaného pomeranče** — a projekce detailů z high-poly na low-poly. Tím dostaneš detail bez polygonů.
5. **Textury nebo shadery** [(5:45)](https://www.youtube.com/watch?v=PfpE5dNTWeI&t=345s): shader je kus kódu diktující vzhled povrchu; táž textura zapojená do jiného kanálu dělá něco úplně jiného (šachovnice v barvě = vzor, v průhlednosti = díry). Materiál kamene vzniká složením tří map: **barva + normal mapa** (jak světlo reaguje na hrbolky) **+ height mapa** (jak moc části vystupují) [(7:22)](https://www.youtube.com/watch?v=PfpE5dNTWeI&t=442s).

Dvě hranice, které video přiznává. Za prvé: **software není ta těžká část — anatomie ano** [(8:08)](https://www.youtube.com/watch?v=PfpE5dNTWeI&t=488s). Bez znalosti kostí a svalů model vypadá divně **a špatně se animuje**. A anatomie není klec: teprve když jí rozumíš, můžeš pravidla ohýbat — příšera v LoL vznikla „frankensteinováním" lví tváře, medvědí pánve a šesti hmyzích končetin, a přesto působí jako **uvěřitelně živý tvor** [(8:54)](https://www.youtube.com/watch?v=PfpE5dNTWeI&t=534s). Za druhé: **co vypadá skvěle ve statické póze, může znemožnit animaci** [(9:40)](https://www.youtube.com/watch?v=PfpE5dNTWeI&t=580s) — límce, šály a brnění umí postavě zablokovat pohyb tak, že „nemůže zvednout ruce, aniž by se bodla do obličeje". Řeší se to zpětnou úpravou modelu ve spolupráci s tech artisty a animátory.

> **Pozn.:** „Hodnoť model ve hře, ne v editoru" je stejná disciplína jako [placeholder jako nástroj](game-feel.md#combat-je-rytmus-kazdy-utok-ma-ucel-a-placeholder-je-nastroj) — obojí brání zamilovat se do něčeho, co v kontextu hry nefunguje. A rada „rozsekej cíle na malé kousky, a když to není těžké, neučíš se" [(11:13)](https://www.youtube.com/watch?v=PfpE5dNTWeI&t=673s) je artistická verze [pomalého učení](uceni-v-ere-ai.md).

**Souvislosti:** [Materiály v UE: master material](../praxe/materialy.md#master-material-pet-textur-nema-mit-kazdy-mesh) *(kam tahle pipeline ústí v enginu)* · [Art specializace: tech art](art-specializace.md#tech-art-most-mezi-artem-a-kodem) · [Game feel: placeholder jako nástroj](game-feel.md#combat-je-rytmus-kazdy-utok-ma-ucel-a-placeholder-je-nastroj) · [Rejstřík: normal mapa](../rejstrik.md#normal-mapa) · [Rejstřík: retopologie](../rejstrik.md#retopologie)

---

## Prostředí je 90 % obrazovky — a musí mluvit

**Zdroj:** [So You Wanna Make Games?? | Episode 4: Environment Art](https://www.youtube.com/watch?v=37LVhP15zGw) · [Riot Games](https://www.youtube.com/channel/UCJEGvSZnQ1pkVfHO8s5G8hA) · ~13 min

**Shrnutí:** Prostředí zabírá zhruba **90 % obrazovky** — odečti ho a zbude prázdno s pár postavami a rozhraním. Ta plocha se ale nedá vyrobit kus po kuse: environment artist musí umět **stanovit priority** (a ty nevyplývají z artu, ale z designu), postavit svět z **modulárních dílů** a hlavně zařídit, aby prostředí bylo současně uvěřitelné **a čitelné jako gameplay informace**.

### Rozpad myšlenky

Vtipná pasáž na začátku [(0:48)](https://www.youtube.com/watch?v=37LVhP15zGw&t=48s) — „udělal tenhle strom, tamten strom, tenhle kámen, tuhle rostlinu…" — má vážnou pointu: objem práce je takový, že bez priorit se nedá pracovat. A priority nevymyslí artista sám: **vznikají ve spolupráci s game designéry a concept artisty** [(1:35)](https://www.youtube.com/watch?v=37LVhP15zGw&t=95s), protože otázka „který kámen je důležitější" má smysl jen ve vztahu k tomu, co má hráč v tom místě dělat.

Pipeline prostředí je proto sendvič mezi dvěma obory [(1:35)](https://www.youtube.com/watch?v=37LVhP15zGw&t=95s): concept artisti určí téma a tón → **designéři postaví greybox** (šedé bloky: kde jsou překážky, kudy se má jít, odkud přijdou nepřátelé) → environment artisti udělají první průchod, který **spojí vizi konceptu s omezeními designu** → následují modely, textury, barvy a **intenzivní testování ve hře se sběrem zpětné vazby** → teprve nakonec světlo a efekty [(2:22)](https://www.youtube.com/watch?v=37LVhP15zGw&t=142s).

Dvojí povaha prostředí — kulisa i informace — se ve videu vysvětluje gagem, ve kterém prvky mluví [(3:08)](https://www.youtube.com/watch?v=37LVhP15zGw&t=188s): „jsem skalní útes, ale všimni si těch lezeckých hran"; „jsem strašidelná chodba, střílej po téhle zrůdě"; „mám tu osvěžující vodu, tady jsi v bezpečí… nebo ne?!" Nástroje, kterými se to dělá:

- **Establishing shot** [(3:57)](https://www.youtube.com/watch?v=37LVhP15zGw&t=237s): kompozice na začátku levelu, která hráči řekne, kde je a co ho čeká — autor ji používal na Ratchet & Clank.
- **Světlo a stín** [(4:44)](https://www.youtube.com/watch?v=37LVhP15zGw&t=284s): tvoří ohnisko a náladu; kontrast světel a stínů je kompoziční prvek, který vede hráče. A obrácené použití [(5:30)](https://www.youtube.com/watch?v=37LVhP15zGw&t=330s): **jasným světlem odvedeš pozornost od místa, kde chceš hráče překvapit**.
- **Environmental storytelling** [(6:16)](https://www.youtube.com/watch?v=37LVhP15zGw&t=376s): převrácení obří roboti v Horizon Zero Dawn vyprávějí dávnou válku; v Kingdom Come: Deliverance mají tábory zbytky jídla, díry zabedněné prkny a bandité věšící prádlo — **„není to mrtvý level, někdo tu žije"**.

Dvě věci, na kterých prostředí nejčastěji padá. **Měřítko** [(7:07)](https://www.youtube.com/watch?v=37LVhP15zGw&t=427s): čte se z věcí, se kterými postava interaguje — židle, kliky, zábradlí, schody; autor se přiznává, že si zničil celou místnost, protože nepoužil postavu jako referenci a skončil u nesmyslně vysokého stolu. A **objem výroby**: velký svět se staví z **modulárních setů** [(7:53)](https://www.youtube.com/watch?v=37LVhP15zGw&t=473s), tedy z opakovaně použitelných dílů „jako z Lega". Ty mají dvě protichůdné podmínky — musí mít **dost variant, aby šly rozlišit**, a být **dost nenápadné, aby si nikdo nevšiml, že je to pořád totéž** (bedna otočená jinak vypadá jinak, skála se dá naaranžovat několika způsoby).

Nejcennější rada dílu je ale o zpětné vazbě [(10:12)](https://www.youtube.com/watch?v=37LVhP15zGw&t=612s). Autorovi kdysi někdo řekl „odstraň z toho lesa všechny stromy". Místo provedení se zeptal, **v čem je problém** — a odpověď zněla „všeho je moc". Řešením nebylo mazání stromů, ale vyčištění textur a přeorganizovaná kompozice. **Pochop problém, neimplementuj navržené řešení.** A jako protijed na srovnávání se s ArtStation [(11:44)](https://www.youtube.com/watch?v=37LVhP15zGw&t=704s): „přes 80 % toho, co vytvořím, je crap, ale málokdo to uvidí" — vidíme jen vyleštěné výsledky, ne neúspěšné verze, které k nim vedly.

> **Pozn.:** Rada „zašpini místa, kterých se lidé dotýkají" [(10:58)](https://www.youtube.com/watch?v=37LVhP15zGw&t=658s) a věta **„kdokoli umí udělat luxusní láhev tequily — ale musíš postavit celý bar a vidět, jak to spolu funguje"** jsou nejlepší shrnutí rozdílu mezi portfoliovým assetem a herním prostředím: samostatný objekt hodnotíš podle sebe sama, prostředí podle vztahů.

**Souvislosti:** [Prostor a hranice: blockout a metriky](prostor-a-hranice.md#jeskyne-ktera-se-hraje-landmark-napred-detail-nakonec) *(greybox z druhé strany — očima level designéra)* · [Prostor vypráví](prostor-vypravi.md#vypraveni-na-rozpocet-navrhni-objekty-ktere-umi-vypravet) *(jak z týchž assetů dostat příběh)* · [Vedení hráče: scripted events](vedeni-hrace.md#scripted-events-veci-se-maji-stat-ve-spravnou-chvili) · [Tvorba prostředí v UE](../praxe/env-tvorba.md#nejdriv-tvary-design-language-a-chiaroscuro) · [Rejstřík: environmental storytelling](../rejstrik.md#environmental-storytelling) · [Rejstřík: blockout](../rejstrik.md#blockout)

---

## Co má artista vědět o designu (a proč art není podřízený)

**Zdroj:** [So You Wanna Make Games?? | Episode 10: Game Design](https://www.youtube.com/watch?v=yYYtBFSxoCg) · [Riot Games](https://www.youtube.com/channel/UCJEGvSZnQ1pkVfHO8s5G8hA) · ~15 min, závěr série

**Shrnutí:** Poslední díl série je určený artistům — a jeho hlavní teze je organizační, ne designová: **art není servisní oddělení designu.** Když art a mechaniky míří jinam, hra působí nepřirozeně, a náprava je dražší než dohoda na začátku. Kolem té teze díl staví minimum designové gramotnosti, kterou artista potřebuje: co je hra, proč se místo „zábavy" definuje konkrétní zážitek a jak vzniká férová obtížnost.

### Rozpad myšlenky

**Co je hra** [(0:50)](https://www.youtube.com/watch?v=yYYtBFSxoCg&t=50s): cíl, opozice, rozhodování a pravidla. Test funguje oběma směry — tenis projde, jedení cereálií ne („ale když přidáme pár pravidel a opozici…"). Užitečnější je ale druhý krok [(1:36)](https://www.youtube.com/watch?v=yYYtBFSxoCg&t=96s): **„zábava" je pro práci v týmu skoro nepoužitelné slovo**, protože je subjektivní. Místo něj se pojmenuje konkrétní zážitek — návštěva jiného světa, napětí, kamarádství, zvládnutí dovednosti, objevování, sebevyjádření. Důvod je praktický: bez toho vzniknou v týmu **konfliktní představy zábavy** a každý táhne jinam. Příklad z domácího hřiště: pár her staví zážitek na příběhu, ale **přidávání příběhových prvků do League of Legends by většinu hráčů nezaujalo**.

Odtud plyne nosná teze [(3:09)](https://www.youtube.com/watch?v=yYYtBFSxoCg&t=189s): art se snadno považuje za podřízený („designéři vymyslí pravidla, artisti to udělají hezké"), ale **v praxi to nefunguje**; nejlepší výsledky vznikají, když art, design a engineering míří ke společnému cíli a **připravují si navzájem cestu k úspěchu**. Video to podkládá dvěma způsoby. Pozitivně: **mechaniky nesou téma i bez grafiky** [(3:56)](https://www.youtube.com/watch?v=yYYtBFSxoCg&t=236s) — kostka na mřížce nic neznamená, ale jakmile způsobí poškození v okolí a zmizí, čteme ji jako bombu; zvětšení dosahu zesílí pocit moci. Totéž s pohybem: přidej ke kostce skok a je z ní žába; jinak se hýbe ninja, jinak zombie, jinak tornádo [(4:44)](https://www.youtube.com/watch?v=yYYtBFSxoCg&t=284s). Negativně: když art a mechaniky nesouhlasí, vzniká **keř, který zastaví kulku**, poštovní schránka zastavující náklaďák a „můj osobní favorit: **otevřené dveře, kterými nemůžeš projít**" [(4:44)](https://www.youtube.com/watch?v=yYYtBFSxoCg&t=284s). Nejpoctivější je ale příklad z vlastní kuchyně [(5:31)](https://www.youtube.com/watch?v=yYYtBFSxoCg&t=331s): jednu postavu v LoL navrhli **designéři jako tanka a artisti jako stealth assassina** — a hráči pak logicky nevěděli, co od ní čekat.

Zbytek dílu je designové minimum s dvěma body, které se vyplatí znát i artistovi:

- **Cíl musí být měřitelný hráčem** [(5:31)](https://www.youtube.com/watch?v=yYYtBFSxoCg&t=331s): checkpoint v Overwatch Payload říká oběma týmům, jak na tom jsou — jednomu „zbývá půlka", druhému „musíme zatlačit". Bez takového ukazatele je hra jako závod, kde nevíš, kolik kol se jede.
- **Férovost není totéž co obtížnost** [(8:40)](https://www.youtube.com/watch?v=yYYtBFSxoCg&t=520s). Trocha frustrace je v pořádku — „pracuješ pro hráče i proti němu" [(7:08)](https://www.youtube.com/watch?v=yYYtBFSxoCg&t=428s) — ale hra působí férově, jen když **jasně vysvětluje a je konzistentní**. Nekonzistentní a nepředvídatelná hra bere hráči to nejcennější: **možnost poučit se z vlastního selhání**. Vypravěčským důkazem je autorova historka o bossovi z Ninja Gaiden, kterého po týdnech konečně složil — a rozbitý ovladač ho stál konzoli [(7:54)](https://www.youtube.com/watch?v=yYYtBFSxoCg&t=474s).

> **Pozn.:** Rozpor „tank versus assassin" je [ludotematická disonance](ludonarativni-soulad.md#ludonarativni-disonance-kdo-ji-citi-a-kdy-vadi) uvnitř týmu — ne mezi příběhem a mechanikou, ale mezi dvěma odděleními. A rozlišení férové/těžké doplňuje dvojici [challenge a difficulty](obtiznost.md#challenge-je-co-difficulty-je-kolik) o třetí osu: **konzistence**. Rada z konce dílu — rozlišuj cíle (jaký zážitek chci) od taktik (jakými pravidly ho vyrobím) [(12:32)](https://www.youtube.com/watch?v=yYYtBFSxoCg&t=752s) — je tentýž nástroj jako [design pillars](zabava.md#zabava-neni-jedna-vec-taxonomie-a-pilire), jen formulovaný pro poradu.

**Souvislosti:** [Obtížnost: challenge vs. difficulty](obtiznost.md#challenge-je-co-difficulty-je-kolik) · [Ludotematický soulad](ludonarativni-soulad.md#ludonarativni-disonance-kdo-ji-citi-a-kdy-vadi) · [Systémy a mechaniky](systemy-a-mechaniky.md#pravidla-mechaniky-systemy-slovnik-s-ostrymi-hranami) · [Zábava: taxonomie a pilíře](zabava.md#zabava-neni-jedna-vec-taxonomie-a-pilire) · [Rejstřík: design pillars](../rejstrik.md#design-pillars)
