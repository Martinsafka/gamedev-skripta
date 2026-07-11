# Voda a buoyancy: Water plugin od jezera po loďku

Vestavěný Water plugin dá oceán, jezero i řeku za pár kliknutí — a s nimi tři věci, které je potřeba umět: **tvarovat vodní tělesa splinami** (a srovnat je s terénem), **nechat věci plavat** postaru přes pontoony a nově (5.7) přes physical material. Interaktivní vlnky řeší [navazující kapitola](interaktivni-voda.md); vor, který se houpe pod nohama, už umí [Physics Control](lana-kabely.md#physics-control-vor-ktery-se-houpe-pod-nohama).

---

## Vodní tělesa: spliny, napojení na terén a řeka s proudem

**Zdroj:** [How To Enable Water Interaction - Unreal Engine 5 Tutorial](https://www.youtube.com/watch?v=EUbSj2hEMCE) · [Pitchfork Academy](https://www.youtube.com/channel/UCXp4W8jzNe280dGy_IvKX4Q) · ~11 min, část o water bodies ·
[How To Make Interactive Water Simulation (Just Like The Witcher 4)](https://www.youtube.com/watch?v=kkwXxeys8JE) · [MakeCodeSimple_Unreal](https://www.youtube.com/channel/UCshQIu-qsu9rDqTqK6X2GHQ) · ~7 min

**Shrnutí:** Water plugin (stále experimental — editor tě varuje) přidává **Water Body** actory: ocean, lake, river, island [(3:56)](https://www.youtube.com/watch?v=EUbSj2hEMCE&t=236s). Všechna tělesa se tvarují splinami, umí se propojit (jezero → řeka → oceán) a řeka má **rychlost proudu per spline point**. Většina „proč to vypadá divně" problémů je o vztahu vody a landscapu.

### Rozpad myšlenky

**Tvarování:** po vložení oceánu vynulovat location (spawne se s divnou hodnotou) [(3:56)](https://www.youtube.com/watch?v=EUbSj2hEMCE&t=236s); klávesa `G` zobrazí spline pointy, right-click na bodě → Add Spline Point, úchyty tangent dělají hladké křivky [(4:42)](https://www.youtube.com/watch?v=EUbSj2hEMCE&t=282s). U řeky nové body přidává `Alt` + tažení posledního bodu [(9:04)](https://www.youtube.com/watch?v=EUbSj2hEMCE&t=544s) a **velocity per point** zrychlí proud třeba jen v zákrutě (512 v ohybu, jinde default) [(9:51)](https://www.youtube.com/watch?v=EUbSj2hEMCE&t=591s).

**Voda × landscape — tři opravy:**

1. Artefakty Niagara simulace kolem terénu → **landscape posunout 1 cm nad nulu**, ať nesedí přesně na hladině [(6:15)](https://www.youtube.com/watch?v=EUbSj2hEMCE&t=375s). Obecně: voda kousek *pod* úrovní terénu [(1:22)](https://www.youtube.com/watch?v=kkwXxeys8JE&t=82s).
2. „Hřeben" podél pobřeží → na water body **Water Heightmap Settings → Falloff Mode: Angle → Width** [(6:15)](https://www.youtube.com/watch?v=EUbSj2hEMCE&t=375s).
3. Sculpting se u vody „zasekává" → **Edge Offset** a **Channel Edge Offset** na 0 přitáhnou terén až k vodě [(7:02)](https://www.youtube.com/watch?v=EUbSj2hEMCE&t=422s), [(7:49)](https://www.youtube.com/watch?v=EUbSj2hEMCE&t=469s) — pak jde vymodelovat pláž i kopce u břehu.

**Zadarmo navrch:** waterline efekt při přechodu kamery hladinou a vestavěný podvodní post-process volume [(5:29)](https://www.youtube.com/watch?v=EUbSj2hEMCE&t=329s).

> **Pozn.:** Water bodies žijí ve vlastním edit layeru landscapu, takže jdou vypínat. Pro naši vesnici u vody je sekvence z videa (jezero → řeka se zákrutami → oceán) prakticky hotový recept — a rychlost proudu per point je nenápadný nástroj level designu: proud říká, kudy se dá plavat.

**Souvislosti:** [Interaktivní voda](interaktivni-voda.md) · [Rejstřík: water body](../rejstrik.md#water-body) · [Mesh Terrain](mesh-terrain.md)

---

## Buoyancy postaru: pontoony

**Zdroj:** [How to Make a Boat Float in Unreal Engine 5 - Buoyancy Tutorial](https://www.youtube.com/watch?v=KwPnb8CglDY) · [Gorka Games](https://www.youtube.com/channel/UCv_n9oioNF6OpzR2dt6E4xg) · ~7 min ·
[Unreal Engine 5 Floating objects a.k.a. Buoyancy](https://www.youtube.com/watch?v=Wg3lP8zW3HI) · [ArtFX 3D](https://www.youtube.com/channel/UCnZiHmQm8zX7zN1IKxt3lBg) · ~3 min

**Shrnutí:** Klasická cesta (5.0–5.6): **Buoyancy komponenta** s **pontoony** — body, ve kterých na těleso působí vztlak. Loď = čtyři pontoony v rozích; kachnička = čtyři body kolem těžiště. Nejrychlejší start: zkopírovat hotový **BP_BuoyancyExample** z obsahu pluginu a vyměnit mesh.

### Rozpad myšlenky

**Vlastní blueprint (Gorka):** static mesh lodi jako **root** (jinak se fyzika a komponenty rozjedou), `Simulate Physics`, a start **nad hladinou** — objekt začínající přesně na hladině nevyplave [(1:36)](https://www.youtube.com/watch?v=KwPnb8CglDY&t=96s). Buoyancy komponenta → Pontoons pole; šikovný workflow: čtyři **arrow komponenty** jako viditelné markery rohů, jejich lokace zkopírovat do pontoonů [(3:09)](https://www.youtube.com/watch?v=KwPnb8CglDY&t=189s). Ladění: pontoony posazené výš (~30) = loď sedí víc na hladině [(5:28)](https://www.youtube.com/watch?v=KwPnb8CglDY&t=328s). Pozor u jeho staršího postupu: kolize oceánu přepnutá na overlap [(0:49)](https://www.youtube.com/watch?v=KwPnb8CglDY&t=49s).

**Hotový příklad (ArtFX 3D):** Engine content → Plugins → **Water Content → Blueprints → BP_BuoyancyExample** → zkopírovat do projektu, vyměnit static mesh, upravit mass (~150 pro kachničku) [(0:49)](https://www.youtube.com/watch?v=Wg3lP8zW3HI&t=49s); pro větší lodě přidat pontoonů víc [(1:37)](https://www.youtube.com/watch?v=Wg3lP8zW3HI&t=97s). A klenot na závěr: **`r.water.debug.buoyancy 1`** vykreslí pontoony jako koule přímo ve hře [(0:03)](https://www.youtube.com/watch?v=Wg3lP8zW3HI&t=3s) — ladění vztlaku naslepo je jinak loterie.

> **Pozn.:** Pontoony jsou aproximace: víc bodů = stabilnější, ale dražší chování. Pro rekvizity stačí 4; u lodě, na které se stojí, počítej s laděním dampingu, jinak „tancuje" (Gorka to poctivě ukazuje). A nezapomeň, že tahle cesta je v 5.7 z velké části nahrazená — viz další myšlenka.

**Souvislosti:** [Rejstřík: buoyancy](../rejstrik.md#buoyancy) · [Kabely, lana a Physics Control: vor](lana-kabely.md#physics-control-vor-ktery-se-houpe-pod-nohama)

---

## Buoyancy v 5.7: physical material místo pontoonů

**Zdroj:** [FIX Water Buoyancy in Unreal Engine 5 (EASY METHOD)](https://www.youtube.com/watch?v=JgWaK3OYqg4) · [World Of VFX](https://www.youtube.com/channel/UCWP2AikFs8LlH0ajpnQiT7w) · ~2 min ·
[Unreal Engine 5.7 - Buoyancy in Shallow Water - Quick Tip](https://www.youtube.com/watch?v=qeG0OxBFwzk) · [Unreal - X - Tutorials](https://www.youtube.com/channel/UCjKg7gsHCEyXtJbZYx2Xu7A) · ~2 min

**Shrnutí:** Od 5.7 plave mesh **bez pontoonů**: `Simulate Physics` + **Physical Material Override → Default Buoyancy Physics Material** [(0:47)](https://www.youtube.com/watch?v=JgWaK3OYqg4&t=47s). Druhá půlka nastavení je na vodním tělese: collision preset **Custom**, Collision Enabled → **Query and Probe**, Physics Body → **Block** [(1:33)](https://www.youtube.com/watch?v=JgWaK3OYqg4&t=93s).

### Rozpad myšlenky

Nový režim „Probe" v kolizích je to, co vztlak pohání — voda se dotazuje fyzikálních těles bez plné kolizní odezvy. Stejný postup funguje pro oceán i **shallow water river** [(0:02)](https://www.youtube.com/watch?v=qeG0OxBFwzk&t=2s) — předměty plavou po proudu řeky. Doladění už je klasika rigid body fyziky: mass, damping a **center of mass** v physics sekci meshe [(1:17)](https://www.youtube.com/watch?v=qeG0OxBFwzk&t=77s).

> **Pozn.:** Dvě cesty vedle sebe = verzní checklist: na 5.6 a starších pontoony, na 5.7+ physical material (a pontoonová cesta zůstává pro jemnou kontrolu — loď se stabilními body vztlaku). Kdo přechází mezi verzemi, tohle je přesně místo, kde se „nefunkční voda" opravuje dvěma checkboxy.

**Souvislosti:** [Rejstřík: buoyancy](../rejstrik.md#buoyancy) · [Rejstřík: physical material](../rejstrik.md#physical-material) · [Kroky a povrchy: physical materials](footsteps.md#physical-materials-a-trace-misto-notify)
