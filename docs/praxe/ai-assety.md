# AI assety: z obrázku po postavu v enginu

Pipeline roku 2026: obrázková AI vyrobí referenci, **image-to-3D** model (Tripo, Hunyuan, Rodin), Blender složí a doladí, AI texturing opraví, rig dodá Mixamo či AccuRig — a Unreal dostane hratelnou postavu. Kapitola jde od bezplatného základu přes srovnání nástrojů a cen po dvě velké aplikace: **modulární postavu** a **konverzi na MetaHumana** v 5.8. Agentní stranu (Claude Code, MCP) řeší [sesterská kapitola](claude-code-ue.md). Průřezová výhrada: nástroje této kapitoly se mění po měsících — vzory přežijí, verze ne.

---

## Bezplatná pipeline: postava za hodinu

**Zdroj:** [Complete Free AI Workflow for Game-Ready 3D Characters](https://www.youtube.com/watch?v=TkP-_LyacMI) · [Stefan 3D AI](https://www.youtube.com/channel/UCRW08KcTVjXEmBzBsVl7XjA) · ~12 min, tutoriál

**Shrnutí:** Herní postava za necelou hodinu a bez placených nástrojů: reference po částech (ruce, hlava, tělo, ocas) z obrázkové AI, 3D přes **Hunyuan 3.1** (20 generací denně zdarma), montáž v Blenderu, optimalizace + AI texturing v Modif, rig přes Mixamo [(0:00)](https://www.youtube.com/watch?v=TkP-_LyacMI&t=0s).

### Rozpad myšlenky

**Po částech, ne vcelku:** tělo generované najednou mívá slité ruce se třemi prsty — ruce, hlava i ocas se generují zvlášť a spojují se až v Blenderu [(0:46)](https://www.youtube.com/watch?v=TkP-_LyacMI&t=46s) [(1:32)](https://www.youtube.com/watch?v=TkP-_LyacMI&t=92s). Multiview (2 pohledy většinou stačí) jen tam, kde jedna reference neukazuje důležitý detail [(1:32)](https://www.youtube.com/watch?v=TkP-_LyacMI&t=92s).

**Blender bez strachu:** hrst nástrojů stačí — mirror modifier na ruce (origin do 3D kurzoru a **Ctrl+A apply rotation & scale**, jinak zrcadlí špatně), lasso mask + mask brush → **Mask Slice and Fill Holes** = čistý řez starých končetin, **Elastic Grab** na dohnutí tvarů („jako hlína"), smooth brush přes Shift, `Ctrl+J` spojit a **Remesh** (~0,0003) sjednotí vše do jednoho povrchu bez vnitřků [(3:04)](https://www.youtube.com/watch?v=TkP-_LyacMI&t=184s) [(4:36)](https://www.youtube.com/watch?v=TkP-_LyacMI&t=276s) [(6:09)](https://www.youtube.com/watch?v=TkP-_LyacMI&t=369s).

**Optimalizace a textury (Modif):** import GLB → simplify na herních 15–50K polygonů **s bake normal mapy** (detail zůstane) [(7:41)](https://www.youtube.com/watch?v=TkP-_LyacMI&t=461s); texturing: multiview vygeneruje základ, kazy se opravují maskou + single-view referencí a **inpaintem po vrstvách** jako ve Photoshopu; na zbraň stačí projekce z obrázku [(8:27)](https://www.youtube.com/watch?v=TkP-_LyacMI&t=507s) [(9:13)](https://www.youtube.com/watch?v=TkP-_LyacMI&t=553s). Rig: export OBJ (apply scale!) → **Mixamo** markery → animace zpět [(10:00)](https://www.youtube.com/watch?v=TkP-_LyacMI&t=600s).

> **Pozn.:** Poctivý disclaimer pro 3D artisty přímo z videa: „topologie" je decimovaný high-poly s normal bake — pro start OK, čistší retopologii umí AI nástroje zvlášť [(11:32)](https://www.youtube.com/watch?v=TkP-_LyacMI&t=692s). Ocas u nestandardní postavy chce ruční doladění vah — viz [weights v MetaHuman kapitole](metahuman.md).

**Souvislosti:** [Nástroje a ceny](#nastroje-a-ceny-tripo-hunyuan-rodin) · [Přehled algoritmů: diffusion](../teorie/algoritmy-prehled.md#algoritmy-ktere-stavi-herni-svety) *(jak generátory obrázků fungují uvnitř)* · [Rejstřík: retopologie](../rejstrik.md#retopologie) · [Rejstřík: PBR](../rejstrik.md#pbr)

---

## Nástroje a ceny: Tripo, Hunyuan, Rodin

**Zdroj:** [Next-Gen 3D AI Is Here (5-Second Game-Ready Models)](https://www.youtube.com/watch?v=mXjUz3viYmQ) · [Stefan 3D AI](https://www.youtube.com/channel/UCRW08KcTVjXEmBzBsVl7XjA) · ~20 min, srovnání

**Shrnutí:** Tři velcí hráči image-to-3D proti sobě na stejných referencích. Závěr autora (který s nimi denně komerčně pracuje): **Tripo** vede v geometrii detailů, obličejích i texturingu a smart mesh generuje za ~5 sekund; Hunyuan je „zdarma" s frontami a přes API vyjde draho; Rodin má slabší základní model [(1:02)](https://www.youtube.com/watch?v=mXjUz3viYmQ&t=62s) [(6:27)](https://www.youtube.com/watch?v=mXjUz3viYmQ&t=387s).

### Rozpad myšlenky

**Čísla, na kterých záleží:** Tripo HD mesh ~30 centů, smart mesh ~20; Hunyuan celkový asset (high poly + retopo + textura) přes API ~1,5 dolaru — a fronta ve free Studiu umí spolknout i 30 minut na model [(4:54)](https://www.youtube.com/watch?v=mXjUz3viYmQ&t=294s) [(5:41)](https://www.youtube.com/watch?v=mXjUz3viYmQ&t=341s). Celá postava: Tripo <2 minuty proti ~10 minutám v Hunyuan Studiu (čínské servery, pomalé uploady, bez kontroly polygonů) [(15:01)](https://www.youtube.com/watch?v=mXjUz3viYmQ&t=901s) [(18:07)](https://www.youtube.com/watch?v=mXjUz3viYmQ&t=1087s). PBR dogenerování stojí centy a viditelně zvedá materiály [(4:07)](https://www.youtube.com/watch?v=mXjUz3viYmQ&t=247s).

**Kvalita:** na testech čtyřruké postavy dá Tripo **pět prstů na každé ruce** a logické detaily i na stranách, které reference neukazovala [(9:35)](https://www.youtube.com/watch?v=mXjUz3viYmQ&t=575s) [(11:08)](https://www.youtube.com/watch?v=mXjUz3viYmQ&t=668s); Hunyuan 3.1 má slabé obličeje, Rodin selhal na katana detailu [(6:27)](https://www.youtube.com/watch?v=mXjUz3viYmQ&t=387s) [(7:14)](https://www.youtube.com/watch?v=mXjUz3viYmQ&t=434s). Dvě systematické pravdy: **text a loga selhávají v každé generativní AI** (oprava v Modif) [(8:02)](https://www.youtube.com/watch?v=mXjUz3viYmQ&t=482s) a dobrá textura **nemá zapečené světlo** z reference — světlo dodá engine [(13:29)](https://www.youtube.com/watch?v=mXjUz3viYmQ&t=809s). Retopo režim navíc **peče normal mapu z HD verze** [(8:48)](https://www.youtube.com/watch?v=mXjUz3viYmQ&t=528s).

> **Pozn.:** Video obsahuje promo kód na Tripo a autor provozuje vlastní srovnávací web — čti čísla jako informovaný, ale zaujatý zdroj; metodika (stejné reference napříč nástroji) je nicméně vidět na obrazovce. Zlaté pravidlo na závěr platí univerzálně: „nikdy to nebude 100% — úspora je v rychlých iteracích" [(18:54)](https://www.youtube.com/watch?v=mXjUz3viYmQ&t=1134s).

**Souvislosti:** [Bezplatná pipeline](#bezplatna-pipeline-postava-za-hodinu) · [Rejstřík: PBR](../rejstrik.md#pbr) · [Rejstřík: mip mapa](../rejstrik.md#mip-mapa)

---

## Hratelná postava v tandemu: assety + AI blueprinty

**Zdroj:** [From AI to Playable 3D Character in Unreal Engine](https://www.youtube.com/watch?v=k1xBERhXtHA) · [Stefan 3D AI](https://www.youtube.com/channel/UCRW08KcTVjXEmBzBsVl7XjA) · ~22 min, kolaborace

**Shrnutí:** Dvojice tvůrců, dvě půlky pipeline naráz: Stefan generuje fortnite-style kocoura se zbraní (Tripo ultra z tří pohledů, Modif fixy, Mixamo rig), zatímco Gorka nechává agenta postavit **third person blueprinty s Enhanced Input a střelbou** — „nesáhl jsem na jediný uzel" [(3:08)](https://www.youtube.com/watch?v=k1xBERhXtHA&t=188s) [(9:36)](https://www.youtube.com/watch?v=k1xBERhXtHA&t=576s). Na konci se obě větve potkají: socket, retarget, hra.

### Rozpad myšlenky

**Asset větev:** reference z obrázkové AI (front/back/side + zbraň zvlášť) [(0:01)](https://www.youtube.com/watch?v=k1xBERhXtHA&t=1s); Tripo ultra multi-image s PBR — srovnání s Hunyuanem ukázalo klasický zádrhel: **prsty jako jeden slitek**, což pohřbí animaci [(1:34)](https://www.youtube.com/watch?v=k1xBERhXtHA&t=94s). Modif: simplify (kocour ~50K, zbraň ~16K) + normal bake; textury spravené inpaintem — na uši si nechal vygenerovat novou referenci „close up shot" přímo v nástroji [(5:26)](https://www.youtube.com/watch?v=k1xBERhXtHA&t=326s) [(6:58)](https://www.youtube.com/watch?v=k1xBERhXtHA&t=418s). Mixamo rig; při návratu FBX do Blenderu **import scale 100** a export s **embed textures (path mode: copy)** [(10:23)](https://www.youtube.com/watch?v=k1xBERhXtHA&t=623s) [(12:41)](https://www.youtube.com/watch?v=k1xBERhXtHA&t=761s).

**Blueprint větev:** plugin v editoru napojený na Claude API — „create third person character with movement and camera control, **use the new Enhanced Input system**" vygeneruje postavu, input akce i mapování; druhý prompt přidá střelbu s projektily (input action, collision sphere, projektil s pohybem a hitem) [(3:54)](https://www.youtube.com/watch?v=k1xBERhXtHA&t=234s) [(8:50)](https://www.youtube.com/watch?v=k1xBERhXtHA&t=530s). Do doby, než dorazí assety, poslouží kostka jako placeholder [(4:40)](https://www.youtube.com/watch?v=k1xBERhXtHA&t=280s).

**Spojení:** zbraň na **socket** pravé ruky (preview asset pro usazení, pak static mesh s parent socketem a vypnutou kolizí) [(15:00)](https://www.youtube.com/watch?v=k1xBERhXtHA&t=900s) [(15:46)](https://www.youtube.com/watch?v=k1xBERhXtHA&t=946s); animace z third person šablony **retargetem** na kocouří skeleton (T-pose varianta cílí líp) — včetně zmínky real-time retargetingu, který drží animace živě bez exportu [(16:32)](https://www.youtube.com/watch?v=k1xBERhXtHA&t=992s).

> **Pozn.:** Přesně dělba ze [72hodinové hry](claude-code-ue.md#72-hodin-delba-prace-clovekai) v malém: člověk kurátor assetů a kompozice, agent kodér. Retarget řemeslně rozebírá [MetaHuman kapitola](metahuman.md#hratelny-metahuman-retarget-jednim-klikem-a-virtual-bones) — tady je vidět, že tentýž vzor unese i nehumanoidní proporce.

**Souvislosti:** [Claude Code kapitola](claude-code-ue.md) · [MetaHuman: retarget](metahuman.md#hratelny-metahuman-retarget-jednim-klikem-a-virtual-bones) · [Rejstřík: PBR](../rejstrik.md#pbr)

---

## Modulární postava: party, AccuRig a rigid doplňky

**Zdroj:** [I Built a Modular Character with AI (Full Workflow)](https://www.youtube.com/watch?v=gZIxrX1n2D4) · [Stefan 3D AI](https://www.youtube.com/channel/UCRW08KcTVjXEmBzBsVl7XjA) · ~27 min, tutoriál

**Shrnutí:** Z jednoho konceptu (kitsune) **modulární systém**: vyměnitelné outfity, zbraně a doplňky. Klíčem je práce po částech od začátku — nástroj rozseká referenci na party automaticky, 3D se generuje dávkou a Blender skládá; rig obstará **AccuRig s exportem přímo na UE skeleton** [(0:00)](https://www.youtube.com/watch?v=gZIxrX1n2D4&t=0s) [(17:46)](https://www.youtube.com/watch?v=gZIxrX1n2D4&t=1066s).

### Rozpad myšlenky

**Extrakce a generování:** referenci v A/T póze nástroj rozloží na party (analysis → confirm); nepovedený part se rejectne a regeneruje s upřesněným promptem [(1:33)](https://www.youtube.com/watch?v=gZIxrX1n2D4&t=93s) [(3:06)](https://www.youtube.com/watch?v=gZIxrX1n2D4&t=186s). Uzly na multi-view, split image (podčásti) a generování obrázků pokrývají variace — prompty píše ChatGPT [(3:52)](https://www.youtube.com/watch?v=gZIxrX1n2D4&t=232s) [(6:57)](https://www.youtube.com/watch?v=gZIxrX1n2D4&t=417s); 3D pak **dávkou** s volbou modelu per part (detailní vs. low-poly rovnou) a rozumným polycountem (8K na zbraň) [(4:38)](https://www.youtube.com/watch?v=gZIxrX1n2D4&t=278s) [(8:29)](https://www.youtube.com/watch?v=gZIxrX1n2D4&t=509s).

**Blender rituál** (u GLB importů vždy): **merge vertices by distance**, **weighted normal modifier** proti flat shadingu (copy to selected na všechny), `Ctrl+A` apply transformů, origin do world originu pro čistý export, elastic grab na dosednutí [(10:49)](https://www.youtube.com/watch?v=gZIxrX1n2D4&t=649s) [(13:09)](https://www.youtube.com/watch?v=gZIxrX1n2D4&t=789s). Chytrá optimalizace: **smazat zakrytou geometrii** (nohy pod kalhotami) — méně polygonů a hlavně méně rig problémů, koleno nemůže prorazit látku, když neexistuje [(15:27)](https://www.youtube.com/watch?v=gZIxrX1n2D4&t=927s).

**Rig a co se nikdy neriguje:** vše nositelné se exportuje k rigu společně — **AccuRig** (zdarma) má víc markerů než Mixamo, kalibrační krok pro nestandardní proporce a umí **exportovat rovnou jako Unreal Engine skeleton** [(16:59)](https://www.youtube.com/watch?v=gZIxrX1n2D4&t=1019s) [(17:46)](https://www.youtube.com/watch?v=gZIxrX1n2D4&t=1066s). **Rigid objekty** (katana, srp, klobouk) se nerigují — patří na sockety; ocas dostane vlastní kosti připojené k armatuře a rozhýbe ho až fyzika v enginu [(16:13)](https://www.youtube.com/watch?v=gZIxrX1n2D4&t=973s) [(18:33)](https://www.youtube.com/watch?v=gZIxrX1n2D4&t=1113s).

> **Pozn.:** Extrakční nástroj (Asset Hub) je autorův oblíbený a video má promo nádech — samotný vzor „části od začátku, dávkové generování, rigid vs. rigged" ale platí s libovolnými nástroji. Modulární výměna outfitů na jednom skeletonu je tentýž princip, na kterém stojí [Crowd outfity u MetaHumanů](metahuman.md#crowd-plugin-tisic-metahumanu-pres-mass).

**Souvislosti:** [Bezplatná pipeline](#bezplatna-pipeline-postava-za-hodinu) · [MetaHuman: crowd](metahuman.md#crowd-plugin-tisic-metahumanu-pres-mass) · [Rejstřík: pivot](../rejstrik.md#pivot) · [Rejstřík: retopologie](../rejstrik.md#retopologie)

---

## AI postava → MetaHuman (5.8)

**Zdroj:** [From AI to Metahuman - Best New UE 5.8 Workflow for Custom Character](https://www.youtube.com/watch?v=4w7oA4oJMqs) · [Stefan 3D AI](https://www.youtube.com/channel/UCRW08KcTVjXEmBzBsVl7XjA) · ~28 min, tutoriál

**Shrnutí:** 5.8 dovolí MetaHumanu **import celého custom meshe** — a tím se každý AI humanoid může stát MetaHumanem s obličejovým i tělesným rigem, live linkem a markerless mocapem [(0:00)](https://www.youtube.com/watch?v=4w7oA4oJMqs&t=0s). Workflow: příprava v Blenderu → Auto Solve → uložit DNA → zapéct textury zpět → doplňky navěsit na rig.

### Rozpad myšlenky

**Příprava vstupu:** póza s prostorem (nohy od sebe, ruce od těla, **prsty oddělené**), hlava generovaná zvlášť kvůli detailu, bez vlasů a řas; vše spojit v Blenderu do jednoho meshe — **rozlišení nešetři**, tenhle HD model bude zdrojem pro pozdější baking [(2:18)](https://www.youtube.com/watch?v=4w7oA4oJMqs&t=138s) [(3:04)](https://www.youtube.com/watch?v=4w7oA4oJMqs&t=184s) [(3:51)](https://www.youtube.com/watch?v=4w7oA4oJMqs&t=231s). Měřítko srovná **MetaHuman conform reference tělo** (zdarma na Fabu); `Ctrl+A` a export GLB [(0:46)](https://www.youtube.com/watch?v=4w7oA4oJMqs&t=46s) [(4:37)](https://www.youtube.com/watch?v=4w7oA4oJMqs&t=277s).

**Konverze:** MetaHuman asset → Import → **From Custom Mesh** → combined mesh → **Auto Solve** (pár minut) [(5:23)](https://www.youtube.com/watch?v=4w7oA4oJMqs&t=323s) [(6:10)](https://www.youtube.com/watch?v=4w7oA4oJMqs&t=370s). Kritický krok, který se snadno přeskočí: v Manual Solve **Save Pose = DNA soubor** — uchová mesh v conform stavu; bez něj později nespárujete UV pro baking, protože póza se dál mění [(6:57)](https://www.youtube.com/watch?v=4w7oA4oJMqs&t=417s). Pak doladění částí a materiálů (oči, zuby zůstávají MetaHuman), **Create Full Rig + Download Texture Sources**; proces je reverzibilní přes DNA [(7:43)](https://www.youtube.com/watch?v=4w7oA4oJMqs&t=463s).

**Textury zpět (nejtěžší část):** z DNA **Generate Skeletal Mesh** → export FBX (stejné UV, conform póza) → v Blenderu **zapéct color + normal z původního HD těla na MetaHuman tělo** (Cycles, selected → active) [(8:29)](https://www.youtube.com/watch?v=4w7oA4oJMqs&t=509s) [(10:48)](https://www.youtube.com/watch?v=4w7oA4oJMqs&t=648s). Past: MetaHuman používá **UDIM** — v Blenderu hlavu oddělit (P → Separate) a UV těla posunout přesně o 1 [(9:15)](https://www.youtube.com/watch?v=4w7oA4oJMqs&t=555s) [(10:01)](https://www.youtube.com/watch?v=4w7oA4oJMqs&t=601s); šev na krku dočistí Clone/Smear v Texture Paint [(12:20)](https://www.youtube.com/watch?v=4w7oA4oJMqs&t=740s); normal pečená mimo UE chce při importu **flip green channel** [(16:58)](https://www.youtube.com/watch?v=4w7oA4oJMqs&t=1018s). Textury pak nahradí originály v MetaHuman materiálech (pozor na LODy) [(13:07)](https://www.youtube.com/watch?v=4w7oA4oJMqs&t=787s).

**Doplňky na rig:** finální skeletal mesh s armaturou zpět do Blenderu, uši/větve dosculptovat, **parent s deform + váha 100 % na head bone**, export FBX s vypnutými leaf bones — a v MetaHuman blueprintu stačí skeletal mesh přetáhnout na Body: skeletony sedí, animace jede [(13:53)](https://www.youtube.com/watch?v=4w7oA4oJMqs&t=833s) [(16:11)](https://www.youtube.com/watch?v=4w7oA4oJMqs&t=971s) [(17:44)](https://www.youtube.com/watch?v=4w7oA4oJMqs&t=1064s). Finální test: **markerless mocap** z videa přes MetaHuman Performance s Body Trackingem — vlastní AI postava se hýbe podle herce z běžného záznamu [(18:30)](https://www.youtube.com/watch?v=4w7oA4oJMqs&t=1110s) [(20:03)](https://www.youtube.com/watch?v=4w7oA4oJMqs&t=1203s).

> **Pozn.:** Markerless pipeline (Live Link Hub → Mono Video Ingest → Performance) do detailu popisuje [kapitola Animační nástroje](animace-nastroje.md) — tady je pointa, že funguje i na custom AI postavě. Titulky videa jsou strojově lámané (en-it stopa); terminologie v textu narovnána podle obrazu.

**Souvislosti:** [Animační nástroje: markerless mocap](animace-nastroje.md) · [MetaHuman v praxi](metahuman.md) · [Rejstřík: MetaHuman](../rejstrik.md#metahuman) · [Rejstřík: retopologie](../rejstrik.md#retopologie)

---

## Animace a 2D: Kimodo a PixelLab

**Zdroj:** [AI Animation Just Got a Revolution — NVIDIA Kimodo](https://www.youtube.com/watch?v=CVA4jGHAbnA) · [Stefan 3D AI](https://www.youtube.com/channel/UCRW08KcTVjXEmBzBsVl7XjA) · ~7 min · + [Make infinite characters in the SAME style!](https://www.youtube.com/watch?v=LcJQQwltQ2Q) · [PixelLab](https://www.youtube.com/channel/UCz-FR-s8sge9njmiUCRSUOg) · ~11 min, produktové demo

**Shrnutí:** Dva okraje asset pipeline. **NVIDIA Kimodo** posouvá AI animaci od „vygeneruj něco" k **režii**: text + path + waypointy + pózy jako constrainty, kombinovatelné na timeline [(0:00)](https://www.youtube.com/watch?v=CVA4jGHAbnA&t=0s). A **PixelLab** řeší 2D bolest číslo jedna — **konzistentní styl** napříč postavami pixel-art hry [(1:37)](https://www.youtube.com/watch?v=LcJQQwltQ2Q&t=97s).

### Rozpad myšlenky

**Kimodo:** proti starším modelům trénovaným na videu stojí **700 hodin optického mocapu** — přesnější pohyb [(0:47)](https://www.youtube.com/watch?v=CVA4jGHAbnA&t=47s). Řízení: multi-text sekvence s délkami, **pose constraint** (zadaná póza se trefí přesně), path („skáče po jedné noze" po křivce) a waypointy jako keyframy — kombinovatelné [(3:05)](https://www.youtube.com/watch?v=CVA4jGHAbnA&t=185s) [(3:52)](https://www.youtube.com/watch?v=CVA4jGHAbnA&t=232s) [(4:38)](https://www.youtube.com/watch?v=CVA4jGHAbnA&t=278s). Export **BVH/NPZ**; do UE vede cesta přes retarget (např. AutoRig Pro v Blenderu) [(5:24)](https://www.youtube.com/watch?v=CVA4jGHAbnA&t=324s). Běží i lokálně (demo na Hugging Face); prakticky ho v agentní lince zapřahá [ComfyUI + Blender kapitola](claude-code-ue.md#agent-v-blenderu-a-comfyui-lokalni-pipeline).

**PixelLab:** postava z promptu (velikost spritu, outline, míra detailu) → **create from style reference**: těsný výřez hotové postavy jako reference a nové postavy (farmářka, čarodějka, rytíř) vylezou ve stejném stylu; vygenerované kusy lze přidávat jako další reference = víc kontextu [(0:02)](https://www.youtube.com/watch?v=LcJQQwltQ2Q&t=2s) [(1:37)](https://www.youtube.com/watch?v=LcJQQwltQ2Q&t=97s) [(2:25)](https://www.youtube.com/watch?v=LcJQQwltQ2Q&t=145s). Animace po stavech (idle/walk/run) s pravidlem: **u loopů nechat první frame zapnutý** (hladké napojení), u one-shotů vypnout [(4:48)](https://www.youtube.com/watch?v=LcJQQwltQ2Q&t=288s) [(5:25)](https://www.youtube.com/watch?v=LcJQQwltQ2Q&t=325s). A disciplína, která drží celé demo pohromadě: **před animací a zrcadlením vždy ruční úklid v editoru** (Pixelorama) — zrcadlit špinavý frame znamená rozmnožit chybu [(0:49)](https://www.youtube.com/watch?v=LcJQQwltQ2Q&t=49s) [(6:55)](https://www.youtube.com/watch?v=LcJQQwltQ2Q&t=415s).

> **Pozn.:** PixelLab je demo z kanálu výrobce — vzor „style reference + úklid před množením" ale platí pro jakoukoli generativní 2D pipeline. Ke Kimodu: doporučené VRAM v přepisu zní zmateně (auto-titulky) — před lokálním nasazením ověř nároky v oficiální dokumentaci. Světlo do 2D spritů pak dodá trik s [normal mapami z kapitoly Osvětlení](osvetleni.md#drobky-tri-triky-a-svetlo-ve-2d).

**Souvislosti:** [Claude Code: agent v Blenderu](claude-code-ue.md#agent-v-blenderu-a-comfyui-lokalni-pipeline) · [Osvětlení: světlo ve 2D](osvetleni.md#drobky-tri-triky-a-svetlo-ve-2d) · [Animační nástroje](animace-nastroje.md) · [Rejstřík: silueta](../rejstrik.md#silueta)

---

## Animace generovaná v reálném čase: kam se posunulo ARDY

**Zdroj:** [NVIDIA ARDY: The Real-Time Leap in AI Animation (Open-Source)](https://www.youtube.com/watch?v=xLf27GC0-hE) · [Stefan 3D AI](https://www.youtube.com/channel/UCRW08KcTVjXEmBzBsVl7XjA) · ~6 min, přehled a test

**Shrnutí:** Dosavadní AI animace v téhle kapitole byla **generativní** — zadáš prompt, počkáš, dostaneš klip. ARDY posouvá hranici jinam: **generuje pohyb v reálném čase a dá se ovládat klávesnicí**, přičemž vstup z klávesnice funguje jako omezení kombinovatelné s textovým promptem. Model je **open source s publikovanými váhami**, takže se dá spustit lokálně — pokud máš dost VRAM.

### Rozpad myšlenky

**Časová osa, která tomu dává smysl** [(0:46)](https://www.youtube.com/watch?v=xLf27GC0-hE&t=46s), je nejužitečnější část videa, protože zasazuje jednotlivé nástroje do vývoje. **Kimodo** — běží lokálně na nízké VRAM, hodně ovládání, *„ale je hlavně o generování"*. **Motion bricks** — už blíž k enginu, latence kolem dvou milisekund, *„takže se pohyb nejen počítá v reálném čase, ale umí i interagovat s prostředím"*; háček podle autora: **vydaná byla jen pohybová část a slíbené interakční „smart primitives" nikdy nevyšly**. A **ARDY** — kompletní generace pohybu v reálném čase se stejnými ovládáními, omezeními a root motion jako Kimodo, s lepší kvalitou dodržování omezení díky dvoustupňovému denoiseru a **datasetu, který je nově kostní**.

**Co je na tom skutečně nové** [(3:50)](https://www.youtube.com/watch?v=xLf27GC0-hE&t=230s): *„můžeš to ovládat klávesnicí — a ty real-time constrainty můžou fungovat společně s promptem. Takže spustíš skripty, které berou vstup z klávesnice nebo myši jako omezení, a zkombinuješ ho s textovým promptem typu ‚skákej po jedné noze'."* Totéž platí pro root motion: zadáš reprezentaci dráhy a k ní textový popis. **Není to tedy generátor klipů, ale běhová vrstva mezi vstupem a pózou** — což je koncepčně jiná kategorie než všechno ostatní v téhle kapitole.

**Hardware a jak ho obejít** [(2:18)](https://www.youtube.com/watch?v=xLf27GC0-hE&t=138s): demo bylo testované na 24GB kartě, *„minimum je kolem 16 až 18 GB, ale pro reálný běh v reálném čase potřebuješ 24"*. Autor tolik VRAM nemá, takže si **pronajal GPU za zhruba dolar na hodinu**, připojil se přes SSH a instalaci nechal udělat agentem. Poctivě dodává, že se službou nemá nic společného — a pro nás je to hlavně připomínka, že **testování těžkých modelů nevyžaduje koupi hardwaru.**

**Cesta do Unrealu** [(4:36)](https://www.youtube.com/watch?v=xLf27GC0-hE&t=276s): export používá kostru o 27 kostech a jednu standardní reprezentaci, o které autor říká, že *„se dá v Unrealu namapovat a retargetovat"*; modely jsou na Hugging Face a dají se prohodit podle skeletonu, k lokálnímu běhu je potřeba bezplatný token a schválení na stránce jednoho z použitých modelů.

> **Pozn.:** Autorova spekulace na konec stojí za zaznamenání právě jako spekulace [(5:22)](https://www.youtube.com/watch?v=xLf27GC0-hE&t=322s): *„brzo budeme mít hry s úplně procedurálními — vlastně AI generovanými — animacemi. Hráč vede, kam jít, skripty upravují textový prompt a všechno se v reálném čase krmí do modelu."* Proti tomu stojí praktická realita, kterou popisuje zbytek kapitoly: **nároky na VRAM zatím vylučují běh na hráčském stroji vedle samotné hry.** Bližší a zajímavější použití je proto to druhé, které zmiňuje — **režírovaný pohyb pro playblasty a následné zpracování**, tedy nástroj do produkce, ne do buildu. Srovnej s [Motion Matchingem](mm-zaklady.md), který tentýž problém (plynulý pohyb odpovídající vstupu) řeší databází skutečných animací a běží na čemkoli.

**Souvislosti:** [Animace a 2D: Kimodo a PixelLab](#animace-a-2d-kimodo-a-pixellab) *(předchozí generace téhož nástroje)* · [MM základy](mm-zaklady.md#dotaz-misto-grafu-jak-motion-matching-vybira-pozy) *(neAI odpověď na tutéž úlohu)* · [Animační nástroje: markerless mocap](animace-nastroje.md#markerless-mocap-v-58-z-videa-na-animaci-bez-obleku) · [Učení v éře AI](../teorie/uceni-v-ere-ai.md) · [Rejstřík: root motion](../rejstrik.md#root-motion) · [Rejstřík: retargeting](../rejstrik.md#retargeting)
