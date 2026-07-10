# Interakce s předměty a úkryty

Dvě interakce, které definují stealth adventuru: **vzít a hodit předmět** (distrakce, puzzle) a **schovat se** (skříň, lokr). Oba systémy tu staví stejný autor a sdílejí rukopis: markery místo hardcodovaných pozic, lerp s timerem místo teleportu a montage notify jako synchronizační bod mezi animací a logikou. Základ interakcí (overlap + interface) pokrývá [Interakce bez Event Ticku](interakce-bez-event-ticku.md).

---

## Házení předmětů s predikcí trajektorie

**Zdroj:** [Throwing Objects System And Projectile Path Trajectory | Unreal Engine 5](https://www.youtube.com/watch?v=B4W9lKbGeIc) · [Vercion Games](https://www.youtube.com/channel/UCLJWGl3ubdibb5h2YjsNe_g) · ~12 min, tutoriál ·
[How To Create Pickup And Drop System In Unreal Engine 5](https://www.youtube.com/watch?v=Hd0od7sQdds) · [Overlook Games](https://www.youtube.com/channel/UC4-Vs26mzBnHhgDbmaRAIUg) · ~17 min (bez přepisu)

**Shrnutí:** Míření = držená klávesa s **aim montáží na play rate 0** (nekonečné držení pózy), hod = throw montáž s **montage notify** v okamžiku vypuštění: mesh z ruky zmizí, spawne se fyzikální projektil s impulsem ve směru kamery. Oblouk dráhy kreslí **Predict Projectile Path** + spline mesh — hráč vidí, kam dopadne, dřív než pustí tlačítko.

### Rozpad myšlenky

**Držení a vrstvení:** static mesh komponenta `throwable` s parent socketem ruky [(0:47)](https://www.youtube.com/watch?v=B4W9lKbGeIc&t=47s). Stisk E → `Set Static Mesh` + aim montáž s **play rate 0** [(1:34)](https://www.youtube.com/watch?v=B4W9lKbGeIc&t=94s) — elegantní trik: jedna smyčková animace poslouží jako held pose. Puštění → throw montáž (rate 1) [(2:21)](https://www.youtube.com/watch?v=B4W9lKbGeIc&t=141s). Celotělová montáž při běhu zamrazí nohy — oprava je klasika z [combat vrstvení](mm-systemy.md#combat-nad-mm-horni-telo-v-montazi-spodni-v-matchingu): cache pose ze state machine + `Layered Blend Per Bone` od spine_01, blend pose = Default Slot [(3:08)](https://www.youtube.com/watch?v=B4W9lKbGeIc&t=188s).

**Vypuštění:** montage notify „throw" na framu, kde ruka pouští [(3:54)](https://www.youtube.com/watch?v=B4W9lKbGeIc&t=234s) → `Set Static Mesh None` → `Spawn Actor` (BP s meshem, `Simulate Physics` a gumovým physical materialem) na world location ruky [(4:41)](https://www.youtube.com/watch?v=B4W9lKbGeIc&t=281s) → **`Add Impulse`** = forward kamery × 1000 [(5:28)](https://www.youtube.com/watch?v=B4W9lKbGeIc&t=328s) + `Set Actor Rotation` podle control rotation. Přirozenější oblouk: Z složka forwardu → `Map Range Clamped` 0–1 → 3–10 × 150 do Z impulsu [(6:15)](https://www.youtube.com/watch?v=B4W9lKbGeIc&t=375s) — hod míří výš, aniž musíš zaklánět kameru.

**Predikce dráhy** [(7:01)](https://www.youtube.com/watch?v=B4W9lKbGeIc&t=421s): při míření timer (0,1 s, loop) volá **`Predict Projectile Path (Advanced)`** — start = pozice ruky, launch velocity = *tentýž výpočet* jako skutečný impulse (jinak predikce lže), trace collision zapnout, ignorovat sebe, sim frequency ~13. Vizualizace [(8:33)](https://www.youtube.com/watch?v=B4W9lKbGeIc&t=513s): body dráhy → `Add Spline Point` (world) → for-loop přes body → **`Add Spline Mesh Component`** (tenký průsvitný válec) a `Set Start and End` z `Get Location and Tangent at Spline Point` bodů i a i+1 [(10:07)](https://www.youtube.com/watch?v=B4W9lKbGeIc&t=607s). Úklid: event `clear spline points` (destroy komponent + clear + clear timeru) před každým překreslením i po hodu [(10:54)](https://www.youtube.com/watch?v=B4W9lKbGeIc&t=654s).

> **Pozn.:** Klíčové pravidlo celého systému: **predikce a hod musí sdílet výpočet rychlosti** — jakmile se rozjedou (jiný násobek, jiný oblouk), čára ukazuje jinam, než míč letí, a hráč to pozná okamžitě. Video Overlook Games (pickup/drop, bez titulků a bez použitelného popisu) nechávám jen jako odkaz — sběr předmětu je beztak podmnožina: overlap/trace → attach na socket, drop = detach + physics. Pro stealth je házení distrakční mechanika číslo jedna: kombinuje se přímo s [Report Noise Eventem](state-trees.md#jedna-percepce-tri-smysly-a-report-eventy) — dopad předmětu ohlásí zvuk AI.

**Souvislosti:** [Systémy nad MM: combat vrstvení](mm-systemy.md#combat-nad-mm-horni-telo-v-montazi-spodni-v-matchingu) · [State Trees: Report eventy](state-trees.md#jedna-percepce-tri-smysly-a-report-eventy) · [Rejstřík: spline](../rejstrik.md#spline) · [Rejstřík: anim notify](../rejstrik.md#anim-notify) · [Rejstřík: physical material](../rejstrik.md#physical-material)

---

## Úkryt ve skříni: markery, lerpy a synchronizace s animací

**Zdroj:** [Hide Inside Locker Almirah | Unreal Engine 5](https://www.youtube.com/watch?v=nLjUs8_5QBI) · [Vercion Games](https://www.youtube.com/channel/UCLJWGl3ubdibb5h2YjsNe_g) · ~17 min, tutoriál

**Shrnutí:** Klasika hororů a stealth her: přijdeš ke skříni, E, postava otevře dveře, vleze dovnitř, dveře se zavřou — a stejně tak ven. Systém je choreografie tří pohybů (postava ke dveřím → dveře → postava dovnitř), kterou drží pohromadě **marker komponenty** (kde stát, kde se schovat), **lerp timery** a **montage notifies**.

### Rozpad myšlenky

**Skříň (actor BP):** tělo + dvoje dveře. Dveře z assetu se otáčejí kolem špatného bodu — oprava je **scene komponenta jako pivot** v místě pantu, dveře jako její child [(1:34)](https://www.youtube.com/watch?v=nLjUs8_5QBI&t=94s) (stejný trik jako válec u [kyvadlových seker](pasti-a-mechaniky.md#kyvadlove-sekery-pivot-ping-pong-a-per-instance-chovani)). K tomu tři neviditelné boxy: **interaction box** (zóna pro prompt widget [(2:20)](https://www.youtube.com/watch?v=nLjUs8_5QBI&t=140s)), **initial position** (kam se postava postaví, aby dosáhla na kliku) a **hide place** (kde stojí uvnitř) [(3:06)](https://www.youtube.com/watch?v=nLjUs8_5QBI&t=186s) — poslední dva čistě jako *markery pozic*, žádná logika. Level designér je posune podle skříně.

**Choreografie dovnitř:** E → `Get Overlapping Actors` (class filter skříň) → reference [(3:52)](https://www.youtube.com/watch?v=nLjUs8_5QBI&t=232s). Přesun k initial position: timer 0,1 s + `timer count` jako **alpha lerpu** `Set Actor Location` [(5:24)](https://www.youtube.com/watch?v=nLjUs8_5QBI&t=324s) — X/Y z markeru, **Z z postavy** (jinak se propadá) [(7:45)](https://www.youtube.com/watch?v=nLjUs8_5QBI&t=465s); rotace `RInterp To` k natočení skříně [(6:11)](https://www.youtube.com/watch?v=nLjUs8_5QBI&t=371s). Pak get-in montáž a dveře: event `open door (bool)` → timer → `RInterp` relativní rotace pivotů, cílový úhel `select(open: 90 : 0)`, druhý pivot × −1 [(9:18)](https://www.youtube.com/watch?v=nLjUs8_5QBI&t=558s); po 3 s clear + snap na finální hodnoty [(10:05)](https://www.youtube.com/watch?v=nLjUs8_5QBI&t=605s). Vstup dovnitř spouští **montage notify „door open"** (~frame 35) → lerp meshe na hide place [(13:10)](https://www.youtube.com/watch?v=nLjUs8_5QBI&t=790s).

**Dvě pasti s montážemi:** get-in montáž potřebuje **`Enable Auto Blend Out` vypnout**, ať postava zůstane v koncové póze [(7:45)](https://www.youtube.com/watch?v=nLjUs8_5QBI&t=465s) — jenže tím přestane chodit `On Completed`. Workaround: **druhý notify na úplném konci animace** („animation completed") a větvit podle jména notify [(13:57)](https://www.youtube.com/watch?v=nLjUs8_5QBI&t=837s) — po něm zavřít dveře a vrátit UI. A stav `hidden` bool musí **gateovat movement input** (+ disable input během přechodů proti spamu) [(14:44)](https://www.youtube.com/watch?v=nLjUs8_5QBI&t=884s), jinak se postava hýbe uvnitř skříně.

**Ven:** obrácená sekvence (otevřít → out montáž → lerp ven s `in = false` → zavřít, `hidden = false`, UI, input) [(15:31)](https://www.youtube.com/watch?v=nLjUs8_5QBI&t=931s) — plus oprava otočení meshe po výstupu (Z = actor rotation − 90), protože dovnitř postava couvá zády [(16:17)](https://www.youtube.com/watch?v=nLjUs8_5QBI&t=977s).

> **Pozn.:** Pro naši hru je tohle přímý stavební díl — a napojení na AI je zadarmo: `hidden` bool může rovnou vypínat [AI Perception Stimuli Source](ai-vnimani.md#tri-nastroje-detekce-pawn-sensing-ai-perception-trigger) na postavě, takže schovaný hráč pro stráže přestane existovat. Slabina tutoriálu: ručně laděné delaye (0,85 s na synchronizaci se zvukem dveří) — robustnější je věšet všechno na notifies v montážích, jak sám ukazuje u „door open". GASP verze téhož by šla přes [smart object](gasp.md#npc-pres-state-tree-a-smart-objects-mozek-na-serveru-motor-v-komponente) se vstupní montáží vybíranou podle pózy.

**Souvislosti:** [AI vnímání](ai-vnimani.md) · [GASP: smart objects](gasp.md#npc-pres-state-tree-a-smart-objects-mozek-na-serveru-motor-v-komponente) · [Interakce bez Event Ticku](interakce-bez-event-ticku.md) · [Rejstřík: anim montage](../rejstrik.md#anim-montage) · [Rejstřík: anim notify](../rejstrik.md#anim-notify)
