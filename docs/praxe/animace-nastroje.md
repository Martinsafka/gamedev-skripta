# Animační nástroje: AnimBP, mocap zdarma a Locomotor

Tři nástroje pro tři situace: **animation blueprint se state machine** (klasika, kterou je potřeba umět číst, i když svět míří k [Motion Matchingu](mm-zaklady.md)), **markerless mocap v 5.8** (video z telefonu → animace, oficiálně a zdarma) a **Locomotor** pro tvory, které by ručně nikdo klíčovat nechtěl. Dohromady uzavírají animační blok: kde animace *vzít* a jak je rozehrát.

---

## AnimBP od nuly: state machine, třídílný skok a blend space

**Zdroj:** [How To Animate Your Character In UE5 With Animation Blueprint And Blendspace](https://www.youtube.com/watch?v=BuoeWNQOe0Y) · [Matt Aspland](https://www.youtube.com/channel/UC8_RNwftEO4isrX2LJowcpg) · ~17 min, tutoriál

**Shrnutí:** Kompletní AnimBP pro libovolnou postavu (hráč i NPC): [state machine](../rejstrik.md#state-machine) Locomotion se stavem idle/walk/run (jeden stav — uvnitř blenduje [blend space](../rejstrik.md#blend-space) podle rychlosti) a **třídílným skokem** start → loop → end. Dva vzory k zapamatování: **automatic rule** místo ručních podmínek a AnimBP **bez castu**, který funguje na jakékoli postavě se správným skeletonem.

### Rozpad myšlenky

**Proč skok na tři části** [(2:22)](https://www.youtube.com/watch?v=BuoeWNQOe0Y&t=142s): jedna animace skoku by musela délkou přesně sedět na dobu letu — tři části (odraz, smyčka ve vzduchu s `Loop Animation`, dopad) se přizpůsobí *jakkoli* dlouhému skoku. Přechody odraz → smyčka a dopad → locomotion neřeší žádná proměnná: **Automatic Rule Based on Sequence Player in State** přepne, jakmile animace dohraje [(3:08)](https://www.youtube.com/watch?v=BuoeWNQOe0Y&t=188s). Zbylé dva přechody řídí bool `jumping` ← `Is Falling` z movement componentu (a jeho negace) [(6:15)](https://www.youtube.com/watch?v=BuoeWNQOe0Y&t=375s).

**AnimBP bez castu** [(4:40)](https://www.youtube.com/watch?v=BuoeWNQOe0Y&t=280s): `Try Get Pawn Owner → Get Movement Component` → velocity → vector length → `speed`. Žádný cast na konkrétní blueprint znamená, že tentýž AnimBP obslouží hráče, NPC i figurínu — jediná podmínka je stejný skeleton. Stejná filozofie jako [interface přístup](komunikace-blueprintu.md), jen zadarmo.

**Blend space prakticky:** osa speed 0–max, `Snap to Grid`, smoothing time ~0,5 s (vyšší = měkčí, pomalejší přechody) [(8:34)](https://www.youtube.com/watch?v=BuoeWNQOe0Y&t=514s). Dvě lekce z ladění naživo: když animace „nesedí na rychlost", uprav **rychlost postavy k animacím**, ne obráceně (pomalý brute má chodit pomalu) [(14:46)](https://www.youtube.com/watch?v=BuoeWNQOe0Y&t=886s) — miniverze pravidla [movement model first](mm-zaklady.md#sparse-set-13-animaci-staci-na-start); a při snižování maxima osy **napřed smaž klipy, pak měň hodnotu** — klipy mimo rozsah sypou chyby [(14:46)](https://www.youtube.com/watch?v=BuoeWNQOe0Y&t=886s).

> **Pozn.:** Tohle je „stará škola", kterou GASP éra nahrazuje MM uzlem — ale číst state machines je pořád denní chleba (AnimBP šablon, cizích projektů, i [hybridního GASP setupu](gasp.md#mover-pohyb-jako-modularni-blueprintovatelna-simulace)). A pro jednoduchá NPC je state machine se třemi stavy pořád nejlevnější správná odpověď.

**Souvislosti:** [Základy pohybu: blend spacy](pohyb-zaklady.md#tri-rychlosti-walk-run-sprint-pres-max-walk-speed) · [MM základy: proč pryč od state machines](mm-zaklady.md#dotaz-misto-grafu-jak-motion-matching-vybira-pozy) · [Art specializace: animace](../teorie/art-specializace.md#animace-citelnost-vaha-a-osobnost) *(proč state machine vůbec vzniká — a co má animace sdělit)* · [Rejstřík: state machine](../rejstrik.md#state-machine) · [Rejstřík: blend space](../rejstrik.md#blend-space)

---

## Markerless mocap v 5.8: z videa na animaci bez obleku

**Zdroj:** [The Fastest "Video to Animation" Tutorial in UE5.8](https://www.youtube.com/watch?v=SHP5fBaTPJQ) · [Kartoon Develop Tips](https://www.youtube.com/channel/UCy_o6kSJ3MdjOysXWLwqBRg) · ~7 min ·
[MetaHuman Markerless Mocap Tutorial FREE in Unreal 5.8](https://www.youtube.com/watch?v=iJXJO-J7z3g) · [Thomas Halpin](https://www.youtube.com/channel/UCb3mBiZmLNj7ATWZ2m_Qu0w) · ~5 min ·
[Unreal Engine 5.8 NEW Markerless Motion Capture Tutorial](https://www.youtube.com/watch?v=kxsncXh8hhM) · [World Of VFX](https://www.youtube.com/channel/UCWP2AikFs8LlH0ajpnQiT7w) · ~5 min

**Shrnutí:** Od 5.8 je v enginu oficiální **markerless mocap**: obyčejné video (jedna kamera, žádné markery, žádný oblek) → animace těla *i obličeje*. Pipeline: Fab plugin **MetaHuman Animator Markerless Motion Capture** → video na capture data přes **Live Link Hub** → **MetaHuman Performance** asset s body trackingem → export a retarget na libovolný skeleton.

### Rozpad myšlenky

**Setup:** plugin z Fabu nainstalovat *do enginu* (jen 5.8) [(0:01)](https://www.youtube.com/watch?v=kxsncXh8hhM&t=1s), v editoru zapnout MetaHuman sadu + Live Link (Hub) a restart [(0:02)](https://www.youtube.com/watch?v=iJXJO-J7z3g&t=2s). Pozor při instalaci enginu: **MetaHuman Creator Core Data** v options — bez něj MetaHumana nevytvoříš [(0:47)](https://www.youtube.com/watch?v=SHP5fBaTPJQ&t=47s).

**Video → capture data:** MP4 engine neumí přímo — Tools → **Live Link Hub** → přepnout z Live Data na **Capture Manager** → **Mono Video Ingest** → složka s videem → Add to Queue → Start [(2:22)](https://www.youtube.com/watch?v=SHP5fBaTPJQ&t=142s). Otočené video z mobilu srovná rotate 90° v output nastavení [(1:27)](https://www.youtube.com/watch?v=iJXJO-J7z3g&t=87s); audio se zpracuje automaticky [(1:33)](https://www.youtube.com/watch?v=kxsncXh8hhM&t=93s).

**Performance:** right-click → MetaHuman → **MetaHuman Performance**: vybrat capture data, **zaškrtnout Body Tracking** (default trackuje jen obličej!) [(4:46)](https://www.youtube.com/watch?v=SHP5fBaTPJQ&t=286s), přiřadit MetaHumana a Process. Počítej s časem: 4K/60fps klip ~10 minut [(3:20)](https://www.youtube.com/watch?v=iJXJO-J7z3g&t=200s), delší záběr ~20 [(2:20)](https://www.youtube.com/watch?v=kxsncXh8hhM&t=140s). **Export Animation** pak nabídne performer/existující skeleton a výsledek nese i blend shapes obličeje [(3:51)](https://www.youtube.com/watch?v=iJXJO-J7z3g&t=231s) — v sequenceru vypnout control rigy a přidat animaci na body i face [(4:19)](https://www.youtube.com/watch?v=iJXJO-J7z3g&t=259s); retarget na vlastní postavu klasicky [(5:48)](https://www.youtube.com/watch?v=SHP5fBaTPJQ&t=348s).

**Co od toho čekat:** kvalita animace = kvalita videa. Kartoon to poctivě limit-testoval na nízkorozlišeném anime klipu — „kind of worked" [(0:01)](https://www.youtube.com/watch?v=SHP5fBaTPJQ&t=1s); čisté video s celou postavou v záběru dává překvapivě dobré ruce i gesta [(2:20)](https://www.youtube.com/watch?v=kxsncXh8hhM&t=140s).

> **Pozn.:** Pro nás přesně ten nástroj, o kterém mluvil [sparse set](mm-zaklady.md#sparse-set-13-animaci-staci-na-start): vlastní mocap „za cenu telefonu na stativu" — prototyp gest vesničanů, interakčních animací nebo referencí pro ruční doladění. Drobné pasti z videí: první rig MetaHumana chce potvrzení licence na webu (jinak tiše selže) a hláška o project settings se řeší „enable missing" + GPU skin volby [(3:11)](https://www.youtube.com/watch?v=SHP5fBaTPJQ&t=191s).

**Souvislosti:** [MM základy: sparse set a vlastní animace](mm-zaklady.md#sparse-set-13-animaci-staci-na-start) · [Rejstřík: MetaHuman](../rejstrik.md#metahuman) · [Rejstřík: Live Link](../rejstrik.md#live-link)

---

## Procedurální pavouk: Locomotor, foot sets a fázové offsety

**Zdroj:** [EASY Procedural Spider Animation in UE5 | Locomotor + Control Rig Tutorial](https://www.youtube.com/watch?v=uhjN4jf3q6k) · [Tank Control Games](https://www.youtube.com/channel/UCoHLpKMSi5LlOMFlxuoR1rA) · ~11 min, tutoriál

**Shrnutí:** Osm nohou, nula animačních klipů: **Locomotor** uzel v Control Rigu počítá došlapy dynamicky podle pohybu — a **fázové offsety** foot setů (0 / 0,25 / 0,5 / 0,75) udělají z unisono cupitání věrohodnou pavoučí chůzi [(5:15)](https://www.youtube.com/watch?v=uhjN4jf3q6k&t=315s). Ruční klíčování plné locomotion sady pro pavouka by trvalo týdny; tohle je hotové za hodinu [(10:44)](https://www.youtube.com/watch?v=uhjN4jf3q6k&t=644s).

### Rozpad myšlenky

**Stavba rigu:** Control Rig na skeletal meshi, nový control „target control" na rootu (za něj se tvor tahá) [(0:49)](https://www.youtube.com/watch?v=uhjN4jf3q6k&t=49s) → **Locomotor uzel** do forward solve, root control = target [(1:37)](https://www.youtube.com/watch?v=uhjN4jf3q6k&t=97s). **Foot sets**: čtyři sady po levé+pravé noze, každá noha = ankle bone (koncová kost) [(2:25)](https://www.youtube.com/watch?v=uhjN4jf3q6k&t=145s). Pak **Full Body IK**: root = tělo, effector na špičku každé nohy, transformy z locomotoru přes `At` uzel s inkrementovaným indexem [(6:03)](https://www.youtube.com/watch?v=uhjN4jf3q6k&t=363s) — teprve tím se procedurální došlapy propíšou do kostí.

**Ladění pro malé nožky:** default Collision Radius a Max Collision Height jsou na pavouka moc (nohy blízko sebe → strkají se do země) — radius 0,5, výška ~1–1,5, zadní nohy až 0,1 [(2:25)](https://www.youtube.com/watch?v=uhjN4jf3q6k&t=145s), [(4:28)](https://www.youtube.com/watch?v=uhjN4jf3q6k&t=268s). Hromadná editace: vybrat Locomotor uzel a v details vyhledat parametr — ukážou se všechna pole napříč foot sety [(3:58)](https://www.youtube.com/watch?v=uhjN4jf3q6k&t=238s). Charakter chůze pak ladí pelvis settings (bob stiffness, lead amount) a stepping (step height, ease in/out) [(7:35)](https://www.youtube.com/watch?v=uhjN4jf3q6k&t=455s).

**Zapojení do hry:** AnimBP = **Sequence Player (idle) → Control Rig uzel** → output pose [(8:21)](https://www.youtube.com/watch?v=uhjN4jf3q6k&t=501s) — idle animace dýchá tělem, rig řídí nohy. BP pavouka = duplikát třetíosobní postavy s vyměněným meshem a anim classou [(9:11)](https://www.youtube.com/watch?v=uhjN4jf3q6k&t=551s); rychlost postavy srazit (~150), ať kapsle neujíždí krokům — nebo zrychlit kroky v rigu [(9:58)](https://www.youtube.com/watch?v=uhjN4jf3q6k&t=598s).

> **Pozn.:** Stejný Locomotor, kterým Epic v [GASP](gasp.md#proceduralni-vrstva-v-control-rigu-foot-placement-springy-a-locomotor) prohání mecha — tady na organickém tvorovi a s návodem krok za krokem. Vzor „idle klip jako podklad + procedurální končetiny" škáluje na cokoli vícenohého (brouci, krabi, mytologičtí pavouci do našeho lesa) a míří přesně tam, kam Epic tlačí celou animaci: RigVM grafy místo klipů.

**Souvislosti:** [GASP: procedurální vrstva a Locomotor](gasp.md#proceduralni-vrstva-v-control-rigu-foot-placement-springy-a-locomotor) · [Rejstřík: Locomotor](../rejstrik.md#locomotor) · [Rejstřík: Control Rig](../rejstrik.md#control-rig)

---

## SAM: izolace jednoho aktéra jako animátorský režim

**Zdroj:** [New FREE Animation Tool in Unreal Engine 5.8 | (S.A.M) Solo Animation Mode](https://www.youtube.com/watch?v=-mcMxpVmnAM) · [Proj Prod](https://www.youtube.com/channel/UCs37G0ljE4hPSddC_gdD_Mw) · ~13 min, představení nástroje

**Shrnutí:** Bezplatný **editor utility widget**, který na jedno kliknutí schová celou scénu kromě vybraného aktéra a nahradí prostředí neutrálním pozadím s rovnoměrným světlem. Vznikl *„po sbírání zpětné vazby od animátorů v různých studiích"* s explicitním cílem **pomoct animátorům přijmout Unreal jako animační nástroj** — a to je zajímavější než sám nástroj: ukazuje, co konkrétně animátorům v UE vadí.

### Rozpad myšlenky

**Co Isolate udělá** [(1:37)](https://www.youtube.com/watch?v=-mcMxpVmnAM&t=97s): vyber aktéra → klik → všechno ostatní zmizí a v outlineru se dočasně objeví **tři aktéři: kamera, prostředí a post process volume**. Izolovat jde nejen skeletal meshe, ale i statické meshe, blueprint aktéry a **spawnable aktéry ze sekvenceru** [(4:44)](https://www.youtube.com/watch?v=-mcMxpVmnAM&t=284s).

**Světla připnutá na kameru** [(2:24)](https://www.youtube.com/watch?v=-mcMxpVmnAM&t=144s) jsou hlavní trik: *„místo abych se spoléhal na směrové světlo levelu a řešil rušivé stíny, nástroj připne vlastní směrová světla přímo na kameru."* Postavu tak posoudíš z jakéhokoli úhlu za stejných podmínek — což je přesně to, co animátor potřebuje a co osvětlení scény systematicky znemožňuje. Volitelně jde světla levelu vrátit (`keep lights`), prostředí vypnout nebo přidat **contact shadows** pro víc hloubky.

**Přepínání na kameru sekvenceru** [(2:24)](https://www.youtube.com/watch?v=-mcMxpVmnAM&t=144s) obsahuje detail, který prozrazuje, že autor s tím opravdu pracuje: přepíná se **na camera cuts track**, ne na pilotování cine camera actoru — *„což pomáhá vyhnout se nechtěným klíčům, hlavně když máš zapnutý auto key."* SAM kamera přitom zůstane, kde jsi ji nechal, takže se dá mezi „prohlížím si postavu" a „koukám se záběrem" plynule skákat.

**Silhouette mode** [(5:30)](https://www.youtube.com/watch?v=-mcMxpVmnAM&t=330s): plná silueta s volitelnou barvou postavy i pozadí, `G` skryje ovladače. *„Užitečné pro kompozici, ladění záběru a soustředění na celkový tvar a čitelnost animace."* Je to praktická podoba [line of action a siluety](../teorie/art-specializace.md#animace-citelnost-vaha-a-osobnost) — pravidla, které se v barevném viewportu špatně kontroluje.

**Drobnosti, které dělají rozdíl** [(4:44)](https://www.youtube.com/watch?v=-mcMxpVmnAM&t=284s): `hide sprites` a `hide camera icons` — ikony blueprintů a kamer v hledáčku při animování ruší a jdou vypnout jedním klikem, aniž zmizí ovládací prvky. A **`Isolate by tag`** [(7:03)](https://www.youtube.com/watch?v=-mcMxpVmnAM&t=423s), který izoluje podle actor tagu bez ručního výběru: *„u layoutů se složitým prostředím můžeš označit skupiny a rychle mezi nimi přepínat."* Vedlejším přínosem je **výkon** — izolovaný viewport je u složité scény podstatně lehčí.

**Restore jako designové rozhodnutí** [(3:57)](https://www.youtube.com/watch?v=-mcMxpVmnAM&t=237s): jedním klikem se vrátí původní stav a **dočasní aktéři se smažou**; totéž se stane při zavření nástroje. *„To pro mě bylo hodně důležité designové rozhodnutí."* Nástroj, který ti může nechat v levelu odpadky, se totiž na produkčním projektu nepoužívá — bez ohledu na to, co umí.

> **Pozn.:** Pod kapotou jsou to tři triviální věci — kamera s vlastním meshem (aby šla odlišit od běžné), **sky sphere s plochým materiálem** a post process volume — a autor **graf záměrně nechal rozbalený a neuklizený** [(9:23)](https://www.youtube.com/watch?v=-mcMxpVmnAM&t=563s): *„mohl jsem přidat víc proměnných a funkcí, aby byla struktura čistší, ale cílem bylo dát vám přístup k celému systému, abyste mu rozuměli a mohli z něj iterovat."* Je to legitimní protiklad k [čistým grafům](organizace-projektu.md#devet-tipu-proti-spagetam-v-grafech): u nástroje určeného k rozebrání je čitelnost pro cizího důležitější než elegance. Funguje v **5.7 i 5.8**.

**Souvislosti:** [Animace: line of action a osobnost](../teorie/art-specializace.md#animace-citelnost-vaha-a-osobnost) *(co silueta kontroluje)* · [Editor tipy](editor-tipy.md) · [Organizace projektu: čisté grafy](organizace-projektu.md#devet-tipu-proti-spagetam-v-grafech) · [Rejstřík: Editor Utility Widget](../rejstrik.md#editor-utility-widget) · [Rejstřík: Silueta](../rejstrik.md#silueta)
