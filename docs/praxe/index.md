# Praxe v UE5

Konkrétní postupy, systémy a vzory v Unreal Enginu 5 — od drobných editor tipů po hluboké ponory do celých subsystémů. Kapitoly uvádějí verzi enginu tam, kde na ní záleží; UE se vyvíjí rychle a některé systémy (zvlášť ty v beta stavu) se mezi verzemi mění.

Témata a kapitoly:

**Blueprint architektura a organizace projektu**

- **[Principy architektury](principy-architektury.md)** — dědičnost a test „is it a?", tři principy škálovatelnosti (separace, volné vazby, data), kde co v UE bydlí a proč se schopnosti skládají z komponent místo dědění.
- **[Komunikace Blueprintů](komunikace-blueprintu.md)** — cast, interface, event dispatcher a broadcast kanály: kdo na kom závisí a kdy který použít — plus observer a mediator jako vzory a změřená cena jednoho castu.
- **[Interakce bez Event Ticku](interakce-bez-event-ticku.md)** — event-driven interakční systém: overlap trigger, Blueprint Interface, tagy a validated gets.
- **[Gameplay Tags](gameplay-tags.md)** — hierarchický stav místo booleanové špagety: tag manager komponenta, dotazy bez skrytých bugů, pojmenování.
- **[Organizace projektu](organizace-projektu.md)** — Content Browser podle Epicu (feature foldery, redirectory, 260znakový limit), devět tipů proti špagetám v grafech a Git přímo z editoru včetně diffu blueprintů.
- **[Levely a streaming](levely-a-streaming.md)** — proč Open Level zamrzá, level streaming s persistent levelem a breakdown, jak loading schovává Resident Evil Requiem.
- **[Ukládání](ukladani.md)** — SaveGame objekty, sloty a vzor Game Instance + function library pro save dostupný odkudkoli — a dál struktury, interface, sync vs. async a ukládání stavu světa.
- **[Telemetrie](telemetrie.md)** — activity tracker z gameplay tagů a vzdálená analytika (TrackEdge + PostHog).

**Motion Matching a GASP**

- **[Motion Matching základy](mm-zaklady.md)** — dotaz místo grafu stavů: trajektorie, databáze, schema a chooser; setup od nuly, sparse set (13 animací stačí) a procedurální uzly.
- **[Systémy nad MM](mm-systemy.md)** — combat přes montáže a choosery, traversal a cover komponenty se state managerem, nescriptované interakce z Witcher 4 dema a směrové hit reakce přes dot product a chooser tabulku.
- **[GASP: Game Animation Sample](gasp.md)** — anatomie Epicova vzorového projektu: capsule-driven autoring animací, řízení výběru, traversal pod kapotou, Mover, NPC přes State Tree, Control Rig vrstva a zbraně přes overlay.

**Pohyb postavy (locomotion)**

- **[Základy pohybu](pohyb-zaklady.md)** — gaity přes Max Walk Speed a blend spacy, podřep a plazení, rychlost podle sklonu, nabíjený skok s křivkou a dvě řešení zdi: zastavení à la RE9 a klouzání à la TLOU2.
- **[Parkour postaru](parkour-vault.md)** — vault a výlez přes tři trace s root motion montážemi; ledge grab se zarovnáním na libovolný mesh přes Get Actor Bounds.
- **[Mover](mover.md)** — proč nahrazuje CMC: modulární movement modes, layered moves, replikace vstupů, dvě síťové větve; setup od nuly v 5.7 a oprava strafu na osm směrů.

**AI a chování NPC**

- **[Základy nepřátelské AI](ai-zaklady.md)** — minimální nepřítel (Pawn Sensing + AI MoveTo + nav mesh), patrola náhodně i po waypointech, chase se ztrátou zájmu, totéž přes AI Controller + Behavior Tree + Blackboard, a Utility AI jako rozhodovací vrstva nad tím vším.
- **[AI vnímání](ai-vnimani.md)** — Pawn Sensing vs. AI Perception vs. trigger; kužel zraku, object permanence, lose sight radius, přesný timing ztráty zájmu a objektový klíč s odloženou ztrátou cíle.
- **[State Trees](state-trees.md)** — kompletní nepřítel: patrola po spline, tři smysly jedné percepce, Report eventy, přechody přes gameplay tagy a event dispatchery.

**Herní systémy a interakce**

- **[Kroky a povrchy](footsteps.md)** — physical materials, trace vs. anim notify, MetaSounds s hlasitostí podle rychlosti, stopy jako decaly s rozpadem a Niagara Data Channel optimalizace.
- **[Pasti a arénové mechaniky](pasti-a-mechaniky.md)** — kostra pasti (overlap → damage → launch), kyvadlové sekery s pivotem a per-instance chováním, mizející podlaha à la Fall Guys a férovost hitboxů.
- **[Interakce s předměty a úkryty](interakce-predmety.md)** — házení s predikcí trajektorie (Predict Projectile Path + spline mesh) a úkryt ve skříni s choreografií přes montage notifies.

**Fyzika: ragdoll, lana, simulace**

- **[Ragdoll](ragdoll.md)** — od minutového přepínače po plnou smyčku: physics asset s ALS triky, active ragdoll s motory řízenými rychlostí, pose snapshot a auto-vstávání správným směrem.
- **[Kabely, lana a Physics Control](lana-kabely.md)** — Cable Component, dynamický kabel s instancovanými meshi po délce a vor na Physics Control pružině.

**Voda**

- **[Voda a buoyancy](voda-a-buoyancy.md)** — water bodies a jejich spliny, napojení na terén, buoyancy přes pontoony i novou 5.7 cestu s physical materialem.
- **[Interaktivní voda](interaktivni-voda.md)** — vlnky za postavou: 5.6 shallow water subsystem checkboxem, nebo ručně Niagara Fluids šablonou s collider tagy.
- **[Nástroje: EasyWaterscape](nastroje-voda.md)** — Faucherův nástroj jako kontext + přenositelné lekce: Single Layer Water limity, TSR rozmazání, výkonové páky.

**Animace: nástroje a mocap**

- **[Animační nástroje](animace-nastroje.md)** — AnimBP se state machine od nuly (třídílný skok, AnimBP bez castu), markerless mocap v 5.8 (video → animace přes MetaHuman Performance), procedurální pavouk na Locomotoru a SAM pro izolaci aktéra při animování.

**MetaHuman**

- **[MetaHuman v praxi](metahuman.md)** — hratelná postava (retarget jedním klikem, virtual bones foot IK), look-at systém přes post-process AnimBP, Chaos Cloth oblečení, Crowd plugin s Mass Entity, lekce z optimalizace obličeje a převod cizího statického meshe na plnohodnotného MetaHumana.

**Terén a krajina**

- **[Landscape tipy](landscape-tipy.md)** — klasický terén: Nanite displacement, skrytý copy/paste gizmo nástroj, malování PCG dat štětcem a anti-tiling technika dvou měřítek.
- **[Mesh Terrain (UE 5.8)](mesh-terrain.md)** — nový terénní systém: partitioned Nanite mesh, nedestruktivní modifier stack, channels — nově s praxí kanálů, malování a PCG.

**PCG a procedurální svět**

- **[PCG: základy a nástroje v editoru](pcg-zaklady.md)** — PCG Mode 5.7 (spline, paint, volume), plot přes linear grammar, vlastní štětec se skutečným scatteringem a výřezy podle kolizí + debug uzly.
- **[Instanced Actors: instance, které ožijí](instanced-actors.md)** — svět z levných instancí, blueprint jen u hráče: setup přes Data Registry, manager pattern pro perzistenci a fyzika s eject prahem.
- **[PCG vegetace: stromy a les](pcg-vegetace.md)** — Procedural Vegetation editor (5.7/5.8), les přes Instance Skinned Mesh Spawner s větrem, proxy kolize, mýtiny a cesty, a hotový nástroj PCG Forest jako srovnání.
- **[PCG liány: po povrchu i zavěšené](pcg-liany.md)** — liány lezoucí po meshích (mesh sampler + pathfinding s fitness score) a závěsné křivky mezi dvěma kliky — od lián po vánoční světla.
- **[Případovka: Hex-A-Gone z PCG](pcg-hexagone.md)** — celá minihra z Fall Guys jedním grafem: hex mřížka aritmetikou řádků a mizející dlaždice přes Instanced Actors s eject trikem.

**Prostředí a environment art**

- **[Breakdowny: jak se staví herní světy](env-breakdowny.md)** — San Francisco 1:1 od jednoho člověka, The Ascent (4 artisti, jeden shader), TLOU trim sheety, RE Requiem vrstvy realismu a detektivka kolem Crimson Desert.
- **[Stavba prostředí: od kompozice po render](env-tvorba.md)** — chiaroscuro test před settingy, 132minutová lesní pěšina v PCG (vegetace, decaly, fyzikální světlo, MRQ), temný les za odpoledne a zvuk + listí jako finální vrstva.

**Materiály a VFX**

- **[Materiály: sdílení, displacement, decay a toon](materialy.md)** — master material se sdílenými texturami, Nanite displacement malovaný vertex colorem, procedurální decay systém (krev/špína/toxin jednou material function + zóny s timeline) a toon shading z 5.8.

**Osvětlení a atmosféra**

- **[Osvětlení: fyzikální základ, mlha a nálady](osvetleni.md)** — PBL workflow s light metery a EV100, mlha ze Silent Hill 2 jako volumetrický materiál, horor ve vrstvách se světelnou navigací, noční scéna z defaultu a rychlé triky.

**Rendering a optimalizace**

- **[Optimalizace scény: draw cally, Nanite a foliage](optimalizace.md)** — proč jsou levely pomalé (ISM → packed level actors → data layers), Nanite vs. LODy bez ideologie, voxelizace proti overdraw a dvoudílná foliage optimalizace v kontextu hry.
- **[Textury a DLSS: paměť a rozlišení](textury-a-dlss.md)** — right-sizing textur (normálka nese detail), unikátní textury vs. atlas vs. virtual textures a DLSS 4.5 s kompenzací mip biasu.

**AI nástroje ve vývoji**

- **[AI agenti: Claude Code a MCP v enginu](claude-code-ue.md)** — nativní MCP v 5.8 (setup a první testy), komunitní cesta s endless runner stress testem, agent v Blenderu a ComfyUI, 72hodinová hra jako mapa dělby člověk–AI, produkty okolo a Convai NPC.
- **[AI assety: z obrázku po postavu v enginu](ai-assety.md)** — bezplatná pipeline za hodinu, srovnání Tripo/Hunyuan/Rodin s cenami, hratelná postava v tandemu, modulární systém s AccuRigem, konverze na MetaHumana v 5.8 a AI animace Kimodo + 2D PixelLab.

**Editor a workflow**

- **[Tipy do editoru](editor-tipy.md)** — jak se učit engine (rady instruktora Epicu), výběry a navigace ve viewportu, pivot bez Blenderu, rozmístění fyzikou a drobné triky, které šetří minuty každý den.
