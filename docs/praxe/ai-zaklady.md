# Základy nepřátelské AI

Nepřítel, který hlídkuje, všimne si tě, honí tě a zase to vzdá — to je základní smyčka, na které stojí stealth i akce. Kapitola ji staví čtyřikrát, pokaždé o úroveň výš: minimální nepřítel na jedné komponentě, dva vzory patroly, chase se ztrátou zájmu, a nakonec totéž „dospěle" přes AI Controller, Behavior Tree a Blackboard. Jak AI *vnímá*, rozebírá [samostatná kapitola](ai-vnimani.md); moderní alternativu k behavior tree pak [State Trees](state-trees.md).

---

## Minimální nepřítel: Pawn Sensing, AI MoveTo a nav mesh

**Zdroj:** [The Easiest Way to Make a Simple Enemy AI in Unreal Engine 5](https://www.youtube.com/watch?v=xm-7m5Fw1HU) · [Gorka Games](https://www.youtube.com/channel/UCv_n9oioNF6OpzR2dt6E4xg) · ~16 min ·
[How To Create A Basic AI Enemy That Follows You](https://www.youtube.com/watch?v=sVV32qivy1A) · [Pitchfork Academy](https://www.youtube.com/channel/UCXp4W8jzNe280dGy_IvKX4Q) · ~15 min

**Shrnutí:** Fungující nepřítel = tři ingredience: **Character blueprint** s Pawn Sensing komponentou (oči), **AI MoveTo** uzel (nohy) a **Nav Mesh Bounds Volume** v levelu (mapa, po které nohy umí chodit). Všechno ostatní — animace, útok, ragdoll — se přidává na tuhle kostru.

### Rozpad myšlenky

**Kostra:** nepřítel jako Character BP (kapsle + movement zadarmo); Pitchfork ho vyrábí kopií třetíosobní postavy — pak je nutné smazat camera boom a follow kameru [(1:36)](https://www.youtube.com/watch?v=sVV32qivy1A&t=96s). **Pawn Sensing** komponenta nabízí zrak i sluch; pro začátek stačí `Sight Radius` (~2500) a `Peripheral Vision Angle` (~70°) [(2:22)](https://www.youtube.com/watch?v=sVV32qivy1A&t=142s). Její event **On See Pawn** vystřelí, když AI uvidí pawna [(2:22)](https://www.youtube.com/watch?v=xm-7m5Fw1HU&t=142s) — odtud se volá **AI MoveTo**: pawn = self, target actor = hráč [(3:26)](https://www.youtube.com/watch?v=xm-7m5Fw1HU&t=206s). A bez **Nav Mesh Bounds Volume** přes level se nepohne nic — klávesa `P` zobrazí zeleně, kudy AI umí chodit [(5:00)](https://www.youtube.com/watch?v=xm-7m5Fw1HU&t=300s).

**Útok bez spamu:** `Acceptance Radius` na AI MoveTo (~70) určuje, kde se nepřítel zastaví [(11:16)](https://www.youtube.com/watch?v=xm-7m5Fw1HU&t=676s). Na `On Success` pak guard vzor: bool `can attack` → false → **Play Anim Montage** (v AnimBP musí být Default Slot) → `Delay` v délce montáže → `can attack` true [(12:02)](https://www.youtube.com/watch?v=xm-7m5Fw1HU&t=722s) — útoky se neseká přes sebe. Animace pohybu klasicky: [blend space](../rejstrik.md#blend-space) 0–600 podle rychlosti, v AnimBP `Try Get Pawn Owner` → velocity → vector length → speed [(8:58)](https://www.youtube.com/watch?v=xm-7m5Fw1HU&t=538s).

**Bonus — ragdoll po zásahu (Pitchfork):** kolizní příprava — mesh preset na `Query and Physics` a blokovat projektil, kapsle naopak projektil **ignoruje** (odrazy od neviditelné kapsle vypadají špatně; test: projektil má proletět mezi nohama) [(6:34)](https://www.youtube.com/watch?v=sVV32qivy1A&t=394s), [(8:12)](https://www.youtube.com/watch?v=sVV32qivy1A&t=492s). Zásah pozná `On Component Hit` na meshi + kontrola **actor tagu** „bullet" na projektilu [(9:19)](https://www.youtube.com/watch?v=sVV32qivy1A&t=559s); ragdoll = `Set Simulate Physics` + `Set Physics Blend Weight` 1 s guardem `is alive` [(10:54)](https://www.youtube.com/watch?v=sVV32qivy1A&t=654s). A detail, který se snadno zapomene: mrtvole vypnout kolizi kapsle, jinak neviditelně blokuje průchod [(13:10)](https://www.youtube.com/watch?v=sVV32qivy1A&t=790s).

> **Pozn.:** Oba autoři poctivě ukazují hlavní slabinu: stačí si stoupnout za záda a AI o tobě neví [(4:56)](https://www.youtube.com/watch?v=sVV32qivy1A&t=296s) — a jakmile tě jednou vidí, honí tě navždy. Obojí řeší vzory z dalších myšlenek (ztráta zájmu, paměť). Pro rychlý prototyp nepřítele je ale tahle kostra hotová za deset minut.

**Souvislosti:** [AI vnímání](ai-vnimani.md) · [Rejstřík: Pawn Sensing](../rejstrik.md#pawn-sensing) · [Rejstřík: nav mesh](../rejstrik.md#nav-mesh) · [Rejstřík: blend space](../rejstrik.md#blend-space)

---

## Patrola dvěma způsoby: náhodné body a waypointy

**Zdroj:** [Unreal Engine 5 AI Patrol and Chase Tutorial](https://www.youtube.com/watch?v=lbqZS-cgcQs) · [Pixel Helmet](https://www.youtube.com/channel/UCUV2d1W23rCb6e6eFqdeKcg) · ~13 min ·
[How to Make an AI Follow a Waypoint Path Patrol](https://www.youtube.com/watch?v=WqcDNlWEgsI) · [Gorka Games](https://www.youtube.com/channel/UCv_n9oioNF6OpzR2dt6E4xg) · ~11 min

**Shrnutí:** Dvě patroly pro dvě situace. **Náhodné bloumání** (tři uzly a smyčka) pro ambientní NPC, kterým je jedno kam jdou. **Waypointy** (actor s ikonou + pole referencí + index) pro stráže, jejichž trasu navrhuje level designér. Obojí stojí na stejném principu: `AI MoveTo` → `On Success` → vyber další cíl → zavolej se znovu.

### Rozpad myšlenky

**Náhodné bloumání (Pixel Helmet):** custom event → **Get Random Location in Navigable Radius** (origin = vlastní pozice, radius ~1000) → `AI MoveTo` self → na `On Success` zavolat tentýž event [(3:56)](https://www.youtube.com/watch?v=lbqZS-cgcQs&t=236s), [(5:30)](https://www.youtube.com/watch?v=lbqZS-cgcQs&t=330s). Smyčku nastartuje `BeginPlay` [(6:16)](https://www.youtube.com/watch?v=lbqZS-cgcQs&t=376s). K tomu dvě zkratky pro jednoduchá NPC: mesh z bezplatného packu a **animation asset** místo celého AnimBP [(3:10)](https://www.youtube.com/watch?v=lbqZS-cgcQs&t=190s). Za pozornost stojí `RecastNavMesh` v levelu: sekce Generation → **Agent Radius** říká, jak daleko od stěn se generují cesty (~50–70; demo s 500 hezky ukazuje efekt) [(1:37)](https://www.youtube.com/watch?v=lbqZS-cgcQs&t=97s) — lék na NPC zasekávající se o rohy.

**Waypointy (Gorka):** `BP_Waypoint` = prázdný actor s **Billboard** komponentou (3D ikona, ať jde v editoru vidět a chytit) [(3:06)](https://www.youtube.com/watch?v=WqcDNlWEgsI&t=186s). Na AI **pole** referencí `waypoints` (object reference, instance editable) — v details umístěné instance naklikáš v pořadí trasy [(3:55)](https://www.youtube.com/watch?v=WqcDNlWEgsI&t=235s). Pohyb: `waypoints[current]` → `AI MoveTo` → success → `current + 1` → znovu [(4:41)](https://www.youtube.com/watch?v=WqcDNlWEgsI&t=281s); přeteční kontrola `current >= length → 0` restartuje okruh [(7:00)](https://www.youtube.com/watch?v=WqcDNlWEgsI&t=420s) — autor předvádí i klasický off-by-one (`>` místo `>=`), na kterém se smyčka zadrhne. `Delay` ~1 s před dalším bodem dodá přirozenou pauzu [(7:46)](https://www.youtube.com/watch?v=WqcDNlWEgsI&t=466s); `Orient Rotation to Movement` (+ vypnout controller yaw) hladké otáčky [(8:34)](https://www.youtube.com/watch?v=WqcDNlWEgsI&t=514s).

> **Pozn.:** Kdy co: náhodné bloumání je zadarmo a stačí davu; waypointy dávají kontrolu nad trasou, ale každá stráž potřebuje ruční setup. Třetí cesta — **spline** jako patrol path — je v [kapitole o State Trees](state-trees.md) a pro delší trasy je nejpohodlnější (tažení bodů po zemi místo klikání actorů). Pro stealth hru s rutinami vesničanů je tohle klíčová volba: čitelná, predikovatelná trasa = hratelný stealth.

**Souvislosti:** [State Trees: patrola po spline](state-trees.md) · [Rejstřík: nav mesh](../rejstrik.md#nav-mesh) · [Rejstřík: spline](../rejstrik.md#spline)

---

## Chase a ztráta zájmu: Do Once a Retriggerable Delay

**Zdroj:** [Unreal Engine 5 AI Patrol and Chase Tutorial](https://www.youtube.com/watch?v=lbqZS-cgcQs) · [Pixel Helmet](https://www.youtube.com/channel/UCUV2d1W23rCb6e6eFqdeKcg) · chase část

**Shrnutí:** Přechod patrola → chase je snadný; návrat je řemeslo. Dva uzly to řeší celé: **Do Once** brání tomu, aby se přechod do chase spouštěl znovu každý sensing tick, a **Retriggerable Delay** funguje jako „ztráta zájmu" — dokud tě AI vidí, odpočet se restartuje; jakmile zmizíš, doběhne a vrátí ji k patrole.

### Rozpad myšlenky

**Přechod do chase:** `On See Pawn` → sequence: přepnout animaci na sprint, `Max Walk Speed` na 600 a `AI MoveTo` s **target actorem** = spatřený pawn (cíl se sleduje průběžně, žádné přepočítávání destinace) [(7:49)](https://www.youtube.com/watch?v=lbqZS-cgcQs&t=469s).

**Past sensing intervalu:** Pawn Sensing vyhodnocuje každých 0,5 s a `On See Pawn` pálí **při každém** ticku, kdy tě vidí — animace se restartovala dvakrát za sekundu a postava „koktala" [(10:09)](https://www.youtube.com/watch?v=lbqZS-cgcQs&t=609s). Oprava: přechodovou logiku obalit **Do Once**; resetuje se custom eventem těsně před návratem k patrole, takže příští spatření zase projde [(10:56)](https://www.youtube.com/watch?v=lbqZS-cgcQs&t=656s). Interval jde snížit (0,1 s = plynulejší reakce), ale je to 10 vyhodnocení za sekundu — cena roste [(10:56)](https://www.youtube.com/watch?v=lbqZS-cgcQs&t=656s).

**Ztráta zájmu:** druhá větev sequence → **Retriggerable Delay** ~2 s → vrátit animaci a rychlost → zavolat patrolu [(9:22)](https://www.youtube.com/watch?v=lbqZS-cgcQs&t=562s). Mechanismus: dokud AI hráče vidí, event se opakuje a retriggerable delay se pokaždé restartuje od nuly — doběhne až po dvou sekundách *bez* spatření. Proč to funguje a jaké minimum délka potřebuje, rozebírá [detailně kapitola o vnímání](ai-vnimani.md#pawn-sensing-v-praxi-kuzel-zdi-a-presny-timing-ztraty).

> **Pozn.:** Tahle dvojice uzlů (Do Once + Retriggerable Delay) je miniaturní stavová logika bez state machine — pro jednoho nepřítele elegantní, pro tři druhy chování už nepřehledná. Přesně v tom bodě se vyplatí přejít na Behavior Tree (další myšlenka) nebo [State Tree](state-trees.md).

**Souvislosti:** [AI vnímání](ai-vnimani.md) · [Rejstřík: Retriggerable Delay](../rejstrik.md#retriggerable-delay) · [Rejstřík: Pawn Sensing](../rejstrik.md#pawn-sensing)

---

## Vyšší liga: AI Controller, Behavior Tree a Blackboard

**Zdroj:** [AI: Easy chasing player setup - Tutorial Unreal Engine 5](https://www.youtube.com/watch?v=EeN65RxmCak) · [LeafBranchGames](https://www.youtube.com/channel/UCPqAMQsTxwdQfC4_GsJrwkQ) · ~27 min, tutoriál s důrazem na architekturu

**Shrnutí:** Stejné chování (patrola + chase + zapomínání), ale rozložené do rolí, jak to dělá engine: **AI Controller** posedne postavu a spustí **Behavior Tree**, strom čte a zapisuje sdílenou tabuli (**Blackboard**), vnímání dodává **AI Perception**. Odměna za režii navíc: chování se skládá z vyměnitelných dílků a nová logika = nový uzel, ne přepis špagety.

### Rozpad myšlenky

**Struktura** [(0:53)](https://www.youtube.com/watch?v=EeN65RxmCak&t=53s): BP AI Controller (postava ho má v `AI Controller Class`) → `BeginPlay` → **Run Behavior Tree** [(2:25)](https://www.youtube.com/watch?v=EeN65RxmCak&t=145s). Patrola ve stromu: sequence → custom task „najdi náhodné místo" → **Move To** (čte Blackboard vektor) → **Wait** 2 s [(3:59)](https://www.youtube.com/watch?v=EeN65RxmCak&t=239s).

**Vlastní BT task** [(4:46)](https://www.youtube.com/watch?v=EeN65RxmCak&t=286s): override `Receive Execute AI` → `Get Random Point in Navigable Radius` → **Set Blackboard Value as Vector** → `Finish Execute` (úspěch/neúspěch). Klíč se nevybírá natvrdo — proměnná typu **Blackboard Key Selector** (exposed) se nastaví v details tasku ve stromu [(5:34)](https://www.youtube.com/watch?v=EeN65RxmCak&t=334s), takže task je znovupoužitelný pro libovolný klíč.

**Vnímání s pamětí:** AI Perception se Sight configem (zaškrtnout detekci enemies/neutrals/friendlies!) [(11:00)](https://www.youtube.com/watch?v=EeN65RxmCak&t=660s); `On Target Perception Updated` vede do **makra**, které stimul klasifikuje do tří větví: nový cíl / ztracený cíl / ignoruj [(12:16)](https://www.youtube.com/watch?v=EeN65RxmCak&t=736s). Filtr cílů přes **actor tag** na hráči (žádné casty na konkrétní třídu) [(13:51)](https://www.youtube.com/watch?v=EeN65RxmCak&t=831s); rozhodnutí dává `Break AIStimulus → Successfully Sensed` [(14:37)](https://www.youtube.com/watch?v=EeN65RxmCak&t=877s). **Paměť**: při ztrátě cíle se spustí timer (memory duration) a teprve jeho doběhnutí vynuluje Blackboard [(22:25)](https://www.youtube.com/watch?v=EeN65RxmCak&t=1345s); při znovuspatření se timer musí **zrušit** (`Clear and Invalidate`), jinak AI „zapomene", zatímco se dívá [(24:16)](https://www.youtube.com/watch?v=EeN65RxmCak&t=1456s).

**Chase větev stromu:** Blackboard klíč `follow target` typu **Object → Actor** — Move To na actora pak cíl plynule sleduje bez přepočítávání [(16:58)](https://www.youtube.com/watch?v=EeN65RxmCak&t=1018s). Selector: chase sequence s **Blackboard decoratorem** (`follow target Is Set`, observer aborts **Both**) nad patrolou jako fallbackem [(20:06)](https://www.youtube.com/watch?v=EeN65RxmCak&t=1206s) — jakmile se klíč změní, strom okamžitě přehodnotí, kterou větví běžet. Vynulování klíče = decorator přeruší chase = patrola sama naskočí [(25:02)](https://www.youtube.com/watch?v=EeN65RxmCak&t=1502s).

**Detail, co spraví klouzání:** manekýn po nav mesh „bruslil" — Character Movement → Nav Movement → **Use Acceleration for Paths** [(9:28)](https://www.youtube.com/watch?v=EeN65RxmCak&t=568s); pohyb po cestách pak zrychluje přirozeně místo okamžité rychlosti.

> **Pozn.:** Nejcennější na videu je disciplína: makro třídí *co se stalo*, funkce zapouzdřují *co s tím*, strom rozhoduje *kdy co běží* — tři vrstvy, které jdou měnit nezávisle [(26:35)](https://www.youtube.com/watch?v=EeN65RxmCak&t=1595s). Stejný přístup jako [separace zodpovědností](principy-architektury.md) z Blueprint batche. Epic dnes pro nové projekty tlačí [State Trees](state-trees.md) — koncepty (tasky, sdílená data, přerušitelné větve) se ale přenášejí 1:1, takže tahle investice se neztratí.

**Souvislosti:** [State Trees](state-trees.md) · [Principy architektury](principy-architektury.md) · [Rejstřík: AI Controller](../rejstrik.md#ai-controller) · [Rejstřík: Behavior Tree](../rejstrik.md#behavior-tree) · [Rejstřík: Blackboard](../rejstrik.md#blackboard) · [Rejstřík: AI Perception](../rejstrik.md#ai-perception)
