# Landscape: tipy pro klasický terén

Než Mesh Terrain dozraje z experimentu, klasický **Landscape** zůstává produkční volbou — a tahle kapitola sbírá pět praktických receptů: Nanite displacement (terén s reliéfem z materiálu), skrytý copy/paste nástroj pro sculpting, malování PCG dat štětcem, dvě techniky proti opakujícím se texturám a hloubku bez geometrie přes POM a contact shadows. Nový systém rozebírá [Mesh Terrain](mesh-terrain.md).

---

## Nanite displacement a krajina jako scéna

**Zdroj:** [Unreal Engine Landscape creation for beginners | Full Tutorial](https://www.youtube.com/watch?v=gNLL1jFmWjQ) · [World Of VFX](https://www.youtube.com/channel/UCWP2AikFs8LlH0ajpnQiT7w) · ~13 min, tutoriál

**Shrnutí:** Plochý landscape s Megascans materiálem vypadá jako tapeta — **Nanite displacement** z něj udělá reliéf: kamínky a hrudky skutečně vystupují z povrchu. Zapíná se na dvou místech: v materiálu (Displacement u parenta) a na landscapu (Enable Nanite + rebuild data) [(2:27)](https://www.youtube.com/watch?v=gNLL1jFmWjQ&t=147s).

### Rozpad myšlenky

**Postup:** landscape z Landscape módu (s možností vlastní height mapy) [(0:49)](https://www.youtube.com/watch?v=gNLL1jFmWjQ&t=49s), Megascans surface materiál přetáhnout na landscape [(1:41)](https://www.youtube.com/watch?v=gNLL1jFmWjQ&t=101s), v parent materiálu zapnout Displacement, na landscapu Nanite a rebuildnout [(3:13)](https://www.youtube.com/watch?v=gNLL1jFmWjQ&t=193s). A drobnost s velkou hodnotou: do scény hned hodit **manekýna jako měřítko** [(4:00)](https://www.youtube.com/watch?v=gNLL1jFmWjQ&t=240s) — kameny a stromy se škálují proti němu, jinak je „velikost od oka" v krajině vždycky vedle [(6:57)](https://www.youtube.com/watch?v=gNLL1jFmWjQ&t=417s).

**Zbytek videa je pipeline krajinné scény** (víc environment než terén, ale jako checklist se hodí): Environment Light Mixer + volumetric fog (Scattering Distribution a Fog Density ~0,02 pro čitelnou mlhu v pozadí [(9:24)](https://www.youtube.com/watch?v=gNLL1jFmWjQ&t=564s)), HDRI backdrop, post-process volume s uzamčenou expozicí [(10:56)](https://www.youtube.com/watch?v=gNLL1jFmWjQ&t=656s) a kamera s DSLR presetem, širokým sklem (12 mm) a ostřením na popředí [(6:57)](https://www.youtube.com/watch?v=gNLL1jFmWjQ&t=417s).

> **Pozn.:** Displacement je tatáž technologie, na které stojí [Mesh Terrain materiály](mesh-terrain.md#materialy-a-channels) — Landscape s Nanite je mezikrok: pořád height mapa (žádné převisy), ale detail povrchu už z materiálu. Pozor na cenu: displacement + hustá teselace není zadarmo, na cílové platformě měř.

**Souvislosti:** [Mesh Terrain](mesh-terrain.md) · [Rejstřík: Nanite](../rejstrik.md#nanite) · [Rejstřík: landscape](../rejstrik.md#landscape) · [Hloubka bez geometrie](#hloubka-bez-geometrie-pom-contact-shadows-a-plugin-ihp) *(iluze místo geometrie)*

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

**Souvislosti:** [Nástroje: EasyWaterscape](nastroje-voda.md#easywaterscape-jak-je-poskladany-dobry-vodni-nastroj) · [Rejstřík: dynamic material instance](../rejstrik.md#dynamic-material-instance) · [Rejstřík: landscape](../rejstrik.md#landscape) · [Hloubka bez geometrie](#hloubka-bez-geometrie-pom-contact-shadows-a-plugin-ihp) *(dvě měřítka dlaždic a k nim POM)*

---

## Hloubka bez geometrie: POM, contact shadows a plugin IHP

**Zdroj:** [Landscape Lab #01 — The Perfect POM + Contact Shadows Combo in Unreal Engine 5](https://www.youtube.com/watch?v=gxk2ulmlkX8) · [Gatyh Interactive](https://www.youtube.com/channel/UCD0NoUWYncvEFwIgvul67yA) · ~21 min, tutoriál ·
[NEXT-GEN Real-Time Displacement | IHP for Unreal Engine](https://www.youtube.com/watch?v=c9WhNdNLheY) · [Denizcan Gok](https://www.youtube.com/channel/UCj71BfR3Nhebwnb8AxFlw4g) · ~15 min, ukázka pluginu od jeho vývojáře

**Shrnutí:** Plochý terén dostane reliéf z výškové mapy bez jediného polygonu navíc:
- **parallax occlusion mapping** posouvá UV podle úhlu pohledu, takže povrch vypadá prostorově;
- **contact shadows** berou tutéž výšku a podle polohy slunce z ní dělají drobné stíny reliéfu, skoro zadarmo.

Obojí běží jen u kamery, dál se materiál přepne na levnější vzdálené dlaždicování. Háček: kvalitu POM určuje počet kroků a každý krok stojí výkon. Plugin IHP slibuje stejnou hloubku bez artefaktů POM, ale jeho čísla jsou zatím jen z ukázky jeho vývojáře.

### Rozpad myšlenky

**Princip.** Výšková mapa nese výšku povrchu: bílá je výš, černá níž. POM z ní předstírá hloubku podle toho, odkud se díváš, takže i úplně plochý povrch vypadá jako geometrie [(0:02)](https://www.youtube.com/watch?v=gxk2ulmlkX8&t=2s), [(0:49)](https://www.youtube.com/watch?v=gxk2ulmlkX8&t=49s). Contact shadows používají stejnou texturu a skoro bez ceny GPU z ní dělají stín. Hodí se i na vegetaci, třeba na vzdálené stromy, kam běžné stíny nedosáhnou [(0:49)](https://www.youtube.com/watch?v=gxk2ulmlkX8&t=49s). Na terénu vznikají z reliéfu textury a polohy slunce [(1:35)](https://www.youtube.com/watch?v=gxk2ulmlkX8&t=95s).

**Blízko a daleko.** Materiál pracuje se dvěma měřítky dlaždic. Proti opakování to podle videa není nejkvalitnější technika, ale výkonem je nejlepší a dovolí pustit POM a contact shadows jen na blízký povrch. Texture bombing s POM podle videa nevypadá dobře [(1:35)](https://www.youtube.com/watch?v=gxk2ulmlkX8&t=95s), [(3:08)](https://www.youtube.com/watch?v=gxk2ulmlkX8&t=188s). Vzdálenost od kamery (uzel Distance mezi Camera Position a World Position) jde přes SmoothStep s parametry začátku a konce přechodu [(3:08)](https://www.youtube.com/watch?v=gxk2ulmlkX8&t=188s), [(3:54)](https://www.youtube.com/watch?v=gxk2ulmlkX8&t=234s). Vzdálené měřítko je tak malé číslo, že ho video ladí přes lerp mezi 0 a 0,0016 [(4:40)](https://www.youtube.com/watch?v=gxk2ulmlkX8&t=280s). Textury jsou zabalené po dvou, BCR (barva a roughness) a NSD (normála, specular a výška). Normála se proto skládá zpátky ze dvou kanálů, se samostatnými texturami to odpadá [(1:35)](https://www.youtube.com/watch?v=gxk2ulmlkX8&t=95s), [(8:33)](https://www.youtube.com/watch?v=gxk2ulmlkX8&t=513s), [(10:06)](https://www.youtube.com/watch?v=gxk2ulmlkX8&t=606s).

**POM.** Vestavěný uzel ParallaxOcclusionMapping dostane [(5:26)](https://www.youtube.com/watch?v=gxk2ulmlkX8&t=326s), [(6:13)](https://www.youtube.com/watch?v=gxk2ulmlkX8&t=373s):
- poměr výšky přes lerp mezi 0 a 0,1, aby se dal jemně ladit;
- minimum a maximum kroků, v ukázce 16 a 32;
- referenční rovinu 0,2 a kanál výškové mapy;
- jen blízké UV. Static switch dovolí POM vypnout [(7:46)](https://www.youtube.com/watch?v=gxk2ulmlkX8&t=466s).

Kroky jsou kvalita: při 2 a 4 jsou schody vidět. Pro nejlepší výsledek video radí minimum kolem 60 kroků, nad které už rozdíl podle něj není znát, a maximum 120. Každý krok navíc stojí výkon. Poměr výšky závisí na kontrastu výškové mapy, v ukázce sedí 3 [(18:41)](https://www.youtube.com/watch?v=gxk2ulmlkX8&t=1121s).

**Contact shadows přes pixel depth offset.** Výška projde přes CheapContrast do Pixel Depth Offset [(10:54)](https://www.youtube.com/watch?v=gxk2ulmlkX8&t=654s). Materiál je kvůli tomu postavený na material attributes [(2:21)](https://www.youtube.com/watch?v=gxk2ulmlkX8&t=141s). Material function pro délku stínu posune ve stínovém průchodu (ShadowPassSwitch) vrcholy podél normály a pixel depth offset dopočítá z délky v prostoru kamery, vynásobené parametrem [(12:28)](https://www.youtube.com/watch?v=gxk2ulmlkX8&t=748s), [(13:14)](https://www.youtube.com/watch?v=gxk2ulmlkX8&t=794s), [(14:01)](https://www.youtube.com/watch?v=gxk2ulmlkX8&t=841s). Na směrovém světle je pak potřeba nastavit Contact Shadow Length, výchozí 0 video zvedá na 0,4 [(19:29)](https://www.youtube.com/watch?v=gxk2ulmlkX8&t=1169s). Cena v ukázce je orientační, video samo upozorňuje, že na pozadí běží spousta věcí. Vypnutí contact shadows podle stat GPU nic nezmění, vypnutí POM ušetří asi 0,4 ms z přibližně 6 až 7 ms [(20:15)](https://www.youtube.com/watch?v=gxk2ulmlkX8&t=1215s).

**IHP od vývojáře.** IHP (Implicit Heightfield Projection) je plugin, jehož autor video natočil [(0:02)](https://www.youtube.com/watch?v=c9WhNdNLheY&t=2s).
- **Nastavení výškové textury**, jak ho video připravuje pro IHP (že se hodí i jinde, je naše úvaha): komprese Vector Displacement Map, když je výška v kanálu jiné textury, a Half Float, když je samostatná. Dál filtr Trilinear, Mip Gen Settings Simple Average, bez ztrátové komprese (No Lossy) a Mip Load Options All Mips [(1:39)](https://www.youtube.com/watch?v=c9WhNdNLheY&t=99s), [(2:30)](https://www.youtube.com/watch?v=c9WhNdNLheY&t=150s), [(3:16)](https://www.youtube.com/watch?v=c9WhNdNLheY&t=196s).
- **Uzel IHP Standard** dostane výšku jako texture object a UV. Normálu si dopočítá z výšky, normal mapa tedy není potřeba, a vrací i masku stínu, kterou se násobí base color [(4:04)](https://www.youtube.com/watch?v=c9WhNdNLheY&t=244s), [(4:52)](https://www.youtube.com/watch?v=c9WhNdNLheY&t=292s).
- **Parametry:** síla výšky, kanál, rozlišení výškové mapy (má odpovídat skutečné textuře, v ukázce 8192), velikost plochy v UV, směr světla pro stíny, kvalita 0 až 3 (sám autor používá skoro jen 3), vlastní stínění a vrhání stínu. Siluetu jde zapnout přes masked blend mode a opacity mask [(8:16)](https://www.youtube.com/watch?v=c9WhNdNLheY&t=496s), [(8:58)](https://www.youtube.com/watch?v=c9WhNdNLheY&t=538s), [(9:49)](https://www.youtube.com/watch?v=c9WhNdNLheY&t=589s), [(10:36)](https://www.youtube.com/watch?v=c9WhNdNLheY&t=636s), [(11:22)](https://www.youtube.com/watch?v=c9WhNdNLheY&t=682s), [(12:09)](https://www.youtube.com/watch?v=c9WhNdNLheY&t=729s).
- **Výkon podle autora:** malá plocha s IHP běží na 120 FPS (8,33 ms) a po zvětšení na 10 000 × 10 000 pořád na 119 až 120 FPS. Srovnání bez IHP ani s Nanitem nebo POM video neukazuje. Nanite podle autora takový výkon většinou nedá, aniž by projekt ztěžkl, a POM má artefakty a lepší výkon dá jen občas, za cenu vzhledu [(5:39)](https://www.youtube.com/watch?v=c9WhNdNLheY&t=339s), [(6:26)](https://www.youtube.com/watch?v=c9WhNdNLheY&t=386s), [(7:29)](https://www.youtube.com/watch?v=c9WhNdNLheY&t=449s). Další video má ukázat IHP s runtime virtual texturou na velkém terénu [(13:48)](https://www.youtube.com/watch?v=c9WhNdNLheY&t=828s).

> **Pozn.:** Dvě měřítka dlaždic jsou tatáž myšlenka jako blend podle vzdálenosti v [Anti-tilingu](#anti-tiling-texture-variation-a-blend-podle-vzdalenosti), jen tady navíc vypínají drahé efekty v dálce. [Nanite displacement](#nanite-displacement-a-krajina-jako-scena) stojí na opačné straně: vytváří skutečnou geometrii se skutečnými stíny, kdežto POM jen předstírá hloubku v pixelech a obrys povrchu nechá rovný. Siluetová maska IHP míří právě na tuhle slabinu. To je naše srovnání. IHP je vývojářův vlastní plugin a jeho výkon i kvalitu zatím ukazuje jen jeho scéna, cenu video neuvádí. Hodnota 8,33 ms je přesně 1000/120, takže měření může narážet na strop snímkové frekvence. To je náš odhad. Gatyh Interactive odkazuje na vlastní texture packer a vlastní web s texturami zdarma pod licencí CC0 [(2:21)](https://www.youtube.com/watch?v=gxk2ulmlkX8&t=141s), [(17:55)](https://www.youtube.com/watch?v=gxk2ulmlkX8&t=1075s).

**Souvislosti:** [Rejstřík: Parallax occlusion mapping](../rejstrik.md#parallax-occlusion-mapping) · [Rejstřík: Contact shadows](../rejstrik.md#contact-shadows) · [Rejstřík: Pixel Depth Offset](../rejstrik.md#pixel-depth-offset) · [Rejstřík: Height mapa](../rejstrik.md#height-mapa) · [Nanite displacement: reliéf malovaný vertex colorem](materialy.md#nanite-displacement-relief-malovany-vertex-colorem) *(skutečná geometrie místo iluze)* · [Stopy do hloubky](footsteps.md#stopy-do-hloubky-render-target-jako-platno-pod-postavou) *(skutečná prohlubeň místo iluze)*
