# Parkour postaru: vault, výlez a ledge grab

GASP má traversal hotový — ale stavět ho jednou vlastníma rukama má cenu: pochopíš, co všechno traces musí zjistit (je tam zeď? jak vysoká? jak tlustá? je nad ní místo?), a ta znalost se hodí i při ladění hotových systémů. Dva důkladné tutoriály tu staví klasiku na Character Movement Componentu: vault/výlez přes root motion montáže a ledge grab se zarovnáním na libovolný mesh. Moderní MM verzi téhož pokrývají [Systémy nad MM](mm-systemy.md) a [GASP traversal](gasp.md#traversal-pod-kapotou-chooser-vybere-montaz-mm-vybere-frame-warping-doladi-zbytek).

---

## Vault, nebo výlez? Tři trace to rozhodnou

**Zdroj:** [Vaulting & Climbing (Parkour) Part 1 - Unreal Engine 5 Tutorial](https://www.youtube.com/watch?v=6hPArmWkKJQ) · [Matt Aspland](https://www.youtube.com/channel/UC8_RNwftEO4isrX2LJowcpg) · ~24 min, tutoriál (part 1) ·
[Make Advance Vaulting System in Unreal Engine!](https://www.youtube.com/watch?v=TZ-lhSHQjPU) · [DevEdge Studio](https://www.youtube.com/channel/UCGa0hsNw3BK6xTDnVvfFltw) · ~13 min (bez přepisu)

**Shrnutí:** Celý systém stojí na třech line traces, které postupně odpovídají: **je přede mnou zeď?** (pozice + normála), **jak je vysoká?** (trace dolů zpoza líce) a **jak je tlustá?** (druhý trace dolů dál za lícem). Z odpovědí padne rozhodnutí — vault přes tenkou překážku, výlez na tlustou, climbing na vysokou — a provedení je root motion montáž s dočasně vypnutou kolizí.

### Rozpad myšlenky

**Příprava animací:** hromadně přes `Asset Actions → Bulk Edit via Property Matrix` zapnout **Enable Root Motion** [(1:36)](https://www.youtube.com/watch?v=6hPArmWkKJQ&t=96s), vyrobit z klipů montáže a těm hromadně prodloužit **Blend Out na 0,35 s** (default 0,25 „snapuje") [(2:23)](https://www.youtube.com/watch?v=6hPArmWkKJQ&t=143s). V AnimBP musí existovat `Default Slot` a control rig uzel je potřeba odpojit — s montážemi se hádá [(3:55)](https://www.youtube.com/watch?v=6hPArmWkKJQ&t=235s).

**Tři otázky, tři traces:**

1. **Je zeď?** Start = pozice postavy −55 Z, end = +forward × 70; zásah uloží `wall location` + `wall normal` [(8:37)](https://www.youtube.com/watch?v=6hPArmWkKJQ&t=517s).
2. **Jak vysoká?** Z bodu 10 jednotek *za* lícem zdi (po normále dovnitř) a 200 nad ním trace dolů → `wall height` [(10:58)](https://www.youtube.com/watch?v=6hPArmWkKJQ&t=658s). Rozhodnutí: `(wall height − wall location).Z > 80` → **should climb**; menší → vault/výlez. Číslo 80 je laditelný práh výšky [(13:17)](https://www.youtube.com/watch?v=6hPArmWkKJQ&t=797s).
3. **Jak tlustá?** Totéž 50 jednotek za lícem z výšky 250 → `wall height 2`; když se obě výšky liší o míň než 30, je nahoře plocha — **is wall thick** [(14:49)](https://www.youtube.com/watch?v=6hPArmWkKJQ&t=889s), [(16:24)](https://www.youtube.com/watch?v=6hPArmWkKJQ&t=984s).

**Provedení** [(17:10)](https://www.youtube.com/watch?v=6hPArmWkKJQ&t=1030s): kapsle `No Collision` + movement mode **Flying** — postavu teď vede root motion, kolize a gravitace by se pletly. Tlustá zeď → posun 50 jednotek proti normále + montáž „getting up" [(18:46)](https://www.youtube.com/watch?v=6hPArmWkKJQ&t=1126s); tenká → nastavit Z na `wall height − 20` (X/Y nechat) + montáž „vault" [(21:06)](https://www.youtube.com/watch?v=6hPArmWkKJQ&t=1266s). Po `Delay` v délce montáže vrátit kolizi (`Query and Physics`) a walking [(19:32)](https://www.youtube.com/watch?v=6hPArmWkKJQ&t=1172s).

**Dvě řemeslné lekce:** logika žije v **makru, ne funkci** — uvnitř jsou `Delay` uzly a latentní kód ve funkcích nefunguje [(7:03)](https://www.youtube.com/watch?v=6hPArmWkKJQ&t=423s). A guard boolean `can parkour` se musí vracet na true **v každé slepé větvi** (trace nic nenašel) — autor to jednu větev zapomněl a systém live umřel, dokud to nedohledal [(22:40)](https://www.youtube.com/watch?v=6hPArmWkKJQ&t=1360s). Klasika guard proměnných: každý exit je musí uklidit.

> **Pozn.:** Part 2 (climbing z „should climb" větve) v playlistu není — vaultovací základ je ale kompletní. DevEdge „Advance Vaulting" nemá anglické titulky, takže jen z popisu: plynulejší vaulting s důrazem na blending animací s pohybem postavy; bez přepisu ho nerozebíráme. Srovnání s [GASP traversalem](gasp.md#traversal-pod-kapotou-chooser-vybere-montaz-mm-vybere-frame-warping-doladi-zbytek) je poučné: stejné otázky (výška, hloubka, typ akce) tam zodpovídá chooser + MM výběr framu + motion warping — tři traces zůstávají, jen odpovědi zpracovává chytřejší mašinerie.

**Souvislosti:** [GASP: traversal pod kapotou](gasp.md#traversal-pod-kapotou-chooser-vybere-montaz-mm-vybere-frame-warping-doladi-zbytek) · [Rejstřík: traversal](../rejstrik.md#traversal) · [Rejstřík: root motion](../rejstrik.md#root-motion) · [Rejstřík: anim montage](../rejstrik.md#anim-montage)

---

## Ledge grab: dva box traces a zarovnání na cokoliv

**Zdroj:** [How To Make Perfect Ledge Grabs Every Time - Unreal Engine](https://www.youtube.com/watch?v=gzb356i0Fqk) · [DEVenestration](https://www.youtube.com/channel/UC63huMjiPMXYy-oxAKNzc3g) · ~34 min, tutoriál

**Shrnutí:** Chytání říms, které sedí na **jakémkoli** meshi — primitiva, asset z Fabu, blueprint s víc meshi — protože pozici nečte z pivotu, ale z **Get Actor Bounds**. Dva box traces (dosah/výška + bok zdi), interpolovaný dojezd místo teleportu, výskok s automatickým řetězením na další římsu a odmítnutí tenkých či nízkých překážek.

### Rozpad myšlenky

**Proč box trace:** line trace stačí na hranaté levely, sphere/capsule trace zase vrací „šišatý" impact na kulatých profilech (tyče). Box s half size 25/5/1 dává rovný, předvídatelný zásah [(3:29)](https://www.youtube.com/watch?v=gzb356i0Fqk&t=209s) — jen mu nastav **orientaci = rotace actora**, jinak zůstane ve world space a při otočení postavy lže [(5:23)](https://www.youtube.com/watch?v=gzb356i0Fqk&t=323s).

**Smyčka a podmínka:** looping timer 0,5 s spuštěný skokem [(1:47)](https://www.youtube.com/watch?v=gzb356i0Fqk&t=107s); chytat jen při **pádu** (`velocity.Z < 0`) — vědomé designové rozhodnutí (druhá možnost: kdykoli ve vzduchu) [(2:24)](https://www.youtube.com/watch?v=gzb356i0Fqk&t=144s). **Trace 1** (od postavy vpřed a vzhůru) určuje dosah i výšku chytání [(4:18)](https://www.youtube.com/watch?v=gzb356i0Fqk&t=258s); **trace 2** míří do **boku** zdi ve výšce impact pointu — z jeho normály bude rotace [(6:59)](https://www.youtube.com/watch?v=gzb356i0Fqk&t=419s).

**Trik s Distance == 0:** místo třetího trace „je nad římsou místo?" stačí pole `Distance` v hit resultu — nula znamená *initial overlap* (trace začal uvnitř geometrie), takže podmínka `Distance > 0` zadarmo pozná, že nad hranou je volno [(9:58)](https://www.youtube.com/watch?v=gzb356i0Fqk&t=598s).

**Zarovnání na libovolný mesh** [(13:32)](https://www.youtube.com/watch?v=gzb356i0Fqk&t=812s): pivoty a root pointy se liší asset od assetu — jediná spolehlivá reference je `Get Actor Bounds` zasaženého actora: origin + box extent = světová výška hrany; od ní odečíst půl výšky kapsle (mesh sedí o půl kapsle níž) [(14:06)](https://www.youtube.com/watch?v=gzb356i0Fqk&t=846s). X/Y = pozice zdi minus forward × 50 (odstup rukou) [(17:02)](https://www.youtube.com/watch?v=gzb356i0Fqk&t=1022s); rotace = `impact normal × (−1)` → **Rot From X Vector** [(18:48)](https://www.youtube.com/watch?v=gzb356i0Fqk&t=1128s).

**Dojezd místo teleportu:** looping timer 0,1 s žene `VInterp To Constant` + `RInterp To Constant` k cílové pozici/rotaci [(23:43)](https://www.youtube.com/watch?v=gzb356i0Fqk&t=1423s); končí, když `Equal (s tolerancí)` potvrdí dosažení cíle (rotaci nech větší margin), *nebo* při předčasném odpojení [(24:32)](https://www.youtube.com/watch?v=gzb356i0Fqk&t=1472s). Visení řídí `grabbed` bool (AnimBP stavy jump→grab, fall→grab) a `can move` gating vstupu; klávesa zpět (`Y < 0`) → detach a walking [(20:34)](https://www.youtube.com/watch?v=gzb356i0Fqk&t=1234s).

**Výskok a řetězení:** montáž výskoku nese anim notify „jump" — v jeho okamžiku detach + `Launch Character` 1000 vzhůru [(29:02)](https://www.youtube.com/watch?v=gzb356i0Fqk&t=1742s); po krátkém delay se grab timer spustí znovu, takže postava **sama chytí další římsu** nad sebou (nebo pod sebou při seskoku) [(30:25)](https://www.youtube.com/watch?v=gzb356i0Fqk&t=1825s). A protože trace 2 startuje hned za koncem trace 1, systém chytá i tenké desky — nechtěné: snížením trace 2 o `grab offset Z` (~140–150) vyžaduješ zeď v délce těla pod římsou, kolena a plotny tím vypadnou [(31:13)](https://www.youtube.com/watch?v=gzb356i0Fqk&t=1873s).

> **Pozn.:** Návazný díl (tyče + shimmy do stran) v playlistu zatím není. Get Actor Bounds zarovnání je největší přenositelná hodnota — stejný princip použije cokoli, co se musí „přisát" na neznámou geometrii (žebříky, okraje střech). Pro srovnání: GASP tohle řeší značkováním překážek splinami a MM výběrem vstupního framu — robustnější, ale vyžaduje připravený obsah; tenhle systém funguje na syrovém blockoutu hned.

**Souvislosti:** [Systémy nad MM: traversal a cover komponenty](mm-systemy.md#traversal-cover-a-splhani-komponenty-se-state-managerem) · [GASP: traversal](gasp.md#traversal-pod-kapotou-chooser-vybere-montaz-mm-vybere-frame-warping-doladi-zbytek) · [Rejstřík: traversal](../rejstrik.md#traversal) · [Rejstřík: anim montage](../rejstrik.md#anim-montage)
