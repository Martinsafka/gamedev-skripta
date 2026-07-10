# Systémy nad Motion Matchingem

Motion Matching řeší locomotion — ale hra potřebuje i útoky, krytí, šplhání a interakce. Tahle kapitola sbírá vzory, jak na MM **navrstvit gameplay systémy**: combat přes montáže a choosery, traversal a cover přes komponenty se state managerem, a výhled tam, kam to celé míří — nescriptované interakce z Witcher 4 dema.

---

## Combat nad MM: horní tělo v montáži, spodní v matchingu

**Zdroj:** [Unreal Engine 5.4: Combining Attack Animations with Motion Matching in Custom Characters](https://www.youtube.com/watch?v=BDjGNdMlEAg) · [The Epic Singh](https://www.youtube.com/channel/UCIUODgrq00Z_ZrhHENQTrVg) · ~34 min ·
[How To Set Up Combat Using Choosers - Unreal Engine 5](https://www.youtube.com/watch?v=G41RGiXLhnE) · [Clydiie](https://www.youtube.com/channel/UCyf25GpFdB5NhNyzPhc_T6w) · ~9 min ·
[Motion Matching | Flexible Combat System | Unreal Engine 5](https://www.youtube.com/watch?v=V1I9gdJD45g) · [Beardgames](https://www.youtube.com/channel/UCaBjhTykCgcQQP5Ecqq9_CQ) · ~11 min, integrace do existujícího projektu

**Shrnutí:** Základní vzor combatu nad MM: **spodní polovinu těla nech matchovat, horní hraje montáž** ve slotu. K tomu combo řetěz řízený anim notifiers a chooser tabulka jako výběr útoku. A když MM taháš do *existujícího* combat projektu, čeká tě checklist slotů, trace channelů a ladění pohybu.

### Rozpad myšlenky

**Vrstvení (The Epic Singh, na retargetovaných Paragon postavách):** útok spustí event dispatcher z characteru [(3:03)](https://www.youtube.com/watch?v=BDjGNdMlEAg&t=183s), na který se AnimBP binduje; montáž hraje ve slotu **Upper Body** a do výsledné pózy se míchá přes **Layered Blend Per Bone** [(21:15)](https://www.youtube.com/watch?v=BDjGNdMlEAg&t=1275s) + **Blend Poses by Bool** [(22:35)](https://www.youtube.com/watch?v=BDjGNdMlEAg&t=1355s): `IsAttacking` → horní tělo z montáže, jinak celé tělo z MM. Výsledek: postava útočí v běhu, ve skoku i v podřepu — locomotion nikdy nepřestal běžet. U retargetovaných postav pozor: montáž hraj na **správném skeletal meshi** (`Play Montage` s mesh parametrem [(18:10)](https://www.youtube.com/watch?v=BDjGNdMlEAg&t=1090s)) a bonusový trik — dynamika ocasu Wukonga přes AnimDynamics v animation layeru [(7:45)](https://www.youtube.com/watch?v=BDjGNdMlEAg&t=465s).

**Combo přes chooser (Clydiie):** chooser tabulka s result class **Anim Montage** [(1:32)](https://www.youtube.com/watch?v=G41RGiXLhnE&t=92s), vstupem combat komponenta a sloupcem **float range na combo count** [(4:21)](https://www.youtube.com/watch?v=G41RGiXLhnE&t=261s) — combo 0/1/2 vybere první/druhý/třetí útok. Okna comba řídí **anim notifies** `AddCombo`/`ResetCombo` [(3:34)](https://www.youtube.com/watch?v=G41RGiXLhnE&t=214s) umístěné v animacích: stiskneš v okně → další útok, nestiskneš → reset. Chooser umí i **output sloupce** [(8:41)](https://www.youtube.com/watch?v=G41RGiXLhnE&t=521s) — např. damage per útok přímo v tabulce. Autor poctivě dodává [(0:25)](https://www.youtube.com/watch?v=G41RGiXLhnE&t=25s): tohle je chooser-driven výběr animací, ne pravý motion matching — pro skutečné MM combat by animace žily v PSD a chooser by jen zužoval výběr.

**Integrace do existujícího projektu (Beardgames, GASP → Flexible Combat System):** přenositelný checklist [(0:28)](https://www.youtube.com/watch?v=V1I9gdJD45g&t=28s) — anim slot skupiny (`traversal ik`) přes Anim Slot Manager [(1:32)](https://www.youtube.com/watch?v=V1I9gdJD45g&t=92s), trace channel `Traversable` [(1:50)](https://www.youtube.com/watch?v=V1I9gdJD45g&t=110s), pluginy, traversal komponenty na characteru [(4:50)](https://www.youtube.com/watch?v=V1I9gdJD45g&t=290s). A hlavně ladění pocitu: **max acceleration ↓ na ~1700** [(9:59)](https://www.youtube.com/watch?v=V1I9gdJD45g&t=599s), aby kapsle seděla k MM animacím (přesně [movement model first](mm-zaklady.md#sparse-set-13-animaci-staci-na-start) v praxi), camera lag podle GASP [(9:36)](https://www.youtube.com/watch?v=V1I9gdJD45g&t=576s) a workaround na známý bug s kamerou v zdi při traversalu [(10:17)](https://www.youtube.com/watch?v=V1I9gdJD45g&t=617s).

**Souvislosti:** [MM základy: blend stack a Pose Search Branch In](mm-zaklady.md#od-70-ke-100-ladeni-biasy-a-proceduralni-uzly) · [Rejstřík: anim montage](../rejstrik.md#anim-montage) · [Rejstřík: chooser](../rejstrik.md#chooser)

---

## Traversal, cover a šplhání: komponenty se state managerem

**Zdroj:** [UE5 Motionmatching ParkourSystem and Motionmatching Cover System Component Setup](https://www.youtube.com/watch?v=bxKzYbA50l0) + [MotionMatching Cover System Component Setup](https://www.youtube.com/watch?v=vm5aPoXgtWM) · [Make A Real One](https://www.youtube.com/channel/UCs4uGt9XS2Tj4dGcOVFjogg) · ~50 min ·
[Master Motion Matching: Climb Everywhere & Export Like a Pro](https://www.youtube.com/watch?v=N60w1Nk0sKU) · [Mask Devlog](https://www.youtube.com/channel/UCyNak3S3u9Z1ZFqtYloA1Dw) · ~12 min

**Shrnutí:** Traversal systémy nad GASP sdílejí architekturu: **actor komponenty** (parkour, cover, inventář) orchestrované **state managerem** [(0:43)](https://www.youtube.com/watch?v=bxKzYbA50l0&t=43s), napojené do AnimBP přes **linked anim graphs s tagy**. A když GASP traversal odmítá šplhat na běžnou geometrii, existuje komunitní oprava.

### Rozpad myšlenky

**Architektura komponent (Make A Real One):** state manager rozhoduje, kdo smí co — pohybová logika se ptá `CanMoveNormal`/`CanChangeGait` [(6:58)](https://www.youtube.com/watch?v=vm5aPoXgtWM&t=418s) a při krytí či šplhu předává řízení komponentě. Do AnimBP se systémy zapojují jako **linked anim graph s tagem** („parkour" [(2:52)](https://www.youtube.com/watch?v=bxKzYbA50l0&t=172s), „overlay" [(2:58)](https://www.youtube.com/watch?v=vm5aPoXgtWM&t=178s)) — tag umožňuje komponentám sáhnout na anim instanci zvenčí [(3:13)](https://www.youtube.com/watch?v=vm5aPoXgtWM&t=193s). Detaily, které rozbíjejí projekty a tady jsou vyřešené: montážní sloty pro zbraně patří do **vlastní slot skupiny** [(16:30)](https://www.youtube.com/watch?v=vm5aPoXgtWM&t=990s) (jinak výměna zbraně přeruší šplh); rotační režim root offsetu podmínit **offset lock křivkou**; po šplhu omezit rychlost otáčky (~500), ať se postava „nesroluje" [(22:50)](https://www.youtube.com/watch?v=bxKzYbA50l0&t=1370s); a bug „postava se v coveru otáčí zády" řeší odškrtnutí **mirrored motion** v mirror data assetu [(22:20)](https://www.youtube.com/watch?v=vm5aPoXgtWM&t=1340s). Cover se definuje **cover actorem se splinou** [(23:16)](https://www.youtube.com/watch?v=bxKzYbA50l0&t=1396s) (+ high cover přepínač [(20:11)](https://www.youtube.com/watch?v=vm5aPoXgtWM&t=1211s)) a hledá se tlačítkem, ne tickem — trace každý frame by byl drahý [(11:39)](https://www.youtube.com/watch?v=vm5aPoXgtWM&t=699s). Omezení šplhu per objekt: tag na *komponentě*, ne actoru [(8:32)](https://www.youtube.com/watch?v=bxKzYbA50l0&t=512s).

**Šplhej kdekoli (Mask Devlog):** GASP traversal funguje jen na vlastních **Traversable blocích** [(4:42)](https://www.youtube.com/watch?v=N60w1Nk0sKU&t=282s) (ukazují výšku — výkon skoku se liší podle výšky i tloušťky [(5:04)](https://www.youtube.com/watch?v=N60w1Nk0sKU&t=304s)). Komunitní plugin (Umut Faruk [(5:38)](https://www.youtube.com/watch?v=N60w1Nk0sKU&t=338s)) to obchází: dvě actor komponenty `AC_TraceTraversal` nahradí `Try Traversal` volání v IA_Jump [(8:02)](https://www.youtube.com/watch?v=N60w1Nk0sKU&t=482s) — a postava šplhá i na standardní geometrii, takže starý blockout nemusíš přestavovat. Limity: bez hloubkových profilů, nerovných hran a kulatých rohů [(9:50)](https://www.youtube.com/watch?v=N60w1Nk0sKU&t=590s); zákaz šplhu = tag `banned` na objektu [(11:12)](https://www.youtube.com/watch?v=N60w1Nk0sKU&t=672s). Bonus: export GASP postavy do jiného projektu migrací s hotovým retargetingem [(1:04)](https://www.youtube.com/watch?v=N60w1Nk0sKU&t=64s) — pluginy pak jen doaktivovat.

> **Pozn.:** Oba kanály staví na vzorech z [batche o architektuře](principy-architektury.md): komponenty s jedinou zodpovědností, state manager jako rozhodčí, tagy jako kontrakt. Videa Make A Real One jsou spíš „follow-along" k jeho placeným komponentám než výuka — cenné jsou hlavně ty opravy okrajových případů (slot skupiny, mirror data, rotace po šplhu), na které jinak narazíš sám.

**Souvislosti:** [Principy architektury](principy-architektury.md) · [MM základy](mm-zaklady.md) · [Rejstřík: linked anim graph](../rejstrik.md#linked-anim-graph) · [Rejstřík: traversal](../rejstrik.md#traversal)

---

## Kam to míří: nescriptované interakce (Witcher 4)

**Zdroj:** [Unscripted Motion Matching Interactions In The Witcher 4](https://www.youtube.com/watch?v=dd35tkF-5io) · [Clydiie](https://www.youtube.com/channel/UCyf25GpFdB5NhNyzPhc_T6w) · ~7 min, komentář k tech demu

**Shrnutí:** Witcher 4 tech demo (standardní PS5, 60 fps s ray tracingem) ukazuje, co z MM roste dál: **multi-character motion matching** [(0:40)](https://www.youtube.com/watch?v=dd35tkF-5io&t=40s) — nasedání na koně z libovolného úhlu a rychlosti [(0:51)](https://www.youtube.com/watch?v=dd35tkF-5io&t=51s), root motion kůň [(0:57)](https://www.youtube.com/watch?v=dd35tkF-5io&t=57s) — a hlavně **nescriptované interakce** s davem, které diváci mylně považovali za nascriptované pro demo [(1:45)](https://www.youtube.com/watch?v=dd35tkF-5io&t=105s).

### Rozpad myšlenky

Tržní scéna z dema: Ciri vrazí do nosiče, ten upustí jablko, kluk ho sebere, prasata se seběhnou [(2:22)](https://www.youtube.com/watch?v=dd35tkF-5io&t=142s) — řetěz reakcí, žádný skript. Pod kapotou (video cituje Unreal Fest talk CDPR): **pose search interaction data assety** [(4:46)](https://www.youtube.com/watch?v=dd35tkF-5io&t=286s) — MM databáze pro *interakce mezi postavami*: vrážení do stojících NPC z různých úhlů a s různými pózami [(3:04)](https://www.youtube.com/watch?v=dd35tkF-5io&t=184s), pozdravy dvou jdoucích NPC, funkční i na svahu. Stejný princip jako locomotion matching, jen dotaz zahrnuje dvě postavy — přesně ta „multi-character MM" budoucnost, kterou Epic avizoval na [Unreal Festu](mm-zaklady.md#od-70-ke-100-ladeni-biasy-a-proceduralni-uzly).

Co z toho pro nás: Epic naznačuje, že ukázka podobného systému dorazí do budoucí verze [Game Animation Sample](gasp.md); a od 5.6 jdou zapnout **UAF (Unreal Animation Framework)** pluginy [(5:51)](https://www.youtube.com/watch?v=dd35tkF-5io&t=351s) — základ nové animační architektury, zatím bez dokumentace. Sledovat, nestavět na tom.

> **Pozn.:** Tohle video je spíš ochutnávka než návod — jeho hodnota je orientační: říká, *kterým směrem* se MM ekosystém hýbe (interakce, davy, více postav) a že GASP je platforma, kam tyhle věci budou přistávat. Pro stealth adventuru je „vrážení do NPC" mimochodem přesně ten druh systémové drobnosti, která dělá [imerzi](../teorie/game-feel.md#imerze-svet-ktery-na-tebe-odpovida).

**Souvislosti:** [MM základy](mm-zaklady.md) · [Game feel a imerze](../teorie/game-feel.md) · [GASP: Game Animation Sample](gasp.md)
