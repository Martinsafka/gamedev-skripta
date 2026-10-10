# Pasti, hádanky a arénové mechaniky

Past je gameplay systém v nejčistší podobě: detekce (overlap) → následek (damage, odhození) → obnova (delay, reset). Kapitola staví pasti — bodáky, tlačící rameno, rotující věž, kyvadlové sekery a mizející podlahu à la Fall Guys. K nim přidává stavebnici hádanky (spínač, kostka, plošina, klíče a dveře) a barel, ze kterého po zásahu teče voda. Končí minutovou, ale zásadní lekcí o férovosti hitboxů. Vzory (timeline, sockety na kostech, instance editable parametry, zprávy přes interface) se hodí daleko za pasti; útoky a zásahy postav řeší [Souboj](souboj.md).

---

## Kostra pasti a tři variace: bodáky, rameno, rotor

**Zdroj:** [3D Platformer Tutorial UE5 - Episode 5 - TRAPS!!!](https://www.youtube.com/watch?v=47d_s2e-RlM) · [Shane_Gamedev](https://www.youtube.com/channel/UCc5lY0z74OjPBtsWzaUni0Q) · ~23 min, tutoriál

**Shrnutí:** Jedna kostra, tři pasti. Kostra: overlap → ověř hráče → **Do Once** → `Apply Damage` → `Launch Character` (odhození) → delay → reset. Variace přidávají pohyb: animovaná kost se socketem, na kterém jede kolize, a **timeline s lerp vektorem** pro pohyb z bodu A do bodu B — s cílem editovatelným přímo v levelu přes 3D widget.

### Rozpad myšlenky

**Kostra (spike pit):** box collision na meshi → `On Component Begin Overlap` → `== Get Player Character` [(3:14)](https://www.youtube.com/watch?v=47d_s2e-RlM&t=194s) — nebo `Actor Has Tag` „damageable", pokud mají pasti zraňovat i nepřátele. `Do Once` brání opakovanému zásahu, `Apply Damage` s **instance editable** base damage (každá instance v levelu může zraňovat jinak) [(4:48)](https://www.youtube.com/watch?v=47d_s2e-RlM&t=288s). **Odhození**: `Launch Character` proti směru příchodu — forward vektor zasaženého × −350 v X/Y, Z = 600, override všech os [(6:23)](https://www.youtube.com/watch?v=47d_s2e-RlM&t=383s); delay 2 s → reset Do Once [(7:09)](https://www.youtube.com/watch?v=47d_s2e-RlM&t=429s). Autor poctivě přiznává, že Do Once na pasti je zkratka — správně patří nezranitelnost na *postavu* [(4:01)](https://www.youtube.com/watch?v=47d_s2e-RlM&t=241s), jinak každá past řeší imunitu po svém.

**Tlačící rameno — kolize na animované kosti:** skeletal mesh s `Use Animation Asset` (loop) [(9:30)](https://www.youtube.com/watch?v=47d_s2e-RlM&t=570s); na kost ramene se přidá **socket** a box collision dostane `Parent Socket` = ten socket — kolize se veze s animací [(10:16)](https://www.youtube.com/watch?v=47d_s2e-RlM&t=616s). Mesh samotný na `Block All`, ať postavu skutečně fyzicky tlačí, ne jen zraňuje [(11:02)](https://www.youtube.com/watch?v=47d_s2e-RlM&t=662s).

**Pohyblivý rotor — timeline dvakrát jinak:** pohyb = **Timeline** s float trackem 0→1 (3 s, linear = konstantní rychlost; Auto klíče = ease) [(16:32)](https://www.youtube.com/watch?v=47d_s2e-RlM&t=992s) → `Lerp (Vector)` mezi startem a **`destination location`** → `Set Relative Location`. Destination je instance editable + **Show 3D Widget**: v levelu se objeví diamant, kterým cíl dráhy prostě odtáhneš — každá instance jinam, bez otevírání blueprintu [(18:05)](https://www.youtube.com/watch?v=47d_s2e-RlM&t=1085s). Ping-pong: na `Finished` přečti `Direction` enum timeline a zavolej `Reverse`/`Play` + delay [(19:41)](https://www.youtube.com/watch?v=47d_s2e-RlM&t=1181s). Rotace = druhá timeline 0→360 za 1 s, **looping**, do Z osy `Set Relative Rotation` [(21:58)](https://www.youtube.com/watch?v=47d_s2e-RlM&t=1318s).

> **Pozn.:** Show 3D Widget je nenápadný editor-workflow klenot — stejné „nastav to v levelu, ne v grafu" myšlení jako spline patrol trasy ze [State Trees](state-trees.md#kostra-state-tree-ai-komponenta-tasky-a-kontext). A trik se socketem na kosti je obecný: cokoli (kolize, particle, zbraň) jde přivěsit na animovanou kost bez jediného řádku logiky.

**Souvislosti:** [Rejstřík: timeline](../rejstrik.md#timeline) · [Interakce bez Event Ticku: overlap vzory](interakce-bez-event-ticku.md) · [Rejstřík: trigger volume](../rejstrik.md#trigger-volume)

---

## Kyvadlové sekery: pivot, ping-pong a per-instance chování

**Zdroj:** [Moving Obstacles (Swinging Axes) Unreal Engine 5 Traps Tutorial](https://www.youtube.com/watch?v=RdItM2xmF5M) · [Zero2GameDev](https://www.youtube.com/channel/UCXloD6nri7psCbJYOBBnpRg) · ~22 min, tutoriál

**Shrnutí:** Kyvadlo stojí na jednom triku: **pivot je samostatná komponenta**. Válec jako root, sekera jako child pod ním — rotuješ válec, sekera se houpe [(2:38)](https://www.youtube.com/watch?v=RdItM2xmF5M&t=158s). Zbytek je konfigurovatelnost: jedna blueprint třída, ze které v levelu naklikáš smrtící kyvadlo, „boop" kyvadlo, pomalé kyvadlo i plně rotující turniket.

### Rozpad myšlenky

**Kyv:** timeline 1 s (0→1) → `Lerp` −90…90 → `Set Relative Rotation` Z **válce** [(7:26)](https://www.youtube.com/watch?v=RdItM2xmF5M&t=446s); default rotace válce −90, ať klidová poloha sedí [(8:34)](https://www.youtube.com/watch?v=RdItM2xmF5M&t=514s). Ping-pong přes `Direction` enum na Finished — stejný vzor jako u rotoru výše [(9:23)](https://www.youtube.com/watch?v=RdItM2xmF5M&t=563s). Kolize schválně jen **tenké boxy na čepelích** [(3:27)](https://www.youtube.com/watch?v=RdItM2xmF5M&t=207s) — autor to říká přesně: hráči chtějí stát co nejblíž a proběhnout; velkorysá mezera je feature (viz hitbox myšlenka níže).

**Per-instance chování přes instance editable proměnné:**

- `death?` bool — smrtící vs. odhazovací instance [(12:06)](https://www.youtube.com/watch?v=RdItM2xmF5M&t=726s); obojí komunikuje přes **Blueprint Interface** (death message / launch character s velocity) — past nezná třídu postavy [(4:23)](https://www.youtube.com/watch?v=RdItM2xmF5M&t=263s), [(13:43)](https://www.youtube.com/watch?v=RdItM2xmF5M&t=823s). Boop = launch v X/Y bez Z (ať to nezvedá do vzduchu), síla ~500 taky editable [(14:24)](https://www.youtube.com/watch?v=RdItM2xmF5M&t=864s).
- `swing time` → `Set Timeline Length` na BeginPlay [(17:33)](https://www.youtube.com/watch?v=RdItM2xmF5M&t=1053s): délka nad rámec klíčů = pauza v krajní poloze (5 s = líné kyvadlo), 0,5 = manické [(18:48)](https://www.youtube.com/watch?v=RdItM2xmF5M&t=1128s).
- `rotate fully` bool → místo timeline se zapne **Rotating Movement komponenta** s rotation rate v Z [(20:22)](https://www.youtube.com/watch?v=RdItM2xmF5M&t=1222s) — plná rotace zadarmo, bez grafu.

**Detail za zapamatování:** kamera se o sekery zasekávala — na meshi `Collision → Custom → Ignore Camera` [(15:12)](https://www.youtube.com/watch?v=RdItM2xmF5M&t=912s); stejná oprava jako u [State Trees punche](state-trees.md#prechody-pres-gameplay-tagy-a-event-dispatchery), jen z druhé strany.

> **Pozn.:** Tohle je učebnicová „designer-friendly" past: jedna třída, čtyři přepínače, level designér skládá obtížnost bez otevření grafu. Přesně tak vypadá [data-driven](../rejstrik.md#data-driven-design) myšlení v malém — a přesně proto se instance editable + expose on spawn vyplatí dávat od začátku.

**Souvislosti:** [Komunikace Blueprintů: interface](komunikace-blueprintu.md) · [Rejstřík: timeline](../rejstrik.md#timeline) · [Rejstřík: Blueprint Interface](../rejstrik.md#blueprint-interface)

---

## Hex-A-Gon: mizející podlaha à la Fall Guys

**Zdroj:** [Fall Guys Hex-A-Gon Tutorial Unreal Engine 4](https://www.youtube.com/watch?v=ANWzAitL0Jg) · [Unreal University](https://www.youtube.com/channel/UCQv4mwerZLQVe3wPbsMc-qw) · ~6 min, tutoriál (UE4 — vzor platí beze změny v UE5)

**Shrnutí:** Aréna z dlaždic, které po došlápnutí zmizí. Dvě části: **dlaždice** (overlap → klesni → zbělej → znič se — třífázový feedback, který dává hráči šanci reagovat) a **spawner**, který z for-loopů a flip flopu poskládá hexagonální mřížku.

### Rozpad myšlenky

**Dlaždice** [(0:50)](https://www.youtube.com/watch?v=ANWzAitL0Jg&t=50s): overlap → cast na hráče → Do Once → `Add Local Offset` −5 Z (dlaždice *cukne dolů* — hmatový signál) → delay 0,2 → `Set Material` bílá (vizuální varování) → delay 0,3 → `Destroy Actor` [(1:36)](https://www.youtube.com/watch?v=ANWzAitL0Jg&t=96s). Půl sekundy od došlapu ke zmizení je celý „coyote time" téhle mechaniky — prodloužením delayů se aréna změkčuje.

**Mřížka** [(2:22)](https://www.youtube.com/watch?v=ANWzAitL0Jg&t=142s): spawner se scene komponentou, na BeginPlay for-loop 0–10, pozice = world location + index × 160 na Y → `Spawn Actor from Class` [(3:08)](https://www.youtube.com/watch?v=ANWzAitL0Jg&t=188s). Druhá varianta řady s offsetem +90 [(3:54)](https://www.youtube.com/watch?v=ANWzAitL0Jg&t=234s) a finální spawner: řady po 150 na X, **Flip Flop** střídá rovnou a posunutou řadu — vzniknou zuby hexagonální mřížky [(5:30)](https://www.youtube.com/watch?v=ANWzAitL0Jg&t=330s).

> **Pozn.:** Za pozornost stojí dramaturgie dlaždice: *cuknutí → zbělení → zmizení* je miniaturní [telegraphing](../teorie/game-feel.md) — hráč se učí číst podlahu periferně. Kdo by stavěl celé kolo Fall Guys, přidá respawn vrstvy a Z-ové patra; kostka mechaniky je ale celá tady. A kdo by chtěl tisíce dlaždic místo stovek, najde v [PCG případovce Hex-A-Gone](pcg-hexagone.md) tutéž hru přes jeden graf a Instanced Actors.

**Souvislosti:** [Případovka: Hex-A-Gone z PCG](pcg-hexagone.md) · [Game feel](../teorie/game-feel.md) · [Rejstřík: trigger volume](../rejstrik.md#trigger-volume)

---

## Hádanka ze stavebnice: spínač nic nezná a level se nesmí dát rozbít

**Zdroj:** [How We Designed a Puzzle Adventure Game in Unreal Engine](https://www.youtube.com/watch?v=tpq66PFyzf0) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~18 min, přehled psané série Epicu (začátečnická úroveň)

**Shrnutí:** Epic ve videu provází výsledkem své psané série *Design a Puzzle Adventure Game*. Je to graybox level s klíči a dveřmi, tlakovou deskou, fyzikální kostkou, pohyblivou plošinou, pastmi, nepřítelem a cílem. Pod začátečnickým povrchem jsou dva vzory, které platí pro každou hádanku. **Spínač, který neví, co spíná:** pošle zprávu přes Blueprint Interface a reaguje, kdo chce. A **level, který se nedá rozbít:** výhra se počítá podle sebraných klíčů, ne podle dosaženého místa, a kostky se doplní, když je hráč ztratí.

### Rozpad myšlenky

**Data místo kopií.** Tři druhy klíčů jsou Enum, struct drží tvar a barvu a barvy jsou instance jednoho rodičovského materiálu [(2:20)](https://www.youtube.com/watch?v=tpq66PFyzf0&t=140s). Klíč i dveře mají mapu typ → vzhled. Druh se v levelu mění jedním rozbalovacím seznamem a barva dveří sama sedí ke klíči [(3:08)](https://www.youtube.com/watch?v=tpq66PFyzf0&t=188s), [(4:42)](https://www.youtube.com/watch?v=tpq66PFyzf0&t=282s).

**Smyčka klíč–dveře.** Klíč při overlapu přes interface řekne hráči, že dostal klíč, a zmizí [(3:56)](https://www.youtube.com/watch?v=tpq66PFyzf0&t=236s). Dveře se při overlapu ptají, jestli klíč vyžadují a jestli ho hráč má, přes `Contains Item` nad jeho seznamem [(5:32)](https://www.youtube.com/watch?v=tpq66PFyzf0&t=332s). Designově patří klíč tam, kde se pro něj musí něco udělat; v ukázce leží na vysoké plošině za skákacími překážkami [(6:18)](https://www.youtube.com/watch?v=tpq66PFyzf0&t=378s). A protože sebraný klíč zmizí z očí, ukazuje HUD zdraví a seznam klíčů. Pod textem je rozmazané pozadí, aby byl čitelný v jakémkoli prostředí [(7:05)](https://www.youtube.com/watch?v=tpq66PFyzf0&t=425s).

**Spínač, který nic nezná.** Tlaková deska se při overlapu rozsvítí a pošle zprávu přes interface `BPI_Interaction`, místo aby měla napevno zadrátováno, co spíná [(8:37)](https://www.youtube.com/watch?v=tpq66PFyzf0&t=517s). Plošina i ohnivá past ten interface implementují a reagují po svém [(9:23)](https://www.youtube.com/watch?v=tpq66PFyzf0&t=563s). Plošina jezdí tam a zpět mezi startem a target pointem a na koncích dvě sekundy čeká [(10:10)](https://www.youtube.com/watch?v=tpq66PFyzf0&t=610s). Deska nerozlišuje, kdo na ni stoupl. Fyzikální kostka ji zatíží a udrží stisknutou i po odchodu hráče, a tím otevře nové hádanky [(9:23)](https://www.youtube.com/watch?v=tpq66PFyzf0&t=563s).

**Pasti z jednoho rodiče.** Rodičovská past drží damage na časovači, dokud je někdo v kolizi [(10:56)](https://www.youtube.com/watch?v=tpq66PFyzf0&t=656s). Bodáky jsou potomek s mřížkou 4 × 4 kuželů. Oheň je potomek s červeným materiálem a interfacem, takže ho spínač zapíná a vypíná [(11:42)](https://www.youtube.com/watch?v=tpq66PFyzf0&t=702s).

**Level, který se nedá rozbít.**
- Cíl na vyvýšené plošině se odemkne jen se všemi třemi klíči. Je to záměr: hráč pak level neobejde ani tím, že najde cestu přes zeď [(16:25)](https://www.youtube.com/watch?v=tpq66PFyzf0&t=985s).
- Spawner kostek je neviditelný blueprint uvnitř trubky, který na spínač vypustí novou kostku. Drží pole vypuštěných kostek a nad limitem zničí nejstarší [(17:14)](https://www.youtube.com/watch?v=tpq66PFyzf0&t=1034s). Kostky se tak nedají ztratit nadobro, level se nezaplní stovkami fyzikálních kostek a hádanka zůstane řešitelná [(18:01)](https://www.youtube.com/watch?v=tpq66PFyzf0&t=1081s).

> **Pozn.:** Video říká, že spínač zprávu „vysílá" a slyšet ji může kdokoli. V termínech [komunikace Blueprintů](komunikace-blueprintu.md#tri-kanaly-a-kdy-ktery-cast-interface-event-dispatcher) je ale interface volání na konkrétní cíl, ne rádio, takže spínač musí vědět, komu volat. Jak série cíle drží, přehled neukazuje; podrobnosti jsou v psaném tutoriálu, na který video odkazuje, i se staženým projektem. Rodičovská past s damage je tentýž tvar jako [kostra pasti](#kostra-pasti-a-tri-variace-bodaky-rameno-rotor), jen místo instance editable přepínačů používá dědičnost. A „level se nesmí dát rozbít" je obrana proti tomu, čemu se říká [softlock](../rejstrik.md#softlock).

**Souvislosti:** [Interakce bez Event Ticku: Blueprint Interface](interakce-bez-event-ticku.md#blueprint-interface-volani-bez-castu) · [Graybox, beautiful corners a první level nakonec](../teorie/level-design-solo.md#graybox-beautiful-corners-a-prvni-level-nakonec) *(graybox, ve kterém se celé video odehrává)* · [Rejstřík: Material Instance](../rejstrik.md#material-instance) · [Rejstřík: Enum](../rejstrik.md#enum) · [Rejstřík: HUD](../rejstrik.md#hud)

---

## Barel, který teče: díry jako data, hladina jako jedno číslo

**Zdroj:** [Create a Water Leak System in Unreal Engine 5 | Blueprint Tutorial (Part 1)](https://www.youtube.com/watch?v=8aDH2KUGdbE) · [Zima Env](https://www.youtube.com/channel/UC1Ob_PAPVw5dL6XlpCfXuKg) · ~11 min, tutoriál (díl 1)

**Shrnutí:** Prostřelený barel začne téct z každé díry pod hladinou. Hladina klesá, s víc dírami rychleji, a vždycky jen k nejnižší díře. Díra, nad kterou hladina klesla, přestane téct [(0:02)](https://www.youtube.com/watch?v=8aDH2KUGdbE&t=2s). Celé je to jedno číslo (výška hladiny), pole děr a časovač místo ticku. Háček je v pravidle cíle: hladina nesměřuje ke dnu, ale k **nejnižší díře**. Právě díky tomu je z efektu systém, který si pamatuje, kam hráč střílel.

### Rozpad myšlenky

**Stav.** Barel a vodní plocha jsou v jednom blueprintu. Výška plochy je hladina, uložená jako float, a pivot barelu u dna určuje nejnižší možnou hladinu [(0:48)](https://www.youtube.com/watch?v=8aDH2KUGdbE&t=48s), [(1:25)](https://www.youtube.com/watch?v=8aDH2KUGdbE&t=85s), [(1:34)](https://www.youtube.com/watch?v=8aDH2KUGdbE&t=94s).

**Zásah.** Střelba může být jakýkoli line trace. Stačí zasaženého aktéra castnout na barel a předat mu impact point a normálu [(2:18)](https://www.youtube.com/watch?v=8aDH2KUGdbE&t=138s), [(2:51)](https://www.youtube.com/watch?v=8aDH2KUGdbE&t=171s). Zásah nad hladinou barel ignoruje. Pod hladinou přidá v místě zásahu Niagara komponentu s proudem vody, natočenou podle normály, a uloží ji do pole děr [(3:27)](https://www.youtube.com/watch?v=8aDH2KUGdbE&t=207s), [(4:34)](https://www.youtube.com/watch?v=8aDH2KUGdbE&t=274s). Efekt mířil o 90° vedle a autor to opraví složením rotací [(4:16)](https://www.youtube.com/watch?v=8aDH2KUGdbE&t=256s).

**Kontrola na časovači.** Místo Event Ticku, který podle autora umí být drahý, projde díry časovač jednou za pár sekund. Každá díra, nad kterou hladina klesla, zmizí [(5:11)](https://www.youtube.com/watch?v=8aDH2KUGdbE&t=311s), [(6:01)](https://www.youtube.com/watch?v=8aDH2KUGdbE&t=361s). Druhá větev sekvence najde nejnižší díru a hladina k ní postupně klesá; počáteční hodnota „nejnižší výšky" musí být obrovské číslo [(7:12)](https://www.youtube.com/watch?v=8aDH2KUGdbE&t=432s). Samotný pokles a jeho rychlost video staví bez komentáře [(7:58)](https://www.youtube.com/watch?v=8aDH2KUGdbE&t=478s).

> **Pozn.:** Barel je malý příklad toho, čemu [teorie imerze](../teorie/game-feel.md#imerze-svet-ktery-na-tebe-odpovida) říká svět, který odpovídá: zásah nezmizí, ale změní stav předmětu, který si ho pamatuje. Druhý díl autor podmiňuje odezvou diváků a chce zůstat u Blueprintů, protože výpočtů je málo [(10:22)](https://www.youtube.com/watch?v=8aDH2KUGdbE&t=622s). Kontrola na časovači místo ticku je stejný tah jako u [interakcí bez Event Ticku](interakce-bez-event-ticku.md#overlap-trigger-misto-trasovani-v-ticku).

**Souvislosti:** [Rejstřík: Set Timer by Event](../rejstrik.md#set-timer-by-event) · [Rejstřík: Line Trace](../rejstrik.md#line-trace) · [Rejstřík: Particle system](../rejstrik.md#particle-system) · [Zdraví po končetinách](souboj.md#zdravi-po-koncetinach-physical-material-jako-adresa-struct-jako-stav) *(jiný systém, který čte, kam hráč trefil)*

---

## Hitboxy: velkorysost, ne přesnost

**Zdroj:** [Game Dev Secrets: A Simple Hitbox Trick!](https://www.youtube.com/watch?v=X0jy94VP_Ko) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~1 min, design tip

**Shrnutí:** Nejčastější chyba začátečníků: hitboxy přesně kopírující sprite/mesh. Dobré hry **podvádějí ve prospěch hráče** [(0:02)](https://www.youtube.com/watch?v=X0jy94VP_Ko&t=2s): zásah, který se *technicky* dotkl jedním pixelem, ale *pocitově* minul, je čistá frustrace. Hollow Knight nechává rytíři čtvrtinu hlavy mimo hurtbox — a hráči si připisují těsné úhyby jako vlastní skill [(0:48)](https://www.youtube.com/watch?v=X0jy94VP_Ko&t=48s).

### Rozpad myšlenky

Pravidlo: **hurtbox hráče menší než postava, hitboxy nepřátel spíš menší než jejich efekty.** Hráč nikdy nemá přemýšlet „jak mě tohle mohlo trefit?" — každý takový moment eroduje důvěru v ovládání. V UE praxi to znamená: kolizní boxy pastí a útoků dělat vědomě těsnější než mesh (přesně jako tenké čepele u seker výš) a u hráče zmenšit zásahové zóny pod vizuální siluetu. „Aim for generosity, not accuracy."

> **Pozn.:** Souvisí s [game feel](../teorie/game-feel.md) kapitolou: férovost je vjem, ne geometrie. A pro naši hru: u stealth detekce platí totéž obráceně — kužel vidění stráže má být *menší*, než vypadá, aby těsné proplížení vycházelo hráčovi, ne AI.

**Souvislosti:** [Game feel](../teorie/game-feel.md) · [AI vnímání](ai-vnimani.md) · [Rejstřík: game feel](../rejstrik.md#game-feel) · [Hitbox podle poctivosti animace](souboj.md#hitbox-podle-toho-jak-poctiva-je-animace-impact-frame-nebo-active-frames) *(kdy se vyplatí přesnost)*
