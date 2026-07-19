# Mover: nový pohybový systém

Mover je nástupce Character Movement Componentu — a tahle kapitola je jeho samostatný portrét: **proč vznikl a jak je navržený** (přednáška architekta z Unreal Festu), **jak se s ním staví postava od nuly v 5.7** včetně síťových záludností, a **jak opravit strafe** v GASP Mover pawnovi. Praktické nasazení Moveru v GASP (movement modes v Blueprintu, smooth walking, rotation offsety) rozebírá [kapitola o GASP](gasp.md#mover-pohyb-jako-modularni-blueprintovatelna-simulace) — tady jde o systém samotný.

---

## Proč Mover existuje: modularita, vstupy a dvě síťové větve

**Zdroj:** [An Introduction to the Mover Plugin | Unreal Fest 2024](https://www.youtube.com/watch?v=P4IKS5k47Wg) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~42 min, přednáška engineera, který Mover vede

**Shrnutí:** CMC je po 20 letech obětí vlastní univerzálnosti: strmá učící křivka, matematika pohybu zamotaná do networkingu a rewind/resim logiky [(2:25)](https://www.youtube.com/watch?v=P4IKS5k47Wg&t=145s), povinný Character pawn s kapslí [(3:11)](https://www.youtube.com/watch?v=P4IKS5k47Wg&t=191s), bespoke replikace, která se nekamarádí s GAS [(3:58)](https://www.youtube.com/watch?v=P4IKS5k47Wg&t=238s), a rozšiřování jen přes C++ dědičnost [(4:46)](https://www.youtube.com/watch?v=P4IKS5k47Wg&t=286s). Mover to obrací: komponenta na **libovolném actoru s libovolným tvarem**, movement modes jako vyměnitelné objekty a replikace postavená čistě na vstupech.

### Rozpad myšlenky

**Stavební kameny** [(14:55)](https://www.youtube.com/watch?v=P4IKS5k47Wg&t=895s):

- **Movement modes** — jeden aktivní; *generují* navržený pohyb a odděleně ho *vykonávají*. Přepnutí umí proběhnout uprostřed timestepu — falling spotřebuje půlku času, walking dostane zbytek.
- **Transitions** — objekty s dotazovací logikou: na módu (výstupní podmínky) nebo globální (environmentální trigger — autor jimi prototypoval zipline) [(17:15)](https://www.youtube.com/watch?v=P4IKS5k47Wg&t=1035s).
- **Layered moves** — nástupce root motion sources: dočasné zdroje rychlosti (dash, naváděný útok, jump), klidně několik naráz; mixují se nebo přepisují podle priority a výsledek zpracuje aktivní mód [(15:42)](https://www.youtube.com/watch?v=P4IKS5k47Wg&t=942s). Důsledek: **animation root motion je rovnoprávný občan** — v CMC platilo root motion *nebo* řízený pohyb, tady je root motion jen další layered move a jde míchat [(19:33)](https://www.youtube.com/watch?v=P4IKS5k47Wg&t=1173s).
- **Composable inputs a state** — vstupy i stav simulace jsou kolekce structů, do kterých projekt přidává vlastní (cokoli net-serializovatelného); vstup autoruje vlastník postavy, stav je snapshot simulace [(16:29)](https://www.youtube.com/watch?v=P4IKS5k47Wg&t=989s).

**Proposed vs. executed movement** [(18:01)](https://www.youtube.com/watch?v=P4IKS5k47Wg&t=1081s) je tichý hrdina návrhu: protože „kam chci" vzniká odděleně od „co se stalo", jde simulaci zavolat *naprázdno* s fake vstupy — a přesně z toho žijí look-ahead dotazy pro Motion Matching trajektorii [(18:47)](https://www.youtube.com/watch?v=P4IKS5k47Wg&t=1127s). Proto „Mover a MM jdou ruku v ruce" — autor převedl čerstvě vydaný GASP na Mover za pár dní [(14:09)](https://www.youtube.com/watch?v=P4IKS5k47Wg&t=849s).

**Networking — největší koncepční skok.** CMC: klient posílá vstupy *i výsledek*, server přepočítává a koriguje; rollback je izolovaný (vrací se jen tvoje postava, okolí zamrzlé) a kadenci simulace diktuje tick rate klienta — 120fps hráč posílá 4× víc moves než 30fps [(25:00)](https://www.youtube.com/watch?v=P4IKS5k47Wg&t=1500s). Network Prediction větev Moveru: posílají se **jen vstupy** s časem simulace, server je bufferuje a konzumuje podle *svých* hodin, stav jen vysílá — chyby detekuje a řeší klient [(28:08)](https://www.youtube.com/watch?v=P4IKS5k47Wg&t=1688s). Rollback je **unified**: vrací se a přehrává celé okolí naráz, takže korekce bývá jedna a dost [(22:40)](https://www.youtube.com/watch?v=P4IKS5k47Wg&t=1360s). A stav je uzamčený — CMC nechává `velocity` veřejně zapisovatelnou („open to Crazy Town"), Mover vnější zásahy detekuje a varuje [(24:14)](https://www.youtube.com/watch?v=P4IKS5k47Wg&t=1454s).

**Druhá větev: Chaos networked physics** [(29:41)](https://www.youtube.com/watch?v=P4IKS5k47Wg&t=1781s) — přepínač, ne kombinace (NP *nebo* fyzika). Simulace běží asynchronně na fyzikálním vlákně (běží napřed, postava se dotahuje hladce) a korekce nemusí být rewind+resim — chyba se může akumulovat a fyzika ji postupně „eroduje" [(30:28)](https://www.youtube.com/watch?v=P4IKS5k47Wg&t=1828s). Demo: postava přetlačuje krabice, stojí na dynamických platformách, dva síťoví hráči rozhoupávají fyzikální most [(31:15)](https://www.youtube.com/watch?v=P4IKS5k47Wg&t=1875s) — s CMC nemyslitelné [(26:35)](https://www.youtube.com/watch?v=P4IKS5k47Wg&t=1595s).

**Upřímný seznam problémů (stav 5.4)** [(32:47)](https://www.youtube.com/watch?v=P4IKS5k47Wg&t=1967s): siloed ticking (pohyblivé platformy off-by-one → foot sliding), chybějící interpolace fixed-tick simulace při vyšším render rate (pohyb „chunky") [(33:33)](https://www.youtube.com/watch?v=P4IKS5k47Wg&t=2013s), C++ boilerplate pro vlastní structy (v 5.7 už vyřešeno — user-defined structy, viz [GASP](gasp.md#mover-pohyb-jako-modularni-blueprintovatelna-simulace)), neověřené škálování a vyšší nároky na bandwidth [(35:05)](https://www.youtube.com/watch?v=P4IKS5k47Wg&t=2105s), a ekosystém, který dvacet let předpokládal Character/CMC — motion warping, AI, navigace se refaktorují postupně [(36:41)](https://www.youtube.com/watch?v=P4IKS5k47Wg&t=2201s).

> **Pozn.:** Dvě uklidnění z pódia: **CMC nikam neodchází** — žádný plán deprecace, jen už nedostává nové featury [(10:10)](https://www.youtube.com/watch?v=P4IKS5k47Wg&t=610s); a pro měkký přechod existuje „default character movement set", který se chová skoro identicky jako CMC [(9:24)](https://www.youtube.com/watch?v=P4IKS5k47Wg&t=564s). Experimental u Epicu znamená „ještě jsme s tím sami neshipli" [(10:59)](https://www.youtube.com/watch?v=P4IKS5k47Wg&t=659s). Z výhledů přednášky se od té doby většina splnila (motion warping, GASP na Moveru, physics postavy v UEFN) — hezky to ilustruje, že roadmapy Epicu z Festů stojí za sledování. Pro učení: **Mover Examples plugin** v enginu, Project Titan prototypoval gliding a grappling „za odpoledne" [(13:20)](https://www.youtube.com/watch?v=P4IKS5k47Wg&t=800s).

**Souvislosti:** [GASP: Mover v praxi](gasp.md#mover-pohyb-jako-modularni-blueprintovatelna-simulace) · [MM základy: trajektorie](mm-zaklady.md#dotaz-misto-grafu-jak-motion-matching-vybira-pozy) · [Rejstřík: Mover](../rejstrik.md#mover) · [Rejstřík: movement mode](../rejstrik.md#movement-mode) · [Rejstřík: layered move](../rejstrik.md#layered-move) · [Rejstřík: Network Prediction](../rejstrik.md#network-prediction)

---

## Setup od nuly v 5.7: pawn, Input Producer a síťové pasti

**Zdroj:** [UE5 Mover Component Setup For Character (5.7) Part 1](https://www.youtube.com/watch?v=7Uu3ocESVIE) + [Part 2: Sprinting and Crouch](https://www.youtube.com/watch?v=-aYbOp65EvQ) · [Make A Real One](https://www.youtube.com/channel/UCs4uGt9XS2Tj4dGcOVFjogg) · ~41 min, follow-along

**Shrnutí:** Praktický protějšek přednášky: postavit Mover postavu z třetíosobní šablony. Kostra je rychlá (pawn + komponenta + interface), skutečná hodnota videí je v **pastech, na které narazíš**: AnimBP plný character castů, tři různé síťové záludnosti a kapsle, která se při crouchi propadá kvůli kolizi skeletal meshe.

### Rozpad myšlenky

**Kostra** [(0:34)](https://www.youtube.com/watch?v=7Uu3ocESVIE&t=34s): Mover **nefunguje na Character class** — založ Pawn, překopíruj komponenty z třetíosobní šablony, kapsli nastav collision preset `Pawn`. Přidej `Character Mover Component` a interface **Mover Input Producer** — objeví se funkce `Produce Input` [(2:15)](https://www.youtube.com/watch?v=7Uu3ocESVIE&t=135s). V ní: struct `Character Default Inputs` (směr, orient intent, control rotation, jump…), směr = osy `IA_Move` → vektor → **rotovat control rotation** → zahodit Z (pozemní pohyb) a clampnout přes 1 [(6:48)](https://www.youtube.com/watch?v=7Uu3ocESVIE&t=408s); `orient intent` = směr pohybu, ať se postava otáčí kam běží [(10:40)](https://www.youtube.com/watch?v=7Uu3ocESVIE&t=640s); struct do data collection → `Make Mover Input Cmd Context` [(9:18)](https://www.youtube.com/watch?v=7Uu3ocESVIE&t=558s). Skok = `jump just pressed` v témže structu [(12:40)](https://www.youtube.com/watch?v=7Uu3ocESVIE&t=760s).

**AnimBP bez Characteru** [(13:26)](https://www.youtube.com/watch?v=7Uu3ocESVIE&t=806s): šablonový AnimBP castí na Character — obojí pryč: `Get Pawn Owner` → cast na vlastního pawna, velocity číst z Mover komponenty, acceleration ze vstupů a stav pádu z **movement mode name** (`Falling` existuje out of the box) [(17:09)](https://www.youtube.com/watch?v=7Uu3ocESVIE&t=1029s). Základní `walking` mód má nastavení minimum; **smooth walking** přidá akceleraci/deceleraci/turning strength — klouzání po puštění vstupu řeší decelerace ~4000 [(17:56)](https://www.youtube.com/watch?v=7Uu3ocESVIE&t=1076s).

**Tři síťové pasti** (každá umí sežrat večer):

1. Sim proxy se klepe → na actoru **vypnout `Replicate Movement`** — pohyb replikuje Mover, ne actor [(19:39)](https://www.youtube.com/watch?v=7Uu3ocESVIE&t=1179s).
2. Animace na ostatních klientech stojí → AnimBP musí číst **replikované** vstupy (`Last Input Cmd` → Get Data From Collection), ne lokální proměnnou [(21:03)](https://www.youtube.com/watch?v=7Uu3ocESVIE&t=1263s).
3. Sim proxy „gumují" (krok vpřed a zpět po ťuknutí) → Project Settings → **Network Prediction** → interpolated režim [(1:41)](https://www.youtube.com/watch?v=-aYbOp65EvQ&t=101s) a na Mover komponentě v advanced zapnout **Sync Inputs for Sim Proxy** [(2:27)](https://www.youtube.com/watch?v=-aYbOp65EvQ&t=147s).

**Crouch** [(3:14)](https://www.youtube.com/watch?v=-aYbOp65EvQ&t=194s): vlastní struct (`wants crouch`, `wants sprint`) přidávaný v `Produce Input`; čtení na eventu **Pre-Simulation Tick** Mover komponenty → `Try Crouch` [(6:46)](https://www.youtube.com/watch?v=-aYbOp65EvQ&t=406s). Funguje až s **shared settings**: na komponentu přidat `Stance Settings` (crouch half height, crouched max speed) [(8:03)](https://www.youtube.com/watch?v=-aYbOp65EvQ&t=483s). A past na závěr: kapsle se zmenší, ale postava se propadá — **skeletal mesh musí mít No Collision**, s Moverem si jeho kolize s kapslí rozbije stance [(9:32)](https://www.youtube.com/watch?v=-aYbOp65EvQ&t=572s).

**Sprint** [(10:51)](https://www.youtube.com/watch?v=-aYbOp65EvQ&t=651s): child mód od smooth walking, override `Generate Simple Walk Move`, z input kolekce vytáhnout custom struct a podle `wants sprint` přepsat max speed — tentýž vzor, který detailně (včetně kontextové decelerace) ukazuje [GASP kapitola](gasp.md#mover-pohyb-jako-modularni-blueprintovatelna-simulace); tady navíc připomínka replikovat i custom struct [(16:21)](https://www.youtube.com/watch?v=-aYbOp65EvQ&t=981s).

> **Pozn.:** Follow-along se vším všudy — autor v části replikace sám chvíli tápe („actually I'm not sure how to do that") a řešení hledá naživo. Hodnota není v eleganci, ale v tom, že na kameru narazil na přesně ty problémy, které potkají každého. Checklist z obou videí (Pawn class, Replicate Movement off, replikované vstupy v AnimBP, NP interpolated, Sync Inputs, mesh No Collision) je to, co si z nich odnést.

**Souvislosti:** [GASP: Mover v praxi](gasp.md#mover-pohyb-jako-modularni-blueprintovatelna-simulace) · [Základy pohybu: klouzání po zdi](pohyb-zaklady.md#klouzani-po-zdi-misto-zastaveni-dokonceni-predchozi-myslenky) *(komponenta napojená na Get Move Input)* · [Rejstřík: Mover](../rejstrik.md#mover) · [Rejstřík: movement mode](../rejstrik.md#movement-mode) · [Rejstřík: Network Prediction](../rejstrik.md#network-prediction)

---

## Strafe na osm směrů: oprava GASP Mover pawna

**Zdroj:** [How To Make Better Looking Locomotion in Mover 2.0](https://www.youtube.com/watch?v=gFDxFskLtck) · [Zero2GameDev](https://www.youtube.com/channel/UCXloD6nri7psCbJYOBBnpRg) · ~10 min, tutoriál

**Shrnutí:** GASP Mover pawn detekuje směr pohybu jen ve **čtyřech** směrech — diagonální běh proto dorovnává rotací kapsle a postava při strafu běží bokem nebo zády ke směru, což rozbíjí míření [(0:02)](https://www.youtube.com/watch?v=gFDxFskLtck&t=2s). Oprava: rozšířit enum směrů na osm, detekovat úhlová pásma a diagonálám dát vlastní animace místo rotace.

### Rozpad myšlenky

**Kde to bydlí:** v sandbox moveru funkce `Get Movement Direction From Thresholds` zná jen forward/left/right/back; výsledek jde do chooseru, který vyrábí rotation offset kapsle [(1:35)](https://www.youtube.com/watch?v=gFDxFskLtck&t=95s). K tomu enum `E_MovementDirection` s matoucími názvy (LL = left, RL = right…) a bez zadních diagonál — první krok je **přejmenovat a doplnit** back-left/back-right [(2:21)](https://www.youtube.com/watch?v=gFDxFskLtck&t=141s).

**Detekce po pásmech:** print stringem zjistíš úhly (forward ≈ 0°, diagonály ±45°, strany ±90°, zadní diagonály ±135°) a thresholds nahradíš řetězem **In Range Float** kontrol s pásmem ±1° kolem každé hodnoty [(3:07)](https://www.youtube.com/watch?v=gFDxFskLtck&t=187s). Rotaci kapsle nech **jen pro sliding** (`current movement mode == sliding` → stará větev), všechno ostatní vrací čistý směr [(6:12)](https://www.youtube.com/watch?v=gFDxFskLtck&t=372s).

**Animace pro diagonály:** v chooseru `stand runs` přidat čtyři **nested choosery** (FL/FR/BL/BR), obsah zkopírovat z existujících směrů a vyměnit klipy za diagonální varianty relaxed setu [(6:59)](https://www.youtube.com/watch?v=gFDxFskLtck&t=419s). Dvě pasti: diagonálním klipům je potřeba ručně zapnout **Loop** (default vypnutý) [(8:32)](https://www.youtube.com/watch?v=gFDxFskLtck&t=512s) a staré čtyřsměrové řádky odškrtnout, jinak s novými soupeří [(10:02)](https://www.youtube.com/watch?v=gFDxFskLtck&t=602s).

> **Pozn.:** Ukázková „chirurgie" na cizím systému: žádné přepisování, jen enum + detekční funkce + řádky chooseru — přesně tak je GASP navržený k ohýbání (viz [kontrola výběru](gasp.md#kontrola-vyberu-databaze-podle-stavu-nested-choosery-interrupt-mode)). Autor slibuje stejný fix pro climbing zvlášť; v playlistu zatím není.

**Souvislosti:** [GASP: kontrola výběru](gasp.md#kontrola-vyberu-databaze-podle-stavu-nested-choosery-interrupt-mode) · [GASP: Mover v praxi](gasp.md#mover-pohyb-jako-modularni-blueprintovatelna-simulace) · [Rejstřík: chooser](../rejstrik.md#chooser) · [Rejstřík: GASP](../rejstrik.md#gasp)
