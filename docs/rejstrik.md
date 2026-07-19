# Rejstřík

Odborné termíny napříč skripty — **termín anglicky, výklad česky**, protože přesně tak se s nimi potkáš v editoru, dokumentaci i komunitě. Rejstřík má dvě vrstvy: každý výskyt termínu kdekoli na webu má automatický tooltip s krátkou definicí a tahle stránka přidává hloubku a odkazy do kapitol, kde termín žije v kontextu.

Rejstřík roste s obsahem — každé zpracované video sem přidává svoje pojmy.

---

### AAA

**Termín z financí, ne z kvality: označuje největší a nejbezpečnější finanční sázky v oboru.**

Analogie s ratingem dluhopisů. Neříká nic o tom, jestli je hra dobrá — říká, že rozpočet a marketing jsou tak velké, že si projekt nemůže dovolit riskovat. Proto může existovat i nezávisle financovaná AAA hra: nezávislost a měřítko jsou dvě různé osy. Doplňkově se používá AA pro střední rozpočty.

Kde se s tím potkáš: [Indie kariéra](teorie/indie-kariera.md#kdy-indie-hra-neni-indie-hra)

### A/B test

**Dvě verze téže hry dvěma skupinám testerů — rozhodne chování hráčů, ne jejich názor.**

Testerům se často neříká, co se testuje, ani že existuje druhá verze. Ukázkový případ: puzzle hra řešila, jestli zrušit skok — verze s nízkým skokem sklidila „na co tu je?", ve verzi bez skoku si většina hráčů absence ani nevšimla. Škrt potvrzen daty, ne debatou.

Kde se s tím potkáš: [Playtesting](teorie/playtesting.md)

### Abstract class

**Třída, kterou nejde umístit do světa ani vybrat v referencích — existuje jen jako rodič pro děti.**

U base class v Blueprintech se zapíná v `Class Settings → Generate Abstract Class`. Smysl: master má nést jen data a logiku, žádné meshe či materiály — cokoli master referencuje, se nahrává do paměti s každou referencí na něj. Abstraktní master nikdo omylem nespawne a size map zůstává štíhlá.

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md)

### Actor Component

**Znovupoužitelný díl chování, který se připne k libovolnému aktérovi — schopnost bez identity.**

Nemá vlastní reprezentaci ve světě (na rozdíl od scene komponent); nese logiku a data. Klíčové pravidlo: komponenta nikdy nepředpokládá, kdo ji používá — smrt, zásah nebo dokončení jen oznamuje dispatcherem a nechá vlastníka reagovat po svém. Skládání komponent je v UE náhrada za hlubokou dědičnost.

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md#komponenty-misto-dedicnosti-skladej-misto-vetveni) · [Komunikace Blueprintů](praxe/komunikace-blueprintu.md#interface-nebo-dispatcher-a-kolik-doopravdy-stoji-cast)

### ADSR

**Čtyři knoby obálky: Attack, Decay, Sustain, Release — jak zvuk naběhne, klesne, drží a dozní.**

Attack = náběh po stisku, decay = pokles k sustainu, sustain = hlasitost při držení, release = doznění po puštění. Platí pro noty i zvukové efekty; malá změna dynamiky výrazně mění pocit.

Kde se s tím potkáš: [Syntéza zvuku od nuly](hudba/synteza-zvuku.md) · [Sound design ve hře](hudba/sound-design-ve-hre.md)

### Affordance

**Vlastnost objektu či prostoru, která signalizuje, jak s ním jde interagovat — dřív, než to hráč zkusí.**

Pojem z designové psychologie (Gibson, Norman): klika říká „stiskni", římsa říká „vylez". V level designu se affordances vyrábějí světlem, kompozicí a kontrastem — tajná odbočka musí *vypadat* zajímavě a interaktivně, jinak ji hráč mine. Zrádné jsou falešné affordances: co vypadá průchozí a není, rozbíjí důvěru (viz invisible wall).

Kde se s tím potkáš: [Prostor a hranice](teorie/prostor-a-hranice.md) · [Vedení hráče](teorie/vedeni-hrace.md)

### AI Controller

**Mozek AI postavy: posedne pawna (tělo) a rozhoduje — kam jít, kdy útočit; tělo řeší pohyb a animace.**

Oddělení mozku od těla umožňuje znovupoužít logiku napříč postavami. Controller typicky spouští Behavior Tree nebo State Tree (`Run Behavior Tree` / StateTreeAI komponenta) a nese AI Perception. Postava ho dostane přes `AI Controller Class` + `Auto Possess AI`.

Kde se s tím potkáš: [Základy AI](praxe/ai-zaklady.md) · [State Trees](praxe/state-trees.md)

### AI Perception

**Percepční systém UE: smysly (sight, hearing, damage) jako konfigurace jedné komponenty, události při změně vjemu.**

Mocnější nástupce Pawn Sensingu: víc smyslů, stárnutí vjemů, lose sight radius (hystereze ztrácení cíle). Dva zádrhely: cíl musí mít AI Perception Stimuli Source komponentu a každý sense config potřebuje zaškrtnout Detect Enemies/Neutrals/Friendlies. Sluch a damage se hlásí přes Report Noise/Damage Event — signály pro AI, ne herní zvuk či poškození.

Kde se s tím potkáš: [AI vnímání](praxe/ai-vnimani.md) · [State Trees](praxe/state-trees.md) · [Základy AI](praxe/ai-zaklady.md)

### Akord

**Tři a více tónů znějících zároveň; nejzákladnější je triáda (základ + tercie + kvinta).**

Podle rozestupů je durový (světlý), mollový (temný) nebo zmenšený (ostrý). Ze stupnice vypadne sedm akordů s předvídatelnou náladou: 1., 4. a 5. stupeň durové, 2., 3. a 6. mollové, 7. zmenšený.

Kde se s tím potkáš: [Základy hudební teorie](hudba/hudebni-teorie-zaklady.md) · [Akordy a harmonie](hudba/akordy-a-harmonie.md)

### Alikvóta

**Vyšší frekvence znějící nad základním tónem (overtone); určuje barvu zvuku a to, co ladí.**

Reálný tón není jedna sinusovka, ale základní frekvence plus řada alikvót. U struny a píšťaly jsou to celočíselné násobky (harmonická řada). Souzvuk vzniká, když se alikvóty dvou tónů dobře potkávají a málo perou.

Kde se s tím potkáš: [Fyzika souzvuku](hudba/fyzika-souzvuku.md)

### ALS

**Advanced Locomotion System — komunitní locomotion framework pro UE; jeho autor dnes v Epicu designově vede GASP.**

Roky de facto standard pokročilého pohybu z marketplace: overlay stavy (pózy držení předmětů vrstvené přes locomotion), layer curves pro per-kost řízení blendů, stance systém. GASP je jeho duchovní nástupce a komunita ALS animace i vzory dál recykluje — overlay přístup ke zbraním nad GASP je přímo z ALS playbooku.

Kde se s tím potkáš: [GASP](praxe/gasp.md)

### Anchor (marketing)

**Povědomý prvek, který hráče ukotví u příliš nové hry: známý žánr, mechanika nebo značka.**

Protiváha hooku (termín Chrise Zukowského): samotná novost budí nedůvěru — „looks cool but I don’t trust it". Hra chce obojí: hook, který zastaví palec, a anchor, díky kterému si hráč umí představit, jak se to hraje. Vzorec Zacharyho Richmana: simple, with something unexpected.

Kde se s tím potkáš: [Nápad: hook, anchor, appeal](teorie/napad.md) · [Steam stránka](teorie/steam-stranka.md)

### Anim montage

**Animační asset pro jednorázové akce (útok, interakce), přehrávaný přes sloty do vybraných částí skeletu.**

Nad Motion Matchingem je montáž základ combatu: spodní tělo matchuje locomotion, horní hraje montáž ve slotu Upper Body (Layered Blend Per Bone + Blend Poses by Bool). Anim notifies uvnitř montáže řídí comba (AddCombo/ResetCombo okna); sloty pro zbraně patří do vlastní slot skupiny, ať výměna nepřeruší jiné montáže. Pro matchování do montáže slouží Pose Search Branch In.

Kde se s tím potkáš: [Systémy nad MM](praxe/mm-systemy.md) · [MM základy](praxe/mm-zaklady.md)

### Anim Notify

**Značka na časové ose animace, která v daném framu spustí logiku — zvuk, efekt, gameplay event.**

Vestavěné (Play Sound) i vlastní blueprint třídy (override Receive Notify) s instance editable parametry — notify pak nese data (která noha, který moment hodu). Notify state je varianta s trváním (od–do framu): motion warping okna, Pose Search Branch In. Pozor v blend space: Notify Trigger Mode default spouští jen nejváženější animaci.

Kde se s tím potkáš: [Kroky](praxe/footsteps.md) · [Interakce s předměty](praxe/interakce-predmety.md) · [Systémy nad MM](praxe/mm-systemy.md)

### Apofenie

**Lidský pud vidět vzory a příběhy i tam, kde nikdo žádný nenapsal — motor emergentního narativu.**

Dej hráči reprezentace, postavy a situace, a příběh si složí v hlavě sám (model, na kterém stojí RimWorld). Pro designéra to znamená, že narativ nemusí být autorský text: stačí systémy, jejichž srážky stojí za převyprávění.

Kde se s tím potkáš: [Engineering experiences](teorie/engineering-experiences.md) · [Příběh a postavy](teorie/pribeh-a-postavy.md)

### Arrangement

**Rozvinutí hudebního loopu do celé skladby — kdy co přidat, ubrat a jak přejít (aranžmá).**

Nejčastější past je „loop trap": pěkný loop, ale nevíš, jak z něj udělat píseň. Pomáhá pravidlo dvou loopů (nejvýš dvě změny na dvě opakování) a vědomí, že píseň žije v přechodech mezi sekcemi.

Kde se s tím potkáš: [Aranžmá: z loopu skladba](hudba/aranz.md)

### Art bible

**Dokument vizuálního jazyka hry: moodboardy, palety, reference a pravidla stylu.**

Vzniká paralelně s gameplay prototypem jako samostatná linka práce — a ve vertical slice se poprvé potká s mechanikami a příběhem. V minimalistickém GDD ji zastupuje pár referenčních obrázků s vytaženou paletou; vlastní dokument si zaslouží, až se tým rozroste nebo styl ustálí.

Kde se s tím potkáš: [GDD](teorie/gdd.md) · [Prototypování](teorie/prototypovani.md) · [Herní art: concept art](teorie/art-pipeline.md)

### Aspirační obtížnost

**Jak těžké je uspět DOBŘE: lepší cesta, víc bodů, volitelná hloubka — obtížnost, po které hráč sahá sám.**

Protipól průběžné obtížnosti (jak moc tě hra tlačí k prohře). Jahody v Celeste jsou učebnice: místo hard módu zvoleného předem se hráč rozhoduje v každém okamžiku, jestli si troufne na těžší verzi. Aspirační obtížnost vyrábí pocit dobře odvedené práce.

Kde se s tím potkáš: [Obtížnost a výzva](teorie/obtiznost.md)

### Asset pack

**Balík hotových assetů — modely, zvuky, UI, shadery — připravený k okamžitému použití.**

Pro sólo vývojáře nástroj přežití: 50 hodin vlastního lokalizačního toolkitu vs. hotový asset za pár desítek dolarů je reálná volba z praxe. Kupuje se to, co dělat neumíš nebo nechceš; vlastní ruce si šetři na to, čím se hra liší. Při prototypování asset packy dodají vizuál a vibe za nulový čas — a u „design by constraint" umí být rovnou zdrojem nápadu („šla by kolem tohohle jediného assetu postavit hra?").

Kde se s tím potkáš: [Žrouti času](teorie/produktivita.md) · [Nápad](teorie/napad.md) · [Scope](teorie/scope.md)

### Astroturfing

**Marketing, který předstírá, že vznikl zdola z komunity, i když ho platí firma.**

Termín z politiky (astroturf je umělý trávník — falešná „grassroots"). V herním kontextu se tak označuje snaha velkého vydavatele vypadat jako indie: cílit na estetiku, tón a hodnoty nezávislé scény bez odpovídajícího produkčního kontextu. Indie publikum na to reaguje citlivě právě proto, že u něj jde o hodnotový systém, ne jen o vkus.

Kde se s tím potkáš: [Indie kariéra](teorie/indie-kariera.md#kdy-indie-hra-neni-indie-hra)

### Attenuation

**Útlum hlasitosti zvuku se vzdáleností od zdroje.**

Ve stealth hrách často vizualizovaný v UI. Trik: dej vysokým frekvencím krátký útlum a nízkým dlouhý — zblízka je výstřel ostrý, z dálky jen temné dunění.

Kde se s tím potkáš: [Sound design ve hře](hudba/sound-design-ve-hre.md)

### B-roll

**Doplňkové záběry, které běží na obrazovce, zatímco mluvíš o něčem obecnějším — ve videích o hrách typicky záběry gameplaye.**

Pravidlo devlogů: na obrazovce má být hra, pořád — ideálně přesně to, o čem zrovna mluvíš, jinak aspoň obecný B-roll. Chytrý zdroj záběrů starších verzí hry: version control — checkout starého commitu a natoč, co potřebuješ.

Kde se s tím potkáš: [Devlogy](teorie/devlogy.md)

### Backlog

**Zásobník všeho, co projekt čeká: úkoly i nezralé nápady — priority se z něj tahají po dávkách.**

Dvojí užitek: nápady se parkují místo zabíjení (secret sauce poznáš často až za měsíc) a rozhodování o nich se přesouvá z emocí brainstormu na pravidelný rytmus — sprint meeting nebo měsíční blok, kde se seznam projde proti pilířům hry. Na dlouhém projektu je backlog nejdelší sloupec kanban boardu.

Kde se s tím potkáš: [Scope: scope creep](teorie/scope.md) · [Plánovací nástroje](teorie/planovani-nastroje.md)

### Backpressure

**Když producent chrlí rychleji, než konzument stíhá: nebufferuj, nezahazuj — propaguj tlak zpět, ať producent zpomalí.**

Naivní odpovědi na přetíženou frontu jsou buffer (odloží problém) a drop (ztratí data). Backpressure místo toho zpomalí zdroj na kapacitu spotřebiče — systém pak pod zátěží degraduje elegantně místo pádu. Ve hrách: spawn throttling, fronty eventů, streaming assetů.

Kde se s tím potkáš: [Programátorské myšlení](teorie/programatorske-mysleni.md)

### Barbell strategie

**Rozdělení sázek na dva krajní póly — velmi bezpečné a velmi riskantní — místo průměru uprostřed.**

Pojem Nassima Taleba pro prostředí, kde platí mocninné rozdělení: střední cesta tam kombinuje nejhorší z obou světů. V praxi indie studia to znamená držet stabilní základ (práce, úspory, backlog malých her) a z něj dělat odvážné, potenciálně obrovské sázky — ne dělat jednu opatrně průměrnou hru.

Kde se s tím potkáš: [Data o úspěchu](teorie/data-o-uspechu.md#extremistan-tri-mechanismy-ktere-vedou-ke-stejne-strategii) · [Přežít jako studio](teorie/prezit-jako-studio.md#ctyri-roky-bez-hitu-financovani-riziko-a-runway)

### Barrier to play

**Překážka, se kterou hráč zápasí, ačkoli ji designér testovat nechtěl: překomplikované ovládání, informace jen barvou.**

Derek Yu (Spelunky): hráč chtěl „odstranit síť", protože nepřehodil míč — a přitom dostal „raketu s prasklým výpletem". Dokud má hra bariéry, nelze ladit obtížnost ani měřit, jestli výzva baví: hráč nebojuje s výzvou, ale s rozhraním.

Kde se s tím potkáš: [Obtížnost a výzva](teorie/obtiznost.md)

### Behavior Tree

**Klasický rozhodovací strom AI v UE: selectory a sequence uzly volí tasky podle podmínek z Blackboardu.**

Strom běží na AI controlleru a čte sdílenou tabuli (Blackboard); decoratory hlídají podmínky a s „observer aborts" přerušují běžící větve při změně dat. Vlastní tasky se píší v blueprintu (Receive Execute AI → Finish Execute). Pro nové projekty Epic tlačí State Trees — koncepty se ale přenášejí.

Kde se s tím potkáš: [Základy AI](praxe/ai-zaklady.md) · [AI vnímání](praxe/ai-vnimani.md)

### Beta

**Pozdní testovací verze hry: obsahově víceméně celá, ladí se balanc, bugy a onboarding.**

Na Steamu jde veřejnou betu spustit přes playtest feature — a vyplatí se z ní udělat marketingový beat: „hratelná beta" je zpráva, kterou novináři a tvůrci obsahu můžou předat dál. Po veřejné vlně se testování často zase zužuje na uzavřené kolo s fokusovanými otázkami.

Kde se s tím potkáš: [Playtesting: škálování](teorie/playtesting.md) · [Steam stránka](teorie/steam-stranka.md)

### Blackboard

**Sdílená tabule AI: pojmenované klíče (vector, object, bool…), přes které si percepce, tasky a strom předávají data.**

Klíč typu Object→Actor umí Move To průběžně sledovat (žádné přepočítávání cíle); Blackboard decorator větví strom podle „Is Set / Is Not Set" a observer aborts okamžitě přepne chování při změně. Zápis z blueprintu: Set Blackboard Value as Bool/Vector/Object — jméno klíče musí sedět do písmene.

Kde se s tím potkáš: [Základy AI](praxe/ai-zaklady.md) · [AI vnímání](praxe/ai-vnimani.md)

### Blend Space

**Asset, který míchá animace podle hodnot na osách grafu — 1D (rychlost) nebo 2D (rychlost × směr).**

Klipy se rozmístí na osu (idle 0, walk 300, run 600…) a vstupní hodnota určuje mix. Klipy různých délek synchronizují sync markery — bez nich se kroky rozjedou. Blend spacy jdou vkládat i do Motion Matching databází a GASP animace jsou na to fázovány.

Kde se s tím potkáš: [Základy pohybu](praxe/pohyb-zaklady.md) · [MM základy](praxe/mm-zaklady.md)

### Blend stack

**Anim uzel, který při každé změně animační proměnné přidá nový blend do zásobníku — bez state machine.**

Základ, na kterém Motion Matching stojí: uvnitř MM uzlu běží graf per vybraná animace (tam žije orientation warping, steering…). Varianty: obyčejný blend stack (animace z proměnné), Chooser Player (animace z chooser tabulky, umí i stitch) a hybridní setup se state machine. Max počet současných blendů je konfigurovatelný.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md)

### Blockout

**Hrubá stavba levelu z primitivních tvarů — testuje prostor, metriky a flow dřív, než přijdou finální assety.**

Blockout disciplína: grid/metrické materiály (okamžitě vidíš, že vchod je úzký nebo skok dlouhý), konzistentní barevný jazyk (cover jedna barva, traversal jiná) a „level design gym" — referenční mapa metrik sdílená napříč levely. Startovní bod hráče a hlavní landmark se rozhodují ještě před blockoutem.

Kde se s tím potkáš: [Prostor a hranice](teorie/prostor-a-hranice.md) · [Prototypování](teorie/prototypovani.md)

### Beautiful corner

**Jeden malý kus hry dotažený do cílové kvality, zatímco zbytek zůstává v grayboxu.**

Mikroverze vertical slice: jedna místnost nebo jeden výjev jako art prototyp, podle kterého se pozná, kam hra míří vizuálně — aniž bys zabetonoval celý projekt. Řeší napětí mezi „drž iterační cykly krátké" a „potřebuju vidět, jak to bude vypadat"; sólo vývojáři navíc slouží jako legitimní odměna, která drží chuť do práce.

Kde se s tím potkáš: [Level design pro sólo vývojáře](teorie/level-design-solo.md) · [Prototypování](teorie/prototypovani.md)

### Blue ocean

**Trh bez konkurence: hra vytváří novou poptávku, místo aby se prala o etablované publikum (red ocean).**

Termín z byznys strategie: red ocean = přeplněné žánry, kde rozhodují zdroje (battle royale, souls-like); blue ocean = unikátní zážitek, který si publikum teprve vyrobí (Minecraft, Undertale). Pro indie bez rozpočtu velkých studií je modrý oceán — unikátní twist — obvykle lepší sázka.

Kde se s tím potkáš: [Sólo vývoj](teorie/solo-vyvoj.md) · [Nápad](teorie/napad.md)

### Blueprint Function Library

**Sbírka funkcí volatelných z libovolného blueprintu v projektu.**

Ideální pro helper funkce, které nepatří žádné konkrétní třídě: bezpečný přístup ke gameplay tag containeru libovolného actora, pure getter na Game Instance, zápis aktivit. Pure funkce bez side effectů se v grafu chovají jako čisté dotazy. Pravidlo: co voláš ze tří míst, patří do funkce; co voláš ze tří blueprintů, patří do library.

Kde se s tím potkáš: [Gameplay Tags](praxe/gameplay-tags.md) · [Ukládání](praxe/ukladani.md) · [Organizace projektu](praxe/organizace-projektu.md)

### Blueprint Interface

**Sada deklarovaných funkcí bez implementace — kontrakt, který si každý Blueprint naplní po svém.**

Volající posílá zprávu (message call) na libovolný actor; pokud actor interface implementuje, zareaguje vlastní logikou, pokud ne, nestane se nic — žádný pád, žádná závislost. Je to enginová podoba principu „programuj proti rozhraní": character nemusí znát třídu dveří, truhly ani panelu, stačí mu smlouva „umíš interagovat?". Přidání nového typu interaktivního objektu pak neznamená žádnou změnu ve volajícím.

Kde se s tím potkáš: [Interakce bez Event Ticku](praxe/interakce-bez-event-ticku.md)

### Boids

**Algoritmus hejna (Reynolds, 1986): tři lokální pravidla — separation, alignment, cohesion — a chování hejna emerguje samo.**

Každý agent se vyhýbá tlačenici, srovnává směr s okolím a drží se těžiště sousedů; výsledné vzory hejna nikdo nenaprogramoval. Učebnicový příklad emergence: komplexní chování se levněji pěstuje z jednoduchých pravidel, než skriptuje. Základ ptáků, ryb i davů ve hrách.

Kde se s tím potkáš: [Algoritmy, které stojí za to znát](teorie/algoritmy-prehled.md)

### Boolean

**Geometrická operace kombinující dvě tělesa: sjednocení (union), rozdíl (subtract), průnik (intersect).**

Pojmenováno po booleovské logice — tělesa se skládají jako množiny bodů. V Mesh Terrainu boolean modifier skutečně vroubuje cizí mesh do terénu: union přiroste, subtract vyřízne díru a geometrie se na okrajích sešije. Klasický nástroj CSG modelování (Constructive Solid Geometry), který znáš z Blenderu i CADů.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Bounds

**Osově zarovnaný obal (kvádr) kolem objektu či bodu — levná aproximace „kolik místa věc zabírá".**

Ve fyzice a tracingu zrychlují testy, v PCG jsou bounds bodů přímo pracovní data: Difference vyřezává podle nich (přesněji to umí kolizní data), Self Pruning jimi měří překryvy a bounds modifier je nafukuje či zmenšuje jako ladicí páku. Get Actor Bounds vrací obal celého actora — základ zarovnávání na neznámé meshe.

Kde se s tím potkáš: [PCG základy](praxe/pcg-zaklady.md) · [Parkour postaru](praxe/parkour-vault.md)

### BPM

**Tempo skladby v dobách za minutu (beats per minute); ukotví žánr dřív než noty.**

Lo-fi kolem 77, house 120–130, drum and bass kolem 170. Pro náladu scény je tempo první páka — energii nastavíš dřív, než vybereš jediný akord.

Kde se s tím potkáš: [Žánry a jejich melodie](hudba/zanry-a-styl.md)

### BRDF

**Model odrazu světla od povrchu — matematický základ toho, jak materiál vypadá.**

Bidirectional Reflectance Distribution Function popisuje, kolik světla se odrazí kterým směrem podle úhlu pohledu a dopadu. V praxi ho artista potkává jako sadu vstupů (base color, roughness, metallic, normal) a jako rozpad, na kterém se dá ladit jednotlivá složka zvlášť. Podle artistů Naughty Dog je nejpodceňovanější z nich roughness.

Kde se s tím potkáš: [Breakdowny: Naughty Dog](praxe/env-breakdowny.md#naughty-dog-shadery-misto-polygonu-a-nastroj-misto-modelovani) · [Rejstřík: PBR](#pbr)

### Building in public

**Stavět veřejně: průběžně ukazovat pokrok, rozhodnutí a zdi, na které narážíš — ne až hotový výsledek.**

Funguje dvakrát: jako disciplína (když je pokrok vidět, skončení přestává být neviditelné — v datech jedné výzvy přežívali skoro výhradně ti, kdo postovali buildy) a jako důkaz (veřejný záznam toho, jak myslíš, se nedá nafejkovat promptem). Nejcennější je sdílet uvažování, ne screenshoty úspěchů.

Kde se s tím potkáš: [Produktivita](teorie/produktivita.md) · [Učení v éře AI](teorie/uceni-v-ere-ai.md)

### Buoyancy

**Vztlak: systém Water pluginu, který nechá simulovaná tělesa plavat na vodních tělesech.**

Dvě cesty: klasicky Buoyancy komponenta s pontoony (body vztlaku — 4 rohy lodi; debug `r.water.debug.buoyancy 1`), od 5.7 stačí Physical Material Override → Default Buoyancy Physics Material + na water body kolize Query and Probe s Block na Physics Body. Objekt musí startovat nad hladinou a simulovat fyziku; ladí se mass, damping, center of mass.

Kde se s tím potkáš: [Voda a buoyancy](praxe/voda-a-buoyancy.md) · [Nástroje: EasyWaterscape](praxe/nastroje-voda.md)

### Burn rate

**Kolik peněz projekt nebo firma spálí za měsíc či rok, bez ohledu na příjmy.**

Základní číslo pro plánování: vynásobené délkou vývoje dá celkovou cenu projektu. U jednoho známého desetiletého indie projektu činí 1,8 až 4,4 milionu dolarů ročně; u tříčlenného studia může jít o zlomek toho. Spolu s [runway](#runway) tvoří dvojici, která rozhoduje o tom, jestli má smysl začínat velkou hru.

Kde se s tím potkáš: [Indie kariéra](teorie/indie-kariera.md#ekonomika-desetileteho-projektu) · [Přežít jako studio](teorie/prezit-jako-studio.md#ctyri-roky-bez-hitu-financovani-riziko-a-runway)

### Cable Component

**Vestavěná komponenta simulovaného lana/kabelu — fyzika z krabice, konce jdou ukotvit na objekty.**

Ladí se délka, počet segmentů (hladkost), tuhost, šířka a počet stran renderu (default 4 vypadá hranatě) + tile material. Váže se k pivotu cílového objektu — typicky doladit Z offset. `Get Cable Particle Locations` vrací body simulace, na které jdou věšet instancované meshe (girlandy, řetězy). Nosnou fyziku ale dělá physics constraint — kabel je vizuál.

Kde se s tím potkáš: [Kabely, lana a Physics Control](praxe/lana-kabely.md)

### Call to action

**Závěrečná výzva trailer u nebo videa: co má divák udělat teď — „Wishlist on Steam", „Demo out now".**

Formát pro herní trailer: 5–8 vteřin na konci, key art + název + jedna výzva. Právě jedna — dvě CTA najednou („demo + wishlist") si konkurují a oslabují se. V širším marketingu platí totéž pro každý kanál: post, devlog i stránka mají mít jeden jasný další krok.

Kde se s tím potkáš: [Steam stránka](teorie/steam-stranka.md)

### Capsule

**Náhledový obrázek hry na Steamu — miniatura, kterou zákazník vidí ve všech seznamech dřív než cokoli jiného.**

Nejdůležitější kus grafiky celé stránky. Zásady: žádné AI generované umění, custom nebo semi-custom logo (volný font + gradient + tematický detail), silný kontrast textu vůči pozadí, žádný text kromě názvu hry, nekolidovat se Steam badgi (Demo) — a rámeček, který capsule vysekne ze seznamu. Rozbory dobrých a špatných: steamcapsule.com.

Kde se s tím potkáš: [Steam stránka](teorie/steam-stranka.md) · [Co prodává](teorie/co-prodava.md)

### Camera director

**Objekt, který vlastní pravidla kamery pro danou oblast: hranice, čeho si všímat, jak plynule předat řízení dalšímu.**

Každá místnost má výchozího režiséra (hranice nastavené tak, aby tajemství zůstala skrytá) a trigger zóny s vlastními režiséry pro výjimky — tajné chodby, cinematic framing vysokých stropů. Předání se tweenuje; detail, na kterém stojí game feel celé kamery.

Kde se s tím potkáš: [Kamera](teorie/kamera.md)

### Cast

**Přetypování obecné reference na konkrétní třídu, aby šlo volat její specifické funkce.**

`Cast To DestroyDoor` řekne enginu „zkus s tímhle actorem zacházet jako s třídou DestroyDoor". Cena: volající Blueprint získává tvrdou závislost na cílové třídě (a tahá si její referenci do paměti), takže s každým novým typem objektu roste řetěz castů. Tam, kde jde jen o „pošli zprávu, kdo umí, zareaguje", je lepší Blueprint Interface.

Kde se s tím potkáš: [Interakce bez Event Ticku](praxe/interakce-bez-event-ticku.md)

### Channel

**V Mesh Terrainu pojmenovaná materiálová vrstva terénu — nástupce landscape layers.**

Channels se definují v data assetu partition definice 1:1 podle vrstev materiálu a rovnou se z nich stávají malovatelné vrstvy, bez ceremonie layer info assetů starého Landscape. Navíc je umí přiřazovat i modifiery (weight channel) — boolean skála si tak vyřízne tvar a zároveň obarví materiál. Pozor na kolizi názvosloví: UE má i kolizní channels (WorldStatic, Pawn…), to je jiný mechanismus.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Chaos Cloth

**Realtime fyzika látek přes Cloth Asset graf: import meshe → skin weights z těla → weight mapa → config → collider.**

Weight mapa (uzel MaxDistance) maluje, co simulovat a co nechat animaci; kolider dodává kopie physics assetu postavy. Ladicí trojúhelník: mapa × collider koule × config (stiffness, iteration/subdivision count = kvalita vs. CPU). Do postavy se zapojuje Chaos Cloth komponentou; aerodynamics config přidá vítr.

Kde se s tím potkáš: [MetaHuman v praxi](praxe/metahuman.md)

### Chooser

**Datová tabulka „když platí tyhle podmínky, vyber tenhle asset" — v MM přepíná databáze, obecně vybírá cokoli.**

Řádky = kandidáti (PSD, montáže, nested choosery), sloupce = podmínky (bool, enum, float range) bindnuté na proměnné AnimBP. V MM: databáze jako Dynamic value, On Update → Evaluate Chooser (All Results) → Set Databases To Search + Interrupt on database change. Umí i output sloupce (damage per útok). Plně integrovaný s rewind debuggerem.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md) · [Systémy nad MM](praxe/mm-systemy.md)

### Chord extension

**Tón přidaný k triádě nad kvintu — septima, nona, undecima… (rozšíření akordu).**

Okamžitě bohatší, „dospělejší" zvuk. Páteř lo-fi, R&B, house a neo soulu. Základní triáda je root + tercie + kvinta; extension staví dál po stejném vzorci obden.

Kde se s tím potkáš: [Žánry a jejich melodie](hudba/zanry-a-styl.md) · [Akordy a harmonie](hudba/akordy-a-harmonie.md)

### Chord generator

**Web nebo nástroj, který vygeneruje smysluplnou akordovou progresi za tebe.**

Pravidla stavby akordů někdo naprogramoval (chordchord.com a další). Vygeneruješ čtyřakordovou progresi, přepíšeš do piano rollu — obchází potřebu teorie pro rychlý start. Dlouhodobě je lepší stavět akordy sám.

Kde se s tím potkáš: [Zdarma a rychle: nástroje a game jam](hudba/nastroje-zdarma-a-game-jam.md)

### Chord progression

**Sled akordů hraných za sebou, který tvoří harmonickou kostru skladby.**

Vyklikáš ji po zvýrazněných tónech tóniny; emoci nese hlavně pohyb mezi akordy (vzestup pozitivní, sestup smutný), ne jednotlivé akordy. Generátory (chordchord.com) rozjezd usnadní, ale stavět ji ručně je z dlouhodobého hlediska lepší.

Kde se s tím potkáš: [Akordy a harmonie](hudba/akordy-a-harmonie.md) · [Jak psát melodie](hudba/melodie.md)

### Cipher

**Typ hráčské postavy: prázdná nádoba bez vlastní osobnosti, hlasu a motivací — oživuje ji hráčova imaginace.**

Jeden ze čtyř typů protagonisty (cipher · fixní · customizovatelný · customizovatelný s fixním základem). „Bez osobnosti" není vada: mlčící postava v puzzle hrách (Half-Life, Tunic) nechává znít hlas v hráčově hlavě. Cena: veškerá tíha charakterizace jde do vizuální komunikace — jak postava vypadá a co reprezentuje. Praktické pravidlo: umíš psát → fixní postava; umíš vyrábět cool věci, ale ne psát → cipher.

Kde se s tím potkáš: [Příběh a postavy](teorie/pribeh-a-postavy.md)

### Closing doors

**Iterační metoda od širokého k úzkému: každé kolo zavře, co nefunguje, a rozvine, co zaujalo.**

Riotí postup pro concept art, ale funguje na jakoukoli tvůrčí volbu. Stojí a padá s jedním sebeovládáním: zavřené dveře se znovu neotevírají. Bez toho pravidla se tým točí v kruhu a projekt se každé tři měsíce potichu promění v jinou hru. Doplňuje se otázkami na cíl (která z nich působí nejděsivěji?) místo otázek na dojem.

Kde se s tím potkáš: [Herní art: pipeline](teorie/art-pipeline.md) · [Nápad](teorie/napad.md)

### Cognitive load

**Kolik mozkové kapacity aktivita právě žere; učení nové dovednosti je vědomé a drahé, automatizace ji zlevňuje.**

Příliš nízká zátěž nudí, příliš vysoká zahltí — onboarding je řízení komplexity vůči fázi učení hráče. Pestřejší nepřátelé, víc informací na obrazovce a nové mechaniky zátěž zvedají; proto se nové věci dávkují a učí v izolaci, než se smíchají.

Kde se s tím potkáš: [Obtížnost a výzva](teorie/obtiznost.md) · [Zábava a flow](teorie/zabava.md)

### Cold open

**Otvírák traileru: prvních 10–15 vteřin nabitých highlighty v rychlých střizích, teprve pak volnější tempo.**

Pojem z filmového střihu (a trailerového řemesla Dereka Lieu). Důvod jsou retention grafy: velká část diváků odpadne během první půlminuty — kdo šetří nejlepší záběry na konec, ukáže je prázdnému sálu. Pravidla k tomu: celková délka 30–50 s, žádný záběr přes ~6 vteřin, na konci call to action.

Kde se s tím potkáš: [Steam stránka](teorie/steam-stranka.md)

### Collision preset

**Předpis, jak objekt reaguje na jednotlivé kolizní kanály: Block, Overlap, nebo Ignore.**

Preset je první a nejlevnější filtr kolizního systému — rozhoduje se ještě před jakoukoli herní logikou. Trigger nastavený „Ignore all, Overlap jen WorldStatic/WorldDynamic/Pawn/PhysicsBody" negeneruje eventy o věcech, které tě nezajímají. Vlastní (Custom) preset se vyplatí kdykoli, kdy výchozí profily neodpovídají roli objektu.

Kde se s tím potkáš: [Interakce bez Event Ticku](praxe/interakce-bez-event-ticku.md)

### Constraints

**Nepsané dohody, se kterými musí souhlasit každý nový řádek kódu, aby program zůstal správný.**

Příklad: gameplay pozice se drží v desetinných číslech, ale zaokrouhluje na celá, zatímco vizuální pozice se plynule interpoluje — a kolize se počítají výhradně z gameplay pozice. Takové rozhodnutí padne brzy a všechno další s ním musí korektně spolupracovat. Čím větší program, tím hustší pavučina omezení — a právě proto jsou hluboké stavové chyby těžší než mělké. Blízký příbuzný pojmu [invariant](#invariant).

Kde se s tím potkáš: [Indie kariéra](teorie/indie-kariera.md#proc-ai-neumi-velky-kod-argument-o-omezenich) · [Principy architektury](praxe/principy-architektury.md)

### Content

**Vše, co jde ve hře opakovat s variacemi: levely, nepřátelé, příběh, odemykatelné věci.**

Protipól gameplaye (mechanik a systémů). Rozlišení má praktický důsledek: levely testují hráčovo porozumění mechanikám, takže je nelze rozumně navrhovat dřív, než víš, o čem hra je. Nejčastější chyba je vyrábět hory contentu do hry, která na to ještě není připravená — u malé hry se proto škrtá content, ne mechaniky.

Kde se s tím potkáš: [Level design: game design vs. level design](teorie/level-design-solo.md) · [Scope](teorie/scope.md)

### Contact curve

**Animační křivka 0/1 říkající, kdy je chodidlo na zemi — řídí foot pinning; v GASP nahradila foot velocity curves.**

Hodnota 0 = noha ve vzduchu, 1 = došlap. Proti rychlostním křivkám je konzistentní napříč gaity (walk i sprint sdílí stejnou škálu) a snadno se ručně edituje, když noha „lepí" špatně. Epic je generuje interním batch nástrojem; starý foot placement anim uzel pořád chce velocity curve, remapuje se přes Curve Expressions plugin.

Kde se s tím potkáš: [GASP](praxe/gasp.md)

### Content scheduling

**Kdy a jak často se ve hře věci dějí — rytmus obsahu, ne jeho množství.**

Nejčastější oprava hry, která „má všechno a nudí": nepřidat obsah, ale přeskládat ho v čase. Série dobrých částí bez rytmu je standup, kde každý vtip funguje a routine nedrží pohromadě.

Kde se s tím potkáš: [Případovky designu](teorie/pripadovky-designu.md)

### Context steering

**Technika pohybu AI: entita průběžně hodnotí všechny směry vahami a vybírá nejlepší proveditelný.**

Vylepšení klasických steering behaviors (boids), jejichž protichůdné vektory se umí vyrušit — AI pak zamrzne u zdi, místo aby ji obešla. Context steering drží ohodnocení celé růžice směrů (typicky přes dot product vůči kýženému směru); zablokovaný nejlepší směr prostě nahradí druhý nejlepší. Tvarováním vah vznikají chování jako kroužení kolem cíle nebo nájezdy a odskoky — základ soubojů, které jsou zábavné pohybem, ne čísly.

Kde se s tím potkáš: [Game feel a imerze](teorie/game-feel.md)

### Continuing pose

**„Co by hrálo dál, kdybych nic neměnil" — kandidát, kterého musí každá nová animace v Motion Matchingu porazit cenou.**

Klíč k ladění MM: v pose search debuggeru vidíš cenu continuing pose vedle vítěze a channels breakdown řekne, který kanál rozhodl. Continuing pose cost bias (záporný) drží systém déle v jedné animaci; notify tag Override Continuing Pose Bias protlačí hezkou animaci, i když matematicky nevyhrává.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md)

### Control Rig

**Grafový rigging a procedurální animace přímo v enginu — běží i za runtime, bez rekompilace.**

V GASP pohání foot placement Mover postavy (slope warping, pinning, root damping) a Locomotor (procedurální chůze bez jediné animace). Zároveň směr, kterým Epic míří s budoucím animačním frameworkem: animační systémy jako vizuální grafy, které si tech animátor otevře a ohne sám. Řemeslný vzor null + control zachovává hratelnost grafu ve viewportu.

Kde se s tím potkáš: [GASP](praxe/gasp.md)

### Core loop

**Základní smyčka činností, kterou hráč ve hře opakuje nejčastěji — jádro, na kterém všechno ostatní stojí.**

„Plíž se → pozoruj → proklouzni" nebo „těž → vyrob → prodej". Užitečný pojem při analýze (co hráč *reálně* dělá většinu času?) i při ořezávání scope — co nesytí core loop, je kandidát na vyhození. Zároveň platí výhrada z kapitoly o smyčkách: popisuje strukturu, nevysvětluje kvalitu.

Kde se s tím potkáš: [Smyčky a řetězce](teorie/smycky-a-retezce.md) · [Nápad](teorie/napad.md) · [Postmortem ShantyTown](teorie/postmortem-shantytown.md)

### Cyklus napětí

**Pět kroků hororové dramaturgie: setup → očekávání → semínko pochyb → diverze → akce; pak se napětí sbírá znovu.**

Setup a očekávání ustaví normál; anomálie ho nahlodají; diverze („čekáš úder — nic") napětí zdvojnásobí; akce ho vybije. Diverze užívej střídmě, jinak hráč prokoukne rytmus. Obecnější verze téhož: oscilace intenzity rozhodování.

Kde se s tím potkáš: [Horor design](teorie/horor-design.md)

### Degenerate strategy

**Strategie, která hru rozkládá: dominantní postup, po jehož objevení přestává být hra zajímavá.**

V kompetitivním prostředí ničí zážitek ostatním (combo winter v Magicu), v singleplayeru hráč „prokletý znalostí" zkazí hru sám sobě. Balanc existuje hlavně proto, aby žádná cesta nebyla čtvercovou dírou na všechno.

Kde se s tím potkáš: [Engineering experiences](teorie/engineering-experiences.md) · [Zábava: balanc](teorie/zabava.md)

### Data asset

**Asset nesoucí čistá strukturovaná data — konfiguraci bez logiky.**

V UE typicky potomek `UDataAsset`: designér edituje hodnoty v editoru, kód/Blueprinty je čtou. Odděluje „co" od „jak" — stejná logika, jiná data, jiné chování. Mesh Terrain v data assetu (Mesh Partition Definition) drží materiál, texel size a definice channels.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md) · [Kolik kódu potřebuješ na start](teorie/co-se-ucit.md)

### Data layer

**Kontejner aktorů ve world-partition světě se třemi stavy: Unloaded / Loaded (v paměti, neviditelné) / Activated.**

Aktory se přiřazují výběrem + right-clickem ve data layer outlineru, vrstvy se dají parentovat (celé patro jedním přepnutím) a aktor smí do víc vrstev. Za běhu je řídí Get Data Layer Manager → Set Data Layer Runtime State — typicky z trigger boxu s počítadlem hráčů. Pro interiéry uvnitř world-partition buňky a stavy „načti až po odemčení"; velké venkovní světy nech streamovat World Partition samotný.

Kde se s tím potkáš: [Optimalizace scény](praxe/optimalizace.md) · [Levely a streaming](praxe/levely-a-streaming.md)

### Data Registry

**Centrální registr konfiguračních dat: pojmenovaný prostor, do kterého se agregují data tables a curve tables.**

Systémy se ptají registru jménem („dej mi settings pro tuhle třídu") místo tvrdých odkazů na konkrétní tabulky. Instanced Actors přes něj čtou per-třída nastavení — řádek tabulky se jmenuje přesně jako třída s příponou `_C`. Registry musí ležet ve složce uvedené v Project Settings → Data Registry → Directories to Scan, jinak pro engine neexistuje.

Kde se s tím potkáš: [Instanced Actors](praxe/instanced-actors.md)

### Data-driven design

**Princip: hodnoty a konfigurace žijí v datech (data assety, tabulky), logika je jen čte.**

Damage, animace, zvuky ani cooldowny nepatří natvrdo do grafu — patří do data assetu, který ability/systém čte. Fragmenty (malé datové objekty pro volitelné části: animace, VFX, damage) řeší, že ne každá entita potřebuje všechno. Odměna: designér vytvoří novou ability výměnou dat, bez zásahu do logiky. UE Gameplay Ability System je tenhle princip dotažený do konce.

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md) · [Rejstřík: data asset](#data-asset)

### DAW

**Program na tvorbu hudby — nahrávání, MIDI, piano roll, mix, export (digital audio workstation).**

FL Studio, Ableton, Reaper, GarageBand nebo bezplatné LMMS. Srdce celého procesu; stačí ti stock nástroje, co s ním přijdou. Reaper má neomezenou zkušební verzi.

Kde se s tím potkáš: [Zdarma a rychle: nástroje a game jam](hudba/nastroje-zdarma-a-game-jam.md)

### Decal

**Materiál promítnutý na povrch světa — otisky, cákance, graffiti; spawnuje se za běhu bez úpravy podkladu.**

`Spawn Decal at Location` s velikostí a rotací; materiál v režimu deferred decal (translucent). Umístění: bod dopadu + normála × malý offset proti z-fightingu; rotace z normály povrchu, ať decal „leží". S dynamic material instancí jde per decal řídit texturu, barvu i fade-out v čase.

Kde se s tím potkáš: [Kroky](praxe/footsteps.md)

### Design by constraint

**Metoda hledání nápadů: nejdřív si zvol omezení, která řežou scope, a nápad nech vzniknout uvnitř nich.**

„Žádný příběh", „celá hra na jedné obrazovce", „žádné viditelné postavy", „jeden level" — omezení zmenší prostor možností tak, že se v něm dá tvořit. Postup: zvol omezení → posbírej hry se stejným omezením jako katalog interakcí → nech omezení třít o téma, dokud nevypadne nápad (piráti × jedna obrazovka = ostrov). Mini Metro tak vzniklo doslova. Druhá půlka metody: každé vývojářské omezení potřebuje player-facing alibi — téma, které ho vysvětlí a prodá.

Kde se s tím potkáš: [Scope: malé hry a design by constraint](teorie/scope.md) · [Prototypování](teorie/prototypovani.md)

### Demo

**Veřejná verze hry, jejímž úkolem je hru prodat — ne ji otestovat.**

Rozdíl proti playtestovacímu buildu je zásadní: demo předpokládá, že už víš, že hra baví. Většina hráčů od něj čeká vertical slice; nejčastější chyba je „diagonální řez", kdy demo naznačí systémy, které pak neukáže. Test dobrého dema: odpovídá na pochybnosti, které bude mít fanoušek žánru.

Kde se s tím potkáš: [Vydání hry: demo prodává, prototyp validuje](teorie/vydani-hry.md) · [Playtesting](teorie/playtesting.md)

### Design pattern

**Pojmenované řešení opakujícího se programátorského problému — slovník, ne dogma.**

Katalog 23 vzorů sepsala v roce 1994 „Gang of Four" do tří rodin: creational (vznik objektů), structural (vztahy), behavioral (komunikace). Vzory nejsou vynálezy, ale jména pro řešení, která dobří programátoři nacházejí opakovaně — a kdo je zná, umí pojmenovat, co staví.

Kde se s tím potkáš: [Design patterns](teorie/design-patterns.md) · [Komunikace Blueprintů](praxe/komunikace-blueprintu.md)

### Design pillars

**2–3 pojmy popisující, co má hráč cítit — a váha, proti které se měří každé rozhodnutí vývoje.**

Pilíře nejsou žánr ani art style („third person shooter" je popis kamery, ne pilíř) — popisují emoce a zkušenost koncového hráče. God of War 2018: exploration, combat, pouto otce a syna; SOMA: everything is story, trust the player. Šetří rozhodování: co pilíře nesytí, letí.

Kde se s tím potkáš: [Zábava: taxonomie a pilíře](teorie/zabava.md) · [Ludotematický soulad](teorie/ludonarativni-soulad.md) · [GDD: pilíře, publikum, jádro](teorie/gdd.md)

### Dependency stack

**Diagram závislostí systémů hry: dole core mechaniky, nahoře obohacení, které jde kdykoli škrtnout.**

Rodiny potřebují postavy, místnosti potřebují stavební mechaniku — pořadí práce padá ze stromu samo a škrty se dělají shora. Sdílený spodek stacku je důvod, proč studia vyrábějí variace téže hry (Fallout/Elder Scrolls).

Kde se s tím potkáš: [Engineering experiences](teorie/engineering-experiences.md) · [Zápisek: Derivační řetěz IZBY](zapisky/derivace-izby.md)

### Devlog

**Video (či zápis) o vývoji vlastní hry — marketingový kanál a žánr s vlastním řemeslem.**

Dvě funkční podoby: showcase (rozbor jedné feature: proč → proces → výsledek → limity) a story (příběh vývoje, včetně slepých uliček); nejlepší devlogy obojí mísí. Klíč ke kvalitě je scénář — psaný nahlas, ne jako sloh — a hra na obrazovce po celou dobu. Devlog není povinnost: dělá se, když tě baví videa, ne pro automatické wishlisty.

Kde se s tím potkáš: [Devlogy](teorie/devlogy.md) · [Postmortem ShantyTown](teorie/postmortem-shantytown.md) · [Zápisky: devlog jako mapa](zapisky/devlog-jako-mapa.md) *(devlog jako interní nástroj, ne marketing)*

### Difficulty curve

**Průběh obtížnosti hry v čase — a hlavní nástroj, jak držet hráče ve flow.**

Skládá se ze dvou složek: novelty (učení nového) a mastery (zvládání naučeného). Šachy mají novelty nafrontovanou na začátek; hry často volí pilový tvar — s každou novou mechanikou schválně klesnou nároky na mastery, aby zbyla kapacita na učení. Doplňkové nástroje: matchmaking, automatické přizpůsobení, skill gates (těžší vstup filtruje nepřipravené) a rubber banding.

Kde se s tím potkáš: [Zábava: flow](teorie/zabava.md)

### Disonance

**Dojem napětí či drsnosti při současném znění tónů; opak konsonance.**

Fyzikálně vzniká ze záznějů blízkých frekvencí a nedokonalého rozlišení ucha. Není to vypínač, ale spojité pásmo — použitelné jako řízená páka napětí (horor, boss vs. klid, domov).

Kde se s tím potkáš: [Fyzika souzvuku](hudba/fyzika-souzvuku.md)

### DLSS

**NVIDIA upscaler: hra se renderuje v nižším rozlišení a AI ji dopočítá do nativního — víc FPS, u 4.5 i stabilnější obraz.**

Do projektu přes plugin z NVIDIA developer webu (složky do engine Plugins). Blueprint vzor: Query Support → Set Mode (quality = 66 % rozlišení, ultra performance = 33 %); k tomu Frame Generation (násobení snímků) a Reflex (nižší latence). Nezapomeň kompenzovat mip/LOD bias — engine při nižším interním rozlišení potichu sníží kvalitu textur i Nanite. Multiplatformní alternativa v enginu je TSR.

Kde se s tím potkáš: [Textury a DLSS](praxe/textury-a-dlss.md)

### DNA soubor

**Popis vyřešené MetaHuman hlavy — topologie a proporce namapované na tvůj mesh.**

Vzniká krokem Save Pose v MetaHuman Creatoru po úspěšném solve a je vstupem pro všechno další: z něj se generuje skeletal mesh pro přenos textury a podle jeho referenční pózy se zarovnávají doplňky, které solver ignoroval (rohy, velké uši). Bez uloženého DNA se pozdější kroky nedají zopakovat.

Kde se s tím potkáš: [MetaHuman: z cizího meshe](praxe/metahuman.md#z-ciziho-meshe-metahuman-solve-prenos-textury-a-prichyceni-rohu)

### Dogfooding

**Používání vlastního produktu jako jeho první a nejpřísnější zákazník.**

Nejlevnější test, že nástroj, komponenta nebo engine unese reálnou práci: postav na něm vlastní věc dřív, než ho dáš ostatním. Náklady vložené do dogfoodingu (hra na vlastním frameworku, demo na vlastním enginu) se konvertují do hodnoty produktu — nálezy přicházejí dřív než support tickety a roadmapa nástroje dostává tvar podle skutečného konzumenta, ne podle domněnek.

Kde se s tím potkáš: [Zápisky: pravidlo 70/30](zapisky/pravidlo-70-30.md) · [Zápisky: devlog jako mapa](zapisky/devlog-jako-mapa.md)

### Dot product

**Skalární součin dvou jednotkových vektorů = kosinus úhlu mezi nimi: 1 stejný směr, 0 kolmost, −1 protisměr.**

Nejlevnější odpověď na otázku „jak moc se dva směry shodují": pár násobení a součtů, žádná goniometrie za běhu. Stojí na něm osvětlení (L·N), zorná pole AI (porovnej dot s cos poloviny FOV) i rozhodnutí „je cíl přede mnou, nebo za mnou" (znaménko).

Kde se s tím potkáš: [Matematika pro gamedev](teorie/matematika-pro-gamedev.md) · [AI vnímání](praxe/ai-vnimani.md)

### Draw call

**Příkaz CPU pro GPU „vykresli tohle" — každý unikátní objekt s unikátním materiálem znamená jeden navíc.**

Tisíce draw calls zahltí CPU dřív, než GPU vůbec začne kreslit. Léky: instancing (stejný mesh + materiál = jeden call pro všechny výskyty), trim sheety a atlasy (víc objektů sdílí materiál) a auto-instancing enginu — v UE4 vázaný i na stejnou lightmapu (trik The Ascent: větší lightmapy = −10 % calls). Pro artistu metrika číslo jedna: šetří se návrhem assetů, ne až profilerem.

Kde se s tím potkáš: [Breakdowny](praxe/env-breakdowny.md)

### Dynamic Material Instance

**Kopie materiálu vytvořená za běhu (`Create Dynamic Material Instance`), jejíž parametry jdou měnit z kódu.**

Scalar/vector/texture parametry pojmenované v materiálu se nastavují uzly Set Parameter Value — jména musí sedět do písmene. Základ všeho, co se vizuálně mění za hry: slábnoucí stopy, zabarvení zásahu, progres přebíjení. MID žije per objekt — změna jedné instance neovlivní ostatní.

Kde se s tím potkáš: [Kroky](praxe/footsteps.md)

### Early access

**Placený předběžný přístup k nedokončené hře, obvykle s příslibem dalšího vývoje.**

Pro hráče je to riziko, a proto jsou u dem ostražití: kdo byl jednou popálený nedokončenou hrou, čte odmávnuté featury jako varování. Historický příklad dobré praxe je hra, která šla do early accessu jen se sandboxovým režimem, bez kampaně — tedy jako poctivý horizontal slice.

Kde se s tím potkáš: [Vydání hry](teorie/vydani-hry.md)

### Edit layer

**Vrstva úprav Landscape terénu — sculpt i paint žijí v pojmenovaných vrstvách, které jdou zapínat a mazat.**

Nástroje pracují s aktuálně vybranou vrstvou: copy/paste gizmo kopíruje jen z ní (jinak prázdno), water bodies si vytvářejí vlastní vrstvu. Zhruba totéž, co v Mesh Terrainu dělají modifiery — jen bez 3D volnosti a přeskládávání priorit.

Kde se s tím potkáš: [Landscape tipy](praxe/landscape-tipy.md) · [Voda a buoyancy](praxe/voda-a-buoyancy.md)

### Editor Utility Widget

**Blueprint UI, které běží v editoru a automatizuje práci — vlastní nástroj bez psaní pluginu.**

Spouští se pravým klikem → Run Editor Utility Widget a dá se ukotvit vedle ostatních panelů. Typické použití: dávkové přejmenování, kontrola konvencí, přepínání zobrazení scény. Protože je to obyčejný blueprint, jde cizí nástroj otevřít, přečíst a upravit — což je zásadní rozdíl proti zkompilovanému pluginu.

Kde se s tím potkáš: [Animační nástroje: SAM](praxe/animace-nastroje.md#sam-izolace-jednoho-aktera-jako-animatorsky-rezim) · [Editor tipy](praxe/editor-tipy.md)

### Eigenvektor

**Směr, který lineární transformace nevychýlí — vektor zůstává na své přímce, jen se natáhne či zkrátí o eigenvalue.**

Pro každou matici jiné; párové číslo eigenvalue říká, kolikrát se eigenvektor při transformaci škáluje. U symetrických matic jsou eigenvektory navzájem kolmé, což umožňuje spektrální rozklad: rotace na osy → škálování → rotace zpět.

Kde se s tím potkáš: [Lineární algebra vizuálně](teorie/linearni-algebra-vizualne.md)

### Elemental tetrad

**Čtyři části každé hry podle Jesseho Schella: estetika, mechaniky, technologie a příběh.**

Z knihy The Art of Game Design. Užitečný ne jako škatulky, ale jako kontrolní seznam iterace: každé kolo vývoje má projít všemi čtyřmi — kdo jede jen ve své silné čtvrtině, hru nezlepšuje, jen leští jednu její stěnu.

Kde se s tím potkáš: [Prototypování: iterační spirála](teorie/prototypovani.md) · [Základy designu](teorie/zaklady.md)

### Elevator pitch

**Popis hry na délku jízdy výtahem — nejčastěji ve formátu „X meets Y".**

Kombinace selhává dvěma způsoby: redundancí („The Walking Dead meets Day of the Dead" — totéž dvakrát) a nespojitelností (prvky, které hlava neposkládá). Dobrý pitch je teze, kterou zbytek dokumentu obhajuje — Monaco: „mechaniky Pac-Mana oženěné se stealth prvky Hitmana", a pak bod po bodu proč. Srovnej s pitch deckem — pitch je věta, deck je prezentace.

Kde se s tím potkáš: [GDD: Monaco](teorie/gdd.md) · [Nápad](teorie/napad.md)

### Environmental storytelling

**Vyprávění prostorem: rozmístění objektů říká, co se tu stalo, dřív než padne jediné slovo.**

Převrácená židle, otevřený šuplík a stopy používání (edge wear, škrábance u dveří, prach v koutech) skládají historii místa. Funguje i kompozičně — stopa předmětů vede hráče ke dveřím — a v hororu buduje napětí dřív, než se cokoli stane. Opak: sterilně čisté a symetrické prostory, které křičí „kulisa".

Kde se s tím potkáš: [Breakdowny](praxe/env-breakdowny.md) · [Vedení hráče](teorie/vedeni-hrace.md)

### EQ

**Zesílení nebo potlačení konkrétních frekvencí ve zvuku (equalizace).**

Čištění šumu, zvýraznění či ztlumení tónů, prosazení zvuku v mixu. Spolu s attenuation a reverbem základní nástroj tvarování herního zvuku.

Kde se s tím potkáš: [Sound design ve hře](hudba/sound-design-ve-hre.md)

### Equity

**Podíl na firmě — na rozdíl od půjčky se nesplácí, ale už nikdy se nevrátí.**

Typická cena inkubátoru: 25 000 až 50 000 € za deset procent firmy. Rozdíl proti smlouvě s vydavatelem je zásadní: u vydavatele podepisuješ jednu hru, u investora celou firmu včetně všeho, co kdy uděláš. Souvisí s tím i vnitřní rozdělení podílů mezi společníky podle toho, kdo nese jaké riziko.

Kde se s tím potkáš: [Financování](teorie/financovani.md#granty-inkubatory-a-investori-co-za-penize-odevzdas)

### Eulerovy úhly

**Rotace jako trojice yaw/pitch/roll aplikovaná v pevném pořadí — intuitivní, kompaktní, ale trpí gimbal lockem.**

Standard pro UI (v UE je to Rotator): tři čísla, kterým rozumíš. Cena: mizerná interpolace a gimbal lock — po otočení prostřední osy o 90° se vnější a vnitřní osa zarovnají a ztratíš stupeň volnosti. Uvnitř enginu proto rotace drží kvaterniony.

Kde se s tím potkáš: [Matematika pro gamedev](teorie/matematika-pro-gamedev.md)

### EV100

**Jednotka expozice: kolik světla pustí kamera do obrazu — EV100 = 1 odpovídá modré hodině, interiér ~5–7, slunečný den ~13.**

Zamčení min = max EV100 v post-process volume vypne auto-exposure a jas scény řídíš ty. Pozor na kopírovaný recept „nastav 1/1": jednička sedí jen velmi tmavým scénám — hodnota se volí podle scénáře a podle toho, pro co exponuješ (slunce, nebo stíny). Vyšší číslo = tmavší obraz.

Kde se s tím potkáš: [Osvětlení](praxe/osvetleni.md) · [Stavba prostředí](praxe/env-tvorba.md)

### EVDB

**Komprimovaný volumetrický asset pluginu Expanse — static mesh, který místo trojúhelníků nese objem.**

Expanse Volume Database drží mrak, kouř nebo oheň ve formě, která zůstává komprimovaná po celou pipeline, takže se dá v levelu duplikovat po stovkách. Rozdíl proti Volume aktéru je tentýž jako mezi static meshem a jeho aktérem: EVDB jsou data, Volume je to, co je zobrazuje. Vzniká konverzí z OpenVDB.

Kde se s tím potkáš: [Osvětlení: objemy přes EVDB](praxe/osvetleni.md#objemy-pres-evdb-mraky-a-mlha-jako-asset)

### Event dispatcher

**Rádio mezi Blueprinty: vlastník dispatcher zavolá, všichni přihlášení posluchači dostanou event.**

Deklaruje se na vysílači; posluchači se bindují (typicky na BeginPlay) a dodávají vlastní custom event. Umí parametry, unbind i více posluchačů najednou — a obrací závislost: vysílač o posluchačích neví. Použití: „stalo se X, koho to zajímá" (dveře otevřeny, cooldown skončil, aktivita zaznamenána). Pozor na race conditions při bindování v BeginPlay — pořadí inicializace actorů není zaručené.

Kde se s tím potkáš: [Komunikace Blueprintů](praxe/komunikace-blueprintu.md) · [Principy architektury](praxe/principy-architektury.md) · [Telemetrie](praxe/telemetrie.md)

### Event Tick

**Blueprint event volaný každý vykreslený snímek.**

Kód v Ticku běží 60× i vícekrát za vteřinu, ať se děje cokoli — je to polling: neustálé kladení otázky, jejíž odpověď se většinou nemění. Občas je nutný (plynulý pohyb, interpolace), ale většina herní logiky patří do eventů, timerů a delegátů, které se spouštějí při změnách. „Dostaň to z Ticku" je jedna z nejčastějších optimalizačních rad v UE — a hlavně rada architektonická.

Kde se s tím potkáš: [Interakce bez Event Ticku](praxe/interakce-bez-event-ticku.md) · [Kolik kódu potřebuješ na start](teorie/co-se-ucit.md)

### Expresivní mechanika

**Mechanika, která nepomáhá vyhrát, ale mění, jak hra chutná: pohladit kočku, emoty, rozbíjení beden bez lootu.**

Rádio a klimatizace auta vedle pedálů. Do prototypu nepatří (jádro první), ale bývá rozdílem mezi docela dobrou a výbornou hrou: vyrábí hravost (paidia), nechává hráče zanechat stopu a projevit vkus — a publikum ji čte jako attention to detail.

Kde se s tím potkáš: [Systémy a mechaniky](teorie/systemy-a-mechaniky.md)

### Extremistan

**Prostředí, kde jeden vzorek může převážit celý zbytek souboru — opak průměrovatelného světa.**

Talebův pojem: v Mediocristanu (tělesná výška) žádný jednotlivec statistiku nezmění, v Extremistanu (příjmy, prodeje her) ano. Prodeje na Steamu do Extremistanu patří — medián a průměr se liší o řády, takže „průměrná hra vydělá X" je neinformativní číslo. Praktický důsledek: strategie musí počítat s tím, že drtivá většina pokusů skončí u nuly a hodnota přijde ze vzácné události.

Kde se s tím potkáš: [Data o úspěchu](teorie/data-o-uspechu.md#extremistan-tri-mechanismy-ktere-vedou-ke-stejne-strategii)

### Find the fun

**Fáze prototypování: experimentuj s jádrem hry, dokud nezačne bavit samo o sobě.**

Indikátor nalezení: přistihneš se, že si s barebones mechanikou hraješ mimo pracovní dobu — „chtěl jsem vylézt na všechno, co šlo". Druhá podoba téhož: když tě při vývoji baví něco jiného, než co sis naplánoval, následuj to — Ape Out vznikl z ninja stealth hry, protože strkání nepřátel bavilo víc než plížení.

Kde se s tím potkáš: [Scope: malé hry v praxi](teorie/scope.md) · [Nápad: ideace](teorie/napad.md)

### Flipbook

**Mřížka snímků v jedné textuře, kterou materiál přehrává jako animaci.**

Standardní způsob, jak do hry dostat výbuch, kouř nebo jiskry bez simulace: 4×4 nebo 8×8 políček v jednom obrázku a uzel, který mezi nimi posouvá UV. Levné na paměť i na výkon, ale rozlišení každého snímku je zlomkem textury — proto se hodí na efekty, které hráč vidí krátce a v pohybu.

Kde se s tím potkáš: [Materiály: VFX textury](praxe/materialy.md#vfx-textury-nedelat-je-a-kdyz-uz-tak-v-krite) · [Tech art a VFX](teorie/art-specializace.md#vfx-primarni-sekundarni-terciarni-a-rozpocet-na-okazalost)

### Flow

**Stav plného zaujetí činností, kdy výzva přesně odpovídá dovednosti (Mihály Csíkszentmihályi, 1990).**

Podmínky: častá a rychlá zpětná vazba, hluboké soustředění, výzva ~ skill. Tyrollerovo vysvětlení, proč flow kanál funguje: je to pásmo nejlepšího poměru signálu k šumu — ve frustraci vrací svět pořád „špatně" a v nudě pořád „dobře", učit se dá jen tam, kde některé akce fungují a jiné ne. Prakticky: flow = nejefektivnější učení = zábava; frustrace emočně přebije flow, flow přebije nudu.

Kde se s tím potkáš: [Zábava: flow](teorie/zabava.md)

### Foley

**Ruční výroba zvukových efektů z reálných předmětů.**

Když knihovna nestačí, zvuk se nahraje z fyzických rekvizit. Riot pro postavu Iverna sroubil „The Creaker" ze dvou prken, pantů a provazu, aby vrzání dodalo napětí před prasknutím štítu.

Kde se s tím potkáš: [Sound design ve hře](hudba/sound-design-ve-hre.md)

### Foot placement

**Procedurální usazení chodidel na terén: IK na svazích, špendlení došlapů, tlumení roota na hrbolech.**

Řeší tři viditelné neduhy: vznášení nohou na svahu (chodidla na terén + pokles pánve, ať noha dosáhne bez hyperextenze), klouzání chodidel při blendech a rotacích (foot pinning na world-space pozici došlapu) a poskakování těla na nerovnostech (root damping pružinou podél normály terénu). V GASP existuje jako anim uzel (CMC postava) i Control Rig graf (Mover postava); došlapy řídí contact curves.

Kde se s tím potkáš: [GASP](praxe/gasp.md) · [MM základy](praxe/mm-zaklady.md)

### Four-on-the-floor

**Bicí groove s kopákem na každé ze čtyř dob taktu.**

Základ house a další taneční hudby. Protože je pravidelný, staví se proti němu synkopovaná melodie a bas, aby vznikl tah a groove.

Kde se s tím potkáš: [Žánry a jejich melodie](hudba/zanry-a-styl.md) · [Aranžmá: z loopu skladba](hudba/aranz.md)

### Game Design Document

**Dokument s návrhem hry (GDD) — funguje jen tehdy, když se do něj tým skutečně vrací.**

Klasická podoba (slohová práce v akademickém formátu) u sólo vývojářů umírá nedopsaná a nečtená. Funkční alternativa je vizuální nástěnka: reference s důvody, levely jako sekvence, mechaniky jako GIFy, centrální to-do. Jediná metrika kvality GDD je, jestli je *živý* — forma je vedlejší.

Kde se s tím potkáš: [GDD: dokument jako způsob myšlení](teorie/gdd.md) · [Start projektu](teorie/jak-zacit.md) · [Zápisky: GDD review](zapisky/gdd-review.md)

### Gestalt

**Psychologická škola, podle níž člověk vnímá celý obraz a z uspořádání si odvozuje vztahy mezi částmi.**

Do grafického designu se dostala dávno před videohrami a odtud se přelily konvence rozhraní. Pro vývojáře z ní plyne obrácený postup: nezačínej jednotlivým assetem (na který jsi vždy zazoomovaný), ale kompozicí celku, protože hráč uvidí obrazovku najednou. Prakticky: prvky v jedné řadě čteme jako příbuzné, oddělené skupiny jako různé kategorie.

Kde se s tím potkáš: [Vizuální komunikace](teorie/vizualni-komunikace.md) · [Art specializace: UI](teorie/art-specializace.md)

### Game feel

**Hmatový dojem z ovládání hry: odezva, váha, šťavnatost interakcí — souhrn tisíce drobností, které dělají z klikání požitek.**

Screen shake, částice, zvuky zásahů, animační mikropohyby. „Game feel je cheat code": 20 % úsilí udělá 80 % dojmu a částice zamaskují nedodělky líp než cokoli jiného — proto patří i do prototypů. Zároveň platí pravidlo hraček: interakce mají být příjemné samy o sobě, dřív než na nich postavíš výzvy a cíle.

Kde se s tím potkáš: [Game feel a imerze](teorie/game-feel.md) · [Základy: engagement a appeal](teorie/zaklady.md) · [Nápad](teorie/napad.md)

### Game Instance

**Objekt žijící od spuštění aplikace po její konec — přežívá přechody mezi levely.**

Domov pro session-wide stav: reference na SaveGame, generátory unikátních ID, nastavení. Existuje vždy (C++ default); vlastní Blueprint verze se registruje v `Project Settings → Maps & Modes → Game Instance Class`. Co do ní nepatří: per-hráč data (Player State) a per-level logika (Game Mode).

Kde se s tím potkáš: [Ukládání](praxe/ukladani.md) · [Principy architektury](praxe/principy-architektury.md)

### Game jam

**Časově omezená akce — typicky 48 hodin až týden — během níž vzniká celá malá hra, obvykle na zadané téma.**

Institucionalizovaný „malý rozsah": deadline ořeže scope za tebe a vynutí dokončení, což je přesně dovednost, kterou začátečník potřebuje trénovat nejvíc. Bonusy: publikum (ostatní účastníci hru zahrají), zpětná vazba a nulová penalizace za nedokonalost. Jamy fungují i jako „design by constraint jako služba" — omezení dostaneš zadáním; jen pozor, mechanika zábavná 10 minut nemusí unést hodinovou hru.

Kde se s tím potkáš: [Začátky bez zkušeností](teorie/zacatky-bez-zkusenosti.md) · [Scope](teorie/scope.md) · [Idea iceberg](teorie/rady-z-praxe.md)

### Game State

**Objekt se stavem probíhající hry, dostupný všem a replikovaný na server i klienty.**

Zatímco Game Instance přežívá levely a Player State patří jednomu hráči, Game State drží to, co platí pro celou aktuální partii — skóre, fázi kola, počet zbývajících nepřátel. Právě proto je to přirozený domov pro event manager: dispatchery na Game State může kdokoli odebírat, aniž by měl referenci na vysílajícího aktéra.

Kde se s tím potkáš: [Komunikace Blueprintů: mediator](praxe/komunikace-blueprintu.md#mediator-koordinator-uprostred-a-event-manager-v-game-state) · [Principy architektury](praxe/principy-architektury.md#naradi-z-workshopu-kde-co-bydli-a-jak-se-to-hybe)

### Gameplay loop

**Smyčka činností, kterou hráč opakuje — nejcitovanější popisný nástroj game designu.**

Základní podoba je reward-investment: akce → odměna → investice odměny → silnější akce. Smyčky pomáhají číst strukturu her a komunikovat záměr, ale samy o sobě vysvětlují málo — model, pod který spadá skoro každá hra, nediskriminuje. Doplňkovým tvarem je řetězec (chain), který na rozdíl od smyčky nese směřování a rostoucí emoční investici.

Kde se s tím potkáš: [Smyčky a řetězce](teorie/smycky-a-retezce.md)

### Gameplay tag

**Hierarchický identifikátor stavu (`Status.MovementBlocked.Stunned`) — náhrada boolean/enum špagety.**

Tag v containeru = true; síla je v hierarchii: dotaz na rodiče (`Status.MovementBlocked`) matchuje všechny potomky, takže nová schopnost blokující pohyb = nový sub-tag, nula změn v podmínkách. Spravují se v Gameplay Tag Manageru (soubory .ini, v týmu dělit podle domén). Pasti: struct z funkce je kopie (Add/Remove jen na skutečné proměnné) a ref counting (dva ohně, jeden tag). V GAS jsou tagy lepidlem celého systému.

Kde se s tím potkáš: [Gameplay Tags](praxe/gameplay-tags.md) · [Telemetrie](praxe/telemetrie.md)

### Garbage collection

**Automatická správa paměti: engine periodicky uklízí objekty, na které už nikdo neukazuje.**

V UE je objekt po zničení (`Destroy Actor`) nejdřív označen jako **pending kill** — existuje v paměti, ale je „mrtvý" — a fyzicky zmizí až při dalším úklidu. Reference na takový objekt projde, ale použití spadne na runtime error. Obrana v Blueprintech: Validated Get / `Is Valid` před každým použitím reference na objekt, který mohl zaniknout.

Kde se s tím potkáš: [Interakce bez Event Ticku](praxe/interakce-bez-event-ticku.md)

### GASP

**Game Animation Sample Project — Epicův „živý" ukázkový projekt gameplay animace: 500+ animací, hotový Motion Matching, traversal a od 5.7 Mover.**

Zdarma, blueprint-only. Smysl projektu: zvednout minimální laťku kvality herní animace a dát šablonu, jak MM stavět — databáze per stav, choosery, procedurální doladění. Není to plugin: do vlastního projektu se migruje content (+ console variables a pluginy) a každá verze enginu přináší výrazné změny.

Kde se s tím potkáš: [GASP](praxe/gasp.md) · [MM základy](praxe/mm-zaklady.md) · [Systémy nad MM](praxe/mm-systemy.md)

### Genre descoping

**Vzít jeden příjemný prvek velkého žánru a nafouknout ho na celou hru — vzorec vzniku nových subžánrů.**

Tower defense je RTS bez jednotek a útočení; backpack hry jsou Diablo svařené na inventář. Škrt musí něco přidat (fokus, přístupnost): dobrý nápad řeší dva problémy — méně práce pro vývojáře a ostřejší zážitek pro hráče.

Kde se s tím potkáš: [Žánry očima designéra](teorie/zanry.md) · [Scope a malé hry](teorie/scope.md)

### Gimbal lock

**Ztráta stupně volnosti u Eulerových úhlů: prostřední osa na 90° zarovná zbylé dvě a rotace se „slepí".**

Důsledek aplikace rotací v pevném pořadí. Vizuálně: tři gimbaly (kroužky), prostřední se otočí o 90° a vnější s vnitřním najednou točí kolem téže osy. Řešení: kvaterniony — proto se v enginech interpoluje přes slerp, ne přes yaw/pitch/roll.

Kde se s tím potkáš: [Matematika pro gamedev](teorie/matematika-pro-gamedev.md)

### Git LFS

**Rozšíření gitu pro velké binární soubory: v repozitáři je jen odkaz, obsah leží zvlášť.**

Bez něj git u každé změny ukládá celý binární soubor znovu, takže repozitář s animacemi a texturami rychle nabobtná. Háček je cena: na GitHubu je zdarma jen první gigabajt úložiště a pak se platí. Rozhodnutí zapnout či nezapnout LFS se dělá na začátku projektu — pozdější migrace je bolestivá.

Kde se s tím potkáš: [Organizace projektu: Git v Unrealu](praxe/organizace-projektu.md#git-v-unrealu-verzovani-z-editoru-a-cesta-zpet-v-case)

### GOAP

**Goal-Oriented Action Planning: AI si sama poskládá posloupnost akcí vedoucí k cíli.**

Každá akce má předpoklady a účinky; plánovač hledá řetěz, který ze současného stavu světa dojde k cíli. Proti behavior tree, kde posloupnost napíšeš ty, tady vzniká za běhu — cenou je horší předvídatelnost a ladění. S Utility AI se nevylučuje: utility vrstva vybere cíl, GOAP naplánuje cestu k němu.

Kde se s tím potkáš: [Základy AI: Utility AI](praxe/ai-zaklady.md#utility-ai-rozhodovani-podle-skore-misto-vetveni) · [State Trees](praxe/state-trees.md)

### God class

**Antipattern: třída, do které se postupně nastěhuje logika všech ostatních — a pak s každou změnou padá půl projektu.**

V dědičnosti vzniká z pohodlnosti („dám to do masteru, ať to mají všichni") — jenže kódový zámek jednoho typu dveří nepatří všem dveřím. Pravidlo: rodič nese jen to, co potřebují všechny děti; specifika bydlí v dětech. Příbuzný jev mimo dědičnost: player character s inventářem, questy a UI v jednom grafu — lék jsou komponenty.

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md) · [Organizace projektu](praxe/organizace-projektu.md)

### Graybox

**Prototyp či blockout ze šedých primitivních tvarů — bez artu, bez nálady, jen prostor a mechanika.**

Správné použití: testování mechanik a metrik (gameplay prototyp, level blockout), kde by krása jen zkreslovala zpětnou vazbu. Špatné použití: testování prodejnosti a emoce — šedé kostky žádnou nemají, tam patří asset packy a hudba od prvního dne. Rozhodni, kterou otázku prototyp klade, a podle toho zvol formu.

Kde se s tím potkáš: [Prototypování](teorie/prototypovani.md) · [Nápad: prototyp do týdne](teorie/napad.md) · [Prostor a hranice](teorie/prostor-a-hranice.md)

### Groom

**Systém vlasů a srsti z jednotlivých pramenů (strands) — MetaHuman vlasy, obočí i řasy.**

Groom komponenty mají vlastní LODy — při skládání postavy z komponent je drží pohromadě LOD Sync komponenta (bez ní se vlasy rozbijí; hlavní postavě typicky Force LOD 0). Dražší než mesh vlasy; v dálce se groomy přepínají na karty.

Kde se s tím potkáš: [MetaHuman v praxi](praxe/metahuman.md)

### Halting problem

**Turingův důkaz (1936): neexistuje obecný algoritmus, který o libovolném programu rozhodne, zda skončí.**

Zní akademicky, funguje jako kompas hranic řešitelnosti: každé „najdeme automaticky všechny bugy" a „AI garantuje správný kód" naráží na tenhle strop. Kdo o něm ví, je imunní vůči celé kategorii technického hadího oleje.

Kde se s tím potkáš: [Programátorské myšlení](teorie/programatorske-mysleni.md)

### HUD

**Heads-up display: vrstva informací zobrazená přes gameplay — zdraví, munice, minimapa, cíle.**

Jen jedna část UI: patří k němu i mapy, výběr postav, inventář, skill tree a questovní okna. Kolik HUDu hra unese, určuje žánr — karetní hra je z velké části rozhraní, narativní hra si vystačí s minimem. Rozvržení HUDu není dekorace: mozek dělá asociace podle blízkosti, takže pruh vedle jména nepřítele čteme jako jeho zdraví.

Kde se s tím potkáš: [Art specializace: UI a UX](teorie/art-specializace.md) · [První dojem](teorie/prvni-dojem.md)

### Hard coding

**Hodnoty napsané natvrdo přímo v kódu místo v proměnné či konfiguraci.**

Funguje přesně do chvíle, kdy je potřeba hodnotu změnit — pak ji lovíš po celém projektu a jednu zapomeneš. Pravidlo: každé surové číslo, které budeš někdy ladit, patří do proměnné; stejný princip platí pro vstupy (pojmenované akce místo kláves). Výjimka potvrzující pravidlo: v prototypu na vyhození je hard coding ctnost — rychlost tam poráží čistotu.

Kde se s tím potkáš: [Kolik kódu potřebuješ na start](teorie/co-se-ucit.md) · [Nápad: prototyp do týdne](teorie/napad.md)

### Hard reference

**Přímý odkaz na asset/třídu, který s sebou tahá vše, co cíl referencuje — do paměti i do buildů.**

Vzniká castem, class referencí, přiřazeným meshem. Diagnóza: pravý klik na asset → Reference Viewer (kdo na kom závisí) a Size Map (kolik paměti reference stáhne). Následky: dlouhé loady, provázané levely, křehké systémy. Léky: abstraktní datový master, interfacy, event dispatchery, broadcast kanály — a u assetů soft reference, které se načítají až na vyžádání.

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md) · [Komunikace Blueprintů](praxe/komunikace-blueprintu.md) · [Organizace projektu](praxe/organizace-projektu.md)

### Harmonická řada

**Řada alikvót struny nebo píšťaly: celočíselné násobky základní frekvence (1×, 2×, 3×…).**

Právě z ní vypadnou intervaly západní hudby — oktáva (2:1), kvinta (3:2), kvarta (4:3). Jiné nástroje (zvony, kovové tyče) mají neharmonické alikvóty, a proto vedou k jiným stupnicím.

Kde se s tím potkáš: [Fyzika souzvuku](hudba/fyzika-souzvuku.md)

### HDRI

**Panoramatická fotografie s vysokým dynamickým rozsahem — obloha a světlo skutečného místa v jednom assetu.**

HDRI Backdrop plugin ji promítne na kupoli a skylight z téže mapy vezme indirect — konzistentní intenzita oblohy i odrazů. Alternativa bez pluginu: obří sphere s Unlit materiálem a isSky checkboxem. Zdroje: Poly Haven, locationtextures.com (s časem a místem pořízení — hodí se pro fyzikální kalibraci světla).

Kde se s tím potkáš: [Osvětlení](praxe/osvetleni.md) · [Stavba prostředí](praxe/env-tvorba.md)

### Height mapa

**Černobílá textura kódující výšku terénu jasem pixelu: černá dole, bílá nahoře.**

Formát, na kterém stojí klasický Landscape — a zdroj jeho hlavního limitu: jedna hodnota na pixel znamená jediný stupeň volnosti (nahoru/dolů), takže jeskyně a převisy nejdou. Zůstává ale skvělým výměnným formátem: sculpt z Gaey či World Machine se přenáší právě height mapou a Mesh Terrain ji umí importovat jako startovní tvar i promítat jako texture modifier.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Hook

**Prvek, který hru prodá na první pohled: mechanika, premisa nebo obraz, u kterého se scrollující palec zastaví.**

Portálové portály, vlak-monstrum z Choo Choo Charles, „staráš se o svoje auto v psychedelické Zóně". Hook je vstupní bod trychtýře appealu — bez něj hra nemá jak oslovit lidi, kteří o ní nikdy neslyšeli. Test: dokážeš hook vtěsnat do titulku na Redditu nebo do 300 znaků short description? Hra bez jediné inovace hook nemá — a bez hooku není důvod, aby vznikla.

Kde se s tím potkáš: [Základy: engagement a appeal](teorie/zaklady.md) · [Prototypování](teorie/prototypovani.md) · [Nápad](teorie/napad.md) · [GDD: Monaco](teorie/gdd.md)

### Iluze plynulosti

**Pocit „rozumím tomu", který vzniká z plynulého čtení — a zhroutí se při prvním pokusu věc vysvětlit krok za krokem.**

Klasický experiment: lidé si věří, že chápou kolo nebo zip, dokud nemají popsat, jak přesně fungují. Proti iluzi pomáhá vybavování (retrieval practice), učení druhých a psaní vlastními slovy — všechno formy nárazu na realitu.

Kde se s tím potkáš: [Učení v éře AI](teorie/uceni-v-ere-ai.md) · [Zápisek: Kvízový protokol](zapisky/kvizovy-protokol.md)

### Inheritance

**Dědičnost: děti přebírají proměnné, funkce a komponenty rodiče — základ, na kterém stojí celý UE (Actor → Pawn → Character).**

Lakmusový test každého vztahu: „is it a?" — pes *je* mazlíček, dům není. Rodič je smlouva (co deklaruje, mají garantovaně všechny děti) a na smlouvě stojí polymorfismus: volající volá `Interact`, každé dítě odpoví po svém. Blueprint specifika: component eventy nejde overridnout (obal je do custom eventů), overridnutý event nespouští rodiče automaticky (Add Call to Parent Function).

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md)

### Idea reservoir

**Zásobník nápadů, které NEJSOU schválené: kanban sloupec před to-do, ze kterého se tahá podle vývoje hry.**

Rozdíl proti klasickému backlogu: nic v rezervoáru není slib. Když se ukáže, co ve hře funguje, taháš nápady, které to sytí — pivot bez přepisování plánu. Protilék na „therapeutic planning": dlouhé dokumenty psané pro dobrý pocit z nejistoty.

Kde se s tím potkáš: [Engineering experiences](teorie/engineering-experiences.md) · [Tvůrčí zásek: Grail metoda](teorie/tvurci-zasek.md)

### Horizontal slice

**Ukázka celé hry skrz zlomek jejích systémů — opak vertical slice.**

Vertikální řez předpokládá, že se všechny podstatné části hry vejdou do jednoho úseku. U pomalých her o postupném odemykání (management, budovatelské strategie, 4X) to neplatí: hráč potřebuje odehrát celou seanci. Řešením je dát mu celou hru, ale jen třicet až čtyřicet procent systémů — a zbytek naznačit jako slib do plné verze.

Kde se s tím potkáš: [Vydání hry: vertikální a horizontální řez](teorie/vydani-hry.md) · [Prototypování](teorie/prototypovani.md)

### Input buffering

**Vstup stisknutý těsně před tím, než je platný, se zapamatuje a provede v první možný moment.**

Skok zmáčknutý dva framy před dopadem se provede při dopadu — spolu s coyote time nejcitovanější výjimka, kterou input systém obsluhuje hráčovo očekávání místo doslovného čtení vstupů. „Input manager nemá slepě překládat stisky."

Kde se s tím potkáš: [Engineering experiences](teorie/engineering-experiences.md) · [Game feel a imerze](teorie/game-feel.md)

### Integer scaling

**Zvětšování obrazu celými násobky (2x, 3x) místo desetinných — jediný způsob, jak udržet pixel art ostrý.**

Neceločíselné zvětšení rozdělí jeden zdrojový pixel mezi dva cílové a hrana se rozmaže. Jde ruku v ruce s filtrováním textur na nearest a se zachováním poměru stran; společně to jsou tři nastavení, na kterých stojí, jestli hra vypadá ostře, nebo jako kaše.

Kde se s tím potkáš: [2D vizuál: pixel art](teorie/2d-vizual.md)

### Instance

**Konkrétní umístěný výskyt assetu v levelu.**

Jeden asset (mesh lampy) → stovky instancí (lampy po celé mapě). Rozlišení asset vs. instance je základ práce v editoru: úprava assetu se propíše všem instancím, úprava instance jen jí. Editor umí s instancemi pracovat hromadně — viz Shift+E pro výběr všech výskytů daného assetu.

Kde se s tím potkáš: [Tipy do editoru](praxe/editor-tipy.md)

### Indexical storytelling

**Vyprávění stopami a náznaky: hráč čte důsledky událostí a příběh si složí sám.**

Termín Clary Fernández-Vary; „index" je ze semiotiky znak, který zastupuje něco jiného, ale poznáš to jen proto, že ses to naučil — kouř znamená oheň, stopy znamenají, že tudy někdo šel. Prakticky to znamená rozmístit vodítka detektivního typu (vlečné stopy, podezřele čistá část místnosti) místo dopisů, které všechno vysvětlí.

Kde se s tím potkáš: [Prostor vypráví](teorie/prostor-vypravi.md) · [Příběh a postavy](teorie/pribeh-a-postavy.md)

### Instanced Actors

**Experimentální systém (5.5+): svět stojí z levných instanced static meshů a objekty u hráče se vymění za plnohodnotné Blueprint actory.**

Swap na blueprint řídí Max Actor Distance, culling samotných instancí Max Instance Distances. Zásadní pravidlo: probuzený actor vzniká pokaždé od nuly — stav (sebraný pickup) musí držet externí manager. Posunutou fyziku vrací na místo, pokud nezapneš Eject on Actor Moved. S PCG spojuje uzel Spawn Instanced Actors (interop od 5.6) a jednorázový setup přes Data Registry.

Kde se s tím potkáš: [Instanced Actors](praxe/instanced-actors.md) · [Případovka Hex-A-Gone](praxe/pcg-hexagone.md)

### Interval

**Vzdálenost mezi dvěma tóny, měřená v půltónech; nese vlastní emoční zabarvení.**

Kvinta (1→5) zní hrdinsky jako Star Wars, malá sexta tajemně, půltón napjatě. V melodii nesou emoci hlavně intervaly s největším důrazem — na začátku nebo ve vrcholu.

Kde se s tím potkáš: [Jak psát melodie](hudba/melodie.md) · [Základy hudební teorie](hudba/hudebni-teorie-zaklady.md)

### Invariant

**Podmínka, která v daném bodě programu platí vždy — bez ohledu na to, kudy se tam běh dostal.**

Rámec precondition → postcondition → invariant pochází z formální verifikace: místo „spusť a koukej, co spadne" se ptáš, co musí platit před, po a během. Herně: „HP nikdy pod 0", „inventář nepřeteče kapacitu" — a assert tam, kudy tečou data.

Kde se s tím potkáš: [Programátorské myšlení](teorie/programatorske-mysleni.md)

### Invisible wall

**Neviditelná kolize tam, kde vizuálně nic nebrání v cestě — nejhorší způsob, jak ohraničit mapu.**

Zabíjí imerzi přesně mechanismem „vidím, že to jde, ale hra mi to nedovolí". Alternativy: tvrdé hranice z přirozených bariér světa (útes, řeka, oceán) a pět druhů měkkých hranic — narativní, countdown, nepřátelská, ekonomická, percepční. Pravidlo: hráč se má rozhodnout sám, že dál nepůjde.

Kde se s tím potkáš: [Prostor a hranice](teorie/prostor-a-hranice.md)

### Iterace

**Jedno kolo smyčky uprav → otestuj → vyhodnoť; hry nevznikají jedním tahem, ale koly.**

Metafora spirály: ve středu je nedosažitelná dokonalá verze hry a každé kolo — přes všechny čtyři čtvrtiny elemental tetradu — tě k ní přiblíží. Playtest je motor iterace: neříká jen, jestli minulé kolo fungovalo, ale co má být v příštím.

Kde se s tím potkáš: [Prototypování: iterační spirála](teorie/prototypovani.md) · [Playtesting](teorie/playtesting.md)

### Izometrie

**Perspektiva bez úběžníku: vzdálené objekty se nezmenšují, takže scéna je čitelná v celé hloubce.**

Proto ji volí budovatelské a simulační hry — dává přehled o prostoru a snese hodně detailu, aniž by si prvky překážely. Dvě daně: perspektivu je nutné držet ve všech assetech (jinak se objekty odmítají slučovat s prostředím) a se statickou kamerou musíš řešit, co komu zakrývá výhled — mřížkou, zdí na horním okraji mapy nebo stupňovitým layoutem.

Kde se s tím potkáš: [2D vizuál: izometrie](teorie/2d-vizual.md)

### Juice

**Vrstva audiovizuálního feedbacku, která prodává akce: screen shake, particles, squash & stretch, flash při zásahu.**

Stejné mechaniky s juice a bez něj jsou dvě různé hry — dash stejné rychlosti působí rychleji, kulka s odletujícími kusy zdi má najednou váhu. Teoreticky čistý signal-to-noise: každý detail hlásí, co se stalo a že to svět zaznamenal. Leští se na jádru, které už baví.

Kde se s tím potkáš: [Game feel a imerze](teorie/game-feel.md)

### Kanban

**Řízení práce kartami ve sloupcích To Do → Doing → Done: tok, jasné vlastnictví, limit rozdělanosti.**

Trello je značka, kanban je systém (jede i v Jira nebo Notionu). Tři nosná pravidla: karty dost malé, aby šly dokončit; jeden vlastník na kartu — když jsou zodpovědní dva, není zodpovědný nikdo; a nejméně karet je uprostřed, protože Doing je deklarace dnešního fokusu, ne evidence ambicí.

Kde se s tím potkáš: [Plánovací nástroje](teorie/planovani-nastroje.md)

### Legibilita

**Čitelnost textu: jak snadno oko rozliší písmena a slova — ne totéž co velikost písma.**

Čtyři nejčastější prohřešky ve hrách: celé věty verzálkami (stejná výška písmen ruší tvar slova, nejvíc to dopadá na dyslektiky), zbytečně dekorativní řezy, velké skoky ve velikosti (oko musí přeostřovat) a slabý kontrast, ve hrách vyhrocený tím, že text leží přes pohyblivé pozadí. Není to kosmetika: hůř čitelná instrukce prokazatelně zhoršuje výkon v úkolu, který popisuje.

Kde se s tím potkáš: [Typografie](teorie/typografie.md) · [První dojem](teorie/prvni-dojem.md)

### Konsonance

**Dojem klidu a souznění při současném znění tónů; opak disonance.**

Vzniká, když se alikvóty tónů dobře zarovnají a málo perou — proto oktáva a kvinta znějí stabilně. Konsonance je „domov", ke kterému se napětí disonance vrací.

Kde se s tím potkáš: [Fyzika souzvuku](hudba/fyzika-souzvuku.md)

### Kontrapunkt

**Skládání nezávislých melodií, které fungují zároveň (counterpoint).**

Horizontální dovednost (proti vertikální harmonii). Podle Inside the Score nejčastěji chybějící dovednost, která odděluje profíky od amatérů — i mírné zvládnutí povýší melodickou a texturní vyspělost hudby.

Kde se s tím potkáš: [Cesta skladatele: sedm pilířů](hudba/cesta-skladatele.md)

### Kumulativní výhoda

**Kdo je vidět, je víc vidět — úspěch se sám zesiluje bez ohledu na kvalitu.**

Známé i jako Matoušův efekt nebo „bohatí bohatnou". Na Steamu funguje mechanicky: algoritmus doporučuje to, co se prodává, a co se doporučuje, se prodává. Je to jeden ze tří mechanismů, které vedou k mocninnému rozdělení výsledků, a zároveň důvod, proč je start hry disproporčně důležitý oproti její dlouhodobé kvalitě.

Kde se s tím potkáš: [Data o úspěchu](teorie/data-o-uspechu.md#extremistan-tri-mechanismy-ktere-vedou-ke-stejne-strategii) · [Co prodává](teorie/co-prodava.md)

### Kvaternion

**Reprezentace 3D rotace čtyřmi čísly: imunní vůči gimbal locku a hladce interpolovatelná (slerp) — výměnou za nulovou intuici.**

Rozšíření komplexních čísel o tři imaginární složky; násobení skládá rotace. V UE je to typ Quat — engine v něm rotace drží interně, zatímco Rotator (Eulerovy úhly) slouží UI. Chápat přesné vnitřnosti netřeba; vědět, kdy sáhnout po slerpu, ano.

Kde se s tím potkáš: [Matematika pro gamedev](teorie/matematika-pro-gamedev.md)

### Jump scare

**Úleková špička hororu: náhlý audiovizuální úder, který vybije nasbírané napětí.**

Rozpočet žánru: hlasité 2–3 na hodinu, tiché (leknutí bez plného vybití tenze) podle potřeby. Nejlepší scary jsou mini-dramaturgie — oči ve tmě, dohrávající písnička, natažené ticho, teprve pak úder — a monstrum smí jen implikovat.

Kde se s tím potkáš: [Horor design](teorie/horor-design.md)

### Landmark

**Výrazný orientační bod levelu — věž, světlo, brána — ke kterému se vztahuje hráčova navigace i kompozice prostoru.**

V postupu „landmark napřed": startovní bod hráče a hlavní point of interest jsou první dvě rozhodnutí návrhu levelu, ještě před blockoutem — dávají měřítko, směr a osu pro pacing a vertikalitu. Cestou k landmarku pak vedou funneling (zúžení prostoru), leading lines a světlo.

Kde se s tím potkáš: [Prostor a hranice](teorie/prostor-a-hranice.md)

### Landscape

**Klasický terénní systém UE: „papírově tenká" plocha deformovaná height mapou — jen nahoru a dolů, žádné převisy.**

Pořád produkční volba, dokud Mesh Terrain nedozraje. Klíčové nástroje: sculpt/paint módy s edit layers, copy/paste gizmo (patche a import height map do zón), paint vrstvy jako data pro PCG, Nanite displacement pro reliéf z materiálu. Limity řeší nástupce Mesh Terrain (skutečná mesh geometrie).

Kde se s tím potkáš: [Landscape tipy](praxe/landscape-tipy.md) · [Mesh Terrain](praxe/mesh-terrain.md)

### Layered Blend Per Bone

**Anim uzel míchající dvě pózy od zadané kosti nahoru — základ vrstvení horního těla přes locomotion.**

V layer setupu se uvádí jméno kosti (přesný spelling!), od které blend působí — typicky clavicle nebo spine; blend depth a weight ladí měkkost přechodu. Nad Motion Matchingem dvě klasická použití: montáž útoku do horního těla (s Blend Poses by Bool) a overlay póza držené zbraně (single frame animace).

Kde se s tím potkáš: [GASP](praxe/gasp.md) · [Systémy nad MM](praxe/mm-systemy.md)

### Layered move

**Dočasný zdroj pohybu v Moveru — nástupce root motion sources: dash, naváděný útok, skok.**

Na rozdíl od movement módů jich může běžet víc naráz; každý generuje rychlost, mixují se nebo přepisují podle priority a výsledek vykoná aktivní mód. Animation root motion přichází jako obyčejný layered move — a proto jde konečně míchat s řízeným pohybem (v CMC platilo buď–anebo).

Kde se s tím potkáš: [Mover](praxe/mover.md)

### Layering

**Vrstvení více zvuků hrajících tutéž linku, aby zněla velce a plně.**

Tatáž melodie na jednom tenkém synthu je „skoro ono"; teprve několik vrstev (piano + bright lead + bas) dá plný zvuk. Melodie a akordy jsou kostra, dojem dělá aranž a vrstvení.

Kde se s tím potkáš: [Jak psát melodie](hudba/melodie.md)

### Leitmotiv

**Melodie svázaná s postavou, místem nebo věcí, která se vrací a mění podle scény.**

Motiv s přiřazeným významem: téma postavy se proměňuje podle nálady, ale zůstává rozpoznatelné. Propojuje soundtrack v jeden svět — Jaies zapracuje téma postavy i do hudby oblasti, kterou postava obývá. Přímá aplikace práce s motivem.

Kde se s tím potkáš: [Tvorba herního soundtracku](hudba/tvorba-soundtracku.md) · [Jak psát melodie](hudba/melodie.md)

### Lerp

**Lineární interpolace A + (B − A)·t — nejlevnější kouzlo enginu: plynulý přechod čehokoli, co jde vyjádřit čísly.**

A a B může být pozice, scale, barva i délka health baru. Strohost lineárního průběhu opravují shaping functions (smoothstep a spol.) aplikované na parametr t; barevné přechody vylepší interpolace v jiném prostoru (HSV, Lab) místo RGB.

Kde se s tím potkáš: [Matematika pro gamedev](teorie/matematika-pro-gamedev.md)

### Level instance

**Znovupoužitelný sub-level: skupina aktorů (klidně s blueprinty) zabalená do jednoho celku, který se dá rozmístit vícekrát.**

Vytváří se výběrem aktorů → right-click → Level → Create Level Instance; sourozenec Packed Level Actor dělá totéž jen pro static meshe a převádí je na instance (jeden draw call, ideální pro modulární budovy). Editace se propíše všem kopiím — varianta se dělá z duplikátu. Vzor „dům z Warzone": jednou postavit, šestkrát položit.

Kde se s tím potkáš: [Optimalizace scény](praxe/optimalizace.md)

### Level streaming

**Načítání a uvolňování částí světa za běhu — místo výměny celého levelu přes Open Level.**

Persistent level je rám; sub-levely (`Window → Levels`) se nahrávají přes Level Streaming Volumes nebo uzly Load/Unload Streaming Level, asynchronně — hra mezitím žije. Detaily: *loaded* ≠ *visible* (neviditelný level drží paměť); streaming volume musí ležet v persistent levelu; persistent nejde unloadnout (trik: veškerý obsah do sub-levelu „Base"). Pro open worldy je nástupcem World Partition.

Kde se s tím potkáš: [Levely a streaming](praxe/levely-a-streaming.md)

### LFO

**Pomalý oscilátor (low-frequency oscillator), který za tebe donekonečna otáčí zvoleným knobem.**

Zatímco obálka otočí knobem jednou (při notě), LFO ho otáčí pořád dokola — vibrato, wobble, pohyb filtru. Modulace (obálka i LFO) otevírá nekonečno zvuků z jednoho patche.

Kde se s tím potkáš: [Syntéza zvuku od nuly](hudba/synteza-zvuku.md)

### Liminální prostor

**Veřejný prostor zbavený lidí a účelu — mall, škola, letiště v prázdnu; děsí tím, že je skoro normální.**

Repetitivní vzory, dlouhé prázdné chodby, známá infrastruktura bez života: mozek hlásí „tohle znám" i „tady něco nesedí" zároveň, příbuzné uncanny valley. Hororová scéna z něj udělala celý subžánr.

Kde se s tím potkáš: [Horor design](teorie/horor-design.md)

### Line Trace

**Raycast — neviditelný paprsek vyslaný z bodu daným směrem, který vrátí první (nebo všechny) kolize na dráze.**

Základní dotazovací nástroj: „na co koukám?", „stojím na zemi?", „vidí mě stráž?". Samotný trace je levný; problém je vzorec „trace každý frame v Event Ticku" — polling tam, kde stačí reagovat na změny. Alternativou pro detekci „něco vstoupilo do zóny" jsou overlap eventy kolizních komponent.

Kde se s tím potkáš: [Interakce bez Event Ticku](praxe/interakce-bez-event-ticku.md)

### Linear grammar

**Gramatika PCG nástrojů: string symbolů, který určuje rytmus modulů podél splinu.**

Modulům (meshům) přiřadíš symboly a zapíšeš vzor: `[A,B]` je sekvence, číslo přesný počet (`A3`, `[A,B]2`), `*` opakuje vzor do vyplnění délky splinu a `+` navíc moduly roztáhne, aby délka vyšla přesně. Plot s brankami nebo zeď se sloupky je pak jeden řádek textu místo ručního skládání dílců.

Kde se s tím potkáš: [PCG základy](praxe/pcg-zaklady.md)

### Linked anim graph

**Samostatný animační graf připojený do AnimBP jako modul — s tagem, přes který na něj komponenty sáhnou zvenčí.**

Vzor z traversal/cover systémů nad GASP: parkour či overlay logika žije ve vlastním grafu, hlavní AnimBP ji jen linkuje; tag („parkour", „overlay") umožňuje actor komponentám najít anim instanci a řídit ji. Drží AnimBP čitelný a systémy přenositelné mezi projekty.

Kde se s tím potkáš: [Systémy nad MM](praxe/mm-systemy.md)

### Line of action

**Pomyslná linie procházející pózou postavy; udává, kam pohyb směřuje.**

Chceš ji rovnou a čitelnou, s částmi těla, které ji následují — zlomená nebo komplikovaná linie ničí účel pózy a pohyb se hůř čte. Spolu s těžištěm (musí padat nad chodidla, pokud zrovna nechceš ukázat ztrátu rovnováhy) je to základ, který stojí před vším ostatním: animace je série póz, takže špatná póza se nedá zachránit časováním.

Kde se s tím potkáš: [Art specializace: animace](teorie/art-specializace.md)

### Live Link

**Systém pro streamování dat do enginu (mocap, kamery, DCC nástroje) — a od 5.8 s Live Link Hubem i offline zpracování videa.**

Pro markerless mocap: Live Link Hub → Capture Manager → Mono Video Ingest převede MP4 na capture data, které umí číst MetaHuman Performance. Živá cesta (telefon jako facial kamera, mocap obleky) používá tentýž systém — proto to jméno.

Kde se s tím potkáš: [Animační nástroje](praxe/animace-nastroje.md)

### Locomotor

**Control Rig uzel pro procedurální chůzi: počítá došlapy dynamicky podle pohybu, žádné animační klipy.**

Foot sets definují končetiny (fázové offsety = charakter chůze — pavouk 0/0,25/0,5/0,75), pelvis settings usazení těla, stepping výšku a tempo kroků; do kostí to propíše Full Body IK s effectory na špičkách. Ladí se collision radius per noha a max collision height. Experimental plugin; Epic jím demí mecha v GASP.

Kde se s tím potkáš: [Animační nástroje](praxe/animace-nastroje.md) · [GASP](praxe/gasp.md)

### Locus of control

**Kde člověk hledá řídicí sílu svého jednání: uvnitř (sám se rozhoduju), nebo venku (čekám, až mě někdo dotlačí).**

Pojem z psychologie: výchova, kde motivaci vždy dodával někdo zvenčí, pěstuje externí locus — a v dospělosti se čeká na dalšího „dozorce". Tvůrčí dospělost znamená převzít roli disciplinující figury sám nad sebou; vnější závazky (ukázka k datu) jsou legitimní berlička.

Kde se s tím potkáš: [Produktivita](teorie/produktivita.md)

### Look ahead

**Předsazení kamery směrem, kam se hráč dívá nebo poletí — kamera sleduje pozornost, ne sprite.**

Horizontálně podle směru pohybu (v obousměrných hrách se přepíná), vertikálně podle fáze skoku: na zemi nad hlavu (plánuješ skok), v apexu na tělo, při pádu pod nohy. Vedlejší efekty (bump při dopadu) bývají zadarmo a stojí za ponechání.

Kde se s tím potkáš: [Kamera](teorie/kamera.md)

### Loose coupling

**Princip: třídy na sobě závisejí co nejméně — komunikují přes smlouvy (interfacy) a eventy, ne přes tvrdé reference.**

Diagnóza vazeb: Reference Viewer („proč ability závisí na třídě nepřítele?"). Léky: interface místo castu (damageable — „poskytneš-li Take Damage, zavolám ji"), mediátor mezi systémy (event subsystem mezi gameplayem a UI), broadcast kanály. Odměna: systémy jdou měnit a nahrazovat nezávisle — definice škálovatelnosti.

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md) · [Komunikace Blueprintů](praxe/komunikace-blueprintu.md)

### Low-fi prototyp

**Prototyp schválně nízké kvality — náčrt na papíře, čmáranice, hrubá animace konceptu — vytvořený za minuty.**

Jeho supersíla je psychologická: do vypiplaného dema se kritikům tluče těžko, ale náčrt za pět minut nikoho nesvazuje — dostaneš syrový názor na *myšlenku*, dokud se dá směr měnit zadarmo. Protějšek high-fi prototypu (funkční hratelné kostry), který je dražší a láká k připoutání. Srovnej s grayboxem: i tam jde o levné testování, ale mechaniky, ne nápadu.

Kde se s tím potkáš: [Start projektu](teorie/jak-zacit.md) · [Prototypování](teorie/prototypovani.md)

### Low-pass filtr

**Filtr propouštějící nízké frekvence a ubírající vysoké (low-pass filter).**

Základní nástroj subtraktivní syntézy: z bohaté vlny „ořízne" výšky. Libovolná vlna v nízké oktávě protažená úzkým low-pass filtrem dá bas.

Kde se s tím potkáš: [Syntéza zvuku od nuly](hudba/synteza-zvuku.md)

### Ludonarativní disonance

**Nesoulad mezi tím, co hra říká příběhem, a tím, co odměňuje gameplayem (Hocking o BioShocku, 2007).**

Sympatický hrdina cutscén vyvraždí v gameplayi stovky lidí. Není inherentně špatná: humor (sbírky zelí ve vážném Skyrimu) i identita hry (Cult of the Lamb: roztomilé + temné) na disonanci stojí. Vadí, když podrývá pointu, kterou hra vážně míní — a cítí ji každý jinak.

Kde se s tím potkáš: [Ludotematický soulad](teorie/ludonarativni-soulad.md)

### Ludus a paidia

**Cailloisovo spektrum hry: ludus = hra podle přísných pravidel, paidia = volné blbnutí bez cíle.**

Videohry dnes potřebují obojí — když hra působí holá, má často moc ludus a málo paidia. Expresivní mechaniky (emoty, hlouposti bez užitku) jsou paidia vrstva nad pravidly. Od téhož autora pochází i čtveřice agon/alea/mimicry/ilinx.

Kde se s tím potkáš: [Systémy a mechaniky](teorie/systemy-a-mechaniky.md) · [Zábava: taxonomie a pilíře](teorie/zabava.md)

### MAYA

**Most Advanced Yet Acceptable: nejpokročilejší varianta, kterou publikum ještě přijme.**

Princip z průmyslového designu, který se dobře hodí na volbu míry inovace ve hře — obvyklé doporučení zní, že hra má být zhruba z třetiny nová a ze zbytku srozumitelně žánrová. Chrání před dvěma extrémy: klonem, který nemá důvod existovat, a hrou tak originální, že jí nikdo nerozumí (viz hook a anchor).

Kde se s tím potkáš: [Co prodává: hraj hry jako profesní povinnost](teorie/co-prodava.md) · [Nápad](teorie/napad.md)

### Map (dictionary)

**Datová struktura klíč → hodnota: místo „co je na indexu 3" se ptáš „kolik stojí Big Mac".**

Klíč je čitelný a smysluplný; přidání a úprava mají stejnou syntax (nový klíč přidá, existující přepíše), klíč musí sedět přesně (překlep = nový klíč = tichý bug) a nesmí být měnitelný. V Blueprintech je to node Map; příbuzné jsou Data Table s Row Name jako klíčem.

Kde se s tím potkáš: [Programátorské myšlení](teorie/programatorske-mysleni.md) · [Ukládání](praxe/ukladani.md)

### Marching cubes

**Algoritmus (1987), který z 3D skalárního pole vyrobí mesh: 8 sousedů = krychle = 256 případů s předpočítanými polygony.**

Původně pro vizualizaci CT/MRI; dnes základ voxelových terénů, deformovatelných jeskyní a metaballů. Hodnoty nad/pod prahem čte jako bity 8bitového čísla a „pochoduje" polem, dokud nevyskládá celý povrch.

Kde se s tím potkáš: [Algoritmy, které stojí za to znát](teorie/algoritmy-prehled.md) · [Mesh Terrain (UE 5.8)](praxe/mesh-terrain.md)

### Market research

**Průzkum trhu před rozhodnutím o hře: výdělky žánrů, tagy, recenze konkurence, benchmarky.**

První krok k objektivitě proti zamilovanosti do vlastního nápadu. Prakticky: Steamové roční žebříčky, SteamDB, Gamalytic/VG Insights, benchmarky Chrise Zukowského; okno posledních ~3 let (starší data lžou) a medián či spodních 25–30 % výdělků, nikdy průměr. Nejcennější levný zdroj: negativní recenze konkurence — seznam bolestí, proti kterým můžeš designovat.

Kde se s tím potkáš: [Idea iceberg](teorie/rady-z-praxe.md) · [Nápad: yoink & twist](teorie/napad.md)

### Markovův řetěz

**Stavy + pravděpodobnosti přechodů + memoryless vlastnost: pro predikci dalšího kroku stačí současný stav, historie je fuk.**

Markov jím dokázal, že i závislé události poslouchají zákon velkých čísel. Sedí uvnitř PageRanku, Monte Carlo simulací i prediktivního textu — a ve hrách v každém stavovém stroji s pravděpodobnostními přechody, generátoru počasí či pity systému dropů.

Kde se s tím potkáš: [Markovovy řetězce a Monte Carlo](teorie/markovovy-retezce.md)

### Mass Entity

**ECS framework UE pro simulaci tisíců entit — davy, doprava; pohání City Sample i MetaHuman Crowd.**

Entity nejsou actory: data žijí ve fragmentech zpracovávaných hromadně, proto škálování na tisíce NPC s navigací a vyhýbáním. Pro viditelnost se kombinuje s instancovanými meshi a streamováním plných actorů u kamery.

Kde se s tím potkáš: [MetaHuman v praxi](praxe/metahuman.md)

### Material function

**Znovupoužitelný blok materiálové logiky — funkce, kterou vložíš do libovolného materiálu v projektu.**

Se vstupem a výstupem typu material attributes funguje jako vrstva: materiál postavy → funkce (decay, sníh, mokro) → výstup. Uvnitř Get/Set Material Attributes upraví jen vybrané atributy, zbytek proteče beze změny. Jedna funkce pro celý projekt znamená i opravy na jednom místě.

Kde se s tím potkáš: [Materiály](praxe/materialy.md)

### Matice

**Blok čísel čtený jako lineární transformace: sloupce říkají, kam se přesunou osy prostoru.**

Identity nedělá nic, diagonála škáluje osy, záporná čísla zrcadlí, rotační matice je bod na jednotkové kružnici. Násobení matic = skládání transformací do jedné. Homogenní souřadnice (4×4 v enginech) propašují do matice i translaci — proto je transform jedna matice.

Kde se s tím potkáš: [Lineární algebra vizuálně](teorie/linearni-algebra-vizualne.md) · [Matematika pro gamedev](teorie/matematika-pro-gamedev.md)

### McNamarův klam

**Chyba rozhodování, kdy se to, co jde snadno změřit, prohlásí za to jediné důležité.**

Pojmenováno po ministru obrany, který během války ve Vietnamu řídil postup podle počtu zabitých nepřátel — metriky rostly, válka se prohrávala. V gamedevu se projevuje sledováním wishlistů, zhlédnutí nebo počtu recenzí namísto obtížně měřitelných věcí, jako je to, jestli hra někoho baví a jestli ji doporučí dál.

Kde se s tím potkáš: [Data o úspěchu](teorie/data-o-uspechu.md#mcnamaruv-klam-co-se-snadno-meri-neni-totez-co-dulezite) · [Playtesting](teorie/playtesting.md)

### MCP

**Model Context Protocol — standard, kterým AI agent (Claude Code, Codex, Gemini…) mluví s nástroji; od 5.8 nativně v Unrealu.**

Trojice pluginů Unreal MCP + Terminal + Editor Toolset dá agentovi kontext projektu a kontrolu nad editorem: blueprinty, materiály, PCG, level design. Config per agent generuje konzolový příkaz (.mcp.json). Stejný protokol propojuje agenty s Blenderem i ComfyUI. Zlaté pravidlo: obecný prompt = obecný výsledek — rozepsaná logika a detailní zadání dělají rozdíl.

Kde se s tím potkáš: [AI agenti: Claude Code a MCP](praxe/claude-code-ue.md)

### MDA framework

**Mechanics → Dynamics → Aesthetics: mechaniky se dějí v kódu, dynamika v akcích hráče, estetika v jeho pocitech.**

Akademický rámec (2004) pro analýzu mechanik: designér sahá jen na mechaniky a změny kaskádují — málo munice → opatrné chování → strach. Půjčuješ-li mechaniku z jiné hry, MDA odpovídá na otázku, PROČ tam funguje a jestli u tebe vyrobí tytéž pocity.

Kde se s tím potkáš: [Základy designu: MDA](teorie/zaklady.md) · [Systémy a mechaniky](teorie/systemy-a-mechaniky.md)

### Mechanika

**Jednotka gameplaye složená z pravidel: sloveso hráče (skoč, seber, unikni) — nástroj, kterým se působí na herní svět.**

Pravidla jsou logika („když tohle, pak tohle"), mechaniky z nich skládají interakce a systémy jsou větší celky, se kterými hráč skrze mechaniky jedná. Stejné sloveso s jinými pravidly je jiný pocit — a pocit jádrové mechaniky je charakter hry.

Kde se s tím potkáš: [Systémy a mechaniky](teorie/systemy-a-mechaniky.md) · [Rejstřík: Core loop](rejstrik.md#core-loop)

### Mediator pattern

**Prostředník, přes kterého aktéři komunikují místo napřímo — každý pak závisí jen na něm.**

Analogie je řízení letového provozu: letadla se nedomlouvají mezi sebou, mluví s věží. V UE typicky aktér v levelu (combat manager koordinující, kdo smí útočit) nebo objekt na Game State (event manager rozesílající události). Kombinuje se s rozhraními: mediátor definuje, co od aktérů potřebuje, a implementaci nechá na nich.

Kde se s tím potkáš: [Komunikace Blueprintů](praxe/komunikace-blueprintu.md#mediator-koordinator-uprostred-a-event-manager-v-game-state) · [Design patterns](teorie/design-patterns.md#tri-rodiny-vzoru-tvorba-struktura-chovani)

### MegaLights

**Systém UE od 5.5, který zlevňuje scény s velkým počtem stínících světel.**

Místo aby každé světlo platilo plnou cenu za stíny a výpočet, MegaLights je vzorkuje sdíleně, takže se desítky až stovky dynamických světel stanou realistickou volbou. Pro workflow, kde se scéna maluje z mnoha malých zdrojů místo jednoho směrového světla, je to zásadní rozdíl.

Kde se s tím potkáš: [Osvětlení: malovat světlem](praxe/osvetleni.md#malovat-svetlem-scena-slozena-z-falesnych-svetel)

### Mesh distance field

**Předpočítané pole vzdáleností k nejbližšímu povrchu meshe — shader se může kdykoli zeptat „jak daleko je geometrie?".**

Zapíná se v project settings, kontroluje vizualizačním viewmodem. Uzel Distance to Nearest Surface na něm staví efekty obtékající objekty: mlha plazící se po zdech, sníh u stěn, ohořelé okraje. Stejná data pohání distance field stíny a AO.

Kde se s tím potkáš: [Osvětlení](praxe/osvetleni.md)

### MetaHuman

**Epicův systém fotorealistických postav: creator, rig obličeje i těla a nástroje (Animator, Performance) kolem.**

Od 5.8 žije tvorba přímo v enginu (MetaHuman Creator plugin; Core Data při instalaci enginu). MetaHuman Performance asset zpracuje capture data na animaci — s Body Trackingem tělo i obličej (blend shapes). První rig vyžaduje potvrzení licence na webu. Výstup jde retargetovat na libovolný skeleton — MetaHuman může sloužit jen jako mocap prostředník.

Kde se s tím potkáš: [MetaHuman v praxi](praxe/metahuman.md) · [Animační nástroje](praxe/animace-nastroje.md) · [GASP](praxe/gasp.md)

### MetaSounds

**Grafový audio systém UE5 — nástupce Sound Cues: procedurální zvuk s parametry měnitelnými za běhu.**

Graf jako AnimBP: wave playery, randomizace, matematika nad audiem. Vstupní parametry (float, trigger…) se nastavují přes audio komponentu — `Spawn Sound at Location` ji vrací (Play Sound ne!), pak `Set Float Parameter`. Typické použití: jeden asset kroků, kde rychlost postavy řídí hlasitost i pitch.

Kde se s tím potkáš: [Kroky](praxe/footsteps.md)

### Mip mapa

**Řetěz zmenšených kopií textury (4K → 2K → 1K → …), ze kterého GPU vybírá podle vzdálenosti a velikosti na obrazovce.**

Mip bias výběr posouvá: +1 = poloviční hrana (čtvrtina paměti), −1 = detailnější. Ladí se per textura (LOD Bias v editoru), per materiál (Mip Value Mode = MipBias) nebo hromadně přes property matrix. Prakticky: base color snese bias klidně +5 — dojem detailu nese normal mapa; a při DLSS/upscalingu je potřeba bias kompenzovat záporně.

Kde se s tím potkáš: [Textury a DLSS](praxe/textury-a-dlss.md)

### Mód hry

**Struktura hraní přes sezení: roguelike, metroidvania, souls-like — neříká nic o tom, co držíš v rukou.**

Prostřední patro pyramidy žánr → mód → nálada: žánr je moment-to-moment činnost (platformer), mód je důvod pokračovat (permadeath, mapa, corpse run), nálada jsou vibes (cozy, horor). Spelunky je platformer v roguelike módu — při jednom hraní mód ani nepoznáš.

Kde se s tím potkáš: [Žánry očima designéra](teorie/zanry.md)

### Moderovaný playtest

**Test, u kterého sedíš: díváš se, jak člověk hraje, mlčíš — a ptáš se přesně v místě tření.**

Setup: „máš 30 minut? chci se dívat, jak to hraješ" — osobně nebo videohovor se sdílenou obrazovkou. Pravidla: think-aloud (komentuj myšlenky nahlas), nezasahovat ani u trápení s tutoriálem, standardní otázky na konec. Protiváha: sledovaný hráč hraje jinak, proto se doplňuje širokým testem bez tebe.

Kde se s tím potkáš: [Playtesting](teorie/playtesting.md)

### Modifier stack

**Vrstvené nedestruktivní úpravy: každá operace zůstává živým objektem, který lze dodatečně měnit, přesouvat, přeskládat nebo smazat.**

Filozofie „scéna je recept, ne výsledek" — známá z Houdini, Geometry Nodes či modifierů v Blenderu. Mesh Terrain na ní staví celé tvarování: brush, noise, spline, texture, mesh, boolean a remesh modifiery se skládají podle priorit a blend módů. Cena: recept se musí přepočítávat (build cost, FPS propady při editaci). Výhoda: žádné rozhodnutí není konečné.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Monte Carlo metoda

**Neumíš to spočítat? Nasimuluj tisíce náhodných běhů a přečti odpověď z histogramu.**

Zrozena z Ulamova Solitaire a neutronů Manhattan Projectu (s von Neumannem a Markovovými řetězy uvnitř), pojmenovaná po kasinu. Aproximuje řešení, která analyticky neexistují — za cenu výpočetního času a statistické jistoty. Pro designéra: balanc ekonomiky a dropů simulací místo tabulky průměrů.

Kde se s tím potkáš: [Markovovy řetězce a Monte Carlo](teorie/markovovy-retezce.md) · [Prototypování](teorie/prototypovani.md)

### Moodboard

**Sbírka referencí, která ukazuje tón a směr dřív, než vznikne první vlastní kresba.**

Dělá se před kreslením ze dvou důvodů: dá týmu možnost zkorigovat směr s minimem odvedené práce, a nutí autora směr pojmenovat. Smí obsahovat krátké deskriptory (pillars). Příliš obecný nebo roztříštěný moodboard je varovný signál — vede ke zmatku a pivotům později, protože ve skutečnosti žádný směr nedeklaroval.

Kde se s tím potkáš: [Herní art: concept art](teorie/art-pipeline.md) · [GDD](teorie/gdd.md)

### Motion matching

**Dotazový systém výběru animací: každý frame hledá v databázi pózu, která nejlépe naváže na trajektorii a aktuální pózu.**

Nahrazuje state machines — žádné stavy a přechody, jen databáze (PSD), schema (co a s jakou vahou měřit) a cena kandidátů; vítězí nejnižší. Stavební kameny: trajektorie (predikce pohybu), pose history (odkud jdu), chooser (která databáze), continuing pose (koho porazit). Od 5.4 v UE, showcase je Game Animation Sample; Fortnite s ním shipuje na všech platformách. Nepotřebuje stovky animací — viz sparse set.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md) · [Systémy nad MM](praxe/mm-systemy.md)

### Motion Warping

**Ohnutí root motion animace tak, aby trefila cílový transform — notify state v montáži + warp target za běhu.**

Základ traversalu a interakcí: Motion Matching vybere nejbližší vhodnou animaci a warp uvnitř svého okna dožene zbytkovou chybu pozice i rotace. Precomputed warp (5.7, z Witcher dema) přidává oddělené křivky pro translaci a rotaci (posun na začátku, dotočení na konci) a steering, který dráhu k cíli ohne do přirozeného oblouku.

Kde se s tím potkáš: [GASP](praxe/gasp.md) · [Systémy nad MM](praxe/mm-systemy.md)

### Motiv

**Krátká, zapamatovatelná dvou- až pětitónová buňka uvnitř melodie.**

Skvělý odrazový můstek: motiv se dá opakovat, posunout výš/níž, obrátit, zrychlit. Když melodické dovednosti nestačí, „kraď sám od sebe" — z jediného motivu vytěžíš půl skladby a výsledek zůstane soudržný. Leitmotiv je motiv přiřazený postavě či místu.

Kde se s tím potkáš: [Jak psát melodie](hudba/melodie.md)

### Movement Mode

**Modulární objekt Moveru definující jeden režim pohybu (walking, falling, slide…) — vyměnitelný a rozšiřitelný i v Blueprintu.**

Proti CMC, kde režimy byly zadrátované v komponentě, si módy skládáš: child mód přepíše generate-move funkci, zavolá parenta a upraví parametry (sprint = přepiš max speed podle custom input structu). Společná data módů řeší shared settings; blueprint proměnné módu se objeví v details panelu komponenty a replikují se samy.

Kde se s tím potkáš: [Mover](praxe/mover.md) · [GASP](praxe/gasp.md)

### Mover

**Nová pohybová komponenta UE — nástupce Character Movement Componentu postavený na replikaci vstupů a modulárních movement módech.**

Klíčové rozdíly proti CMC: replikují se inputy (i vlastní blueprint structy) místo výsledků pohybu, rotace je zcela volná (spin transitions, twin-stick intent) a predikce trajektorie pro Motion Matching spouští skutečný simulační kód včetně custom módů. V GASP od 5.7 výchozí; CMC postava zůstává jako legacy. Pozor na frame zpoždění vstupu (network prediction tiká před pawnem) — kameru a AnimBP krmit post-sim hodnotami.

Kde se s tím potkáš: [Mover](praxe/mover.md) · [GASP](praxe/gasp.md)

### Multithreading

**Rozdělení práce na víc vláken, aby dlouhý výpočet neblokoval běh hry.**

Kód hry běží standardně na jediném hlavním vlákně — pohyb, stavové automaty i kolize. Jedna drahá operace tam zastaví všechno ostatní. Vlákna navíc se hodí na úkoly typu „pošli data, vrať se s výsledkem": hledání cesty, načítání assetů, procedurální generování. Cena je omezení: mimo hlavní vlákno se na aktéry ve scéně obvykle sahat nesmí.

Kde se s tím potkáš: [Optimalizace: co blokuje hlavní vlákno](praxe/optimalizace.md#druha-osa-optimalizace-co-blokuje-hlavni-vlakno) · [Rejstřík: race condition](#race-condition)

### MVP

**Minimum Viable Product: nejmenší verze produktu, která doručí jádro hodnoty — jen core loop, žádný dezert.**

Ve hrách: přihlas se → udělej věc → viz výsledek; leaderboardy, dark mode a marketplace počkají. Smysl MVP není ošidit kvalitu, ale co nejdřív ověřit, že jádro funguje a někoho zajímá — příbuzný gameplay prototypu a vertical slice.

Kde se s tím potkáš: [Jak se učit kódovat](teorie/jak-se-ucit-kodovat.md) · [Prototypování](teorie/prototypovani.md) · [GDD](teorie/gdd.md)

### Nanite

**Virtualizovaná geometrie UE5: engine dynamicky přizpůsobuje detail meshů vzdálenosti a velikosti na obrazovce.**

Prakticky ruší ruční LOD řetězce — mesh se subdivuje a redukuje průběžně, po clusterech, podle toho, co kamera reálně vidí. Mesh Terrain je na Nanite postavený; právě adaptivní subdivize je jeden z důvodů, proč zvládá větší plochy než starý Landscape. Po editaci terénu se Nanite reprezentace přestavuje — proto FPS propad během úprav a krátký build po odkliknutí.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Narrative design

**Návrh vyprávění integrovaný s herním designem — protiklad modelu „designér nechá díry na cutscény a spisovatel je dopíše".**

Pojem posledních ~20 let; zahrnuje volbu typu protagonisty, směr dialogů, rejstříky řeči i vyprávěcí prostředky, které mají jen hry (flavor texty, prostředí, mechaniky). Pro malé týmy začíná třemi branami: kolik implementace vyprávění přinese, jaká je tvá spisovatelská praxe a jaké příběhy ti nabízejí tvoje nástroje.

Kde se s tím potkáš: [Příběh a postavy](teorie/pribeh-a-postavy.md)

### Nav Mesh

**Navigační síť: oblast, ve které AI umí počítat cesty — bez ní se žádné AI MoveTo nepohne.**

Do levelu se přidává jako Nav Mesh Bounds Volume; klávesa P zobrazí zeleně pochozí plochy. Vygenerovaný RecastNavMesh má v Generation nastavení jako Agent Radius (odstup cest od stěn — lék na zasekávání o rohy) nebo výšku kroku. Body pro pohyb dodávají uzly typu Get Random Location in Navigable Radius.

Kde se s tím potkáš: [Základy AI](praxe/ai-zaklady.md) · [State Trees](praxe/state-trees.md)

### Network Prediction

**Generalizovaný rollback framework UE — jedna ze dvou síťových větví Moveru (druhá je Chaos networked physics).**

Klienti posílají jen vstupy s časem simulace; server je bufferuje, konzumuje podle svých hodin a vysílá stav — chyby detekuje a řeší klient. Rollback je „unified": vrací se a přehrává celé okolí naráz, takže korekce bývá jedna. Prakticky: režim interpolated + Sync Inputs for Sim Proxy řeší klepání simulated proxies; pozor na frame zpoždění vstupu (tiká před pawnem).

Kde se s tím potkáš: [Mover](praxe/mover.md) · [GASP](praxe/gasp.md)

### Niagara Data Channel

**Kanál, do kterého gameplay jen zapisuje data (pozice, normála…) a jediný běžící Niagara systém z nich spawnuje částice.**

Řeší nešvar „nový particle systém per událost": sto kroků = sto zápisů do kanálu, ne sto systémů. Emitter čte přes Spawn from Data Channel; typ gameplay boost (5.7) umí při zápisu přepnout, který systém se spawne. NDC referenci ukládej jako system value.

Kde se s tím potkáš: [Kroky](praxe/footsteps.md)

### Niagara Fluids

**Plugin s šablonami fyzikálních simulací — pro interaktivní hladinu šablona Grid 2D SW Particle Collisions.**

2D grid simulace mělké vody: postava a objekty s tagy „collider" (actor i component tag, case-sensitive) dělají vlny. Ladicí trio: Velocity Dissipation (dozvuk vln), Delta Time Multiplier (tempo), Collision Velocity Multiplier (síla vstupu). Od 5.6 totéž zapíná Water Advanced plugin checkboxem (shallow water subsystem).

Kde se s tím potkáš: [Interaktivní voda](praxe/interaktivni-voda.md)

### Normal mapa

**Textura kódující, jak má povrch odrážet světlo — dodá reliéf bez přidání polygonů.**

Vzniká nejčastěji bakem z high-poly modelu na low-poly mesh: detail vysochaný v sochacím programu se promítne do textury. Spolu s height mapou (jak moc části vystupují) a barvou tvoří základní trojici map, ze které se skládá materiál.

Kde se s tím potkáš: [Herní art: character art](teorie/art-pipeline.md) · [Materiály v UE](praxe/materialy.md)

### Normalizace vektoru

**Zmenšení vektoru na délku 1 se zachováním směru: složky vydělíš délkou (Pythagoras — a tedy odmocnina).**

Jednotkové vektory vyžaduje skoro všechno: dot product jako kosinus, osvětlení, raycasty, klouzání po zdi. Právě cena té odmocniny zrodila slavný Quake 3 hack rychlé inverzní odmocniny — dnes ji řeší hardwarová instrukce.

Kde se s tím potkáš: [Matematika pro gamedev](teorie/matematika-pro-gamedev.md)

### Obrat akordu

**Tentýž akord s jiným pořadím tónů — jednu notu posuneš o oktávu.**

Akord zůstane týž, ale zní jinak a přechody mezi akordy sedí líp. Praktický zvyk: nejdřív si odděl basové tóny (o oktávu dolů), pak obracej zbytek, ať neztratíš přehled, co je bas.

Kde se s tím potkáš: [Akordy a harmonie](hudba/akordy-a-harmonie.md)

### Observer pattern

**Objekty se přihlásí k odběru událostí jiného objektu; zdroj při události obvolá odběratele — nikdo nepolluje smyčkou.**

YouTube zvoneček jako architektura: subscribe/unsubscribe u zdroje, notify při události. V UE je to doslova Event Dispatcher (bind/unbind/call). Pozor na event callback hell — událost spouštějící událost spouštějící událost.

Kde se s tím potkáš: [Design patterns](teorie/design-patterns.md) · [Komunikace Blueprintů](praxe/komunikace-blueprintu.md)

### Oktáva

**Vzdálenost mezi tónem a jeho příštím výskytem; frekvenční poměr 2:1.**

Dvanáct tónů se dokola opakuje po oktávách; C o oktávu výš je „totéž C, jen výš" a spolu splývají. Nejkonsonantnější interval — přímý důsledek zarovnání první alikvóty.

Kde se s tím potkáš: [Základy hudební teorie](hudba/hudebni-teorie-zaklady.md)

### Onboarding

**Prvních pár minut, kdy se hráč učí hru — a rozhoduje se, jestli zůstane.**

Nejhůř testovatelná část hry vlastníma očima: svoje hře rozumíš, takže tření nevidíš. Playtesty mívají největší dopad právě tady; a pozor na překlad feedbacku — „hra je moc těžká" v raných minutách často znamená „hráč je zmatený", ne „sniž obtížnost".

Kde se s tím potkáš: [Playtesting](teorie/playtesting.md) · [První dojem](teorie/prvni-dojem.md)

### One-pager

**Pitch na jednu stránku: jeden obrázek, co chci vyrobit a jak vypadá úspěch.**

Nejmenší dokument v rodině GDD — předchází i minimalistickému návrhu; slouží k prvnímu testu, jestli myšlenka unese větu a obrázek. Když one-pager nejde napsat, je pozdě na dokumenty a brzy na engine: nápad ještě není hra.

Kde se s tím potkáš: [GDD](teorie/gdd.md) · [Nápad: test 300 znaků](teorie/napad.md)

### One-way door

**Rozhodnutí drahé nebo nemožné na reverz — dělá se pomalu, vědomě a s jasným vlastníkem; opak je two-way door.**

Metafora dělí rozhodnutí na dva druhy: jednosměrné dveře (žánr hry, veřejné API, volba enginu) chtějí rozmysl, vyslovené premisy a datovaný zápis; obousměrné dveře (mechanika uvnitř žánru, interní refactor) jsou levné experimenty, kde rychlost přebíjí jistotu. Premisy jednosměrného rozhodnutí se znovu otevírají jen v sankcionovaném okně (preprodukce, gate s vertical slicem) — ne pokaždé, když má projekt špatný den. Po gate platí disagree & commit.

Kde se s tím potkáš: [Zápisky: derivační řetěz IZBY](zapisky/derivace-izby.md) · [Zápisky: cut line](zapisky/cut-line.md)

### Orchestrace

**Rozdělení hudby mezi nástroje a jejich smíchání do barvy (orchestration).**

Často to, co odděluje začátečnicky znějící kus od profesionálního — ale má přijít až po zvládnutí melodie, harmonie a kontrapunktu, jinak „orchestruješ prázdno". V herní hudbě obdoba výběru a vrstvení zvuků a sound fontů.

Kde se s tím potkáš: [Cesta skladatele: sedm pilířů](hudba/cesta-skladatele.md)

### Oscilátor

**Zdroj surového zvuku v synthu (oscillator); tvar vlny určuje barvu, a tím alikvóty.**

Sinus (bez alikvót, teplý), obdélník a pila (bohaté na alikvóty), trojúhelník. Unison navrství víc kopií vlny na notu a rozšíří zvuk do sterea.

Kde se s tím potkáš: [Syntéza zvuku od nuly](hudba/synteza-zvuku.md)

### Overdraw

**Tentýž pixel vykreslený vícekrát, protože se geometrie překrývá — tichý zabiják výkonu hustých scén.**

Typicky listí, masky a průhlednost; vizualizuje ho Nanite overdraw view (jasné/bílé plochy = zle). Léčba: redukovat překryvy — voxelizace vzdálené vegetace, plná geometrie místo masek, menší footprint assetů, mazat zakopanou geometrii. Nikdy nebude nula; loví se největší viníci vypínáním spawnerů jednoho po druhém.

Kde se s tím potkáš: [Optimalizace scény](praxe/optimalizace.md) · [PCG vegetace](praxe/pcg-vegetace.md)

### Overlay state

**Enum-řízená vrstva pózy horního těla přes locomotion — drž pistoli, luk nebo pochodeň bez vlastních pohybových animací.**

Vzor z ALS: animation layer s Blend Poses by Enum a per ozbrojený stav Layered Blend Per Bone se single-frame pózou od clavicle nahoru; spodní tělo dál plně řídí Motion Matching. Levná cesta k „postava drží předmět" — skutečný pohyb se zbraní už chce vlastní databáze per stance.

Kde se s tím potkáš: [GASP](praxe/gasp.md)

### Pacing

**Rytmus zážitku: střídání napětí a klidu, akce a ticha, učení a mistrovství v čase.**

Nástroj režie levelů i celých her: scripted events doručují momenty „ve správnou chvíli", struktura levelu střídá zúžení a otevření, obtížnostní křivka střídá novelty a mastery. Špatný pacing má dva póly — monotónní nuda a únavný nonstop tlak; dobrý pacing je dramaturgie.

Kde se s tím potkáš: [Vedení hráče](teorie/vedeni-hrace.md) · [Zábava a flow](teorie/zabava.md)

### Parallax occlusion mapping

**Pixel-shader iluze hloubky: UV se posouvají podle úhlu kamery a height mapy — reliéf bez jediného vertexu navíc.**

Levnější než displacement (žádná tessellace), ale na hraně meshe „uřízne" — siluetu neumí; varianty silhouette POM a screen space displacement to řeší až přepisem hloubky v Z-bufferu. Základ kamenných zdí Crimson Desert i kované brány v TLOU (geometrii má jen rám, ornament je textura). Cena: flickering a wobble při ostrých úhlech kamery.

Kde se s tím potkáš: [Breakdowny](praxe/env-breakdowny.md)

### Pareto distribuce

**Mocninné rozdělení, kde malá menšina případů drží většinu celkové hodnoty.**

Lidově pravidlo 80/20, ale u her je poměr mnohem drastičtější — top procento titulů bere většinu tržeb celé platformy. Zásadní vlastnost: takové rozdělení nemá smysluplný průměr, takže mediánová čísla o prodejích jsou informativnější než průměrná. Viz [Extremistan](#extremistan).

Kde se s tím potkáš: [Data o úspěchu](teorie/data-o-uspechu.md#extremistan-tri-mechanismy-ktere-vedou-ke-stejne-strategii)

### Particle system

**Systém, který z emitteru vystřeluje sprity nebo modely a řídí jejich chování v čase.**

Emitter je neviditelný bod v prostoru; nastavením se z něj stane proud vody reagující na gravitaci i jediný nehybný obrázek. Základní stavební kámen herních VFX, které na rozdíl od filmových musí běžet v reálném čase, a proto se počítají každý snímek.

Kde se s tím potkáš: [Art specializace: VFX](teorie/art-specializace.md)

### Pass by reference

**Předání odkazu na data místo kopie: levné a rychlé, ale změny vidí všichni, kdo sdílejí tentýž originál.**

Jazyky typicky předávají lehké typy (čísla, stringy) hodnotou — kopií — a těžké (pole, mapy, objekty) referencí („sticky note s šipkou na heap"). Mentální test proti bugům: kopíruju, nebo sdílím? V UE běží tahle hranice mezi structy (kopie) a objekty/aktory (reference).

Kde se s tím potkáš: [Programátorské myšlení](teorie/programatorske-mysleni.md) · [Gameplay Tags](praxe/gameplay-tags.md)

### Passing chord

**Průchozí akord vložený mezi dva hlavní, který přemostí jejich přechod.**

Rozbije příliš jednolitý tok — do sestupné, „moc smutné" progrese vloží malé vzepětí nahoru. Krátký, obslužný akord, ne nositel harmonie.

Kde se s tím potkáš: [Akordy a harmonie](hudba/akordy-a-harmonie.md)

### Pawn Sensing

**Jednoduchá smyslová komponenta: kužel zraku + rádius sluchu, viditelné jako gizmo přímo ve viewportu.**

Event On See Pawn pálí každý sensing interval (default 0,5 s), dokud cíl vidí — logiku přechodu proto obal Do Once a ztrátu zájmu řeš Retriggerable Delay delším než interval. Přes zdi s kolizí nevidí. Pro víc smyslů a jemnější kontrolu je nástupce AI Perception.

Kde se s tím potkáš: [AI vnímání](praxe/ai-vnimani.md) · [Základy AI](praxe/ai-zaklady.md)

### PBR

**Physically Based Rendering: materiály popsané fyzikálními vlastnostmi (albedo, roughness, metallic, normal) místo „namalovaného" vzhledu.**

Standard herních materiálů — povrch reaguje na libovolné světlo správně, protože mapy nesou vlastnosti, ne výsledek. Proto dobrá textura nemá zapečené světlo ani stíny z reference (světlo dodá engine) a proto se AI generátorům PBR dogenerování vyplatí. Mapy nemusí sdílet rozlišení: roughness snese polovinu albeda.

Kde se s tím potkáš: [AI assety](praxe/ai-assety.md) · [Textury a DLSS](praxe/textury-a-dlss.md)

### PCG

**Procedural Content Generation — UE framework pro procedurální osazování a generování obsahu světa.**

Grafem definuješ pravidla (sampluj povrch, filtruj podle sklonu či namalované vrstvy, rozmísti stromy s hustotou X) a engine je aplikuje na libovolnou plochu. Typický řetěz: Get Landscape Data / Mesh Partition Query → Surface Sampler → Filter → Transform Points → Spawner. S Mesh Terrainem spolupracuje přes interop plugin — v beta fázi s beta mírou spolehlivosti (spolehlivější je World Ray Hit Query). V 5.7 plugin opustil betu (verze 1.0) a přibyl PCG Mode — kreslení grafů přímo v editoru.

Kde se s tím potkáš: [PCG základy](praxe/pcg-zaklady.md) · [PCG vegetace](praxe/pcg-vegetace.md) · [Instanced Actors](praxe/instanced-actors.md) · [Landscape tipy](praxe/landscape-tipy.md) · [Mesh Terrain](praxe/mesh-terrain.md)

### PCG Mode

**Editorový režim (5.7): PCG grafy se kreslí přímo do světa — splinou, štětcem nebo volumem.**

Aktor s grafem vzniká sám a panel nástroje zrcadlí exposed parametry grafu; vlastní graf zaregistruješ přes Tool Data sekci (compatible tool tags — konvence „zahoď draw, zbytek bez mezer + tool"). Pasti verze 1.0: paint klade body podle vzdálenosti od posledního bodu (ne plochou štětce), guma maže na původních pozicích před transformy a Ctrl+Z ruší celý rozdělaný nástroj.

Kde se s tím potkáš: [PCG základy](praxe/pcg-zaklady.md)

### Pedal tone

**Tón, který zní pod celou progresí a nikdy se nemění (česky prodleva).**

Sjednotí přechody — všechny akordy teď sdílejí aspoň jeden tón — a přidá dojemnost. Když je pak zvuku moc, postav akordy kolem prodlevy: sundej kvinty a nech ji uprostřed.

Kde se s tím potkáš: [Akordy a harmonie](hudba/akordy-a-harmonie.md)

### Persistent level

**Hlavní (rodičovský) level, pod kterým žijí streamované sub-levely — rám, který nikdy neopouštíš.**

Hráč, GameMode i stav přežívají, protože se nikdy nemění celý level — jen sub-levely uvnitř. Nejde unloadnout; chceš-li „vyměnit svět", drž persistent prázdný a veškerý obsah měj v sub-levelech. Objekty, které mají spouštět streaming (volumes, trigger boxy), musí ležet v persistentu — jinak jsou schované spolu s levelem, který mají nahrát.

Kde se s tím potkáš: [Levely a streaming](praxe/levely-a-streaming.md)

### Physical Animation Component

**Komponenta, která motory kloubů táhne simulované kosti k animované póze — základ active ragdollu.**

`Set Skeletal Mesh Component` na BeginPlay, pak `Apply Physical Animation Settings Below` od zvolené kosti (typicky pelvis) s daty orientation/position strength. Síly jdou měnit za běhu — mapování na rychlost těla (letí = tuhý, leží = hadr) je klíčový trik věrohodných ragdollů. Gang Beasts/Human Fall Flat pocit.

Kde se s tím potkáš: [Ragdoll](praxe/ragdoll.md)

### Physical Material

**Asset nesoucí fyzikální vlastnosti povrchu — včetně Surface Type, přes který systémy poznají, po čem stojíš.**

Surface typy se definují v Project Settings (Physical Surface, až 62 + Default). Přiřazení: v materiálu/instanci (všechny meshe s ním automaticky) nebo per-mesh override v levelu. Čtení: hit result → Get Surface Type → Switch on EPhysicalSurface, nebo mapa physical material → data v data assetu. Krom povrchových systémů nese i friction/restituci (gumový míč).

Kde se s tím potkáš: [Kroky](praxe/footsteps.md) · [Interakce s předměty](praxe/interakce-predmety.md)

### Physics Asset

**Fyzikální kostra skeletal meshe: kolizní těla (primitiva per kost) + constrainty (kloubové limity) — bez něj není ragdoll.**

Defaultní assety manekýnů jsou pro ragdoll nedoladěné — limity swing/twist je potřeba ladit (Simulate Selected). Klíčové triky: kinematic body na root kosti (jinak se mesh při simulaci odpojí a nejde číst rychlost), angular drive motory Twist and Swing s výjimkou pelvis, kolize tělo×tělo per dvojice tvarů.

Kde se s tím potkáš: [Ragdoll](praxe/ragdoll.md)

### Physics Constraint

**Kloub mezi dvěma fyzikálními těly: limity pohybu (linear/angular) + volitelné motory, které táhnou k cílové póze.**

Existuje v physics assetu (klouby ragdollu) i jako samostatný actor/komponenta ve scéně (závěs houpačky, pant). Angular limity: swing 1/2 a twist, každý Locked/Limited/Free; drive mode Twist and Swing vrací kloub do přirozené pózy. Motorům se ladí spring (tuhost) a damping.

Kde se s tím potkáš: [Ragdoll](praxe/ragdoll.md) · [Kabely, lana a Physics Control](praxe/lana-kabely.md)

### Physics Control

**Komponenta (plugin, 5.1+), která drží simulovaná tělesa u cíle laditelnou pružinou — „fyzikální, ale ovladatelné".**

`Create Control` + `Create Body Modifier` (bez něj se nastavení neaplikuje); cíl se posouvá přes `Set Control Target Position and Orientation` — pozor, uzel chce auto-generované jméno controlu. Linear Strength = poddajnost, Damping Ratio = dohoupání. Obecnější sourozenec Physical Animation komponenty — funguje na libovolných tělesech.

Kde se s tím potkáš: [Kabely, lana a Physics Control](praxe/lana-kabely.md)

### Pitch deck

**Krátká prezentace hry, která ještě neexistuje — simulace prvního kontaktu zákazníka s nápadem.**

Logika: první krok nákupu hry stejně neobsahuje hraní (trailer, GIF, screenshot) — pitch deck tenhle moment vyrobí bez jediného řádku kódu. Proces: brainstorm → hlasování → u top nápadů popsat smyčku (slabé se rozpadnou samy) → decky → nechat lidi vybírat. Opory: lidé skvěle *vybírají* a mizerně radí, jak zlepšovat; a deck za hodinu se zahazuje bez bolesti — málo vloženého času = málo biasu.

Kde se s tím potkáš: [Idea iceberg: pracuj zpátky](teorie/rady-z-praxe.md) · [Nápad: test 300 znaků](teorie/napad.md)

### Pixel-perfect

**Celočíselné škálování pixel artu, kde každý herní pixel je stejně velká mřížka pixelů monitoru.**

360p se škáluje 3× na 1080p a 4× na 1440p beze zbytku; necelé faktory míchají velikosti pixelů. Dogma s trhlinou: ve slepém testu necelé faktory skoro nikdo nepozná — teoretická vada není automaticky vnímaná vada. Zoom se řeší škálováním finálního renderu, ne kamerou.

Kde se s tím potkáš: [Kamera](teorie/kamera.md)

### Pivot

**Vztažný bod objektu: kolem něj se rotuje a škáluje, k němu se přichytává — na jeho umístění záleží víc, než je vidět.**

Nekonzistentní pivoty mezi asset packy rozbíjejí sockety (každá zbraň sedí v ruce jinak) i navazování dílců. Oprava bez DCC: modeling mode → Transform → Edit Pivot, přijmout a instance v levelu vyměnit. U kyvadel a pák je pivot přímo herní mechanika — bod závěsu určuje dráhu.

Kde se s tím potkáš: [Tipy do editoru](praxe/editor-tipy.md) · [Pasti a mechaniky](praxe/pasti-a-mechaniky.md)

### Pivot (design)

**Změna směru projektu: hra našla těžiště jinde, než byl plán — a plán se přizpůsobí hře.**

Nezaměňovat s pivotem objektu (viz předchozí heslo). Signál bývá „monstrum v rohu": oblast, které se měsíce vyhýbáš, i když technicky zvládnutelná je. Recept: pivotuj k subsystému, který už prokazatelně funguje — a ověř rychlým prototypem („je to jiná hra, ale lepší"). Historická opora: GTA vzniklo pivotem z policejní honičky Race’n’Chase.

Kde se s tím potkáš: [Scope: pivot](teorie/scope.md) · [GDD: dokument není smlouva](teorie/gdd.md)

### Placeholder

**Provizorní asset, který drží místo finálnímu — kostka místo postavy, čmáranice místo ilustrace.**

Nástroj řazení priorit: dokud není jisté, že mechanika žije, každá hodina v grafice je sázka naslepo. Rada z praxe: dělej vlastní placeholdery *záměrně špatně* — hezký provizorní asset svádí k ladění, ošklivý ne. Pozor na licence: placeholdery z cizích her nesmí do ničeho vydaného, včetně dema.

Kde se s tím potkáš: [Start projektu](teorie/jak-zacit.md) · [Prototypování](teorie/prototypovani.md)

### Player State

**Objekt nesoucí data jednoho hráče — inventář, skóre, klíče — nezávisle na jeho pawnovi.**

Pawn může zemřít a respawnout, Player State žije dál (a v multiplayeru se replikuje všem). Vlastní Blueprint verze se registruje v Game Mode. Pravidlo „kde co bydlí": per-hráč data → Player State; session-wide → Game Instance; per-level pravidla → Game Mode.

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md)

### Playtest

**Testování hry skutečnými hráči s cílem získat zpětnou vazbu — o srozumitelnosti, obtížnosti, zábavnosti.**

Nejmenší funkční forma je „ukaž rozdělanou věc kamarádovi": i to je zpětnovazební smyčka, bez které se cvičné hodiny nepočítají. Klíčová dovednost je kalibrace publika podle fáze — shovívavé publikum pro motivaci na začátku, kritické pro růst později. A čti chování, ne slova: playtesteři, kteří si o nový build říkají sami, jsou jiný signál než zdvořilé „je to hezký" (the gap).

Kde se s tím potkáš: [Playtesting](teorie/playtesting.md) · [Vydání hry: demo prodává](teorie/vydani-hry.md) · [Začátky bez zkušeností](teorie/zacatky-bez-zkusenosti.md) · [Idea iceberg: the Gap](teorie/rady-z-praxe.md) · [Postmortem ShantyTown](teorie/postmortem-shantytown.md)

### POM

**Zkratka pro parallax occlusion mapping — viz [Parallax occlusion mapping](#parallax-occlusion-mapping).**

Pixel-shader trik hloubky bez geometrie; v breakdownech a diskusích se běžně používá jen zkratka.

Kde se s tím potkáš: [Breakdowny](praxe/env-breakdowny.md)

### Pose Search Database

**PSD — kolekce animací pro jeden typ pohybu, ve které Motion Matching hledá pózy.**

Databáze se dělí podle stavů (idle, run starts, stops, crouch…) — jednak kvůli přehlednosti, jednak kvůli responzivitě: chooser vynutí prohledání správné databáze v ten samý frame (vzor z Fortnite). Ceny mezi oddělenými databázemi zporovnatelní normalization set. Do PSD patří sekvence, blend spacy i montáže; klipy musí mít root motion + force root lock.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md)

### Pose Search Schema

**Definice, co Motion Matching měří: kanály (trajektorie, pozice a rychlosti kostí) s vahami.**

Váhy říkají, na čem při výběru záleží — pozice chodidel typicky 1, rychlosti 0,3, trajektorie 1 (default 7 je moc). Vzorky trajektorie sahají do minulosti (−0,05 s) i budoucnosti (+0,35/0,7/1,0 s). Ladění je „umělecký proces": experimentuj a čti channels breakdown v debuggeru. Různé databáze můžou mít různá schémata (při skoku na chodidlech záleží míň). Kvadrupedi: přední a zadní nohy měřit zvlášť.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md)

### Pose Snapshot

**Zmrazení aktuální pózy skeletu (`Save Pose Snapshot`) jako blendovací zdroj v AnimBP — most z fyziky zpět do animace.**

Klíč k plynulému vstávání z ragdollu: tělo leží v póze, kterou žádná animace nezná — snapshot ji zachytí a Pose Snapshot uzel (stejné jméno!) z ní nechá blendovat do vstávací montáže. Alternativa: timeline nad Physics Blend Weight (postupné předání fyziky animaci).

Kde se s tím potkáš: [Ragdoll](praxe/ragdoll.md)

### Post-process AnimBP

**Animation blueprint přiřazený meshi (ne postavě), který se vyhodnocuje po hlavní animaci — vždy poslední.**

Ideální pro vrstvení: look-at hlavy a očí, korekce, cloth logika — cokoli, co se má aplikovat „přes" libovolnou animaci. Vázaný na skeleton (nový skeleton = duplikát + Assign Skeleton) a sdílený všemi instancemi meshe — logika pro víc postav se větví přes Get Owning Actor.

Kde se s tím potkáš: [MetaHuman v praxi](praxe/metahuman.md)

### Postmortem

**Ohlédnutí za dokončeným (nebo pohřbeným) projektem: co fungovalo, co ne a proč.**

Nejhutnější studijní žánr gamedevu — na rozdíl od tutoriálů obsahuje i cenu rozhodnutí a slepé uličky. Dobrý postmortem přiznává čísla (wishlisty, prodeje, časové odhady vs. realita) i emoce (launch blues). Psát vlastní postmortemy je nejrychlejší způsob, jak z odehraných projektů vytěžit zkušenost — viz Zápisky.

Kde se s tím potkáš: [Postmortem: tři roky na ShantyTown](teorie/postmortem-shantytown.md)

### Premature optimization

**Optimalizace před důkazem, že je potřeba — přepis na ECS ve hře, která běží na 200 FPS.**

Klasická past programátorů: výkonový strop se řeší dřív než hratelnost, workflow se deformuje kolem optimalizací a vývoj zpomalí. Pragmatická rada z praxe: 80/20 — většina velkých problémů se dá vyřešit měsíc před vydáním za zlomek času. Výjimka: tvrdý platformní cíl (slabý handheld) je požadavek, ne optimalizace. Pojem zpopularizoval Donald Knuth („premature optimization is the root of all evil").

Kde se s tím potkáš: [Žrouti času](teorie/produktivita.md)

### Press kit

**Balíček pro novináře: popis hry, kontakty, loga, screenshoty a trailer v plné kvalitě na jednom místě.**

Novinář, který o hře chce napsat, potřebuje assety hned — press kit mu šetří mailování a tobě zvyšuje šanci na pokrytí. Nástroj presskit() ho vygeneruje zdarma za odpoledne; odkaz na něj plní roli webu, dokud web není. Patří k němu press release při velkých beatech (zveřejnění stránky, datum vydání) — rozesílá se např. přes GamesPress.

Kde se s tím potkáš: [Steam stránka](teorie/steam-stranka.md)

### Procedural Vegetation

**Editor procedurálních stromů v enginu (5.7+): strom je graf uzlů — od presetu či od nuly po export static/skeletal meshe s Nanite foliage.**

Preset Loader nebo Grower dá strukturu, žluté modifiery (carve, gravity, slope) tvarují point cloud před Mesh Builderem, foliage palette + distributor olistí (ethylene threshold = plnost) a bone reduction ladí cenu větru. Vítr běží jen na instancích (wind transform provider + BP Global Foliage Actor). Presety Mega Plants dává Quixel zdarma na Fabu zhruba měsíčně; 5.8 přidává extract to mesh (procedurální strom z existující geometrie) a object interaction.

Kde se s tím potkáš: [PCG vegetace](praxe/pcg-vegetace.md)

### Producent

**V herním týmu project manager: zná timeline, drží seznam úkolů a ví, kdo co dělá a kdo je volný.**

Titul „producent" znamená v každém médiu něco jiného — ve hrách je to tahle role (občas s přesahem do kreativních rozhodnutí). Kdo vede kanban board na jamech s kamarády, dělá produkci doopravdy: je to reálná praxe pro industry roli.

Kde se s tím potkáš: [Plánovací nástroje](teorie/planovani-nastroje.md)

### Prokletí znalosti

**Expert na vlastní hru si neumí dát zážitek nováčka — ví příliš mnoho, než aby viděl tření.**

Dvě podoby: u tutorialu se svou hru nedokážeš odnaučit (proto onboarding testují cizí oči), u launche zase hraješ „správně", takže nevidíš exploity, které hardcore hráči najdou za večer. Playtest je jediný pohled na hru bez tohohle prokletí.

Kde se s tím potkáš: [Playtesting](teorie/playtesting.md) · [První dojem](teorie/prvni-dojem.md)

### Průběžná obtížnost

**Jak moc tě hra aktivně tlačí k prohře — kolik odporu klade cestou k cíli.**

Protipól aspirační obtížnosti. Bullet hell má průběžnou obtížnost vysokou, cozy sim skoro žádnou (grind není totéž co odpor); upgrade zdraví v roguelite ji snižuje. Vyrábí stres a úlevu — a spolu s estetikou říká hráči dopředu, jaké pocity čekat.

Kde se s tím potkáš: [Obtížnost a výzva](teorie/obtiznost.md)

### Půltón

**Nejmenší vzdálenost mezi dvěma sousedními tóny (E–F, C–C#).**

Se svým dvojčetem (celý tón) je stavební jednotkou stupnic i akordů. Sám o sobě není „čistý" interval; zblízka ve stejné oktávě pere výrazně víc než rozhozený po oktávách.

Kde se s tím potkáš: [Základy hudební teorie](hudba/hudebni-teorie-zaklady.md)

### Quad

**Čtyřúhelníková buňka mřížky meshe — u terénu základní jednotka rozlišení.**

Rozlišení Mesh Terrainu se zadává počtem quadů v osách XY; víc quadů = jemnější síť = víc detailu i dat. Interně se quady stejně dělí na trojúhelníky (GPU nic jiného nekreslí), ale pro autorskou práci je čtyřúhelníková mřížka přehlednější — proto s ní pracují terény, subdivision modeling i retopologie.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Race condition

**Chyba závislá na pořadí: dva kusy kódu se inicializují souběžně a jeden čte data, která druhý ještě nenastavil.**

V UE klasicky mezi BeginPlay různých actorů — klíč se ptá dveří na ID dřív, než si ho dveře vygenerovaly. Pořadí inicializace není zaručené; nespoléhej na něj. Lék: event dispatcher („KeyAssigned") — místo čtení hned se posluchač binduje a data si nechá oznámit, až existují.

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md)

### Random pitch variation

**Náhodný posun výšky zvuku při každém přehrání; zabíjí mechanickou repetici.**

Zvuk sebrání předmětu ve Stardew Valley je mlasknutí pusou — s náhodným pitchem přestane znít digitálně a otravně. Často je způsob implementace důležitější než samotný zvuk.

Kde se s tím potkáš: [Sound design ve hře](hudba/sound-design-ve-hre.md)

### Recall priming

**Level design technika: rozmístit do prostředí nenápadné nápovědy, které hráči zpřístupní správnou vzpomínku těsně před tím, než ji bude potřebovat.**

Hráči se u puzzlů nezasekávají hloupostí, ale nedostupností správného nástroje v paměti. Priming ji zvedá prostředím: tmavá chodba donutí vytáhnout pochodeň, hořlavé liány cestou připomenou, že oheň pálí vegetaci — a u puzzle s liánami řešení „samo" naskočí. Hráč se necítí veden, cítí se chytrý; UI nápověda by mu ten pocit ukradla.

Kde se s tím potkáš: [Vedení hráče](teorie/vedeni-hrace.md)

### Recoup

**Splacení vydavatelovy investice z tržeb, než se vývojáři začne vyplácet jeho podíl.**

Do okamžiku recoupu obvykle plyne vydavateli 80 až 90 procent tržeb; teprve pak se poměr překlopí ve prospěch studia. Proto se na vydavatelskou smlouvu vyplatí dívat jako na půjčku splácenou z budoucích prodejů, ne jako na grant — a proto je klíčové, co všechno se do splácené částky započítá (marketing, lokalizace, portace).

Kde se s tím potkáš: [Financování](teorie/financovani.md#vydavatel-je-banka-ne-darce)

### Refundace

**Vrácení peněz za koupenou hru — na Steamu automatické do dvou hodin hraní a dvou týdnů od nákupu.**

Z pohledu vývojáře je to první srážka z hrubé tržby, po níž následuje podíl obchodu, bankovní poplatky a daně. Praktický důsledek: číslo na dashboardu není příjem — v rozpadu jednoho indie studia zbyla z hrubé tržby po všech srážkách zhruba polovina, a to ještě před zdaněním.

Kde se s tím potkáš: [Vydání hry: co ti reálně zbyde](teorie/vydani-hry.md)

### Redirector

**Ghost soubor, který po přesunu assetu zůstává na starém místě a přesměrovává reference na nové.**

Důvod, proč „prázdné" složky nejdou smazat — a proč force delete rozbije projekt (reference vedou do prázdna). Správně: pravý klik → Update Redirector References (odkazy se přepíšou natrvalo), pak Delete Unreferenced Redirectors, pak teprve mazat složku. Stěhuj po jedné složce — hromadné přesuny editor shazují.

Kde se s tím potkáš: [Organizace projektu](praxe/organizace-projektu.md)

### Referenční transparentnost

**Funkci lze nahradit její návratovou hodnotou, aniž se program změní — žádné skryté závislosti, žádný sdílený stav.**

Odměna: triviální testování, paralelizace i cachování. Užitečnější jako čočka na design než jako akademický pojem: když se něco blbě testuje, neptej se po mock knihovně — ptej se, proč ta funkce není referenčně transparentní. V UE: pure funkce bez side-effectů.

Kde se s tím potkáš: [Programátorské myšlení](teorie/programatorske-mysleni.md)

### Rekurze

**Funkce, která volá sama sebe — s base case proti nekonečnu a zmenšováním problému směrem k němu.**

Tři principy: volá sebe; má base case (nejmenší problém s přímou odpovědí); každé volání problém zmenšuje. Zbytek je „recursive leap of faith" — důvěra, že menší práci funkce odvede. Přirozená pro stromy: složky, dialogy, scene graph, behavior tree.

Kde se s tím potkáš: [Programátorské myšlení](teorie/programatorske-mysleni.md)

### Relativní dur

**Durová tónina sdílející tytéž tóny s danou mollovou (a naopak).**

C dur a A moll mají stejné tóny, liší se domovským tónem. Trik na radost v moll: třetí akord mollové stupnice je tónika relativní durové — kdykoli po něm sáhneš, vlije se do skladby světlo.

Kde se s tím potkáš: [Jak psát melodie](hudba/melodie.md) · [Akordy a harmonie](hudba/akordy-a-harmonie.md)

### Render target

**Textura, do které engine vykresluje za běhu — použitelná jako vstup i jako výstup.**

Slouží k obrazovkám kamer, zrcadlům nebo malování do textury za běhu. Šikovné vedlejší použití: materiál složený z noise uzlů se dá do render targetu vypéct a uložit jako obyčejnou texturu — takže na generování šumu nepotřebuješ žádný externí program.

Kde se s tím potkáš: [Materiály: VFX textury](praxe/materialy.md#vfx-textury-nedelat-je-a-kdyz-uz-tak-v-krite)

### Retargeting

**Přenos animace z jedné kostry na jinou, která má odlišné proporce.**

Bez něj by každá postava potřebovala vlastní sadu animací. V UE se řeší IK Rigem a IK Retargeterem: řekneš, které kosti si odpovídají, a engine dopočítá zbytek. Právě proto je u AI generovaných animací důležité, na jaké standardní kostře model exportuje — mapování na běžný skeleton je rozdíl mezi „použitelné" a „k ničemu".

Kde se s tím potkáš: [AI assety: animace v reálném čase](praxe/ai-assety.md#animace-generovana-v-realnem-case-kam-se-posunulo-ardy) · [MetaHuman v praxi](praxe/metahuman.md#hratelny-metahuman-retarget-jednim-klikem-a-virtual-bones)

### Retopologie

**Přestavba geometrie na čistší síť: z milionů neuspořádaných trojúhelníků (sculpt, sken, AI generát) použitelný mesh pro rig a animaci.**

AI pipeline ji řeší třemi cestami: decimace + normal bake (rychlá, „topologie pro start"), smart low poly režimy generátorů (pečou normal mapu z HD verze), nebo nástroje jako Quad Remesher. Na čem záleží: deformující se části (klouby, obličej) chtějí pořádnou topologii, rekvizity snesou decimát.

Kde se s tím potkáš: [AI assety](praxe/ai-assety.md) · [AI agenti](praxe/claude-code-ue.md)

### Retrieval practice

**Učení vybavováním: odvrať zrak a zkus si vzpomenout — poráží opakované čtení, i když se hůř „cítí".**

Opakované čtení buduje známost, ne vlastnictví; vybavování nutí mozek znalost rekonstruovat, a tím ji ukládá. Prakticky: po kapitole ji převyprávěj vlastními slovy, uč druhé (klidně zeď), dej si kvíz. Věda za kvízovým protokolem.

Kde se s tím potkáš: [Učení v éře AI](teorie/uceni-v-ere-ai.md) · [Zápisek: Kvízový protokol](zapisky/kvizovy-protokol.md)

### Retriggerable Delay

**Delay, který se každým dalším spuštěním restartuje od nuly — doběhne až po klidu na vstupu.**

Ideální „ztráta zájmu" AI: dokud percepce cíl hlásí (a event se opakuje), odpočet se resetuje; jakmile hlásit přestane, delay doběhne a vrátí AI k patrole. Délka musí být větší než interval, kterým se vstup opakuje (u Pawn Sensingu > 0,5 s), jinak doběhne i mezi dvěma hlášeními.

Kde se s tím potkáš: [AI vnímání](praxe/ai-vnimani.md) · [Základy AI](praxe/ai-zaklady.md)

### Reverb

**Odraz zvuku od prostředí; dozvuk.**

Slouží dvěma věcem: slepit zvuky dohromady, nebo vyjádřit prostor (chodba, koupelna, kaňon). Přidává realističnost a hloubku — bez něj zní zvuk synteticky.

Kde se s tím potkáš: [Sound design ve hře](hudba/sound-design-ve-hre.md)

### Rewind Debugger

**Nahraje běh hry a nechá tě scrollovat časem: co hrálo, proč to Motion Matching vybral, jak rozhodoval State Tree.**

`Debug → Rewind Debugger`, zapni auto-record (+ auto-eject). Dvojklik na track otevře asset na správném framu; šipkami jdeš frame po framu; eject kamery přehraje pohyb ve světě. Pose search debugger uvnitř ukazuje kandidáty, ceny a channels breakdown; od 5.7 má vlastní track i State Tree — vidíš přesný frame, kdy padlo rozhodnutí.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md) · [GASP](praxe/gasp.md)

### RITE

**Rapid Iterative Testing and Evaluation: jeden tester → oprav vážné problémy → další tester.**

Metoda z UX designu pro vývojáře bez velkého poolu testerů: sleduj jednoho hráče, zapisuj vše pozoruhodné, komunikuj minimálně; po sezení oprav každý vážný problém a opakuj s novým člověkem, který by na staré problémy už neměl narazit. Cíl není hra snadná na hraní, ale snadná na chtění hrát.

Kde se s tím potkáš: [Playtesting: kadence a RITE](teorie/playtesting.md)

### Rigging

**Vložení kostry do modelu a nastavení, jak kosti ovládají mesh — bez toho zůstane model socha.**

Následuje weight painting (malování vlivu jednotlivých kostí, aby deformace vypadala přirozeně) a stavba ovladačů, které animátorovi umožní hýbat kostrou jednoduše — jako provázky loutky. Na téhle vrstvě se řeší i to, aby chodidlo drželo na zemi, když se hýbe zbytek těla. Typická práce technického artisty.

Kde se s tím potkáš: [Art specializace: tech art](teorie/art-specializace.md) · [Animace v UE](praxe/animace-nastroje.md)

### Roguelike

**Žánr postavený na opakovaných bězích: smrt je součást smyčky, svět se generuje procedurálně, znalost hráče je hlavní trvalý pokrok.**

Pro design je podstatný důsledek mnoha běhů: hráč potkává stejné systémy znovu a znovu, což násobí šanci na náhodné objevení skrytých pravidel — proto žánru tak sedí tajné řetězce (Spelunky). Odnož s trvalým meta-postupem mezi běhy se označuje roguelite.

Kde se s tím potkáš: [Smyčky a řetězce](teorie/smycky-a-retezce.md)

### Root motion

**Pohyb uložený v animaci samotné (v root kosti) — postava se hýbe tak, jak animátor animoval, kapsle následuje.**

Protiklad capsule driven přístupu (vstup hýbe kapslí, animace se lepí). Motion Matching root motion data vyžaduje — z nich čte trajektorie klipů; hromadně se zapíná přes Property Matrix (Enable Root Motion + Force Root Lock, u smyček Looping). GASP je capsule driven, ale animace root motion mají — budoucnost je blending obou přístupů po částech animace.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md)

### Rovnoměrně temperované ladění

**Ladění, které dělí oktávu na dvanáct stejně velkých kroků (equal temperament).**

Nejčistší intervaly (z alikvót) jen přibližuje, ne přesně trefuje — velká tercie tak reálně sedí lehce na vrcholu disonance. Kompromis, který umožňuje hrát ve všech tóninách bez přelaďování.

Kde se s tím potkáš: [Fyzika souzvuku](hudba/fyzika-souzvuku.md)

### Rubber banding

**Umělá podpora hráče, který je pozadu, a brzda hráče napřed — v multiplayeru se říká catch-up mechanika.**

Nejde o podvod na hráče, ale o opravu učebního prostředí: kdo je beznadějně pozadu, dostává od hry konstantní „špatně" a nemá se z čeho učit; kdo je nedostižně napřed, dostává konstantní „dobře". Rubber banding oba vrací do pásma, kde akce zase mají čitelné následky. Příbuzné nástroje: hinty, skipy, měkké stavy úspěchu (skóre místo výhra/prohra).

Kde se s tím potkáš: [Zábava: flow](teorie/zabava.md)

### Rubber duck debugging

**Vysvětli problém nahlas — klidně gumové kachně — a řešení se často objeví v půlce vysvětlování.**

Formulace nutí seřadit fakta a předpoklady, a přesně v tom seřazení bývá chyba vidět. Funguje s kachnou, kamarádem i AI; s člověkem má bonus druhé perspektivy („z ptačí vidím díru v úvaze").

Kde se s tím potkáš: [Programátorské návyky](teorie/programatorske-navyky.md)

### Runway

**Kolik měsíců dokážeš pracovat, než dojdou peníze — ne kolik peněz máš.**

Runway se dá prodloužit z obou stran: naspořením hotovosti i snížením výdajů. Typický vzorec u přeživších indie studií je období cíleného šetření před skokem na plný úvazek. Jedno tříčlenné studio si takto koupilo rok a půl jistoty a skromným životem ji natáhlo na dva roky. Protějšek [burn rate](#burn-rate).

Kde se s tím potkáš: [Přežít jako studio](teorie/prezit-jako-studio.md#ctyri-roky-bez-hitu-financovani-riziko-a-runway) · [Financování](teorie/financovani.md#co-si-udrzi-kontrolu-uspory-prijmy-z-backlogu-a-komunita)

### Sampling

**Použití kusu existující nahrávky jako stavebního materiálu nové skladby.**

Základ hip hopu (vintage soul samply) i moderního hood trapu (remix nečekané písně). Nahrávku izoluješ, nasekáš, přeskládáš, zrychlíš nebo přeladíš. Pozor na práva k původní nahrávce.

Kde se s tím potkáš: [Žánry a jejich melodie](hudba/zanry-a-styl.md)

### SaveGame objekt

**Blueprint třída typu SaveGame: nese proměnné k uložení a přes pojmenovaný slot se zapisuje na disk.**

Tři uzly stačí: Create Save Game Object / Load Game From Slot / Save Game to Slot (+ Delete Game in Slot). Architektura okolo: referenci drží Game Instance (přežije přechody levelů), přístup odkudkoli dává function library. Load není magie — hodnoty se musí ručně aplikovat zpět (rychlost do movementu, transform na actora). Myslet dopředu: verze formátu a více slotů.

Kde se s tím potkáš: [Ukládání](praxe/ukladani.md)

### SCAMPER

**Sedm pák na nápad: Substitute, Combine, Adapt, Magnify, Purpose, Eliminate, Rearrange.**

Formální ideační technika — funguje na vylepšení rozdělané hry i generování nové z oblíbené. Nejužitečnější páky pro gamedev: Magnify (zazoomuj na nejzábavnější prvek a udělej z něj celou hru) a Eliminate (generátor „hra bez X": Skyrim bez magie, Fortnite bez stavění).

Kde se s tím potkáš: [Nápad: ideace jako řemeslo](teorie/napad.md)

### Scope

**Rozsah projektu: kolik obsahu, systémů a ambicí hra obsáhne.**

Hlavní páka proveditelnosti — a nejčastější příčina nedokončených her. Pro začátečníka platí, že malý scope není kompromis, ale strategie: krátká smyčka dokončení → zpětná vazba → další projekt o úroveň výš. Malá hra přitom není zmenšená velká hra, ale jedna vyjmutá mechanika, které všechno slouží. „Scope creep" je plíživé bobtnání rozsahu během vývoje; game jam je institucionalizovaná obrana.

Kde se s tím potkáš: [Začátky bez zkušeností](teorie/zacatky-bez-zkusenosti.md) · [Scope: malé hry a design by constraint](teorie/scope.md) · [Start projektu](teorie/jak-zacit.md)

### Scope creep

**Plíživé bobtnání rozsahu během vývoje: „co kdybychom přidali rybaření?"**

Dvojsečná past: někdy je to přesně ten twist, který hře chyběl, častěji fraktální bobtnání (rybaření → pruty → rybářské lodě) nebo míchání žánrů, které vyrobí hru pro nikoho — publikum dvou žánrů je průnik, ne součet. Rozhodovací filtr: sytí nápad účel hry, nebo ho ředí? Obrana: sticky note test na začátku, momentum bar a psaní nápadů do šuplíku během vývoje.

Kde se s tím potkáš: [Žrouti času](teorie/produktivita.md) · [Scope: nápad zaparkuj, nezabíjej](teorie/scope.md) · [Nápad](teorie/napad.md) · [Start projektu](teorie/jak-zacit.md)

### Scrum

**Agilní metodika: práce ve sprintech, priority se na sprint meetingu tahají z backlogu.**

Oproti kanbanu (plynulý tok karet) přidává rytmus: pevné bloky času s jasným cílem a review na konci. Indie hybrid: kanban board + měsíční „sprint" zakončený týdnem playtestů. Kříženec obou metodik se jmenuje scrumban.

Kde se s tím potkáš: [Plánovací nástroje](teorie/planovani-nastroje.md) · [Playtesting: kadence](teorie/playtesting.md)

### Semiotika

**Nauka o tom, co symboly znamenají a proč — u písma a tvarů dřív, než přečteš obsah.**

Typografie nese význam třemi cestami: materiálem a nástrojem vzniku (dláto do kamene, brk, tiskový lis), historickou epochou a odkazy na jiná média (filmové plakáty, umělecká hnutí). Proto font sdělí žánr a dobu dřív, než hráč přečte první slovo — a proto hra zasazená do konkrétní éry znamená spoustu práce na cedulích a plakátech ve světě.

Kde se s tím potkáš: [Typografie](teorie/typografie.md) · [Ludotematický soulad](teorie/ludonarativni-soulad.md)

### Seamless loop

**Hudební smyčka, jejíž konec plynule navazuje na začátek — bez slyšitelného „švu".**

Herní hudba se přehrává donekonečna, takže poslední takt musí přejít do prvního. Jinak uslyšíš šev při každém opakování. Je to aranžérský přechod zapojený do kruhu.

Kde se s tím potkáš: [Tvorba herního soundtracku](hudba/tvorba-soundtracku.md)

### Self Pruning

**PCG uzel, který z překrývajících se bodů nechá jen některé — procedurální „ať se to nedotýká".**

Překryvy měří podle bounds, volitelně podle skutečných kolizí (use collision attribute) — pozor, bere menší z obou, takže pro kolizní režim bounds záměrně nafoukni bounds modifierem. S bounds nastavenými na požadovaný rozestup funguje jako foliage garance minimální vzdálenosti, jen checkboxem v grafu.

Kde se s tím potkáš: [PCG základy](praxe/pcg-zaklady.md)

### Separation of concerns

**Princip: systém se dělí na malé části s jedinou zodpovědností — jako motor z vyměnitelných dílů.**

Návrhová otázka „co mají všechny X společné?" oddělí obecné (base classa, komponenta) od specifického (děti). Ability se vytáhne z komponenty do vlastního objektu; komponenta pak řeší jen aktivaci a cooldowny. Odměna: 20 abilit = 20 nezávislých blueprintů se stejnou strukturou, každý laditelný zvlášť.

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md) · [Organizace projektu](praxe/organizace-projektu.md)

### Short description

**Krátký popis hry na Steamu — ~300 znaků pod capsule obrázkem, první text, který potenciální hráč čte.**

Zároveň nejlevnější validační nástroj nápadu: „test 300 znaků" = zkus popis napsat v den nula. Dvě věty se žánrem, perspektivou, hlavními činnostmi (hodně sloves!), cílem a prostředím. Když to nejde, nemáš vágní popis — máš vágní hru. Rozšířená verze testu je mock Steam page: dlouhý popis, features, zkusmá capsule.

Kde se s tím potkáš: [Nápad: test 300 znaků](teorie/napad.md) · [Scope](teorie/scope.md)

### Serif

**Patka: drobné zakončení na koncích tahů písmene. Nese historickou asociaci a mírně zpomaluje čtení.**

Vznikla v době fyzického tisku, kde bránila rozpíjení inkoustu a opotřebení stroje — proto s patkovým písmem podvědomě spojujeme starší dobu. Praktický důsledek pro hry: dekorativní patkový font se hodí na názvy a nápisy ve světě, ale funkční text (popisy schopností, tutoriály) patří do bezpatkového, protože se čte rychleji.

Kde se s tím potkáš: [Typografie](teorie/typografie.md)

### Signal-to-noise ratio

**Poměr užitečné informace (signál) k balastu (šum) — klíčová veličina učení, soustředění i designu obtížnosti.**

Učení je budování prediktivního modelu světa a potřebuje data, ze kterých se dá učit. Frustrace = konstantní „špatně" (nulový signál), nuda = konstantní „dobře" (nulový signál); flow kanál je pásmo, kde některé akce fungují a jiné ne — nejlepší signál. Jasné cíle jsou filtr šumu; soustředění je totéž z druhé strany (rozptýlení a vizuální balast = šum).

Kde se s tím potkáš: [Zábava: flow](teorie/zabava.md)

### Shape language

**Standardizace tvarů pro významy napříč celou hrou: plus je zdraví, kruh štít, špičaté tvary poškození.**

Nutnost všude, kde je efektů nebo ikon hodně — konzistentní tvarosloví umožní pochopit funkci prvku bez čtení. Klíčová vlastnost: když jsou barvy podobné, tvar je jediné, co prvky rozliší. Používá se stejně ve VFX i v rozhraní, a spolu s barvou a pozicí tvoří pravidla, kterým se říká vizuální jazyk hry.

Kde se s tím potkáš: [Art specializace: VFX](teorie/art-specializace.md) · [Game feel](teorie/game-feel.md)

### Silueta

**Obrys tvaru — nejrychlejší nosič identity a čitelnosti; poznáš z ní postavu i prostředí bez jediného detailu.**

V prostředí siluety vyrábí kontrast světla a stínu (chiaroscuro): žádný kontrast = žádné tvary = „proč to vypadá špatně, když mám Nanite?". Test: screenshot → odbarvit → levels stáhnout na černobílou; když nezbydou čitelné plochy světla a tmy, žádný setting scénu nezachrání. U assetů rozhoduje silueta o rozpoznatelnosti víc než textury.

Kde se s tím potkáš: [Stavba prostředí](praxe/env-tvorba.md) · [Breakdowny](praxe/env-breakdowny.md)

### Simulated annealing

**Optimalizace po vzoru žíhání kovů: začni ochotou přijímat i horší kroky (explorace) a postupně chladni k vylepšování.**

Prostý hill-climb uvízne na prvním lokálním vrcholu; klesající „teplota" dává šanci přeskočit údolí k lepším řešením. Tentýž explore/exploit trade-off, na kterém stojí teorie zábavy — tady jako nástroj na rozvrhy, rozmístění a tuning parametrů.

Kde se s tím potkáš: [Algoritmy, které stojí za to znát](teorie/algoritmy-prehled.md) · [Zábava a flow](teorie/zabava.md)

### Single Layer Water

**Shading model pro vodu: translucence a kaustika za cenu jednoho průchodu — de facto standard v UE.**

Zásadní limit: stíny přijímá jen z primárního directional lightu — scéna svícená spotlighty se na hladině rozpadne. Řešení per záběr: přepnout materiál na Default Lit (+ metallic 1 pro tmavou hlubokou vodu) tam, kde translucenci nepotřebuješ. Žádný z modelů není univerzálně lepší.

Kde se s tím potkáš: [Nástroje: EasyWaterscape](praxe/nastroje-voda.md)

### Singleton

**Vzor garantující jedinou instanci s globálním přístupem — a zároveň „glorifikovaná globální proměnná".**

Legitimní pro centrální logger či connection pool; nebezpečný jako výmluva pro globální stav (mizerné testování, multithreading chce ošetření). V UE singleton žije jako Game Instance a Subsystems — jedinost garantuje engine; co tam nacpeš, to se rozleze.

Kde se s tím potkáš: [Design patterns](teorie/design-patterns.md) · [Principy architektury](praxe/principy-architektury.md)

### Size Map

**Nástroj editoru, který ukáže, kolik paměti asset zabere i se vším, co s sebou táhne.**

Pravý klik na asset → Size Map → Memory Size. Nejlepší způsob, jak zviditelnit cenu tvrdých referencí: přidání jediného cast uzlu do blueprintu může jeho paměťovou stopu zdvojnásobit, protože cílová třída se od té chvíle nahrává s ním. Diagnostický protějšek Reference Vieweru, který ukazuje vazby, ne velikost.

Kde se s tím potkáš: [Komunikace Blueprintů: kolik stojí cast](praxe/komunikace-blueprintu.md#interface-nebo-dispatcher-a-kolik-doopravdy-stoji-cast) · [Principy architektury](praxe/principy-architektury.md#tri-principy-skalovatelnosti-separace-volne-vazby-data)

### Skill ceiling

**Maximální dosažitelná úroveň dovednosti ve hře — strop toho, jak dobře se dá hrát.**

Vysoký ceiling znamená prostor pro růst a mastery (fighting hry, závodní simy); nízký znamená, že hru brzy „vytěžíš". „Easy to learn, hard to master" = nízký floor + vysoký ceiling — drahý ideál, který vyžaduje hloubku systémů, ne jen tvrdší čísla.

Kde se s tím potkáš: [Obtížnost a výzva](teorie/obtiznost.md)

### Skill floor

**Minimální dovednost nutná k tomu, hru vůbec hrát — bariéra vstupu.**

Kdo na floor nedosáhne, nehraje (dítě s ovladačem hru „hraje" jen zdánlivě). Komplexita ovládání je floor sama o sobě — proto casual hry sázely na Wii remote a touchscreeny. Hardcore hry mají floor záměrně výš: předpokládají znalost konvencí žánru.

Kde se s tím potkáš: [Obtížnost a výzva](teorie/obtiznost.md)

### Skills audit

**Inventura vlastních dovedností před volbou projektu: co umím, co neumím, co napůl.**

Zdroje projektu nejsou jen čas a peníze — hlavně schopnosti. Audit vyřadí 90 % nápadů a zbydou proveditelné: máš ilustrátora bez animátora → hra s mluvícími portréty (Dredge nemá walk cycle, Mini Metro nemá postavy — dohromady přes 6 milionů kopií). Tvrdší varianta otázky: co neumím tak, že to do projektu nesmí?

Kde se s tím potkáš: [Nápad: ideace jako řemeslo](teorie/napad.md) · [Scope: rozpočet pozornosti](teorie/scope.md)

### Smart Object

**Objekt světa, který inzeruje interakce: sloty k zabrání a chování (State Tree), které se po claimu spustí na postavě.**

Lavička nese smart object komponentu a definition data asset; NPC si najde volný slot, claimne ho (druhé NPC už ho nedostane) a spustí injektovaný strom — jiný objekt dodá jinou logiku, beze změny AI postavy. V GASP navázané na Motion Matching: vstupní montáž se vybírá pose match sloupcem podle pózy a vzdálenosti od vstupního bodu.

Kde se s tím potkáš: [GASP](praxe/gasp.md)

### Soft boundary

**Hranice mapy, kterou lze fyzicky překročit — ale svět dá jasně najevo, že je to špatný nápad.**

Pět vzorů: narativní (most se zřítí, postava odmítne jít dál), countdown (mráz, plyn, dezerce — tlak času místo kolize), nepřátelská (za hranicí loví něco silnějšího; nemusí zabíjet — stačí probrat se potlučený zpátky), ekonomická (kyslík/palivo nevystačí na návrat) a percepční (ztráta orientace a viditelnosti). Nejlépe fungují kombinované a vždy s fikčním alibi.

Kde se s tím potkáš: [Prostor a hranice](teorie/prostor-a-hranice.md)

### Soft skills

**Dovednosti bez přímo viditelného výstupu — úsudek, komunikace, analýza, empatie; modifikují kvalitu všeho, co vzniká.**

Protiklad hard skills (kód, obrázek — měřitelný výstup). Zásadní rozdíl pro učení: hard skills se dají učit didakticky (návodem), soft skills jen objevováním — hraním, rozborem, workshopem. Game design je svazek soft skills; proto na něj neexistují recepty.

Kde se s tím potkáš: [Rady z praxe](teorie/rady-z-praxe.md) · [Učení v éře AI](teorie/uceni-v-ere-ai.md)

### Sound Cue

**Klasický zvukový asset UE: graf uzlů nad wave soubory — random variace, mixování, attenuace.**

Multi-select wave souborů → Create Sound Cue vloží Random uzel automaticky (variace kroků jedním klikem). Pro pokročilejší práci (parametry za běhu, procedurální audio) je nástupcem MetaSounds; Sound Cue zůstává nejrychlejší cesta k „přehraj náhodnou variaci".

Kde se s tím potkáš: [Kroky](praxe/footsteps.md)

### Sound font

**Kolekce nasamplovaných zvuků nástroje, přehrávaná sound font playerem (soubory .sf2).**

Charakteristický retro zvuk herní hudby (Undertale) často dělá paleta, ne skladba — Toby Fox použil fonty ze SNES her. Rychlá, autentická alternativa ke stavbě zvuku od nuly v synthu.

Kde se s tím potkáš: [Tvorba herního soundtracku](hudba/tvorba-soundtracku.md)

### Sparse set

**Minimální sada animací pro Motion Matching: ~13 klipů bez strafu, ~26 se strafem, ~60–80 se stavy.**

Epicův recept proti mýtu „potřebuju 500 animací jako GASP": idle, run forward, starty a stopy (levá i pravá noha kvůli stutter-stepům), oblouky (run arcs) a refacing starty. Rozsah řídí otázky na hru: co gameplay potřebuje a kolik movement states (každý ≈ 2×). S procedurálními uzly je 26animační set podle Epicu shippable. Klidně hand-keyed a stylizovaný.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md)

### Spline

**Komponenta s křivkou z tažitelných bodů — trasa, po které se dá vést pohyb, geometrie nebo obsah.**

Body se tahají přímo v levelu (Alt + tažení duplikuje); kód čte Get Location at Spline Point / Get Number of Spline Points — pozor na coordinate space (typicky World). V AI definuje patrol trasy, v traversal systémech značí hrany překážek, u coveru tvar krytí.

Kde se s tím potkáš: [State Trees](praxe/state-trees.md) · [GASP](praxe/gasp.md) · [Systémy nad MM](praxe/mm-systemy.md) · [Interakce s předměty](praxe/interakce-predmety.md)

### Spline mesh

**Mesh procedurálně natažený a ohnutý podél segmentu splinu — křivka se stává viditelnou geometrií.**

Každý segment dostane instanci meshe zdeformovanou mezi počátečním a koncovým bodem (Set Start and End v Blueprintu, spline mesh spawner v PCG). Na orientaci záleží: forward axis musí odpovídat ose meshe, jinak se geometrie kroutí. Liány a lana z obyčejného válce, oblouk předpovězené dráhy hodu z tenkého průsvitného válce.

Kde se s tím potkáš: [PCG liány](praxe/pcg-liany.md) · [Interakce s předměty](praxe/interakce-predmety.md)

### Square hole

**Chyba balancu: univerzální nástroj či strategie, která řeší každou situaci — a tím zabíjí všechna rozhodnutí.**

Podle memu „it goes in the square hole". Vzniká z balancování jedinou osou síly: jeden nástroj vždycky vyjde o chlup líp a stane se odpovědí na všechno. Lék: vícerozměrné nástroje (každý dobrý na něco jiného) + pestré problémy + zajímavé hraniční případy, kde volba vyžaduje úvahu. Cíl balancu: rozhodnutí netriviální, předvídatelná a nosná i po opakování.

Kde se s tím potkáš: [Zábava: balanc rozhodnutí](teorie/zabava.md)

### Squash & stretch

**Animační princip: deformace objektu při akci — zploštění při dopadu, natažení při výskoku.**

Nejstarší trik animace (Disney) přenesený do her: skok s deformací působí pružně, nepřítel, který se při zásahu „zmáčkne", působí živě. Levný a účinný kus juice — mění pocit, ne mechaniku.

Kde se s tím potkáš: [Game feel a imerze](teorie/game-feel.md)

### State alias

**Zástupný uzel ve state machine, který reprezentuje všechny zaškrtnuté stavy — jedno přechodové pravidlo místo N.**

Alias „to crouch" zastupující idle i walk/run znamená jediný přechod do podřepu místo přechodu z každého stavu zvlášť. S rostoucím počtem stavů drží graf čitelný; pravidla se píší jednou a platí pro všechny zastoupené stavy.

Kde se s tím potkáš: [Základy pohybu](praxe/pohyb-zaklady.md)

### State machine

**Stavový automat v AnimBP: stavy = animace, přechody = pravidla — klasická architektura herní animace.**

Užitečné vzory: vícedílné akce (skok start → loop → end) s Automatic Rule Based on Sequence Player (přechod po dohrání klipu), state aliases proti explozi přechodů, AnimBP bez castu (Try Get Pawn Owner + Get Movement Component = funguje na každé postavě se stejným skeletonem). Motion Matching state machines nahrazuje, ale hybridní setupy je kombinují dál.

Kde se s tím potkáš: [Animační nástroje](praxe/animace-nastroje.md) · [MM základy](praxe/mm-zaklady.md) · [Základy pohybu](praxe/pohyb-zaklady.md)

### State Tree

**Hierarchický stavový automat UE pro AI i obecnou logiku — sesterský systém behavior tree.**

Vyhodnocuje se shora dolů, stavy nesou tasky a přechody podle úspěchu/selhání; umí linkované podstromy (patrol) i stromy injektované zvenčí (smart objects). Přechody spouští i eventy s gameplay tagy (Send State Tree Event); Finish Task končí celý stav, context injektuje taskům AI controller. Tasků má z krabice málo — píšou se per projekt.

Kde se s tím potkáš: [State Trees](praxe/state-trees.md) · [GASP](praxe/gasp.md)

### Steam Next Fest

**Steamový online festival demoverzí nevydaných her, koná se třikrát ročně.**

Funguje jako multiplikátor wishlistů — čím víc jich máš na vstupu, tím víc akce vygeneruje — a každá hra se smí zúčastnit jen jednou, takže načasování je strategické rozhodnutí (jít tam s maximem, klidně couvnout a počkat na další termín). Citované minimum pro smysluplný efekt ~7 000 wishlistů na vstupu (údaj jednoho vydání, ne konstanta).

Kde se s tím potkáš: [Postmortem ShantyTown](teorie/postmortem-shantytown.md) · [Idea iceberg](teorie/rady-z-praxe.md)

### Stitching

**Experimentální MM technika: místo lineárního blendu najde animaci, která tě za daný čas dostane z aktuální pózy do cílové.**

Řeší přechody locomotion → gameplay akce (úder, který má za 0,25 s dopadnout) a gameplay → cinematika (sequencer stitch track v 5.6; Witcher 4 demo). Nosiče: Chooser Player se stitch databází, Sequence Player se „start with matching pose" + Pose Search Branch In notify. Čas přechodu je laditelný designérem, ne zadrátovaný animátorem.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md)

### Strategy pattern

**Rodina zaměnitelných algoritmů, každý ve své třídě za společným rozhraním — místo rostoucího if/else stromu.**

„Programování na úrovni rozhraní": cíl jeden, strategií víc, výměna za běhu. Ukázka open-closed principu — nové chování přidáš novou třídou bez sahání do existujícího kódu. V UE: movement modes Moveru, choosery, Blueprint Interface místo kaskády castů.

Kde se s tím potkáš: [Design patterns](teorie/design-patterns.md) · [Mover](praxe/mover.md)

### Struct

**Pojmenovaná skupina proměnných, se kterou se zachází jako s jednou hodnotou.**

Místo osmi vstupů do funkce jeden; místo osmi proměnných v SaveGame objektu jedna. Kromě čitelnosti přináší hlavně jedno místo změny: přidáš-li do struktury pole, všechna místa, která ji předávají, fungují dál. V save systémech je to rozdíl mezi rozšiřitelným formátem a rozsypaným seznamem.

Kde se s tím potkáš: [Ukládání: struktury a interface](praxe/ukladani.md#save-system-ktery-prezije-druhy-projekt-struktury-interface-a-async)

### Stupnice

**Sada tónů, které spolu znějí dobře, daná vzorcem půltónů a celých tónů.**

Durová = celý–celý–půl–celý–celý–celý–půl, mollová = celý–půl–celý–celý–půl–celý–celý; vzorec přiložíš na libovolný tón. Nemusíš znát tóny každé tóniny — stačí vzorec a počítat půltóny.

Kde se s tím potkáš: [Základy hudební teorie](hudba/hudebni-teorie-zaklady.md)

### Subsystem

**Automaticky vytvářený singleton s definovaným životním cyklem (engine / game instance / world / local player).**

Nemusíš ho spawnovat ani registrovat — engine ho vytvoří a drží podle typu. Game instance subsystem žije po celou dobu aplikace, ideální pro mediátory (event manager, broadcast kanály) a služby bez vlastního místa ve světě. Blueprintově se konzumuje snadno; definice vyžaduje C++.

Kde se s tím potkáš: [Komunikace Blueprintů](praxe/komunikace-blueprintu.md) · [Principy architektury](praxe/principy-architektury.md)

### Subtraktivní syntéza

**Nejběžnější typ syntézy (subtractive synthesis): oscilátor generuje bohatý zvuk, filtr z něj ubírá.**

Řetězec oscilátor → filtr → obálka/LFO. Slavný pad je jen pila protažená filtrem. Pochopíš-li tenhle jeden signálový řetězec, přečteš skoro každý synth.

Kde se s tím potkáš: [Syntéza zvuku od nuly](hudba/synteza-zvuku.md)

### Survivorship bias

**Zkreslení z toho, že vidíš jen ty, kdo přežili — neúspěšné pokusy zmizí z dohledu.**

V gamedevu je obzvlášť silné: postmortemy píšou hlavně ti, komu to vyšlo, a zrušené projekty nemají Steam stránku. Poctivé odhady mluví o tom, že úspěchu ve smyslu udržitelné obživy dosáhne méně než patnáct procent těch, kdo to zkusí. Praktický důsledek: rady od úspěšných vývojářů popisují nutné, ne postačující podmínky.

Kde se s tím potkáš: [Data o úspěchu](teorie/data-o-uspechu.md#krivka-preziti-proc-se-sance-zlepsuji-s-patou-hrou) · [Přežít jako studio](teorie/prezit-jako-studio.md#stesti-dovednost-a-veci-ktere-cisla-neukazou)

### SVD

**Singular Value Decomposition: každá matice — bez ohledu na tvar a symetrii — je rotace → škálování se změnou dimenze → rotace.**

„Velké finále" lineární algebry: A = UΣVᵀ, kde U a V jsou rotace (singulární vektory) a Σ nese singulární hodnoty. Geometricky posílá koule na elipsoidy; prakticky stojí za kompresí obrázků (low-rank aproximace) i PCA.

Kde se s tím potkáš: [Lineární algebra vizuálně](teorie/linearni-algebra-vizualne.md)

### Sync marker

**Značka v animaci (typicky došlap L/R), podle které se synchronizují klipy různých délek při blendování.**

Bez markerů se walk/run/sprint v blend space fázově rozjedou a mix „plave". Markery musí mít **stejná jména** napříč klipy (L, R) — stažené animace je často nemají a je potřeba je doplnit ručně podle došlapů.

Kde se s tím potkáš: [Základy pohybu](praxe/pohyb-zaklady.md)

### Tagy

**Štítky hry na obchodní platformě; primárně vstup pro doporučovací algoritmus, ne popis pro zákazníka.**

Vybírají se obráceně, než by člověk čekal: najdi hru se stejným publikem a opiš si její tagy, protože cílem je dostat se v databázi vedle správných her. Nejčastější chyba je použít nejgeneričtější tagy (promarníš místo) — a poznávacím znamením špatných tagů jsou nesourodé hry v sekci doporučení.

Kde se s tím potkáš: [Steam stránka: screenshoty a tagy](teorie/steam-stranka.md)

### Synkopa

**Akcent na nepřízvučnou dobu; hlavní koření rytmické proměny.**

Přesun not z přízvučných dob na „mezidoby" oživí mrtvou melodii. Dobrý rytmus balancuje opakování a proměnu — a synkopa je nejlevnější způsob, jak dodat proměnu.

Kde se s tím potkáš: [Jak psát melodie](hudba/melodie.md)

### Telemetrie

**Sběr dat o tom, co hráči ve hře skutečně dělají — lokálně (čítače, achievementy) i vzdáleně (analytický backend).**

Lokální patro: activity tracker — gameplay tagy hlášené centrální funkci, dispatcher pro odběratele, mapa tag→počet. Vzdálené patro: plugin (TrackEdge) + backend (PostHog): person properties, eventy s vlastnostmi, sessions s trváním, dashboardy. K vydání patří privacy rozvaha (poloha, GDPR). Telemetrie je chování, ne slova — sesterská měna „the gap".

Kde se s tím potkáš: [Telemetrie](praxe/telemetrie.md) · [Idea iceberg](teorie/rady-z-praxe.md)

### Tessellation

**Dělení geometrie na jemnější trojúhelníky, aby povrch unesl víc detailu.**

V Mesh Terrainu ve dvou podobách: adaptivní teselace texture modifieru (zjemní síť tam, kde height mapa nese detail, řízeno error tolerancí) a Tessellate režim remesh modifieru. Protiklad k uniformnímu remeshi: adaptivní přístup šetří trojúhelníky, ale hůř se predikuje výsledný tvar. Obecná rada z praxe: hrubé tvarování s teselací vypnutou, detail zapínat cíleně na konci.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Timeline

**Blueprint uzel s křivkami v čase: Play/Reverse/Finished — animace hodnot bez animačního assetu.**

Float track 0→1 + Lerp = pohyb A→B (linear klíče = konstantní rychlost, Auto = ease); looping track 0→360 = rotace. Ping-pong vzor: na Finished přečti Direction enum a zavolej Reverse/Play. Set Timeline Length za běhu mění tempo — délka nad poslední klíč vyrábí pauzu v krajní poloze. Latentní uzel — jen v event graphu, ne ve funkcích.

Kde se s tím potkáš: [Pasti a arénové mechaniky](praxe/pasti-a-mechaniky.md)

### Tónina

**Domovská stupnice skladby — tón a stupnice, ke kterým vše tíhne.**

V piano rollu ji nastavíš přes scale highlighting; „špatné" tóny pak zmizí z dohledu a skládáš skoro naslepo po zvýrazněných. C dur a A moll mají stejné tóny, liší se právě cítěným domovem.

Kde se s tím potkáš: [Základy hudební teorie](hudba/hudebni-teorie-zaklady.md)

### Toon shading

**Stylizované stínování v ostrých pásech (cel shading) — od 5.8 vestavěný shading model přes Substrate Toon BSDF.**

Toon Profile asset řídí diffuse/specular rampu (počet, pozice a tvrdost pásů) a offset textury (halftone, malířský rozpad). Není to post-process — nasazuje se per materiál; největší výhoda proti ručním cel shaderům: správně reaguje na barevná světla, více světel i Lumen.

Kde se s tím potkáš: [Materiály](praxe/materialy.md)

### Trajektorie

**V Motion Matchingu spočítaná historie a predikce pohybu postavy — modrá budoucnost, červená minulost.**

Každý frame se z rychlosti a vstupu predikuje, kde postava bude (+0,35/0,7/1 s) — a proti tomu se matchují animace. Nezaměňovat s traversal (detekce překážek) ani s intentem (co hráč chce = vstup; trajektorie = co se asi stane). Generuje ji Character Trajectory komponenta nebo Pose Search Generate Trajectory; debug: `a.CharacterTrajectory.Debug 1`. Expozice trajektorie gameplayi umí předpovědět zastavení či budoucí rychlost.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md)

### Traversal

**Překonávání překážek (vault, mantle, hurdle) — v GASP detekce hran + výběr animace podle stavu a překážky.**

Vzor z GASP: spline/trace detekce překážky → chooser (hurdle/vault/mantle podle typu a výšky) → montáž s Pose Search Branch In oknem + motion warping na hranu (get-to-bone, interaction transform přes blueprint channel ve schématu). Funguje jen na Traversable blocích; komunitní komponenty (AC_TraceTraversal) ho naučí šplhat i na běžnou geometrii — zákaz per objekt tagem.

Kde se s tím potkáš: [Systémy nad MM](praxe/mm-systemy.md) · [GASP](praxe/gasp.md) · [Parkour postaru](praxe/parkour-vault.md) · [MM základy](praxe/mm-zaklady.md)

### Triáda

**Nejzákladnější akord ze tří tónů: základ, tercie a kvinta.**

Rozestupy určí barvu: 4+3 půltóny = durová, 3+4 = mollová, 3+3 = zmenšená. Postavíš-li triádu na každém stupni stupnice, dostaneš pevný vzorec durových, mollových a zmenšených akordů.

Kde se s tím potkáš: [Základy hudební teorie](hudba/hudebni-teorie-zaklady.md)

### Trigger volume

**Neviditelná zóna v levelu, která při vstupu hráče (či jiné entity) spustí událost.**

Základní nástroj skriptovaných momentů: rozhovor NPC na tržišti, změna hudby, otevření cesty, cinematika na správném místě. Designové pravidlo: nejdřív otázky „jaký zážitek, jaká emoce, jaká informace, jaká další akce?" — trigger je jen doručovací mechanismus. V UE odpovídá trigger box/volume s overlap eventy (viz praxe: interakce bez Event Ticku).

Kde se s tím potkáš: [Vedení hráče](teorie/vedeni-hrace.md) · [Interakce bez Event Ticku](praxe/interakce-bez-event-ticku.md)

### Trim sheet

**Sdílená textura z pásů detailů (římsy, sokly, hrany), po kterých se mapují UV mnoha různých assetů.**

Jedna textura obslouží stovky modelů — draw calls i VRAM klesají řádově. Varianta baked bevel (TLOU): modely hard-edge v 90° úhlech a všechno zaoblení dodá normal mapa trimu. Bonusové triky: UV přeložené přes roh trimu = falešný bevel bez geometrie, bílý trim + color parametr = přebarvitelnost. Základ produkce od The Ascent po San Francisco 1:1.

Kde se s tím potkáš: [Breakdowny](praxe/env-breakdowny.md)

### TSR

**Temporal Super Resolution — upscaler UE5; nejčastější viník „rozmazané" vody a jemných pohyblivých detailů.**

Viewport typicky běží na 80–90 % screen percentage a TSR dopočítává — pohyblivá hladina pak ghostuje a smearuje. Diagnóza: screen percentage 100 % (či 125–200 %) a porovnat. Léčba: jiná AA metoda přes console variable, tonemapper sharpen 0,5–1, a hlavně vyhnout se upscalingu, kde to jde.

Kde se s tím potkáš: [Nástroje: EasyWaterscape](praxe/nastroje-voda.md)

### Tři C

**Character, camera, controls — trojice, kterou žánr definuje: koho ovládáš, odkud se díváš, čím to řídíš.**

Průmyslový termín; ve velkých studiích existují vyhraněné 3C designérské role. „Platformer" nebo „RTS" v hlavě okamžitě vykreslí všechny tři C — proto jsou to žánry; „roguelike" nevykreslí žádné — proto je to mód.

Kde se s tím potkáš: [Žánry očima designéra](teorie/zanry.md)

### Tutorial hell

**Smyčka „sleduju tutoriály, umím je zopakovat, ale sám nepostavím nic" — nejčastější past učení enginu.**

Sledování není učení. Útěk je vždycky stejný: po každém tutoriálu zavřít video a postavit něco malého vlastního s tím, co ses právě naučil. Mezera mezi následováním kroků a vlastním myšlením se zavírá jen malými dokončenými projekty — dveře, mince, postava s damage.

Kde se s tím potkáš: [Tipy do editoru](praxe/editor-tipy.md) · [Začátky bez zkušeností](teorie/zacatky-bez-zkusenosti.md)

### Typografie

**Řemeslo práce s písmem: volba řezů, jejich role v hierarchii textu a pravidla, kdy se který používá.**

Praktické minimum pro hru: dva fonty s jasnou rolí (nadpisy, tělo), a každý další styl — tučné, kurzíva, jiný řez — jen s důvodem, který platí v celé hře. Kurzíva vyhrazená pro flavor text hráči napoví, že tohle nemusí číst kvůli hraní; tučné klíčové slovo naopak říká, že tohle je mechanika.

Kde se s tím potkáš: [Typografie](teorie/typografie.md) · [Art specializace: UI](teorie/art-specializace.md)

### Two-loop rule

**Aranžérské pravidlo: každé dva loopy hlavního nástroje uděláš nejvýš dvě změny.**

Změna = přidat nástroj, ubrat nástroj, přidat výraz, ubrat výraz. Mechanické lešení, které rozhýbe loop v píseň, aniž bys musel „vymyslet aranž".

Kde se s tím potkáš: [Aranžmá: z loopu skladba](hudba/aranz.md)

### Type 2 fun

**Zábava, která bolí teď a těší až ve vzpomínce: námaha a peril, na které jsi hrdý.**

Z třístupňové Fun Scale (Newberry): Type 1 baví hned, Type 2 až zpětně (výstup na horu, soulsovka), Type 3 je „zábava, co se pokazila" — a rage hry ji vyrábějí schválně. Co je pro jednoho Type 2, je pro jiného Type 3; volba publika, ne kvality.

Kde se s tím potkáš: [Zábava: taxonomie a pilíře](teorie/zabava.md) · [Obtížnost a výzva](teorie/obtiznost.md)

### Unison

**Navrstvení více kopií téže vlny na jednu notu; rozšíří zvuk do sterea.**

Tři noty × 10 hlasů unisonu = 30 pil přes sebe. Nejvíc těží pila. Slavný supersaw je pila s vysokým unisonem protažená filtrem.

Kde se s tím potkáš: [Syntéza zvuku od nuly](hudba/synteza-zvuku.md)

### User story

**Popis funkce jako kroky uživatele: co vidí a co dělá — ne jak je to naprogramované.**

Termín ze softwarového vývoje, který se hodí i do GDD: pitch Diabla obsahuje pasáž „hráč vede postavu po cestě do opuštěného chrámu, počítač vygeneruje první patro…" — krok za krokem zážitek hráče. Dobrý test srozumitelnosti návrhu: jde odvyprávět jako user story?

Kde se s tím potkáš: [GDD: dokument není smlouva](teorie/gdd.md)

### USP

**Unique selling point: co má jen tvoje hra — důvod koupit ji, a ne konkurenci.**

Uklidňující lekce z historie: USP nemusí existovat od začátku. GTA vyrostlo z tech dema o streamování velkého města a všechen „GTA flavor" se nastěhoval po letech; unikátnost se do projektu dá dovézt i pivotem nebo škrtem.

Kde se s tím potkáš: [GDD: dokument není smlouva](teorie/gdd.md) · [Co prodává](teorie/co-prodava.md)

### Utility AI

**Rozhodovací rámec, kde si každý úkol spočítá skóre a spustí se ten s nejvyšším.**

Není to plugin ani kód, ale způsob návrhu — a nenahrazuje behavior trees ani state trees, používá je jako výkonnou vrstvu. Skóre není konstanta, ale součet důvodů (počet nepřátel, zdraví, vzdálenost, povaha), takže z týchž úkolů vznikne se zbabělcem jiné chování než s veteránem. Škáluje tam, kde by strom podmínek přestal být čitelný.

Kde se s tím potkáš: [Základy AI](praxe/ai-zaklady.md#utility-ai-rozhodovani-podle-skore-misto-vetveni) · [State Trees](praxe/state-trees.md) · [Rejstřík: GOAP](#goap)

### UX

**User experience: informační architektura hry — kde informace bydlí a kolika kroky se k nim hráč dostane.**

Předchází UI: nejdřív se mapuje cesta hráče a minimalizuje počet nutných akcí, teprve pak se staví vizuál. U malých týmů je to jedna role, a právě proto se vyplatí držet obě zadání oddělená — jinak se optimalizuje vzhled obrazovky, která neměla vzniknout.

Kde se s tím potkáš: [Art specializace: UI a UX](teorie/art-specializace.md) · [První dojem](teorie/prvni-dojem.md)

### Value chain

**Hodnotový řetězec (Dan Cook): smysl a zábavnost sběrné činnosti nedává činnost sama, ale její zamýšlené použití dál v řetězci.**

Sbírání klacíků nudí, dokud z nich hráč nestaví něco, co sytí fantazii hry — pak se každé rozhodnutí „co sebrat" stává plánováním. Prakticky: nudnou mechaniku neoživuj pozlátkem, dej jí destinaci. Cíl řetězce zpětně obarvuje všechny jeho články.

Kde se s tím potkáš: [Smyčky a řetězce](teorie/smycky-a-retezce.md)

### Vektor

**Dvojice/trojice čísel se dvěma čteními: bod v prostoru (pozice), nebo směr s velikostí (velocity, síla).**

Rozlišení užití chrání před nesmysly: pozice + vektor = nová pozice, pozice − pozice = vektor „odsud tam", pozice + pozice = nesmysl. Z pár operací padá celý pohyb (Eulerova integrace: pozice += velocity·dt) i dotazy na svět (dot product).

Kde se s tím potkáš: [Matematika pro gamedev](teorie/matematika-pro-gamedev.md)

### Value curve

**Profil hry přes dimenze appealu: na čem stojí, na čem ne — a s kým se tím pádem vlastně měří.**

Rozepiš, co hru prodává (téma, mechanický hook, atmosféra…), oskóruj důležitost a polož vedle konkurence: klon trefující stejné kolonky nemá důvod existovat. Lepší 1–2 výjimečnosti (jedna neobvyklá) než všechno na sedm z deseti.

Kde se s tím potkáš: [Engineering experiences](teorie/engineering-experiences.md) · [Rady z praxe: idea iceberg](teorie/rady-z-praxe.md)

### Version control

**Verzování projektu (typicky Git): každá změna se ukládá jako commit, ke kterému se lze kdykoli vrátit.**

Dvě služby: záchranné lano z každé katastrofy a viditelná historie pokroku (protilék na „nic nestíhám"). Zásada zrnitosti: commituj malé celky s popisnou zprávou — velký commit se špatně popisuje, vrací i slučuje. UE specifika: Blueprinty jsou binární (diff neuvidíš, zpráva je vše), na velké assety Git LFS, v editoru vestavěná integrace Revision Control.

Kde se s tím potkáš: [Start projektu](teorie/jak-zacit.md)

### Vizuální hierarchie

**Uspořádání scény tak, aby nejdůležitější informace byla nejsnáze vidět.**

Vzniká kontrastem — v tvaru, velikosti, barvě, saturaci i míře detailu. Kontraintuitivní jádro: fokus se nedělá zvýrazněním jednoho místa, ale potlačením všech ostatních (na šachovnici, kde má stejný kontrast všechno, oko nemá kde přistát). Postup je dvoukrokový: nejdřív informační hierarchie (co je jak důležité), pak její překlad do vizuálních prostředků.

Kde se s tím potkáš: [Herní art: pipeline](teorie/art-pipeline.md) · [Vizuální komunikace](teorie/vizualni-komunikace.md) · [Prostor a hranice](teorie/prostor-a-hranice.md)

### Vertical slice

**Reprezentativní výsek hry ve finální kvalitě — brána mezi prototypem a plnou produkcí.**

Ne nutně začátek hry: libovolných 5–60 minut zážitku, na kterém se poprvé potkají mechaniky z prototypu, art style a tón. Otázka, na kterou odpovídá: nadchne lidi reprezentativní ukázka natolik, aby se vyplatilo vyrábět zbytek obsahu? U komplexních her se skládá z ~60 % žánrových standardů a ~40 % inovací — testovat jde jen to nové.

Kde se s tím potkáš: [Prototypování a vertical slice](teorie/prototypovani.md) · [Základy designu](teorie/zaklady.md) · [Zápisky: cut line](zapisky/cut-line.md)

### Virtual bone

**Kost existující jen v enginu — přidá se na skeleton (Add Virtual Bone) bez re-exportu z DCC nástroje.**

Sleduje transform zdrojové kosti vůči jiné; typické použití: IK cíle (foot IK pro skeleton, který IK kosti nemá — MetaHuman) a odvozené sockety. Rychlá cesta, jak cizímu skeletonu doplnit, co rig očekává.

Kde se s tím potkáš: [MetaHuman v praxi](praxe/metahuman.md)

### Virtual Shadow Maps

**Stínový systém UE5 navržený pro Nanite a Lumen — vysoké rozlišení bez ručního ladění kaskád.**

Nahrazuje klasické cascaded shadow maps: stíny se počítají po dlaždicích a v rozlišení, které odpovídá tomu, co je vidět. Prakticky to znamená ostré stíny zblízka i v dálce bez typického přeskakování kaskád. Je to doporučené nastavení všude, kde běží Nanite — s nímž si naopak ray traced shadows nerozumí.

Kde se s tím potkáš: [Osvětlení: malovat světlem](praxe/osvetleni.md#malovat-svetlem-scena-slozena-z-falesnych-svetel) · [Rejstřík: Nanite](#nanite)

### Virtual texture

**Textura rozsekaná na stránky, které se streamují jen tam, kam se kamera dívá — „Nanite pro textury".**

Pevný pool stránek ve VRAM: při přeplnění nejhůř rozmazání, nikdy out-of-memory. Ulevuje CPU (méně unikátních materiálů) i paměti, daní je page table indirekce — extra GPU čas na každý přístup, takže ne na všechno. Ideální pro obří plochy s kritickým detailem; runtime virtual textures navíc pohánějí blending terénu.

Kde se s tím potkáš: [Textury a DLSS](praxe/textury-a-dlss.md) · [Breakdowny](praxe/env-breakdowny.md)

### Voice leading

**Vedení tónů tak, aby přechody mezi akordy byly co nejjemnější (vedení hlasů).**

Vyhledej tón, který „trčí" a ruší tok, a schovej ho tak, aby sousední akordy sdílely co nejvíc společných tónů. Když akordy plynou hladce, emoce je „z jiného světa".

Kde se s tím potkáš: [Akordy a harmonie](hudba/akordy-a-harmonie.md)

### Voicing

**Způsob, jak rozmístíš tóny akordu — v jakém pořadí a oktávách znějí.**

Základní tvar (root–tercie–kvinta natěsno) zní basicky; zvedneš-li jednu notu o oktávu, dostaneš otevřený voicing s prostornějším zvukem. Stejné noty, jiný dojem — páka, kterou začátečníci přeskakují.

Kde se s tím potkáš: [Akordy a harmonie](hudba/akordy-a-harmonie.md)

### Volumetric fog

**Objemová mlha: světlo se rozptyluje v „hustotě vzduchu" — paprsky, god rays a atmosféra s hloubkou.**

Zapíná se na Exponential Height Fog; tvar řídí scattering distribution, start distance a height falloff. Materiály s domain Volume do ní kreslí vlastní objemy (mlha Silent Hill 2). Kvalita: r.VolumetricFog.GridPixelSize (default 8, nižší = jemnější) a GridSizeZ (128 → 256/512, ten dražší).

Kde se s tím potkáš: [Osvětlení](praxe/osvetleni.md) · [Stavba prostředí](praxe/env-tvorba.md)

### Oblique

**Perspektiva, ve které je scéna nakloněná tak, že vidíš horní i boční stranu objektů.**

Perspektiva her jako Harvest Moon nebo Stardew Valley — není to čistý pohled shora, ale ani izometrie. Rozdíl proti izometrii je v tom, jak se osy sbíhají; prakticky se volí tam, kde je potřeba čitelný půdorys a zároveň rozpoznatelné postavy zpředu.

Kde se s tím potkáš: [2D vizuál: izometrie](teorie/2d-vizual.md)

### Water Body

**Actor Water pluginu: ocean, lake, river, island — vodní tělesa tvarovaná splinami, vzájemně propojitelná.**

Klávesa G ukáže spline pointy; řeka má rychlost proudu per point (alt+tažení přidává body). Vztah k terénu řeší Edge Offset / Channel Edge Offset a falloff mode (Angle→Width proti hřebeni u břehu); landscape drž ~1 cm nad nulou. Vestavěné: waterline efekt kamery a podvodní post-process.

Kde se s tím potkáš: [Voda a buoyancy](praxe/voda-a-buoyancy.md) · [Interaktivní voda](praxe/interaktivni-voda.md)

### Wave Function Collapse

**Procedurální generátor: každé políčko je superpozicí všech dlaždic a „pozorování" ho zkolabuje podle pravidel sousedství.**

Metafora z kvantové mechaniky, mechanika ze sudoku: vyber políčko, zkolabuj na dlaždici konzistentní se sousedy (silnice navazují), opakuj. Výsledek náhodný, a přitom soudržný — nekonečné mapy bez ruční práce a bez generativní AI.

Kde se s tím potkáš: [Algoritmy, které stojí za to znát](teorie/algoritmy-prehled.md) · [PCG: základy a nástroje](praxe/pcg-zaklady.md)

### WIP limit

**Strop rozdělané práce v kanbanu: jedna, maximálně dvě karty v Doing na osobu.**

„Kdo tvrdí, že právě dělá tři věci, v podstatě lže — jednu dělá a ostatní ignoruje, nebo mezi nimi těká." Limit dělá z prostředního sloupce pravdivý komunikační kanál: tým vidí, na čem kdo dnes opravdu je, a pozná, kdo je volný.

Kde se s tím potkáš: [Plánovací nástroje](teorie/planovani-nastroje.md) · [Žrouti času](teorie/produktivita.md)

### Wishlist

**Přání na Steamu — před vydáním hlavní měřítko zájmu o hru a palivo algoritmu viditelnosti.**

Wishlisty pohánějí doporučování a rozhodují o síle launche; Steam Next Fest funguje jako jejich multiplikátor. Zároveň pozor na „the gap": wishlist je zdvořilý zájem, nákup je závazek — konverze není samozřejmá. V žebříčku důkazů síly nápadu stojí wishlisty vysoko, ale pozdě; validovat jde mnohem dřív a levněji.

Kde se s tím potkáš: [Postmortem ShantyTown](teorie/postmortem-shantytown.md) · [Idea iceberg](teorie/rady-z-praxe.md)

### World Partition

**Streamovací systém UE5: svět rozdělený na buňky, které se nahrávají a uvolňují podle vzdálenosti či logiky.**

Nahrazuje starší ruční level streaming; open world level je level s aktivním World Partition. Mesh Terrain na něm závisí — terén existuje jako partition chunky viditelné ve World Partition okně, kde jde s regiony pracovat (load/unload) i během editace, což šetří paměť při práci na velkých plochách.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Zákon opaků

**Marketingová technika: najdi slabinu, na kterou si stěžují fanoušci žánru, odstraň ji a postav na tom svůj slib.**

Případovka: survival hra si všimla, že hráči mají dost mechaniky hladovění, vyřadila ji a udělala z toho hlavní sdělení — hra zůstala z devadesáti procent žánrová a prodávala se tou jednou změnou. Působí to jako honba za trendem, ale je to opak: vidíš, čeho mají lidé dost, a jdeš před ně.

Kde se s tím potkáš: [Co prodává: zákon opaků](teorie/co-prodava.md) · [Žánry očima designéra](teorie/zanry.md)

### Yomi

**Čtení soupeřovy mysli jako herní dovednost: vím, že on ví, že já vím — a přesně o tom je vrcholné hraní.**

Termín z fighting her: mind game nad mechanikami. Šachy proti dítěti nebaví, protože Yomi předpokládá sdílené porozumění; skryté karty (Scythe) jsou konfrontačnější než kostky, protože hraješ proti mysli, ne proti hodu.

Kde se s tím potkáš: [Engineering experiences](teorie/engineering-experiences.md)

### Yoink & twist

**Vzorec tvorby nápadu: vezmi žánr s prokázaným publikem (yoink) a přidej vlastní vylepšení nebo obrat (twist).**

Protiklad honby za stoprocentní originalitou, která znamená nulovou validaci trhu a chybějící referenční body. Rozhodovací pravidlo: v mladém žánru stačí být *lepší* (oprav pár bolestí z negativních recenzí — Fields of Mistria vs. Stardew Valley), ve starém žánru musíš být *jiný* (Age of Empires neporazíš kvalitou). Twist často stojí jen reskin a fikci — v kódu se nemusí změnit nic.

Kde se s tím potkáš: [Nápad: yoink & twist](teorie/napad.md) · [Prototypování: standardy vs. inovace](teorie/prototypovani.md)

### Zázněj

**Pomalé kolísání hlasitosti, když spolu znějí dvě skoro stejné frekvence (beating).**

Vzniká střídavým sčítáním a odečítáním vln („wa-wa-wa"). Čím dál od sebe frekvence, tím rychlejší kolísání, až se z něj stane obecná drsnost — jedna ze dvou příčin pásma nepohody mezi tóny.

Kde se s tím potkáš: [Fyzika souzvuku](hudba/fyzika-souzvuku.md)

### Zero indexing

**První prvek má index 0: lidské „první" je strojová nula — a na záměně padly nespočetné hodiny ladění.**

Konvence většiny jazyků (i UE polí): n-tý prvek sedí na indexu n − 1. Klasický důsledek je off-by-one chyba — smyčka o jedno projede či nedojede. Kdykoli sáhneš po indexu, řekni si nahlas, jestli počítáš od nuly.

Kde se s tím potkáš: [Programátorské myšlení](teorie/programatorske-mysleni.md)
