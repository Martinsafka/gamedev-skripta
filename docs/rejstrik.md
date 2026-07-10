# Rejstřík

Odborné termíny napříč skripty — **termín anglicky, výklad česky**, protože přesně tak se s nimi potkáš v editoru, dokumentaci i komunitě. Rejstřík má dvě vrstvy: každý výskyt termínu kdekoli na webu má automatický tooltip s krátkou definicí a tahle stránka přidává hloubku a odkazy do kapitol, kde termín žije v kontextu.

Rejstřík roste s obsahem — každé zpracované video sem přidává svoje pojmy.

---

### Abstract class

**Třída, kterou nejde umístit do světa ani vybrat v referencích — existuje jen jako rodič pro děti.**

U base class v Blueprintech se zapíná v `Class Settings → Generate Abstract Class`. Smysl: master má nést jen data a logiku, žádné meshe či materiály — cokoli master referencuje, se nahrává do paměti s každou referencí na něj. Abstraktní master nikdo omylem nespawne a size map zůstává štíhlá.

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md)

### Affordance

**Vlastnost objektu či prostoru, která signalizuje, jak s ním jde interagovat — dřív, než to hráč zkusí.**

Pojem z designové psychologie (Gibson, Norman): klika říká „stiskni", římsa říká „vylez". V level designu se affordances vyrábějí světlem, kompozicí a kontrastem — tajná odbočka musí *vypadat* zajímavě a interaktivně, jinak ji hráč mine. Zrádné jsou falešné affordances: co vypadá průchozí a není, rozbíjí důvěru (viz invisible wall).

Kde se s tím potkáš: [Prostor a hranice](teorie/prostor-a-hranice.md) · [Vedení hráče](teorie/vedeni-hrace.md)

### Anim montage

**Animační asset pro jednorázové akce (útok, interakce), přehrávaný přes sloty do vybraných částí skeletu.**

Nad Motion Matchingem je montáž základ combatu: spodní tělo matchuje locomotion, horní hraje montáž ve slotu Upper Body (Layered Blend Per Bone + Blend Poses by Bool). Anim notifies uvnitř montáže řídí comba (AddCombo/ResetCombo okna); sloty pro zbraně patří do vlastní slot skupiny, ať výměna nepřeruší jiné montáže. Pro matchování do montáže slouží Pose Search Branch In.

Kde se s tím potkáš: [Systémy nad MM](praxe/mm-systemy.md) · [MM základy](praxe/mm-zaklady.md)

### Asset pack

**Balík hotových assetů — modely, zvuky, UI, shadery — připravený k okamžitému použití.**

Pro sólo vývojáře nástroj přežití: 50 hodin vlastního lokalizačního toolkitu vs. hotový asset za pár desítek dolarů je reálná volba z praxe. Kupuje se to, co dělat neumíš nebo nechceš; vlastní ruce si šetři na to, čím se hra liší. Při prototypování asset packy dodají vizuál a vibe za nulový čas — a u „design by constraint" umí být rovnou zdrojem nápadu („šla by kolem tohohle jediného assetu postavit hra?").

Kde se s tím potkáš: [Žrouti času](teorie/produktivita.md) · [Nápad](teorie/napad.md) · [Scope](teorie/scope.md)

### B-roll

**Doplňkové záběry, které běží na obrazovce, zatímco mluvíš o něčem obecnějším — ve videích o hrách typicky záběry gameplaye.**

Pravidlo devlogů: na obrazovce má být hra, pořád — ideálně přesně to, o čem zrovna mluvíš, jinak aspoň obecný B-roll. Chytrý zdroj záběrů starších verzí hry: version control — checkout starého commitu a natoč, co potřebuješ.

Kde se s tím potkáš: [Devlogy](teorie/devlogy.md)

### Blend stack

**Anim uzel, který při každé změně animační proměnné přidá nový blend do zásobníku — bez state machine.**

Základ, na kterém Motion Matching stojí: uvnitř MM uzlu běží graf per vybraná animace (tam žije orientation warping, steering…). Varianty: obyčejný blend stack (animace z proměnné), Chooser Player (animace z chooser tabulky, umí i stitch) a hybridní setup se state machine. Max počet současných blendů je konfigurovatelný.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md)

### Blockout

**Hrubá stavba levelu z primitivních tvarů — testuje prostor, metriky a flow dřív, než přijdou finální assety.**

Blockout disciplína: grid/metrické materiály (okamžitě vidíš, že vchod je úzký nebo skok dlouhý), konzistentní barevný jazyk (cover jedna barva, traversal jiná) a „level design gym" — referenční mapa metrik sdílená napříč levely. Startovní bod hráče a hlavní landmark se rozhodují ještě před blockoutem.

Kde se s tím potkáš: [Prostor a hranice](teorie/prostor-a-hranice.md) · [Prototypování](teorie/prototypovani.md)

### Blueprint Function Library

**Sbírka funkcí volatelných z libovolného blueprintu v projektu.**

Ideální pro helper funkce, které nepatří žádné konkrétní třídě: bezpečný přístup ke gameplay tag containeru libovolného actora, pure getter na Game Instance, zápis aktivit. Pure funkce bez side effectů se v grafu chovají jako čisté dotazy. Pravidlo: co voláš ze tří míst, patří do funkce; co voláš ze tří blueprintů, patří do library.

Kde se s tím potkáš: [Gameplay Tags](praxe/gameplay-tags.md) · [Ukládání](praxe/ukladani.md) · [Organizace projektu](praxe/organizace-projektu.md)

### Blueprint Interface

**Sada deklarovaných funkcí bez implementace — kontrakt, který si každý Blueprint naplní po svém.**

Volající posílá zprávu (message call) na libovolný actor; pokud actor interface implementuje, zareaguje vlastní logikou, pokud ne, nestane se nic — žádný pád, žádná závislost. Je to enginová podoba principu „programuj proti rozhraní": character nemusí znát třídu dveří, truhly ani panelu, stačí mu smlouva „umíš interagovat?". Přidání nového typu interaktivního objektu pak neznamená žádnou změnu ve volajícím.

Kde se s tím potkáš: [Interakce bez Event Ticku](praxe/interakce-bez-event-ticku.md)

### Boolean

**Geometrická operace kombinující dvě tělesa: sjednocení (union), rozdíl (subtract), průnik (intersect).**

Pojmenováno po booleovské logice — tělesa se skládají jako množiny bodů. V Mesh Terrainu boolean modifier skutečně vroubuje cizí mesh do terénu: union přiroste, subtract vyřízne díru a geometrie se na okrajích sešije. Klasický nástroj CSG modelování (Constructive Solid Geometry), který znáš z Blenderu i CADů.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Call to action

**Závěrečná výzva trailer u nebo videa: co má divák udělat teď — „Wishlist on Steam", „Demo out now".**

Formát pro herní trailer: 5–8 vteřin na konci, key art + název + jedna výzva. Právě jedna — dvě CTA najednou („demo + wishlist") si konkurují a oslabují se. V širším marketingu platí totéž pro každý kanál: post, devlog i stránka mají mít jeden jasný další krok.

Kde se s tím potkáš: [Steam stránka](teorie/steam-stranka.md)

### Capsule

**Náhledový obrázek hry na Steamu — miniatura, kterou zákazník vidí ve všech seznamech dřív než cokoli jiného.**

Nejdůležitější kus grafiky celé stránky. Zásady: žádné AI generované umění, custom nebo semi-custom logo (volný font + gradient + tematický detail), silný kontrast textu vůči pozadí, žádný text kromě názvu hry, nekolidovat se Steam badgi (Demo) — a rámeček, který capsule vysekne ze seznamu. Rozbory dobrých a špatných: steamcapsule.com.

Kde se s tím potkáš: [Steam stránka](teorie/steam-stranka.md) · [Co prodává](teorie/co-prodava.md)

### Cast

**Přetypování obecné reference na konkrétní třídu, aby šlo volat její specifické funkce.**

`Cast To DestroyDoor` řekne enginu „zkus s tímhle actorem zacházet jako s třídou DestroyDoor". Cena: volající Blueprint získává tvrdou závislost na cílové třídě (a tahá si její referenci do paměti), takže s každým novým typem objektu roste řetěz castů. Tam, kde jde jen o „pošli zprávu, kdo umí, zareaguje", je lepší Blueprint Interface.

Kde se s tím potkáš: [Interakce bez Event Ticku](praxe/interakce-bez-event-ticku.md)

### Channel

**V Mesh Terrainu pojmenovaná materiálová vrstva terénu — nástupce landscape layers.**

Channels se definují v data assetu partition definice 1:1 podle vrstev materiálu a rovnou se z nich stávají malovatelné vrstvy, bez ceremonie layer info assetů starého Landscape. Navíc je umí přiřazovat i modifiery (weight channel) — boolean skála si tak vyřízne tvar a zároveň obarví materiál. Pozor na kolizi názvosloví: UE má i kolizní channels (WorldStatic, Pawn…), to je jiný mechanismus.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Chooser

**Datová tabulka „když platí tyhle podmínky, vyber tenhle asset" — v MM přepíná databáze, obecně vybírá cokoli.**

Řádky = kandidáti (PSD, montáže, nested choosery), sloupce = podmínky (bool, enum, float range) bindnuté na proměnné AnimBP. V MM: databáze jako Dynamic value, On Update → Evaluate Chooser (All Results) → Set Databases To Search + Interrupt on database change. Umí i output sloupce (damage per útok). Plně integrovaný s rewind debuggerem.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md) · [Systémy nad MM](praxe/mm-systemy.md)

### Cipher

**Typ hráčské postavy: prázdná nádoba bez vlastní osobnosti, hlasu a motivací — oživuje ji hráčova imaginace.**

Jeden ze čtyř typů protagonisty (cipher · fixní · customizovatelný · customizovatelný s fixním základem). „Bez osobnosti" není vada: mlčící postava v puzzle hrách (Half-Life, Tunic) nechává znít hlas v hráčově hlavě. Cena: veškerá tíha charakterizace jde do vizuální komunikace — jak postava vypadá a co reprezentuje. Praktické pravidlo: umíš psát → fixní postava; umíš vyrábět cool věci, ale ne psát → cipher.

Kde se s tím potkáš: [Příběh a postavy](teorie/pribeh-a-postavy.md)

### Cold open

**Otvírák traileru: prvních 10–15 vteřin nabitých highlighty v rychlých střizích, teprve pak volnější tempo.**

Pojem z filmového střihu (a trailerového řemesla Dereka Lieu). Důvod jsou retention grafy: velká část diváků odpadne během první půlminuty — kdo šetří nejlepší záběry na konec, ukáže je prázdnému sálu. Pravidla k tomu: celková délka 30–50 s, žádný záběr přes ~6 vteřin, na konci call to action.

Kde se s tím potkáš: [Steam stránka](teorie/steam-stranka.md)

### Collision preset

**Předpis, jak objekt reaguje na jednotlivé kolizní kanály: Block, Overlap, nebo Ignore.**

Preset je první a nejlevnější filtr kolizního systému — rozhoduje se ještě před jakoukoli herní logikou. Trigger nastavený „Ignore all, Overlap jen WorldStatic/WorldDynamic/Pawn/PhysicsBody" negeneruje eventy o věcech, které tě nezajímají. Vlastní (Custom) preset se vyplatí kdykoli, kdy výchozí profily neodpovídají roli objektu.

Kde se s tím potkáš: [Interakce bez Event Ticku](praxe/interakce-bez-event-ticku.md)

### Context steering

**Technika pohybu AI: entita průběžně hodnotí všechny směry vahami a vybírá nejlepší proveditelný.**

Vylepšení klasických steering behaviors (boids), jejichž protichůdné vektory se umí vyrušit — AI pak zamrzne u zdi, místo aby ji obešla. Context steering drží ohodnocení celé růžice směrů (typicky přes dot product vůči kýženému směru); zablokovaný nejlepší směr prostě nahradí druhý nejlepší. Tvarováním vah vznikají chování jako kroužení kolem cíle nebo nájezdy a odskoky — základ soubojů, které jsou zábavné pohybem, ne čísly.

Kde se s tím potkáš: [Game feel a imerze](teorie/game-feel.md)

### Continuing pose

**„Co by hrálo dál, kdybych nic neměnil" — kandidát, kterého musí každá nová animace v Motion Matchingu porazit cenou.**

Klíč k ladění MM: v pose search debuggeru vidíš cenu continuing pose vedle vítěze a channels breakdown řekne, který kanál rozhodl. Continuing pose cost bias (záporný) drží systém déle v jedné animaci; notify tag Override Continuing Pose Bias protlačí hezkou animaci, i když matematicky nevyhrává.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md)

### Core loop

**Základní smyčka činností, kterou hráč ve hře opakuje nejčastěji — jádro, na kterém všechno ostatní stojí.**

„Plíž se → pozoruj → proklouzni" nebo „těž → vyrob → prodej". Užitečný pojem při analýze (co hráč *reálně* dělá většinu času?) i při ořezávání scope — co nesytí core loop, je kandidát na vyhození. Zároveň platí výhrada z kapitoly o smyčkách: popisuje strukturu, nevysvětluje kvalitu.

Kde se s tím potkáš: [Smyčky a řetězce](teorie/smycky-a-retezce.md) · [Nápad](teorie/napad.md) · [Postmortem ShantyTown](teorie/postmortem-shantytown.md)

### Data asset

**Asset nesoucí čistá strukturovaná data — konfiguraci bez logiky.**

V UE typicky potomek `UDataAsset`: designér edituje hodnoty v editoru, kód/Blueprinty je čtou. Odděluje „co" od „jak" — stejná logika, jiná data, jiné chování. Mesh Terrain v data assetu (Mesh Partition Definition) drží materiál, texel size a definice channels.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md) · [Kolik kódu potřebuješ na start](teorie/co-se-ucit.md)

### Data-driven design

**Princip: hodnoty a konfigurace žijí v datech (data assety, tabulky), logika je jen čte.**

Damage, animace, zvuky ani cooldowny nepatří natvrdo do grafu — patří do data assetu, který ability/systém čte. Fragmenty (malé datové objekty pro volitelné části: animace, VFX, damage) řeší, že ne každá entita potřebuje všechno. Odměna: designér vytvoří novou ability výměnou dat, bez zásahu do logiky. UE Gameplay Ability System je tenhle princip dotažený do konce.

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md) · [Rejstřík: data asset](#data-asset)

### Design by constraint

**Metoda hledání nápadů: nejdřív si zvol omezení, která řežou scope, a nápad nech vzniknout uvnitř nich.**

„Žádný příběh", „celá hra na jedné obrazovce", „žádné viditelné postavy", „jeden level" — omezení zmenší prostor možností tak, že se v něm dá tvořit. Postup: zvol omezení → posbírej hry se stejným omezením jako katalog interakcí → nech omezení třít o téma, dokud nevypadne nápad (piráti × jedna obrazovka = ostrov). Mini Metro tak vzniklo doslova. Druhá půlka metody: každé vývojářské omezení potřebuje player-facing alibi — téma, které ho vysvětlí a prodá.

Kde se s tím potkáš: [Scope: malé hry a design by constraint](teorie/scope.md) · [Prototypování](teorie/prototypovani.md)

### Devlog

**Video (či zápis) o vývoji vlastní hry — marketingový kanál a žánr s vlastním řemeslem.**

Dvě funkční podoby: showcase (rozbor jedné feature: proč → proces → výsledek → limity) a story (příběh vývoje, včetně slepých uliček); nejlepší devlogy obojí mísí. Klíč ke kvalitě je scénář — psaný nahlas, ne jako sloh — a hra na obrazovce po celou dobu. Devlog není povinnost: dělá se, když tě baví videa, ne pro automatické wishlisty.

Kde se s tím potkáš: [Devlogy](teorie/devlogy.md) · [Postmortem ShantyTown](teorie/postmortem-shantytown.md)

### Difficulty curve

**Průběh obtížnosti hry v čase — a hlavní nástroj, jak držet hráče ve flow.**

Skládá se ze dvou složek: novelty (učení nového) a mastery (zvládání naučeného). Šachy mají novelty nafrontovanou na začátek; hry často volí pilový tvar — s každou novou mechanikou schválně klesnou nároky na mastery, aby zbyla kapacita na učení. Doplňkové nástroje: matchmaking, automatické přizpůsobení, skill gates (těžší vstup filtruje nepřipravené) a rubber banding.

Kde se s tím potkáš: [Zábava: flow](teorie/zabava.md)

### Event dispatcher

**Rádio mezi Blueprinty: vlastník dispatcher zavolá, všichni přihlášení posluchači dostanou event.**

Deklaruje se na vysílači; posluchači se bindují (typicky na BeginPlay) a dodávají vlastní custom event. Umí parametry, unbind i více posluchačů najednou — a obrací závislost: vysílač o posluchačích neví. Použití: „stalo se X, koho to zajímá" (dveře otevřeny, cooldown skončil, aktivita zaznamenána). Pozor na race conditions při bindování v BeginPlay — pořadí inicializace actorů není zaručené.

Kde se s tím potkáš: [Komunikace Blueprintů](praxe/komunikace-blueprintu.md) · [Principy architektury](praxe/principy-architektury.md) · [Telemetrie](praxe/telemetrie.md)

### Event Tick

**Blueprint event volaný každý vykreslený snímek.**

Kód v Ticku běží 60× i vícekrát za vteřinu, ať se děje cokoli — je to polling: neustálé kladení otázky, jejíž odpověď se většinou nemění. Občas je nutný (plynulý pohyb, interpolace), ale většina herní logiky patří do eventů, timerů a delegátů, které se spouštějí při změnách. „Dostaň to z Ticku" je jedna z nejčastějších optimalizačních rad v UE — a hlavně rada architektonická.

Kde se s tím potkáš: [Interakce bez Event Ticku](praxe/interakce-bez-event-ticku.md) · [Kolik kódu potřebuješ na start](teorie/co-se-ucit.md)

### Flow

**Stav plného zaujetí činností, kdy výzva přesně odpovídá dovednosti (Mihály Csíkszentmihályi, 1990).**

Podmínky: častá a rychlá zpětná vazba, hluboké soustředění, výzva ~ skill. Tyrollerovo vysvětlení, proč flow kanál funguje: je to pásmo nejlepšího poměru signálu k šumu — ve frustraci vrací svět pořád „špatně" a v nudě pořád „dobře", učit se dá jen tam, kde některé akce fungují a jiné ne. Prakticky: flow = nejefektivnější učení = zábava; frustrace emočně přebije flow, flow přebije nudu.

Kde se s tím potkáš: [Zábava: flow](teorie/zabava.md)

### Game Design Document

**Dokument s návrhem hry (GDD) — funguje jen tehdy, když se do něj tým skutečně vrací.**

Klasická podoba (slohová práce v akademickém formátu) u sólo vývojářů umírá nedopsaná a nečtená. Funkční alternativa je vizuální nástěnka: reference s důvody, levely jako sekvence, mechaniky jako GIFy, centrální to-do. Jediná metrika kvality GDD je, jestli je *živý* — forma je vedlejší.

Kde se s tím potkáš: [Start projektu](teorie/jak-zacit.md)

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

### God class

**Antipattern: třída, do které se postupně nastěhuje logika všech ostatních — a pak s každou změnou padá půl projektu.**

V dědičnosti vzniká z pohodlnosti („dám to do masteru, ať to mají všichni") — jenže kódový zámek jednoho typu dveří nepatří všem dveřím. Pravidlo: rodič nese jen to, co potřebují všechny děti; specifika bydlí v dětech. Příbuzný jev mimo dědičnost: player character s inventářem, questy a UI v jednom grafu — lék jsou komponenty.

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md) · [Organizace projektu](praxe/organizace-projektu.md)

### Graybox

**Prototyp či blockout ze šedých primitivních tvarů — bez artu, bez nálady, jen prostor a mechanika.**

Správné použití: testování mechanik a metrik (gameplay prototyp, level blockout), kde by krása jen zkreslovala zpětnou vazbu. Špatné použití: testování prodejnosti a emoce — šedé kostky žádnou nemají, tam patří asset packy a hudba od prvního dne. Rozhodni, kterou otázku prototyp klade, a podle toho zvol formu.

Kde se s tím potkáš: [Prototypování](teorie/prototypovani.md) · [Nápad: prototyp do týdne](teorie/napad.md) · [Prostor a hranice](teorie/prostor-a-hranice.md)

### Hard coding

**Hodnoty napsané natvrdo přímo v kódu místo v proměnné či konfiguraci.**

Funguje přesně do chvíle, kdy je potřeba hodnotu změnit — pak ji lovíš po celém projektu a jednu zapomeneš. Pravidlo: každé surové číslo, které budeš někdy ladit, patří do proměnné; stejný princip platí pro vstupy (pojmenované akce místo kláves). Výjimka potvrzující pravidlo: v prototypu na vyhození je hard coding ctnost — rychlost tam poráží čistotu.

Kde se s tím potkáš: [Kolik kódu potřebuješ na start](teorie/co-se-ucit.md) · [Nápad: prototyp do týdne](teorie/napad.md)

### Hard reference

**Přímý odkaz na asset/třídu, který s sebou tahá vše, co cíl referencuje — do paměti i do buildů.**

Vzniká castem, class referencí, přiřazeným meshem. Diagnóza: pravý klik na asset → Reference Viewer (kdo na kom závisí) a Size Map (kolik paměti reference stáhne). Následky: dlouhé loady, provázané levely, křehké systémy. Léky: abstraktní datový master, interfacy, event dispatchery, broadcast kanály — a u assetů soft reference, které se načítají až na vyžádání.

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md) · [Komunikace Blueprintů](praxe/komunikace-blueprintu.md) · [Organizace projektu](praxe/organizace-projektu.md)

### Height mapa

**Černobílá textura kódující výšku terénu jasem pixelu: černá dole, bílá nahoře.**

Formát, na kterém stojí klasický Landscape — a zdroj jeho hlavního limitu: jedna hodnota na pixel znamená jediný stupeň volnosti (nahoru/dolů), takže jeskyně a převisy nejdou. Zůstává ale skvělým výměnným formátem: sculpt z Gaey či World Machine se přenáší právě height mapou a Mesh Terrain ji umí importovat jako startovní tvar i promítat jako texture modifier.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Hook

**Prvek, který hru prodá na první pohled: mechanika, premisa nebo obraz, u kterého se scrollující palec zastaví.**

Portálové portály, vlak-monstrum z Choo Choo Charles, „staráš se o svoje auto v psychedelické Zóně". Hook je vstupní bod trychtýře appealu — bez něj hra nemá jak oslovit lidi, kteří o ní nikdy neslyšeli. Test: dokážeš hook vtěsnat do titulku na Redditu nebo do 300 znaků short description? Hra bez jediné inovace hook nemá — a bez hooku není důvod, aby vznikla.

Kde se s tím potkáš: [Základy: engagement a appeal](teorie/zaklady.md) · [Prototypování](teorie/prototypovani.md) · [Nápad](teorie/napad.md)

### Inheritance

**Dědičnost: děti přebírají proměnné, funkce a komponenty rodiče — základ, na kterém stojí celý UE (Actor → Pawn → Character).**

Lakmusový test každého vztahu: „is it a?" — pes *je* mazlíček, dům není. Rodič je smlouva (co deklaruje, mají garantovaně všechny děti) a na smlouvě stojí polymorfismus: volající volá `Interact`, každé dítě odpoví po svém. Blueprint specifika: component eventy nejde overridnout (obal je do custom eventů), overridnutý event nespouští rodiče automaticky (Add Call to Parent Function).

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md)

### Instance

**Konkrétní umístěný výskyt assetu v levelu.**

Jeden asset (mesh lampy) → stovky instancí (lampy po celé mapě). Rozlišení asset vs. instance je základ práce v editoru: úprava assetu se propíše všem instancím, úprava instance jen jí. Editor umí s instancemi pracovat hromadně — viz Shift+E pro výběr všech výskytů daného assetu.

Kde se s tím potkáš: [Tipy do editoru](praxe/editor-tipy.md)

### Invisible wall

**Neviditelná kolize tam, kde vizuálně nic nebrání v cestě — nejhorší způsob, jak ohraničit mapu.**

Zabíjí imerzi přesně mechanismem „vidím, že to jde, ale hra mi to nedovolí". Alternativy: tvrdé hranice z přirozených bariér světa (útes, řeka, oceán) a pět druhů měkkých hranic — narativní, countdown, nepřátelská, ekonomická, percepční. Pravidlo: hráč se má rozhodnout sám, že dál nepůjde.

Kde se s tím potkáš: [Prostor a hranice](teorie/prostor-a-hranice.md)

### Landmark

**Výrazný orientační bod levelu — věž, světlo, brána — ke kterému se vztahuje hráčova navigace i kompozice prostoru.**

V postupu „landmark napřed": startovní bod hráče a hlavní point of interest jsou první dvě rozhodnutí návrhu levelu, ještě před blockoutem — dávají měřítko, směr a osu pro pacing a vertikalitu. Cestou k landmarku pak vedou funneling (zúžení prostoru), leading lines a světlo.

Kde se s tím potkáš: [Prostor a hranice](teorie/prostor-a-hranice.md)

### Level streaming

**Načítání a uvolňování částí světa za běhu — místo výměny celého levelu přes Open Level.**

Persistent level je rám; sub-levely (`Window → Levels`) se nahrávají přes Level Streaming Volumes nebo uzly Load/Unload Streaming Level, asynchronně — hra mezitím žije. Detaily: *loaded* ≠ *visible* (neviditelný level drží paměť); streaming volume musí ležet v persistent levelu; persistent nejde unloadnout (trik: veškerý obsah do sub-levelu „Base"). Pro open worldy je nástupcem World Partition.

Kde se s tím potkáš: [Levely a streaming](praxe/levely-a-streaming.md)

### Line Trace

**Raycast — neviditelný paprsek vyslaný z bodu daným směrem, který vrátí první (nebo všechny) kolize na dráze.**

Základní dotazovací nástroj: „na co koukám?", „stojím na zemi?", „vidí mě stráž?". Samotný trace je levný; problém je vzorec „trace každý frame v Event Ticku" — polling tam, kde stačí reagovat na změny. Alternativou pro detekci „něco vstoupilo do zóny" jsou overlap eventy kolizních komponent.

Kde se s tím potkáš: [Interakce bez Event Ticku](praxe/interakce-bez-event-ticku.md)

### Linked anim graph

**Samostatný animační graf připojený do AnimBP jako modul — s tagem, přes který na něj komponenty sáhnou zvenčí.**

Vzor z traversal/cover systémů nad GASP: parkour či overlay logika žije ve vlastním grafu, hlavní AnimBP ji jen linkuje; tag („parkour", „overlay") umožňuje actor komponentám najít anim instanci a řídit ji. Drží AnimBP čitelný a systémy přenositelné mezi projekty.

Kde se s tím potkáš: [Systémy nad MM](praxe/mm-systemy.md)

### Loose coupling

**Princip: třídy na sobě závisejí co nejméně — komunikují přes smlouvy (interfacy) a eventy, ne přes tvrdé reference.**

Diagnóza vazeb: Reference Viewer („proč ability závisí na třídě nepřítele?"). Léky: interface místo castu (damageable — „poskytneš-li Take Damage, zavolám ji"), mediátor mezi systémy (event subsystem mezi gameplayem a UI), broadcast kanály. Odměna: systémy jdou měnit a nahrazovat nezávisle — definice škálovatelnosti.

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md) · [Komunikace Blueprintů](praxe/komunikace-blueprintu.md)

### Low-fi prototyp

**Prototyp schválně nízké kvality — náčrt na papíře, čmáranice, hrubá animace konceptu — vytvořený za minuty.**

Jeho supersíla je psychologická: do vypiplaného dema se kritikům tluče těžko, ale náčrt za pět minut nikoho nesvazuje — dostaneš syrový názor na *myšlenku*, dokud se dá směr měnit zadarmo. Protějšek high-fi prototypu (funkční hratelné kostry), který je dražší a láká k připoutání. Srovnej s grayboxem: i tam jde o levné testování, ale mechaniky, ne nápadu.

Kde se s tím potkáš: [Start projektu](teorie/jak-zacit.md) · [Prototypování](teorie/prototypovani.md)

### Market research

**Průzkum trhu před rozhodnutím o hře: výdělky žánrů, tagy, recenze konkurence, benchmarky.**

První krok k objektivitě proti zamilovanosti do vlastního nápadu. Prakticky: Steamové roční žebříčky, SteamDB, Gamalytic/VG Insights, benchmarky Chrise Zukowského; okno posledních ~3 let (starší data lžou) a medián či spodních 25–30 % výdělků, nikdy průměr. Nejcennější levný zdroj: negativní recenze konkurence — seznam bolestí, proti kterým můžeš designovat.

Kde se s tím potkáš: [Idea iceberg](teorie/rady-z-praxe.md) · [Nápad: yoink & twist](teorie/napad.md)

### Modifier stack

**Vrstvené nedestruktivní úpravy: každá operace zůstává živým objektem, který lze dodatečně měnit, přesouvat, přeskládat nebo smazat.**

Filozofie „scéna je recept, ne výsledek" — známá z Houdini, Geometry Nodes či modifierů v Blenderu. Mesh Terrain na ní staví celé tvarování: brush, noise, spline, texture, mesh, boolean a remesh modifiery se skládají podle priorit a blend módů. Cena: recept se musí přepočítávat (build cost, FPS propady při editaci). Výhoda: žádné rozhodnutí není konečné.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Motion matching

**Dotazový systém výběru animací: každý frame hledá v databázi pózu, která nejlépe naváže na trajektorii a aktuální pózu.**

Nahrazuje state machines — žádné stavy a přechody, jen databáze (PSD), schema (co a s jakou vahou měřit) a cena kandidátů; vítězí nejnižší. Stavební kameny: trajektorie (predikce pohybu), pose history (odkud jdu), chooser (která databáze), continuing pose (koho porazit). Od 5.4 v UE, showcase je Game Animation Sample; Fortnite s ním shipuje na všech platformách. Nepotřebuje stovky animací — viz sparse set.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md) · [Systémy nad MM](praxe/mm-systemy.md)

### Nanite

**Virtualizovaná geometrie UE5: engine dynamicky přizpůsobuje detail meshů vzdálenosti a velikosti na obrazovce.**

Prakticky ruší ruční LOD řetězce — mesh se subdivuje a redukuje průběžně, po clusterech, podle toho, co kamera reálně vidí. Mesh Terrain je na Nanite postavený; právě adaptivní subdivize je jeden z důvodů, proč zvládá větší plochy než starý Landscape. Po editaci terénu se Nanite reprezentace přestavuje — proto FPS propad během úprav a krátký build po odkliknutí.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Narrative design

**Návrh vyprávění integrovaný s herním designem — protiklad modelu „designér nechá díry na cutscény a spisovatel je dopíše".**

Pojem posledních ~20 let; zahrnuje volbu typu protagonisty, směr dialogů, rejstříky řeči i vyprávěcí prostředky, které mají jen hry (flavor texty, prostředí, mechaniky). Pro malé týmy začíná třemi branami: kolik implementace vyprávění přinese, jaká je tvá spisovatelská praxe a jaké příběhy ti nabízejí tvoje nástroje.

Kde se s tím potkáš: [Příběh a postavy](teorie/pribeh-a-postavy.md)

### Pacing

**Rytmus zážitku: střídání napětí a klidu, akce a ticha, učení a mistrovství v čase.**

Nástroj režie levelů i celých her: scripted events doručují momenty „ve správnou chvíli", struktura levelu střídá zúžení a otevření, obtížnostní křivka střídá novelty a mastery. Špatný pacing má dva póly — monotónní nuda a únavný nonstop tlak; dobrý pacing je dramaturgie.

Kde se s tím potkáš: [Vedení hráče](teorie/vedeni-hrace.md) · [Zábava a flow](teorie/zabava.md)

### PCG

**Procedural Content Generation — UE framework pro procedurální osazování a generování obsahu světa.**

Grafem definuješ pravidla (sampluj povrch, filtruj podle sklonu, rozmísti stromy s hustotou X) a engine je aplikuje na libovolnou plochu. S Mesh Terrainem spolupracuje přes interop plugin (Mesh Partition PCG Interop) — v beta fázi s beta mírou spolehlivosti.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Persistent level

**Hlavní (rodičovský) level, pod kterým žijí streamované sub-levely — rám, který nikdy neopouštíš.**

Hráč, GameMode i stav přežívají, protože se nikdy nemění celý level — jen sub-levely uvnitř. Nejde unloadnout; chceš-li „vyměnit svět", drž persistent prázdný a veškerý obsah měj v sub-levelech. Objekty, které mají spouštět streaming (volumes, trigger boxy), musí ležet v persistentu — jinak jsou schované spolu s levelem, který mají nahrát.

Kde se s tím potkáš: [Levely a streaming](praxe/levely-a-streaming.md)

### Pitch deck

**Krátká prezentace hry, která ještě neexistuje — simulace prvního kontaktu zákazníka s nápadem.**

Logika: první krok nákupu hry stejně neobsahuje hraní (trailer, GIF, screenshot) — pitch deck tenhle moment vyrobí bez jediného řádku kódu. Proces: brainstorm → hlasování → u top nápadů popsat smyčku (slabé se rozpadnou samy) → decky → nechat lidi vybírat. Opory: lidé skvěle *vybírají* a mizerně radí, jak zlepšovat; a deck za hodinu se zahazuje bez bolesti — málo vloženého času = málo biasu.

Kde se s tím potkáš: [Idea iceberg: pracuj zpátky](teorie/rady-z-praxe.md) · [Nápad: test 300 znaků](teorie/napad.md)

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

Kde se s tím potkáš: [Začátky bez zkušeností](teorie/zacatky-bez-zkusenosti.md) · [Idea iceberg: the Gap](teorie/rady-z-praxe.md) · [Postmortem ShantyTown](teorie/postmortem-shantytown.md)

### Pose Search Database

**PSD — kolekce animací pro jeden typ pohybu, ve které Motion Matching hledá pózy.**

Databáze se dělí podle stavů (idle, run starts, stops, crouch…) — jednak kvůli přehlednosti, jednak kvůli responzivitě: chooser vynutí prohledání správné databáze v ten samý frame (vzor z Fortnite). Ceny mezi oddělenými databázemi zporovnatelní normalization set. Do PSD patří sekvence, blend spacy i montáže; klipy musí mít root motion + force root lock.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md)

### Pose Search Schema

**Definice, co Motion Matching měří: kanály (trajektorie, pozice a rychlosti kostí) s vahami.**

Váhy říkají, na čem při výběru záleží — pozice chodidel typicky 1, rychlosti 0,3, trajektorie 1 (default 7 je moc). Vzorky trajektorie sahají do minulosti (−0,05 s) i budoucnosti (+0,35/0,7/1,0 s). Ladění je „umělecký proces": experimentuj a čti channels breakdown v debuggeru. Různé databáze můžou mít různá schémata (při skoku na chodidlech záleží míň). Kvadrupedi: přední a zadní nohy měřit zvlášť.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md)

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

### Quad

**Čtyřúhelníková buňka mřížky meshe — u terénu základní jednotka rozlišení.**

Rozlišení Mesh Terrainu se zadává počtem quadů v osách XY; víc quadů = jemnější síť = víc detailu i dat. Interně se quady stejně dělí na trojúhelníky (GPU nic jiného nekreslí), ale pro autorskou práci je čtyřúhelníková mřížka přehlednější — proto s ní pracují terény, subdivision modeling i retopologie.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Race condition

**Chyba závislá na pořadí: dva kusy kódu se inicializují souběžně a jeden čte data, která druhý ještě nenastavil.**

V UE klasicky mezi BeginPlay různých actorů — klíč se ptá dveří na ID dřív, než si ho dveře vygenerovaly. Pořadí inicializace není zaručené; nespoléhej na něj. Lék: event dispatcher („KeyAssigned") — místo čtení hned se posluchač binduje a data si nechá oznámit, až existují.

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md)

### Recall priming

**Level design technika: rozmístit do prostředí nenápadné nápovědy, které hráči zpřístupní správnou vzpomínku těsně před tím, než ji bude potřebovat.**

Hráči se u puzzlů nezasekávají hloupostí, ale nedostupností správného nástroje v paměti. Priming ji zvedá prostředím: tmavá chodba donutí vytáhnout pochodeň, hořlavé liány cestou připomenou, že oheň pálí vegetaci — a u puzzle s liánami řešení „samo" naskočí. Hráč se necítí veden, cítí se chytrý; UI nápověda by mu ten pocit ukradla.

Kde se s tím potkáš: [Vedení hráče](teorie/vedeni-hrace.md)

### Redirector

**Ghost soubor, který po přesunu assetu zůstává na starém místě a přesměrovává reference na nové.**

Důvod, proč „prázdné" složky nejdou smazat — a proč force delete rozbije projekt (reference vedou do prázdna). Správně: pravý klik → Update Redirector References (odkazy se přepíšou natrvalo), pak Delete Unreferenced Redirectors, pak teprve mazat složku. Stěhuj po jedné složce — hromadné přesuny editor shazují.

Kde se s tím potkáš: [Organizace projektu](praxe/organizace-projektu.md)

### Roguelike

**Žánr postavený na opakovaných bězích: smrt je součást smyčky, svět se generuje procedurálně, znalost hráče je hlavní trvalý pokrok.**

Pro design je podstatný důsledek mnoha běhů: hráč potkává stejné systémy znovu a znovu, což násobí šanci na náhodné objevení skrytých pravidel — proto žánru tak sedí tajné řetězce (Spelunky). Odnož s trvalým meta-postupem mezi běhy se označuje roguelite.

Kde se s tím potkáš: [Smyčky a řetězce](teorie/smycky-a-retezce.md)

### Root motion

**Pohyb uložený v animaci samotné (v root kosti) — postava se hýbe tak, jak animátor animoval, kapsle následuje.**

Protiklad capsule driven přístupu (vstup hýbe kapslí, animace se lepí). Motion Matching root motion data vyžaduje — z nich čte trajektorie klipů; hromadně se zapíná přes Property Matrix (Enable Root Motion + Force Root Lock, u smyček Looping). GASP je capsule driven, ale animace root motion mají — budoucnost je blending obou přístupů po částech animace.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md)

### Rubber banding

**Umělá podpora hráče, který je pozadu, a brzda hráče napřed — v multiplayeru se říká catch-up mechanika.**

Nejde o podvod na hráče, ale o opravu učebního prostředí: kdo je beznadějně pozadu, dostává od hry konstantní „špatně" a nemá se z čeho učit; kdo je nedostižně napřed, dostává konstantní „dobře". Rubber banding oba vrací do pásma, kde akce zase mají čitelné následky. Příbuzné nástroje: hinty, skipy, měkké stavy úspěchu (skóre místo výhra/prohra).

Kde se s tím potkáš: [Zábava: flow](teorie/zabava.md)

### SaveGame objekt

**Blueprint třída typu SaveGame: nese proměnné k uložení a přes pojmenovaný slot se zapisuje na disk.**

Tři uzly stačí: Create Save Game Object / Load Game From Slot / Save Game to Slot (+ Delete Game in Slot). Architektura okolo: referenci drží Game Instance (přežije přechody levelů), přístup odkudkoli dává function library. Load není magie — hodnoty se musí ručně aplikovat zpět (rychlost do movementu, transform na actora). Myslet dopředu: verze formátu a více slotů.

Kde se s tím potkáš: [Ukládání](praxe/ukladani.md)

### Scope

**Rozsah projektu: kolik obsahu, systémů a ambicí hra obsáhne.**

Hlavní páka proveditelnosti — a nejčastější příčina nedokončených her. Pro začátečníka platí, že malý scope není kompromis, ale strategie: krátká smyčka dokončení → zpětná vazba → další projekt o úroveň výš. Malá hra přitom není zmenšená velká hra, ale jedna vyjmutá mechanika, které všechno slouží. „Scope creep" je plíživé bobtnání rozsahu během vývoje; game jam je institucionalizovaná obrana.

Kde se s tím potkáš: [Začátky bez zkušeností](teorie/zacatky-bez-zkusenosti.md) · [Scope: malé hry a design by constraint](teorie/scope.md) · [Start projektu](teorie/jak-zacit.md)

### Scope creep

**Plíživé bobtnání rozsahu během vývoje: „co kdybychom přidali rybaření?"**

Dvojsečná past: někdy je to přesně ten twist, který hře chyběl, častěji fraktální bobtnání (rybaření → pruty → rybářské lodě) nebo míchání žánrů, které vyrobí hru pro nikoho — publikum dvou žánrů je průnik, ne součet. Rozhodovací filtr: sytí nápad účel hry, nebo ho ředí? Obrana: sticky note test na začátku, momentum bar a psaní nápadů do šuplíku během vývoje.

Kde se s tím potkáš: [Žrouti času](teorie/produktivita.md) · [Nápad](teorie/napad.md) · [Start projektu](teorie/jak-zacit.md)

### Separation of concerns

**Princip: systém se dělí na malé části s jedinou zodpovědností — jako motor z vyměnitelných dílů.**

Návrhová otázka „co mají všechny X společné?" oddělí obecné (base classa, komponenta) od specifického (děti). Ability se vytáhne z komponenty do vlastního objektu; komponenta pak řeší jen aktivaci a cooldowny. Odměna: 20 abilit = 20 nezávislých blueprintů se stejnou strukturou, každý laditelný zvlášť.

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md) · [Organizace projektu](praxe/organizace-projektu.md)

### Short description

**Krátký popis hry na Steamu — ~300 znaků pod capsule obrázkem, první text, který potenciální hráč čte.**

Zároveň nejlevnější validační nástroj nápadu: „test 300 znaků" = zkus popis napsat v den nula. Dvě věty se žánrem, perspektivou, hlavními činnostmi (hodně sloves!), cílem a prostředím. Když to nejde, nemáš vágní popis — máš vágní hru. Rozšířená verze testu je mock Steam page: dlouhý popis, features, zkusmá capsule.

Kde se s tím potkáš: [Nápad: test 300 znaků](teorie/napad.md) · [Scope](teorie/scope.md)

### Signal-to-noise ratio

**Poměr užitečné informace (signál) k balastu (šum) — klíčová veličina učení, soustředění i designu obtížnosti.**

Učení je budování prediktivního modelu světa a potřebuje data, ze kterých se dá učit. Frustrace = konstantní „špatně" (nulový signál), nuda = konstantní „dobře" (nulový signál); flow kanál je pásmo, kde některé akce fungují a jiné ne — nejlepší signál. Jasné cíle jsou filtr šumu; soustředění je totéž z druhé strany (rozptýlení a vizuální balast = šum).

Kde se s tím potkáš: [Zábava: flow](teorie/zabava.md)

### Soft boundary

**Hranice mapy, kterou lze fyzicky překročit — ale svět dá jasně najevo, že je to špatný nápad.**

Pět vzorů: narativní (most se zřítí, postava odmítne jít dál), countdown (mráz, plyn, dezerce — tlak času místo kolize), nepřátelská (za hranicí loví něco silnějšího; nemusí zabíjet — stačí probrat se potlučený zpátky), ekonomická (kyslík/palivo nevystačí na návrat) a percepční (ztráta orientace a viditelnosti). Nejlépe fungují kombinované a vždy s fikčním alibi.

Kde se s tím potkáš: [Prostor a hranice](teorie/prostor-a-hranice.md)

### Sparse set

**Minimální sada animací pro Motion Matching: ~13 klipů bez strafu, ~26 se strafem, ~60–80 se stavy.**

Epicův recept proti mýtu „potřebuju 500 animací jako GASP": idle, run forward, starty a stopy (levá i pravá noha kvůli stutter-stepům), oblouky (run arcs) a refacing starty. Rozsah řídí otázky na hru: co gameplay potřebuje a kolik movement states (každý ≈ 2×). S procedurálními uzly je 26animační set podle Epicu shippable. Klidně hand-keyed a stylizovaný.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md)

### Square hole

**Chyba balancu: univerzální nástroj či strategie, která řeší každou situaci — a tím zabíjí všechna rozhodnutí.**

Podle memu „it goes in the square hole". Vzniká z balancování jedinou osou síly: jeden nástroj vždycky vyjde o chlup líp a stane se odpovědí na všechno. Lék: vícerozměrné nástroje (každý dobrý na něco jiného) + pestré problémy + zajímavé hraniční případy, kde volba vyžaduje úvahu. Cíl balancu: rozhodnutí netriviální, předvídatelná a nosná i po opakování.

Kde se s tím potkáš: [Zábava: balanc rozhodnutí](teorie/zabava.md)

### Steam Next Fest

**Steamový online festival demoverzí nevydaných her, koná se třikrát ročně.**

Funguje jako multiplikátor wishlistů — čím víc jich máš na vstupu, tím víc akce vygeneruje — a každá hra se smí zúčastnit jen jednou, takže načasování je strategické rozhodnutí (jít tam s maximem, klidně couvnout a počkat na další termín). Citované minimum pro smysluplný efekt ~7 000 wishlistů na vstupu (údaj jednoho vydání, ne konstanta).

Kde se s tím potkáš: [Postmortem ShantyTown](teorie/postmortem-shantytown.md) · [Idea iceberg](teorie/rady-z-praxe.md)

### Stitching

**Experimentální MM technika: místo lineárního blendu najde animaci, která tě za daný čas dostane z aktuální pózy do cílové.**

Řeší přechody locomotion → gameplay akce (úder, který má za 0,25 s dopadnout) a gameplay → cinematika (sequencer stitch track v 5.6; Witcher 4 demo). Nosiče: Chooser Player se stitch databází, Sequence Player se „start with matching pose" + Pose Search Branch In notify. Čas přechodu je laditelný designérem, ne zadrátovaný animátorem.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md)

### Subsystem

**Automaticky vytvářený singleton s definovaným životním cyklem (engine / game instance / world / local player).**

Nemusíš ho spawnovat ani registrovat — engine ho vytvoří a drží podle typu. Game instance subsystem žije po celou dobu aplikace, ideální pro mediátory (event manager, broadcast kanály) a služby bez vlastního místa ve světě. Blueprintově se konzumuje snadno; definice vyžaduje C++.

Kde se s tím potkáš: [Komunikace Blueprintů](praxe/komunikace-blueprintu.md) · [Principy architektury](praxe/principy-architektury.md)

### Telemetrie

**Sběr dat o tom, co hráči ve hře skutečně dělají — lokálně (čítače, achievementy) i vzdáleně (analytický backend).**

Lokální patro: activity tracker — gameplay tagy hlášené centrální funkci, dispatcher pro odběratele, mapa tag→počet. Vzdálené patro: plugin (TrackEdge) + backend (PostHog): person properties, eventy s vlastnostmi, sessions s trváním, dashboardy. K vydání patří privacy rozvaha (poloha, GDPR). Telemetrie je chování, ne slova — sesterská měna „the gap".

Kde se s tím potkáš: [Telemetrie](praxe/telemetrie.md) · [Idea iceberg](teorie/rady-z-praxe.md)

### Tessellation

**Dělení geometrie na jemnější trojúhelníky, aby povrch unesl víc detailu.**

V Mesh Terrainu ve dvou podobách: adaptivní teselace texture modifieru (zjemní síť tam, kde height mapa nese detail, řízeno error tolerancí) a Tessellate režim remesh modifieru. Protiklad k uniformnímu remeshi: adaptivní přístup šetří trojúhelníky, ale hůř se predikuje výsledný tvar. Obecná rada z praxe: hrubé tvarování s teselací vypnutou, detail zapínat cíleně na konci.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Trajektorie

**V Motion Matchingu spočítaná historie a predikce pohybu postavy — modrá budoucnost, červená minulost.**

Každý frame se z rychlosti a vstupu predikuje, kde postava bude (+0,35/0,7/1 s) — a proti tomu se matchují animace. Nezaměňovat s traversal (detekce překážek) ani s intentem (co hráč chce = vstup; trajektorie = co se asi stane). Generuje ji Character Trajectory komponenta nebo Pose Search Generate Trajectory; debug: `a.CharacterTrajectory.Debug 1`. Expozice trajektorie gameplayi umí předpovědět zastavení či budoucí rychlost.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md)

### Traversal

**Překonávání překážek (vault, mantle, hurdle) — v GASP detekce hran + výběr animace podle stavu a překážky.**

Vzor z GASP: spline/trace detekce překážky → chooser (hurdle/vault/mantle podle typu a výšky) → montáž s Pose Search Branch In oknem + motion warping na hranu (get-to-bone, interaction transform přes blueprint channel ve schématu). Funguje jen na Traversable blocích; komunitní komponenty (AC_TraceTraversal) ho naučí šplhat i na běžnou geometrii — zákaz per objekt tagem.

Kde se s tím potkáš: [Systémy nad MM](praxe/mm-systemy.md) · [MM základy](praxe/mm-zaklady.md)

### Trigger volume

**Neviditelná zóna v levelu, která při vstupu hráče (či jiné entity) spustí událost.**

Základní nástroj skriptovaných momentů: rozhovor NPC na tržišti, změna hudby, otevření cesty, cinematika na správném místě. Designové pravidlo: nejdřív otázky „jaký zážitek, jaká emoce, jaká informace, jaká další akce?" — trigger je jen doručovací mechanismus. V UE odpovídá trigger box/volume s overlap eventy (viz praxe: interakce bez Event Ticku).

Kde se s tím potkáš: [Vedení hráče](teorie/vedeni-hrace.md) · [Interakce bez Event Ticku](praxe/interakce-bez-event-ticku.md)

### Value chain

**Hodnotový řetězec (Dan Cook): smysl a zábavnost sběrné činnosti nedává činnost sama, ale její zamýšlené použití dál v řetězci.**

Sbírání klacíků nudí, dokud z nich hráč nestaví něco, co sytí fantazii hry — pak se každé rozhodnutí „co sebrat" stává plánováním. Prakticky: nudnou mechaniku neoživuj pozlátkem, dej jí destinaci. Cíl řetězce zpětně obarvuje všechny jeho články.

Kde se s tím potkáš: [Smyčky a řetězce](teorie/smycky-a-retezce.md)

### Version control

**Verzování projektu (typicky Git): každá změna se ukládá jako commit, ke kterému se lze kdykoli vrátit.**

Dvě služby: záchranné lano z každé katastrofy a viditelná historie pokroku (protilék na „nic nestíhám"). Zásada zrnitosti: commituj malé celky s popisnou zprávou — velký commit se špatně popisuje, vrací i slučuje. UE specifika: Blueprinty jsou binární (diff neuvidíš, zpráva je vše), na velké assety Git LFS, v editoru vestavěná integrace Revision Control.

Kde se s tím potkáš: [Start projektu](teorie/jak-zacit.md)

### Vertical slice

**Reprezentativní výsek hry ve finální kvalitě — brána mezi prototypem a plnou produkcí.**

Ne nutně začátek hry: libovolných 5–60 minut zážitku, na kterém se poprvé potkají mechaniky z prototypu, art style a tón. Otázka, na kterou odpovídá: nadchne lidi reprezentativní ukázka natolik, aby se vyplatilo vyrábět zbytek obsahu? U komplexních her se skládá z ~60 % žánrových standardů a ~40 % inovací — testovat jde jen to nové.

Kde se s tím potkáš: [Prototypování a vertical slice](teorie/prototypovani.md) · [Základy designu](teorie/zaklady.md)

### Wishlist

**Přání na Steamu — před vydáním hlavní měřítko zájmu o hru a palivo algoritmu viditelnosti.**

Wishlisty pohánějí doporučování a rozhodují o síle launche; Steam Next Fest funguje jako jejich multiplikátor. Zároveň pozor na „the gap": wishlist je zdvořilý zájem, nákup je závazek — konverze není samozřejmá. V žebříčku důkazů síly nápadu stojí wishlisty vysoko, ale pozdě; validovat jde mnohem dřív a levněji.

Kde se s tím potkáš: [Postmortem ShantyTown](teorie/postmortem-shantytown.md) · [Idea iceberg](teorie/rady-z-praxe.md)

### World Partition

**Streamovací systém UE5: svět rozdělený na buňky, které se nahrávají a uvolňují podle vzdálenosti či logiky.**

Nahrazuje starší ruční level streaming; open world level je level s aktivním World Partition. Mesh Terrain na něm závisí — terén existuje jako partition chunky viditelné ve World Partition okně, kde jde s regiony pracovat (load/unload) i během editace, což šetří paměť při práci na velkých plochách.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Yoink & twist

**Vzorec tvorby nápadu: vezmi žánr s prokázaným publikem (yoink) a přidej vlastní vylepšení nebo obrat (twist).**

Protiklad honby za stoprocentní originalitou, která znamená nulovou validaci trhu a chybějící referenční body. Rozhodovací pravidlo: v mladém žánru stačí být *lepší* (oprav pár bolestí z negativních recenzí — Fields of Mistria vs. Stardew Valley), ve starém žánru musíš být *jiný* (Age of Empires neporazíš kvalitou). Twist často stojí jen reskin a fikci — v kódu se nemusí změnit nic.

Kde se s tím potkáš: [Nápad: yoink & twist](teorie/napad.md) · [Prototypování: standardy vs. inovace](teorie/prototypovani.md)
