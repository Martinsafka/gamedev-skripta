# Mesh Terrain (UE 5.8)

Epic v UE 5.8 představil Mesh Terrain — nové pojetí terénu, které má výhledově nahradit klasický Landscape. Kapitola destiluje 47minutový deep dive do systému (proč vznikl, jak se zakládá, nedestruktivní modifier stack, partitioned Nanite mesh) a v závěrečné myšlence ho doplňuje o praktické workflow kanálů, malování a PCG ze dvou dalších zdrojů. Klasický Landscape pokrývají [Landscape tipy](landscape-tipy.md).

**Zdroj prvních čtyř myšlenek:** [Unreal Engine 5.8 Mesh Terrain — Full Deep Dive](https://www.youtube.com/watch?v=JzQrUAVPmr4) · [Aziel Arts](https://www.youtube.com/channel/UCxGoreKfZxDBxJzirLWuOuw) · ~47 min, praktický deep dive (záznam z koučovacího callu)

!!! warning "Beta stav"
    Autor videa opakovaně zdůrazňuje [(7:02)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=422s): systém je raná beta — padá, některé operace jsou pomalé a **nepatří do projektů mířících k vydání**. Ukládej často. Kapitola popisuje stav v UE 5.8; u beta systému čekej změny mezi verzemi.

---

## Proč Mesh Terrain existuje: limity Landscape

**Shrnutí:** Klasický Landscape ukládá tvar do height mapy — černobílé textury, kde jas kóduje výšku. Z toho plyne jeho fundamentální limit: povrch se umí hýbat **jen nahoru a dolů**. Jeskyně, převisy, skalní stěny se řešily obcházením (díra v Landscape + ručně poskládané static meshe). Mesh Terrain je přestavba od základů: terén je skutečná mesh geometrie, rozřezaná na partitions a renderovaná přes Nanite.

### Rozpad myšlenky

Video otevírá přesnou diagnózou staré technologie [(0:48)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=48s): Landscape není mesh, ale proprietární typ povrchu, „papírově tenká" plocha deformovaná height mapou. Vertexy (přesněji jejich landscape obdoba) mají jediný stupeň volnosti — výšku. Jakmile tvar potřebuje víc (jeskyně, převis, vyšší lokální detail, než dovoluje rozlišení Landscape), workflow se láme do dvou světů: terén + záplaty ze static meshů [(1:35)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=95s).

Mesh Terrain oba světy slučuje: **terén je partitioned Nanite mesh** [(2:22)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=142s). Tři důsledky téhle věty:

1. **Mesh** → geometrie může kamkoli; jeskyni vyhloubíš přímo do terénu.
2. **Partitioned** → terén není jeden obří mesh, ale chunky, které se streamují přes World Partition — proto systém **vyžaduje open world (partitioned) level**; v klasickém levelu ho nezaložíš.
3. **Nanite** → dynamická subdivize podle vzdálenosti kamery [(14:03)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=843s). Autor poznamenává, že Nanite Landscape tohle dělal méně efektivně — a právě adaptivita otevírá cestu k větším světům.

K velikosti: Landscape narážel podle RAM na praktický strop kolem 8–16 km; mesh přístup limit posouvá, ale nezruší ho úplně — kolem ~20 km od originu se ozve floating point přesnost [(10:55)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=655s), tedy limit matematiky, ne terénního systému.

> **Pozn.:** Floating point problém stojí za vlastní vysvětlení, protože video ho jen zmíní: 32bitový float má pevný počet platných číslic, takže čím větší souřadnice, tím hrubší nejmenší reprezentovatelný krok — daleko od originu se objekty začnou „třást" a přesné operace selhávat. Velké světy to řeší technikami typu origin shifting / Large World Coordinates, ne větším terénem.

**Souvislosti:** [Založení a partitions](#zalozeni-terenu-partitions-a-rozliseni) níže · [Rejstřík: Nanite](../rejstrik.md#nanite) · [Rejstřík: World Partition](../rejstrik.md#world-partition) · [Rejstřík: height mapa](../rejstrik.md#height-mapa)

---

## Založení terénu: partitions a rozlišení

**Shrnutí:** Mesh Terrain se zapíná pluginem, žije v open world levelu a vzniká čtyřmi cestami: prázdný obdélník, import height mapy, nakreslený spline, nebo konverze existujícího static meshe. Klíčová rozhodnutí při založení jsou velikost, rozlišení (počet quadů) a způsob dělení na partitions.

### Rozpad myšlenky

**Prerekvizity** [(3:10)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=190s): open world level (empty open world stačí) + plugin **Mesh Terrain Mode**; pro spolupráci s PCG resp. vodou navíc příslušné interop pluginy. Po restartu editoru přibude Mesh Terrain mód v přepínači módů vlevo nahoře.

**Cesty vzniku** [(4:42)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=282s): obdélník je výchozí bod pro sculpting od nuly; import height mapy slouží hlavně migraci (existující Landscape → export height mapy → import jako Mesh Terrain) nebo hotovým sculptům z externích nástrojů (Gaea, World Machine); konverze static meshe [(5:28)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=328s) vezme libovolný mesh a rozřeže ho na partition chunky — cesta, jak z „velkého šutru" udělat pochozí terén.

**Velikost a rozlišení** [(8:36)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=516s): velikost se zadává v centimetrech (UE jednotky; 100 000 = 1 km), rozlišení je počet quadů v XY. Generation type pak řídí dělení [(9:22)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=562s): **Automatic** si počet partitions odvodí z rozlišení, **Explicit** nechá zadat počet partitions a rozlišení každé z nich. Video přiznává, že Epic zatím nevydal guidelines, jak partitions dimenzovat [(6:14)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=374s) — autorovy testy dávají smíšené výsledky pro „málo velkých" vs. „hodně malých", takže: testuj na vlastním levelu.

**Práce s velkými plochami:** terén jde založit unloaded a nahrávat si jen regiony, na kterých pracuješ [(10:09)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=609s) — v World Partition okně se partitions objeví jako buňky s load/unload region ovládáním [(13:16)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=796s). Výsledný **Mesh Partition Actor** v outlineru je kontejner celého terénu; ve scéně jich může být víc a lze k nim přidávat další sekce — terén nemusí být čtverec [(11:42)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=702s). Pro správu modifikací pak slouží **Mesh Partition Outliner** (`Tools → Miscellaneous`) [(13:16)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=796s).

**Souvislosti:** [Modifier stack](#modifier-stack-nedestruktivni-tvarovani) níže · [Rejstřík: PCG](../rejstrik.md#pcg) · [Rejstřík: quad](../rejstrik.md#quad)

---

## Modifier stack: nedestruktivní tvarování

**Shrnutí:** Nejdůležitější workflow poznatek celého videa: přímé sculptování na terén je destruktivní a zahazuje hlavní sílu systému. Správný postup je skládat **modifiery** — brush, noise, spline, texture, mesh projekce, boolean, remesh — které zůstávají živé: lze je přesouvat, duplikovat, přeskládat v prioritě a mazat. Terén se chová jako vrstvený dokument, ne jako hlína.

### Rozpad myšlenky

**Brush modifier jako kontejner sculptu** [(17:09)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=1029s): místo malování přímo na terén nejdřív přidat Brush modifier vymezující oblast a sculptovat uvnitř něj. Odměna přijde okamžitě [(20:15)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=1215s) — vysculptovaná jeskyně je objekt: posuneš ji, Alt-dragem naklonuješ celou sérii jeskyní. Sculpt nástroje uvnitř: **Sculpt N** pracuje plně ve 3D (Ctrl obrací směr — tak se vrtá jeskyně, což Landscape neuměl [(17:56)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=1076s)), Move posouvá vertexy „jako hlínu", dále Smooth, Pinch, Flatten; vedle nich klasická height-only rodina (Height Sculpt/Smooth/Flatten) a **Erode** [(19:28)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=1168s), jehož vyhlazování napodobuje erozi — na svazích působí přirozeněji než čistý smooth (autor doporučuje ubrat strength).

**Další modifiery:** Noise přidá procedurální variaci povrchu (intenzitu držet nízko, ~10) [(21:49)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=1309s); Spline je mesh-obdoba landscape splinů — zatlačí terén podél křivky, s falloff a plateau šířkou pro cesty [(22:35)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=1355s) (noise zatím nemá); **Texture** promítá height mapu shora jako přemístitelný „patch" [(29:31)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=1771s) — s falloff blendem a volitelnou adaptivní teselací, která lokálně zjemní mesh podle detailu textury [(31:04)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=1864s); **Mesh** dělá totéž s 3D geometrií místo textury (projekce raycastem — hora ze static meshe jako razítko) [(34:58)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=2098s); **Boolean** [(36:31)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=2191s) mesh do terénu skutečně vroubuje — union přiroste, subtract vyřízne, geometrie meshe zůstane vlastní a na okrajích se sešije s terénem (organické díry, skalnaté okraje kráterů); **Remesh** [(32:37)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=1957s) lokálně mění hustotu mesh — detail jen tam, kde je potřeba, ve dvou režimech (Remesh = uniformní přestavba podle target edge length, Tessellate = adaptivní dělení).

**Pravidla stacku:**

- **Modifiery jsou 3D volumy** [(24:07)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=1447s) — působí jen uvnitř svého žlutého boxu. „Efekt končí v půlce kopce" = zvětšit Max Z, ne hledat bug.
- **Priorita = pořadí vyhodnocení** [(24:53)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=1493s). Sculpt vrstva s nízkou prioritou „přemaže" spline, protože se vyhodnocuje ve špatném bodě stacku [(25:40)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=1540s) — když modifikace nerespektuje ostatní, první podezřelý je priorita. (Drag-and-drop přeskládání zatím chybí; mění se číslem.)
- **Blending módy** Normal/Minimum/Maximum [(26:26)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=1586s): Minimum se projeví jen tam, kde tlačí terén níž, Maximum jen výš. Autorova analogie sedí — chová se to jako blend módy vrstev v grafickém editoru; use case je cesta, která se má do terénu jen zařezávat, nikdy ho nenavyšovat [(27:13)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=1633s).
- **Editační vs. zbuildovaný stav** [(27:59)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=1679s): s vybraným partition actorem jsi v dynamickém editačním režimu; kliknutím pryč se přestaví Nanite mesh — propad FPS během editace je normální a po odkliknutí zmizí. Shadow artefakty po přestavbě řeší `Build → Precompute Static Visibility` nebo zoom out/in [(28:45)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=1725s).
- **Build cost** u každého modifieru [(21:02)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=1262s) ukazuje, co terén při přestavbě stojí — vodítko, kterou techniku volit, když editor začne zpomalovat. Praktický tip z videa: adaptivní teselaci a těžké patche nechávat vypnuté během hrubého tvarování a zapínat cíleně na konci [(31:51)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=1911s).

> **Pozn.:** Kdo zná node-based nedestruktivní workflow (Houdini, Geometry Nodes v Blenderu, ostatně i modifier stack tamtéž), pozná tu stejnou filozofii: **scéna je recept, ne výsledek.** Cena je stejná jako všude — recept se musí přepočítávat, proto build cost a FPS propady. Výhoda taky: žádné rozhodnutí není konečné.

**Souvislosti:** [Materiály a channels](#materialy-a-channels) níže · [Rejstřík: modifier stack](../rejstrik.md#modifier-stack) · [Rejstřík: boolean](../rejstrik.md#boolean) · [Rejstřík: tessellation](../rejstrik.md#tessellation)

---

## Materiály a channels

**Shrnutí:** Landscape layers dostaly nové jméno — **channels** — a jednodušší setup: definují se v data assetu partition definice a rovnou se z nich stávají malovatelné vrstvy. Novinka s velkým dosahem: vrstvy nemusí malovat jen štětec — **weight channel umí přiřadit kterýkoli modifier**, takže boolean skála si s sebou nese vlastní materiál.

### Rozpad myšlenky

Materiál terénu se přiřazuje v **MPD (Mesh Partition Definition)** data assetu v Details panelu partition actoru [(39:37)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=2377s) — tam žije i texel size (hustota materiálu) a definice channels. Auto-materiály fungují dál: material function řízená sklonem povrchu (surface angle) se aplikuje stejně jako na Landscape a přirozeně pokrývá i boolean/mesh části, protože jsou součástí téhož povrchu [(40:23)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=2423s).

**Channels = landscape layers bez ceremonie** [(41:10)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=2470s): pojmenuješ je v data assetu 1:1 podle vrstev materiálu a jsou k dispozici v paint sekci brush modifieru [(41:56)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=2516s) — odpadá setup layer info assetů. Malované vrstvy jsou pořád modifiery, takže platí všechno z předchozí sekce: duplikace, přesun, blending (attribute weight channels → add).

Nejzajímavější je **weight channel na modifierech** [(43:30)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=2610s): boolean díře přiřadíš channel „dirt" a výřez si materiál obarví sám — mesh, který terén tvaruje, ho zároveň otexturuje. Video zmiňuje i směr přes vertex colors meshe (zatím netestováno autorem) [(44:19)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=2659s). **Voda:** water body si s Mesh Terrainem sám nepotyká — řece je třeba v Details přidat river modifier a ukázat mu cílový mesh partition [(45:06)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=2706s); funguje pro řeky i jezera, se stabilitou odpovídající beta stavu. Závěrečná 10km testovací scéna [(45:53)](https://www.youtube.com/watch?v=JzQrUAVPmr4&t=2753s) ukazuje, že stack unese desítky vrstev: booleany na detailní útesy, height map patche na vzdálené kopce, mesh hory na horizont.

> **Pozn.:** Migrace pro existující projekty se nabízí sama: height mapa Landscape se dá importovat jako startovní tvar Mesh Terrainu. Ale dokud je systém beta, dává smysl spíš druhý směr — prototypovat v něm dovednosti a workflow, produkci nechat na Landscape. Video v tom mluví jasně.

**Souvislosti:** [Proč Mesh Terrain existuje](#proc-mesh-terrain-existuje-limity-landscape) výše · [Rejstřík: channel](../rejstrik.md#channel) · [Rejstřík: data asset](../rejstrik.md#data-asset)

---

## Kanály v praxi: materiál, malování a PCG

**Zdroj:** [How to use Mesh terrain layers? Material + PCG](https://www.youtube.com/watch?v=LWhQwVILHMk) · [DK 3D](https://www.youtube.com/channel/UC3fGhbgSpR2BSSeTls3R6Sg) · ~28 min, tutoriál ·
[How to Use Unreal Engine's New Landscape System - Mesh Terrain Tutorial](https://www.youtube.com/watch?v=Lhj2LutYNjA) · [Unreal Sensei](https://www.youtube.com/channel/UCue7TFlrt9FxXarpsl872Dg) · ~66 min, tutoriál

**Shrnutí:** Předchozí myšlenka popsala kanály koncepčně — tahle je zapojuje do praxe: **jak je materiál čte** (dvojice uzlů Mesh Partition Resource + Channel Sample), na co si dát pozor při **malování** (vrstvy leží doslova na sobě) a jak nad terénem rozjet **PCG** včetně nových nanite foliage stromů.

### Rozpad myšlenky

**Materiál čte kanály dvěma uzly** [(15:21)](https://www.youtube.com/watch?v=LWhQwVILHMk&t=921s): `Mesh Partition Resource` → **`Get Mesh Partition Channel Sample`** (vybereš MPD a kanál) → výstup řídí lerp mezi vrstvami materiálu. Nejrychlejší start: zkopírovat si `M_MeshPartitionDefault` + `MPD_Default` z Engine → Plugins → Mesh Partition do projektu [(12:11)](https://www.youtube.com/watch?v=LWhQwVILHMk&t=731s), v kopii MPD nadefinovat vlastní Channel Descriptions [(14:34)](https://www.youtube.com/watch?v=LWhQwVILHMk&t=874s) a přiřadit ji partition actoru.

**Malování — tři pasti (Sensei):** paint brush modifier patří **nahoru** stacku, ať maluje na všechny vertexy vyrobené pod ním [(39:41)](https://www.youtube.com/watch?v=Lhj2LutYNjA&t=2381s). Vrstvy leží **doslova na sobě** — základní vrstva nemá „štětec": chceš-li zpátky trávu, musíš vrstvy nad ní odmazat (`Ctrl`), jednu po druhé [(43:36)](https://www.youtube.com/watch?v=Lhj2LutYNjA&t=2616s); na auto-vrstvy ze sklonu je zvláštní kanál remove auto material. A **value slider ≠ strength**: value 0 znamená „maluju nulu" a přepisuje, co už namalované je [(42:48)](https://www.youtube.com/watch?v=Lhj2LutYNjA&t=2568s) — sílu ředit strengthem, hodnotu nechat na 1.

**PCG nad terénem:** DK používá **`Mesh Partition Query`** [(20:02)](https://www.youtube.com/watch?v=LWhQwVILHMk&t=1202s) — s klíčovou volbou **Layer = Final**: default vrací základní vrstvu *před* modifikacemi a body plavou ve vzduchu [(20:48)](https://www.youtube.com/watch?v=LWhQwVILHMk&t=1248s). Do query jde přidat namalovaný kanál a filtrovat `Point Filter > 0,5` [(21:36)](https://www.youtube.com/watch?v=LWhQwVILHMk&t=1296s) — stejný vzor jako [malování PCG dat na Landscape](landscape-tipy.md#malovani-dat-paint-layers-ridi-pcg). Sensei k témuž uzlu poznamenává, že je zatím glitchy, a jako spolehlivou cestu doporučuje **`World Ray Hit Query`** [(1:01:42)](https://www.youtube.com/watch?v=Lhj2LutYNjA&t=3702s) — dvě cesty, vyber podle verze a chování. Důležité obecně: **foliage mode se s editem terénu neaktualizuje** (stromy zůstanou viset) — Epic pro Mesh Terrain doporučuje vegetaci přes PCG [(1:00:54)](https://www.youtube.com/watch?v=Lhj2LutYNjA&t=3654s).

**Nanite foliage stromy** [(23:10)](https://www.youtube.com/watch?v=LWhQwVILHMk&t=1390s): po zapnutí Nanite Foliage v project settings a pluginu Procedural Vegetation Editor jsou k dispozici skinned mesh stromy (vítr řídí global foliage actor). V PCG je spawnuje **`Instance Skinned Mesh Spawner`** s atributem typu soft object path [(24:45)](https://www.youtube.com/watch?v=LWhQwVILHMk&t=1485s) — a před ním `Transform Points` s **absolutní Z rotací** 0–360°, jinak stromy rostou po normále svahu [(25:33)](https://www.youtube.com/watch?v=LWhQwVILHMk&t=1533s).

> **Pozn.:** Sensei navíc ukazuje migrační cestu, kterou deep dive neměl: starý Landscape → `Export Selected` jako FBX → import → **Convert** na Mesh Terrain [(1:04:48)](https://www.youtube.com/watch?v=Lhj2LutYNjA&t=3888s) — s původní geometrií, hned Nanite. K tomu dvě workflow pravidla pro remesh: **tessellate před sculptem** oblasti, o které víš, že ponese detail, a **remesh po extrémním sculptu**, který natáhl quady [(18:42)](https://www.youtube.com/watch?v=Lhj2LutYNjA&t=1122s). Virtual texture blending s terénem funguje (TP_VirtualTexture v definici) [(1:02:29)](https://www.youtube.com/watch?v=Lhj2LutYNjA&t=3749s) a Sensei rozdává zdarma svůj terrain master materiál (auto-slope vrstvy, cell bombing, distance blend) [(0:49)](https://www.youtube.com/watch?v=Lhj2LutYNjA&t=49s) — dobrá učebnice, jak Mesh Terrain materiály stavět.

**Souvislosti:** [Landscape tipy: malování PCG dat](landscape-tipy.md#malovani-dat-paint-layers-ridi-pcg) · [Rejstřík: channel](../rejstrik.md#channel) · [Rejstřík: PCG](../rejstrik.md#pcg) · [Rejstřík: Nanite](../rejstrik.md#nanite)
