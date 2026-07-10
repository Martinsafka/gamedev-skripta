# Praxe v UE5

Konkrétní postupy, systémy a vzory v Unreal Enginu 5 — od drobných editor tipů po hluboké ponory do celých subsystémů. Kapitoly uvádějí verzi enginu tam, kde na ní záleží; UE se vyvíjí rychle a některé systémy (zvlášť ty v beta stavu) se mezi verzemi mění.

Témata a kapitoly:

**Blueprint architektura a organizace projektu**

- **[Principy architektury](principy-architektury.md)** — dědičnost a test „is it a?", tři principy škálovatelnosti (separace, volné vazby, data) a kde co v UE bydlí.
- **[Komunikace Blueprintů](komunikace-blueprintu.md)** — cast, interface, event dispatcher a broadcast kanály: kdo na kom závisí a kdy který použít.
- **[Interakce bez Event Ticku](interakce-bez-event-ticku.md)** — event-driven interakční systém: overlap trigger, Blueprint Interface, tagy a validated gets.
- **[Gameplay Tags](gameplay-tags.md)** — hierarchický stav místo booleanové špagety: tag manager komponenta, dotazy bez skrytých bugů, pojmenování.
- **[Organizace projektu](organizace-projektu.md)** — Content Browser podle Epicu (feature foldery, redirectory, 260znakový limit) a devět tipů proti špagetám v grafech.
- **[Levely a streaming](levely-a-streaming.md)** — proč Open Level zamrzá, level streaming s persistent levelem a breakdown, jak loading schovává Resident Evil Requiem.
- **[Ukládání](ukladani.md)** — SaveGame objekty, sloty a vzor Game Instance + function library pro save dostupný odkudkoli.
- **[Telemetrie](telemetrie.md)** — activity tracker z gameplay tagů a vzdálená analytika (TrackEdge + PostHog).

**Motion Matching a GASP**

- **[Motion Matching základy](mm-zaklady.md)** — dotaz místo grafu stavů: trajektorie, databáze, schema a chooser; setup od nuly, sparse set (13 animací stačí) a procedurální uzly.
- **[Systémy nad MM](mm-systemy.md)** — combat přes montáže a choosery, traversal a cover komponenty se state managerem, a nescriptované interakce z Witcher 4 dema.
- **[GASP: Game Animation Sample](gasp.md)** — anatomie Epicova vzorového projektu: capsule-driven autoring animací, řízení výběru, traversal pod kapotou, Mover, NPC přes State Tree, Control Rig vrstva a zbraně přes overlay.

**Pohyb postavy (locomotion)**

- **[Základy pohybu](pohyb-zaklady.md)** — gaity přes Max Walk Speed a blend spacy, podřep a plazení, rychlost podle sklonu, nabíjený skok s křivkou a zastavení u zdi à la RE9.
- **[Parkour postaru](parkour-vault.md)** — vault a výlez přes tři trace s root motion montážemi; ledge grab se zarovnáním na libovolný mesh přes Get Actor Bounds.
- **[Mover](mover.md)** — proč nahrazuje CMC: modulární movement modes, layered moves, replikace vstupů, dvě síťové větve; setup od nuly v 5.7 a oprava strafu na osm směrů.

**AI a chování NPC**

- **[Základy nepřátelské AI](ai-zaklady.md)** — minimální nepřítel (Pawn Sensing + AI MoveTo + nav mesh), patrola náhodně i po waypointech, chase se ztrátou zájmu, a totéž přes AI Controller + Behavior Tree + Blackboard.
- **[AI vnímání](ai-vnimani.md)** — Pawn Sensing vs. AI Perception vs. trigger; kužel zraku, object permanence, lose sight radius a přesný timing ztráty zájmu.
- **[State Trees](state-trees.md)** — kompletní nepřítel: patrola po spline, tři smysly jedné percepce, Report eventy, přechody přes gameplay tagy a event dispatchery.

**Terén a krajina**

- **[Mesh Terrain (UE 5.8)](mesh-terrain.md)** — nový terénní systém: partitioned Nanite mesh, nedestruktivní modifier stack, channels.

**Editor a workflow**

- **[Tipy do editoru](editor-tipy.md)** — drobné triky, které šetří minuty každý den.
