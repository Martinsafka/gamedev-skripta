# Optimalizace scény: draw cally, Nanite a foliage

Výkonová kapitola od základů po specializaci: **proč jsou levely pomalé** (draw cally a čtyři úrovně léčby od instancí po data layers), **Nanite vs. LODy** bez ideologie, **voxelizace** jako zabiják overdraw — a dvoudílný hluboký ponor do **optimalizace foliage v kontextu skutečné hry**. Paměťovou stranu (textury, DLSS) řeší [sesterská kapitola](textury-a-dlss.md); jak výkonově uvažují velké produkce, ukazují [Breakdowny](env-breakdowny.md).

---

## Proč jsou levely pomalé: od instancí po data layers

**Zdroj:** [Why your levels are Slow in Unreal Engine 5](https://www.youtube.com/watch?v=4fjTSbDaeYQ) · [Taken Grace](https://www.youtube.com/channel/UCLagdpQoUG-jtyH8bF0IGZg) · ~34 min, tutoriál

**Shrnutí:** Když je každý kámen, židle a světlo „unikátní sněhová vločka v outlineru", CPU krvácí na draw callech — každý objekt je jeden pracovní příkaz pro GPU [(3:06)](https://www.youtube.com/watch?v=4fjTSbDaeYQ&t=186s). Video vede čtyřmi úrovněmi léčby: **ISM → packed level actors → level instances → data layers** — měřeno přes `stat fps` a `stat drawcount` (Slate UI řádek = editor sám, odečti ho) [(1:33)](https://www.youtube.com/watch?v=4fjTSbDaeYQ&t=93s).

### Rozpad myšlenky

**ISM (junior):** instanced static mesh registruje mesh u CPU jednou a zbytek jsou razítka transformů — 513 gemů za cenu jednoho [(3:06)](https://www.youtube.com/watch?v=4fjTSbDaeYQ&t=186s). V blueprintu: ISM komponenta + construction script s vnořenými for loopy = procedurální mřížka s instance-editable rozměry [(3:52)](https://www.youtube.com/watch?v=4fjTSbDaeYQ&t=232s) [(5:26)](https://www.youtube.com/watch?v=4fjTSbDaeYQ&t=326s). Limit: instance nenesou vlastní logiku, animace ani dynamická světla [(6:59)](https://www.youtube.com/watch?v=4fjTSbDaeYQ&t=419s).

**Packed level actors (lead):** označ static meshe → right-click → Level → **Create Packed Level Actor** — engine je sám převede na instance a vznikne znovupoužitelný celek [(8:31)](https://www.youtube.com/watch?v=4fjTSbDaeYQ&t=511s). Blueprinty dovnitř nesmí — Niagara koš hned vyhodí error s radou „použij level instance" [(9:18)](https://www.youtube.com/watch?v=4fjTSbDaeYQ&t=558s). Skvělé pro celé modulární budovy: z dálky stojí, interiér nenačtený [(15:34)](https://www.youtube.com/watch?v=4fjTSbDaeYQ&t=934s). **Level instances** jsou totéž pro cokoli včetně blueprintů (truhly, dveře) — znovupoužitelný sub-level à la domy ve Warzone [(11:42)](https://www.youtube.com/watch?v=4fjTSbDaeYQ&t=702s) [(12:28)](https://www.youtube.com/watch?v=4fjTSbDaeYQ&t=748s). Pozor: editace se propíše **všem** kopiím (jako u blueprintu) — variantu dělej z duplikátu [(16:20)](https://www.youtube.com/watch?v=4fjTSbDaeYQ&t=980s).

**Data layers (senior):** kontejnery aktorů se stavy **Unloaded / Loaded (v paměti, neviditelné) / Activated** — fungují jen ve world-partition světě (starému levelu pomůže right-click → Add Partition Streaming Support) [(16:20)](https://www.youtube.com/watch?v=4fjTSbDaeYQ&t=980s) [(17:06)](https://www.youtube.com/watch?v=4fjTSbDaeYQ&t=1026s). Outliner organizuj **podle load zón** (atrium, chodby, patro) — přiřazení aktorů vrstvě je pak jeden right-click [(14:01)](https://www.youtube.com/watch?v=4fjTSbDaeYQ&t=841s) [(18:39)](https://www.youtube.com/watch?v=4fjTSbDaeYQ&t=1119s); aktor smí do víc vrstev (místnost se dvěma vchody) [(19:26)](https://www.youtube.com/watch?v=4fjTSbDaeYQ&t=1166s) a vrstvy se dají **parentovat** (celé přízemí jedním přepnutím, `is recursive` bere hierarchii) [(30:20)](https://www.youtube.com/watch?v=4fjTSbDaeYQ&t=1820s).

**Spouštění (engineer):** načítání přes dveře (Get Data Layer Manager → Set Data Layer Runtime State) má past — zavřeš dveře zevnitř a místnost kolem tebe zmizí [(21:47)](https://www.youtube.com/watch?v=4fjTSbDaeYQ&t=1307s) [(24:53)](https://www.youtube.com/watch?v=4fjTSbDaeYQ&t=1493s). Robustnější je **BP_LoadTrigger**: box collision, **Switch Has Authority** (o vrstvách rozhoduje server — multiplayer ready), počítadlo hráčů v zóně (++ při vstupu, load při prvním; −− při odchodu, unload při nule) a **pole data layer assetů** s for-each — jeden trigger může řídit víc vrstev [(26:25)](https://www.youtube.com/watch?v=4fjTSbDaeYQ&t=1585s) [(27:57)](https://www.youtube.com/watch?v=4fjTSbDaeYQ&t=1677s) [(29:32)](https://www.youtube.com/watch?v=4fjTSbDaeYQ&t=1772s). Bonusový vzor: trigger „při druhém vstupu" naloaduje věci za zády hráče — strašidelný dům z Hogwarts Legacy [(32:40)](https://www.youtube.com/watch?v=4fjTSbDaeYQ&t=1960s).

> **Pozn.:** Kdy co: obří open world nech streamovat **World Partition samotný** — data layers nastupují pro interiéry uvnitř jedné buňky (nemocnice se sto místnostmi) a pro herní stavy „načti až po odemčení" [(26:25)](https://www.youtube.com/watch?v=4fjTSbDaeYQ&t=1585s). Poctivě přiznaný nedořešený detail: světla po skrytí vrstvy zmizí tvrdě — autor fix nezná [(21:00)](https://www.youtube.com/watch?v=4fjTSbDaeYQ&t=1260s). Data layers jsou world-partition sourozenec [ručního level streamingu](levely-a-streaming.md) — principy (persistent rám, loaded ≠ visible) se přenášejí.

**Souvislosti:** [Levely a streaming](levely-a-streaming.md) · [Breakdowny: San Francisco](env-breakdowny.md#san-francisco-11-mesto-od-jednoho-cloveka) · [Rejstřík: draw call](../rejstrik.md#draw-call) · [Rejstřík: data layer](../rejstrik.md#data-layer) · [Rejstřík: level instance](../rejstrik.md#level-instance)

---

## Nanite, nebo LODy?

**Zdroj:** [LOD or Nanite in UE5?](https://www.youtube.com/watch?v=-FmFOiqTO-8) · [Sergey Maryshev](https://www.youtube.com/channel/UCVAdTnZgQ40jpKzC0-_RPAQ) · ~9 min, srovnání

**Shrnutí:** Ne ideologie, ale měření: LODy vs. Nanite ve VRAM, na disku a v overdraw. Závěr má tvar rozhodovacího pravidla: **hodně jednoduchých objektů → LODy; high-poly bez masek a průhlednosti → Nanite** — a hlavně vědět, že jediný Nanite objekt ve scéně rezervuje celý **streaming pool** [(4:00)](https://www.youtube.com/watch?v=-FmFOiqTO-8&t=240s) [(7:59)](https://www.youtube.com/watch?v=-FmFOiqTO-8&t=479s).

### Rozpad myšlenky

**Co stojí LODy:** předpřipravené kopie se přepínají podle vzdálenosti — průhlednost zvládají, ale ruční setup žere čas a přepnutí je vidět (popping) [(0:47)](https://www.youtube.com/watch?v=-FmFOiqTO-8&t=47s). Paměťová past: při umístění objektu se do VRAM nahrají **všechny jeho LOD kopie najednou** — u high-poly stromu s plnou sadou LODů to eskaluje [(2:26)](https://www.youtube.com/watch?v=-FmFOiqTO-8&t=146s) [(3:13)](https://www.youtube.com/watch?v=-FmFOiqTO-8&t=193s).

**Co stojí Nanite:** clustery fungují jako „chytré LODy" per část objektu — automaticky, bez skoků [(1:36)](https://www.youtube.com/watch?v=-FmFOiqTO-8&t=96s); streamuje se jen viditelné, ale **streaming pool je rezervovaný bez ohledu na to, kam se díváš** [(3:13)](https://www.youtube.com/watch?v=-FmFOiqTO-8&t=193s). Proto: 100 jednoduchých modelů = ~50 MB geometrie, ale pool klidně 500 MB — na low-end cílech je Nanite na drobnostech čisté plýtvání [(4:00)](https://www.youtube.com/watch?v=-FmFOiqTO-8&t=240s). U LODů platí klasika: stejný mesh 100× = geometrie v paměti jednou, HISM srazí draw cally; **Nanite má instancing vestavěný** a ISM/HISM nepotřebuje [(4:51)](https://www.youtube.com/watch?v=-FmFOiqTO-8&t=291s).

**Dva trumfy LODů:** overdraw vizualizace ukáže, že tenká geometrie (listí) a masky Nanite bolí [(5:40)](https://www.youtube.com/watch?v=-FmFOiqTO-8&t=340s) — a LODy umí, co Nanite ne: **na poslední LOD přiřadit primitivní materiál** (dveře se sklem v dálce = nejlevnější shader), zatímco Nanite počítá plný shader do posledního pixelu [(6:27)](https://www.youtube.com/watch?v=-FmFOiqTO-8&t=387s).

**Ladění Nanite assetů:** **Keep Triangle Percent** sníží uložené triangly (rozmazání a blikání ve scéně = hladovějící streaming pool) a **Trim Relative Error** odřeže detaily pod rozlišovací schopnost oka [(7:13)](https://www.youtube.com/watch?v=-FmFOiqTO-8&t=433s).

> **Pozn.:** Přesně tohle rozhodnutí udělal [tvůrce San Francisca](env-breakdowny.md#san-francisco-11-mesto-od-jednoho-cloveka) — LODy kvůli kompatibilitě a kontrole, Nanite jako volitelný upgrade. A rada „vyber jednu hlavní technologii" má výjimku popsanou tamtéž: mix je legitimní, jen věz, že pool platíš od prvního Nanite objektu [(7:59)](https://www.youtube.com/watch?v=-FmFOiqTO-8&t=479s).

**Souvislosti:** [Breakdowny: San Francisco](env-breakdowny.md#san-francisco-11-mesto-od-jednoho-cloveka) · [Voxelizace](#voxelizace-nanite-listi-bez-overdraw) · [Rejstřík: Nanite](../rejstrik.md#nanite) · [Rejstřík: overdraw](../rejstrik.md#overdraw)

---

## Voxelizace: Nanite listí bez overdraw

**Zdroj:** [How to use Nanite Voxelization (like in the Witcher Demo)](https://www.youtube.com/watch?v=q2T4ni7UPfI) · [DK 3D](https://www.youtube.com/channel/UC3fGhbgSpR2BSSeTls3R6Sg) · ~11 min, tutoriál

**Shrnutí:** Experimentální feature 5.7, kterou proslavilo Witcher 4 demo: vzdálená vegetace se místo hustých polygonů kreslí jako **voxely** — v testu +20 % FPS **a zároveň** lepší čitelnost siluet v dálce [(0:02)](https://www.youtube.com/watch?v=q2T4ni7UPfI&t=2s).

### Rozpad myšlenky

**Zapnutí:** project settings → **Nanite foliage** (experimental) → restart; pak má každý Nanite mesh v Details volbu **shape preservation**: none / preserve area (stará cesta pro opacity-mapovou vegetaci) / **voxelize** [(0:44)](https://www.youtube.com/watch?v=q2T4ni7UPfI&t=44s) [(1:30)](https://www.youtube.com/watch?v=q2T4ni7UPfI&t=90s). Drobná past UI: napřed **Apply Changes**, teprve pak Save [(2:18)](https://www.youtube.com/watch?v=q2T4ni7UPfI&t=138s).

**Proč to funguje:** v Nanite overdraw vizualizaci svítí les s preserve area doběla — tytéž pixely se kreslí mnohokrát přes sebe [(4:43)](https://www.youtube.com/watch?v=q2T4ni7UPfI&t=283s). Voxelize scénu zklidní: jakmile je geometrie menší než pixel, nahradí ji krychle (čím dál, tím větší) — a krychle **zakrývají stromy za sebou**, takže overdraw mizí [(5:31)](https://www.youtube.com/watch?v=q2T4ni7UPfI&t=331s) [(9:24)](https://www.youtube.com/watch?v=q2T4ni7UPfI&t=564s). V defaultu jsou voxely sub-pixelové — vizuálně je nepoznáš; na náhled poslouží `r.Nanite.ViewMeshLODBiasOffset 4`, který je přitáhne ke kameře [(8:36)](https://www.youtube.com/watch?v=q2T4ni7UPfI&t=516s) [(10:13)](https://www.youtube.com/watch?v=q2T4ni7UPfI&t=613s).

**Hromadná konverze:** označit meshe napříč složkami (trik: hodit je do favorites) → right-click → Asset Actions → **Edit Selection in Property Matrix** → Nanite settings → shape preservation pro všechny naráz [(6:18)](https://www.youtube.com/watch?v=q2T4ni7UPfI&t=378s) [(7:04)](https://www.youtube.com/watch?v=q2T4ni7UPfI&t=424s).

> **Pozn.:** Tentýž property matrix trik doporučuje [right-sizing textur](textury-a-dlss.md#right-size-ne-vsechno-si-zaslouzi-4k) pro LOD bias — nástroj na hromadné ladění čehokoli. Voxelizace je součást stejné 5.7 vlny jako [Procedural Vegetation editor](pcg-vegetace.md#proceduralni-stromy-v-enginu-57) (output uzel má „voxelize" preservation přímo v exportu) a prakticky ji nasazuje [foliage optimalizace níž](#foliage-optimalizace-i-kotva-vykonu-a-velka-trojka).

**Souvislosti:** [PCG vegetace: stromy](pcg-vegetace.md#proceduralni-stromy-v-enginu-57) · [Foliage optimalizace](#foliage-optimalizace-i-kotva-vykonu-a-velka-trojka) · [Rejstřík: overdraw](../rejstrik.md#overdraw) · [Rejstřík: Nanite](../rejstrik.md#nanite)

---

## Foliage optimalizace I: kotva výkonu a velká trojka

**Zdroj:** [Foliage Optimization Done Right (UE 5.7)](https://www.youtube.com/watch?v=QvE_EUuGFm4) · [Dallas Drapeau](https://www.youtube.com/channel/UCatEMsDp-qF_bix_1ST2llw) · ~55 min, tutoriál

**Shrnutí:** Optimalizace foliage **v kontextu hry**, ne izolovaného benchmarku: napřed rozhodni, co děláš, pro jaký hardware a kde je tvá **kotva výkonu** — a pak systematicky projdi velkou trojku: **stíny, overdraw, world position offset** [(1:35)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=95s) [(4:47)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=287s). Výsledek dema: z 78 na 90+ FPS bez viditelné ztráty.

### Rozpad myšlenky

**Kotva výkonu:** každá hra utrácí rozpočet snímku jinde — Alan Wake ho kotví ve vegetaci lesa, The Finals v destrukci [(3:11)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=191s). Open-world RPG kotví ve foliage, protože v ní hráč tráví většinu času; kritika „foliage stojí moc" bez téhle nuance je bezcenná [(3:58)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=238s). Prakticky: cíl 60 FPS na RTX 3060 znamená vyvíjet na 90+ na jeho 4080 [(2:24)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=144s) [(11:47)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=707s). A biomy staví na **prázdné mapě** — čistý pohled na detail a izolovaný výkonový baseline, ještě než set potká město plné NPC [(9:28)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=568s).

**Stíny:** největší tichý žrout — stíny na assetech, které je nepotřebují [(4:47)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=287s). V optimalizovaném lese vrhá stín **jediný grass mesh** — a dojem „tráva vrhá stíny" drží; jehličí, jetel ani malé kameny stíny nemají a nikdo to nepozná (u kamenů autor „neviděl žádný rozdíl, jen cenu") [(37:32)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=2252s) [(42:36)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=2556s). Metoda: projít spawnery jeden po druhém a vypínat cast shadows [(39:05)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=2345s).

**Overdraw:** = překrývající se geometrie; proto Nanite foliage přešlo na plnou geometrii místo masek [(6:19)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=379s). „Geometrie je zadarmo" platí jen z půlky — cenou je velikost buildu [(7:07)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=427s). Lov: v overdraw vizualizaci vypínat spawnery, dokud nesvítí viník — tady „pine ground" asset za 10 FPS, jehož kořeny zvládne landscape materiál [(29:32)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=1772s) [(30:19)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=1819s). Otázka zní vždy stejně: **stojí ten efekt za tolik?** A pozor na zakopanou geometrii — scatter assety s většinou objemu pod zemí spraví duplikát a plane cut [(35:30)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=2130s).

**Audit assetů:** i drahé marketplace packy píšou „Nanite foliage" a myslí tím masky se zaškrtnutým Nanite — masked materiál s Nanite je overhead [(26:10)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=1570s). Kde velikost dovolí (jehličí, drobné kytky), stačí **přepnout na opaque** — z herního úhlu pohledu to nepoznáš [(26:57)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=1617s) [(28:29)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=1709s).

> **Pozn.:** Dvě zásady, které video opakuje: měř **živý svět** — „optimalizace", která vypne vítr, není optimalizace, tvá hra vítr má [(12:34)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=754s); a nejjistější cesta k výkonu je vlastní asset — koupený strom neopravíš, svůj ano [(16:26)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=986s).

**Souvislosti:** [Foliage II](#foliage-optimalizace-ii-gpu-scatter-a-runtime-kvalita) · [Voxelizace](#voxelizace-nanite-listi-bez-overdraw) · [PCG vegetace](pcg-vegetace.md) · [Rejstřík: overdraw](../rejstrik.md#overdraw)

---

## Foliage optimalizace II: GPU scatter a runtime kvalita

**Zdroj:** [Foliage Optimization Done Right (UE 5.7)](https://www.youtube.com/watch?v=QvE_EUuGFm4) · [Dallas Drapeau](https://www.youtube.com/channel/UCatEMsDp-qF_bix_1ST2llw) · ~55 min, tutoriál

**Shrnutí:** Druhá půlka receptu: **voxelize na všechen drobný scatter** (a lék na chvění s WPO), variace přes Per Instance Random, **GPU runtime scatter** z 5.7 šablony s pevným milisekundovým budgetem — a scalability větev, která nechá epic hráče zapnout si luxus [(19:23)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=1163s) [(44:10)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=2650s).

### Rozpad myšlenky

**Voxelize + WPO:** všechen mikro scatter (tráva, jetel, jehličí — vše „nesolidní") přepnout na voxelize; project setting Nanite foliage zapni **před importem Megaplants**, jinak nedorazí parent materiál [(19:48)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=1188s). Voxelizace zatím nesnáší world position offset animaci — vzdálená tráva „chvěje" [(20:49)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=1249s). Lék: **distance blend do WPO** — lerp mezi animací a nulou s alphou z Distance Blend uzlu (defaultní hodnoty sedí na vzdálenost, kde voxely nastupují); pro ladění týž lerp do base coloru — červená = animuje se [(21:37)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=1297s) [(22:23)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=1343s).

**Variace zadarmo:** **Per Instance Random** → tříbarevný lerp → násobit subsurface (nebo barvu): každé stéblo jinak prosvítá, každý kámen jinak světlý — jeden materiál, žádné textury navíc [(23:10)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=1390s) [(25:24)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=1524s).

**GPU scatter:** pro trávu použij PCG šablonu **Runtime Grass GPU** — 5.7 klipuje runtime generování na ~2–5 ms, takže se neutrhne z řetězu; výkonnější než landscape grass [(44:10)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=2650s). Nutná trojice: **is partitioned** + **generate at runtime** + na PCG world actoru „treat editor viewport as runtime" (jinak v editoru všechno zmizí) [(45:44)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=2744s) [(46:34)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=2794s). Grid size řídí dosah generování — proti mizejícím čtvercům přidej distance fade v materiálu [(46:34)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=2794s); hustotu drží point generator (260k → 25k bodů) [(47:22)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=2842s). Na spawnerech drobného scatteru zapni **Execute on GPU** (na Megaplants geometrii zatím nejde) [(53:11)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=3191s). Skinned keře/stromy do PCG: přímé vložení skinned assetu hodí error „at last is not in the metadata" — cesta vede přes **graph parameter pole + Match and Set Attributes** a **wind transform provider** ve spawneru [(48:59)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=2939s) [(52:05)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=3125s).

**Runtime quality switch:** efekty „hezké, ale drahé" (kořenový scatter, stíny květin) zapoj přes **scalability větev** (low/medium/high/epic/cinematic) — default je nevidí, epic hráč s odpovídajícím hardwarem ano; vyžaduje generate at runtime [(30:58)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=1858s) [(40:39)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=2439s).

> **Pozn.:** Mega Plants skeletal stromy běží „překvapivě dobře" i podle autora s dekádou foliage praxe — bolest z milionů trianglů v enginu je z velké části už jen zvyk [(43:24)](https://www.youtube.com/watch?v=QvE_EUuGFm4&t=2604s). Celý setup navazuje na [PCG vegetaci](pcg-vegetace.md) (stejné wind providery a spawner vzory) — tahle kapitola je její výkonová druhá půlka.

**Souvislosti:** [Foliage I](#foliage-optimalizace-i-kotva-vykonu-a-velka-trojka) · [PCG vegetace: les](pcg-vegetace.md#les-pcg-graf-se-skeletal-stromy) · [Rejstřík: PCG](../rejstrik.md#pcg) · [Rejstřík: overdraw](../rejstrik.md#overdraw)

---

## Druhá osa optimalizace: co blokuje hlavní vlákno

**Zdroj:** [Game Dev Secrets: Multithreaded Optimization!](https://www.youtube.com/watch?v=44hfu7ELgVc) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~2 min, short

**Shrnutí:** Zbytek téhle kapitoly řeší **co a jak se vykresluje**. Tenhle dvouminutový klip připomíná druhou osu, na kterou se u vizuálně zaměřené optimalizace snadno zapomene: **kolik času zabere kód, který s vykreslováním nemá nic společného.** Demonstrace je nemilosrdně jednoduchá — přidání drahého výpočtu srazí hru na **10 snímků za sekundu**, přesunutí téhož výpočtu na jiné vlákno ji vrátí na **144**.

### Rozpad myšlenky

**Proč vůbec jeden pomalý výpočet zabije celou hru** [(0:01)](https://www.youtube.com/watch?v=44hfu7ELgVc&t=1s): autor tu otázku sám položí za diváka — *„teoreticky by přece pobíhání postavy po mapě nemělo být ovlivněné matematikou běžící na pozadí, ne?"* A odpoví: **ta matematika na pozadí neběží.** *„Hra běží na tom, čemu se říká hlavní vlákno. A všechen kód, co pro hru píšu — kromě shaderů — běží na tom jediném vlákně."* Tedy pohyb postavy, její stavový automat, systém hitboxů i parallax pozadí. **„Takže když je tam jedna věc, která zabere spoustu času, všechno ostatní na ni musí čekat."**

**Co na jiné vlákno smíš** [(0:47)](https://www.youtube.com/watch?v=44hfu7ELgVc&t=47s) je ta část, kvůli které se multithreading nedá použít všude: *„je to docela komplikované, protože mimo hlavní vlákno spoustu věcí nesmíš."* Konkrétně jmenuje omezení dvou jiných enginů, ale princip je společný — **na herní objekty a scénu smí sahat jen hlavní vlákno**; totéž platí v UE pro Blueprinty a většinu gameplay API.

**Mentální model, který z toho plyne** [(0:47)](https://www.youtube.com/watch?v=44hfu7ELgVc&t=47s), je nejpřenositelnější věta klipu: *„ostatní vlákna jsou dobrá v tom, že si vezmou konkrétní úkol. Pošleš je pryč se všemi daty, která k tomu potřebují, a ona se po čase vrátí s odpovědí."* Z toho plyne i seznam vhodných kandidátů: **hledání cesty, načítání assetů a procedurální generování** — *„dlouho to běží, ale nepotřebuješ průběžné aktualizace."* Naopak nic, co musí každý snímek sáhnout na aktéry ve světě.

> **Pozn.:** Pro naši knihovnu je tenhle klip užitečný hlavně jako **rozcestník**: většina rad o výkonu v UE (Nanite, LODy, foliage, [instance](instanced-actors.md)) míří na GPU a na počet draw callů, ale hra, která se zadrhává při otevření inventáře nebo při generování levelu, má problém jinde. Diagnostika se proto dělá jinými nástroji — profiler ukáže, jestli je snímek limitovaný **game threadem**, nebo renderem, a to rozhodne, kterou půlkou téhle kapitoly se vůbec zabývat. Klip je engine-agnostický (autor pracuje v jiném enginu), ale rozdělení práce mezi vlákna platí všude stejně.

**Souvislosti:** [Proč jsou levely pomalé](#proc-jsou-levely-pomale-od-instanci-po-data-layers) *(druhá osa: co se vykresluje)* · [Interakce bez Event Ticku](interakce-bez-event-ticku.md#overlap-trigger-misto-trasovani-v-ticku) *(příbuzný lék: nedělej to každý snímek)* · [Instanced Actors](instanced-actors.md) · [Programátorské myšlení](../teorie/programatorske-mysleni.md) · [Rejstřík: race condition](../rejstrik.md#race-condition) · [Rejstřík: Multithreading](../rejstrik.md#multithreading)
