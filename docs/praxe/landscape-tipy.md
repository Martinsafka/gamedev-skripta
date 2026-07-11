# Landscape: tipy pro klasický terén

Než Mesh Terrain dozraje z experimentu, klasický **Landscape** zůstává produkční volbou — a tahle kapitola sbírá čtyři praktické recepty: Nanite displacement (terén s reliéfem z materiálu), skrytý copy/paste nástroj pro sculpting, malování PCG dat štětcem a dvě techniky proti opakujícím se texturám. Nový systém rozebírá [Mesh Terrain](mesh-terrain.md).

---

## Nanite displacement a krajina jako scéna

**Zdroj:** [Unreal Engine Landscape creation for beginners | Full Tutorial](https://www.youtube.com/watch?v=gNLL1jFmWjQ) · [World Of VFX](https://www.youtube.com/channel/UCWP2AikFs8LlH0ajpnQiT7w) · ~13 min, tutoriál

**Shrnutí:** Plochý landscape s Megascans materiálem vypadá jako tapeta — **Nanite displacement** z něj udělá reliéf: kamínky a hrudky skutečně vystupují z povrchu. Zapíná se na dvou místech: v materiálu (Displacement u parenta) a na landscapu (Enable Nanite + rebuild data) [(2:27)](https://www.youtube.com/watch?v=gNLL1jFmWjQ&t=147s).

### Rozpad myšlenky

**Postup:** landscape z Landscape módu (s možností vlastní height mapy) [(0:49)](https://www.youtube.com/watch?v=gNLL1jFmWjQ&t=49s), Megascans surface materiál přetáhnout na landscape [(1:41)](https://www.youtube.com/watch?v=gNLL1jFmWjQ&t=101s), v parent materiálu zapnout Displacement, na landscapu Nanite a rebuildnout [(3:13)](https://www.youtube.com/watch?v=gNLL1jFmWjQ&t=193s). A drobnost s velkou hodnotou: do scény hned hodit **manekýna jako měřítko** [(4:00)](https://www.youtube.com/watch?v=gNLL1jFmWjQ&t=240s) — kameny a stromy se škálují proti němu, jinak je „velikost od oka" v krajině vždycky vedle [(6:57)](https://www.youtube.com/watch?v=gNLL1jFmWjQ&t=417s).

**Zbytek videa je pipeline krajinné scény** (víc environment než terén, ale jako checklist se hodí): Environment Light Mixer + volumetric fog (Scattering Distribution a Fog Density ~0,02 pro čitelnou mlhu v pozadí [(9:24)](https://www.youtube.com/watch?v=gNLL1jFmWjQ&t=564s)), HDRI backdrop, post-process volume s uzamčenou expozicí [(10:56)](https://www.youtube.com/watch?v=gNLL1jFmWjQ&t=656s) a kamera s DSLR presetem, širokým sklem (12 mm) a ostřením na popředí [(6:57)](https://www.youtube.com/watch?v=gNLL1jFmWjQ&t=417s).

> **Pozn.:** Displacement je tatáž technologie, na které stojí [Mesh Terrain materiály](mesh-terrain.md#materialy-a-channels) — Landscape s Nanite je mezikrok: pořád height mapa (žádné převisy), ale detail povrchu už z materiálu. Pozor na cenu: displacement + hustá teselace není zadarmo, na cílové platformě měř.

**Souvislosti:** [Mesh Terrain](mesh-terrain.md) · [Rejstřík: Nanite](../rejstrik.md#nanite) · [Rejstřík: landscape](../rejstrik.md#landscape)

---

## Copy/paste gizmo: sculpty jako znovupoužitelné patche

**Zdroj:** [Secret Copy/Paste Tool for Landscapes in Unreal Engine 5](https://www.youtube.com/watch?v=1ySwXsKR4VM) · [Aziel Arts](https://www.youtube.com/channel/UCxGoreKfZxDBxJzirLWuOuw) · ~12 min, tutoriál

**Shrnutí:** V landscape nástrojích se skrývá copy/paste, o kterém „nikdo nemluví" [(0:01)](https://www.youtube.com/watch?v=1ySwXsKR4VM&t=1s): vysculptovaný kopec označíš, zkopíruješ do **gizmo volume** a vložíš jinam — klidně přeškálovaný. A totéž gizmo umí **importovat height mapu do vybrané zóny** místo celého landscapu.

### Rozpad myšlenky

**Kopírování:** selection tool → namalovat výběr kolem útvaru → `Ctrl+C` zkopíruje výšková data do gizma [(1:34)](https://www.youtube.com/watch?v=1ySwXsKR4VM&t=94s) → přesunout gizmo → `Ctrl+V` [(2:22)](https://www.youtube.com/watch?v=1ySwXsKR4VM&t=142s). Škálování má háček: po zvětšení/zmenšení gizma je nutné kliknout **Fit Height Values to Gizmo Size**, jinak se vloží původní výšky [(3:08)](https://www.youtube.com/watch?v=1ySwXsKR4VM&t=188s). Paste má režimy raise/lower only a tool strength; v copy módu existuje i brush — kopií jde *malovat* po částech [(3:54)](https://www.youtube.com/watch?v=1ySwXsKR4VM&t=234s).

**Past číslo jedna — edit layers** [(1:34)](https://www.youtube.com/watch?v=1ySwXsKR4VM&t=94s): kopíruje se z **aktuálně vybrané edit layer**. Když je sculpt v jiné vrstvě, zkopíruje se prázdno, i když kopec na obrazovce vidíš.

**Import height mapy do zóny** [(5:28)](https://www.youtube.com/watch?v=1ySwXsKR4VM&t=328s): copy tool → Advanced → Gizmo Import/Export. Dva háčky: bere **jen 16bit RAW** [(6:15)](https://www.youtube.com/watch?v=1ySwXsKR4VM&t=375s) a RAW nemá metadata — při importu musíš rozlišení zadat ručně, takže exportuj sám (z Gaea: export node, u-short raw formát, build [(7:01)](https://www.youtube.com/watch?v=1ySwXsKR4VM&t=421s)) a rozlišení si pamatuj [(9:21)](https://www.youtube.com/watch?v=1ySwXsKR4VM&t=561s). Detail vloženého útvaru limituje rozlišení landscapu — větší gizmo z height mapy vytáhne víc [(10:53)](https://www.youtube.com/watch?v=1ySwXsKR4VM&t=653s).

> **Pozn.:** Ve světě Mesh Terrainu tohle dělá [texture modifier](mesh-terrain.md#modifier-stack-nedestruktivni-tvarovani) elegantněji (patch je živý objekt) — gizmo je jeho předchůdce pro klasický Landscape. Workflow „knihovna kopců z Gaea → razítkování do levelu" je ale stejný a přenositelný.

**Souvislosti:** [Mesh Terrain: modifier stack](mesh-terrain.md#modifier-stack-nedestruktivni-tvarovani) · [Rejstřík: height mapa](../rejstrik.md#height-mapa) · [Rejstřík: edit layer](../rejstrik.md#edit-layer)

---

## Malování dat: paint layers řídí PCG

**Zdroj:** [Unreal Engine 5.7 - Procedural Landscape Painting - Tutorial](https://www.youtube.com/watch?v=REpMPdptKWQ) · [Unreal - X - Tutorials](https://www.youtube.com/channel/UCjKg7gsHCEyXtJbZYx2Xu7A) · ~8 min, tutoriál

**Shrnutí:** „Nemalujeme meshe, malujeme **data**" [(0:02)](https://www.youtube.com/watch?v=REpMPdptKWQ&t=2s): landscape paint vrstvy PCG_grass/PCG_trees/PCG_rocks nenesou textury, ale váhy, které si čte PCG graf — tah štětcem spawnuje trávu, stromy a kameny, a změna nastavení grafu je přemaluje bez přemalování.

### Rozpad myšlenky

**Materiál:** landscape layer blend s vrstvami dvojího druhu — PCG vrstvy (weight blend, jen debug šedé barvy, ať je vidět tah) a skutečné materiálové vrstvy (alpha blend, textury + `Landscape Layer Coords` pro škálování) [(0:50)](https://www.youtube.com/watch?v=REpMPdptKWQ&t=50s). Pozor: **normal mapy potřebují vlastní layer blend uzel** (každý parametr má svůj) a netexturované vrstvy neutrální normálu (0, 0, 1) [(2:24)](https://www.youtube.com/watch?v=REpMPdptKWQ&t=144s). V paint módu pak `Create Layer from Assigned Material` → auto-fill layer assets → fill base vrstvy [(3:11)](https://www.youtube.com/watch?v=REpMPdptKWQ&t=191s).

**PCG graf** [(4:45)](https://www.youtube.com/watch?v=REpMPdptKWQ&t=285s): `Get Landscape Data` → `Surface Sampler` (hustota bodů dle vrstvy — tráva 10/m²) → **`Filter Attribute Elements`**: target attribute = **přesné jméno vrstvy**, operátor greater than, constant threshold 0,2 → `Transform Points` (rotace Z 360°, scale 0,5–1) → `Static Mesh Spawner`. Per vrstva se řetěz duplikuje s jinými hodnotami [(6:20)](https://www.youtube.com/watch?v=REpMPdptKWQ&t=380s). Váhy vrstev se sčítají do 1 — threshold 0,2 dovolí vrstvy **míchat** (tráva pod stromy) [(5:33)](https://www.youtube.com/watch?v=REpMPdptKWQ&t=333s).

> **Pozn.:** Přesně ten vzor, který se vrací ve velkém v [PCG tématu](pcg-zaklady.md) — a jeho Mesh Terrain dvojče je v [rozšířené Mesh Terrain kapitole](mesh-terrain.md). Prakticky: tohle je level-designové UX snů — art directing vegetace štětcem, s procedurální disciplínou pod povrchem.

**Souvislosti:** [Mesh Terrain: kanály v praxi](mesh-terrain.md) · [Rejstřík: PCG](../rejstrik.md#pcg) · [Rejstřík: landscape](../rejstrik.md#landscape)

---

## Anti-tiling: texture variation a blend podle vzdálenosti

**Zdroj:** [Unreal Engine 5.7 - Fix Repeating Landscape Textures - Tutorial](https://www.youtube.com/watch?v=A1P8LK7POuM) · [Unreal - X - Tutorials](https://www.youtube.com/channel/UCjKg7gsHCEyXtJbZYx2Xu7A) · ~6 min, tutoriál

**Shrnutí:** Opakující se textura je poznávací znamení amatérské krajiny — a oprava jsou dva uzly: **Texture Variation** (náhodně posouvá, rotuje a škáluje dlaždice — „99 % opakování zmizí okamžitě" [(0:49)](https://www.youtube.com/watch?v=A1P8LK7POuM&t=49s)) a **Camera Depth Fade** blend mezi dvěma měřítky mapování — malé detaily u kamery, velké v dálce.

### Rozpad myšlenky

**Texture Variation:** landscape coords → UV input uzlu, shifted UV výstup → textury; static bool true na random rotation and scale [(0:49)](https://www.youtube.com/watch?v=A1P8LK7POuM&t=49s). Dither volba změkčí švy vzoru — ale korektně funguje jen s Nanite landscapem [(1:35)](https://www.youtube.com/watch?v=A1P8LK7POuM&t=95s). Variation Scale (default 3,24) a Variation Levels (6) povýšit na parametry, ať se ladí z instance [(2:21)](https://www.youtube.com/watch?v=A1P8LK7POuM&t=141s).

**Dvě měřítka podle vzdálenosti** [(3:07)](https://www.youtube.com/watch?v=A1P8LK7POuM&t=187s): celý setup přesunout do **material function** s function inputem (Vector 2) místo landscape coords → v materiálu dvě volání s mapping scale 15 (blízko) a 50 (dálka) → **Blend Material Attributes** s alphou z **Camera Depth Fade** (fade length 10 000, offset 20 000). Výsledek: jedna čtvercová textura + normálka pokryje celý landscape a vypadá přirozeně zblízka i z kopce [(5:29)](https://www.youtube.com/watch?v=A1P8LK7POuM&t=329s).

> **Pozn.:** Stejné myšlenky, jiná jména: Faucherův EasyWaterscape tomu říká cell bombing a distance blend ([nástroje vody](nastroje-voda.md#easywaterscape-jak-je-poskladany-dobry-vodni-nastroj)) a Sensei terrain materiál to nabízí pro Mesh Terrain — anti-tiling dvojice „rozbij dlaždice + přepni měřítko v dálce" je univerzální slovník materiálů velkých ploch.

**Souvislosti:** [Nástroje: EasyWaterscape](nastroje-voda.md#easywaterscape-jak-je-poskladany-dobry-vodni-nastroj) · [Rejstřík: dynamic material instance](../rejstrik.md#dynamic-material-instance) · [Rejstřík: landscape](../rejstrik.md#landscape)
