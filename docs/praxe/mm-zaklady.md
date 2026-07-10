# Motion Matching: základy

Motion Matching je největší změna v herní animaci od state machines — a od 5.4 je v UE k dispozici všem, včetně 500+ animací z Game Animation Sample. Kapitola skládá osm zdrojů do čtyř vrstev: **co MM dělá** (koncept), **jak ho postavit od nuly**, **kolik animací doopravdy potřebuješ** (spoiler: 13) a **jak ho doladit z „funguje" na „vypadá skvěle"**. GASP samotnému se věnuje [samostatná kapitola](gasp.md).

---

## Dotaz místo grafu: jak Motion Matching vybírá pózy

**Zdroj:** [Motion Matching Explained (State Machines to GASP) in Unreal Engine 5!](https://www.youtube.com/watch?v=9BWLj98pekM) · [DevEdge Studio](https://www.youtube.com/channel/UCGa0hsNw3BK6xTDnVvfFltw) · ~59 min, explainer ·
[Motion Matching and the Game Animation Sample in UE 5.4 | Unreal Fest 2024](https://www.youtube.com/watch?v=tNw9lD2PW3U) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~41 min, přednáška Epicu

**Shrnutí:** Motion Matching je **dotazový systém výběru animací** [(0:46)](https://www.youtube.com/watch?v=tNw9lD2PW3U&t=46s): místo grafu stavů se každý frame ptá „která póza v databázi nejlépe naváže na to, co se děje?" Dotaz má dvě části [(0:52)](https://www.youtube.com/watch?v=tNw9lD2PW3U&t=52s) — *co hra chce* (trajektorie) a *aktuální stav* (současná póza a její pokračování) — a vítěz se vybírá podle nejnižší **ceny** (cost).

### Rozpad myšlenky

**Proč pryč od state machines:** klasický AnimBP tahá proměnné (rychlost, crouch) do grafu stavů s přechodovými pravidly a blend spacy — a každý nový stav znamená další explozi přechodů [(7:48)](https://www.youtube.com/watch?v=9BWLj98pekM&t=468s). MM stavy ruší: všechno je jedna databáze póz a matematika. K tomu limity CMC: postava je **kapsle s fyzikou** [(8:25)](https://www.youtube.com/watch?v=9BWLj98pekM&t=505s) — animace se jen lepí na její pohyb, a rotace nabízí jen dvě volby.

**Stavební kameny** (názvosloví, které budeš potkávat všude):

- **Trajektorie** [(14:59)](https://www.youtube.com/watch?v=9BWLj98pekM&t=899s): každý frame spočítaná historie (červeně) a *predikce budoucí pozice* (modře) z rychlosti a vstupu. Pozor na záměnu s traversal (parkourová detekce překážek) a s **intentem** [(54:23)](https://www.youtube.com/watch?v=9BWLj98pekM&t=3263s): intent = co hráč *chce* (vstup), trajektorie = co se *asi stane* (predikce).
- **Pose Search Database (PSD)** [(21:06)](https://www.youtube.com/watch?v=9BWLj98pekM&t=1266s): kolekce animací pro jeden typ pohybu (idle, run starts, stops…). Hledá se v ní, nevykresluje.
- **Schema** [(25:41)](https://www.youtube.com/watch?v=9BWLj98pekM&t=1541s): definice *co se měří* — kanály (trajektorie, pozice chodidel, rychlosti, pelvis) s **vahami** [(27:18)](https://www.youtube.com/watch?v=9BWLj98pekM&t=1638s), které říkají, na čem při výběru záleží. Cena kandidáta = vážená vzdálenost od dotazu.
- **Chooser** [(23:19)](https://www.youtube.com/watch?v=9BWLj98pekM&t=1399s): datová tabulka, která podle stavu hry (crouch? běh?) vybírá *kterou databázi* prohledávat — DevEdge jí říká „tranzistor" systému. Fortnite tímhle vynucuje responzivitu: databáze jsou rozdělené podle stavů a chooser přepne v ten samý frame, kdy stiskneš pohyb [(14:46)](https://www.youtube.com/watch?v=tNw9lD2PW3U&t=886s).
- **Pose History**: uzel, který sbírá kostní data a trajektorii pro schema — bez něj se nedá ptát „odkud jdu".
- **Continuing pose** [(17:29)](https://www.youtube.com/watch?v=tNw9lD2PW3U&t=1049s): „co by hrálo dál, kdybych nic neměnil" — kandidát, kterého musí každá nová animace *porazit cenou*. Klíč k celému ladění.

> **Pozn.:** MM není zadarmo: GASP používá ~500–900 animací jen na locomotion a DevEdge správně varuje, že s combat systémy poroste váha dál [(41:01)](https://www.youtube.com/watch?v=9BWLj98pekM&t=2461s) — ale Fortnite s MM shipuje na všech platformách včetně mobilů a hlavně: **nepotřebuješ stovky animací** (viz sparse set níže). DevEdge navíc ukazuje 5.7 novinky (Mover pawn místo CMC, procedurální Locomotor, hybridní blend stack + state machine) — to pokrývá [kapitola o GASP](gasp.md).

**Souvislosti:** [GASP: Game Animation Sample](gasp.md) · [Rejstřík: motion matching](../rejstrik.md#motion-matching) · [Rejstřík: trajektorie](../rejstrik.md#trajektorie) · [Rejstřík: Pose Search Database](../rejstrik.md#pose-search-database)

---

## Setup od nuly: root motion, schema, databáze, chooser

**Zdroj:** [UE5 | Motion Matching Breakdown | Part-1](https://www.youtube.com/watch?v=-r4nafTJI5c) · [TechAnim Studios](https://www.youtube.com/channel/UCUZz7MzEZRRa09quU9LzIoQ) · ~54 min, stavba od nuly ·
[Understand Motion Matching in Unreal Engine 5 - Part 1](https://www.youtube.com/watch?v=YtIxWtMPYQE) + [Part 2](https://www.youtube.com/watch?v=q-Ag6iYalAo) · [Ryan Laley](https://www.youtube.com/channel/UCsS5i15vvUbwfr_1JdRKCAA) · ~33 min ·
[Unreal Engine 5.4 Motion Matching in 13 Minutes](https://www.youtube.com/watch?v=LJi_vPAuTv4) · [Reality Forge](https://www.youtube.com/channel/UCINisoTvoEzhPb8MBtR3Feg) · ~14 min ·
[Unreal Engine 5.4 Tutorial - Motion Matching](https://www.youtube.com/watch?v=HxY0WWQe_XA) · [Unreal University](https://www.youtube.com/channel/UCQv4mwerZLQVe3wPbsMc-qw) · ~8 min

**Shrnutí:** Čtyři tutoriály, jeden sdílený postup: **root motion animace** → pluginy → **schema** → **databáze** → MM uzel + pose history → chooser pro přepínání databází. A dvě lekce, které v dokumentaci nenajdeš: kdy chooser *nepotřebuješ* a proč se MM „zblázní", když mu dáš moc podobných póz.

### Rozpad myšlenky

**Prerekvizity:** animace musí být **root motion** [(0:49)](https://www.youtube.com/watch?v=YtIxWtMPYQE&t=49s) — MM čte pohyb z root kosti. Hromadné nastavení přes `Asset Actions → Edit Selection in Property Matrix` [(2:41)](https://www.youtube.com/watch?v=LJi_vPAuTv4&t=161s): zapnout *EnableRootMotion* + **Force Root Lock** [(7:12)](https://www.youtube.com/watch?v=YtIxWtMPYQE&t=432s) (jinak animace „ujíždí a snapuje zpět") a *Looping* u smyček. Pluginy: **Pose Search**, **Motion Trajectory**, **Chooser** (+ Motion Warping pro pozdější systémy) [(1:16)](https://www.youtube.com/watch?v=YtIxWtMPYQE&t=76s).

**Kostra v AnimBP:** na character přidej **Character Trajectory** komponentu [(3:45)](https://www.youtube.com/watch?v=YtIxWtMPYQE&t=225s) (nebo trajektorii generuj v thread-safe update přes `Pose Search Generate Trajectory` — cesta TechAnim); v anim grafu **Motion Matching uzel → Pose History → Output Pose** [(5:55)](https://www.youtube.com/watch?v=HxY0WWQe_XA&t=355s). Základní chování je hotové bez jediného přechodu [(0:27)](https://www.youtube.com/watch?v=HxY0WWQe_XA&t=27s) — a debug vykreslíš konzolí `a.CharacterTrajectory.Debug 1`.

**Schema doladění** (TechAnim jde nejhlouběji): default váha trajektorie 7 je moc — sraž na 1 a přidej vzorky do minulosti (−0,05 s) a budoucnosti (+0,35/0,7/1,0 s); pozice chodidel s vahou 1, rychlosti chodidel 0,3 [(23:47)](https://www.youtube.com/watch?v=-r4nafTJI5c&t=1427s) — *pozice preferuješ, rychlost jen zohledňuješ*. K tomu **continuing pose cost bias** záporně [(26:57)](https://www.youtube.com/watch?v=-r4nafTJI5c&t=1617s) (ať systém neskáče mezi klipy) a **normalization set** [(28:42)](https://www.youtube.com/watch?v=-r4nafTJI5c&t=1722s), aby ceny z oddělených databází šly porovnávat.

**Kdy chooser (ne)potřebuješ:** chůze a běh můžou žít **v jedné databázi** — delší trajektorie běhu je odliší sama [(1:11)](https://www.youtube.com/watch?v=q-Ag6iYalAo&t=71s) a blending je hladší. Chooser nastupuje, když se trajektorie *podobají*: crouch [(5:19)](https://www.youtube.com/watch?v=q-Ag6iYalAo&t=319s). Recept: databáze jako **Dynamic value** [(10:12)](https://www.youtube.com/watch?v=q-Ag6iYalAo&t=612s), `On Update → Evaluate Chooser (All Results) → Set Databases To Search` [(11:37)](https://www.youtube.com/watch?v=q-Ag6iYalAo&t=697s) a **Interrupt Mode = on database change** [(13:07)](https://www.youtube.com/watch?v=q-Ag6iYalAo&t=787s) — bez toho přepnutí čeká, až doběhne póza.

Dvě klasické pasti: **chybějící směr** — MM vybere *nejbližší* pózu, takže bez forward loop klipu ti dopředu poběží diagonály [(12:41)](https://www.youtube.com/watch?v=YtIxWtMPYQE&t=761s); a **moc podobných póz** v jedné databázi (turn-in-place vs. pohyb) systém mate [(16:17)](https://www.youtube.com/watch?v=q-Ag6iYalAo&t=977s) — odděl je.

> **Pozn.:** Reality Forge navíc ukazuje zdroj animací zdarma: Mixamo (přes konvertor na root motion) a migrace + **one-click retargeting** animací z Lyry [(11:11)](https://www.youtube.com/watch?v=LJi_vPAuTv4&t=671s) — použitelné, než dorazí vlastní mocap. Charakter movement doladit: `Orient Rotation to Movement` vypnout / `Use Controller Desired Rotation` zapnout, jinak strafe nefunguje.

**Souvislosti:** [Principy architektury: kde co bydlí](principy-architektury.md#naradi-z-workshopu-kde-co-bydli-a-jak-se-to-hybe) · [Rejstřík: root motion](../rejstrik.md#root-motion) · [Rejstřík: chooser](../rejstrik.md#chooser) · [Rejstřík: Pose Search Database](../rejstrik.md#pose-search-database)

---

## Sparse set: 13 animací stačí na start

**Zdroj:** [Embracing Motion Matching: Using a Little to Get a Lot | Unreal Fest Bali 2025](https://www.youtube.com/watch?v=FLDXtAV7qsw) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~48 min, přednáška senior tech animátora Epicu

**Shrnutí:** Mýtus číslo jedna: „na Motion Matching potřebuju 500 animací jako GASP" [(3:39)](https://www.youtube.com/watch?v=FLDXtAV7qsw&t=219s). Přednáška ho bourá prakticky: **non-strafing set = ~13 animací** [(11:39)](https://www.youtube.com/watch?v=FLDXtAV7qsw&t=699s), strafing ~26 [(13:16)](https://www.youtube.com/watch?v=FLDXtAV7qsw&t=796s), s crouch/jump/sprint stavy ~60–80 [(14:39)](https://www.youtube.com/watch?v=FLDXtAV7qsw&t=879s) — zvládnutelné pro sólo tým, klidně hand-keyed a stylizované [(15:14)](https://www.youtube.com/watch?v=FLDXtAV7qsw&t=914s). A hlavní metodická rada: **nejdřív movement model, pak animace.**

### Rozpad myšlenky

**Movement model first** [(7:08)](https://www.youtube.com/watch?v=FLDXtAV7qsw&t=428s): postaru se animovalo podle zadání designéra a pohyb hry se ladil k animacím. S MM je to obráceně — nejdřív vylaď kapsli (akcelerace, rychlosti, decelerace), dokud *pocitově* nesedí [(7:35)](https://www.youtube.com/watch?v=FLDXtAV7qsw&t=455s), pak pohyb **nahraj rewind debuggerem a exportuj** [(8:42)](https://www.youtube.com/watch?v=FLDXtAV7qsw&t=522s) (5.6 má tlačítko v trajectories; starší verze přes Take Recorder) a animátor animuje *proti té křivce*. K tomu rozhodnutí předem: capsule driven vs. root motion driven [(7:49)](https://www.youtube.com/watch?v=FLDXtAV7qsw&t=469s) (GASP je capsule driven, ale animace mají root motion — použitelné obojím způsobem); a hygiena root kosti (postava centrovaná v kapsli, sledovat deltu hrudník/pelvis vs. root — „Spine 5 trik").

**Co do minimálního setu** [(11:39)](https://www.youtube.com/watch?v=FLDXtAV7qsw&t=699s): idle, run forward, starty, stopy, **run arcs** (oblouky — lepší foot crossover v zatáčkách [(12:19)](https://www.youtube.com/watch?v=FLDXtAV7qsw&t=739s)) a refacing starty — všechno v **levé i pravé nohové variantě** [(11:54)](https://www.youtube.com/watch?v=FLDXtAV7qsw&t=714s): při stutter-stepu na klávesnici MM najde start z druhé nohy a vypadá to přirozeně. Strafing přidá zadní a boční starty/stopy — 2× tolik. Rozsah řídí **otázky na hru** [(6:06)](https://www.youtube.com/watch?v=FLDXtAV7qsw&t=366s): co gameplay potřebuje? kolik movement states? (každý stav ≈ zdvojnásobení). Schema sparse setu měří trajektorii, rozestup a rychlost chodidel a pelvis — víc měřit = dráž a hůř.

Výsledek: 13animační set vedle 500animačního GASP vypadá překvapivě dobře — a **26 animací s procedurálními uzly je podle Epicu shippable** pro spoustu her [(35:53)](https://www.youtube.com/watch?v=FLDXtAV7qsw&t=2153s), zvlášť indie a mobile. Základ, na který se dá růst.

> **Pozn.:** Pro nás asi nejdůležitější sdělení celého batche: MM není „AAA technologie pro AAA obsah", ale systém, kde malý, *dobře vybraný* set + procedurální dolaďování porazí velký neuspořádaný. Stejná filozofie jako [design by constraint](../teorie/scope.md#design-by-constraint-krabice-napred-napad-dovnitr) — omezení jako výchozí bod. Quadrupedi (kůň): měřit přední a zadní nohy zvlášť; viz GDC talk o koních v RDR2, na který přednáška odkazuje.

**Souvislosti:** [Scope: malé hry](../teorie/scope.md) · [Rejstřík: sparse set](../rejstrik.md#sparse-set) · [Rejstřík: root motion](../rejstrik.md#root-motion)

---

## Od 70 % ke 100 %: ladění, biasy a procedurální uzly

**Zdroj:** [Motion Matching and the Game Animation Sample in UE 5.4 | Unreal Fest 2024](https://www.youtube.com/watch?v=tNw9lD2PW3U) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · debug část ·
[Embracing Motion Matching | Unreal Fest Bali 2025](https://www.youtube.com/watch?v=FLDXtAV7qsw) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · stitching a procedurální uzly

**Shrnutí:** Epic sám říká, že tutoriály tě dostanou na 70 % — tahle myšlenka je o zbylých 30 % [(2:35)](https://www.youtube.com/watch?v=tNw9lD2PW3U&t=155s): číst ceny v pose search debuggeru, ohýbat výběr notify tagy místo přepisování schémat, a čtyři procedurální uzly, které z řídkého setu udělají plný dojem.

### Rozpad myšlenky

**Ladění = čtení cen.** Rewind debugger (zapni auto-record a auto-eject) nahraje běh hry; **pose search debugger** pak pro každý frame ukáže **continuing pose** a vítěze s cenami [(17:29)](https://www.youtube.com/watch?v=tNw9lD2PW3U&t=1049s) — a **channels breakdown** [(18:05)](https://www.youtube.com/watch?v=tNw9lD2PW3U&t=1085s) rozloží cenu po kanálech: přesně vidíš, *který* kanál rozhodl. Ladění schémat je „umělecký proces" — experimentuj [(15:47)](https://www.youtube.com/watch?v=tNw9lD2PW3U&t=947s); a databáze klidně děl podle stavů s vlastními schématy (při skoku ti na pozici chodidel záleží míň než při běhu [(15:39)](https://www.youtube.com/watch?v=tNw9lD2PW3U&t=939s)).

**Chirurgie místo přestavby — anim notify tagy:** když pozdě ve vývoji nesedí výběr, neměň schema (ovlivní celou hru) — označ animaci: **Override Continuing Pose Bias** [(19:40)](https://www.youtube.com/watch?v=tNw9lD2PW3U&t=1180s) „preferuj tuhle animaci, i když matematicky nevyhrává" (takhle GASP protlačil hezké refacing turny), **Exclude From Database** [(20:05)](https://www.youtube.com/watch?v=tNw9lD2PW3U&t=1205s) „tenhle úsek nikdy nevybírej" a **Block Transition** [(20:11)](https://www.youtube.com/watch?v=tNw9lD2PW3U&t=1211s) „z tohohle úseku ven ano, dovnitř ne".

**Čtyři procedurální uzly** (Bali; všechny v GASP k okoukání):

- **Offset Root Bone** [(29:24)](https://www.youtube.com/watch?v=FLDXtAV7qsw&t=1764s): laditelná pružina mezi kapslí a root kostí — kapsle zůstane responzivní, mesh se dotahuje „s máslem". (Cena: mesh může vyjet z kapsle u zdí [(31:31)](https://www.youtube.com/watch?v=tNw9lD2PW3U&t=1891s).)
- **Steering** [(30:31)](https://www.youtube.com/watch?v=FLDXtAV7qsw&t=1831s): zpomalí skokovou změnu směru (klávesnice: 0→1 za frame), aby MM stíhal vybírat — v grafu *před* offset root bone; desired facing se čte z trajektorie ~0,5 s dopředu.
- **Foot Placement** [(28:53)](https://www.youtube.com/watch?v=FLDXtAV7qsw&t=1733s): IK na svazích + **zamykání chodidel** podle křivek z animation modifieru — hlavní zbraň proti foot slidingu.
- **Mesh-space additive lean/aim** [(28:56)](https://www.youtube.com/watch?v=FLDXtAV7qsw&t=1736s): náklon těla a pohled do zatáčky — „intencionalita" pohybu za pár additivních klipů.

**Kam to roste — stitching** [(16:02)](https://www.youtube.com/watch?v=FLDXtAV7qsw&t=962s): experimentální technika (od 5.4), která místo lineárního blendu *najde animaci*, jež tě za daný čas dostane z aktuální pózy do cílové — základ pro přechody locomotion → gameplay akce (Witcher 4 demo, sequencer stitch track v 5.6). Nosné uzly: **Blend Stack** [(20:15)](https://www.youtube.com/watch?v=FLDXtAV7qsw&t=1215s) (změna proměnné = nový blend do zásobníku; uvnitř MM uzlu běží graf per vybraná animace — tam žije orientation warping [(12:55)](https://www.youtube.com/watch?v=tNw9lD2PW3U&t=775s)) a **Chooser Player** se stitch volbou. Pro diskrétní akce: **Pose Search Branch In** [(24:58)](https://www.youtube.com/watch?v=tNw9lD2PW3U&t=1498s) — okno v montáži, do kterého se smí matchovat — a blueprint funkce **Motion Match** [(22:17)](https://www.youtube.com/watch?v=tNw9lD2PW3U&t=1337s), kterou zavoláš odkudkoli nad libovolným seznamem assetů. Tyhle nástroje jsou přesně to, na čem stojí traversal a combat systémy z [navazující kapitoly](mm-systemy.md).

**Souvislosti:** [Systémy nad Motion Matchingem](mm-systemy.md) · [Rejstřík: blend stack](../rejstrik.md#blend-stack) · [Rejstřík: stitching](../rejstrik.md#stitching) · [Rejstřík: continuing pose](../rejstrik.md#continuing-pose)
