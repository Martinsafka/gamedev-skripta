# Případovka: Hex-A-Gone z PCG

Rekonstrukce minihry z Fall Guys — hex podlaha, kde se dlaždice za hráčem roztřesou a odpadnou, patro po patru — jako **jeden PCG graf**, který jde vzít, položit kamkoli a klidně otočit. Případovka spojuje dvě předchozí kapitoly do funkční hry: [PCG](pcg-zaklady.md) staví mřížku, [Instanced Actors](instanced-actors.md) ji nechají žít jen kolem hráče. Tutéž mechaniku stavěla [kapitola o pastech](pasti-a-mechaniky.md#hex-a-gon-mizejici-podlaha-a-la-fall-guys) postaru — ručně poskládanými dlaždicemi s per-instance blueprintem; srovnání obou přístupů je půlka poučení.

---

## Hex mřížka z jednoho grafu

**Zdroj:** [I Recreated Fall Guy's Hex-A-Gone Game Using PCG. Here's How I Did It!](https://www.youtube.com/watch?v=G5eXYvFbMko) · [Procedural Minds](https://www.youtube.com/channel/UCkfvcZJ6dGNUSCWOCVQnkXw) · ~25 min, tutoriál

**Shrnutí:** Hexagonovou podlahu o třech patrech vygeneruje graf z jediného splinu — jádro je aritmetika: **řádek bodu spočítat z jeho X pozice**, liché řádky posunout o půl dlaždice a řady sesunout k sobě, aby do sebe šestiúhelníky zapadly [(6:16)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=376s). Žádný asset zvenku — i hexagon vznikne v enginu.

### Rozpad myšlenky

**Dlaždice v modeling mode:** `Shift+5` → Create → Cylinder s radius 100, height 20 a **sides 6** — hotový hexagon (skončí ve složce _GENERATED) [(0:48)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=48s) [(1:34)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=94s). Kolizi mesh dostane přes **auto convex collision** v mesh editoru [(2:20)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=140s); materiál poslouží basic orange z engine contentu (cog → zapnout engine/plugin content) [(12:28)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=748s).

**Nosný blueprint:** box collision 2000×2000 vymezuje arénu a **spline** definuje její tvar — right-click na bod → spline generation panel → **generate circle** (radius 2000) → počet bodů **6** → closed loop → všechny body **linear**: šestiúhelník ze šestiúhelníků [(3:07)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=187s) [(3:53)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=233s) [(4:41)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=281s). K tomu PCG komponenta s grafem.

**Mřížka:** **Spline Sampler** s dimension *on interior* a spacing 200 (= průměr dlaždice) [(4:41)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=281s) [(5:28)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=328s) dá čtvercový rastr — hexagony na něm nezapadají [(6:16)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=376s). Oprava ve třech krocích:

1. **Číslo řádku:** Subtract `position.X` bodu − `position.X` aktoru (Get Actor Data, single point) do atributu `row` — díky relativnosti přežije posun celé arény [(7:03)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=423s) [(7:50)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=470s); Divide 200 → row −8…8 [(7:50)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=470s).
2. **Liché řádky posunout:** Modulo 2 + compare == 0 do filter pinu **Filter Attribute Elements** (target = point density, která je všude 1 — boolean z compare se s ní přímo porovná) [(8:36)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=516s) [(9:23)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=563s); outside větev → Transform Points +100 Y (půl dlaždice) [(9:23)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=563s). Obě větve pak scale 1,1 v X/Y (ne Z, bez uniform) proti spárám [(10:10)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=610s).
3. **Sesunout řady:** merge → Multiply `row` × −20 → **Add Attribute** `position.X += row` — řady se stáhnou na správnou rozteč [(10:56)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=656s) [(11:42)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=702s).

**Patra:** **Duplicate Point** ×3 s transformem +500 Z [(11:42)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=702s) [(12:28)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=748s). Spline okraj není dokonalý — pár bodů se doladí ručně [(12:28)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=748s).

> **Pozn.:** Hodnoty 200/100/±20 vycházejí z radius 100 dlaždice — jiná velikost, jiná čísla, vzorec zůstává [(5:28)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=328s). A trik s density ve filtru je chytrá špína: filter potřebuje atribut k porovnání a density == 1 je vždy po ruce. Srovnej s [row-based logikou v brush scatteringu](pcg-zaklady.md#opravdovy-stetec-scattering-vlastnim-grafem) — attribute matematika je univerzální jazyk PCG.

**Souvislosti:** [Mizející dlaždice](#mizejici-dlazdice-instanced-actors-v-akci) · [PCG základy](pcg-zaklady.md) · [Rejstřík: PCG](../rejstrik.md#pcg) · [Rejstřík: spline](../rejstrik.md#spline)

---

## Mizející dlaždice: Instanced Actors v akci

**Zdroj:** [I Recreated Fall Guy's Hex-A-Gone Game Using PCG. Here's How I Did It!](https://www.youtube.com/watch?v=G5eXYvFbMko) · [Procedural Minds](https://www.youtube.com/channel/UCkfvcZJ6dGNUSCWOCVQnkXw) · ~25 min, tutoriál

**Shrnutí:** Stovky dlaždic nemůžou být blueprinty — a static meshe z PCG zase nemají kolizi ani logiku [(13:15)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=795s). **Spawn Instanced Actors** dá obojí: podlaha je levné instance, a jen dlaždice do 750 jednotek od hráče se probouzejí jako blueprinty se shake-and-destroy logikou [(17:54)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=1074s) [(18:40)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=1120s). Nejhezčí trik případovky: **destrukce dlaždice začíná miniaturním posunem**, který ji ejektne z hive mind.

### Rozpad myšlenky

**Setup:** BP_HexagonPlatform se static mesh komponentou; v grafu místo Static Mesh Spawneru **Spawn Instanced Actors**; registry rituál stejný jako v [kapitole Instanced Actors](instanced-actors.md#swap-podle-vzdalenosti-setup-pres-data-registry) — Data Registry + data table (row `BP_HexagonPlatform_C`), directories to scan, validace Force Regen; autorovi warningy dělal vlastní překlep v registry type [(14:02)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=842s) [(16:21)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=981s) [(17:08)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=1028s). V data table: **max actor distance 750** (blíž = blueprint, dál = instance) a **eject on actor moved** s prahem téměř nula — jakýkoli pohyb dlaždici trvale osamostatní [(18:40)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=1120s).

**Detekce hráče bez hex kolizního primitivu:** box/kapsle/koule tvarem nesedí — **duplikát hexagon meshe** `_Overlap` nad dlaždicí, custom kolize ignore all + overlap Pawn, hidden in game [(19:28)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=1168s). Begin Overlap → **Get Instigator → Is Player Controlled** → spustit zánik [(20:15)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=1215s).

**Shake and destroy:** delay 0,5 s (ať dlaždice nepanikaří hned) → **Set Timer by Event** 0,05 s, loop, *max once per frame* → shake event: Set Relative Rotation s random floaty ±2° v X/Y/Z [(21:03)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=1263s) [(21:49)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=1309s). Pak pointa: **Set Actor Location** (world, ne relative!) na `get actor location − 0,1` — miniposun překročí ejekční práh, dlaždice opustí hive mind a **teprve pak** ji smí Destroy Actor sprovodit ze světa; instanci by nezničil [(22:35)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=1355s). Dalších 0,5 s třesu a destroy [(22:35)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=1355s).

**Bug třesoucí se kamery:** hráč stojící na rotující dlaždici rotuje s ní i s kamerou [(22:35)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=1355s). Řešení — rozdělit zodpovědnosti: **vizuální hexagon no collision** (ten se třese) + **kolizní duplikát** block, hidden in game (ten drží hráče a nehýbe se); alternativa je čistě materiálový třes přes world position offset [(23:23)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=1403s) [(24:11)](https://www.youtube.com/watch?v=G5eXYvFbMko&t=1451s).

> **Pozn.:** Srovnání s [ruční verzí ze starší kapitoly](pasti-a-mechaniky.md#hex-a-gon-mizejici-podlaha-a-la-fall-guys) je celá lekce: tam každá dlaždice je blueprint od začátku (jednodušší, ale stovky actorů), tady blueprint vzniká jen kolem hráče a podlaha škáluje na tisíce dlaždic. Dramaturgie zániku (cuknutí → pád) zůstává stejná — změnila se infrastruktura pod ní. A vzor „chci instanci zabít → napřed ji miniposunem ejektni" se hodí kdekoli, kde Instanced Actors potkají destrukci.

**Souvislosti:** [Instanced Actors](instanced-actors.md) · [Pasti: Hex-A-Gon postaru](pasti-a-mechaniky.md#hex-a-gon-mizejici-podlaha-a-la-fall-guys) · [Rejstřík: instanced actors](../rejstrik.md#instanced-actors) · [Rejstřík: trigger volume](../rejstrik.md#trigger-volume)
