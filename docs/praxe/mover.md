# Mover: nový pohybový systém

Mover je nástupce Character Movement Componentu — a tahle kapitola je jeho samostatný portrét: **proč vznikl a jak je navržený** (přednáška architekta z Unreal Festu), **jak se s ním staví postava od nuly v 5.7** včetně síťových záludností, **jak opravit strafe** v GASP Mover pawnovi a dvě myšlenky z přednášky fyzikálního týmu: **postava jako fyzikální těleso** (Chaos Mover) a **jak se fyzika drží v síti** (snímky, resimulace, input decay). Praktické nasazení Moveru v GASP (movement modes v Blueprintu, smooth walking, rotation offsety) rozebírá [kapitola o GASP](gasp.md#mover-pohyb-jako-modularni-blueprintovatelna-simulace) — tady jde o systém samotný.

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

---

## Chaos Mover: postava jako fyzikální těleso se stropem síly

**Zdroj:** [A Dive Into Networked Physics-Based Character Movement | Unreal Fest Stockholm 2025](https://www.youtube.com/watch?v=_jRLlTDqoGI) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~41 min, přednáška (fyzikální tým Epicu; Chaos Mover experimentální, v 5.7)

**Shrnutí:** Výchozí postava v Unrealu je kinematická kapsle s nekonečnou hmotností. Kód ji posouvá a kolize řeší dotazy na překryv, takže každou fyzikální interakci musí pohybový kód znát a mít naprogramovanou zvlášť. Chaos Mover z postavy dělá dynamické těleso ve fyzikálním světě. Pohybový mód spočítá cíl jako dřív, ale k cíli postavu táhne vlastní constraint, který smí použít jen nastavenou sílu a moment. Háček: když nic nepřekáží, je pohyb přesně stejný jako u kinematické postavy. Rozdíl se ukáže teprve ve chvíli, kdy postava do něčeho narazí, něco tlačí nebo na něčem stojí.

### Rozpad myšlenky

**Proč.** Kinematická kapsle se posune, zkontroluje překryvy, vycouvá z nich a dojede zbytek kroku [(0:53)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=53s). Fyzikální interakce jdou, ale pohybový kód jim musí rozumět a většinou jsou jednosměrné [(1:39)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=99s). Cílem je postava simulovaná ve fyzikálním světě s obousměrnými interakcemi, kde hraje roli její hmotnost, hybnost i tření. A protože solver už umí vyřešit víc kolizí najednou, odpadá ruční kód pro zakřivené plochy a rohy [(2:25)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=145s).

**Co se tím získá.**
- Těžká věc postavu přibrzdí, lehká skoro ne, a tlačit jde i několik věcí najednou. S rozběhem postava pohne i něčím těžším, ze stoje tření nepřekoná [(3:58)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=238s).
- Sílu, kterou postava na svět působí, jde ladit a postava zároveň reaguje na vnější síly a srážky [(4:44)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=284s).
- Na pérující plošině postava pružinu stlačí a ta ji vrátí nahoru. Jen přes síly by se to stabilní dostávalo velmi těžko, rovnováhu spolehlivě najde až solver [(5:30)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=330s).
- Kinematická postava, která klouže po svahu podél zdi s malou římsou, vezme římsu za strop a zastaví se. Fyzikální po hraně prostě sklouzne [(5:50)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=350s).

**Jak se zapíná.** Postava má dál Mover komponentu s pohybovými módy, přechody a nastavením. Liší se backend: třída, která určuje, jak simulace tiká a jak se replikují vstupy a stav, se přepne na Chaos Mover backend [(6:40)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=400s). Módy chůze a pádu mají fyzikální verze s limitem síly a momentu pro každý mód [(7:26)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=446s). Plugin je experimentální a je k dispozici od 5.7. Zapíná se spolu s pluginem Mover a ukázkovou fyzikální postavu má plugin Mover Examples. Fyzikální postava v UEFN stojí na stejné technologii [(20:33)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=1233s).

**Constraint místo posouvání.** Constraint v solveru Chaosu dostane cílovou polohu a orientaci a táhne k nim těleso, ale jen do zadaného limitu síly a momentu [(7:26)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=446s), [(8:12)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=492s). Když nic nepřekáží, postava cíl splní přesně. Když vejde do zdi, constraint kolize smí použít větší sílu a vyhraje, takže pohybový constraint se dostane co nejblíž cíli a do zdi nevnikne [(8:59)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=539s).

Druhá polovina drží postavu nad zemí. Uživatel zadá vzdálenost a normálu země a postava musí být od roviny země aspoň tak daleko [(8:59)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=539s). Zem se hledá dotazem, ne kolizí kapsle, ze dvou důvodů. Dává to kontrolu nad tím, jak postava jede po nerovném terénu a schodech. A kolize, která kapsli vytlačí ze schodu, by přidala rychlost a postavu vystřelila [(9:45)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=585s). Obecný drive constraint jde použít taky, ale vlastní constraint má parametry šité na pohyb, takže designér neladí tlumení. Navíc odděluje pohyb od jednosměrného držení nad zemí [(10:32)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=632s).

**Jiný průběh kroku.** Obyčejný Mover vezme vstup, simulace spočítá cíl a stav se nastaví postavě přímo, případně v několika podkrocích. Chaos Mover cíl předá constraintu, ten se vyřeší ve fyzice a stav se teprve přečte zpátky. Může tedy vyjít jinak, než byl cíl [(12:05)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=725s), [(12:51)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=771s).

**Cena: asynchronní fyzika a latence.**
- Multiplayer potřebuje fyziku s pevným krokem. V Project Settings se proto zapne Async Physics a nastaví jeho krok. Fyzika pak tiká pevně na vlastním vlákně, zatímco hra tiká proměnlivě [(13:38)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=818s), [(14:24)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=864s).
- Herní vlákno na výsledek fyziky nečeká a interpoluje mezi posledními dvěma kroky, takže je vždy trochu pozadu, nanejvýš o dva kroky asynchronní fyziky [(15:10)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=910s), [(15:57)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=957s).
- Chaos Mover tiká na fyzikálním vlákně, a proto nesmí sahat na data herního vlákna. Co potřebuje, se musí předem posbírat a poslat k němu [(16:44)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=1004s).
- Výsledkem je mírná latence vstupu: fyzikální postava vyskočí o kousek později než kinematická [(17:35)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=1055s), [(18:23)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=1103s). Většině her to nevadí a schovat se to dá animací předzvěsti. U velmi rychlých her, které potřebují minimální latenci, to problém být může a tým na řešení pracuje [(19:09)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=1149s).

> **Pozn.:** Tohle je naplnění „druhé síťové větve" z [přednášky o Moveru z roku 2024](#proc-mover-existuje-modularita-vstupy-a-dve-sitove-vetve), kde se fyzikální postava teprve ukazovala. Vzor „táhni k cíli omezenou silou" zná knihovna z [Physics Control](lana-kabely.md#physics-control-vor-ktery-se-houpe-pod-nohama), kde pružina drží vor u cíle. Rozdíl je v tom, kdo cíl určuje: tam level, tady pohybový mód. A pro srovnání: [ragdoll v GASP](ragdoll.md#ragdoll-ktery-se-chrani-pozy-z-animace-sila-z-krivek-a-cas-do-dopadu) jde opačnou cestou. Kapsle zůstává kinematická a jen dojíždí za pánví fyzikálního těla.

**Souvislosti:** [Rejstřík: Chaos Mover](../rejstrik.md#chaos-mover) · [Rejstřík: Async Physics](../rejstrik.md#async-physics) · [Rejstřík: Mover](../rejstrik.md#mover) · [Co je v herním vlákně a co v renderovacím](profiling.md#co-je-v-hernim-vlakne-a-co-v-renderovacim)

---

## Síťová fyzika zevnitř: snímky místo času, resimulace a input decay

**Zdroj:** [A Dive Into Networked Physics-Based Character Movement | Unreal Fest Stockholm 2025](https://www.youtube.com/watch?v=_jRLlTDqoGI) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~41 min, přednáška (fyzikální tým Epicu, síťová část)

**Shrnutí:** Aby fyzika fungovala v multiplayeru, musí klient i server simulovat ve stejných snímcích se stejnými vstupy. Pevný krok fyziky dovolí počítat v číslech snímků místo času. Klient zná posun mezi svým a serverovým snímkem, a tak může vlastní postavu i server držet v jedné časové ose. Kopie cizích postav dostávají vstupy pozdě a srovnají se resimulací: návrat do minulosti, oprava a přehrání až do současnosti s predikovanými vstupy. Háček: predikované vstupy po zastavení přestřelí a postava pak couvá. Zmírní to input decay, tedy vstup tím slabší, čím hlouběji je v predikci. A gameplay logika, která sahá na fyziku, musí běžet na fyzikálním vlákně, jinak ji síť přepíše.

### Rozpad myšlenky

**Skoro deterministicky.** Stejný vstup na klientovi a na serveru má dát zhruba stejný výsledek. Když se simulace rozcházejí, klient dostává časté korekce a pohyb se trhá [(12:51)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=771s). Přesný determinismus není podmínkou, ale čím blíž mu simulace je, tím méně korekcí přijde. Fyzika je deterministická jen s pevným krokem, proto je potřeba asynchronní fyzika [(13:38)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=818s).

**Snímky místo času.** Pevný krok dovolí místo času používat čísla snímků [(21:34)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=1294s). Klient po připojení serveru napíše, že je na snímku 20, a server odpoví, že v tu chvíli byl na snímku 100. Posun je tedy 80 [(22:21)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=1341s). Klient pak umí převést svůj snímek na serverový: player controller ho vrací přes `Get Network Physics Tick Offset` a na serveru je vždy nulový [(23:07)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=1387s). Posun se drží stálý. Když se změní síťové podmínky, server klienta požádá o opětovné srovnání a klient nepatrně zrychlí nebo zpomalí simulaci, třeba o jeden snímek za příštích sto, což není vidět [(23:53)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=1433s).

**Tři časové osy.** Vlastní postava hráče (autonomous proxy) běží s predikcí napřed, server ve své ose a kopie postavy u ostatních klientů (simulated proxy) v interpolované ose za nimi [(24:40)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=1480s). Míč hozený mezi ně by každou z kopií trefil jinde, nebo některou minul [(26:15)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=1575s). Odpovídající si snímky srovnají vlastní postavu se serverem, kopie cizích postav ale zůstává pozadu [(27:03)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=1623s).

**Resimulace.** Rewind do minulosti, nastavení fyziky do tehdejšího stavu, oprava podle dat ze serveru a přehrání až do současného snímku [(27:03)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=1623s). U vstupů to vypadá takto. Hráč má vstup 12, server dostal teprve 9 a kopie u druhého klienta 6. Kopie vstup 6 aplikuje na snímku 12, tedy špatně [(27:50)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=1670s). Až z toho vznikne desync, vrátí se, aplikuje vstup 6 na snímek 6 a přehraje simulaci do predikované přítomnosti, se vstupy odhadnutými z těch, které už má [(28:36)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=1716s). Pak jsou všechny tři osy srovnané a míč se odrazí správně od všech [(29:22)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=1762s).

**Input decay.** Predikce předpokládá, že hráč drží vstup dál. Když zastaví, kopie popojela příliš daleko a po resimulaci musí couvnout, což vypadá špatně [(30:12)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=1812s). Pomůže vstup tlumit, a to tím víc, čím hlouběji v predikci resimulace je [(30:54)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=1854s). Křivka útlumu je v data assetu Network Physics Settings a ve výchozím stavu má tři body. Na vstupu postavy je funkce, kterou resimulace volá s hodnotou křivky. Útlum o 20 % je prostě vynásobení pohybového vstupu 0,8 [(31:41)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=1901s). Vyladěné to vypadá podstatně líp [(32:27)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=1947s).

**Logika na fyzikálním vlákně.** Všechno, co ovlivňuje fyziku, musí běžet stejně na klientovi i na serveru a přežít resimulaci, a tedy běžet na fyzikálním vlákně [(32:44)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=1964s). Ukázkou je kinematická plošina v callback objektu, který tiká s fyzikou. Vezme aktuální snímek plus posun, tedy serverový snímek, a začne se hýbat, když je větší nebo roven startovnímu snímku. Na serveru je posun nulový, takže výsledek je na obou stranách stejný [(33:31)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=2011s), [(34:17)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=2057s). Protože se callback volá i během resimulace, chová se správně i tam. Startovní snímek a polohy je ale potřeba replikovat zvlášť [(35:03)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=2103s).

**Rozhodnutí na herním vlákně.** Když se o zásahu rozhoduje v herní logice, pomůžou plánované fyzikální příkazy. Herní vlákno naplánuje funkci na konkrétní serverový snímek a fyzikální vlákno ji v tom snímku spustí. Uloží se i do historie pro rewind, takže se při resimulaci přehraje znovu. Snímek a sílu je opět potřeba replikovat [(36:28)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=2188s), [(37:14)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=2234s). Bez toho krumpáč, který na herním vlákně přidá předmětu sílu, prohraje se síťovou korekcí a pohyb se trhá [(38:00)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=2280s). S plánovaným příkazem je plynulý [(38:39)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=2319s).

**Co chybí.** Na řadě jsou optimalizace procesoru, paměti a přenosu, replikační LOD, který kombinuje resimulaci s levnější predictive interpolation, a jednorázové události vedle proudu vstupů a stavů [(38:39)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=2319s), [(40:12)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=2412s). Na Epic Developer Community je tutoriál, který celý postup ukazuje na kouli ovládané vstupy [(40:12)](https://www.youtube.com/watch?v=_jRLlTDqoGI&t=2412s).

> **Pozn.:** [Přednáška o Moveru z roku 2024](#proc-mover-existuje-modularita-vstupy-a-dve-sitove-vetve) slibovala, že fyzikální větev nemusí korigovat rewindem a chyba se může postupně „erodovat". O rok později je pro postavy hlavním režimem právě resimulace a levnější [predictive interpolation](destrukce-a-latky.md#rozbiti-v-multiplayeru-predictive-interpolation-misto-predikce) má připadnout vzdáleným objektům. Že síťová fyzika umí potrápit i Epic, ukazuje [ragdoll v GASP](ragdoll.md#ragdoll-ktery-se-chrani-pozy-z-animace-sila-z-krivek-a-cas-do-dopadu): replikovaný se do projektu nedostal, protože korekce kapsle teleportovaly fyziku těla. Multiplayer je v knihovně dlouhodobě slabé místo a tohle je zatím nejhlubší zdroj k němu.

**Souvislosti:** [Rejstřík: Resimulation](../rejstrik.md#resimulation) · [Rejstřík: Input decay](../rejstrik.md#input-decay) · [Rejstřík: Network Prediction](../rejstrik.md#network-prediction) · [Chaos Visual Debugger: klient vedle serveru](debugging.md#chaos-visual-debugger-zevnitr-faze-solveru-kontakty-a-klient-vedle-serveru)
