# Pasti a arénové mechaniky

Past je gameplay systém v nejčistší podobě: detekce (overlap) → následek (damage, odhození) → obnova (delay, reset). Kapitola staví pět pastí ze dvou tutoriálů — bodáky, tlačící rameno, rotující věž, kyvadlové sekery, mizející podlaha à la Fall Guys — a končí minutovou, ale zásadní lekcí o férovosti hitboxů. Vzory (timeline, sockety na kostech, instance editable parametry) se hodí daleko za pasti.

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

## Hitboxy: velkorysost, ne přesnost

**Zdroj:** [Game Dev Secrets: A Simple Hitbox Trick!](https://www.youtube.com/watch?v=X0jy94VP_Ko) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~1 min, design tip

**Shrnutí:** Nejčastější chyba začátečníků: hitboxy přesně kopírující sprite/mesh. Dobré hry **podvádějí ve prospěch hráče** [(0:02)](https://www.youtube.com/watch?v=X0jy94VP_Ko&t=2s): zásah, který se *technicky* dotkl jedním pixelem, ale *pocitově* minul, je čistá frustrace. Hollow Knight nechává rytíři čtvrtinu hlavy mimo hurtbox — a hráči si připisují těsné úhyby jako vlastní skill [(0:48)](https://www.youtube.com/watch?v=X0jy94VP_Ko&t=48s).

### Rozpad myšlenky

Pravidlo: **hurtbox hráče menší než postava, hitboxy nepřátel spíš menší než jejich efekty.** Hráč nikdy nemá přemýšlet „jak mě tohle mohlo trefit?" — každý takový moment eroduje důvěru v ovládání. V UE praxi to znamená: kolizní boxy pastí a útoků dělat vědomě těsnější než mesh (přesně jako tenké čepele u seker výš) a u hráče zmenšit zásahové zóny pod vizuální siluetu. „Aim for generosity, not accuracy."

> **Pozn.:** Souvisí s [game feel](../teorie/game-feel.md) kapitolou: férovost je vjem, ne geometrie. A pro naši hru: u stealth detekce platí totéž obráceně — kužel vidění stráže má být *menší*, než vypadá, aby těsné proplížení vycházelo hráčovi, ne AI.

**Souvislosti:** [Game feel](../teorie/game-feel.md) · [AI vnímání](ai-vnimani.md) · [Rejstřík: game feel](../rejstrik.md#game-feel)
