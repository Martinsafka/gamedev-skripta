# Ragdoll: od přepínače po seamless návrat

Ragdoll je na první pohled checkbox — a na druhý celá disciplína: aby tělo padalo věrohodně, potřebuje vyladěný **physics asset**; aby se dalo ovládat pádem, **motory řízené rychlostí**; a aby z něj postava vstala bez střihu, **pose snapshot** a detekci polohy. Kapitola skládá pět zdrojů od minutového základu po kompletní systém nad GASP. Ragdoll po zásahu projektilem už ukázaly [základy AI](ai-zaklady.md#minimalni-nepritel-pawn-sensing-ai-moveto-a-nav-mesh); tady jde o plnou smyčku tam a zpět.

---

## Ragdoll za minutu: preset, simulace, kamera

**Zdroj:** [Unreal Engine 5 Tutorial - Ragdoll](https://www.youtube.com/watch?v=ZHgnfFj7pco) · [The Real Unreal](https://www.youtube.com/channel/UC0is_44ph-5eC-K1uImsoRA) · ~4 min, tutoriál

**Shrnutí:** Minimální ragdoll = tři uzly: mesh na **collision preset „Ragdoll"**, `Set Simulate Physics` true a `Disable Movement` na character movementu [(0:54)](https://www.youtube.com/watch?v=ZHgnfFj7pco&t=54s). Předpoklad je existující [physics asset](../rejstrik.md#physics-asset) — UE manekýn má `PA_Mannequin` z krabice [(0:08)](https://www.youtube.com/watch?v=ZHgnfFj7pco&t=8s).

### Rozpad myšlenky

Bez presetu „Ragdoll" simulace nefunguje správně — nastavuje objektový typ a odpovědi kanálů tak, jak je fyzikální tělo čeká. Čtvrtý krok, na který se zapomíná: **kamera**. Camera boom zůstal na kapsli, která po zapnutí simulace stojí na místě — `Attach Component to Component` ho přepne na mesh se socketem `pelvis`, a `Do Collision Test` off zabrání kolizím s vlastním tělem [(2:22)](https://www.youtube.com/watch?v=ZHgnfFj7pco&t=142s), [(2:42)](https://www.youtube.com/watch?v=ZHgnfFj7pco&t=162s).

> **Pozn.:** Tohle je „ragdoll na smrt" — jednosměrka. Všechno ostatní v téhle kapitole řeší, jak z něj udělat obousměrný stav. Ale pro nepřátele, kteří vstávat nemusí, je tahle minutová verze plus kolizní úpravy z [AI kapitoly](ai-zaklady.md#minimalni-nepritel-pawn-sensing-ai-moveto-a-nav-mesh) (kapsle No Collision po smrti!) všechno, co potřebuješ.

**Souvislosti:** [Základy AI: ragdoll po zásahu](ai-zaklady.md#minimalni-nepritel-pawn-sensing-ai-moveto-a-nav-mesh) · [Rejstřík: physics asset](../rejstrik.md#physics-asset) · [Rejstřík: collision preset](../rejstrik.md#collision-preset)

---

## Physics asset: těla, constrainty a triky z ALS

**Zdroj:** [UE5 Ragdoll Deep Dive Guide](https://www.youtube.com/watch?v=ZpcOYg1Qfm4) · [frinky](https://www.youtube.com/channel/UCepxYGyRNUXgqve42r60q8g) · část 1 ·
[UE5 Ragdoll Physics Tutorial (Complete Guide)](https://www.youtube.com/watch?v=R5o2CjPb3Tk) · [LocoDev](https://www.youtube.com/channel/UCr8NttLeGyLd6m4qVS2Zb8g) · úvodní část

**Shrnutí:** Physics asset = **těla** (kolizní primitiva per kost — koule, kapsle, kvádry) + **constrainty** (kloubové limity: swing 1/2 a twist) [(0:51)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=51s), [(3:12)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=192s). Defaultní assety manekýnů jsou pro ragdoll **nedoladěné** — končetiny se kroutí nevěrohodně [(8:21)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=501s). Frinky dodává sadu úprav vykoukanou z ALS, které z „hadru" udělají tělo.

### Rozpad myšlenky

**Jak si constrainty osahat:** vybrat constraint → `Simulate Selected` a tahat myší [(4:01)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=241s) — hned vidíš, co který limit (Locked/Limited/Free na swing/twist) dělá. `Angular Drive Mode: Twist and Swing` znamená, že se kloub po puštění **vrací do přirozené pózy** [(5:34)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=334s) — základ „aktivního" chování.

**ALS recept (frinky):**

1. Select All Constraints → drive mode **Twist and Swing**, zaškrtnout všechny čtyři motory, `Target Velocity Strength` = 1 [(3:38)](https://www.youtube.com/watch?v=ZpcOYg1Qfm4&t=218s).
2. **Výjimka pelvis**: motory vypnout, drive mode zpět na SLERP — pánev nesmí tahat tělo za animací, jinak se ragdoll „vzpírá" [(4:25)](https://www.youtube.com/watch?v=ZpcOYg1Qfm4&t=265s). U chodidel vypnout target velocity.
3. Všechna těla: **Angular Damping 15** (hodnota z ALS) [(5:11)](https://www.youtube.com/watch?v=ZpcOYg1Qfm4&t=311s).
4. **Kinematic root body**: root kost defaultně tělo nemá — a mesh se při simulaci od parenta *odpojí*. Root → Add Shape (malá koule) → Physics Type **Kinematic** [(5:59)](https://www.youtube.com/watch?v=ZpcOYg1Qfm4&t=359s). DK 3D variantu doplňuje o constraint root↔pelvis s linear limity Free a **vypnutou kolizní odpovědí** root těla — jinak se ragdoll hádá s terénem [(4:58)](https://www.youtube.com/watch?v=-mHfpyBn_UQ&t=298s), [(5:46)](https://www.youtube.com/watch?v=-mHfpyBn_UQ&t=346s).

**Kolize tělo × tělo:** defaultně končetiny prochází skrz sebe — vybrat dvojici tvarů → `Enable Collision` (typicky nohy, paže × trup) [(11:11)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=671s).

> **Pozn.:** Kinematic root má druhý, nenápadný účel (LocoDev): za ragdollu se **actor velocity nepočítá** — rychlost těla čteš z root/pelvis kosti (`Get Physics Linear Velocity`), a právě na ní stojí všechno ladění v další myšlence [(16:25)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=985s). LocoDev k videu přikládá dokument s kompletními hodnotami limitů pro UEFN manekýna [(10:25)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=625s) — rychlejší než ladit od nuly.

**Souvislosti:** [Rejstřík: physics asset](../rejstrik.md#physics-asset) · [Rejstřík: physics constraint](../rejstrik.md#physics-constraint) · [Rejstřík: ALS](../rejstrik.md#als)

---

## Active ragdoll: motory řízené rychlostí

**Zdroj:** [How to Make an Active Ragdoll (like Gang Beasts)](https://www.youtube.com/watch?v=l4nfL9RHcA4) · [Gorka Games](https://www.youtube.com/channel/UCv_n9oioNF6OpzR2dt6E4xg) · ~7 min ·
[UE5 Ragdoll Deep Dive Guide](https://www.youtube.com/watch?v=ZpcOYg1Qfm4) · [frinky](https://www.youtube.com/channel/UCepxYGyRNUXgqve42r60q8g) · část 2 ·
[UE5 Ragdoll Physics Tutorial (Complete Guide)](https://www.youtube.com/watch?v=R5o2CjPb3Tk) · [LocoDev](https://www.youtube.com/channel/UCr8NttLeGyLd6m4qVS2Zb8g) · blueprint část (nad GASP, 5.5)

**Shrnutí:** Active ragdoll = tělo simuluje fyziku, ale **motory kloubů ho táhnou k animaci** (Gang Beasts, Human Fall Flat). Dvě páky: **Physical Animation Component** (síla, s jakou se kosti drží animované pózy) a **angular drive motory** z physics assetu — a nejlepší trik batche: obě řídit **rychlostí těla**. Letící tělo je tuhé a drží tvar, ležící tělo je hadr.

### Rozpad myšlenky

**Základ (Gorka):** Physical Animation Component → BeginPlay `Set Skeletal Mesh Component` → `Apply Physical Animation Settings Below` od **pelvis** (první kost po rootu; jiné skelety „hips") [(2:22)](https://www.youtube.com/watch?v=l4nfL9RHcA4&t=142s) s `Make Physical Animation Data`: orientation strength ~1000, angular velocity ~100, position ~1000, velocity ~100 [(3:08)](https://www.youtube.com/watch?v=l4nfL9RHcA4&t=188s). K tomu `Set All Bodies Below Simulate Physics` a kolize: mesh preset **Pawn**, kapsle **ignoruje Pawn** [(4:44)](https://www.youtube.com/watch?v=l4nfL9RHcA4&t=284s).

**Checkbox, který šetří hodiny (frinky):** na meshi **`Update Joints from Animation`** — bez něj ragdoll **T-pózuje** [(15:17)](https://www.youtube.com/watch?v=ZpcOYg1Qfm4&t=917s). Vstup do ragdollu jinak klasika: kapsle bez kolize, movement None, mesh objektový typ Physics Body + query and physics, simulate below pelvis [(16:03)](https://www.youtube.com/watch?v=ZpcOYg1Qfm4&t=963s); frinky navíc přepíná **input mapping contexty** (default ↔ ragdoll s vlastními akcemi) [(14:30)](https://www.youtube.com/watch?v=ZpcOYg1Qfm4&t=870s) a drží stav v pure util funkci `Is Simulating Physics(pelvis)` [(10:40)](https://www.youtube.com/watch?v=ZpcOYg1Qfm4&t=640s).

**Rychlost → tuhost:** v update smyčce `Set All Motors Angular Drive Params` se **spring** mapuje z délky rychlosti pánve: frinky 0–500 → 500–5000 [(22:17)](https://www.youtube.com/watch?v=ZpcOYg1Qfm4&t=1337s), LocoDev 0–1000 → 1000–2800 [(21:26)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=1286s). Efekt: při letu tělo drží pózu (stabilizuje se po nárazu, líp se pak blenduje vstávání [(21:51)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=1311s)), po dopadu zplihne. LocoDev stejným mapováním řídí i **per-řetěz síly** (`Apply Settings Below` zvlášť pro spine_05, stehna, ruce) [(27:25)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=1645s) — simulace od kosti níž zasahuje jen její hierarchii [(25:07)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=1507s).

**Kapsle za tělem:** každý frame `Set Actor Location and Rotation` ← socket transform pelvis, +90 Z (kapsle nad zemí), z rotace **jen yaw** [(18:22)](https://www.youtube.com/watch?v=ZpcOYg1Qfm4&t=1102s); camera lag na boomu vyhladí zbytek [(19:11)](https://www.youtube.com/watch?v=ZpcOYg1Qfm4&t=1151s). LocoDev přidává vypnutí gravitace při pádu rychlejším než −4000 (proti nekonečné akceleraci a propadům podlahou) [(28:59)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=1739s).

> **Pozn.:** LocoDev staví nad [GASP](gasp.md) a narazil na tvrdou verzní past (5.5): kombinace Physical Animation komponenty a simulace **mrazí engine**, dokud se na BeginPlay GASP postavy neodpojí uzel `Add Tick Prerequisite Component` [(36:32)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=2192s) — přesně ten typ „proč mi to padá" zádrhelu, který stojí za zápis. Hodnoty všech mapování ber jako startovní: oba autoři přiznávají, že čísla vyladili iterováním na vlastních animacích.

**Souvislosti:** [GASP](gasp.md) · [Rejstřík: physical animation component](../rejstrik.md#physical-animation-component) · [Rejstřík: physics asset](../rejstrik.md#physics-asset)

---

## Vstávání: pose snapshot, front/back a auto-recovery

**Zdroj:** [Advanced Seamless Ragdoll mode enter/exit](https://www.youtube.com/watch?v=-mHfpyBn_UQ) · [DK 3D](https://www.youtube.com/channel/UC3fGhbgSpR2BSSeTls3R6Sg) · ~53 min ·
[UE5 Ragdoll Deep Dive Guide](https://www.youtube.com/watch?v=ZpcOYg1Qfm4) · [frinky](https://www.youtube.com/channel/UCepxYGyRNUXgqve42r60q8g) · část 3 ·
[UE5 Ragdoll Physics Tutorial (Complete Guide)](https://www.youtube.com/watch?v=R5o2CjPb3Tk) · [LocoDev](https://www.youtube.com/channel/UCr8NttLeGyLd6m4qVS2Zb8g) · stand-up část

**Shrnutí:** Návrat z ragdollu má tři problémy: **odkud blendovat** (tělo leží v póze, kterou žádná animace nezná), **kterou animaci hrát** (na zádech vs. na břiše) a **kdy vůbec vstávat**. Odpovědi: **pose snapshot** zmrazí poslední fyzikální pózu jako blendovací zdroj, **dot product pánve se světovou osou Z** rozhodne front/back, a looping timer čeká, až se tělo přestane hýbat.

### Rozpad myšlenky

**Pose snapshot** [(33:13)](https://www.youtube.com/watch?v=ZpcOYg1Qfm4&t=1993s): při ukončení ragdollu `Save Pose Snapshot("ragdoll")` na anim instanci; v AnimBP větev s uzlem **Pose Snapshot** téhož jména (blend time 0) — strom pak plynule blenduje *z* zmrzlé fyzikální pózy do vstávací montáže místo lupnutí. LocoDev totéž staví jako stav ve state machine s přechody podle `is ragdolling` (property access, žádný cast) a Hermite Cubic blendem [(40:16)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=2416s), [(50:24)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=3024s). DK 3D nabízí alternativu bez snapshotu: timeline 0,5 s žene `Set All Bodies Below Physics Blend Weight` 1→0 a teprve pak vypne simulaci [(22:46)](https://www.youtube.com/watch?v=-mHfpyBn_UQ&t=1366s).

**Na zádech, nebo na břiše?** DK 3D: right vector rotace pelvis socketu → **dot product s (0,0,1)** → kladný = na zádech → select montáže stand-back/stand-front [(36:40)](https://www.youtube.com/watch?v=-mHfpyBn_UQ&t=2200s). K tomu rotace kapsle při vstávání: yaw z pelvisu + select(na zádech: +180° : 0) — jinak postava vstane čelem vzad [(43:41)](https://www.youtube.com/watch?v=-mHfpyBn_UQ&t=2621s); frinky řeší totéž přes roll < 0 → yaw − 180 [(37:50)](https://www.youtube.com/watch?v=ZpcOYg1Qfm4&t=2270s).

**Montáže a pořadí operací:** blend in krátký (0–0,25 s — rychle „chytit" ragdoll pózu), blend out delší a měkký (0,3–1 s, cubic/sinusoidal) [(13:33)](https://www.youtube.com/watch?v=-mHfpyBn_UQ&t=813s), [(46:26)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=2786s). Dvě pasti: **simulate physics musí být false, než montáž spustíš** — jinak nehraje [(20:27)](https://www.youtube.com/watch?v=-mHfpyBn_UQ&t=1227s); a movement vracet až na konci — DK přes anim notify „standing" umístěný tam, kde póza ≈ idle [(17:43)](https://www.youtube.com/watch?v=-mHfpyBn_UQ&t=1063s), frinky timerem v délce montáže [(35:31)](https://www.youtube.com/watch?v=ZpcOYg1Qfm4&t=2131s).

**Kdy vstát — samo:** DK klávesou jen *vstupuje*; **looping** `Set Timer by Function Name` (0,5 s — checkbox looping, klasická past [(49:50)](https://www.youtube.com/watch?v=-mHfpyBn_UQ&t=2990s)) hlídá `Get Physics Linear Velocity(pelvis)` → `Vector Is Nearly Zero` (tolerance 5) → tělo se dokutálelo → clear timer → vstávej [(47:24)](https://www.youtube.com/watch?v=-mHfpyBn_UQ&t=2844s). Postava se tak skutálí ze schodů a vstane sama, správnou animací. LocoDev doplňuje výstup **ve vzduchu**: not-on-ground → movement Falling + `Set Velocity` = poslední ragdoll rychlost — hybnost se přenese a postava letí dál [(43:46)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=2626s). A pozor na kapsli u podlahy: line trace z pelvis dolů s fallbackem, když nic netrefí — jinak se postava teleportuje na nulové souřadnice [(32:37)](https://www.youtube.com/watch?v=-mHfpyBn_UQ&t=1957s).

> **Pozn.:** LocoDev na závěr staví pohyblivé platformy jako **test rig** (timeline lerp + overlap → ragdoll start) [(54:23)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=3263s) — dobrá praxe: fyzikální systém potřebuje hřiště, kde ho jde opakovaně mučit. Pro nás je celá tahle smyčka (zásah → ragdoll → dokutálení → vstání správným směrem) přesně to, co udělá z omráčení stráže *systém* místo cutscény.

**Souvislosti:** [Rejstřík: pose snapshot](../rejstrik.md#pose-snapshot) · [Rejstřík: anim notify](../rejstrik.md#anim-notify) · [Rejstřík: retriggerable delay](../rejstrik.md#retriggerable-delay) · [Pasti a arénové mechaniky: timeline](pasti-a-mechaniky.md#kostra-pasti-a-tri-variace-bodaky-rameno-rotor)
