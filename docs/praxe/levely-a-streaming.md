# Levely a streaming: načítání bez zamrznutí

Jak dostat hráče z levelu do levelu, aniž by hra ztuhla — a jak to dělají profíci. Tutoriál DevEdge Studia staví základy (proč `Open Level` zamrzá, level streaming, asynchronní načítání, loading screen) a breakdown HALbot Studios pak volnou kamerou prochází Resident Evil Requiem a ukazuje tytéž techniky v AAA produkci.

---

## Open Level zamrzne hru; streaming ji drží živou

**Zdroj:** [How to CORRECTLY Load Levels in Unreal Engine!](https://www.youtube.com/watch?v=mwyJ7rKUqKE) · [DevEdge Studio](https://www.youtube.com/channel/UCGa0hsNw3BK6xTDnVvfFltw) · ~23 min, tutoriál

**Shrnutí:** `Open Level by Name` zastaví celou hru [(1:22)](https://www.youtube.com/watch?v=mwyJ7rKUqKE&t=82s): jediný thread se věnuje jen načítání — zvuk stojí, animace stojí, i případný loading widget jen ztuhle visí [(1:50)](https://www.youtube.com/watch?v=mwyJ7rKUqKE&t=110s). Navíc vymění GameMode, controller i stav hráče (přenos statistik pak zbývá řešit přes Game Instance [(2:58)](https://www.youtube.com/watch?v=mwyJ7rKUqKE&t=178s)). Odpověď je **level streaming**: persistent level jako rám a sub-levely nahrávané asynchronně za běhu.

### Rozpad myšlenky

**Mechanika streamingu:** okno `Window → Levels` [(4:00)](https://www.youtube.com/watch?v=mwyJ7rKUqKE&t=240s) ukazuje **persistent level** (rodičovský rám) a sub-levely. Obsah se do sub-levelu dostane výběrem actorů → pravý klik na level → *Move Selected Actors to Level* [(4:56)](https://www.youtube.com/watch?v=mwyJ7rKUqKE&t=296s). Každý sub-level má **streaming mode** [(5:27)](https://www.youtube.com/watch?v=mwyJ7rKUqKE&t=327s): *Always Loaded*, nebo *Blueprint* (řízený logikou). Dvě cesty načítání: **Level Streaming Volume** [(6:04)](https://www.youtube.com/watch?v=mwyJ7rKUqKE&t=364s) — vstup hráče do objemu nahraje level (pozor: volume musí ležet v persistent levelu [(6:20)](https://www.youtube.com/watch?v=mwyJ7rKUqKE&t=380s), jinak je schovaný spolu s levelem, který má spouštět) — a uzly **Load/Unload Streaming Level** [(9:27)](https://www.youtube.com/watch?v=mwyJ7rKUqKE&t=567s) z trigger boxů. Detail, který šetří paměťové omyly: *loaded* ≠ *visible* [(9:47)](https://www.youtube.com/watch?v=mwyJ7rKUqKE&t=587s) — neviditelný level pořád sedí v paměti; teprve unload ji vrací.

**Trik s base levelem:** persistent level nejde unloadnout [(14:20)](https://www.youtube.com/watch?v=mwyJ7rKUqKE&t=860s). Chceš-li „vyměnit celý svět", přesuň veškerý obsah persistentu do sub-levelu `Base` (pravý klik → Select All Actors → move [(14:54)](https://www.youtube.com/watch?v=mwyJ7rKUqKE&t=894s)) — persistent zůstane prázdná skořápka, která na BeginPlay nahraje `Base`, a pak jde `Base` unloadnout a nahradit jiným sub-levelem. Hráč, jeho stav i GameMode přitom žijí dál — všechno se odehrává uvnitř jednoho persistent levelu.

**Async a loading screen:** streaming běží na vlastním threadu [(18:17)](https://www.youtube.com/watch?v=mwyJ7rKUqKE&t=1097s) — hudba hraje, hra žije, jen svět se na pozadí skládá. Krátký hitch při přepnutí zakryje widget [(16:57)](https://www.youtube.com/watch?v=mwyJ7rKUqKE&t=1017s): vytvoř před `Load Streaming Level`, odstraň po dokončení [(20:29)](https://www.youtube.com/watch?v=mwyJ7rKUqKE&t=1229s). Moderní hry ale míří na **seamless loading** [(17:07)](https://www.youtube.com/watch?v=mwyJ7rKUqKE&t=1027s) — hráč přechází most a svět se mezitím vymění; loading screen je poslední záchrana, ne cíl.

> **Pozn.:** Video učí klasický level streaming — pro velké otevřené světy má UE5 nástupce: [World Partition](../rejstrik.md#world-partition) s automatickými buňkami (viz [Mesh Terrain](mesh-terrain.md), který na něm stojí). Principy (async, persistent rám, loaded ≠ visible) platí v obou systémech; ruční sub-levely dávají smysl pro řízené přechody à la RE Requiem níže.

**Souvislosti:** [Jak to dělá Resident Evil Requiem](#jak-to-dela-resident-evil-requiem) níže · [První dojem](../teorie/prvni-dojem.md) *(loading na vlastních podmínkách)* · [Rejstřík: level streaming](../rejstrik.md#level-streaming) · [Rejstřík: persistent level](../rejstrik.md#persistent-level)

---

## Jak to dělá Resident Evil Requiem

**Zdroj:** [How Resident Evil Requiem Hides Loading and Level Instancing | Game Dev Breakdown](https://www.youtube.com/watch?v=l_U0enrB9IY) · [HALbot Studios](https://www.youtube.com/channel/UCIXYn8CgVS8GnS2RJI2zkWQ) · ~19 min, breakdown volnou kamerou

**Shrnutí:** Autor vypustí kameru z první lokace RE Requiem a čte z ní produkční triky [(0:39)](https://www.youtube.com/watch?v=l_U0enrB9IY&t=39s): hratelná plocha je maličká, kulisy jsou recyklované, interiéry jsou textury s parallaxem — a level se nahrává po kouscích, schovaný za cutscénami a dveřmi. AAA iluze je z 90 % disciplína, ne technologie.

### Rozpad myšlenky

**Kulisy:** pozadí tvoří pár velkých building assetů opakovaných dokola [(1:37)](https://www.youtube.com/watch?v=l_U0enrB9IY&t=97s) (vodárenské věže = stejný model, jiná textura); „interiéry" oken jsou parallax textury s přesvědčivou hloubkou [(5:29)](https://www.youtube.com/watch?v=l_U0enrB9IY&t=329s); za oknem chodby visí velká plocha s HDRI budovy [(11:17)](https://www.youtube.com/watch?v=l_U0enrB9IY&t=677s) — z jediného úhlu, odkud ji hráč zahlédne, vypadá jako svět. Osvětlení interiéru pomáhají **bílé bounce stěny** schované nad stropem [(4:37)](https://www.youtube.com/watch?v=l_U0enrB9IY&t=277s) a černé boxy proti light leakům [(5:09)](https://www.youtube.com/watch?v=l_U0enrB9IY&t=309s); slavný volumetrický god-ray je jeden spotlight [(11:00)](https://www.youtube.com/watch?v=l_U0enrB9IY&t=660s). Ulice končí pohledovou zátkou — geometrie postavená jen proto, aby za ní nemuselo nic existovat [(6:42)](https://www.youtube.com/watch?v=l_U0enrB9IY&t=402s).

**Streaming vzorec:** prostředí se nahrává po chuncích na triggerech — vstup do hotelu, použití klíče, přestřižení drátu [(15:42)](https://www.youtube.com/watch?v=l_U0enrB9IY&t=942s): chodba je nahraná, pokoj za dveřmi ne, a objeví se až s interakcí [(17:01)](https://www.youtube.com/watch?v=l_U0enrB9IY&t=1021s). **Cutscény slouží jako loading obrazovky** [(13:47)](https://www.youtube.com/watch?v=l_U0enrB9IY&t=827s) — pokaždé, když se hraje, na pozadí se skládá další část levelu. Zajímavý detail: **interaktivní objekty** (dveře, šuplíky, rádio) jsou spawnuté v hlavním levelu od začátku [(8:30)](https://www.youtube.com/watch?v=l_U0enrB9IY&t=510s), i když jejich okolí ještě neexistuje — patrně musí žít v paměti kvůli stavu. A unloading je **fázovaný** [(18:10)](https://www.youtube.com/watch?v=l_U0enrB9IY&t=1090s): z opuštěné ulice zmizí nejdřív chodci [(18:01)](https://www.youtube.com/watch?v=l_U0enrB9IY&t=1081s), velké budovy zůstávají — postupné uvolňování brání frame hitchi.

**Bonus pro first-person tvůrce:** hráčka nemá hlavu [(3:11)](https://www.youtube.com/watch?v=l_U0enrB9IY&t=191s) — first-person mesh je jiný než třetí osoba, ramena stabilizovaná, bunda animovaná; a tělo se renderuje skrz překážky, aby při clippingu nezmizelo.

> **Pozn.:** Nejcennější lekce breakdownu: *nic z toho hráč nevidí, a přesně proto to funguje.* Zapadá do sebe s [imerzí](../teorie/game-feel.md#imerze-svet-ktery-na-tebe-odpovida) (fake > simulace) i s [hranicemi mapy](../teorie/prostor-a-hranice.md#hranice-mapy-hrac-se-ma-rozhodnout-sam-ze-dal-nepujde) — pohledová zátka je tvrdá hranice s dokonalým alibi. Do vlastní stealth adventury: cutscény a dveře jako loading kryty jsou dosažitelné i pro sólo projekt.

**Souvislosti:** [Streaming výše](#open-level-zamrzne-hru-streaming-ji-drzi-zivou) · [Game feel a imerze](../teorie/game-feel.md) · [Prostor a hranice](../teorie/prostor-a-hranice.md) · [Rejstřík: level streaming](../rejstrik.md#level-streaming)
