# PCG: základy a nástroje v editoru

**PCG** (Procedural Content Generation) dospěl: v UE 5.7 plugin opustil betu jako verze 1.0 a přibyl **PCG Mode** — režim editoru, kde se procedurální grafy kreslí přímo do světa splinou, štětcem nebo volumem. Tahle kapitola pokrývá základy ovládání: co nový režim umí a kde má hrany, jak postavit plot přes linear grammar, jak si napsat vlastní štětec se skutečným rozptylem a jak grafy ladit — výřezy podle kolizí, vizualizace atributů a print string. Malování PCG dat přes landscape vrstvy rozebírá [kapitola Landscape tipy](landscape-tipy.md#malovani-dat-paint-layers-ridi-pcg), spolupráci s novým terénem [Mesh Terrain](mesh-terrain.md#kanaly-v-praxi-material-malovani-a-pcg). Téma pokračuje [vegetací a lesem](pcg-vegetace.md), [liánami](pcg-liany.md) a [případovkou Hex-A-Gone](pcg-hexagone.md).

---

## PCG Mode: spline, paint a volume přímo v editoru

**Zdroj:** [How To Use the NEW UE5.7 PCG Mode, and Tips To Make It MORE Powerful!](https://www.youtube.com/watch?v=IPwVOhvQ2bo) · [Procedural Minds](https://www.youtube.com/channel/UCkfvcZJ6dGNUSCWOCVQnkXw) · ~23 min, tutoriál

**Shrnutí:** Do 5.7 znamenalo „nakreslit PCG splinu" vyrobit blueprint se spline komponentou a grafem. **PCG Mode** (nový selection mode vedle Landscape a Foliage) to obrací: vybereš nástroj, kreslíš do světa a aktor s grafem vznikne sám [(0:02)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=2s). Tři rodiny nástrojů — **spline, paint, volume** — a všechno, co nakreslíš, zůstává před potvrzením živé: meshe, váhy i sampling se ladí za běhu [(0:48)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=48s).

### Rozpad myšlenky

**Spline nástroje:** draw spline nabízí tři vestavěné grafy — spacing tool, linear grammar tool a spline mesh tool [(0:48)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=48s). Nakreslíš tah a dokud nezmáčkneš **Accept**, všechno se dá měnit: přidat druhý mesh, zvážit poměry výskytu, přepnout sampling z count na distance, randomizovat pozice [(1:35)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=95s) [(3:07)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=187s). Kreslí se free draw (default), tangent drag nebo closed spline; **draw spline surface** je totéž s vynucenou uzavřenou smyčkou pro nástroje samplující vnitřek plochy [(6:59)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=419s). Po Accept vznikne aktor se spline komponentou, PCG komponentou a hodnotami zapsanými jako **PCG parameter overrides** — panel nástroje jen zrcadlí exposed parametry grafu, včetně kategorií a clampů (v grafu se definují bohužel ručně psanými stringy) [(2:21)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=141s) [(4:40)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=280s).

**Víc splin v jednom grafu (workaround):** nové kreslení splinu **přepisuje** — PCG Mode ovládá vždy spline component s indexem 0. Trik: hotovou splinu zduplikuj (`Ctrl+D`; jméno „spline component" je rezervované, přejmenuj) a kresli dál — kopie zůstává [(4:40)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=280s) [(5:27)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=327s). Kopii pak edituješ přes **modeling mode → Draw Spline** s output mode „existing actor" a spline indexem 1; změna se v grafu projeví až po pohnutí aktorem [(6:13)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=373s).

**Raycast rules:** kam se body promítají — default landscape + meshe, PCG geometrie se ignoruje (odškrtnutelné); jde přidat vlastní pravidla po třídách, nebo promítání **omezit na konkrétní aktor** — kreslení PCG po povrchu jednoho meshe [(3:07)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=187s) [(3:54)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=234s).

**Vlastní graf jako nástroj:** v grafu s ničím nevybraným má detail panel sekci **Tool Data** — display name, tooltip, cílový actor a **compatible tool tags** [(8:31)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=511s). Tag určuje, pod kterým nástrojem se graf objeví, a jmenná konvence je mechanická: vezmi název režimu, zahoď „draw", slep bez mezer a přidej „tool" — `spline tool`, `spline surface tool`, `paint tool` [(9:17)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=557s). Vestavěné grafy needituj — jsou to engine content, dělej si kopie [(8:31)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=511s).

**Volume a jeho limity:** volume se kreslí od podlahy nahoru a před Accept nejde posouvat gizmem (QWER je vypnuté — jen přes outliner) [(19:26)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=1166s); výsledek je obyčejný PCG Volume bez možnosti připnout na aktor [(20:14)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=1214s). Chceš-li volume s event graphem, vytvoř blueprint child třídy **Location Volume** (brush volume podtřídu dělat nejde) a nastav ho v grafu volume nástroje [(21:00)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=1260s). Tvrdý limit: **jeden volume na graf** — na rozdíl od splin se duplikací obejít nedá; víc oblastí = vlastní blueprint s několika box kolizemi, ovšem bez kreslicího pohodlí [(21:46)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=1306s).

> **Pozn.:** PCG Mode je jen vstupní vrstva nad stejnými grafy, jaké znáš — všechno o samplování, filtrech a spawnerech platí dál, mode jen ruší povinnost stavět kolem grafu blueprint. Do PCG Mode se přepneš i zkratkou `Shift+9`. Verze: 5.7, plugin 1.0.

**Souvislosti:** [Landscape tipy: malování dat](landscape-tipy.md#malovani-dat-paint-layers-ridi-pcg) · [Mesh Terrain: kanály v praxi](mesh-terrain.md#kanaly-v-praxi-material-malovani-a-pcg) · [Rejstřík: PCG](../rejstrik.md#pcg) · [Rejstřík: PCG Mode](../rejstrik.md#pcg-mode) · [Rejstřík: spline](../rejstrik.md#spline)

---

## Paint tool pod kapotou: vzdálenost, bounds a vrstvy

**Zdroj:** [How To Use the NEW UE5.7 PCG Mode, and Tips To Make It MORE Powerful!](https://www.youtube.com/watch?v=IPwVOhvQ2bo) · [Procedural Minds](https://www.youtube.com/channel/UCkfvcZJ6dGNUSCWOCVQnkXw) · ~23 min, tutoriál

**Shrnutí:** Paint tool **není** foliage štětec, i když tak vypadá. Body neklade hustotou po ploše tahu, ale podle **minimum point spacing od posledního umístěného bodu** — široký štětec pořád maluje jednu čáru středem [(10:03)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=603s) [(10:50)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=650s). Velikost štětce ovlivňuje něco jiného: **bounds** bodů — a to se dá v grafu využít.

### Rozpad myšlenky

**Chování štětce:** spacing 300 znamená „300 jednotek od posledního bodu" — dvěma tahy klidně položíš body těsně vedle sebe [(10:50)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=650s). Pomůcka: nastav radius štětce na stejnou hodnotu jako spacing a kruh ti ukazuje, kde nejblíž může vzniknout další bod [(11:36)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=696s). Na rozdíl od splinu paint **přidává** — každý tah staví na předchozích [(17:05)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=1025s); `Shift` přepne na gumu, která jediná používá plnou plochu štětce [(12:22)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=742s).

**Radius = bounds:** body namalované větším štětcem mají větší bounds (debug: *display painted points wireframe bounds*) [(12:22)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=742s) — v grafu pak můžeš třeba škálovat meshe podle bounds a velikost štětce se stane kreativním ovladačem [(13:09)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=789s). Paint je zároveň **click mode**: červená čárka na kurzoru je forward axis, kolečkem myši bod rotuješ a **rotate yaw step size** (třeba 45°) z toho dělá zarovnávání do gridu; při tažení rotace nefunguje, celý tah míří stejně [(13:56)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=836s) [(14:44)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=884s).

**Odkud graf body bere:** uzel **Get Tool Data** — tool tag (`paint tool`) + jméno data instance [(15:31)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=931s). Víc instancí = vrstvy: vestavěný *layered place tool* má layer 0/1/2 plus **exclusion layer**, takže v jednom grafu maluješ kostky na vrstvu 0, koule na vrstvu 1 a gumuješ výřezovou vrstvou [(16:18)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=978s).

**Dvě pasti:** *(1)* Guma maže body na jejich **původní namalované pozici** — když graf body posune random transformem, gumuješ naslepo místo, kde bod býval; debug *show brush wireframe bounds* pomůže jen přibližně [(17:52)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=1072s) [(18:39)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=1119s). *(2)* `Ctrl+Z` neodvolá poslední tah, ale **zruší celý rozpracovaný nástroj** [(10:03)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=603s) [(18:39)](https://www.youtube.com/watch?v=IPwVOhvQ2bo&t=1119s).

> **Pozn.:** Autor sám říká, že by foliage chování (garantované rozestupy, malování plochou) uvítal — v 1.0 to engine nedává a musí se to dostavět grafem. Přesně to dělá [vlastní štětec se scatteringem](#opravdovy-stetec-scattering-vlastnim-grafem) o dvě myšlenky níž.

**Souvislosti:** [Vlastní štětec](#opravdovy-stetec-scattering-vlastnim-grafem) · [Rejstřík: PCG Mode](../rejstrik.md#pcg-mode) · [Rejstřík: bounds](../rejstrik.md#bounds)

---

## Plot za pár minut: spacing tool a linear grammar

**Zdroj:** [UE5.7 Just Upgraded PCG! Here's How to Use the New Editor Tools](https://www.youtube.com/watch?v=fjuCUJ1r-Wk) · [All things GAME!](https://www.youtube.com/channel/UChvuZHvrA6ZEBOOh5D0i3dw) · ~15 min, tutoriál

**Shrnutí:** Nejrychlejší praktická výhra PCG Mode: plot podél splinu. Spacing tool + vzdálenost odečtená z rozměru meshe = navazující dílce; **linear grammar tool** pak přidá rytmus — plaňka, sloupek, plaňka — zapsaný jako gramatika `[A,B]2 A3` [(9:51)](https://www.youtube.com/watch?v=fjuCUJ1r-Wk&t=591s).

### Rozpad myšlenky

**Plot přes spacing tool:** `Shift+9` do PCG Mode [(0:52)](https://www.youtube.com/watch?v=fjuCUJ1r-Wk&t=52s), draw spline, do spawning přidat mesh plotu [(1:38)](https://www.youtube.com/watch?v=fjuCUJ1r-Wk&t=98s), sampling přepnout na **distance** — a správná vzdálenost není odhad: otevři static mesh a opiš **rozměr podél osy X** (tady 334), dílce pak navazují beze spár [(2:51)](https://www.youtube.com/watch?v=fjuCUJ1r-Wk&t=171s) [(3:37)](https://www.youtube.com/watch?v=fjuCUJ1r-Wk&t=217s). Pozor: klik mimo bez Accept začne kreslit **další** splinu [(2:51)](https://www.youtube.com/watch?v=fjuCUJ1r-Wk&t=171s). Víc druhů dílců = další static mesh + **weight** pro poměr výskytu [(5:11)](https://www.youtube.com/watch?v=fjuCUJ1r-Wk&t=311s); špatně pivotovaný asset srovná **global position offset** a život dodá **random position offset** min/max [(5:30)](https://www.youtube.com/watch?v=fjuCUJ1r-Wk&t=330s), případně změna sampling seedu [(6:38)](https://www.youtube.com/watch?v=fjuCUJ1r-Wk&t=398s). Splinu jde editovat i po Accept — vybrat aktor v selection mode a tahat body [(7:26)](https://www.youtube.com/watch?v=fjuCUJ1r-Wk&t=446s). Hotový výsledek se dá **convert to static mesh / bake** a odpojit přes clear PCG link [(8:59)](https://www.youtube.com/watch?v=fjuCUJ1r-Wk&t=539s).

**Linear grammar:** v nástroji zapnout grammar a modules, každému modulu (mesh) přiřadit **symbol** — plaňka `A`, sloupek `B` [(9:51)](https://www.youtube.com/watch?v=fjuCUJ1r-Wk&t=591s) [(10:39)](https://www.youtube.com/watch?v=fjuCUJ1r-Wk&t=639s). Gramatika je string, který se čte podél splinu:

- `A` — jeden modul; `A3` — přesně třikrát [(13:33)](https://www.youtube.com/watch?v=fjuCUJ1r-Wk&t=813s)
- `[A,B]` — sekvence (plaňka a sloupek); `[A,B]2` — sekvence dvakrát [(11:29)](https://www.youtube.com/watch?v=fjuCUJ1r-Wk&t=689s) [(13:07)](https://www.youtube.com/watch?v=fjuCUJ1r-Wk&t=787s)
- `*` — opakuj do vyplnění délky splinu; `+` — podobně, s roztažením modulů, aby délka vyšla přesně [(12:21)](https://www.youtube.com/watch?v=fjuCUJ1r-Wk&t=741s) [(13:07)](https://www.youtube.com/watch?v=fjuCUJ1r-Wk&t=787s)

Složením vzniknou rytmy jako `[A,B]2 A3 B*` — dvakrát pár, tři plaňky, sloupky do konce [(14:17)](https://www.youtube.com/watch?v=fjuCUJ1r-Wk&t=857s) — užitečné pro zdi s branami a opakující se moduly [(12:21)](https://www.youtube.com/watch?v=fjuCUJ1r-Wk&t=741s).

> **Pozn.:** Video je průzkum naživo — autor syntaxi zkouší a některé pokusy nevyjdou napoprvé, což je samo o sobě poučné (chování `*` vs. `+` odhaluje experimentem). Pro produkční použití si gramatiku ověř v oficiální dokumentaci PCG; tady je vidět hlavně to, jak málo stojí plot, který by ručně zabral odpoledne.

**Souvislosti:** [PCG Mode: nástroje](#pcg-mode-spline-paint-a-volume-primo-v-editoru) · [Rejstřík: linear grammar](../rejstrik.md#linear-grammar) · [Rejstřík: spline](../rejstrik.md#spline)

---

## Opravdový štětec: scattering vlastním grafem

**Zdroj:** [Add Scattering To The PCG Mode Brush To Simulate Actual Painting](https://www.youtube.com/watch?v=AYulmKtqhLM) · [Procedural Minds](https://www.youtube.com/channel/UCkfvcZJ6dGNUSCWOCVQnkXw) · ~24 min, tutoriál

**Shrnutí:** Náprava největší slabiny paint toolu: graf, který kolem každého namalovaného bodu vygeneruje grid v **plné velikosti a tvaru štětce**, takže tah skutečně maluje plochu — les štětcem, s volitelným pruningem proti překryvům [(0:02)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=2s). Cestou ukazuje obecný vzor: **jakýkoli graf se dá zaregistrovat jako nástroj** přes Tool Data.

### Rozpad myšlenky

**Registrace štětce:** prázdný PCG graf, v Tool Data vyplnit display name, tool tab a compatible tool tags = `paint tool`, zapnout *enabled as preset* — a graf se objeví mezi paint nástroji [(0:49)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=49s) [(1:35)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=95s). Body tahu dodá **Get Tool Data** — dvě data instances (`square brush`, `circle brush`) pro dva tvary štětce, rozvedené přes named reroute declarations [(2:21)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=141s) [(3:08)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=188s). Co v bodech je: pozice, rotace z projekce na povrch, scale 1, **bounds podle velikosti štětce** a density 1 — density jde zvyšovat parametrem strength, takže „malování hustoty" je taky na stole [(3:55)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=235s) [(4:41)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=281s). A ergonomie: náhled nástroje resetuj **reset tlačítkem u data instance**, ne `Ctrl+Z` — ten zahodí celý rozdělaný setup [(3:55)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=235s).

**Jádro grafu — grid na každý bod tahu:** ze **Set Attribute** ulož extents bodu jako atribut `radius` [(4:41)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=281s) a přidej graph parameter `point spacing` [(5:27)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=327s). Protože každý tah může mít jinou velikost štětce, generování běží v **loop subgrafu** (drag grafu do plátna → create loop node; vstupní pin přepnout na loop/required/any) [(7:00)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=420s), před nímž **Attribute Partition** podle `radius` rozdělí body na skupiny stejné velikosti [(7:46)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=466s). Uvnitř smyčky: **Get Attribute From Point Index** vytáhne radius a spacing [(8:32)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=512s), `radius.Z` se zploští na 1 („chceme palačinku") [(9:18)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=558s), **Create Point Grid** (extents = radius, cell size = spacing) vyrobí mřížku a **Copy Points** ji nakopíruje na původní body tahu [(9:18)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=558s). Box štětec tím je hotový [(10:04)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=604s).

**Kruhový štětec = filtr vzdáleností:** stejný řetěz + **Distance (spatial)** uzel — pozor, ne stejnojmenná vector operace [(10:51)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=651s) [(11:38)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=698s) — měří vzdálenost gridu od středů tahu. Hodnoty vycházejí záporné, proto **Absolute**, pak **Attribute Filter** proti `radius.x` — a protože absolute hodnoty otočil, patří tam **greater or equal**, ne intuitivní less [(11:38)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=698s) [(13:10)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=790s). Warning „threshold point data doesn't have the same number of elements" řeší **Merge Points** před filtrem [(12:24)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=744s); error „attribute radius not found" při ladění jen říká, že daným štětcem jsi ještě nic nenamaloval [(10:51)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=651s).

**Z prototypu nástroj — parametry:** pole **meshes to spawn** → **Match and Set Attributes** → spawner s mesh selector *by attribute* [(13:56)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=836s) [(20:05)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=1205s); bool **prune overlapping** → branch → Merge (kruhové + hranaté body dohromady) + **Self Pruning**, kde bounds = spacing znamená „nikdy blíž než X" — foliage garance rozestupů checkboxem [(14:42)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=882s) [(19:19)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=1159s). Offsety elegantně: **global transform + random min/max jako tři transform parametry** (místo šesti vektorů) rozbité přes **Break Transform Attribute** do Transform Points; k tomu booly uniform scaling a absolute rotation — ta drží stromy svisle i na svahu [(15:28)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=928s) [(16:14)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=974s) [(23:10)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=1390s). Drobnost: slider rotace nejde do 360 — zadává se −180 až 180, výsledek je stejný [(17:46)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=1066s).

**Debug proti slepé gumě:** bool `debug original points` → branch → **Bounds Modifier** se Z protaženým na 5000 → Debug uzel: původní body tahu svítí jako **sloupy** viditelné přes koruny stromů, takže víš, kam s gumou i po divokých offsetech [(21:37)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=1297s) [(22:24)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=1344s).

> **Pozn.:** Kategorie parametrů mají UX past: název kategorie potvrď kliknutím jinam, `Enter` vloží nový řádek [(5:27)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=327s); rychlejší je hotové parametry do kategorií rovnou přetahovat myší [(14:42)](https://www.youtube.com/watch?v=AYulmKtqhLM&t=882s). Celý recept je zároveň šablona: „štětec" je jen graf s tool tagem — stejným postupem si zabalíš rozhazovač kamení, odpadků nebo nepřátelských spawnů.

**Souvislosti:** [Paint tool pod kapotou](#paint-tool-pod-kapotou-vzdalenost-bounds-a-vrstvy) · [Rejstřík: self pruning](../rejstrik.md#self-pruning) · [Rejstřík: PCG Mode](../rejstrik.md#pcg-mode)

---

## Výřezy podle kolizí a debug grafu

**Zdroj:** [Precise Cutouts Using Collisions in UE5 PCG, And More Tips and Tricks](https://www.youtube.com/watch?v=-G14-4m4-LA) · [Procedural Minds](https://www.youtube.com/channel/UCkfvcZJ6dGNUSCWOCVQnkXw) · ~16 min, tipy

**Shrnutí:** **Difference** uzel vyřezává podle bounds bodů — kolem stromu zmizí čtverec trávy, ne kruh kmene. Jediný uzel to spraví: **Create Collision Data** za spawnerem pošle do Difference skutečné kolizní tvary a výřez najednou kopíruje konturu meshe [(0:01)](https://www.youtube.com/watch?v=-G14-4m4-LA&t=1s) [(3:54)](https://www.youtube.com/watch?v=-G14-4m4-LA&t=234s). K tomu kolizní self pruning a dva debug uzly, které šetří hodiny.

### Rozpad myšlenky

**Demo scéna:** Create Points Grid 4000×4000, cell size 50 [(0:48)](https://www.youtube.com/watch?v=-G14-4m4-LA&t=48s); pole `meshes` (strom, balvan) → Match and Set Attributes → spawner *by attribute* [(1:35)](https://www.youtube.com/watch?v=-G14-4m4-LA&t=95s); Select Points 0.05 prořeže na pár kusů a Transform Points dodá offsety, rotaci a scale [(2:21)](https://www.youtube.com/watch?v=-G14-4m4-LA&t=141s). Tráva se pak spawnuje na původní grid **minus** okolí stromů: Difference v binary režimu [(3:08)](https://www.youtube.com/watch?v=-G14-4m4-LA&t=188s) — jenže s bounds jako vstupem zejí kolem všeho obří mrtvé zóny [(3:54)](https://www.youtube.com/watch?v=-G14-4m4-LA&t=234s).

**Create Collision Data:** vlož ho mezi spawner a Difference a vyřezává se podle kolize — u válce kruh, u kamene jeho obrys [(3:54)](https://www.youtube.com/watch?v=-G14-4m4-LA&t=234s). Dvě dolaďovačky: **Bounds Modifier ~0,5** před Match and Set Attributes zmenší bodům bounds, aby tráva mohla až ke kmeni (0,4 vs. 0,5 znatelně mění, co se kam vejde) [(4:40)](https://www.youtube.com/watch?v=-G14-4m4-LA&t=280s) [(5:26)](https://www.youtube.com/watch?v=-G14-4m4-LA&t=326s), a **pořadí operací**: random offsety trávy dělej **před** Difference, jinak se vyřezává na neposunutých pozicích [(5:26)](https://www.youtube.com/watch?v=-G14-4m4-LA&t=326s). Cena: kolize jsou výpočetně dražší než body — pro editor-time generování jedno, u runtime PCG s nimi šetři [(6:12)](https://www.youtube.com/watch?v=-G14-4m4-LA&t=372s).

**Self pruning podle kolizí:** klasika „bounds from mesh" u pruningu selhává — koruna stromu má obří bounds, takže pruning zabíjí i kameny daleko od kmene [(7:00)](https://www.youtube.com/watch?v=-G14-4m4-LA&t=420s) [(7:47)](https://www.youtube.com/watch?v=-G14-4m4-LA&t=467s). Self Pruning má **use collision attribute** (atribut = `meshes`) — a nezdokumentovanou past: bere **menší** z bounds vs. kolize. Řešení silou: Bounds Modifier ×100 nafoukne bounds do absurdna, takže vždy vyhraje kolize [(7:47)](https://www.youtube.com/watch?v=-G14-4m4-LA&t=467s) [(8:33)](https://www.youtube.com/watch?v=-G14-4m4-LA&t=513s). Výsledek: kameny těsně u kmenů, které dřív pruning nedovolil, a hustší scéna při férovém odstupu (srovnání 204 vs. 226 entries) [(8:33)](https://www.youtube.com/watch?v=-G14-4m4-LA&t=513s) [(9:19)](https://www.youtube.com/watch?v=-G14-4m4-LA&t=559s). Náhled kolizních tvarů: `A` na **Create Collision Data** uzlu — data viewport je vykreslí (na self pruningu náhled nefunguje) [(10:06)](https://www.youtube.com/watch?v=-G14-4m4-LA&t=606s).

**Debug Visualize Attribute:** uzel, který hodnoty atributu **vypíše do světa** nad body — volíš atribut (mesh path, position…), prefix, index, barvu a **duration**: „ukaž mi hodnoty 5 s po Generate a zmiz" [(10:52)](https://www.youtube.com/watch?v=-G14-4m4-LA&t=652s) [(11:38)](https://www.youtube.com/watch?v=-G14-4m4-LA&t=698s). Typický workflow: zobrazit pozice, najít zlobící bod, odečíst hodnotu a postavit podle ní filtr; `E` uzel zapíná/vypíná [(12:25)](https://www.youtube.com/watch?v=-G14-4m4-LA&t=745s).

**PCG Print String:** runtime odpověď na „generuje se to vůbec?" — vlastní text nebo atribut, print to screen, per component, **verbosity** log/warning/error (error svítí červeně v output logu) [(13:12)](https://www.youtube.com/watch?v=-G14-4m4-LA&t=792s) [(14:44)](https://www.youtube.com/watch?v=-G14-4m4-LA&t=884s). Past na pochopení: string se tiskne **jen když graf generuje** — komponenta vygenerovaná v editoru při Play negeneruje znovu (generate on load nemá co dělat), takže ticho neznamená rozbitý graf; po Cleanup a simulate (`Alt+S`) se print objeví [(13:58)](https://www.youtube.com/watch?v=-G14-4m4-LA&t=838s) [(14:44)](https://www.youtube.com/watch?v=-G14-4m4-LA&t=884s). Základní duo pořád platí: `A` = point data v inspektoru, `D` = debug bodů ve viewportu [(15:30)](https://www.youtube.com/watch?v=-G14-4m4-LA&t=930s).

> **Pozn.:** Create Collision Data + Difference je obecný vzor „respektuj, co už stojí" — stejně vyřízneš trávu kolem ručně postavených budov nebo cest. A dvojice debug uzlů řeší dva různé světy: Visualize Attribute pro editor (co graf spočítal), Print String pro runtime (jestli vůbec běžel).

**Souvislosti:** [Instanced Actors](instanced-actors.md) · [Rejstřík: self pruning](../rejstrik.md#self-pruning) · [Rejstřík: PCG](../rejstrik.md#pcg)
