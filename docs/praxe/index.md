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

**Terén a krajina**

- **[Mesh Terrain (UE 5.8)](mesh-terrain.md)** — nový terénní systém: partitioned Nanite mesh, nedestruktivní modifier stack, channels.

**Editor a workflow**

- **[Tipy do editoru](editor-tipy.md)** — drobné triky, které šetří minuty každý den.
