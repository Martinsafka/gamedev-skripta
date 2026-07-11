# Nástroje: EasyWaterscape a lekce o vodě v UE

Produktové video k placenému nástroji — ale od Williama Fauchera, takže z něj kape víc obecného poučení o vodě v Unrealu než z leckterého tutoriálu: proč pěna vzniká z choppiness, kdy Single Layer Water nestačí, proč voda vypadá rozmazaně (TSR) a kterými dvěma pákami se ladí výkon. Kapitola má dvě části: co nástroj umí (kontext pro případný nákup) a lekce přenositelné kamkoli.

---

## EasyWaterscape: jak je poskládaný dobrý vodní nástroj

**Zdroj:** [Introducing EasyWaterscape for Unreal Engine 5](https://www.youtube.com/watch?v=dXuwb4PpodQ) · [William Faucher](https://www.youtube.com/channel/UCGKjGGjdl-GzEcFPf1EQwqw) · ~25 min, produktové video (placený nástroj na Fab)

**Shrnutí:** Tile-free oceán řízený z jednoho blueprintu: presety, 5 LOD meshů (0–1 pro cinematiku, 2–4 pro hry) [(2:45)](https://www.youtube.com/watch?v=dXuwb4PpodQ&t=165s), **fyzikálně motivovaná pěna** (vzniká lámáním strmých vln, ne náhodným spawnem) [(6:36)](https://www.youtube.com/watch?v=dXuwb4PpodQ&t=396s), automatický **Coast Maker** pro pobřeží a tři úrovně buoyancy. Zajímavé i jako ukázka, jak se navrhuje nástroj pro lidi.

### Rozpad myšlenky

**Vlny:** wind speed a fetch = velikost a energie vln; **wave directionality** 0,75–0,95 mění omnidirectional „bublání" v přirozené směrové vlny (+ wave spread pro dlouhé rovné hřebeny) [(5:04)](https://www.youtube.com/watch?v=dXuwb4PpodQ&t=304s). **Patch size** = zachycená plocha oceánu: menší patch = detailnější vlny, ale tiling — tile breaking (offset −500, blend 1500) ho maskuje [(5:50)](https://www.youtube.com/watch?v=dXuwb4PpodQ&t=350s). **Pěna z choppiness**: strmá vlna se zlomí a uvězní vzduch — proto ji řídí choppiness a dolaďuje threshold/decay/smoothing [(7:22)](https://www.youtube.com/watch?v=dXuwb4PpodQ&t=442s). Navrch tři vrstvy proti opakování: swells (velké vlny v dálce), currents (vířivý noise vzor) a wind gusts [(13:33)](https://www.youtube.com/watch?v=dXuwb4PpodQ&t=813s).

**Coast Maker:** bounding box zachytí pevninu, vygeneruje mapy pobřeží a přidá vlny + pěnu kolem břehů; běží **jednou při startu** — po startu nulový dopad na výkon [(9:41)](https://www.youtube.com/watch?v=dXuwb4PpodQ&t=581s). Detaily promyšlené k praxi: **windward mask** (vlny jen ze směru větru — závětrná strana ostrova je klidná) [(11:59)](https://www.youtube.com/watch?v=dXuwb4PpodQ&t=719s), capture height pro [Mesh Terrain](mesh-terrain.md) převisy z 5.8 [(11:13)](https://www.youtube.com/watch?v=dXuwb4PpodQ&t=673s) a `Hidden in Scene Capture` pro meshe, kolem kterých pěna být nemá.

**Buoyancy třikrát** [(14:21)](https://www.youtube.com/watch?v=dXuwb4PpodQ&t=861s): material function do World Position Offsetu (fake, levné, pozadí), **Niagara blueprint** (GPU, hejno trosek — default volba) a blueprint komponenta pro hero objekty s logikou [(15:08)](https://www.youtube.com/watch?v=dXuwb4PpodQ&t=908s).

> **Pozn.:** Dvě věci k ocenění nad rámec vody. Poctivost: Faucher sám říká, že **lámání vln na plážích je nejslabší část nástroje** a že nástroj září u útesů [(11:59)](https://www.youtube.com/watch?v=dXuwb4PpodQ&t=719s) — prodejní video, které přizná slabinu, je vodítko k důvěryhodnosti tvůrce (viz [co prodává](../teorie/co-prodava.md)). A UX detail: každá proměnná má tooltip a workflow past „aktivní preset zamyká nastavení" je řešená viditelným tlačítkem [(3:31)](https://www.youtube.com/watch?v=dXuwb4PpodQ&t=211s) — stejný princip jako naše dvouvrstvá [rejstříková](../rejstrik.md) konvence: vysvětlení má být tam, kde vzniká otázka.

**Souvislosti:** [Voda a buoyancy](voda-a-buoyancy.md) · [Mesh Terrain](mesh-terrain.md) · [Rejstřík: buoyancy](../rejstrik.md#buoyancy)

---

## Přenositelné lekce: Single Layer Water, TSR a výkonové páky

**Zdroj:** [Introducing EasyWaterscape for Unreal Engine 5](https://www.youtube.com/watch?v=dXuwb4PpodQ) · [William Faucher](https://www.youtube.com/channel/UCGKjGGjdl-GzEcFPf1EQwqw) · troubleshooting části

**Shrnutí:** Čtyři lekce, které platí pro *jakoukoli* vodu v UE: **Single Layer Water** shading model má limit se stíny; rozmazaná voda je skoro vždycky vina **upscalingu (TSR)**, ne vody; výkon se ladí **frame ratem a rozlišením simulace**; a pro cinematiku musí voda tikat 5–10× rychleji, než renderuješ.

### Rozpad myšlenky

**Single Layer Water a jeho strop** [(17:28)](https://www.youtube.com/watch?v=dXuwb4PpodQ&t=1048s): standard pro vodu v UE — translucence a kaustika za rozumnou cenu. Háček: **stíny přijímá jen z primárního directional lightu**. Scéna nasvícená spotlightem (dramatická noční zátoka) se rozpadne — voda stín nevrhne ani nepřijme. Řešení: přepnout material instance na **Default Lit** (+ metallic 1 pro tmavou hlubokou vodu) tam, kde translucenci nepotřebuješ [(18:14)](https://www.youtube.com/watch?v=dXuwb4PpodQ&t=1094s) — žádný z modelů není „lepší", volí se per záběr.

**Rozmazaná voda = TSR, ne voda** [(21:21)](https://www.youtube.com/watch?v=dXuwb4PpodQ&t=1281s): viewport typicky běží na 80–90 % screen percentage a upscaler (Temporal Super Resolution) detailní pohyblivou hladinu rozmaže a „ghostuje". Diagnóza: nastav 100 % (nebo 125–200 %) a porovnej. Léčba pro hry: jiná AA metoda přes console variable a/nebo tonemapper sharpen 0,5–1 [(22:07)](https://www.youtube.com/watch?v=dXuwb4PpodQ&t=1327s). Bottom line: **vyhni se upscalingu, kde můžeš** — platí pro jakýkoli jemný pohyblivý detail, ne jen vodu.

**Výkon = dvě páky** [(19:00)](https://www.youtube.com/watch?v=dXuwb4PpodQ&t=1140s): frame rate simulace (překvapivě nízko — 10–15 fps stačí pro záběry z výšky) a rozlišení (4K je overkill; 256–2048 pracovní rozsah). Plus úklid: vypnout underwater/two-sided/foam, když nejsou potřeba [(19:47)](https://www.youtube.com/watch?v=dXuwb4PpodQ&t=1187s). A Lumen bez screen traces dělá na displaced hladině černé artefakty — fix posunem výšky nad nulu [(20:34)](https://www.youtube.com/watch?v=dXuwb4PpodQ&t=1234s).

**Cinematika:** frame rate vody nastav na **5–10× renderovaných fps** — jinak nejsou mezisnímky pro motion blur a vlny „cvakají" [(22:07)](https://www.youtube.com/watch?v=dXuwb4PpodQ&t=1327s).

> **Pozn.:** Bonusová meta-lekce: k panice kolem „Blueprinty budou deprecated po UE6" Faucher střízlivě: launch UE6 2–3 roky daleko, deprecace až po dozrání nového frameworku, s migračními nástroji — Blueprint znalosti mají před sebou ~5 let relevance minimálně [(23:40)](https://www.youtube.com/watch?v=dXuwb4PpodQ&t=1420s). Dobrý rámec pro každou „engine mění základy" zprávu (viz [Mover](mover.md): CMC taky nikam neodešel).

**Souvislosti:** [Rejstřík: Single Layer Water](../rejstrik.md#single-layer-water) · [Rejstřík: TSR](../rejstrik.md#tsr) · [Mover: „CMC nikam neodchází"](mover.md#proc-mover-existuje-modularita-vstupy-a-dve-sitove-vetve)
