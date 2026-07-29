# Případovka: level a mapa

Čtyři kusy práce, které spolu drží svět pohromadě: **místnost** jako nejmenší návrhová jednotka, **nástroj**, ve kterém se ten svět zdobí, **mapa**, která říká, co s čím sousedí, a **paměť**, díky které svět nezapomene, co v něm hráč udělal.

Nejcennější kapitola tématu je ta druhá — autor v ní stráví jedenáct hodin stavbou nástroje, který nakonec zahodí, a pak popíše, proč. Chyba nebyla v kódu; byla ve **špatně přečteném požadavku**.

---

## Místnost jako parametrizovaný celek

**Zdroj:** [I made a Custom Level Editor for my Indie Game!](https://www.youtube.com/watch?v=wQwHKKzKQL4) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~19 min, devlog

**Shrnutí:** Level se nenavrhuje jako celek, ale **po místnostech**, a každá dostane tři parametry: **mechaniku** (nebo kombinaci), **typ výzvy** (plošinovka / souboj) a **obtížnost 0 až 5**. Nula není prázdná místnost — je to **tutoriál**, a ten má u autora přesnou dvoufázovou stavbu. Háček, kvůli kterému ten systém funguje: parametry se dají **kombinovat a měnit nezávisle**, takže se z jedné mechaniky dá vytěžit deset různých místností místo jedné.

### Rozpad myšlenky

**Tři parametry** [(0:47)](https://www.youtube.com/watch?v=wQwHKKzKQL4&t=47s): mechanika (například plošinka, která se po pár vteřinách vystřelí vzhůru a zase klesne), typ výzvy a obtížnost. Smysl toho rozdělení je průzkumný — autor přiřadí novou mechaniku **spoustě místností naráz**, *„protože ji chci prozkoumat a zjistit, jestli je vůbec zábavná"*. Místnost tedy není finální obsah, ale **experiment s adresou**.

**Tutoriál jako obtížnost nula** [(1:34)](https://www.youtube.com/watch?v=wQwHKKzKQL4&t=94s) je ta část, kterou má smysl si zapamatovat celou, protože je použitelná mimo tuhle hru. Autor rovnou odmítá, co tutoriál **není**: není to postava, která vyskočí a řekne „musíš si stoupnout na houbu". Je to **místnost, kde se mechanika představí bez skutečného nebezpečí**, a to ve dvou fázích:

1. **Vůbec žádné nebezpečí.** Plošina vystřelí, ty se svezeš nahoru. Nic tě nemůže zabít.
2. **Zdání nebezpečí.** Na plošině jsou po stranách bodce — jenže *„stojíš-li na plošině, nemáš šanci se o ně zranit"*. Jejich skutečná funkce je jiná: **brání ti vylézt po zdi**, takže tě donutí použít setrvačnost z odrazu.

Celé to trvá **dvacet až třicet vteřin** a naučí to hráče *„skoro všechno, co o té mechanice potřebuje vědět"*. A pointa, kvůli které se to vyplatí: až později přijdou těžké verze téže mechaniky, **budou působit férově**, protože hráč pravidla zná.

**Pro srovnání obtížnost čtyři** [(2:20)](https://www.youtube.com/watch?v=wQwHKKzKQL4&t=140s): tatáž plošina, ale mezi bodci, kde **setrvačnost pracuje proti tobě** a místo protažení mezerou tě do bodců hodí. Sekce končí skokem, kde plošina v klidovém stavu **visí pod bodci**, takže se musí trefit okamžik. Autorovo hodnocení je zároveň definice dobré čtyřky: *„je to hodně přesné, ale když to trefíš, je to skvělý pocit."*

**Souboj se řídí týmiž parametry** [(4:40)](https://www.youtube.com/watch?v=wQwHKKzKQL4&t=280s), jen se mění, co mechanika umožňuje **nepřátelům**. Plošina dá rychlému nepříteli zajímavější pohyb po místnosti; kutálejícímu se nepříteli dovolí měnit výšku místo ježdění po jedné rovině. *„Souboj je díky tomu zajímavější, protože mají víc možností."* To je nenápadné, ale zásadní: **mechanika je vstupem pro obě strany**, ne jen pro hráče.

> **Pozn.:** Tenhle systém je hezká odpověď na otázku „jak vzniká level design, když nejsi level designér" — **rozděl prostor na jednotky a dej každé zadání**. Táž disciplína jako [rozklad problému](../teorie/co-se-ucit.md#skutecna-dovednost-je-rozklad-problemu-ne-syntax), jen aplikovaná na obsah místo na kód. Zajímavé je i to, že dvoufázový tutoriál (nejdřív bez rizika, pak se zdáním rizika) je fakticky **onboarding bez textu** — přesně to, co se v knihovně probírá u [vedení hráče](../teorie/vedeni-hrace.md) a [obtížnosti](../teorie/obtiznost.md). A stojí za zmínku, že tenhle celý návrh vznikl v **modrých krabicích** — autor otevřeně říká, že testovací místnosti *„vypadají hrozně"*, protože je celé postavené z ikony enginu. Vizuál přišel měsíce po hratelnosti.

**Souvislosti:** [Level editor, který nakonec nebyl level editor](#level-editor-ktery-nakonec-nebyl-level-editor) *(jak se ty místnosti zdobí)* · [Obtížnost a výzva](../teorie/obtiznost.md) · [Level design pro sólo vývojáře](../teorie/level-design-solo.md) · [Vedení hráče](../teorie/vedeni-hrace.md) · [Rejstřík: Graybox](../rejstrik.md#graybox) · [Rejstřík: Onboarding](../rejstrik.md#onboarding)

---

## Level editor, který nakonec nebyl level editor

**Zdroj:** [I made a Custom Level Editor for my Indie Game!](https://www.youtube.com/watch?v=wQwHKKzKQL4) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~19 min, devlog · + [Game Dev Secrets: A trick for environmental immersion!](https://www.youtube.com/watch?v=ok4Zst3R7aQ) · týž kanál · ~1 min

**Shrnutí:** Autor sepsal čtyři požadavky, deset hodin stavěl vlastní editor levelů běžící za chodu hry — a pak ho zahodil. Ne proto, že by ho nezvládl, ale proto, že si **jeden z požadavků přečetl špatně**: nešlo o to, že jeho výtvarník neumí Godot, ale že **neumí pracovat v tomhle projektu**. Řešením byl **druhý, hloupější Godot projekt** s importem a exportem. Háček, který stojí za převzetí: nejdražší chyba nebyla v implementaci, ale v tom, co se považovalo za zadání.

### Rozpad myšlenky

**Čtyři požadavky** [(10:03)](https://www.youtube.com/watch?v=wQwHKKzKQL4&t=603s), sepsané předem — autor u toho výslovně odkazuje na svůj vlastní postup [z frame data systému](pripadovka-nepratele.md#frame-data-definuj-system-driv-nez-ho-postavis): *„první krok v řešení problému je problém definovat."*

1. **Obdélník.** Parallaxové vrstvy pozadí jsou v editoru **jeden barevný obdélník** — v běžící hře fungují, v editoru se nedají vidět ani upravovat. Změna pozadí tedy znamená: najdi vrstvu ve stromu, změň číslo *„čistě podle pocitu"*, spusť hru, počkej na načtení, podívej se. A znovu.
2. **Místnosti.** Editor musí umět načíst data testovacích místností, zdobit **přímo na nich** a uložit výzdobu zpět.
3. **Renderovací tagy.** Kvůli vrstvenému kamerovému systému musí být každý sprite a dlaždicová sada **označená**, na kterou vrstvu patří — a výsledek těch značek **není v editoru vidět**. Autorovo shrnutí: *„zdobíme podle pocitu."*
4. **Výtvarník neumí Godot.** Přišel z Unity a Unrealu.

**Chyba** [(11:36)](https://www.youtube.com/watch?v=wQwHKKzKQL4&t=696s): z toho čtvrtého bodu autor usoudil, že nástroj **nesmí být editorový**, a začal stavět něco jako Mario Maker běžící ve hře. Jedna sobota, **deset až jedenáct hodin v kuse** — a výsledek popisuje bez příkras: *„je to špatné. Není to ani zdaleka hotové, už jsem do toho dal obrovský kus času a nejsem ani na pěti procentech."* Došlo mu to při ukládání a načítání levelů: *„proč proboha píšu vlastní tilemapový systém? Godot ho má a je dobrý."*

**A teď to přeformulování**, které je celým jádrem myšlenky [(12:22)](https://www.youtube.com/watch?v=wQwHKKzKQL4&t=742s): *„špatně jsem pochopil požadavek číslo čtyři. Není to tak, že by výtvarník nemohl pracovat v Godotu. Je to tak, že nemůže pracovat v projektu Isadora's Edge."* A na zdobení levelů **nic z té složitosti není potřeba**. Řešení je proto **druhý projekt**, který obsahuje jen to, co je na zdobení nutné — takže může použít všechny vestavěné nástroje enginu a k tomu si autor doplní vlastní editorové pomůcky. Zbývá jen import a export mezi projekty.

**Jak se vyřešil obdélník** [(13:54)](https://www.youtube.com/watch?v=wQwHKKzKQL4&t=834s) je hezký kus tool-scriptové matematiky: v editoru se parallax počítá proti **pozici editorového pohledu**. Posuneš-li pohled o 100 jednotek doprava, vrstva se vůči němu ocitne o 100 vlevo — ale při 25% rychlosti se měla posunout jen o 25, takže se **o 75 vrátí zpátky**. Vedlejší efekt: změna velikosti okna (nebo otevření záložky) pohledem taky pohne a pozadí se „samo od sebe" posune.

A oprava toho vedlejšího efektu je nejlepší věc v celém videu [(15:26)](https://www.youtube.com/watch?v=wQwHKKzKQL4&t=926s), protože **matematika byla správně a problém byl vjemový**. Autor přidal tlačítko, které do editoru **vloží postavu a obrys herní kamery**, ukotvené k pozici editorového pohledu. Najednou dává posun smysl, protože je vidět, **vůči čemu** se posouvá. Bonus zdarma: podle té postavy se dají assety rovnou skládat tak, jak je uvidí hráč.

**Zbylé dva požadavky vypadly samy.** Vrstvy v novém projektu **spravují Z index svých dětí**, takže pořadí je vidět v editoru — a při exportu se Z indexy převedou na renderovací tagy původního projektu [(16:13)](https://www.youtube.com/watch?v=wQwHKKzKQL4&t=973s). Geometrie místností se exportuje do **JSON** a v editoru se z něj poskládá dlaždicová sada, na kterou se zdobí; při spuštění se geometrie skryje, **ale kolize zůstanou** [(16:59)](https://www.youtube.com/watch?v=wQwHKKzKQL4&t=1019s). A protože si autor přenesl i celý ovladač postavy, dá se v editoru **rovnou hrát** — a pocit odpovídá jedna ku jedné.

> **Pozn.:** Dvě věci na okraj. **Parallax sám** má v knihovně i minutové vysvětlení, proč se dělá [(0:02)](https://www.youtube.com/watch?v=ok4Zst3R7aQ&t=2s): pozadí, které se hýbe stejně rychle jako kamera, působí jako *„namalovaný obraz hor místo skutečných hor v dálce"*; zpomalením vzniká iluze hloubky a **rychlostí se řídí vnímaná velikost** — pomalejší pozadí působí větší a vzdálenější. **A ta hlavní lekce** se dá zobecnit takhle: dřív než postavíš nástroj, ověř, **jestli řešíš skutečné omezení, nebo jeho zástupný popis.** „Nemůže používat Godot" a „nemůže používat tenhle projekt" znějí podobně a vedou k řešením, jejichž pracnost se liší o řád. Autorových deset hodin je levná cena za tuhle lekci — a on ji navíc dal veřejně, což se v devlozích nevidí často.

**Souvislosti:** [Nástroje pro sebe](projekt-a-vykon.md#nastroje-pro-sebe-editor-script-ktery-ti-usetri-boilerplate) *(editorové nástroje obecně)* · [Místnost jako parametrizovaný celek](#mistnost-jako-parametrizovany-celek) · [Kdy scéna a kdy resource](resources.md#kdy-scena-a-kdy-resource-prestavena-hra-jako-dukaz) *(oddělení obsahu od formy)* · [Dokumentace jako audit](../zapisky/dokumentace-jako-audit.md) *(psaní jako nástroj rozhodování)* · [Rejstřík: Parallax](../rejstrik.md#parallax) · [Rejstřík: Z index](../rejstrik.md#z-index)

---

## Mapa metroidvanie: data, pohled a jediné místo pravdy

**Zdroj:** [Making a Massive Metroidvania Map (The Right Way)](https://www.youtube.com/watch?v=FI0-yz5Xcz0) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~18 min, devlog · + [Game Dev Secrets: Maps and Transitions!](https://www.youtube.com/watch?v=zG4ShItsV_Q) · týž kanál · ~2 min

**Shrnutí:** Velká propojená mapa se rozpadá na dvě nezávislé věci: **datový model** (co s čím sousedí a jak se mezi tím přechází) a **pohled** (jak se to hráči nakreslí). Autor si nejdřív vyzkoušel hotové řešení, pak si postavil vlastní — a klíčové rozhodnutí je jediné: **spojení mezi místnostmi se definuje na jednom místě, v mapě**, ne dvakrát ve dvou místnostech. Háček, který dvě minuty shortu vysvětlují líp než celý devlog: dveře popsané z obou stran **spolu můžou nesouhlasit**.

### Rozpad myšlenky

**Napřed hledej hotové řešení** [(0:47)](https://www.youtube.com/watch?v=FI0-yz5Xcz0&t=47s) — autor to dělá a doporučuje: vyzkoušel existující metroidvania systém pro Godot a zjistil, že nedělá přesně to, co chce. Teprve pak píše vlastní. Ten pořádek stojí za převzetí; hledání trvá odpoledne, psaní týdny.

**Tři pojmy, které to celé nesou** [(1:34)](https://www.youtube.com/watch?v=FI0-yz5Xcz0&t=94s): **world room** je skutečná místnost se vším (assety, nepřátelé, výzdoba). **Map room** je uzel v mapě, který jen **odkazuje** na tu místnost — bílý obdélníček. A **map metadata** je uzel uvnitř místnosti, který nese dvě věci pro mapu: jak se místnost má kreslit a **seznam všech přechodů, které v ní jsou**.

**Proč se kreslení deleguje na místnost** [(2:21)](https://www.youtube.com/watch?v=FI0-yz5Xcz0&t=141s), i když by člověk čekal opak: mapa by ráda kreslila všechno sama, jenže **nemá jak** — bez přístupu k datům té konkrétní místnosti nemá co nakreslit. Autor to řeší háčkem: metadata místnosti řeknou, jak se má vykreslit, a mapa to jen zavolá.

**Přechody jako past na ruční práci** [(4:41)](https://www.youtube.com/watch?v=FI0-yz5Xcz0&t=281s). Trigger zóna na okraji místnosti funguje, ale její umístění je *„bolestivý ruční proces, který je navíc náchylný k chybám"*, a ty chyby jsou vidět: hranice kamery nejsou v editoru vidět, takže se musí odečítat z pravítek — **a přechod nemá být přesně na hraně obrazovky**, ale kousek za ní, jinak se spustí, i když hráč už zjevně zastavil. K tomu: špatně tvarovaná zóna dovolí přeskočit ji úplně, a **změna velikosti zóny mění i její pozici**, takže se hráč v další místnosti objeví jinde — třeba ve vzduchu.

**Oprava má tři kroky a všechny jsou vizuální** [(6:13)](https://www.youtube.com/watch?v=FI0-yz5Xcz0&t=373s):

- **Hranice kamery se kreslí do editoru** — žlutá čára plus červený pruh kolem ní, protože *„při přibližování a oddalování pixel artu se jednotlivé řádky pixelů občas ztratí"*, a červená to udrží viditelné.
- **Parametr velikosti přechodu**, který zónu přeškáluje a přemístí **bez vlivu na místo, kde se hráč objeví**.
- **Přechod se kreslí jako obdélník s červeným okrajem na jedné straně** — a ten okraj označuje, kde má být hranice kamery. Umístění se pak scvrkne na *„srovnej červené se zlatým"*. Autorův popis toho pocitu je výmluvný: *„je to jako lego, prostě to zacvakneš na správné místo."*

**A teď to jediné místo pravdy.** Minutový klip to formuluje čistěji než devlog [(0:02)](https://www.youtube.com/watch?v=zG4ShItsV_Q&t=2s): přidáš dveře do hory („odsud do jeskyně") a druhé dveře do jeskyně („odsud do hory"). Funguje to — a **je to tentýž průchod popsaný dvakrát**, takže se ty dva popisy můžou rozejít. Splete-li se ten druhý, vejdeš do jeskyně a vyjdeš v cizí jeskyni. Řešení: **objekt přechodu žije mimo obě místnosti** a obě dveře na něj jen odkazují. *„Nemůžou se neshodnout, protože odkazují na tentýž objekt."*

Přesně to autor v devlogu postaví [(9:17)](https://www.youtube.com/watch?v=FI0-yz5Xcz0&t=557s): každý přechod si při vzniku vygeneruje **resource se jménem a unikátním ID**, mapa má uzly, které spojují **dva takové resources**, a v inspektoru se vybírají z rozbalovacího seznamu. Výsledek: *„nikdy jsem se nemusel dotknout přechodů v samotných místnostech. Ani jsem je nemusel otevřít."* Za běhu se pak přechod zeptá mapy „ke kterému jsem připojený", načte se cílová místnost a postava se objeví u protějšího přechodu.

**A jedna metodická perla** [(11:37)](https://www.youtube.com/watch?v=FI0-yz5Xcz0&t=697s): *„zkus to nejdřív hrubou silou. Vymysli nejhloupější, nejjednodušší řešení a podívej se, jestli funguje. Když jo bez vedlejších efektů, ušetřil jsi spoustu času. Když ne, aspoň problému líp rozumíš."* Hrubá síla tady byla „zmenšit dlaždice místnosti na velikost mapy". Autor zjistil, že Hollow Knight má **462 místností**, hodil jich na obrazovku **300** — a hra spadla z 2500 FPS na **zhruba 40**. Test trval chvíli a **vyloučil celou rodinu řešení**.

> **Pozn.:** Jeho druhý pokus (překryvná mapovací dlaždicová sada → polygon) selhal na shaderech, protože polygon **neměl texturu ani UV**. Poučení, ke kterému došel, je hezky obecné: jakmile si texturu musel vygenerovat, byl polygon zbytečný a stačil sprite. **Meziřešení, které existuje jen kvůli historii vývoje, je většinou znamení, že se máš vrátit o krok.** A pak přijde poslední přiznání, které je nejvíc poučné [(16:17)](https://www.youtube.com/watch?v=FI0-yz5Xcz0&t=977s): u skrývání neprozkoumaných částí mapy narazil na to, že každý nápad má hraniční případ — *„a nakonec mi došlo, že se musím napřed rozhodnout, jak má mapa vypadat, než začnu navrhovat systémy pod ní."* To je poctivé pojmenování situace, kdy technický problém není technický: **chybí rozhodnutí, ne řešení.**

**Souvislosti:** [Jediný zdroj pravdy](signaly.md#jediny-zdroj-pravdy-dva-budiky-ukazuji-ruzny-cas) *(týž princip pojmenovaný)* · [Persistence key](#persistence-key-svet-ktery-si-pamatuje) *(co si mapa musí pamatovat)* · [Změna žánru po třech letech](pripadovka-proces.md#zmena-zanru-po-trech-letech) *(proč ta mapa vůbec vznikla)* · [Prostor vypráví](../teorie/prostor-vypravi.md) · [Rejstřík: Single source of truth](../rejstrik.md#single-source-of-truth) · [Rejstřík: Level streaming](../rejstrik.md#level-streaming)

---

## Persistence key: svět, který si pamatuje

**Zdroj:** [Game Dev Secrets: Loading Zone Trick!](https://www.youtube.com/watch?v=EP-fIhAe2Jo) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~2 min

**Shrnutí:** Ve hře s **neviditelnými načítacími zónami** vzniká problém, který v hrách s oddělenými místnostmi není: přejdeš zónu, oblast se odloží z paměti — a když se vrátíš, **poražený nepřítel je zase naživu**. Řešení se jmenuje **persistence key** a je pěkně minimalistické: poražený nepřítel předá „klíč" něčemu, co se z paměti neodkládá, a při dalším načtení se sám zeptá, jestli ten klíč existuje.

### Rozpad myšlenky

**Proč to vůbec vzniká** [(0:01)](https://www.youtube.com/watch?v=EP-fIhAe2Jo&t=1s): porazíš nepřítele u načítací zóny, přejdeš do další oblasti (předchozí se uvolní), otočíš se a vrátíš — oblast se načte znovu **i s nepřítelem**. Autor pojmenovává, proč to vadí, přesně: *„z pohledu hráče to nedává smysl. Vypadá to, jako by se prostě náhodně obnovil."*

**A tady je ta zajímavá část**: spousta her tenhle problém **nemá**, protože mají načítací zóny svázané s oddělenými místnostmi — *„a obnovit nepřátele při vstupu do nové místnosti působí úplně v pořádku."* Rozdíl tedy není technický, ale **v očekávání hráče**: viditelná hranice obnovu ospravedlní, neviditelná ne. Kdo chce plynulý svět, musí si připlatit pamětí.

**Mechanismus** [(0:47)](https://www.youtube.com/watch?v=EP-fIhAe2Jo&t=47s) má tři kroky a je záměrně hloupý:

1. **Zvol místo, které se neodkládá.** V ukázce je to hráčka — *„představ si, že má velkou tašku, do které si dává klíče, co dostane."*
2. **Při porážce nepřítel odevzdá klíč** s vlastním podpisem („jsem mrtvý, podepsán Runtonk").
3. **Při načtení se nepřítel zeptá**, jestli jeho klíč existuje. Ne → načti normálně. Ano → načti ho **v poraženém stavu**.

Výsledek: *„můžeme ho odkládat a načítat, kolikrát chceme, a on kouzelně neobživne."*

> **Pozn.:** Za tou jednoduchostí se schovává rozhodnutí, které stojí za vyslovení: **stav světa nepatří objektům, které ze světa mizí.** Nepřítel nemůže být zdrojem pravdy o vlastní smrti, protože smrtí přestane existovat — takže se ta informace musí přesunout jinam. Tentýž vzor má v knihovně [ukládání stavu světa v UE](../praxe/ukladani.md#ukladani-stavu-sveta-spawn-update-zniceni-a-indikator), jen tam pod jménem „co se ukládá a co se dopočítá". Praktická výhrada, kterou video nezmiňuje: **taška na klíče roste**, a u hry velikosti metroidvanie je potřeba rozmyslet, co do ní patří (poražení bossové, otevřené zkratky, sebrané předměty) a co ne (každý zabitý slimák) — jinak se z ní stane [save soubor, který nabobtná](../praxe/ukladani.md#save-system-ktery-prezije-druhy-projekt-struktury-interface-a-async). A pozor na sousední rozhodnutí ze [systémů](pripadovka-systemy.md#dve-drobnosti-ktere-hrac-pozna-premapovani-a-psaci-stroj): **nastavení hry do téhle tašky nepatří**, protože přežívá i nové hry.

**Souvislosti:** [Mapa metroidvanie](#mapa-metroidvanie-data-pohled-a-jedine-misto-pravdy) · [Ukládání stavu světa](../praxe/ukladani.md#ukladani-stavu-sveta-spawn-update-zniceni-a-indikator) *(týž problém v UE)* · [Dvě drobnosti, které hráč pozná](pripadovka-systemy.md#dve-drobnosti-ktere-hrac-pozna-premapovani-a-psaci-stroj) *(co do save souboru naopak nepatří)* · [Rejstřík: Persistence key](../rejstrik.md#persistence-key) · [Rejstřík: Level streaming](../rejstrik.md#level-streaming)
