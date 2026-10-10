# Jak se učit kódovat: složitost, tutoriály a ego

Čtyři videa o nejčastějších zásecích samouků: pocit, že „programování je moc složité" (není — složité je to, co po počítači chceš); nekonečná smyčka tutoriálů (výstupem je pocit pokroku, ne dovednost); ego, které chce vědět místo řešit; a nakonec otázka, co vlastně dělá kód *tvým*. Kapitola navazuje na [Kolik kódu na start](co-se-ucit.md) — tam bylo *co* se učit, tady *jak*.

---

## Složitá není řeč, ale to, co po počítači chceš

**Zdroj:** [Why You Struggle to Learn Game Coding](https://www.youtube.com/watch?v=SU8d0c9aAQo) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · ~15 min, pep talk s reality checkem

**Shrnutí:** Lidé přicházejí ke kódu s domněnkou, že složitý je jazyk. Obrat, který video nabízí po stovkách odučených studentů: **jazyk je jednoduchý — složité je zadání, které počítači dáváš, a ty mu často sám nerozumíš** [(2:23)](https://www.youtube.com/watch?v=SU8d0c9aAQo&t=143s). Počítač dělá přesně to, co řekneš; bug je tvůj pokyn, ne jeho rozmar.

### Rozpad myšlenky

Demonstrace na visual novelu [(3:59)](https://www.youtube.com/watch?v=SU8d0c9aAQo&t=239s): „zobraz postavu, textové okno, text co naskakuje po znacích, přehraj zvuk" zní jako čtyři kroky — a při rozepsání je to ke třiceti pod-úkolům (sprite v enginu, pozice, scale, souřadnice rohů okna, string, časování znaků, rozlišení „celý text" vs. „text doteď"…). Specializovaný nástroj jako Ren'Py většinu těch kroků udělá za tebe — **proto** je skok z Ren'Py do obecného enginu tak bolestivý: nezvedla se složitost jazyka, ale počet věcí, které najednou řešíš ty [(7:51)](https://www.youtube.com/watch?v=SU8d0c9aAQo&t=471s). Přidej větvící se dialog a jsi ve správě dat — seznamy, indexy od nuly a jejich mstivé drobnosti [(8:37)](https://www.youtube.com/watch?v=SU8d0c9aAQo&t=517s).

Z toho plyne definice řemesla: **programování = promyslet, co přesně chceš, rozbít to na nejmenší kousky — a ke každému si otevřít manuál** [(9:24)](https://www.youtube.com/watch?v=SU8d0c9aAQo&t=564s). Zkušení programátoři nikdy nepřestanou věci vyhledávat; mění se jen, *co* vyhledávají [(10:11)](https://www.youtube.com/watch?v=SU8d0c9aAQo&t=611s). Frustrace začátečníka je z velké části špatná kalibrace: srovnáváš svůj první krok s cizí internalizovanou rutinou.

Nejlepší metafora videa: francouzská konverzační příručka [(11:45)](https://www.youtube.com/watch?v=SU8d0c9aAQo&t=705s). Turista se ptá, kde je radnice — začátečník v enginu ale chce rovnou „iluzi světa": postavu, fyziku, sociální interakce. To je jako chtít v prvním měsíci francouzštiny psát poezii. **Realistické očekávání prvního měsíce: pár věcí, které se hýbou po obrazovce** [(12:32)](https://www.youtube.com/watch?v=SU8d0c9aAQo&t=752s). A dvě hygienické poznámky: „zkoušel jsem to" začíná u 4–8 hodin v kuse, ne u dvaceti minut [(0:49)](https://www.youtube.com/watch?v=SU8d0c9aAQo&t=49s); a rady „uč se to natvrdo od nuly" dávají hlavně programátoři, ne designéři — když tě obecný engine odrazuje, specializovaný nástroj je legitimní volba [(13:19)](https://www.youtube.com/watch?v=SU8d0c9aAQo&t=799s).

> **Pozn.:** Tohle je praktická strana [rozkladu problému](co-se-ucit.md#skutecna-dovednost-je-rozklad-problemu-ne-syntax) — tam teze, tady třicetikrokový důkaz. A vysvětluje, proč Blueprint „nody nejsou o nic snazší než kód", když nevíš, co stavíš: vizuální syntax nezmenší zadání.

**Souvislosti:** [Kolik kódu na start](co-se-ucit.md) · [Programátorské myšlení](programatorske-mysleni.md) · [Rady z praxe: rady nefungují tam, kde začíná design](rady-z-praxe.md)

---

## Aktivní sledování: tutoriál je odrazový můstek, ne recept

**Zdroj:** [How to Actually LEARN from YouTube Tutorials!](https://www.youtube.com/watch?v=APwQFdaH0eY) · [Brainless.](https://www.youtube.com/channel/UCJmAuKzz_VHa3Yb7v19KIvQ) · ~9 min, návod proti smyčce

**Shrnutí:** Nekonečná smyčka tutoriálů má známou anatomii: noční „learning fever", ráno watch-later očistec (autorových 36 videí [(0:01)](https://www.youtube.com/watch?v=APwQFdaH0eY&t=1s)) a pocit pokroku bez pokroku. Protilék má tři části: žádný backlog, **aktivní sledování** (dělej to, co video učí, během sledování) a vědomý přechod k samostatnosti — nejtěžší část každého učení [(4:41)](https://www.youtube.com/watch?v=APwQFdaH0eY&t=281s).

### Rozpad myšlenky

**Backlog ne** [(1:34)](https://www.youtube.com/watch?v=APwQFdaH0eY&t=94s): fronta tutoriálů je pojistka pro situaci „nemám co dělat", která při učení nenastává. Hledej přesně to, co potřebuješ *teď*, a sleduj hned — tutoriál na „víc imerze" je k ničemu, dokud hra nefunguje.

**Aktivní sledování** [(2:20)](https://www.youtube.com/watch?v=APwQFdaH0eY&t=140s): kód z videa piš vlastníma rukama, žádné kopírování z popisku. Deset zhlédnutých tutoriálů denně je snadných; učení se děje jen při přímé interakci. Nejčastější past: nerozumět půlce vlastního kódu — ať už z memorování, copy-paste nebo protože ho napsala AI. „Lepší je messy kód, který jsi napsal, než optimální kód, který neumíš upravit" [(3:07)](https://www.youtube.com/watch?v=APwQFdaH0eY&t=187s). Autorův pracovní setup: engine + tutoriál + **dokumentace** + AI výhradně na vysvětlování a připomenutí syntaxe — „nikdy nenech AI kódovat přímo za tebe: nenaučíš se nic, a až se to rozbije, neopravíš to. AI je nástroj efektivity, ne černá skříňka" [(3:54)](https://www.youtube.com/watch?v=APwQFdaH0eY&t=234s).

**Přechod k samostatnosti** [(4:41)](https://www.youtube.com/watch?v=APwQFdaH0eY&t=281s): školní mindset (memoruj, odevzdej, zapomeň; strach ze selhání kvůli známkám) je přesný opak toho, co učení řemesla potřebuje — děti se učí efektivně mimo jiné proto, že se **nerozhodnou skončit** a selhání neřeší [(0:47)](https://www.youtube.com/watch?v=APwQFdaH0eY&t=47s). Prakticky pomáhá expoziční terapie a jeden konkrétní krok, který video samo předvádí: po dokončení tutoriálu na dungeon generátor autor **mění algoritmus** (obrací logiku vyřezávání) [(6:13)](https://www.youtube.com/watch?v=APwQFdaH0eY&t=373s) — tutoriál jako odrazový můstek k vlastní úpravě, ne recept k reprodukci. A klíč z celé smyčky ven: k engine tutoriálům přibrat základy kódu samotného [(7:47)](https://www.youtube.com/watch?v=APwQFdaH0eY&t=467s).

> **Pozn.:** „Uprav tutoriál, než ho opustíš" je nejlevnější test porozumění, jaký existuje — v duchu [kvízového protokolu](../zapisky/kvizovy-protokol.md): malý náraz intuice na realitu. Tutorial hell už má v knihovně [vlastní heslo](../praxe/editor-tipy.md#jak-se-ucit-engine-rady-po-peti-letech); tahle myšlenka je jeho únikový plán.

**Souvislosti:** [Tipy do editoru: jak se učit engine](../praxe/editor-tipy.md#jak-se-ucit-engine-rady-po-peti-letech) · [Učení v éře AI](uceni-v-ere-ai.md) · [Rejstřík: Tutorial hell](../rejstrik.md#tutorial-hell) · [Jak se učit z GASP](../praxe/gasp.md#posledni-update-pro-ue5-sample-ne-framework) *(tytéž rady od tvůrců Epic sample projektu)*

---

## Řešitelé, ne vědoucí: jeden uživatel, jeden stack, jedna smyčka

**Zdroj:** [Coding is Hard Until You Learn This](https://www.youtube.com/watch?v=gaCY4QxfSzA) · [Phillip Choi](https://www.youtube.com/channel/UCadUgezGZkA5IknHj2C89yg) · ~19 min, tvrdá diagnóza + plán

**Shrnutí:** „Nejsi špatný v kódování — jsi špatný ve způsobu, jak se ho učíš" [(0:02)](https://www.youtube.com/watch?v=gaCY4QxfSzA&t=2s). Diagnóza: obsluhuješ špatného zákazníka — vlastní ego, které chce pohodlí a pocit chytrosti, a tak konzumuje obsah místo stavění [(0:50)](https://www.youtube.com/watch?v=gaCY4QxfSzA&t=50s). „Tech neodměňuje vědoucí, odměňuje řešitele: nikdo neplatí za ‚vím, co je for loop', platí za ‚oprav to do pátku'" [(1:37)](https://www.youtube.com/watch?v=gaCY4QxfSzA&t=97s).

### Rozpad myšlenky

**Pasti fake progressu:** šest stacků v plánu devátý den učení [(1:37)](https://www.youtube.com/watch?v=gaCY4QxfSzA&t=97s); kopírování univerzitního kurikula (binary search trees před prvním login formem — „škola je hra na známky, průmysl na shipping" [(3:11)](https://www.youtube.com/watch?v=gaCY4QxfSzA&t=191s)); a AI verze téže pasti: nechat si vygenerovat dashboard a cítit se nezastavitelně — „dočasně babysitting codebase, které nerozumíš; závislost s rtěnkou" [(2:24)](https://www.youtube.com/watch?v=gaCY4QxfSzA&t=144s). Nejtišší past je psychologická [(7:04)](https://www.youtube.com/watch?v=gaCY4QxfSzA&t=424s): každé „tento týden se naučím React", po kterém nic nepostavíš, učí mozek, že sliby sobě nedržíš — a tohle poškození identity se úročí.

**Plán** [(10:11)](https://www.youtube.com/watch?v=gaCY4QxfSzA&t=611s): (1) **vyber si zákazníka** — jednoho člověka s jednou bolestí („učím se kódovat" není problém; „sestra zapomíná léky při směnném provozu" je [(14:03)](https://www.youtube.com/watch?v=gaCY4QxfSzA&t=843s)); kdo si dnes řešení lepí z tabulek, nosí urgenci v kapse. (2) **Jeden stack, 60–90 dní, žádné přebíhání** — „generalisté bez odježděných opakování jsou neviditelní" [(10:57)](https://www.youtube.com/watch?v=gaCY4QxfSzA&t=657s). (3) **MVP = jen core loop**: přihlásit → udělat věc → vidět hodnotu; „dark mode je dezert a ty jsi ještě nejedl protein" [(11:44)](https://www.youtube.com/watch?v=gaCY4QxfSzA&t=704s). (4) **Stav veřejně a rychle** — ošklivé screenshoty, „login konečně funguje, chce se mi brečet"; poptávka a testeři si tě najdou [(12:31)](https://www.youtube.com/watch?v=gaCY4QxfSzA&t=751s).

K tomu tři tvrdé pravdy: budeš **škrtat features** („to teď neshipujeme" je kódová verze odmítání špatných klientů); budeš **couvat** (smazat dva týdny práce a postavit to správně bolí — a přesně tak vypadá růst [(13:17)](https://www.youtube.com/watch?v=gaCY4QxfSzA&t=797s)); a přijde **rána identitě**: z „znám buzzwordy" do „proč mi expiruje token" — to není ztráta statusu, to je začátek stavění [(13:17)](https://www.youtube.com/watch?v=gaCY4QxfSzA&t=797s). Odměna na konci smyčky: po první end-to-end věci se AI mění z šéfa na asistenta — „napiš mi helper na X, zapojím si ho" [(14:03)](https://www.youtube.com/watch?v=gaCY4QxfSzA&t=843s). A metrika úspěchu je jedna věta od cizího člověka: **„Hele, můžu to zkusit?"** [(17:09)](https://www.youtube.com/watch?v=gaCY4QxfSzA&t=1029s).

> **Pozn.:** Kontext je web dev a autor v závěru promuje vlastní mentoring — ale mechanika sedí na gamedev beze změny: jeden hráč s jednou bolestí = [nápad validovaný brzy](rady-z-praxe.md#pracuj-zpatky-jak-brzy-jde-poznat-ze-by-hru-nekdo-koupil), core loop first = [vertical slice myšlení](prototypovani.md), „rule of 100" (100 minut denně, 100 řádků denně, 100 oslovení měsíčně [(14:49)](https://www.youtube.com/watch?v=gaCY4QxfSzA&t=889s)) je disciplinární rámec z [motivace vs. disciplíny](produktivita.md#motivace-startuje-disciplina-dokoncuje). „Waiting is the new quitting" [(18:43)](https://www.youtube.com/watch?v=gaCY4QxfSzA&t=1123s).

**Souvislosti:** [Produktivita](produktivita.md) · [Učení v éře AI: čtyři úrovně inženýra](uceni-v-ere-ai.md#ctyri-urovne-inzenyra-nahrazuje-se-output-ne-usudek) · [Prototypování](prototypovani.md) · [Rejstřík: MVP](../rejstrik.md#mvp) · [Rejstřík: Core loop](../rejstrik.md#core-loop)

---

## Rozbij to schválně: kdy je kód konečně tvůj

**Zdroj:** [Nobody Tells Beginners These 7 Coding Tips | learn to code in Godot](https://www.youtube.com/watch?v=N7UgrLFzW08) · [DeeRaghooGames](https://www.youtube.com/channel/UC-KLgU0nzoCCEU6W16CS3vQ) · ~16 min, esej

**Shrnutí:** Autor po pěti letech v Godotu formuluje test vlastnictví, který se dá použít okamžitě: **nedokážeš-li svůj kód vysvětlit, ještě není tvůj.** Cesta k vysvětlitelnosti přitom nevede přes větší soustředění, ale přes **záměrné rozbíjení** — změň číslo, smaž řádek, přesuň funkci a dívej se, co se stane. Háček je, že to jde proti všemu, co nás naučila škola: rozbít věc je tam chyba, tady je to jediný levný zdroj zpětné vazby.

### Rozpad myšlenky

**Odkud ta potřeba plyne.** Video otevírá diagnózou, kterou zná každý samouk [(0:01)](https://www.youtube.com/watch?v=N7UgrLFzW08&t=1s): tutoriál běží, všechno funguje, člověk má pocit, že to konečně pochopil — a druhý den u prázdného projektu si nepamatuje nic. Autor tvrdí, že chyba je v cíli: **nesnaž se pamatovat, snaž se rozumět.** A dokládá to pozorováním, které začátečníkům chybí [(0:48)](https://www.youtube.com/watch?v=N7UgrLFzW08&t=48s): *profesionálové nemají nic nabiflované; jedna z nejčastějších věcí, kterou u zkušených vývojářů uvidíš, je vyhledávání.* To je totéž zjištění jako u [Složitá není řeč](#slozita-neni-rec-ale-to-co-po-pocitaci-chces), jen z druhé strany — tam „vyhledávat nikdy nepřestaneš", tady „a proto memorování není cíl".

**Mechanismus: experiment místo poslušnosti** [(6:59)](https://www.youtube.com/watch?v=N7UgrLFzW08&t=419s). Místo krok-za-krokem podle videa se autor začal ptát *„co se stane, když tohle změním?"* — zdvojnásobím hodnotu, přesunu funkci jinam, smažu kus logiky. Přiznává, že to bylo zpočátku nepříjemné, *protože nás učili, že rozbíjet věci je špatně*. Jenže **každé rozbití je zpětná vazba**: teprve když něco přestane fungovat, uvidíš, co ten řádek doopravdy dělal. Konkrétní repertoár je krátký [(7:45)](https://www.youtube.com/watch?v=N7UgrLFzW08&t=465s): přidej `print` a podívej se, co se děje pod povrchem · změň čísla a sleduj efekt · odeber kus logiky a zjisti, co se rozpadne. Cíl je posun od hádání k **předvídání**.

**Test vlastnictví** je to, co z toho dělá použitelné pravidlo [(8:31)](https://www.youtube.com/watch?v=N7UgrLFzW08&t=511s). Autor popisuje vlastní zkušenost bez příkras: opisoval skripty na pohyb, skákání, signály — a hra fungovala, *ale kdyby se mě někdo zeptal, proč tenhle řádek existuje, neuměl bych to vysvětlit.* Odtud věta, kterou stojí za to si zapamatovat: **„když neumíš vysvětlit svůj kód, ještě ti nepatří."** Recept není nekopírovat; recept je **kopírovat a pak si ten kód přivlastnit** [(9:17)](https://www.youtube.com/watch?v=N7UgrLFzW08&t=557s) — spustit ho, projít řádek po řádku a u každého se ptát „co dělá tenhle? byl tu potřeba? co se stane, když ho smažu?". Tím se z tutoriálu stane **reference místo berličky**.

**Zmenšuj problém, dokud nezmizí zásek** [(5:24)](https://www.youtube.com/watch?v=N7UgrLFzW08&t=324s). Druhá polovina eseje míří na rozklad: začátečník se dívá na celý projekt místo na další krok, a „udělám plošinovku" se v hlavě rozpadne na pohyb, skákání, nepřátele, mince, levely, menu, zvuky a ukládání *ještě než napíše první řádek*. Autorova diagnóza je použitelná jako nástroj: **cítíš-li se zaseknutý, je problém, který zrovna řešíš, pořád ještě moc velký — zmenšuj ho dál** [(6:11)](https://www.youtube.com/watch?v=N7UgrLFzW08&t=371s). Ne „potřebuju plošinovku", ale „potřebuju plošinu, na které se dá stát".

**A konzistence místo intenzity** [(10:10)](https://www.youtube.com/watch?v=N7UgrLFzW08&t=610s): typický vzorec je nával motivace, prodřený víkend, pak týden pauza a pocit, že člověk všechno zapomněl. Autor staví proti tomu **20 minut denně** a přirovnání k nástroji — *na kytaru se nenaučíš hrát tím, že si ji jednou měsíčně vezmeš na osm hodin*. Praktická formulace na konec: neptej se „kolik toho dnes zmáknu?", ale **„jak se dnes můžu aspoň trochu ukázat?"**

> **Pozn.:** Video obsahuje **sponzorovaný bonusový díl o AI nástroji** — a co je zajímavé, sponzor v něm dostane překvapivě přísné podmínky [(12:01)](https://www.youtube.com/watch?v=N7UgrLFzW08&t=721s): autor AI vědomě vyřadil z hlavní sedmičky s odůvodněním, že *bez postavených základů se z ní stane zkratka, která nahradí učení*, a pořadí je „nejdřív zkus sám, pak se chvíli trap, teprve pak se ptej AI — abys rozuměl, ne aby ses vyhnul". Sedí to na [čtyři úrovně inženýra](uceni-v-ere-ai.md#ctyri-urovne-inzenyra-nahrazuje-se-output-ne-usudek) i na Brainlessovo „AI je nástroj efektivity, ne černá skříňka". Naší jedinou výhradou je, že rada zůstává u dobré vůle: **žádný mechanismus, který by odlišil „ptám se, abych rozuměl" od „ptám se, abych to měl hotové", tu není** — a přesně kvůli tomu je test „umíš to vysvětlit?" cennější než jakékoli pravidlo o tom, kdy se ptát.

**Souvislosti:** [Aktivní sledování](#aktivni-sledovani-tutorial-je-odrazovy-mustek-ne-recept) *(uprav tutoriál, než ho opustíš — tatáž mechanika)* · [Skutečná dovednost je rozklad problému](co-se-ucit.md#skutecna-dovednost-je-rozklad-problemu-ne-syntax) · [Učení v éře AI: vlastnictví znalosti](uceni-v-ere-ai.md#vlastnictvi-znalosti-odpoved-nestaci) *(týž test, tvrději formulovaný)* · [Godot: co si přinést, než otevřeš editor](../godot/zaklady.md#co-si-prinest-nez-otevres-editor) *(týž autor o prvních návycích v enginu)* · [Rejstřík: Tutorial hell](../rejstrik.md#tutorial-hell) · [Rejstřík: Retrieval practice](../rejstrik.md#retrieval-practice)

---

## Rychlostní daň, pit crew a „přestaň být student"

**Zdroj:** [How I Beat 99% of Computer Science Students (Georgia Tech Lessons)](https://www.youtube.com/watch?v=oJ6LN7t0Vr8) · [Sajjaad Khader](https://www.youtube.com/channel/UC7zZ2-Q_oxbUaoMVL0z51wg) · ~12 min, zkušenost · + [How to Learn Coding FAST And Make Cool Stuff](https://www.youtube.com/watch?v=nCZbZyyuHRg) · [Eray Sona](https://www.youtube.com/channel/UCZJiDye9aqg68BfMNbFS5jw) · ~4 min

**Shrnutí:** Dvě videa o učení, která spolu nesouvisejí a dohromady dávají jednu použitelnou věc: **rozdíl mezi být dobrý student a být dobrý inženýr.** První to formuluje na čtyřech univerzitních tradicích (a je to nezvykle funkční rámec), druhé dodává, kde se ten posun odehrává v praxi. Háček, který stojí za pozornost: **oba nezávisle říkají, že učení tutoriály je past, a oba nabízejí jinou cestu ven.**

### Rozpad myšlenky

**Rychlostní daň** [(0:47)](https://www.youtube.com/watch?v=oJ6LN7t0Vr8&t=47s) je jeho výklad kampusové píšťaly, která každou hodinu oznamuje konec bloku: *„čas není jen něco, co spravuješ — je to něco, za co ti můžou naúčtovat."* Zjistil to hned v prvním týdnu: sotva se nastěhoval, a v budově informatiky už firmy nabíraly stážisty **na příští léto** a starší studenti stáli ve frontě. Jeho zobecnění: *„mimo univerzitu je ta daň za čekání ještě větší, zvlášť v éře AI. Ta píšťala zní každý den."*

**Pit crew** [(2:19)](https://www.youtube.com/watch?v=oJ6LN7t0Vr8&t=139s) je nejlepší obrázek z obou videí. Vychází ze studentského závodu na tříkolkách, kde má tým sedm lidí — čtyři jezdce a **tři v servisní jámě**, kteří mění kolo. *„Nerozhoduje jen to, kdo šlape nejrychleji. Rozhodují předávky, výměna kola, komunikace."* Aplikace na code review je přesná a řeší běžnou emoci: první revize mu vrátily desítky komentářů a *„seděl jsem tam a říkal si — umím vůbec kódovat?"* Přerámování: **recenzenti nejsou kritici, jsou tvůj servisní tým** — nejsou tam, aby tě zahanbili, ale aby zachytili uvolněné kolo, než se to celé rozsype. A druhá půlka, kterou vyvodí sám: **staň se pit crew pro ostatní**. Začal poctivě recenzovat i seniorům; drobnosti se sčítají a *„firmy si toho všímají"*.

**Přestaň být student** [(6:59)](https://www.youtube.com/watch?v=oJ6LN7t0Vr8&t=419s) je jádro celého videa a vychází z řádku školní hymny: *„nestojí tam ‚jsem skvělý student' ani ‚jsem skvělý na testy'. Stojí tam ‚jsem sakra dobrý inženýr'."* Přiznává, že přišel plně v režimu studenta — chtěl samé jedničky, protože ho k tomu dvanáct let školy vytrénovalo. *„Skvělý student si dokáže systém zapamatovat. Skvělý inženýr musí uvnitř toho systému stavět. To jsou dvě úplně různé dovednosti a jen jedna z nich pomáhá ve skutečném světě."* Co ho z toho vytáhlo, byla **volba zaměření** — a projekty z ní (herní AI, predikční model) *„se staly tím, o čem jsem mluvil na pohovorech, a doslova mi pomohly získat práci."*

**A odkud začít, když ještě nic neumíš** [(1:34)](https://www.youtube.com/watch?v=nCZbZyyuHRg&t=94s). Druhý autor to říká přímočaře: *„v okamžiku, kdy se naučíš nový koncept, zastav tutoriál a začni projekt."* Naučil ses cyklus? Napiš program, který vypíše hloupý příběh. Naučil ses seznamy? Udělej seznam úkolů. Pak druhý krok: **postav to nejambicióznější, co tvoje malá sada dovedností unese** — *„rychle zjistíš, že vůbec netušíš, co děláš. A to je ta pointa."* Jeho vlastní zkušenost: mobilní hra, u které musel googlit všechno od grafiky po detekci kolizí, ho naučila víc za měsíc než rok tutoriálů. A k AI má jasné pravidlo: **použij ji jako doučujícího, ne jako berlu** — *„kopírovat bez učení je jako podvádět u testu, který stejně později neuděláš."*

**A poslední rámec, který stojí za zmínku** [(10:06)](https://www.youtube.com/watch?v=oJ6LN7t0Vr8&t=606s): **konstruktivní chaos.** Vezmi něco rušivého a udělej z toho něco užitečného. U AI to znamená rozdíl mezi *„nech si dopsat úkol"* (*„to je verze AI, která tě dělá slabším"*) a stavěním věcí, které bez ní nešly.

> **Pozn.:** Nejužitečnější je tady **pit crew**, protože řeší emoci, o které se v návodech nepíše: **první seriózní code review bolí** a bolí přesně u lidí, kteří to myslí vážně. Přerámování z „kritiky" na „servisní tým" není utěšování — je věcné, protože recenzent má stejný cíl jako ty. A druhá půlka (staň se pit crew pro ostatní) je návod, jak z toho udělat něco, co ti pomůže: **recenzovat cizí kód je nejlevnější způsob, jak číst hodně kódu**. Souvisí to přímo s [řešiteli, ne vědoucími](#resitele-ne-vedouci-jeden-uzivatel-jeden-stack-jedna-smycka) i s [rozbij to schválně](#rozbij-to-schvalne-kdy-je-kod-konecne-tvuj). Vlastní výhrada k oběma zdrojům: **jsou to úspěšné příběhy vyprávěné zpětně** (a jeden z nich má v titulku „porazil jsem 99 % studentů", což je marketingový rám, ne měření). Rámce, které nabízejí, jsou dobré; kauzalita „udělal jsem tohle, proto mám 250 tisíc dolarů ročně" je slabá. Ber to jako **sadu použitelných obrázků**, ne jako recept.

**Souvislosti:** [Aktivní sledování: tutoriál je odrazový můstek](#aktivni-sledovani-tutorial-je-odrazovy-mustek-ne-recept) · [Řešitelé, ne vědoucí](#resitele-ne-vedouci-jeden-uzivatel-jeden-stack-jedna-smycka) · [Rozbij to schválně](#rozbij-to-schvalne-kdy-je-kod-konecne-tvuj) · [Učení v éře AI](uceni-v-ere-ai.md#novy-programovaci-jazyk-se-jmenuje-srozumitelnost) · [Rejstřík: Dogfooding](../rejstrik.md#dogfooding) · [Rejstřík: Retrieval practice](../rejstrik.md#retrieval-practice)
