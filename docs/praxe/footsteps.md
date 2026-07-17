# Kroky: povrchy, zvuk a stopy

Kroky jsou nejčastější zvuk i nejčastější vizuální otisk hry — a přesně proto se vyplatí je udělat pořádně. Kapitola skládá čtyři zdroje do jednoho systému: **physical materials** jako společný základ (co je pode mnou?), dva způsoby spouštění (trace vs. anim notify), zvuk přes **MetaSounds** s hlasitostí podle rychlosti, **stopy jako decaly** s rozpadem v čase a optimalizace částic přes **Niagara Data Channel**. Pro stealth hru je tohle dvojnásob důležité: kroky jsou informace — pro hráče i pro [AI, která slyší](state-trees.md#jedna-percepce-tri-smysly-a-report-eventy).

---

## Physical materials a trace místo notify

**Zdroj:** [Unreal Engine 5.7 - Smart Footstep System (Physical Materials)](https://www.youtube.com/watch?v=6E-l9tWSCt4) · [Unreal - X - Tutorials](https://www.youtube.com/channel/UCjKg7gsHCEyXtJbZYx2Xu7A) · ~12 min, tutoriál

**Shrnutí:** Základ všech povrchových systémů: **Physical Surface typy** v Project Settings (sníh, štěrk, dlažba…), **physical material** asset pro každý typ a přiřazení buď v materiálu (všechny meshe s ním automaticky), nebo per-mesh overridem [(9:24)](https://www.youtube.com/watch?v=6E-l9tWSCt4&t=564s). Spouštění kroků řeší **trace z kostí chodidel** — a autor dobře vysvětluje proč: anim notify v každé animaci přestává škálovat v éře Motion Matchingu.

### Rozpad myšlenky

**Proč trace, ne notify** [(2:50)](https://www.youtube.com/watch?v=6E-l9tWSCt4&t=170s): klasika je Play Sound notify v každé walk/run animaci. Se stovkami MM animací (chůze, běh, strafe, crouch, stopy, otočky…) je to neudržitelné — a rozbije se při každé výměně animací. Trace systém animace vůbec nezná: ptá se *kostí*, kde jsou.

**Mechanika:** sphere trace (radius 5) z pozice foot socketu 10 jednotek dolů [(4:26)](https://www.youtube.com/watch?v=6E-l9tWSCt4&t=266s). Zásah → **Switch on EPhysicalSurface** ← `Get Surface Type` z hit resultu → nastavit odpovídající [Sound Cue](../rejstrik.md#sound-cue) [(5:48)](https://www.youtube.com/watch?v=6E-l9tWSCt4&t=348s) (cue z variací kroku: multi-select → Create Sound Cue → automatický Random uzel [(1:16)](https://www.youtube.com/watch?v=6E-l9tWSCt4&t=76s)). Klíčový je **edge detection bool `has touched`** [(6:34)](https://www.youtube.com/watch?v=6E-l9tWSCt4&t=394s): zvuk hraje jen v momentě *došlapu* (trace hit + `has touched` false), ne celou dobu kontaktu; bez zásahu se resetuje. Nohy se **střídají** proměnnou se jménem socketu — po každém kroku se přepne foot_r ↔ foot_l [(7:22)](https://www.youtube.com/watch?v=6E-l9tWSCt4&t=442s); jména socketů musí sedět přesně.

**Okrajové případy:** celé se to pouští jen při pohybu (velocity length > 0), jinak reset proměnných [(8:08)](https://www.youtube.com/watch?v=6E-l9tWSCt4&t=488s). Dopad ze skoku jede mimo — **Event On Landed**: hit location je uprostřed kapsle, takže odečíst `Get Scaled Capsule Half Height` a zavolat trace + zvuk [(10:10)](https://www.youtube.com/watch?v=6E-l9tWSCt4&t=610s).

> **Pozn.:** Trace-based vs. notify-based je stejný spor jako u [foot placementu v GASP](gasp.md#proceduralni-vrstva-v-control-rigu-foot-placement-springy-a-locomotor): notify (nebo contact curve) ví *přesně*, kdy animace došlapuje; trace to jen odhaduje z pozice kosti — zato funguje s čímkoli. Pro MM projekt bych volil trace nebo contact curves; pro ručně vyladěnou sadu animací jsou notifies přesnější (viz další myšlenka — obě cesty se nevylučují).

**Souvislosti:** [Rejstřík: physical material](../rejstrik.md#physical-material) · [Rejstřík: sound cue](../rejstrik.md#sound-cue) · [GASP: contact curves](gasp.md#proceduralni-vrstva-v-control-rigu-foot-placement-springy-a-locomotor) · [Hudba a zvuk: sound design ve hře](../hudba/sound-design-ve-hre.md) *(principy za herním zvukem)*

---

## MetaSounds: hlasitost a pitch podle rychlosti

**Zdroj:** [Footstep Sounds by Surface Type in Unreal Engine 5 (MetaSounds)](https://www.youtube.com/watch?v=e2N0dRLHsGY) · [Tank Control Games](https://www.youtube.com/channel/UCoHLpKMSi5LlOMFlxuoR1rA) · ~28 min, díl 2 série o surface detection

**Shrnutí:** Notify cesta udělaná pořádně — s enum pro levou/pravou nohu — a hlavně **MetaSound**, který randomizuje variace kroků a **plynule mění hlasitost i pitch podle rychlosti postavy**: jeden asset pro chůzi i běh, žádné duplikáty. Klíčový uzel na straně blueprintu: `Spawn Sound at Location` (ne Play!) — vrací audio komponentu, do které jde posílat parametry.

### Rozpad myšlenky

**Notify s daty:** blueprint třída AnimNotify → `Receive Notify` → owner meshe → cast na postavu → custom event [(3:32)](https://www.youtube.com/watch?v=e2N0dRLHsGY&t=212s). Na notify **instance editable enum** `E_StepType` (left/right) [(5:07)](https://www.youtube.com/watch?v=e2N0dRLHsGY&t=307s) — v animaci pak každý notify nese, která noha došlapuje [(6:40)](https://www.youtube.com/watch?v=e2N0dRLHsGY&t=400s).

**MetaSound graf** [(8:13)](https://www.youtube.com/watch?v=e2N0dRLHsGY&t=493s): pole wave assetů → `Random Get` → `Wave Player` (On Finished → output). **Speed input** (0–1) dělá dvě věci: clamp + **power 2** → multiply audio = hlasitost (mocnina roztáhne rozdíl chůze/běh) [(10:50)](https://www.youtube.com/watch?v=e2N0dRLHsGY&t=650s); druhý clamp 0,5–1 → pitch shift [(11:38)](https://www.youtube.com/watch?v=e2N0dRLHsGY&t=698s). V postavě: rychlost → `Map Range Clamped` (0…max run → 0…1) → **Set Float Parameter** „speed" na komponentě vrácené ze `Spawn Sound at Location` [(22:20)](https://www.youtube.com/watch?v=e2N0dRLHsGY&t=1340s), [(23:07)](https://www.youtube.com/watch?v=e2N0dRLHsGY&t=1387s). Per povrch pak stačí duplikovat MetaSound a vyměnit pole zvuků [(23:53)](https://www.youtube.com/watch?v=e2N0dRLHsGY&t=1433s).

**Gotcha, která sežere hodinu:** při pomalé chůzi zvuky zmizely — blend space defaultně spouští notifies jen z **highest weighted** animace, a u pomalé rychlosti vede idle (bez notifies). Oprava: v blend space `Notify Trigger Mode → All Animations` [(26:12)](https://www.youtube.com/watch?v=e2N0dRLHsGY&t=1572s).

> **Pozn.:** Video mimochodem staví i per-surface rychlosti pohybu (sníh a bláto zpomalují, na sněhu se nedá sprintovat…) přes struct hodnot per povrch [(19:52)](https://www.youtube.com/watch?v=e2N0dRLHsGY&t=1192s) — povrch tak ovlivňuje gameplay, ne jen audio. MetaSounds jsou proti Sound Cues výrazně schopnější (grafy jako AnimBP, parametry za běhu) a tohle je pěkný první kontakt: jeden parametr, dva efekty.

**Souvislosti:** [Rejstřík: MetaSounds](../rejstrik.md#metasounds) · [Rejstřík: anim notify](../rejstrik.md#anim-notify) · [Rejstřík: blend space](../rejstrik.md#blend-space) · [Základy pohybu: gaity](pohyb-zaklady.md#tri-rychlosti-walk-run-sprint-pres-max-walk-speed)

---

## Stopy jako decaly: nosíš s sebou předchozí povrch

**Zdroj:** [Surface-Based Footprint Decals in Unreal Engine 5 (Dynamic & Fading)](https://www.youtube.com/watch?v=buQ6JvwvHuw) · [Tank Control Games](https://www.youtube.com/channel/UCoHLpKMSi5LlOMFlxuoR1rA) · ~33 min, díl 4 série ·
[UE5 - Tutorial Interactive World (free plugin)](https://www.youtube.com/watch?v=xYGz-oGAGkk) · [REFORCH](https://www.youtube.com/channel/UCIo-VeCVIck9U3Oq1k9NPaw) · ~5 min (bez přepisu)

**Shrnutí:** Nejlepší nápad celé série: stopy se nespawnují podle povrchu, na kterém stojíš, ale podle **předchozího** povrchu [(3:10)](https://www.youtube.com/watch?v=buQ6JvwvHuw&t=190s) — projdeš blátem a pár vteřin roznášíš blátivé otisky po dlažbě. Technicky: decal + **dynamic material instance** s parametry pro sílu, barvu, zrcadlení nohy a fade-out.

### Rozpad myšlenky

**Sledování povrchu:** funkce `set surface` nejdřív uloží `previous ← current`, teprve pak nový current [(1:36)](https://www.youtube.com/watch?v=buQ6JvwvHuw&t=96s). Když *opouštíš* značkující povrch (sníh, bláto, voda, krev), zapne se `footprints active`, uloží se start time a **strength** začne na 1 [(4:42)](https://www.youtube.com/watch?v=buQ6JvwvHuw&t=282s). Timer (0,05 s) sílu rozpouští: `1 − (uplynulý čas / duration)`, clamp 0–1 [(7:13)](https://www.youtube.com/watch?v=buQ6JvwvHuw&t=433s) — každý další otisk je slabší, po pár vteřinách stopy zmizí a timer se uklidí [(7:57)](https://www.youtube.com/watch?v=buQ6JvwvHuw&t=477s).

**Spawn decalu** (v okamžiku došlapu z footstep systému): `Spawn Decal at Location`, pozice = impact point + normála × 3 (offset proti z-fightingu) [(13:24)](https://www.youtube.com/watch?v=buQ6JvwvHuw&t=804s); rotace = **forward vektor promítnutý na rovinu povrchu** (`Project Vector onto Plane` s impact normálou) → `Make Rot from XZ` + yaw korekce per noha (−80/−110 pro manekýna) [(14:11)](https://www.youtube.com/watch?v=buQ6JvwvHuw&t=851s) — stopa leží na povrchu a míří ve směru chůze i na svahu.

**Dynamic material instance** [(17:16)](https://www.youtube.com/watch?v=buQ6JvwvHuw&t=1036s): na spawnutém decalu se nastaví parametry — `foot mirror` (0/1 podle nohy; v materiálu lerp U souřadnice s 1−U [(25:55)](https://www.youtube.com/watch?v=buQ6JvwvHuw&t=1555s) — jedna textura pro obě nohy), `strength`, `spawn time`, `lifespan` (8 s), `fade out`, barva a **textura vybraná podle síly**: nad 0,7 plné otisky, pod ním lehčí částečné (random z polí heavy/light) [(20:24)](https://www.youtube.com/watch?v=buQ6JvwvHuw&t=1224s). Materiál je **deferred decal, translucent** [(23:31)](https://www.youtube.com/watch?v=buQ6JvwvHuw&t=1411s); opacity řídí řetěz `(Time − spawn time)` vs. `(lifespan − fade out)` → saturate → 1−x → × starting opacity × strength [(28:16)](https://www.youtube.com/watch?v=buQ6JvwvHuw&t=1696s) — decal se stihne plně vytratit, než se po lifespanu zničí. Starting opacity per povrch (voda 0,5 = průsvitné mokré šlápoty) [(30:35)](https://www.youtube.com/watch?v=buQ6JvwvHuw&t=1835s).

> **Pozn.:** Otisky *do* sněhu (deformace, tání pod nohama) autor odkládá na render targets v dalším díle [(32:10)](https://www.youtube.com/watch?v=buQ6JvwvHuw&t=1930s) — ten v playlistu zatím není. Kdo chce hotové řešení hned: video REFORCH (bez titulků, popisujeme z popisu) ukazuje bezplatný plugin **Interactive World** (LingFeng) se sněžnými stopami, otisky v blátě, vlnami na vodě a ohýbáním trávy — pro prototyp rychlejší než stavět vlastní render-target systém. Pro stealth: stopy nejsou jen kosmetika, jsou *mechanika* — trail, který po tobě zůstává, může číst i nepřítel.

**Souvislosti:** [Rejstřík: decal](../rejstrik.md#decal) · [Rejstřík: dynamic material instance](../rejstrik.md#dynamic-material-instance) · [AI vnímání](ai-vnimani.md)

---

## Niagara Data Channel: částice kroků bez stovky systémů

**Zdroj:** [Complete Unreal Footsteps System Using Niagara Data Channel!](https://www.youtube.com/watch?v=sGJ8cqe94ps) · [Grid & Node](https://www.youtube.com/channel/UCtkNl5rg-xwQjOin2h9dC1Q) · ~10 min, tutoriál (5.7)

**Shrnutí:** Prach nebo šplouchnutí u každého kroku znamená v naivní verzi **nový Niagara systém per krok** — drahé. **Niagara Data Channel (NDC)** to obrací: kroky jen zapisují data (pozice, normála) do kanálu a **jediný** běžící systém z nich spawnuje particly [(1:48)](https://www.youtube.com/watch?v=sGJ8cqe94ps&t=108s). K tomu čistý datový design: mapa physical material → {zvuk, particle systém} v data assetu.

### Rozpad myšlenky

**NDC setup:** NDC asset s channel variables `position` a `normal`; typ „gameplay boost" (novinka 5.7) navíc dovoluje **přepsat spawnovaný Niagara systém přímo při zápisu** [(1:48)](https://www.youtube.com/watch?v=sGJ8cqe94ps&t=108s) — jeden kanál obslouží prach, sníh i šplouchance. V particle systému: loop infinite, `Complete if Unused` (uklízí nepoužívané), v emitteru `Spawn from Data Channel` — vygeneruje moduly, které si z kanálu přečtou pozici a normálu per particle [(2:40)](https://www.youtube.com/watch?v=sGJ8cqe94ps&t=160s); NDC referenci ulož jako system value, ať se nastavuje jednou [(2:40)](https://www.youtube.com/watch?v=sGJ8cqe94ps&t=160s).

**Datový slovník efektů** [(5:49)](https://www.youtube.com/watch?v=sGJ8cqe94ps&t=349s): struct {Sound Cue, Niagara System} + **data asset s mapou `physical material → struct`** — přidání povrchu = nový řádek mapy, žádný kód. Notify pak: line trace z kosti (±Z offsety) [(3:48)](https://www.youtube.com/watch?v=sGJ8cqe94ps&t=228s) → phys material z hitu → `Find` v mapě (validated get na data asset) [(6:53)](https://www.youtube.com/watch?v=sGJ8cqe94ps&t=413s) → **Write Data Channel**: pozice, normála, override system to spawn [(7:26)](https://www.youtube.com/watch?v=sGJ8cqe94ps&t=446s) + zvuk. Nepokryté povrchy spadnou na **Default** surface type [(9:00)](https://www.youtube.com/watch?v=sGJ8cqe94ps&t=540s).

> **Pozn.:** Vzor „mapa v data assetu místo switch uzlu" stojí za zapamatování i mimo kroky — je to [data-driven design](../rejstrik.md#data-driven-design) v praxi a škáluje líp než Switch on EPhysicalSurface z první myšlenky (62 povrchů = 62 pinů vs. 62 řádků mapy). Drobný tip z konce videa: pokud particle „simulation position" zlobí, použij uloženou NDC pozici z init modulu [(9:09)](https://www.youtube.com/watch?v=sGJ8cqe94ps&t=549s).

**Souvislosti:** [Rejstřík: Niagara Data Channel](../rejstrik.md#niagara-data-channel) · [Rejstřík: data asset](../rejstrik.md#data-asset) · [Principy architektury: data-driven](principy-architektury.md)
