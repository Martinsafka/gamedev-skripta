# Programátorské myšlení: common sense éry AI

Visual Kernel ve dvouhodinovém kurzu *Programming Thinking* neučí Python — učí **myslet jako program**: co doopravdy dělá rovnítko, proč akumulátor patří ven ze smyčky, kdy se kopíruje hodnota a kdy putuje jen odkaz. Teze videa: v éře, kdy kód píše AI, je tohle nový common sense — bez něj vibe coder narazí na strop, s ním z AI vytěžíš násobky. Pro Blueprint vývojáře platí dvojnásob: každý z těch mentálních modelů má v UE přesný protějšek. Kapitolu uzavírají čtyři koncepty „z vyšší ligy" ze Shade of Code.

---

## Vibe coding má strop; myšlení ho nemá

**Zdroj:** [Programming Thinking](https://www.youtube.com/watch?v=KtBefDeECVU) · [Visual Kernel](https://www.youtube.com/channel/UC9Cz481L3CeYm-ZqwqevCPQ) · ~130 min, kurz mentálních modelů

**Shrnutí:** „Nepotřebuješ už psát kód" — souhlas. „Nepotřebuješ programátorské myšlení" — zásadní nesouhlas [(0:02)](https://www.youtube.com/watch?v=KtBefDeECVU&t=2s). Autor to srovnává se školou: matiku a fyziku se neučíš, abys počítal ručně, ale abys **kladl lepší otázky**. Hodnota čistých vibe coderů podle něj časem stagnuje; lidé s programátorským myšlením z AI dostávají násobně víc [(0:48)](https://www.youtube.com/watch?v=KtBefDeECVU&t=48s).

### Rozpad myšlenky

Video své poselství nese i formou: definice programování v něm postupně „levelují" a ten žebřík je sám o sobě učební pomůcka. Programování je tvorba zajímavých věcí → **umění vytváření a měnění proměnných** [(13:58)](https://www.youtube.com/watch?v=KtBefDeECVU&t=838s) → umění měnit proměnné **uprostřed běžící smyčky s podmínkami** [(54:08)](https://www.youtube.com/watch?v=KtBefDeECVU&t=3248s) → a nakonec „programming is mathematics in action" [(1:37:36)](https://www.youtube.com/watch?v=KtBefDeECVU&t=5856s). Každý level odpovídá jednomu mentálnímu modelu z dalších myšlenek téhle kapitoly.

Stojí za pozornost, čím autor ilustruje podmínky a logické operátory: herními situacemi ze Zeldy [(20:55)](https://www.youtube.com/watch?v=KtBefDeECVU&t=1255s) — truhla s rupee (if/elif/else podle barvy), jídlo jde sníst, jen když je jedlé **a zároveň** nemáš plné zdraví (vnořený if [(23:10)](https://www.youtube.com/watch?v=KtBefDeECVU&t=1390s)), střelba vyžaduje luk **a** šíp (AND [(25:30)](https://www.youtube.com/watch?v=KtBefDeECVU&t=1530s)), zima nezraňuje, když máš teplé oblečení **nebo** jsi snědl pálivé jídlo (OR [(27:26)](https://www.youtube.com/watch?v=KtBefDeECVU&t=1646s)). Herní logika *je* výroková logika — kdo skládá Branch nody v Blueprintech, programuje výroky, jen jim tak neříká. Bonusová intuice: AND je sériový obvod (obě brány musí pustit proud), OR paralelní [(28:15)](https://www.youtube.com/watch?v=KtBefDeECVU&t=1695s) — odtud „short-circuit" vyhodnocování.

> **Pozn.:** Pedagogický trik, který stojí za ukradení: autor nejdřív nechá diváka **tipnout** chování šesti kvízů o proměnných a teprve pak ukáže výsledek [(5:29)](https://www.youtube.com/watch?v=KtBefDeECVU&t=329s) — náraz vlastní intuice na realitu drží v paměti víc než výklad. Stejný mechanismus popisuje zápisek [Kvízový protokol](../zapisky/kvizovy-protokol.md).

**Souvislosti:** [Kolik kódu na start](co-se-ucit.md) — stavebnice pěti konstruktů, na kterou tahle kapitola navazuje · [Zápisek: Kvízový protokol](../zapisky/kvizovy-protokol.md) · [AI agenti: Claude Code a MCP](../praxe/claude-code-ue.md)

---

## Rovnítko je sloveso a program teče shora dolů

**Zdroj:** [Programming Thinking](https://www.youtube.com/watch?v=KtBefDeECVU) · [Visual Kernel](https://www.youtube.com/channel/UC9Cz481L3CeYm-ZqwqevCPQ) · stejné video, kapitoly o proměnných a smyčkách

**Shrnutí:** Ze školy máme rovnítko zažité jako popis („1 + 1 = 2"), v programování je to **akce**: „ulož hodnotu do proměnné" [(1:35)](https://www.youtube.com/watch?v=KtBefDeECVU&t=95s). Z téhle drobnosti plyne většina začátečnických překvapení — od `n = n + 1` po nefunkční swap. Druhá polovina modelu: program se vykonává **shora dolů, řádek po řádku**, a smyčka je jen automatizované opakování s proměnnou, která si sama hopsá po prvcích [(44:09)](https://www.youtube.com/watch?v=KtBefDeECVU&t=2649s).

### Rozpad myšlenky

Šest kvízů o proměnných [(6:15)](https://www.youtube.com/watch?v=KtBefDeECVU&t=375s) v kostce: proměnná není datový typ (dnes drží string, zítra číslo [(7:25)](https://www.youtube.com/watch?v=KtBefDeECVU&t=445s)); `B = A` ukládá **hodnotu** A, ne symbol — pozdější změna B se A netkne [(8:12)](https://www.youtube.com/watch?v=KtBefDeECVU&t=492s); `n = n + 1` čte staré n vpravo a ukládá vlevo [(9:46)](https://www.youtube.com/watch?v=KtBefDeECVU&t=586s); použití proměnné před definicí je chyba, protože řádek 3 neví, co přijde na řádku 4 [(11:44)](https://www.youtube.com/watch?v=KtBefDeECVU&t=704s); a prohození dvou proměnných potřebuje třetí — jinak obě skončí se stejnou hodnotou, protože první přiřazení tu původní nenávratně přepíše [(12:25)](https://www.youtube.com/watch?v=KtBefDeECVU&t=745s).

U smyček video buduje **vzory, ne syntax** — tři archetypy, které se vracejí v každém programu [(47:16)](https://www.youtube.com/watch?v=KtBefDeECVU&t=2836s):

1. **Akumulátor**: proměnná založená *před* smyčkou sbírá výsledek (součet, seznam unikátů). Založit ji uvnitř znamená resetovat ji každou otočku — klasický bug [(48:55)](https://www.youtube.com/watch?v=KtBefDeECVU&t=2935s). A u násobení se inicializuje na 1, ne 0, jinak nula všechno spolkne [(1:04:37)](https://www.youtube.com/watch?v=KtBefDeECVU&t=3877s).
2. **Průběžné maximum**: drž nejlepší dosud viděné, přepisuj při zlepšení [(49:46)](https://www.youtube.com/watch?v=KtBefDeECVU&t=2986s).
3. **Modifikace přes index**: měnit prvky pole jde jen přes index; smyčka přes hodnoty mění jen svou lokální proměnnou [(59:04)](https://www.youtube.com/watch?v=KtBefDeECVU&t=3544s).

**Vnořená smyčka** není „dvě proměnné běžící vedle sebe": vnitřní smyčka dokončí *celý* svůj běh na jediný krok vnější — složitost neroste dvojnásobně, ale **kvadraticky** [(1:10:54)](https://www.youtube.com/watch?v=KtBefDeECVU&t=4254s). Hezký herní příklad: balíček karet = vnější smyčka přes hodnoty × vnitřní přes barvy [(1:12:51)](https://www.youtube.com/watch?v=KtBefDeECVU&t=4371s). A když vnitřní smyčka počítá něco per položka vnější (faktoriál každého čísla v seznamu), **reset akumulátoru patří mezi smyčky** — jinak rezidua z minulého běhu přežijí do dalšího [(1:17:21)](https://www.youtube.com/watch?v=KtBefDeECVU&t=4641s).

Do třetice drobnosti s velkým dopadem: **zero indexing** — „první prvek" znamená index 0 a na záměně s jedničkou „padly nespočetné hodiny lidské inteligence" [(33:55)](https://www.youtube.com/watch?v=KtBefDeECVU&t=2035s); a sigma notace z matiky je jen for loop v převleku [(1:08:30)](https://www.youtube.com/watch?v=KtBefDeECVU&t=4110s).

> **Pozn.:** V Blueprintech je tohle všechno vidět doslova: ForEachLoop s akumulátorem v lokální proměnné, Set node = rovnítko-sloveso, execution wire = tok shora dolů. Kdo umí přečíst `n = n + 1`, umí přečíst i graf — a naopak; rozdíl je jen v tom, že graf ten tok kreslí šipkami.

**Souvislosti:** [Kolik kódu na start: rozklad problému](co-se-ucit.md#skutecna-dovednost-je-rozklad-problemu-ne-syntax) · [Rejstřík: Zero indexing](../rejstrik.md#zero-indexing)

---

## Funkce je vstup → výstup; return není print

**Zdroj:** [Programming Thinking](https://www.youtube.com/watch?v=KtBefDeECVU) · [Visual Kernel](https://www.youtube.com/channel/UC9Cz481L3CeYm-ZqwqevCPQ) · stejné video, kapitoly o funkcích a scope

**Shrnutí:** Funkce není statický graf z učebnice — je to **akce transformace vstupu na výstup** [(1:19:19)](https://www.youtube.com/watch?v=KtBefDeECVU&t=4759s). Parametry jsou placeholdery, které se naplní až při volání [(1:23:18)](https://www.youtube.com/watch?v=KtBefDeECVU&t=4998s), `return` je jediná cesta výsledku ven — a zároveň okamžitý konec funkce. Každé volání si otevře vlastní **sandbox** (lokální scope), který po návratu beze stopy zmizí [(1:32:01)](https://www.youtube.com/watch?v=KtBefDeECVU&t=5521s).

### Rozpad myšlenky

Dvě pasti, které video vypichuje. **Print není return** [(1:25:39)](https://www.youtube.com/watch?v=KtBefDeECVU&t=5139s): funkce, která výsledek jen vypíše, vrací „nic" (None) — a kdo s tím „ničím" počítá dál, diví se. Výstup bez returnu „zůstane zaseknutý uvnitř" [(1:22:31)](https://www.youtube.com/watch?v=KtBefDeECVU&t=4951s). **Return okamžitě končí** [(1:27:13)](https://www.youtube.com/watch?v=KtBefDeECVU&t=5233s): všechno za ním se ignoruje — což není past, ale nástroj: `is_prime` vrací false hned u prvního dělitele a zbytek smyčky nikdy neběží [(1:28:50)](https://www.youtube.com/watch?v=KtBefDeECVU&t=5330s). Early-exit je nejjednodušší optimalizace a nejčitelnější způsob zápisu podmínek.

**Scope jako sandbox** [(1:32:01)](https://www.youtube.com/watch?v=KtBefDeECVU&t=5521s): při hledání proměnné má přednost lokální písek, teprve pak globál [(1:33:41)](https://www.youtube.com/watch?v=KtBefDeECVU&t=5621s); lokální proměnné po návratu zmizí i s pískovištěm — a globál dovnitř cizích sandboxů nevidí [(1:34:28)](https://www.youtube.com/watch?v=KtBefDeECVU&t=5668s). **Kompozice** funkcí se vyhodnocuje jako loupání cibule: vnitřní volání první, jeho návratová hodnota je vstup vnějšího [(1:36:00)](https://www.youtube.com/watch?v=KtBefDeECVU&t=5760s) — a matematické f(g(x)), které ve škole strašilo, je najednou triviální [(1:37:36)](https://www.youtube.com/watch?v=KtBefDeECVU&t=5856s).

A pointa, kvůli které tahle myšlenka patří do skript o architektuře stejně jako do úvodu do programování: **čitelnost roste dekompozicí do pojmenovaných funkcí** [(1:39:09)](https://www.youtube.com/watch?v=KtBefDeECVU&t=5949s). Video staví vedle sebe jednu smyčku přecpanou vším a tentýž program rozbitý do funkcí, jejichž *jména čtou záměr* — burzovní pipeline „zjisti trend → stáhni zprávy → ohodnoť → kup" se čte jako lidská řeč [(1:39:55)](https://www.youtube.com/watch?v=KtBefDeECVU&t=5995s). Autor to rámuje citátem Terryho Davise „Idiots admire complexity. Genius admire simplicity." — s poznámkou, že Davis je kontroverzní figura, ale věta sedí [(1:38:22)](https://www.youtube.com/watch?v=KtBefDeECVU&t=5902s).

> **Pozn.:** UE překlad: čisté funkce v Blueprint Function Library jsou přesně „vstup → výstup, žádný sandbox se stavem"; Collapse to Function je dekompozice pro čitelnost. A „print není return" má v BP podobu Print Stringu, který debugguje, ale nic nevrací — viz [tipy do editoru](../praxe/editor-tipy.md).

**Souvislosti:** [Principy architektury](../praxe/principy-architektury.md) · [Rejstřík: Blueprint Function Library](../rejstrik.md#blueprint-function-library) · [Rejstřík: Rekurze](../rejstrik.md#rekurze)

---

## Hodnota vs. reference: kopie, nebo lísteček s šipkou

**Zdroj:** [Programming Thinking](https://www.youtube.com/watch?v=KtBefDeECVU) · [Visual Kernel](https://www.youtube.com/channel/UC9Cz481L3CeYm-ZqwqevCPQ) · stejné video, kapitola value vs. reference

**Shrnutí:** Čísla a stringy se přiřazením **kopírují**; seznamy (a slovníky, objekty) se předávají **odkazem** — nová proměnná ukazuje na tatáž data [(1:40:42)](https://www.youtube.com/watch?v=KtBefDeECVU&t=6042s). Důsledek: změna „kopie" seznamu změní i originál, a funkce, která dostala seznam, ho umí zmutovat zvenčí neviditelně [(1:43:50)](https://www.youtube.com/watch?v=KtBefDeECVU&t=6230s). Tohle je nejčastější zdroj „záhadných" bugů napříč jazyky — Blueprinty nevyjímaje.

### Rozpad myšlenky

Pravidlo z videa [(1:46:10)](https://www.youtube.com/watch?v=KtBefDeECVU&t=6370s): **lehké typy hodnotou, těžké referencí.** Proč to tak jazyky dělají, vysvětlují dvě vrstvy. Analogie [(1:44:37)](https://www.youtube.com/watch?v=KtBefDeECVU&t=6277s): článek kamarádovi nepřepisuješ slovo po slovu do zprávy — pošleš **odkaz**; je lehký a rychlý. Hardware [(1:45:24)](https://www.youtube.com/watch?v=KtBefDeECVU&t=6324s): velká data žijí na heapu, funkce pracují na stacku — do stacku se místo kopie milionového seznamu položí „sticky note" s šipkou a CPU si pro data dojde. Kopírování velkých dat stojí čas i paměť, často zbytečně.

Mentální test, který chytá bugy: u každého přiřazení a každého předání do funkce se zeptej — **kopíruju, nebo sdílím?** Když sdílím, kdo všechno teď vidí moje změny? Video ukazuje oba klasické scénáře: `listB = listA; listB[1] = 99` změní i listA [(1:41:29)](https://www.youtube.com/watch?v=KtBefDeECVU&t=6089s); funkce dostane seznam, appenduje — a volajícímu se „sám od sebe" změnil svět [(1:43:50)](https://www.youtube.com/watch?v=KtBefDeECVU&t=6230s).

> **Pozn.:** V UE tahle hranice běží mezi **structy (hodnota, kopie)** a **objekty/aktory (reference)**. Přesně na ní stojí past popsaná v [Gameplay Tags](../praxe/gameplay-tags.md#kde-tagy-bydli-a-jak-se-na-ne-ptat-bez-skrytych-bugu): Break/Make na structu ti tiše vyrobí kopii, kterou pak modifikuješ do prázdna — zatímco u aktoru měníš sdílený originál. Kdo má z téhle myšlenky v hlavě „kopíruju, nebo sdílím?", tomu se to nestane. Pro pole a mapy v BP platí pythonovská intuice: předávají se referencí.

**Souvislosti:** [Gameplay Tags: struct-copy past](../praxe/gameplay-tags.md) · [Rejstřík: Pass by reference](../rejstrik.md#pass-by-reference) · [Rejstřík: Hard reference](../rejstrik.md#hard-reference)

---

## Slovník: vztahy místo indexů

**Zdroj:** [Programming Thinking](https://www.youtube.com/watch?v=KtBefDeECVU) · [Visual Kernel](https://www.youtube.com/channel/UC9Cz481L3CeYm-ZqwqevCPQ) · stejné video, kapitola o dictionary

**Shrnutí:** Seznam odpovídá na „co je na pozici 3", slovník na „kolik stojí Big Mac" — mapuje **klíč na hodnotu**, a klíč je čitelný a smysluplný [(1:47:45)](https://www.youtube.com/watch?v=KtBefDeECVU&t=6465s). Kdykoli data v hlavě popisuješ větou „pro tohle mi řekni tamto" (jméno → cena, item → počet, hráč → skóre), říkáš si o slovník, ne o pole s indexy.

### Rozpad myšlenky

Operace zrcadlí seznam — přístup, přidání, úprava, odebrání — jen přes klíč místo indexu [(1:50:06)](https://www.youtube.com/watch?v=KtBefDeECVU&t=6606s); přidání a úprava mají dokonce stejnou syntax (nový klíč přidá, existující přepíše [(1:51:38)](https://www.youtube.com/watch?v=KtBefDeECVU&t=6698s)). Dvě pravidla k zapamatování: klíč musí sedět **přesně** — překlep je nový klíč, ne chyba, a přesně tak vznikají tiché bugy [(1:50:06)](https://www.youtube.com/watch?v=KtBefDeECVU&t=6606s); a klíčem nesmí být měnitelná struktura (seznam) — klíč, který se změní, by přestal odemykat svou hodnotu [(1:53:11)](https://www.youtube.com/watch?v=KtBefDeECVU&t=6791s). Hodnoty naopak můžou být cokoli včetně dalších slovníků (restaurace → menu → ceny [(1:52:24)](https://www.youtube.com/watch?v=KtBefDeECVU&t=6744s)).

Ukázka síly na závěr: spočítat výskyty jmen postav v celém Harry Potterovi (78 000 slov) = slovník jméno→počet plus jedna smyčka; doběhne pod sekundu [(1:56:46)](https://www.youtube.com/watch?v=KtBefDeECVU&t=7006s). Iterace má tři režimy — přes klíče, hodnoty, nebo páry současně [(1:54:45)](https://www.youtube.com/watch?v=KtBefDeECVU&t=6885s).

> **Pozn.:** V Blueprintech je slovník node **Map** (a jeho datová sestra Data Asset / Data Table s Row Name jako klíčem). Kdykoli v BP stavíš „najdi v poli prvek, kde Name == X", stavíš pomalou ruční verzi mapy — Map to udělá za tebe a bez lineárního hledání.

**Souvislosti:** [Ukládání](../praxe/ukladani.md) — SaveGame jako mapování dat · [Rejstřík: Map (dictionary)](../rejstrik.md#map-dictionary)

---

## Rekurze: skok důvěry s třemi pojistkami

**Zdroj:** [Programming Thinking](https://www.youtube.com/watch?v=KtBefDeECVU) · [Visual Kernel](https://www.youtube.com/channel/UC9Cz481L3CeYm-ZqwqevCPQ) · stejné video, závěrečná kapitola

**Shrnutí:** Faktoriál šestky je šest krát faktoriál pětky — a v tom okamžiku definuješ funkci pomocí jí samé [(1:59:45)](https://www.youtube.com/watch?v=KtBefDeECVU&t=7185s). Rekurze stojí na třech principech [(2:02:58)](https://www.youtube.com/watch?v=KtBefDeECVU&t=7378s): funkce volá sebe; má **base case**, který zastaví nekonečno; a každé volání **zmenšuje problém** směrem k base case. Zbytek je „recursive leap of faith" — důvěra, že funkce, kterou právě píšeš, svou menší práci odvede [(2:06:06)](https://www.youtube.com/watch?v=KtBefDeECVU&t=7566s).

### Rozpad myšlenky

Mechanika běhu, předvedená na fact(5) [(2:01:19)](https://www.youtube.com/watch?v=KtBefDeECVU&t=7279s): každé volání otevře vlastní rámec (sandbox z myšlenky o funkcích!), řetěz roste až k base case fact(1) = 1 a hodnoty se pak **vracejí nahoru** — 1 → 2 → 6 → 24 → 120. „Loupání cibule tam, skládání zpátky ven." Druhý příklad — otočení stringu — ukazuje návrhový postup [(2:04:32)](https://www.youtube.com/watch?v=KtBefDeECVU&t=7472s): najdi, jak problém zmenšit (první znak + zbytek), věř funkci, že zbytek zvládne, a slep výsledek. Bez zmenšování se k base case nikdy nedostaneš — to je nejčastější způsob, jak si rekurzí vyrobit nekonečno [(2:03:44)](https://www.youtube.com/watch?v=KtBefDeECVU&t=7424s).

Kde se rekurze potkává s gamedevem: stromové struktury — složky assetů, dialogové stromy, scene graph, behavior tree — se procházejí přirozeně rekurzivně („zpracuj uzel, pak totéž pro každé dítě"). Autor přiznává vysoký skill ceiling tématu a video bere jako „turistického průvodce" [(2:07:25)](https://www.youtube.com/watch?v=KtBefDeECVU&t=7645s); pro skripta stačí tři principy a vědomí, že strom = rekurze.

**Souvislosti:** [Behavior Tree](../rejstrik.md#behavior-tree) — stromy, které UE prochází za tebe · [Rejstřík: Rekurze](../rejstrik.md#rekurze)

---

## Čtyři koncepty z vyšší ligy

**Zdroj:** [Programming Concepts Only the TOP 0.1% Know](https://www.youtube.com/watch?v=5xSQR5shQYk) · [Shade of Code](https://www.youtube.com/channel/UCmxKkv3HQUNbTCshLwwDu3g) · ~4 min, koncentrát

**Shrnutí:** Rozdíl mezi dobrým a nebezpečným vývojářem podle videa nedělají frameworky, ale hrstka konceptů, které mění uvažování o výpočtech [(0:01)](https://www.youtube.com/watch?v=5xSQR5shQYk&t=1s): **invarianty**, **referenční transparentnost**, **backpressure** a **halting problem**. Všechny čtyři jsou jazykově nezávislé a všechny čtyři mají herní use-case.

### Rozpad myšlenky

**Invariant** [(0:01)](https://www.youtube.com/watch?v=5xSQR5shQYk&t=1s): podmínka, která v daném bodě programu platí *vždy*, ať se tam běh dostal jakkoli. Rámec precondition → postcondition → invariant pochází z formální verifikace a otáčí debugging naruby: místo „spusť a koukej, co se rozbije" se ptáš, **co musí platit před, po a během** — a celé třídy chyb zahyneš dřív, než je napíšeš. Herní překlad: „HP nikdy pod 0", „inventář nikdy nepřekročí kapacitu", „po load-u má každý item validního ownera" — a assert na místech, kudy data tečou.

**Referenční transparentnost** [(0:48)](https://www.youtube.com/watch?v=5xSQR5shQYk&t=48s): funkci lze nahradit její návratovou hodnotou, aniž se program změní — žádné skryté závislosti, žádný sdílený stav. Odměna: triviální testování, paralelizace i cachování. A hlavně **jako čočka na design**: když se něco blbě testuje, neptej se po mock knihovně, ptej se, *proč ta funkce není referenčně transparentní* [(1:34)](https://www.youtube.com/watch?v=5xSQR5shQYk&t=94s). V UE jsou to „pure" funkce bez side-effectů — zelené nody bez execution pinu jsou slib referenční transparentnosti, který jde bohužel porušit; nedělej to.

**Backpressure** [(1:34)](https://www.youtube.com/watch?v=5xSQR5shQYk&t=94s): co dělat, když producent chrlí rychleji, než konzument stíhá. Naivně bufferovat, míň naivně zahazovat — správně **propagovat tlak zpátky**, aby producent zpomalil. Systémy s backpressure degradují elegantně; bez ní padají „v nejhorší možný moment". Herní obdoby: spawn throttling, fronty eventů, streaming assetů — i damage nad ragdollem chce občas frontu místo laviny.

**Halting problem** [(2:20)](https://www.youtube.com/watch?v=5xSQR5shQYk&t=140s): Turing 1936 — neexistuje obecný algoritmus, který o libovolném programu rozhodne, zda skončí. Nezní prakticky, ale funguje jako **kompas hranic řešitelnosti**: každé „tool, co automaticky najde všechny bugy" a „AI, co garantuje správný kód" naráží na tenhle strop — a kdo o něm ví, je „trvale imunní vůči jisté kategorii technického hadího oleje" [(2:20)](https://www.youtube.com/watch?v=5xSQR5shQYk&t=140s).

> **Pozn.:** Video končí sponzorským segmentem (Tracer) [(3:07)](https://www.youtube.com/watch?v=5xSQR5shQYk&t=187s) — fakta z něj nečerpám. A titulek „TOP 0.1 %" ber jako clickbait koření; obsah je solidní standard informatiky.

**Souvislosti:** [Principy architektury](../praxe/principy-architektury.md) · [Telemetrie](../praxe/telemetrie.md) — fronty událostí v praxi · [Rejstřík: Invariant](../rejstrik.md#invariant) · [Rejstřík: Referenční transparentnost](../rejstrik.md#referencni-transparentnost) · [Rejstřík: Backpressure](../rejstrik.md#backpressure) · [Rejstřík: Halting problem](../rejstrik.md#halting-problem)
