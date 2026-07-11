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

### AI Controller

**Mozek AI postavy: posedne pawna (tělo) a rozhoduje — kam jít, kdy útočit; tělo řeší pohyb a animace.**

Oddělení mozku od těla umožňuje znovupoužít logiku napříč postavami. Controller typicky spouští Behavior Tree nebo State Tree (`Run Behavior Tree` / StateTreeAI komponenta) a nese AI Perception. Postava ho dostane přes `AI Controller Class` + `Auto Possess AI`.

Kde se s tím potkáš: [Základy AI](praxe/ai-zaklady.md) · [State Trees](praxe/state-trees.md)

### AI Perception

**Percepční systém UE: smysly (sight, hearing, damage) jako konfigurace jedné komponenty, události při změně vjemu.**

Mocnější nástupce Pawn Sensingu: víc smyslů, stárnutí vjemů, lose sight radius (hystereze ztrácení cíle). Dva zádrhely: cíl musí mít AI Perception Stimuli Source komponentu a každý sense config potřebuje zaškrtnout Detect Enemies/Neutrals/Friendlies. Sluch a damage se hlásí přes Report Noise/Damage Event — signály pro AI, ne herní zvuk či poškození.

Kde se s tím potkáš: [AI vnímání](praxe/ai-vnimani.md) · [State Trees](praxe/state-trees.md) · [Základy AI](praxe/ai-zaklady.md)

### ALS

**Advanced Locomotion System — komunitní locomotion framework pro UE; jeho autor dnes v Epicu designově vede GASP.**

Roky de facto standard pokročilého pohybu z marketplace: overlay stavy (pózy držení předmětů vrstvené přes locomotion), layer curves pro per-kost řízení blendů, stance systém. GASP je jeho duchovní nástupce a komunita ALS animace i vzory dál recykluje — overlay přístup ke zbraním nad GASP je přímo z ALS playbooku.

Kde se s tím potkáš: [GASP](praxe/gasp.md)

### Anim montage

**Animační asset pro jednorázové akce (útok, interakce), přehrávaný přes sloty do vybraných částí skeletu.**

Nad Motion Matchingem je montáž základ combatu: spodní tělo matchuje locomotion, horní hraje montáž ve slotu Upper Body (Layered Blend Per Bone + Blend Poses by Bool). Anim notifies uvnitř montáže řídí comba (AddCombo/ResetCombo okna); sloty pro zbraně patří do vlastní slot skupiny, ať výměna nepřeruší jiné montáže. Pro matchování do montáže slouží Pose Search Branch In.

Kde se s tím potkáš: [Systémy nad MM](praxe/mm-systemy.md) · [MM základy](praxe/mm-zaklady.md)

### Anim Notify

**Značka na časové ose animace, která v daném framu spustí logiku — zvuk, efekt, gameplay event.**

Vestavěné (Play Sound) i vlastní blueprint třídy (override Receive Notify) s instance editable parametry — notify pak nese data (která noha, který moment hodu). Notify state je varianta s trváním (od–do framu): motion warping okna, Pose Search Branch In. Pozor v blend space: Notify Trigger Mode default spouští jen nejváženější animaci.

Kde se s tím potkáš: [Kroky](praxe/footsteps.md) · [Interakce s předměty](praxe/interakce-predmety.md) · [Systémy nad MM](praxe/mm-systemy.md)

### Asset pack

**Balík hotových assetů — modely, zvuky, UI, shadery — připravený k okamžitému použití.**

Pro sólo vývojáře nástroj přežití: 50 hodin vlastního lokalizačního toolkitu vs. hotový asset za pár desítek dolarů je reálná volba z praxe. Kupuje se to, co dělat neumíš nebo nechceš; vlastní ruce si šetři na to, čím se hra liší. Při prototypování asset packy dodají vizuál a vibe za nulový čas — a u „design by constraint" umí být rovnou zdrojem nápadu („šla by kolem tohohle jediného assetu postavit hra?").

Kde se s tím potkáš: [Žrouti času](teorie/produktivita.md) · [Nápad](teorie/napad.md) · [Scope](teorie/scope.md)

### B-roll

**Doplňkové záběry, které běží na obrazovce, zatímco mluvíš o něčem obecnějším — ve videích o hrách typicky záběry gameplaye.**

Pravidlo devlogů: na obrazovce má být hra, pořád — ideálně přesně to, o čem zrovna mluvíš, jinak aspoň obecný B-roll. Chytrý zdroj záběrů starších verzí hry: version control — checkout starého commitu a natoč, co potřebuješ.

Kde se s tím potkáš: [Devlogy](teorie/devlogy.md)

### Behavior Tree

**Klasický rozhodovací strom AI v UE: selectory a sequence uzly volí tasky podle podmínek z Blackboardu.**

Strom běží na AI controlleru a čte sdílenou tabuli (Blackboard); decoratory hlídají podmínky a s „observer aborts" přerušují běžící větve při změně dat. Vlastní tasky se píší v blueprintu (Receive Execute AI → Finish Execute). Pro nové projekty Epic tlačí State Trees — koncepty se ale přenášejí.

Kde se s tím potkáš: [Základy AI](praxe/ai-zaklady.md) · [AI vnímání](praxe/ai-vnimani.md)

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

### Bounds

**Osově zarovnaný obal (kvádr) kolem objektu či bodu — levná aproximace „kolik místa věc zabírá".**

Ve fyzice a tracingu zrychlují testy, v PCG jsou bounds bodů přímo pracovní data: Difference vyřezává podle nich (přesněji to umí kolizní data), Self Pruning jimi měří překryvy a bounds modifier je nafukuje či zmenšuje jako ladicí páku. Get Actor Bounds vrací obal celého actora — základ zarovnávání na neznámé meshe.

Kde se s tím potkáš: [PCG základy](praxe/pcg-zaklady.md) · [Parkour postaru](praxe/parkour-vault.md)

### Buoyancy

**Vztlak: systém Water pluginu, který nechá simulovaná tělesa plavat na vodních tělesech.**

Dvě cesty: klasicky Buoyancy komponenta s pontoony (body vztlaku — 4 rohy lodi; debug `r.water.debug.buoyancy 1`), od 5.7 stačí Physical Material Override → Default Buoyancy Physics Material + na water body kolize Query and Probe s Block na Physics Body. Objekt musí startovat nad hladinou a simulovat fyziku; ladí se mass, damping, center of mass.

Kde se s tím potkáš: [Voda a buoyancy](praxe/voda-a-buoyancy.md) · [Nástroje: EasyWaterscape](praxe/nastroje-voda.md)

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

### Contact curve

**Animační křivka 0/1 říkající, kdy je chodidlo na zemi — řídí foot pinning; v GASP nahradila foot velocity curves.**

Hodnota 0 = noha ve vzduchu, 1 = došlap. Proti rychlostním křivkám je konzistentní napříč gaity (walk i sprint sdílí stejnou škálu) a snadno se ručně edituje, když noha „lepí" špatně. Epic je generuje interním batch nástrojem; starý foot placement anim uzel pořád chce velocity curve, remapuje se přes Curve Expressions plugin.

Kde se s tím potkáš: [GASP](praxe/gasp.md)

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

### Decal

**Materiál promítnutý na povrch světa — otisky, cákance, graffiti; spawnuje se za běhu bez úpravy podkladu.**

`Spawn Decal at Location` s velikostí a rotací; materiál v režimu deferred decal (translucent). Umístění: bod dopadu + normála × malý offset proti z-fightingu; rotace z normály povrchu, ať decal „leží". S dynamic material instancí jde per decal řídit texturu, barvu i fade-out v čase.

Kde se s tím potkáš: [Kroky](praxe/footsteps.md)

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

### DLSS

**NVIDIA upscaler: hra se renderuje v nižším rozlišení a AI ji dopočítá do nativního — víc FPS, u 4.5 i stabilnější obraz.**

Do projektu přes plugin z NVIDIA developer webu (složky do engine Plugins). Blueprint vzor: Query Support → Set Mode (quality = 66 % rozlišení, ultra performance = 33 %); k tomu Frame Generation (násobení snímků) a Reflex (nižší latence). Nezapomeň kompenzovat mip/LOD bias — engine při nižším interním rozlišení potichu sníží kvalitu textur i Nanite. Multiplatformní alternativa v enginu je TSR.

Kde se s tím potkáš: [Textury a DLSS](praxe/textury-a-dlss.md)

### Draw call

**Příkaz CPU pro GPU „vykresli tohle" — každý unikátní objekt s unikátním materiálem znamená jeden navíc.**

Tisíce draw calls zahltí CPU dřív, než GPU vůbec začne kreslit. Léky: instancing (stejný mesh + materiál = jeden call pro všechny výskyty), trim sheety a atlasy (víc objektů sdílí materiál) a auto-instancing enginu — v UE4 vázaný i na stejnou lightmapu (trik The Ascent: větší lightmapy = −10 % calls). Pro artistu metrika číslo jedna: šetří se návrhem assetů, ne až profilerem.

Kde se s tím potkáš: [Breakdowny](praxe/env-breakdowny.md)

### Dynamic Material Instance

**Kopie materiálu vytvořená za běhu (`Create Dynamic Material Instance`), jejíž parametry jdou měnit z kódu.**

Scalar/vector/texture parametry pojmenované v materiálu se nastavují uzly Set Parameter Value — jména musí sedět do písmene. Základ všeho, co se vizuálně mění za hry: slábnoucí stopy, zabarvení zásahu, progres přebíjení. MID žije per objekt — změna jedné instance neovlivní ostatní.

Kde se s tím potkáš: [Kroky](praxe/footsteps.md)

### Edit layer

**Vrstva úprav Landscape terénu — sculpt i paint žijí v pojmenovaných vrstvách, které jdou zapínat a mazat.**

Nástroje pracují s aktuálně vybranou vrstvou: copy/paste gizmo kopíruje jen z ní (jinak prázdno), water bodies si vytvářejí vlastní vrstvu. Zhruba totéž, co v Mesh Terrainu dělají modifiery — jen bez 3D volnosti a přeskládávání priorit.

Kde se s tím potkáš: [Landscape tipy](praxe/landscape-tipy.md) · [Voda a buoyancy](praxe/voda-a-buoyancy.md)

### Environmental storytelling

**Vyprávění prostorem: rozmístění objektů říká, co se tu stalo, dřív než padne jediné slovo.**

Převrácená židle, otevřený šuplík a stopy používání (edge wear, škrábance u dveří, prach v koutech) skládají historii místa. Funguje i kompozičně — stopa předmětů vede hráče ke dveřím — a v hororu buduje napětí dřív, než se cokoli stane. Opak: sterilně čisté a symetrické prostory, které křičí „kulisa".

Kde se s tím potkáš: [Breakdowny](praxe/env-breakdowny.md) · [Vedení hráče](teorie/vedeni-hrace.md)

### EV100

**Jednotka expozice: kolik světla pustí kamera do obrazu — EV100 = 1 odpovídá modré hodině, interiér ~5–7, slunečný den ~13.**

Zamčení min = max EV100 v post-process volume vypne auto-exposure a jas scény řídíš ty. Pozor na kopírovaný recept „nastav 1/1": jednička sedí jen velmi tmavým scénám — hodnota se volí podle scénáře a podle toho, pro co exponuješ (slunce, nebo stíny). Vyšší číslo = tmavší obraz.

Kde se s tím potkáš: [Osvětlení](praxe/osvetleni.md) · [Stavba prostředí](praxe/env-tvorba.md)

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

### Foot placement

**Procedurální usazení chodidel na terén: IK na svazích, špendlení došlapů, tlumení roota na hrbolech.**

Řeší tři viditelné neduhy: vznášení nohou na svahu (chodidla na terén + pokles pánve, ať noha dosáhne bez hyperextenze), klouzání chodidel při blendech a rotacích (foot pinning na world-space pozici došlapu) a poskakování těla na nerovnostech (root damping pružinou podél normály terénu). V GASP existuje jako anim uzel (CMC postava) i Control Rig graf (Mover postava); došlapy řídí contact curves.

Kde se s tím potkáš: [GASP](praxe/gasp.md) · [MM základy](praxe/mm-zaklady.md)

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

### GASP

**Game Animation Sample Project — Epicův „živý" ukázkový projekt gameplay animace: 500+ animací, hotový Motion Matching, traversal a od 5.7 Mover.**

Zdarma, blueprint-only. Smysl projektu: zvednout minimální laťku kvality herní animace a dát šablonu, jak MM stavět — databáze per stav, choosery, procedurální doladění. Není to plugin: do vlastního projektu se migruje content (+ console variables a pluginy) a každá verze enginu přináší výrazné změny.

Kde se s tím potkáš: [GASP](praxe/gasp.md) · [MM základy](praxe/mm-zaklady.md) · [Systémy nad MM](praxe/mm-systemy.md)

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

### Hard coding

**Hodnoty napsané natvrdo přímo v kódu místo v proměnné či konfiguraci.**

Funguje přesně do chvíle, kdy je potřeba hodnotu změnit — pak ji lovíš po celém projektu a jednu zapomeneš. Pravidlo: každé surové číslo, které budeš někdy ladit, patří do proměnné; stejný princip platí pro vstupy (pojmenované akce místo kláves). Výjimka potvrzující pravidlo: v prototypu na vyhození je hard coding ctnost — rychlost tam poráží čistotu.

Kde se s tím potkáš: [Kolik kódu potřebuješ na start](teorie/co-se-ucit.md) · [Nápad: prototyp do týdne](teorie/napad.md)

### Hard reference

**Přímý odkaz na asset/třídu, který s sebou tahá vše, co cíl referencuje — do paměti i do buildů.**

Vzniká castem, class referencí, přiřazeným meshem. Diagnóza: pravý klik na asset → Reference Viewer (kdo na kom závisí) a Size Map (kolik paměti reference stáhne). Následky: dlouhé loady, provázané levely, křehké systémy. Léky: abstraktní datový master, interfacy, event dispatchery, broadcast kanály — a u assetů soft reference, které se načítají až na vyžádání.

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md) · [Komunikace Blueprintů](praxe/komunikace-blueprintu.md) · [Organizace projektu](praxe/organizace-projektu.md)

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

Kde se s tím potkáš: [Základy: engagement a appeal](teorie/zaklady.md) · [Prototypování](teorie/prototypovani.md) · [Nápad](teorie/napad.md)

### Inheritance

**Dědičnost: děti přebírají proměnné, funkce a komponenty rodiče — základ, na kterém stojí celý UE (Actor → Pawn → Character).**

Lakmusový test každého vztahu: „is it a?" — pes *je* mazlíček, dům není. Rodič je smlouva (co deklaruje, mají garantovaně všechny děti) a na smlouvě stojí polymorfismus: volající volá `Interact`, každé dítě odpoví po svém. Blueprint specifika: component eventy nejde overridnout (obal je do custom eventů), overridnutý event nespouští rodiče automaticky (Add Call to Parent Function).

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md)

### Instance

**Konkrétní umístěný výskyt assetu v levelu.**

Jeden asset (mesh lampy) → stovky instancí (lampy po celé mapě). Rozlišení asset vs. instance je základ práce v editoru: úprava assetu se propíše všem instancím, úprava instance jen jí. Editor umí s instancemi pracovat hromadně — viz Shift+E pro výběr všech výskytů daného assetu.

Kde se s tím potkáš: [Tipy do editoru](praxe/editor-tipy.md)

### Instanced Actors

**Experimentální systém (5.5+): svět stojí z levných instanced static meshů a objekty u hráče se vymění za plnohodnotné Blueprint actory.**

Swap na blueprint řídí Max Actor Distance, culling samotných instancí Max Instance Distances. Zásadní pravidlo: probuzený actor vzniká pokaždé od nuly — stav (sebraný pickup) musí držet externí manager. Posunutou fyziku vrací na místo, pokud nezapneš Eject on Actor Moved. S PCG spojuje uzel Spawn Instanced Actors (interop od 5.6) a jednorázový setup přes Data Registry.

Kde se s tím potkáš: [Instanced Actors](praxe/instanced-actors.md) · [Případovka Hex-A-Gone](praxe/pcg-hexagone.md)

### Invisible wall

**Neviditelná kolize tam, kde vizuálně nic nebrání v cestě — nejhorší způsob, jak ohraničit mapu.**

Zabíjí imerzi přesně mechanismem „vidím, že to jde, ale hra mi to nedovolí". Alternativy: tvrdé hranice z přirozených bariér světa (útes, řeka, oceán) a pět druhů měkkých hranic — narativní, countdown, nepřátelská, ekonomická, percepční. Pravidlo: hráč se má rozhodnout sám, že dál nepůjde.

Kde se s tím potkáš: [Prostor a hranice](teorie/prostor-a-hranice.md)

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

### Level instance

**Znovupoužitelný sub-level: skupina aktorů (klidně s blueprinty) zabalená do jednoho celku, který se dá rozmístit vícekrát.**

Vytváří se výběrem aktorů → right-click → Level → Create Level Instance; sourozenec Packed Level Actor dělá totéž jen pro static meshe a převádí je na instance (jeden draw call, ideální pro modulární budovy). Editace se propíše všem kopiím — varianta se dělá z duplikátu. Vzor „dům z Warzone": jednou postavit, šestkrát položit.

Kde se s tím potkáš: [Optimalizace scény](praxe/optimalizace.md)

### Level streaming

**Načítání a uvolňování částí světa za běhu — místo výměny celého levelu přes Open Level.**

Persistent level je rám; sub-levely (`Window → Levels`) se nahrávají přes Level Streaming Volumes nebo uzly Load/Unload Streaming Level, asynchronně — hra mezitím žije. Detaily: *loaded* ≠ *visible* (neviditelný level drží paměť); streaming volume musí ležet v persistent levelu; persistent nejde unloadnout (trik: veškerý obsah do sub-levelu „Base"). Pro open worldy je nástupcem World Partition.

Kde se s tím potkáš: [Levely a streaming](praxe/levely-a-streaming.md)

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

### Live Link

**Systém pro streamování dat do enginu (mocap, kamery, DCC nástroje) — a od 5.8 s Live Link Hubem i offline zpracování videa.**

Pro markerless mocap: Live Link Hub → Capture Manager → Mono Video Ingest převede MP4 na capture data, které umí číst MetaHuman Performance. Živá cesta (telefon jako facial kamera, mocap obleky) používá tentýž systém — proto to jméno.

Kde se s tím potkáš: [Animační nástroje](praxe/animace-nastroje.md)

### Locomotor

**Control Rig uzel pro procedurální chůzi: počítá došlapy dynamicky podle pohybu, žádné animační klipy.**

Foot sets definují končetiny (fázové offsety = charakter chůze — pavouk 0/0,25/0,5/0,75), pelvis settings usazení těla, stepping výšku a tempo kroků; do kostí to propíše Full Body IK s effectory na špičkách. Ladí se collision radius per noha a max collision height. Experimental plugin; Epic jím demí mecha v GASP.

Kde se s tím potkáš: [Animační nástroje](praxe/animace-nastroje.md) · [GASP](praxe/gasp.md)

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

### Mass Entity

**ECS framework UE pro simulaci tisíců entit — davy, doprava; pohání City Sample i MetaHuman Crowd.**

Entity nejsou actory: data žijí ve fragmentech zpracovávaných hromadně, proto škálování na tisíce NPC s navigací a vyhýbáním. Pro viditelnost se kombinuje s instancovanými meshi a streamováním plných actorů u kamery.

Kde se s tím potkáš: [MetaHuman v praxi](praxe/metahuman.md)

### Material function

**Znovupoužitelný blok materiálové logiky — funkce, kterou vložíš do libovolného materiálu v projektu.**

Se vstupem a výstupem typu material attributes funguje jako vrstva: materiál postavy → funkce (decay, sníh, mokro) → výstup. Uvnitř Get/Set Material Attributes upraví jen vybrané atributy, zbytek proteče beze změny. Jedna funkce pro celý projekt znamená i opravy na jednom místě.

Kde se s tím potkáš: [Materiály](praxe/materialy.md)

### MCP

**Model Context Protocol — standard, kterým AI agent (Claude Code, Codex, Gemini…) mluví s nástroji; od 5.8 nativně v Unrealu.**

Trojice pluginů Unreal MCP + Terminal + Editor Toolset dá agentovi kontext projektu a kontrolu nad editorem: blueprinty, materiály, PCG, level design. Config per agent generuje konzolový příkaz (.mcp.json). Stejný protokol propojuje agenty s Blenderem i ComfyUI. Zlaté pravidlo: obecný prompt = obecný výsledek — rozepsaná logika a detailní zadání dělají rozdíl.

Kde se s tím potkáš: [AI agenti: Claude Code a MCP](praxe/claude-code-ue.md)

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

### Modifier stack

**Vrstvené nedestruktivní úpravy: každá operace zůstává živým objektem, který lze dodatečně měnit, přesouvat, přeskládat nebo smazat.**

Filozofie „scéna je recept, ne výsledek" — známá z Houdini, Geometry Nodes či modifierů v Blenderu. Mesh Terrain na ní staví celé tvarování: brush, noise, spline, texture, mesh, boolean a remesh modifiery se skládají podle priorit a blend módů. Cena: recept se musí přepočítávat (build cost, FPS propady při editaci). Výhoda: žádné rozhodnutí není konečné.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Motion matching

**Dotazový systém výběru animací: každý frame hledá v databázi pózu, která nejlépe naváže na trajektorii a aktuální pózu.**

Nahrazuje state machines — žádné stavy a přechody, jen databáze (PSD), schema (co a s jakou vahou měřit) a cena kandidátů; vítězí nejnižší. Stavební kameny: trajektorie (predikce pohybu), pose history (odkud jdu), chooser (která databáze), continuing pose (koho porazit). Od 5.4 v UE, showcase je Game Animation Sample; Fortnite s ním shipuje na všech platformách. Nepotřebuje stovky animací — viz sparse set.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md) · [Systémy nad MM](praxe/mm-systemy.md)

### Motion Warping

**Ohnutí root motion animace tak, aby trefila cílový transform — notify state v montáži + warp target za běhu.**

Základ traversalu a interakcí: Motion Matching vybere nejbližší vhodnou animaci a warp uvnitř svého okna dožene zbytkovou chybu pozice i rotace. Precomputed warp (5.7, z Witcher dema) přidává oddělené křivky pro translaci a rotaci (posun na začátku, dotočení na konci) a steering, který dráhu k cíli ohne do přirozeného oblouku.

Kde se s tím potkáš: [GASP](praxe/gasp.md) · [Systémy nad MM](praxe/mm-systemy.md)

### Movement Mode

**Modulární objekt Moveru definující jeden režim pohybu (walking, falling, slide…) — vyměnitelný a rozšiřitelný i v Blueprintu.**

Proti CMC, kde režimy byly zadrátované v komponentě, si módy skládáš: child mód přepíše generate-move funkci, zavolá parenta a upraví parametry (sprint = přepiš max speed podle custom input structu). Společná data módů řeší shared settings; blueprint proměnné módu se objeví v details panelu komponenty a replikují se samy.

Kde se s tím potkáš: [Mover](praxe/mover.md) · [GASP](praxe/gasp.md)

### Mover

**Nová pohybová komponenta UE — nástupce Character Movement Componentu postavený na replikaci vstupů a modulárních movement módech.**

Klíčové rozdíly proti CMC: replikují se inputy (i vlastní blueprint structy) místo výsledků pohybu, rotace je zcela volná (spin transitions, twin-stick intent) a predikce trajektorie pro Motion Matching spouští skutečný simulační kód včetně custom módů. V GASP od 5.7 výchozí; CMC postava zůstává jako legacy. Pozor na frame zpoždění vstupu (network prediction tiká před pawnem) — kameru a AnimBP krmit post-sim hodnotami.

Kde se s tím potkáš: [Mover](praxe/mover.md) · [GASP](praxe/gasp.md)

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

### Pivot

**Vztažný bod objektu: kolem něj se rotuje a škáluje, k němu se přichytává — na jeho umístění záleží víc, než je vidět.**

Nekonzistentní pivoty mezi asset packy rozbíjejí sockety (každá zbraň sedí v ruce jinak) i navazování dílců. Oprava bez DCC: modeling mode → Transform → Edit Pivot, přijmout a instance v levelu vyměnit. U kyvadel a pák je pivot přímo herní mechanika — bod závěsu určuje dráhu.

Kde se s tím potkáš: [Tipy do editoru](praxe/editor-tipy.md) · [Pasti a mechaniky](praxe/pasti-a-mechaniky.md)

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

### Retopologie

**Přestavba geometrie na čistší síť: z milionů neuspořádaných trojúhelníků (sculpt, sken, AI generát) použitelný mesh pro rig a animaci.**

AI pipeline ji řeší třemi cestami: decimace + normal bake (rychlá, „topologie pro start"), smart low poly režimy generátorů (pečou normal mapu z HD verze), nebo nástroje jako Quad Remesher. Na čem záleží: deformující se části (klouby, obličej) chtějí pořádnou topologii, rekvizity snesou decimát.

Kde se s tím potkáš: [AI assety](praxe/ai-assety.md) · [AI agenti](praxe/claude-code-ue.md)

### Retriggerable Delay

**Delay, který se každým dalším spuštěním restartuje od nuly — doběhne až po klidu na vstupu.**

Ideální „ztráta zájmu" AI: dokud percepce cíl hlásí (a event se opakuje), odpočet se resetuje; jakmile hlásit přestane, delay doběhne a vrátí AI k patrole. Délka musí být větší než interval, kterým se vstup opakuje (u Pawn Sensingu > 0,5 s), jinak doběhne i mezi dvěma hlášeními.

Kde se s tím potkáš: [AI vnímání](praxe/ai-vnimani.md) · [Základy AI](praxe/ai-zaklady.md)

### Rewind Debugger

**Nahraje běh hry a nechá tě scrollovat časem: co hrálo, proč to Motion Matching vybral, jak rozhodoval State Tree.**

`Debug → Rewind Debugger`, zapni auto-record (+ auto-eject). Dvojklik na track otevře asset na správném framu; šipkami jdeš frame po framu; eject kamery přehraje pohyb ve světě. Pose search debugger uvnitř ukazuje kandidáty, ceny a channels breakdown; od 5.7 má vlastní track i State Tree — vidíš přesný frame, kdy padlo rozhodnutí.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md) · [GASP](praxe/gasp.md)

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

### Signal-to-noise ratio

**Poměr užitečné informace (signál) k balastu (šum) — klíčová veličina učení, soustředění i designu obtížnosti.**

Učení je budování prediktivního modelu světa a potřebuje data, ze kterých se dá učit. Frustrace = konstantní „špatně" (nulový signál), nuda = konstantní „dobře" (nulový signál); flow kanál je pásmo, kde některé akce fungují a jiné ne — nejlepší signál. Jasné cíle jsou filtr šumu; soustředění je totéž z druhé strany (rozptýlení a vizuální balast = šum).

Kde se s tím potkáš: [Zábava: flow](teorie/zabava.md)

### Silueta

**Obrys tvaru — nejrychlejší nosič identity a čitelnosti; poznáš z ní postavu i prostředí bez jediného detailu.**

V prostředí siluety vyrábí kontrast světla a stínu (chiaroscuro): žádný kontrast = žádné tvary = „proč to vypadá špatně, když mám Nanite?". Test: screenshot → odbarvit → levels stáhnout na černobílou; když nezbydou čitelné plochy světla a tmy, žádný setting scénu nezachrání. U assetů rozhoduje silueta o rozpoznatelnosti víc než textury.

Kde se s tím potkáš: [Stavba prostředí](praxe/env-tvorba.md) · [Breakdowny](praxe/env-breakdowny.md)

### Single Layer Water

**Shading model pro vodu: translucence a kaustika za cenu jednoho průchodu — de facto standard v UE.**

Zásadní limit: stíny přijímá jen z primárního directional lightu — scéna svícená spotlighty se na hladině rozpadne. Řešení per záběr: přepnout materiál na Default Lit (+ metallic 1 pro tmavou hlubokou vodu) tam, kde translucenci nepotřebuješ. Žádný z modelů není univerzálně lepší.

Kde se s tím potkáš: [Nástroje: EasyWaterscape](praxe/nastroje-voda.md)

### Smart Object

**Objekt světa, který inzeruje interakce: sloty k zabrání a chování (State Tree), které se po claimu spustí na postavě.**

Lavička nese smart object komponentu a definition data asset; NPC si najde volný slot, claimne ho (druhé NPC už ho nedostane) a spustí injektovaný strom — jiný objekt dodá jinou logiku, beze změny AI postavy. V GASP navázané na Motion Matching: vstupní montáž se vybírá pose match sloupcem podle pózy a vzdálenosti od vstupního bodu.

Kde se s tím potkáš: [GASP](praxe/gasp.md)

### Soft boundary

**Hranice mapy, kterou lze fyzicky překročit — ale svět dá jasně najevo, že je to špatný nápad.**

Pět vzorů: narativní (most se zřítí, postava odmítne jít dál), countdown (mráz, plyn, dezerce — tlak času místo kolize), nepřátelská (za hranicí loví něco silnějšího; nemusí zabíjet — stačí probrat se potlučený zpátky), ekonomická (kyslík/palivo nevystačí na návrat) a percepční (ztráta orientace a viditelnosti). Nejlépe fungují kombinované a vždy s fikčním alibi.

Kde se s tím potkáš: [Prostor a hranice](teorie/prostor-a-hranice.md)

### Sound Cue

**Klasický zvukový asset UE: graf uzlů nad wave soubory — random variace, mixování, attenuace.**

Multi-select wave souborů → Create Sound Cue vloží Random uzel automaticky (variace kroků jedním klikem). Pro pokročilejší práci (parametry za běhu, procedurální audio) je nástupcem MetaSounds; Sound Cue zůstává nejrychlejší cesta k „přehraj náhodnou variaci".

Kde se s tím potkáš: [Kroky](praxe/footsteps.md)

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

### Subsystem

**Automaticky vytvářený singleton s definovaným životním cyklem (engine / game instance / world / local player).**

Nemusíš ho spawnovat ani registrovat — engine ho vytvoří a drží podle typu. Game instance subsystem žije po celou dobu aplikace, ideální pro mediátory (event manager, broadcast kanály) a služby bez vlastního místa ve světě. Blueprintově se konzumuje snadno; definice vyžaduje C++.

Kde se s tím potkáš: [Komunikace Blueprintů](praxe/komunikace-blueprintu.md) · [Principy architektury](praxe/principy-architektury.md)

### Sync marker

**Značka v animaci (typicky došlap L/R), podle které se synchronizují klipy různých délek při blendování.**

Bez markerů se walk/run/sprint v blend space fázově rozjedou a mix „plave". Markery musí mít **stejná jména** napříč klipy (L, R) — stažené animace je často nemají a je potřeba je doplnit ručně podle došlapů.

Kde se s tím potkáš: [Základy pohybu](praxe/pohyb-zaklady.md)

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

### Tutorial hell

**Smyčka „sleduju tutoriály, umím je zopakovat, ale sám nepostavím nic" — nejčastější past učení enginu.**

Sledování není učení. Útěk je vždycky stejný: po každém tutoriálu zavřít video a postavit něco malého vlastního s tím, co ses právě naučil. Mezera mezi následováním kroků a vlastním myšlením se zavírá jen malými dokončenými projekty — dveře, mince, postava s damage.

Kde se s tím potkáš: [Tipy do editoru](praxe/editor-tipy.md) · [Začátky bez zkušeností](teorie/zacatky-bez-zkusenosti.md)

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

### Virtual bone

**Kost existující jen v enginu — přidá se na skeleton (Add Virtual Bone) bez re-exportu z DCC nástroje.**

Sleduje transform zdrojové kosti vůči jiné; typické použití: IK cíle (foot IK pro skeleton, který IK kosti nemá — MetaHuman) a odvozené sockety. Rychlá cesta, jak cizímu skeletonu doplnit, co rig očekává.

Kde se s tím potkáš: [MetaHuman v praxi](praxe/metahuman.md)

### Virtual texture

**Textura rozsekaná na stránky, které se streamují jen tam, kam se kamera dívá — „Nanite pro textury".**

Pevný pool stránek ve VRAM: při přeplnění nejhůř rozmazání, nikdy out-of-memory. Ulevuje CPU (méně unikátních materiálů) i paměti, daní je page table indirekce — extra GPU čas na každý přístup, takže ne na všechno. Ideální pro obří plochy s kritickým detailem; runtime virtual textures navíc pohánějí blending terénu.

Kde se s tím potkáš: [Textury a DLSS](praxe/textury-a-dlss.md) · [Breakdowny](praxe/env-breakdowny.md)

### Volumetric fog

**Objemová mlha: světlo se rozptyluje v „hustotě vzduchu" — paprsky, god rays a atmosféra s hloubkou.**

Zapíná se na Exponential Height Fog; tvar řídí scattering distribution, start distance a height falloff. Materiály s domain Volume do ní kreslí vlastní objemy (mlha Silent Hill 2). Kvalita: r.VolumetricFog.GridPixelSize (default 8, nižší = jemnější) a GridSizeZ (128 → 256/512, ten dražší).

Kde se s tím potkáš: [Osvětlení](praxe/osvetleni.md) · [Stavba prostředí](praxe/env-tvorba.md)

### Water Body

**Actor Water pluginu: ocean, lake, river, island — vodní tělesa tvarovaná splinami, vzájemně propojitelná.**

Klávesa G ukáže spline pointy; řeka má rychlost proudu per point (alt+tažení přidává body). Vztah k terénu řeší Edge Offset / Channel Edge Offset a falloff mode (Angle→Width proti hřebeni u břehu); landscape drž ~1 cm nad nulou. Vestavěné: waterline efekt kamery a podvodní post-process.

Kde se s tím potkáš: [Voda a buoyancy](praxe/voda-a-buoyancy.md) · [Interaktivní voda](praxe/interaktivni-voda.md)

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
