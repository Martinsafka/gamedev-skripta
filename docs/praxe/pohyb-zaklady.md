# Základy pohybu postavy

Než přijdou Motion Matching a Mover, stojí za to umět pohyb „postaru" — Character Movement Component, pár proměnných a blend spacy. Tahle kapitola sbírá drobné pohybové mechaniky z šesti tutoriálů: tři rychlosti chůze, podřep a plazení, rychlost podle sklonu, nabíjený skok a zastavení u zdi. Každá je malá, ale dohromady dávají slovník, ze kterého se skládá pocit z pohybu — a pár vzorů (timer místo ticku, křivka místo lerpu, enum místo booleanů), které se hodí kdekoli.

---

## Tři rychlosti: walk, run, sprint přes Max Walk Speed

**Zdroj:** [Unreal Engine 5 Tutorial - Walk, Run, and Sprint Toggle](https://www.youtube.com/watch?v=f-NEj00qprs) · [The Real Unreal](https://www.youtube.com/channel/UC0is_44ph-5eC-K1uImsoRA) · ~8 min, tutoriál

**Shrnutí:** Nejjednodušší gait systém: tři float proměnné (walk 300, run 600, sprint 900), držení klávesy přepisuje `Max Walk Speed` v Character Movement Componentu a **blend space** podle rychlosti plynule míchá animace. Klíčový detail, který tutoriály často vynechají: bez **sync markerů** se běh a sprint nesynchronizují.

### Rozpad myšlenky

**Blend Space 1D** [(0:56)](https://www.youtube.com/watch?v=f-NEj00qprs&t=56s): osa pojmenovaná `speed`, minimum 0, maximum 900, šest dílků mřížky a `Snap to Grid` [(1:44)](https://www.youtube.com/watch?v=f-NEj00qprs&t=104s). Na hodnoty 0/300/600/900 se natahají klipy idle/walk/run/sprint [(2:30)](https://www.youtube.com/watch?v=f-NEj00qprs&t=150s) — s podrženým `Ctrl` jde po grafu přejíždět a blend si prohlédnout. Hotový blend space se pak jen vymění v locomotion stavu AnimBP [(4:30)](https://www.youtube.com/watch?v=f-NEj00qprs&t=270s).

**Sync markery — proč se mix rozpadá:** na rychlosti 750 (mezi run a sprint) animace „plavou" [(3:18)](https://www.youtube.com/watch?v=f-NEj00qprs&t=198s). Důvod: klipy různé délky se synchronizují podle markerů došlapů — a stažený sprint klip žádné nemá. Oprava je přidat do sprintu markery **L a R** (došlap levé/pravé) se *stejnými jmény*, jaká používá run animace [(4:05)](https://www.youtube.com/watch?v=f-NEj00qprs&t=245s). Od té chvíle se kroky fázově potkávají.

**Ovládání:** držení `Ctrl` → `Set Max Walk Speed` = walk, puštění → run; držení `Shift` → sprint, puštění → run [(5:38)](https://www.youtube.com/watch?v=f-NEj00qprs&t=338s). Default `Max Walk Speed` v komponentě nastavit na run (600), ať postava startuje v běhu [(6:46)](https://www.youtube.com/watch?v=f-NEj00qprs&t=406s).

> **Pozn.:** Hodnoty rychlostí drž na jednom místě (proměnné, ideálně stejné jako maxima blend spaců) — jakmile se rychlost v komponentě a v blend space rozjedou, animace přestane odpovídat pohybu. Je to primitivní příbuzný pravidla „movement model je ground truth" z [GASP](gasp.md#autoring-animaci-movement-model-je-ground-truth).

**Souvislosti:** [Rejstřík: blend space](../rejstrik.md#blend-space) · [Rejstřík: sync marker](../rejstrik.md#sync-marker) · [GASP: autoring animací](gasp.md#autoring-animaci-movement-model-je-ground-truth)

---

## Podřep a plazení: vestavěný Crouch, vlastní prone

**Zdroj:** [Unreal Engine 5 Tutorial - How to Crouch](https://www.youtube.com/watch?v=0DQJkzLqCLk) · [The Real Unreal](https://www.youtube.com/channel/UC0is_44ph-5eC-K1uImsoRA) · ~7 min ·
[How To Add A Crouch And Prone Mechanic With Animations](https://www.youtube.com/watch?v=7yRKF-_hMok) · [H2 Unreal](https://www.youtube.com/channel/UCYArU_xjvPYScURoHewLSAg) · ~14 min

**Shrnutí:** Crouch je v Character class **zadarmo**: funkce `Crouch`/`UnCrouch` + tři properties. Prone (plazení) engine nemá — staví se ručně: enum tří postojů, rozlišení tap/hold na jedné klávese timerem a ruční zmenšení kapsle. Pro čitelné přechody v AnimBP se hodí **state aliases**.

### Rozpad myšlenky

**Vestavěný crouch** [(0:49)](https://www.youtube.com/watch?v=0DQJkzLqCLk&t=49s): zavolej `Crouch` při stisku, `UnCrouch` při puštění. V Character Movement nastav `Crouched Half Height` (60 — menší kapsle projde nižším prostorem), `Max Walk Speed Crouched` (250) a hlavně **`Can Crouch` = true** [(1:37)](https://www.youtube.com/watch?v=0DQJkzLqCLk&t=97s) — bez toho se nestane nic. AnimBP si stav čte přímo z komponenty (`Is Crouching`) [(2:23)](https://www.youtube.com/watch?v=0DQJkzLqCLk&t=143s); kapsli při ladění zviditelníš odškrtnutím `Hidden in Game` [(5:06)](https://www.youtube.com/watch?v=0DQJkzLqCLk&t=306s).

**State aliases místo špagety přechodů** [(3:09)](https://www.youtube.com/watch?v=0DQJkzLqCLk&t=189s): alias ve state machine *zastupuje* všechny stavy zaškrtnuté v jeho details — jedno přechodové pravidlo z aliasu platí pro všechny najednou. Vzor: alias „to crouch" (zastupuje idle i walk/run) → stav Crouch při `is crouching`; alias „to stand" (zastupuje crouch i crouch walk) → idle při `not is crouching` [(3:57)](https://www.youtube.com/watch?v=0DQJkzLqCLk&t=237s). Dva aliasy nahradí čtyři ruční přechody — a s každým dalším stavem náskok roste. Nezapomeň crouch-walk klipu zapnout `Loop` [(5:57)](https://www.youtube.com/watch?v=0DQJkzLqCLk&t=357s).

**Prone na téže klávese — tap vs. hold** [(0:01)](https://www.youtube.com/watch?v=7yRKF-_hMok&t=1s): postoje řídí **enum** (standing/crouching/proning) a `Switch on Enum` po stisku [(1:52)](https://www.youtube.com/watch?v=7yRKF-_hMok&t=112s). Držení se detekuje kombinací bool (`true` na Started, `false` na Completed) a **Set Timer by Event** na 0,5 s spuštěného při crouchi [(3:17)](https://www.youtube.com/watch?v=7yRKF-_hMok&t=197s): když timer doběhne a klávesa je pořád dole, jde se do prone [(4:08)](https://www.youtube.com/watch?v=7yRKF-_hMok&t=248s); při puštění se timer zruší (`Clear and Invalidate Timer by Handle`) [(5:51)](https://www.youtube.com/watch?v=7yRKF-_hMok&t=351s).

**Prone uzel neexistuje** — dělá se ručně [(4:54)](https://www.youtube.com/watch?v=7yRKF-_hMok&t=294s): `Set Capsule Half Height` 20 (crouch má 40), `Max Walk Speed Crouched` 150; návrat do podřepu hodnoty vrací [(6:43)](https://www.youtube.com/watch?v=7yRKF-_hMok&t=403s). Animačně tři blend spacy (standing/crouching/proning) s maximem osy = příslušná max rychlost [(7:30)](https://www.youtube.com/watch?v=7yRKF-_hMok&t=450s) a state machine se třemi stavy, přechody podle rovnosti enumu [(12:31)](https://www.youtube.com/watch?v=7yRKF-_hMok&t=751s).

> **Pozn.:** Ruční prone přes `Set Capsule Half Height` je poctivý hack — na rozdíl od vestavěného crouche neřeší interpolaci kapsle ani „můžu se vůbec postavit?" (strop nad hlavou). Pro plnohodnotný stealth pohyb počítej s dopsáním overlap testu před vstáváním. Enum postojů je mimochodem přesně vzor stance systému, který GASP řeší [chooserem](gasp.md#kontrola-vyberu-databaze-podle-stavu-nested-choosery-interrupt-mode).

**Souvislosti:** [Rejstřík: state alias](../rejstrik.md#state-alias) · [Rejstřík: blend space](../rejstrik.md#blend-space) · [GASP: kontrola výběru](gasp.md#kontrola-vyberu-databaze-podle-stavu-nested-choosery-interrupt-mode)

---

## Rychlost podle sklonu terénu

**Zdroj:** [Using Floor Angle to Determine Walk Speed](https://www.youtube.com/watch?v=K87dmHB1M54) · [DEVenestration](https://www.youtube.com/channel/UC63huMjiPMXYy-oxAKNzc3g) · ~5 min, tip

**Shrnutí:** Do kopce pomaleji, z kopce rychleji — úměrně sklonu. Celé je to jeden line trace dolů, jeden utility uzel na úhel svahu a jeden **Map Range Clamped** do `Max Walk Speed`.

### Rozpad myšlenky

Trace z pozice postavy 150 jednotek dolů [(0:51)](https://www.youtube.com/watch?v=K87dmHB1M54&t=51s) vrátí normálu podlahy; uzel **Get Slope Degree Angles** (normála + up vector + right vector postavy) z ní spočítá *pitch* svahu ve stupních [(1:34)](https://www.youtube.com/watch?v=K87dmHB1M54&t=94s). Ten se přemapuje: **Map Range Clamped** ze vstupu −45…45° (default `Walkable Floor Angle` je 44,76° [(2:56)](https://www.youtube.com/watch?v=K87dmHB1M54&t=176s)) na výstup 900…200 a výsledek rovnou do `Set Max Walk Speed` [(3:42)](https://www.youtube.com/watch?v=K87dmHB1M54&t=222s). Znaménko úhlu rozliší stoupání od klesání samo — proto ta záporná polovina rozsahu.

> **Pozn.:** Video to pouští na ticku; po vzoru wall-stop myšlenky níž to snese timer. A autor sám ukazuje limit: na ~40° svahu přestává sedět foot IK [(4:29)](https://www.youtube.com/watch?v=K87dmHB1M54&t=269s) — řešení téhle kategorie problémů rozebírá [procedurální vrstva GASP](gasp.md#proceduralni-vrstva-v-control-rigu-foot-placement-springy-a-locomotor). Pro naši hru je tohle levný realismus: únava z kopce je čitelná okamžitě, bez UI.

**Souvislosti:** [GASP: foot placement](gasp.md#proceduralni-vrstva-v-control-rigu-foot-placement-springy-a-locomotor) · [Rejstřík: Line Trace](../rejstrik.md#line-trace) · [Rejstřík: foot placement](../rejstrik.md#foot-placement)

---

## Nabíjený skok: Elapsed Seconds, normalizace a křivka

**Zdroj:** [Unreal Engine 5 Tutorial - Charged Jump Part 1: The Jump](https://www.youtube.com/watch?v=CKvTgBf-9Ss) · [Ryan Laley](https://www.youtube.com/channel/UCsS5i15vvUbwfr_1JdRKCAA) · ~12 min, tutoriál

**Shrnutí:** Držíš klávesu, skáčeš výš. Technicky tři kroky: skok přesunout ze Started na **Completed**, dobu držení přečíst z pinu **Elapsed Seconds**, normalizovat na 0–1 a namapovat na `Jump Z Velocity`. A jedna lekce navíc: **tvar odezvy je Curve Float asset**, ne konstanta v kódu.

### Rozpad myšlenky

**Metoda napřed:** autor úlohu demonstrativně krájí na malé, *měřitelné* kroky [(0:54)](https://www.youtube.com/watch?v=CKvTgBf-9Ss&t=54s) — nejdřív „skoč při puštění" (přepojit `Jump` z pinu Started na Completed), otestovat, pak teprve výška. Drobnost, ale přesně takhle se dá stavět cokoli.

**Měření držení:** event input akce má pin **Elapsed Seconds** — čas mezi Started a Completed [(2:26)](https://www.youtube.com/watch?v=CKvTgBf-9Ss&t=146s). `Normalize to Range` s maximem 2 s ho převede na 0–1 [(3:13)](https://www.youtube.com/watch?v=CKvTgBf-9Ss&t=193s) — pozor, delší držení vrací hodnoty **přes 1**, takže následuje `Clamp` 0–1, jinak hráč „nabije" skok do nekonečna. Print string test před pokračováním [(4:00)](https://www.youtube.com/watch?v=CKvTgBf-9Ss&t=240s).

**Aplikace:** `Set Jump Z Velocity` **před** voláním `Jump` — lerp od 420 (default, minimum) do ~1680 s clampnutou hodnotou jako alphou [(4:46)](https://www.youtube.com/watch?v=CKvTgBf-9Ss&t=286s).

**Křivka místo lerpu** [(6:13)](https://www.youtube.com/watch?v=CKvTgBf-9Ss&t=373s): Curve Float asset s klíči (0;0) a (1;1) dělá totéž co lerp — jeho smysl je ve *tvaru*. Klíče přepnout na Auto tangenty, přidat třetí klíč a máš odezvu, která preferuje vysoké hodnoty (0,5 s držení → 0,8 síly) nebo naopak [(8:27)](https://www.youtube.com/watch?v=CKvTgBf-9Ss&t=507s). Na characteru proměnná typu Curve Float → `Get Float Value` → alpha lerpu [(9:20)](https://www.youtube.com/watch?v=CKvTgBf-9Ss&t=560s). Ladění tvaru je čistý [game feel](../teorie/game-feel.md): testovat, ptát se hráčů [(10:23)](https://www.youtube.com/watch?v=CKvTgBf-9Ss&t=623s).

> **Pozn.:** Křivka jako asset = designér ladí odezvu bez sahání do grafů; stejný princip, jakým GASP řídí retargeting nebo foot pinning křivkami. Part 2 (UI ukazatel nabití) je za Patreon paywallem — v playlistu není, ukazatel si případně postavíme sami.

**Souvislosti:** [Game feel](../teorie/game-feel.md) · [Rejstřík: game feel](../rejstrik.md#game-feel) · [Rejstřík: data-driven design](../rejstrik.md#data-driven-design)

---

## Zastavení u zdi à la Resident Evil 9

**Zdroj:** [Epic Games Didn't Fix This, So I Had To Fix Myself | Resident Evil 9 Style](https://www.youtube.com/watch?v=83eC8TtVZTw) · [Hydra](https://www.youtube.com/channel/UCr_IB7PCjPJvh4dl8UdzH7g) · ~14 min, tutoriál

**Shrnutí:** Postava, která do zdi donekonečna „běží" s přehrávanou run animací, působí lacině — RE9 ji prostě zastaví [(0:10)](https://www.youtube.com/watch?v=83eC8TtVZTw&t=10s). Řešení: sphere trace před postavu, a když vidí zeď, **vynulovat dopřednou složku vstupu** dřív, než dojde do `Add Movement Input`. Ani GASP tohle v 5.7 neřeší [(0:56)](https://www.youtube.com/watch?v=83eC8TtVZTw&t=56s).

### Rozpad myšlenky

**Detekce:** funkce se **sphere trace** (spolehlivější zásah než tenký line trace [(2:53)](https://www.youtube.com/watch?v=83eC8TtVZTw&t=173s)): start = pozice + up × 50 (výška hrudi), end = + forward × 70, radius 10 [(3:24)](https://www.youtube.com/watch?v=83eC8TtVZTw&t=204s). Výsledek do proměnné `is hitting wall` [(5:02)](https://www.youtube.com/watch?v=83eC8TtVZTw&t=302s).

**Filtr vstupu:** vlastní funkce mezi input akcí a pohybem [(5:57)](https://www.youtube.com/watch?v=83eC8TtVZTw&t=357s). Osa X (strafe) jde do `Add Movement Input` s right vektorem z control rotation beze změny; osa Y projde testem `Y > 0 AND is hitting wall` → **Select Float** vybere 0, jinak původní Y [(8:00)](https://www.youtube.com/watch?v=83eC8TtVZTw&t=480s). Couvání a úkroky fungují dál, jen tlačení do zdi zmizí [(9:31)](https://www.youtube.com/watch?v=83eC8TtVZTw&t=571s) — a funguje to i v podřepu [(12:51)](https://www.youtube.com/watch?v=83eC8TtVZTw&t=771s).

**Timer místo ticku:** trace každý frame je zbytečný — `Set Timer by Function Name` (loop, `Max Once Per Frame`) na 0,5 s dělá tutéž práci za zlomek ceny; video to demonstruje print stringem, kde tick sype stovky výpisů za sekundu [(10:17)](https://www.youtube.com/watch?v=83eC8TtVZTw&t=617s). Stejná filozofie jako [interakce bez Event Ticku](interakce-bez-event-ticku.md).

> **Pozn.:** Půlvteřinový timer znamená, že stav zdi může být až 0,5 s starý — u pomalé hry v pohodě, u rychlé stáhni interval. A trace jede z **forward vektoru postavy**: ve strafe režimu (postava kouká jinam, než běží) by správně měl jet ze směru *pohybu*. Autor přiznává, že Mover postava má vstup jinde (`Get Move Input` funkce) a adaptaci nechává na příště [(12:05)](https://www.youtube.com/watch?v=83eC8TtVZTw&t=725s). Mimochodem přesně tohle je kategorie problému, kterou Epic plánuje řešit v Moveru trajectory queries s kolizemi — „brace for impact" animace (viz [Mover kapitola](mover.md)).

**Souvislosti:** [Interakce bez Event Ticku](interakce-bez-event-ticku.md) · [Game feel a imerze](../teorie/game-feel.md#imerze-svet-ktery-na-tebe-odpovida) · [Klouzání po zdi místo zastavení](#klouzani-po-zdi-misto-zastaveni-dokonceni-predchozi-myslenky) *(pokračování téhož autora — strafe i Mover dořešené)* · [Mover](mover.md) · [Rejstřík: Line Trace](../rejstrik.md#line-trace)

---

## Klouzání po zdi místo zastavení: dokončení předchozí myšlenky

**Zdroj:** [I Created THE LAST OF US PART 2 Style Wall Detection System | UE 5.8](https://www.youtube.com/watch?v=EL4s7sHAFV8) · [Hydra](https://www.youtube.com/channel/UCr_IB7PCjPJvh4dl8UdzH7g) · ~12 min, rozbor a ukázka integrace

**Shrnutí:** Předchozí myšlenka končí dvěma přiznanými dírami — trace jede z forward vektoru postavy (tedy špatně při strafu) a u Mover postavy to autor „nechává na příště". Tohle je to příště. A přináší k tomu **lepší chování než pouhé zastavení**: zeď hráče nezabrzdí, ale **odkloní**, podle toho, jak moc mimo její střed míří.

### Rozpad myšlenky

**Pozorování z hotové hry** [(0:02)](https://www.youtube.com/watch?v=EL4s7sHAFV8&t=2s): *„hrál jsem The Last of Us Part II a všiml si, jak funguje detekce zdi."* Pravidlo, které z toho vyčetl, má dvě polohy. Míří-li vstup **na střed zdi**, pohybový vstup se vynuluje — postava se zastaví, nešlape na místě. Jakmile směr **překročí hranici středu** doleva nebo doprava, zapne se příslušný **boční** vstup a postava po zdi plynule klouže.

Rozdíl proti [zastavení à la RE9](#zastaveni-u-zdi-a-la-resident-evil-9) je designový, ne technický: zastavení je **korektní**, klouzání je **ochotné**. Hráč, který běží podél stěny a mírně do ní tlačí, nechce zastavit — chce běžet dál. Zeď, která ho po sobě sveze, tedy neopravuje jeho chybu, ale **čte jeho záměr**. Proto tenhle vzor uvidíš ve hrách s rychlým pohybem a ten první ve hrách, kde má být kontakt se světem cítit.

**Druhé pozorování** [(2:54)](https://www.youtube.com/watch?v=EL4s7sHAFV8&t=174s) je nezávislé a stejně užitečné: *„když držíš protilehlé vstupy zároveň, pohyb se zastaví — W a S zároveň = nic. Totéž A a D."* Vypadá to jako drobnost, ale je to volba: alternativou je nechat vyhrát poslední stisk. Zastavení je čitelnější.

**Co to opravuje proti předchozí verzi.** Trace **jede podle vstupu a control rotation** [(5:34)](https://www.youtube.com/watch?v=EL4s7sHAFV8&t=334s) — *„což zajišťuje, že systém funguje i pro strafe"*. To je přesně ta výhrada z Pozn. u RE9 myšlenky. A **Mover varianta** [(10:00)](https://www.youtube.com/watch?v=EL4s7sHAFV8&t=600s): Epic dal u Mover postavy pohybovou logiku do **pure funkce `GetMoveInput`**, takže se její obsah smaže, ponechá se `IA_Move`, přidá komponenta a `SetMovementInput` se napojí rovnou na return node. Dvě otevřené věci z minula tedy padly obě.

**Zabalení do komponenty** [(4:40)](https://www.youtube.com/watch?v=EL4s7sHAFV8&t=280s): jedna složka s actor komponentou a enumem, *„díky oddělené složce se snadno migruje a je to plug and play"*. Parametry jsou **vystavené na komponentě** [(6:36)](https://www.youtube.com/watch?v=EL4s7sHAFV8&t=396s), takže se ladí přímo v detailech postavy — což je tentýž princip konfigurace místo větvení jako u [komponentního vzoru](principy-architektury.md#komponenty-misto-dedicnosti-skladej-misto-vetveni).

> **Pozn.:** Buď si vědom, co tohle video je a co není: **není to build tutoriál**. Je to rozbor mechaniky z cizí hry plus ukázka, jak hotovou komponentu zapojit — samotný systém autor prodává přes Patreon a graf ukazuje jen letmo. Hodnota pro nás je proto v **pozorování a v pravidle**, ne v postupu; obojí se dá naimplementovat podle popisu za odpoledne, protože jádrem je jediné rozhodnutí — porovnat směr vstupu s normálou zdi a podle odchylky vynulovat, nebo přesměrovat. Mimochodem přesně tohle je kategorie problému, kterou Epic plánuje řešit v Moveru přes trajectory queries s kolizemi.

**Souvislosti:** [Zastavení u zdi à la Resident Evil 9](#zastaveni-u-zdi-a-la-resident-evil-9) *(předchozí díl téhož problému)* · [Mover: setup a vstupy](mover.md#setup-od-nuly-v-57-pawn-input-producer-a-sitove-pasti) · [Principy architektury: komponenty](principy-architektury.md#komponenty-misto-dedicnosti-skladej-misto-vetveni) · [Game feel a imerze](../teorie/game-feel.md#imerze-svet-ktery-na-tebe-odpovida) · [Rejstřík: Movement Mode](../rejstrik.md#movement-mode)
