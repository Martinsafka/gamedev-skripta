# MetaHuman v praxi: hratelná postava, pohled, oblečení a davy

MetaHuman už není jen „digitální dvojník pro cinematiku" — [markerless mocap](animace-nastroje.md#markerless-mocap-v-58-z-videa-na-animaci-bez-obleku) z něj udělal mocap prostředníka a tahle kapitola pokrývá zbytek herního života: jak z MetaHumana udělat **hratelnou postavu**, jak mu dát **pohled** (look-at bez klíčování), **fyzikální oblečení** přes Chaos Cloth, **davy** přes nový Crowd plugin a co znamená optimalizace obličeje třetí stranou.

---

## Hratelný MetaHuman: retarget jedním klikem a virtual bones

**Zdroj:** [Unreal Engine 5.7 - Turn Your Metahuman Into A Player Character](https://www.youtube.com/watch?v=cARn14Ec14w) · [Unreal - X - Tutorials](https://www.youtube.com/channel/UCjKg7gsHCEyXtJbZYx2Xu7A) · ~6 min, tutoriál

**Shrnutí:** Z MetaHumana třetíosobní postava za pár minut: zkopírovat komponenty (body → cloth) do duplikátu TPP characteru a **celý AnimBP retargetovat jedním krokem** — right-click na ABP → `Retarget Animations` → cílový mesh = MetaHuman body [(2:23)](https://www.youtube.com/watch?v=cARn14Ec14w&t=143s). Zbývají tři opravy: LOD, oblečení a foot IK.

### Rozpad myšlenky

**Sestavení:** duplikát TPP characteru, smazat manekýní mesh, z MetaHuman blueprintu zkopírovat komponenty od body po cloth, body jako child mesh komponenty s vynulovaným transformem [(0:50)](https://www.youtube.com/watch?v=cARn14Ec14w&t=50s). **LOD oprava:** groomy (vlasy) se rozbijí — zkopírovat i **LOD Sync komponentu** a nastavit `Number of LODs = 1`, `Force LOD = 0`; hlavní postava stejně vždycky poběží v plném detailu [(1:37)](https://www.youtube.com/watch?v=cARn14Ec14w&t=97s). **Oblečení neanimuje:** cloth meshi přiřadit `ABP_Clothing_PostProcess` [(3:38)](https://www.youtube.com/watch?v=cARn14Ec14w&t=218s).

**Foot IK přes virtual bones** [(4:37)](https://www.youtube.com/watch?v=cARn14Ec14w&t=277s): MetaHuman skeleton nemá IK kosti manekýna, takže retargetovaný foot IK control rig křičí chybami. Oprava bez editace skeletonu v DCC: na skeletonu **Add Virtual Bone** (root→root, root→foot_r, root→foot_l), zkopírovat manekýní foot IK control rig, v kopii `Refresh` hierarchie na MetaHuman mesh a červené uzly přepojit na virtual bones [(5:23)](https://www.youtube.com/watch?v=cARn14Ec14w&t=323s).

> **Pozn.:** `Retarget Animations` na celém AnimBP je novější workflow, který zkracuje starou cestu (IK rig + retargeter per animace) na jeden dialog — funguje, protože MetaHuman i manekýn sdílejí kompatibilní kosterní logiku. Virtual bones jsou obecný trik: kost, která existuje jen v enginu (žádný re-export z DCC), ideální pro IK cíle a sockety odvozené z jiných kostí.

**Souvislosti:** [Animační nástroje: mocap](animace-nastroje.md#markerless-mocap-v-58-z-videa-na-animaci-bez-obleku) · [Rejstřík: MetaHuman](../rejstrik.md#metahuman) · [Rejstřík: virtual bone](../rejstrik.md#virtual-bone) · [Rejstřík: groom](../rejstrik.md#groom)

---

## Look-at systém: pohled vrstvený přes jakoukoli animaci

**Zdroj:** [Unreal Engine 5.7 - Metahuman Cinematic Look At System](https://www.youtube.com/watch?v=UBSNmxXurkk) · [Unreal - X - Tutorials](https://www.youtube.com/channel/UCjKg7gsHCEyXtJbZYx2Xu7A) · ~9 min, tutoriál

**Shrnutí:** Klíčovat rotace hlavy ručně pro každý pohled je otrava — tenhle systém přidá **Look At uzel do post-process AnimBP**, který se vyhodnocuje *po* všem ostatním, takže pohled se navrství na libovolnou animaci [(1:36)](https://www.youtube.com/watch?v=UBSNmxXurkk&t=96s). V sequenceru pak stačí dvě čísla: head movement control a eye movement control (0–1).

### Rozpad myšlenky

**Kostra:** actor `BP_LookAtTarget` (klidně připnutý na cine kameru) [(0:49)](https://www.youtube.com/watch?v=UBSNmxXurkk&t=49s); na MetaHuman blueprintu float proměnné `head/eye movement control` — **Expose to Cinematics** + instance editable — a reference na target, nastavená v **construction scriptu** (`Get Actor of Class`), ať funguje v sequenceru bez play [(1:36)](https://www.youtube.com/watch?v=UBSNmxXurkk&t=96s).

**Hlava (body post-process ABP):** initialize → `Get Actor of Class` → reference na MetaHumana; update → přečíst control a `Get Actor Location` targetu [(2:22)](https://www.youtube.com/watch?v=UBSNmxXurkk&t=142s); v anim grafu **Look At uzel** těsně před output pose — bone `head`, look at location z pinu, alpha = control [(3:58)](https://www.youtube.com/watch?v=UBSNmxXurkk&t=238s). **Oči (face post-process ABP):** totéž pro kosti `facial_L_I` / `facial_R_I`, ale **look at axis Z místo Y** — oční kosti mají jinou orientaci [(6:32)](https://www.youtube.com/watch?v=UBSNmxXurkk&t=392s).

**Použití v sequenceru:** přidat control tracky přes plus na MetaHuman tracku; past — i bez animace musí existovat **aspoň prázdný control rig track**, jinak post-process nemá základní pózu k vyhodnocení [(4:45)](https://www.youtube.com/watch?v=UBSNmxXurkk&t=285s). Filmový recept: target na kameře, **oči 1,0 + hlava 0,5** — oči vždy do objektivu, hlava dotáčí napůl; působí přirozeně [(7:18)](https://www.youtube.com/watch?v=UBSNmxXurkk&t=438s).

> **Pozn.:** Post-process ABP je **sdílený všemi MetaHumany** — pro víc postav je nutné větvení podle `Get Owning Actor → Get Class` s referencí a controly per postava, a nulovat controly pro nespárované [(8:05)](https://www.youtube.com/watch?v=UBSNmxXurkk&t=485s). Pro naši hru se stejný vzor hodí i mimo cinematiku: NPC, které se otočí za procházejícím hráčem, je tenhle uzel + [AI perception](ai-vnimani.md) místo sequenceru.

**Souvislosti:** [Rejstřík: post-process AnimBP](../rejstrik.md#post-process-animbp) · [AI vnímání](ai-vnimani.md) · [Rejstřík: MetaHuman](../rejstrik.md#metahuman)

---

## Chaos Cloth: sukně, která se hýbe

**Zdroj:** [Unreal Engine 5.6 - Chaos Cloth for Metahuman](https://www.youtube.com/watch?v=RXq1X8q04Dk) · [Unreal - X - Tutorials](https://www.youtube.com/channel/UCjKg7gsHCEyXtJbZYx2Xu7A) · ~7 min, tutoriál

**Shrnutí:** Realtime fyzika oblečení přes **Cloth Asset** graf: import statického outfitu → přenos skin weights z těla → **namalovaná weight mapa** (co simulovat, co nechat na animaci) → config uzly → collider z physics assetu MetaHumana. Výsledná látka reaguje na pohyb i vítr.

### Rozpad myšlenky

**Graf cloth assetu** [(0:42)](https://www.youtube.com/watch?v=RXq1X8q04Dk&t=42s): `Static Mesh Import` (outfit; přepnout 2D → **3D simulation**) → `Transfer Skin Weights` (source = skeletal body mesh MetaHumana, render mesh transfer source = skeletal mesh) [(1:26)](https://www.youtube.com/watch?v=RXq1X8q04Dk&t=86s) → **weight mapa štětcem**: spodek sukně plná simulace, přechod vyhladit smooth nástrojem (k dispozici i lasso, gradient, fill); uzel pojmenovat přesně **MaxDistance** [(1:53)](https://www.youtube.com/watch?v=RXq1X8q04Dk&t=113s) → `Simulation Default Config` → `Simulation Max Distance Config` (napojit weight mapu) → **`Set Physics Asset`** — kolider látky = **kopie** physics assetu MetaHumana, ať jde ladit bez zásahu do originálu [(2:27)](https://www.youtube.com/watch?v=RXq1X8q04Dk&t=147s) → terminal. Do MetaHuman BP pak **Chaos Cloth komponenta** na body s přiřazeným assetem [(5:44)](https://www.youtube.com/watch?v=RXq1X8q04Dk&t=344s).

**Ladění = trojúhelník** [(4:08)](https://www.youtube.com/watch?v=RXq1X8q04Dk&t=248s): weight mapa × collider koule v physics assetu × config (stiffness, bending, density). Clipping se opravuje kombinací všech tří — po změně kolidérů je potřeba **reset cloth** pro obnovu náhledu [(4:56)](https://www.youtube.com/watch?v=RXq1X8q04Dk&t=296s). Kvalita vs. CPU: `Iteration Count` (kvalita při <60 fps) a `Subdivision Count` (kvalita kolizí) [(5:44)](https://www.youtube.com/watch?v=RXq1X8q04Dk&t=344s); `Simulation Aerodynamics Config` přidá vítr [(3:14)](https://www.youtube.com/watch?v=RXq1X8q04Dk&t=194s).

> **Pozn.:** Outfit autor šije v bezplatné alternativě Marvelous Designeru (odkazuje na svůj cloth tutoriál) — pro nás je podstatný ten UE konec: cloth asset graf je stejný nedestruktivní vzor jako [Mesh Terrain modifiery](mesh-terrain.md#modifier-stack-nedestruktivni-tvarovani) — uzly jdou kdykoli přeladit. Pro hru měř: plná simulace sukně na každém NPC je luxus; kombinace „hlavní postava simuluje, dav má oblečení pečené" je běžný kompromis (viz Crowd níže).

**Souvislosti:** [Rejstřík: Chaos Cloth](../rejstrik.md#chaos-cloth) · [Rejstřík: physics asset](../rejstrik.md#physics-asset) · [Mesh Terrain: modifier stack](mesh-terrain.md#modifier-stack-nedestruktivni-tvarovani)

---

## Crowd plugin: tisíc MetaHumanů přes Mass

**Zdroj:** [New Unreal Engine 5.8 Metahuman Crowd Plugin](https://www.youtube.com/watch?v=bJIPlvmoTVw) · [Smart Poly](https://www.youtube.com/channel/UCp1e34nrTQqVXkNU5ekH9CQ) · ~9 min, showcase sample projektu

**Shrnutí:** Nový experimentální **MetaHuman Crowd plugin** (5.8): davy od desítek po tisíce postav simulované přes **Mass Entity** — s plynulým přepínáním mezi levnými instancovanými meshi v dálce a plnohodnotnými MetaHuman actory u kamery [(0:01)](https://www.youtube.com/watch?v=bJIPlvmoTVw&t=1s). Sample projekt s 1000 postavami běží v editoru kolem 50–60 fps [(1:34)](https://www.youtube.com/watch?v=bJIPlvmoTVw&t=94s).

### Rozpad myšlenky

**Jak to škáluje:** HUD sample projektu ukazuje tři čísla — spawnuto / na obrazovce (culling) / **MetaHuman actors** (plné meshe). Poslední je nula, dokud kamera nepřijde blízko; pak se streamuje ~5 plných postav naráz [(2:20)](https://www.youtube.com/watch?v=bJIPlvmoTVw&t=140s). Navigace (náhodné cesty, předepsané trasy, vyhýbání) jede na **Mass Entity** systému známém z City Sample [(3:06)](https://www.youtube.com/watch?v=bJIPlvmoTVw&t=186s) — tady ale bez limitu pár stovek NPC. Postavy jsou Nanite [(4:40)](https://www.youtube.com/watch?v=bJIPlvmoTVw&t=280s).

**Modularita outfitů:** **crowd collection asset** drží presety hlav, vlasů, bot, kalhot… včetně editovatelných barev (barva švů na džínách, trika) — a jde do něj přidat vlastní oblečení; z presetů se dav náhodně skládá [(5:27)](https://www.youtube.com/watch?v=bJIPlvmoTVw&t=327s). Sample má i debug widget na klávese `O` (zpomalení času — detailní prohlídka postav) [(6:14)](https://www.youtube.com/watch?v=bJIPlvmoTVw&t=374s).

**Jak to získat** [(7:46)](https://www.youtube.com/watch?v=bJIPlvmoTVw&t=466s): sample projekt zdarma na Fabu → nainstalovat do 5.8 → v projektu zapnout pluginy **MetaHuman Crowd** + **MetaHuman Crowd Content**.

> **Pozn.:** Showcase, ne tutoriál — a čísla ber s rezervou (editor + nahrávání). Podstatný je vzor: **dav = levné instance + streamovaní hrdinové u kamery**, stejná filozofie jako dense/sparse databáze v [GASP](gasp.md#anatomie-gasp-jeden-mm-uzel-a-kapsle-jako-pravda) nebo NDC pooling u [kroků](footsteps.md#niagara-data-channel-castice-kroku-bez-stovky-systemu). Pro naši vesnici je tohle výhled — desítky vesničanů s rutinami spíš utáhne [State Tree + smart objects](state-trees.md), ale trh nebo slavnost by Crowd zvládl.

**Souvislosti:** [GASP: NPC](gasp.md#npc-pres-state-tree-a-smart-objects-mozek-na-serveru-motor-v-komponente) · [Rejstřík: Mass Entity](../rejstrik.md#mass-entity) · [Rejstřík: MetaHuman](../rejstrik.md#metahuman) · [Rejstřík: Nanite](../rejstrik.md#nanite)

---

## Optimalizace obličeje: co dělá Metapipe Nitrous

**Zdroj:** [Optimize Metahuman Facial Performance | Metapipe 3.3 Nitrous](https://www.youtube.com/watch?v=TE9NJHHVHsM) · [Arts and Spells](https://www.youtube.com/channel/UCUNcjczcJ2K4MjY3fYrWa2w) · ~12 min, workflow placeného Maya nástroje

**Shrnutí:** MetaHuman obličej žene stovky kostí — **Metapipe Nitrous** (placený Maya plugin) skeleton „vysaje": odstraní klouby a všech ~700 výrazů přenese do **blend shapes** [(2:20)](https://www.youtube.com/watch?v=TE9NJHHVHsM&t=140s). Kapitola z workflow vytahuje hlavně přenositelné znalosti o tom, jak je MetaHuman obličej uvnitř poskládaný.

### Rozpad myšlenky

**Pipeline v kostce:** export **DNA** hlavy a těla z MetaHuman Creatoru (vyžaduje full rig) [(0:47)](https://www.youtube.com/watch?v=TE9NJHHVHsM&t=47s) → Maya/Metapipe: load DNA (pořadí: hlava, pak tělo!), Nitrous s režimem joints-remove [(1:33)](https://www.youtube.com/watch?v=TE9NJHHVHsM&t=93s) → export FBX s pečlivými importními volbami (bez skeletonu u hlavy, high precision skin weights, import morph targets) [(6:15)](https://www.youtube.com/watch?v=TE9NJHHVHsM&t=375s) → import DNA assetu k head meshi (souřadnice Y down / Z front) [(7:02)](https://www.youtube.com/watch?v=TE9NJHHVHsM&t=422s).

**Přenositelné poznatky** (platí i bez nástroje):

- **Post-process ABP a control rig jsou vázané na skeleton** — nový skeleton znamená duplikovat `ABP_Face_PostProcess` + face control rig a přeřadit (`Assign Skeleton`, import hierarchie do rig grafu) [(7:48)](https://www.youtube.com/watch?v=TE9NJHHVHsM&t=468s). Jednorázová práce per typ skeletonu [(10:08)](https://www.youtube.com/watch?v=TE9NJHHVHsM&t=608s).
- **Animace se převádějí přes `Replace Skeleton`** — right-click na animaci, vybrat nový skeleton, hotovo [(11:42)](https://www.youtube.com/watch?v=TE9NJHHVHsM&t=702s); MetaHuman Animator výstupy tak jedou dál.
- Detail k neviditelnému švu hlava–tělo: **vertex color mapa** z DNA calibration dat [(3:56)](https://www.youtube.com/watch?v=TE9NJHHVHsM&t=236s) — šev kryje shader, ne geometrie.

> **Pozn.:** Zaznamenáno jako „co existuje": vyžaduje Mayu a placený plugin, pro nás teď mimo pipeline. Kdy dává smysl: hodně mluvících NPC na slabším hardwaru — blend shapes škálují líp než stovky kostí per hlava. Bezplatná odpověď Epicu jde jiným směrem (LODy MetaHuman rigu a [Crowd](#crowd-plugin-tisic-metahumanu-pres-mass) instance).

**Souvislosti:** [Rejstřík: MetaHuman](../rejstrik.md#metahuman) · [Rejstřík: post-process AnimBP](../rejstrik.md#post-process-animbp) · [Animační nástroje: mocap](animace-nastroje.md#markerless-mocap-v-58-z-videa-na-animaci-bez-obleku)