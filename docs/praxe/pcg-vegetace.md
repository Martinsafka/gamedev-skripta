# PCG vegetace: stromy a les

UE 5.7 přineslo vedle [PCG Mode](pcg-zaklady.md) druhou velkou novinku: **Procedural Vegetation Editor** — stromy se poprvé staví přímo v enginu, uzlovým grafem, a hýbou se novým wind systémem. Tahle kapitola projde celou pipeline: stavbu stromu (z presetu i od nuly), osazení krajiny PCG grafem, opravy dvou dětských nemocí (kolize a vítr na dálku), mýtiny a cesty — a na závěr pohled na dva hotové nástroje. Placený PCG Forest totéž balí do data assetů, autorský QuickScatter ukazuje, jak les naškálovat na [otevřený svět](#les-pro-otevreny-svet-co-se-nacte-s-levelem-a-co-roste-kolem-hrace). Liány a závěsné křivky mají [vlastní kapitolu](pcg-liany.md), základy PCG grafů [tady](pcg-zaklady.md).

---

## Procedurální stromy v enginu (5.7)

**Zdroj:** [Unreal Engine 5.7 - Procedural Vegetation - Build Your Own Forest - Tutorial (Part 1/2)](https://www.youtube.com/watch?v=o-kMXZX_oK8) a [Procedural Vegetation Pine Trees - Quick Tip](https://www.youtube.com/watch?v=Wqmr0bSR99U) · [Unreal - X - Tutorials](https://www.youtube.com/channel/UCjKg7gsHCEyXtJbZYx2Xu7A) · ~9 + 1,5 min, tutoriál + tip

**Shrnutí:** Strom jako graf: **Preset Loader** načte tvar, žluté modifiery ho ohnou a prořežou, **Mesh Builder** vyrobí geometrii, **Foliage Palette + Distributor** olistí a **Output** vyexportuje static/skeletal mesh s Nanite foliage [(0:50)](https://www.youtube.com/watch?v=o-kMXZX_oK8&t=50s). Vítr je „zadarmo" — ale jen na instancích, což určuje celý zbytek workflow [(7:12)](https://www.youtube.com/watch?v=o-kMXZX_oK8&t=432s).

### Rozpad myšlenky

**Setup:** plugin Procedural Vegetation Editor **plus** Nanite foliage v project settings, pak restart [(0:03)](https://www.youtube.com/watch?v=o-kMXZX_oK8&t=3s). Asset vzniká přes content browser → Foliage → Procedural Vegetation; k dispozici dva vestavěné presety a rostoucí řada **Mega Plants** od Quixelu na Fabu — přidané presety se v Preset Loaderu objeví samy [(0:03)](https://www.youtube.com/watch?v=o-kMXZX_oK8&t=3s) [(0:50)](https://www.youtube.com/watch?v=o-kMXZX_oK8&t=50s). Quixel jich vydává nové zhruba měsíčně zdarma (Baltic Pines, bambus, sakura, anglický dub…) — vyplatí se Fab pravidelně kontrolovat [(0:49)](https://www.youtube.com/watch?v=Wqmr0bSR99U&t=49s).

**Ergonomie grafu:** viewport vždy ukazuje stav **vybraného** uzlu (Preset Loader = point cloud, Mesh Builder = mesh); `Ctrl+L` viewport na uzel **zamkne**, takže ladíš modifier a vidíš finální strom [(0:50)](https://www.youtube.com/watch?v=o-kMXZX_oK8&t=50s) [(1:38)](https://www.youtube.com/watch?v=o-kMXZX_oK8&t=98s). K měřítku pomáhá zapnutý manekýn a scale vizualizace [(1:38)](https://www.youtube.com/watch?v=o-kMXZX_oK8&t=98s).

**Žluté modifiery** (pracují s point cloudem, patří **před** Mesh Builder, dají se stackovat): **Carve** ořezává tvar (od délky, od kořene, od Z, od poloměru), **Gravity** ohýbá — v phototropic režimu rostou větve k imaginárnímu slunci, **Slope** naklání strom pro svahy, **Scale** škáluje, **Remove Branches** maže větve podle délky/poloměru/stáří [(2:26)](https://www.youtube.com/watch?v=o-kMXZX_oK8&t=146s) [(3:14)](https://www.youtube.com/watch?v=o-kMXZX_oK8&t=194s). **Mesh Builder** pak drží materiály kmene a větví, redukci bodů/segmentů (low-poly stylizace), **plant profile** — tloušťku kmene i větví křivkou — a displacement texturu [(3:14)](https://www.youtube.com/watch?v=o-kMXZX_oK8&t=194s) [(4:01)](https://www.youtube.com/watch?v=o-kMXZX_oK8&t=241s).

**Za builderem:** **Bone Reduction** — méně kostí znamená hrubší vítr, ale výrazně levnější strom; při stovkách instancí zásadní páka [(4:48)](https://www.youtube.com/watch?v=o-kMXZX_oK8&t=288s). **Foliage Palette** přijme do slotů jakýkoli static/skeletal mesh (klidně jablko — pivot musí sedět v místě napojení, pozor na orientaci) [(5:34)](https://www.youtube.com/watch?v=o-kMXZX_oK8&t=334s) [(6:21)](https://www.youtube.com/watch?v=o-kMXZX_oK8&t=381s) a **Foliage Distributor** řídí olistění parametrem *ethylene threshold* — vysoký = bujný strom, nízký = řídký a suchý; simulace stárnutí a sezón jedním sliderem [(5:34)](https://www.youtube.com/watch?v=o-kMXZX_oK8&t=334s). **Output**: static vs. skeletal export, *create nanite foliage*, preservation method **voxelize** (novinka „jako ve Witcher 4 demu") a volitelná kolize [(7:12)](https://www.youtube.com/watch?v=o-kMXZX_oK8&t=432s).

**Vítr jen na instancích:** strom přetažený do levelu se nehýbe. Mimo PCG pomůže blueprint s **Instanced Skinned Mesh komponentou**, přiřazeným skeletal stromem a **wind transform providerem** [(7:12)](https://www.youtube.com/watch?v=o-kMXZX_oK8&t=432s) [(8:00)](https://www.youtube.com/watch?v=o-kMXZX_oK8&t=480s). Vítr celé scény řídí **BP Global Foliage Actor** z engine contentu — intenzita, směr, a navíc *seasonal state* a *health* stromů [(8:00)](https://www.youtube.com/watch?v=o-kMXZX_oK8&t=480s).

> **Pozn.:** Systém je zatím uzavřený — bere jen vlastní presety, „přines si svůj mesh" nefunguje (na limit naráží i [kapitola o liánách](pcg-liany.md)). Cestu pro externí assety ukazuje video **SpeedTree to Nanite foliage with Wind!** (lumpy668, [YouTube](https://www.youtube.com/watch?v=67-W5lCSD_0), kanál [lumpy668](https://www.youtube.com/channel/UCDFhtSIQKBxr4vCu9PwiVCQ)): SpeedTree geometrie napojená na Nanite foliage + wind, s Houdini HDA konverzí alpha karet na plnou geometrii kvůli osvětlení i výkonu. *Video nemá přepis, shrnutí vychází z popisu — detaily ověř přímo ve videu.*

**Souvislosti:** [Strom od nuly (5.8)](#strom-od-nuly-a-58-grower-koreny-extract-to-mesh) · [Rejstřík: Procedural Vegetation](../rejstrik.md#procedural-vegetation) · [Rejstřík: Nanite](../rejstrik.md#nanite)

---

## Strom od nuly a 5.8: grower, kořeny, extract to mesh

**Zdroj:** [Everything You Need to Know About Procedural Vegetation in UE5.8](https://www.youtube.com/watch?v=DvBECqijNDg) · [PolyBoost](https://www.youtube.com/channel/UCHzLwhfU8b07C8WOAcrXiYA) · ~14 min, tutoriál

**Shrnutí:** Bez presetu: **Grower** uzel vypěstuje základní strukturu a zbytek grafu ji tvaruje — až po dvě 5.8 lahůdky: **Object Interaction** (strom se ohne kolem překážky) a **Extract to Mesh** (procedurální strom zrekonstruovaný z existujícího meshe) [(0:48)](https://www.youtube.com/watch?v=DvBECqijNDg&t=48s) [(12:05)](https://www.youtube.com/watch?v=DvBECqijNDg&t=725s).

### Rozpad myšlenky

**Růst:** Grower řídí *cycles* (víc = větší a hustší strom) [(1:06)](https://www.youtube.com/watch?v=DvBECqijNDg&t=66s), **axial angle** otevírá či zavírá úhel větvení (obdoba start angle ze SpeedTree) a growth modes umí větve zploštit nebo uspořádat přeslenitě jako u borovice [(1:18)](https://www.youtube.com/watch?v=DvBECqijNDg&t=78s); k tomu segment length a branch scale [(2:13)](https://www.youtube.com/watch?v=DvBECqijNDg&t=133s). Když parametry nestačí, **Manual Edit** dovolí konkrétní větev ručně natočit, přetvarovat nebo smazat [(2:54)](https://www.youtube.com/watch?v=DvBECqijNDg&t=174s).

**Tloušťka a vrstvení:** **Recompute Point Scale** nastavuje tloušťku kmene — sám o sobě vyrobí pěkný stylizovaný strom [(3:23)](https://www.youtube.com/watch?v=DvBECqijNDg&t=203s) — a **taper profile křivka** ladí průběh od báze ke špičce (`Shift` přidává kontrolní body) [(4:12)](https://www.youtube.com/watch?v=DvBECqijNDg&t=252s). Menší větve = **Graph Distributor** s graph palette a dalším Growerem; density/size/orientation řídí, kde a jak nové větve vyrostou [(4:42)](https://www.youtube.com/watch?v=DvBECqijNDg&t=282s) [(5:15)](https://www.youtube.com/watch?v=DvBECqijNDg&t=315s). Noise element v Mesh Builderu přidá povrchovou variaci [(6:35)](https://www.youtube.com/watch?v=DvBECqijNDg&t=395s), materiál a foliage distributor doplní zbytek [(7:32)](https://www.youtube.com/watch?v=DvBECqijNDg&t=452s) [(7:59)](https://www.youtube.com/watch?v=DvBECqijNDg&t=479s).

**Trik na kořeny:** další Graph Distributor, v parametrických nastaveních snížit **relative end** — nové „větve" se vygenerují dole na kmeni místo v koruně, a po úpravě úhlů a náhodnosti z nich jsou kořenové náběhy [(8:44)](https://www.youtube.com/watch?v=DvBECqijNDg&t=524s) [(9:25)](https://www.youtube.com/watch?v=DvBECqijNDg&t=565s).

**Object Interaction:** strom dostane referenční mesh a tvaruje se kolem něj — posuneš kouli, koruna se přelije; režimy inner/outer cutting větve v průniku rovnou ořežou. Strom rostoucí kolem zdi nebo pod převisem přestává být ruční práce [(10:55)](https://www.youtube.com/watch?v=DvBECqijNDg&t=655s) [(11:28)](https://www.youtube.com/watch?v=DvBECqijNDg&t=688s).

**Extract to Mesh (5.8):** import existujícího stromu do procedurálního systému — rekonstrukce je překvapivě věrná a dál se s ní pracuje jako s čímkoli vypěstovaným od nuly [(12:55)](https://www.youtube.com/watch?v=DvBECqijNDg&t=775s) [(13:16)](https://www.youtube.com/watch?v=DvBECqijNDg&t=796s). Prakticky: **high-poly stromy padají** — autor doporučuje low-poly vstupy (demo se SpeedTree stromem) [(12:05)](https://www.youtube.com/watch?v=DvBECqijNDg&t=725s).

> **Pozn.:** Extract to Mesh je odpověď na největší kritiku 5.7 verze („bere jen presety") — a zároveň zůstává experimentální: nečekej produkční stabilitu, testuj na kopiích. Auto-titulky videa jsou místy rozbité („trapper profile" = taper profile), terminologii ověř v enginu.

**Souvislosti:** [Procedurální stromy (5.7)](#proceduralni-stromy-v-enginu-57) · [Rejstřík: Procedural Vegetation](../rejstrik.md#procedural-vegetation)

---

## Les: PCG graf se skeletal stromy

**Zdroj:** [Unreal Engine 5.7 - PCG Vegatation - Build Your Own Forest - Tutorial (Part 2/2)](https://www.youtube.com/watch?v=4TZG9fBEiR0) · [Unreal - X - Tutorials](https://www.youtube.com/channel/UCjKg7gsHCEyXtJbZYx2Xu7A) · ~6 min, tutoriál

**Shrnutí:** Z vyexportovaných skeletal stromů udělá les jeden krátký graf: **World Ray Hit Query → Surface Sampler → Density Filter → Match and Set Attributes → Instance Skinned Mesh Spawner** — s wind providerem ve spawneru, aby se celý les hýbal [(1:38)](https://www.youtube.com/watch?v=4TZG9fBEiR0&t=98s) [(3:58)](https://www.youtube.com/watch?v=4TZG9fBEiR0&t=238s).

### Rozpad myšlenky

**Řetěz:** graph parameter `trees` jako **skeletal mesh array** (varianty presetů) [(0:50)](https://www.youtube.com/watch?v=4TZG9fBEiR0&t=50s); World Ray Hit Query + Surface Sampler — `D` na uzlu zapne debug bodů; density řídí hustotu, *looseness* rozbíjí mřížku (0 = perfektní grid) [(1:38)](https://www.youtube.com/watch?v=4TZG9fBEiR0&t=98s) [(2:25)](https://www.youtube.com/watch?v=4TZG9fBEiR0&t=145s). Transform Points: rotace Z 360°, scale 0,7–1,3 uniform [(2:25)](https://www.youtube.com/watch?v=4TZG9fBEiR0&t=145s); **Density Filter** prořeže body podle density vah (šedé hodnoty v debugu) [(3:12)](https://www.youtube.com/watch?v=4TZG9fBEiR0&t=192s). **Get Graph Parameter** (property path = `trees`, output attribute `forest`) → Match and Set Attributes → **Instance Skinned Mesh Spawner** s mesh attribute name `forest` [(3:12)](https://www.youtube.com/watch?v=4TZG9fBEiR0&t=192s) [(3:58)](https://www.youtube.com/watch?v=4TZG9fBEiR0&t=238s).

**Dva detaily, které dělají výsledek:** do provider slotu spawneru patří **wind transform provider** — bez něj les stojí [(3:58)](https://www.youtube.com/watch?v=4TZG9fBEiR0&t=238s); a stromy default rostou kolmo ke svahu — **absolute rotation** v Transform Points je narovná, ±5° v X/Y pak vrátí přirozený náklon [(3:58)](https://www.youtube.com/watch?v=4TZG9fBEiR0&t=238s) [(4:46)](https://www.youtube.com/watch?v=4TZG9fBEiR0&t=286s).

**Oblast = volume:** stromy vznikají jen uvnitř bounds PCG volume — posunem a škálováním volume se les tvaruje bez sahání do grafu; dno volume nad terénem znamená prázdné místo [(4:46)](https://www.youtube.com/watch?v=4TZG9fBEiR0&t=286s). Kulisu dotáhne free height mapa + auto materiál z Fabu a jezero z plane s vestavěným water materiálem [(0:03)](https://www.youtube.com/watch?v=4TZG9fBEiR0&t=3s) [(5:33)](https://www.youtube.com/watch?v=4TZG9fBEiR0&t=333s).

> **Pozn.:** Stejný sampler-řetěz jako v [malování dat na landscape](landscape-tipy.md#malovani-dat-paint-layers-ridi-pcg) — liší se jen spawner: static mesh vs. **instance skinned mesh** (skeletal stromy kvůli větru). World Ray Hit Query se tu potvrzuje jako univerzální vstup — doporučovala ho už [Mesh Terrain kapitola](mesh-terrain.md#kanaly-v-praxi-material-malovani-a-pcg) místo vrtkavého Mesh Partition Query.

**Souvislosti:** [Kolize a vítr na dálku](#kolize-a-vitr-na-dalku) · [Landscape tipy: malování dat](landscape-tipy.md#malovani-dat-paint-layers-ridi-pcg) · [Rejstřík: PCG](../rejstrik.md#pcg) · [Rejstřík: Procedural Vegetation](../rejstrik.md#procedural-vegetation)

---

## Kolize a vítr na dálku

**Zdroj:** [How To Add Collision To PCG Wind Trees](https://www.youtube.com/watch?v=Ag6r2YNtSe0) a [Distance Wind Fix - QuickTip](https://www.youtube.com/watch?v=X_83dlYoZ7w) · [Unreal - X - Tutorials](https://www.youtube.com/channel/UCjKg7gsHCEyXtJbZYx2Xu7A) · ~5 + 1 min, tutoriál + tip

**Shrnutí:** Dvě dětské nemoci wind lesa. Stromy nemají kolizi, protože simple/complex kolize umí jen static meshe, skeletal je bere z physics assetu — a **instanced skinned meshe physics asset nepodporují** [(0:02)](https://www.youtube.com/watch?v=Ag6r2YNtSe0&t=2s). A vítr se kus od kamery zastaví. Léčba: neviditelný **statický proxy kolizní mesh** spawnovaný na stejné body [(0:50)](https://www.youtube.com/watch?v=Ag6r2YNtSe0&t=50s) a jeden CVar [(0:03)](https://www.youtube.com/watch?v=X_83dlYoZ7w&t=3s).

### Rozpad myšlenky

**Výroba proxy meshe:** v tree assetu zduplikuj uzly k druhému outputu; Foliage Distributor s ethylene threshold 0 svlékne listí, a chceš-li kolizi jen na kmeni, Remove Branches s basis *generation* a threshold 1 nechá holý kmen [(0:50)](https://www.youtube.com/watch?v=Ag6r2YNtSe0&t=50s) [(1:24)](https://www.youtube.com/watch?v=Ag6r2YNtSe0&t=84s). Export jako static mesh bez kolize, pak v mesh editoru **convex decomposition → apply** s defaulty [(1:51)](https://www.youtube.com/watch?v=Ag6r2YNtSe0&t=111s).

**Napojení v grafu:** Static Mesh Spawner s proxy meshem, **collision preset Block All a vypnutá viditelnost**, připojený na **poslední uzel řady** — stejná pozice, rotace i scale jako strom [(2:19)](https://www.youtube.com/watch?v=Ag6r2YNtSe0&t=139s). U více druhů stromů: druhý parametr-array `collider` **ve stejném pořadí jako `trees`** (index 0 ↔ index 0), vlastní Get Graph Parameter + Match and Set Attributes — a klíčový detail: **zkopíruj seed** z Match and Set uzlu stromů do uzlu colliderů, jinak náhodné párování přiřadí dubu kolizi břízy [(3:09)](https://www.youtube.com/watch?v=Ag6r2YNtSe0&t=189s) [(3:56)](https://www.youtube.com/watch?v=Ag6r2YNtSe0&t=236s).

**Vítr na dálku:** animace instancí se od určité screen size vypne. Konzole: **`r.Skinning.DefaultAnimationMinScreenSize 0`** — všechno se hýbe bez ohledu na vzdálenost, za téměř nulovou cenu; default je 0,1 a vyšší hodnota culling vrací [(0:03)](https://www.youtube.com/watch?v=X_83dlYoZ7w&t=3s).

> **Pozn.:** Instanced skinned mesh + statický proxy je řádově levnější než spawnovat plné skeletal actory — tisíce animovaných stromů „skoro zadarmo" [(3:56)](https://www.youtube.com/watch?v=Ag6r2YNtSe0&t=236s). Stejný problém řeší jinou cestou [Rbnks nástroj](#hotovy-nastroj-pcg-forest-per-vrstvy-a-s-kolizi) — kapslí v blueprintu; proxy z convex decomposition sedí na tvar stromu přesněji.

**Souvislosti:** [Les přes PCG](#les-pcg-graf-se-skeletal-stromy) · [Rejstřík: bounds](../rejstrik.md#bounds) · [Rejstřík: Physics Asset](../rejstrik.md#physics-asset)

---

## Mýtiny a cesty

**Zdroj:** [Unreal Engine 5.7 - Create Forest Clearings & Paths With PCG - Tutorial](https://www.youtube.com/watch?v=8UxAmQfIj5s) · [Unreal - X - Tutorials](https://www.youtube.com/channel/UCjKg7gsHCEyXtJbZYx2Xu7A) · ~8 min, tutoriál

**Shrnutí:** Les je plný — teď do něj vyříznout prostor. Tři nástroje se stupňující flexibilitou: **blocking volume** (rychlá mýtina), **uzavřená spline** (libovolný tvar) a **spline cesty**, která nejen odstraní stromy, ale rovnou spawne decal cesty a kamení podél [(0:02)](https://www.youtube.com/watch?v=8UxAmQfIj5s&t=2s). Všechno přes jeden Difference uzel — a všechno živé: posun splinu přegeneruje les okamžitě [(7:56)](https://www.youtube.com/watch?v=8UxAmQfIj5s&t=476s).

### Rozpad myšlenky

**Mýtina z volume:** Blocking Volume do levelu (brush shape cylinder pro kulatou mýtinu; **no collision**, ať skrz projde postava) [(0:02)](https://www.youtube.com/watch?v=8UxAmQfIj5s&t=2s) [(0:48)](https://www.youtube.com/watch?v=8UxAmQfIj5s&t=48s). V grafu: **Get Volume Data** (all world actors, by class BlockingVolume, select multiple) → **Volume Sampler** → **Difference** — volume do difference pinu, surface sampler lesa do source; výstup pokračuje do transform points [(0:48)](https://www.youtube.com/watch?v=8UxAmQfIj5s&t=48s) [(1:34)](https://www.youtube.com/watch?v=8UxAmQfIj5s&t=94s). Další mýtina = zkopírovat volume, les se srovná sám [(1:34)](https://www.youtube.com/watch?v=8UxAmQfIj5s&t=94s).

**Mýtina ze splinu:** modeling mode → Draw Spline s uzavřenou smyčkou, po Accept aktoru přidat **tag** (`clearing`) [(1:34)](https://www.youtube.com/watch?v=8UxAmQfIj5s&t=94s) [(2:20)](https://www.youtube.com/watch?v=8UxAmQfIj5s&t=140s). Graf: **Get Spline Data** (by tag, select multiple) → **Spline Sampler** s dimension **on interior**, interior spacing 50 a **unbounded** [(2:20)](https://www.youtube.com/watch?v=8UxAmQfIj5s&t=140s) [(3:07)](https://www.youtube.com/watch?v=8UxAmQfIj5s&t=187s). Aby body seděly na terénu: **Get Landscape Data + Projection** (landscape do target, sampler do input) → difference pin [(3:07)](https://www.youtube.com/watch?v=8UxAmQfIj5s&t=187s).

**Cesta:** spline s tagem `forest path`; Spline Sampler tentokrát **on spline** s mode distance + unbounded + projekce (Get Landscape Data se recykluje) [(4:43)](https://www.youtube.com/watch?v=8UxAmQfIj5s&t=283s) [(5:29)](https://www.youtube.com/watch?v=8UxAmQfIj5s&t=329s). Šířku průseku určuje **Bounds Modifier** (debug `D`, min/max bounds) → difference pin [(5:29)](https://www.youtube.com/watch?v=8UxAmQfIj5s&t=329s). A tady se cesta stává cestou: z bounds modifieru větev → Transform Points (rotace Z 360) → **Spawn Actor** s template třídou decal blueprintu (decal actor + free Mega Skin decal materiál) — povrch cesty kopíruje spline [(3:55)](https://www.youtube.com/watch?v=8UxAmQfIj5s&t=235s) [(6:17)](https://www.youtube.com/watch?v=8UxAmQfIj5s&t=377s); druhá větev → Transform Points → Static Mesh Spawner s kamením a smetím podél [(7:03)](https://www.youtube.com/watch?v=8UxAmQfIj5s&t=423s).

**Decal pasti:** postavě vypni **Receive Decals** v character BP, jinak se cesta promítne na ni [(6:17)](https://www.youtube.com/watch?v=8UxAmQfIj5s&t=377s); u kamenů v parent materiálu **decal response = none** [(7:03)](https://www.youtube.com/watch?v=8UxAmQfIj5s&t=423s).

> **Pozn.:** Stejná myšlenka jako [výřezy kolizemi](pcg-zaklady.md#vyrezy-podle-kolizi-a-debug-grafu) — Difference je univerzální „tady ne" — jen zdroj výřezu je tentokrát autorský záměr (volume, spline), ne spawnovaná překážka. Kombinují se volně: mýtiny + cesty + kolizní výřezy v jednom grafu.

**Souvislosti:** [PCG základy: výřezy](pcg-zaklady.md#vyrezy-podle-kolizi-a-debug-grafu) · [Rejstřík: spline](../rejstrik.md#spline) · [Rejstřík: decal](../rejstrik.md#decal)

---

## Hotový nástroj: PCG Forest per vrstvy a s kolizí

**Zdroj:** [How to integrate PCG with landscape layers - Part 2](https://www.youtube.com/watch?v=hEHF0x22LpY) a [Create a PCG forest with the new Megaplants and Collision](https://www.youtube.com/watch?v=ryb0sb2SQ-U) · [Rbnks](https://www.youtube.com/channel/UCADQ4N7nSoCmCklU0KeXntQ) · ~10 + 8 min, produktová videa

**Shrnutí:** Rbnksův **PCG Forest** je placený nástroj (Fab/Gumroad) — celý les jako blueprint s data assety místo grafů. Obě videa jsou update dema vlastního produktu, a přesto nesou dvě přenositelné lekce: jak vypadá **vegetace řízená landscape paint vrstvami** dotažená do UX, a že **na enginové limity kolizí narazí i hotové nástroje** [(0:04)](https://www.youtube.com/watch?v=ryb0sb2SQ-U&t=4s).

### Rozpad myšlenky

**Vrstvy jako region:** data asset každého druhu vegetace (tráva, vysoká tráva, květiny, stromy) dostal *use paint layer info* + pole na **přesné jméno landscape vrstvy** (L0, L1…) — tráva na L0, vysoká tráva na L1, cesta namalovaná třetí vrstvou vegetaci maže; víc assetů smí sdílet vrstvu a nepřiřazený asset roste všude [(4:25)](https://www.youtube.com/watch?v=hEHF0x22LpY&t=265s) [(5:11)](https://www.youtube.com/watch?v=hEHF0x22LpY&t=311s) [(6:42)](https://www.youtube.com/watch?v=hEHF0x22LpY&t=402s) [(8:02)](https://www.youtube.com/watch?v=hEHF0x22LpY&t=482s). Malování i posun blueprintu se projevují okamžitě a funguje to i ve world partition variantě [(7:47)](https://www.youtube.com/watch?v=hEHF0x22LpY&t=467s) [(8:34)](https://www.youtube.com/watch?v=hEHF0x22LpY&t=514s). Je to tentýž vzor, který [Landscape tipy](landscape-tipy.md#malovani-dat-paint-layers-ridi-pcg) staví ručně (Filter Attribute Elements na jméno vrstvy) — tady zabalený do checkboxu.

**Kolize po druhé:** update reaguje na tutéž bolest jako [DIY řešení výš](#kolize-a-vitr-na-dalku) — skeletal stromy přes PCG nekolidují. Nástroj to řeší obalem: mega plants strom žije v **blueprintu s kapslí** na kmeni (výška/radius se ladí per strom) a data asset odkazuje na blueprinty [(0:50)](https://www.youtube.com/watch?v=ryb0sb2SQ-U&t=50s) [(3:21)](https://www.youtube.com/watch?v=ryb0sb2SQ-U&t=201s). Vítr je i tady ruční krok: tree komponenta → transform provider = **wind transform provider**, řízení přes Global Foliage Actor (rychlost, směr, season/health) [(6:04)](https://www.youtube.com/watch?v=ryb0sb2SQ-U&t=364s) [(6:59)](https://www.youtube.com/watch?v=ryb0sb2SQ-U&t=419s). Setup vyžaduje stejné pluginy jako DIY cesta (Nanite foliage + Procedural Vegetation Editor; „nanite assembly" warning znamená, že chybí) [(2:12)](https://www.youtube.com/watch?v=ryb0sb2SQ-U&t=132s).

**Co koupí nekoupíš:** kapsle je hrubší aproximace než convex proxy z [DIY postupu](#kolize-a-vitr-na-dalku) a autor sám přiznává „not that advanced" s tím, že ohýbající se tráva je teprve výhled [(7:46)](https://www.youtube.com/watch?v=ryb0sb2SQ-U&t=466s).

> **Pozn.:** Produktová videa — Part 1 nástroje v playlistu není a tahle dvě nejsou návod, jak si systém postavit, ale jak vypadá, když ho někdo dotáhne do produktu. Čti je jako badatelský vzorek: checkbox „use paint layer info" je přesně ta míra UX, ke které směřuje vlastní graf, a blueprint-obal s kapslí ukazuje, že proxy kolize není hack, ale standardní řešení.

**Souvislosti:** [Landscape tipy: malování dat](landscape-tipy.md#malovani-dat-paint-layers-ridi-pcg) · [Kolize a vítr na dálku](#kolize-a-vitr-na-dalku) · [Nástroje: EasyWaterscape](nastroje-voda.md#easywaterscape-jak-je-poskladany-dobry-vodni-nastroj) · [Rejstřík: data asset](../rejstrik.md#data-asset)

---

## Les pro otevřený svět: co se načte s levelem a co roste kolem hráče

**Zdroj:** [Building Open World Forests: The Fastest Way in UE5](https://www.youtube.com/watch?v=ufZrhbZWPto) · [Aziel Arts](https://www.youtube.com/channel/UCxGoreKfZxDBxJzirLWuOuw) · ~40 min, tutoriál (s autorovým nástrojem QuickScatter)

**Shrnutí:** Malování foliage, ruční rozmisťování i složité PCG grafy fungují na malé ploše. Na několika kilometrech čtverečních ale narazí na limity hardwaru [(1:03)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=63s). Aziel Arts proto hustý biom dělí na dvě skupiny. Velké věci, které chceš vidět z dálky a které často potřebují kolizi, se spočítají na CPU a autor je zapeče do blueprintu. Hustý pokryv země se generuje za běhu, jen v buňkách kolem hráče. Háček: hranice mezi skupinami není pevná. Rozhoduje, jestli věc musí být vidět z dálky a vydržet, nebo jestli je jí tolik, že by se přes celý svět spočítat nedala. Hraniční případy autor nechává na tobě.

### Rozpad myšlenky

**Recept z reference.** Meshe jsou podle autora ingredience receptu a jejich výběr rozhoduje o výkonu i o výtvarném dojmu [(2:48)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=168s). Referencí jsou vlastní fotky borového lesa na Cape Codu. Z nich vytáhne velké prvky, které dávají biomu chuť: borovice, jehličí na zemi, bílý písek, který mezi ním prosvítá, velký zelený keř a drobné větvičky [(7:25)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=445s). Přesně tak sukovité borovice nenašel, a tak vzal rovnější a vyšší, nejspíš jiný druh. Reference má být inspirace, ne předloha jedna k jedné [(8:11)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=491s). Vybrané meshe si nejdřív postaví vedle sebe do pomocného levelu, aby viděl, jestli k sobě sedí [(3:34)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=214s). Pak je dá do lokální kolekce v Content Browseru, aby je ve velkém asset packu nemusel hledat [(8:58)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=538s).

**Dvě skupiny.** Onload objekty jsou větší a často potřebují kolizi [(5:06)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=306s). Hlavně je chceš vidět z dálky: když se podíváš na kopec naproti, mají na něm stát stromy. Patří sem stromy a skály. Runtime skupina je pokryv země, tedy jehličí, klacky a rostlinky. Je tak hustý, že se nesmí generovat přes kilometry najednou, a přepočítává se kolem postavy, jak se pohybuje [(5:52)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=352s). Hraniční případy, třeba velký pařez nebo větší rostlina s kolizí, jsou na tobě. Autor doporučuje vyzkoušet obojí.

**Biome map.** Kde je který biom, říká barevná mapa přes celý landscape [(10:30)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=630s). Nejjednodušší cesta je screenshot terénu shora, přes který v Paintu, Photoshopu nebo Photopea namaluješ barvy biomů. Mapa musí na landscape sedět přesně. Textuře mapy se podle autora vyplatí zapnout Never Stream, protože jinak se mu po znovuotevření levelu sama nenačítala [(12:05)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=725s) [(12:52)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=772s). Každý scatter pak dostane barvu svého biomu a roste jen v ní.

**Hustota a shluky.** Hustota se zadává jako počet bodů na metr čtvereční a jednička znamená hodně [(15:10)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=910s). Velké keře autor nakonec zkusí stáhnout na 0,1 nebo 0,05 [(20:35)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=1235s). Vzhled shluků dělá spatial noise, černobílý vzor, který meshe škáluje a v černých místech vyřízne [(19:02)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=1142s). Větší size, třeba 2000 až 3000, dá větší shluky. Vyšší strength zostří rozdíl mezi shlukem a prázdným místem [(19:48)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=1188s). Na odhad hustoty pomůže reference ze vzduchu, třeba záběr z dronu. Každá skupina má vlastní seed noisu. Když mají větve stejný seed a size jako jiné rostliny, často se sesypou na stejná místa a stačí seed změnit [(32:36)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=1956s).

**Onload: CPU, kolize a zapečení.** Velké objekty autor přepne z GPU spawnu na CPU [(21:03)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=1263s). Je to pomalejší, ale meshe spawnované na GPU nemůžou mít kolizi. Pak volí mezi generováním při načtení levelu a zapečením. Před zapečením nastaví stíny, u velkých objektů dynamické, a zapne kolizi [(21:50)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=1310s). Clear PCG Link vyrobí PCG stamp, blueprint s instancovanými meshi, který se při startu levelu načte okamžitě. Původní generátor se pak vypne [(22:37)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=1357s). Když je potřeba les změnit, stamp smažeš, generátor zapneš a upravíš. Během ladění je rychlejší pracovat na GPU a na CPU přepnout až před dalším zapečením [(34:10)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=2050s).

**Runtime: buňky kolem hráče.** Generate at Runtime samo nestačí. Bez Is Partitioned se pořád generuje celý objem najednou [(23:40)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=1420s). Partitions rozsekají oblast výpočtu na buňky, které se načítají a uvolňují. Po jednotlivých bodech to na GPU nejde, proto buňky [(24:27)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=1467s). Výsledkem je řádově víc hustoty přímo kolem hráče a bez toho by jehličí přes celou zem nešlo. Generation grid size určuje velikost buňky. V pokročilém nastavení má každá velikost buňky vzdálenost, do které se generuje [(25:14)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=1514s). Méně velkých buněk je pro počítač lehčí, ale můžou se načítat zbytečně daleko. Malé buňky dají kolem postavy kulatější tvar, jenže když jich je moc, výpočet zpomalí [(26:01)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=1561s). Autor drží 1600 na blízko a 3200 na střední vzdálenost. Moc velká mřížka podle něj ztrácí smysl, protože pak generuješ celý svět najednou. Co je nejrychlejší, si ověř na vlastním stroji [(26:48)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=1608s). Jehličí s hustotou 2 běží za běhu rychle. V onload skupině by se při stejné hustotě všechno nejspíš začalo sekat [(28:42)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=1722s).

**Drobnosti pokryvu.** Pokryv začíná jehličím. Podle autora se ladí nejhůř a tvoří základ lesní půdy, a pokryvem země prý často začíná, protože zabere nejvíc plochy [(27:56)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=1676s). Jehličí plavalo nad zemí, takže ho autor posunul o −2 v Z [(29:31)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=1771s). Na runtime skupinu dá contact shadows. Jsou skoro zadarmo, protože fungují jako stín vržený z výřezu objektu a nesimulují se jako běžné stíny. Aby se ukázaly, potřebuje directional light nastavenou contact shadow length. Stíny se pak hýbou se sluncem [(30:17)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=1817s). Doskakování buněk na úrovni očí skoro nevidíš. Kdyby vadilo, pomůže fade nebo postupné zvětšení v materiálu rostlin. Měřítko nakonec ověř tak, že lesem projdeš s postavou [(33:23)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=2003s).

**Cesty a řeky.** Průsek začíná vždy spline, třeba z Modeling Tools [(35:00)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=2100s). Maskou může být aktor nebo blocking volume, třeba kolem domu nebo vesnice [(35:46)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=2146s). U spline volíš vyříznutí uvnitř nebo vně volume, případně uvnitř nebo vně cesty, a mask extend určí šířku průseku [(36:33)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=2193s). Masku musí dostat obě skupiny, onload i runtime. S pluginem Water jde stejnou spline jedním skriptem převést na řeku. Skript je přibalený k nástroji [(37:21)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=2241s) [(38:08)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=2288s).

> **Pozn.:** Video je ukázka autorova vlastního nástroje QuickScatter. Popis videa ho představuje jako GPU scatter nástroj s odkazem na autorův web [(0:16)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=16s) a na konci autor zve do své akademie a kurzů [(38:55)](https://www.youtube.com/watch?v=ufZrhbZWPto&t=2335s). Obojí je promo. Přenositelné je rozhodnutí o dvou skupinách a samotná nastavení. Volby Generate at Runtime a Is Partitioned i velikost mřížky popisuje bez nástroje [Foliage optimalizace II](optimalizace.md#foliage-optimalizace-ii-gpu-scatter-a-runtime-kvalita), i s volbou treat editor viewport as runtime. Toto propojení je naše. Kolizi tu omezuje jiná příčina než u [skeletal stromů](#kolize-a-vitr-na-dalku): tam chybí physics asset, tady jde o GPU spawn. Průseky stojí na stejném principu jako [mýtiny a cesty](#mytiny-a-cesty).

**Souvislosti:** [Les přes PCG](#les-pcg-graf-se-skeletal-stromy) · [Hotový nástroj: PCG Forest](#hotovy-nastroj-pcg-forest-per-vrstvy-a-s-kolizi) *(druhý nástroj, jiné řešení kolizí)* · [Rejstřík: Runtime generation](../rejstrik.md#runtime-generation) · [Rejstřík: Biome map](../rejstrik.md#biome-map) · [Rejstřík: Spatial Noise](../rejstrik.md#spatial-noise) · [Rejstřík: Contact shadows](../rejstrik.md#contact-shadows)
