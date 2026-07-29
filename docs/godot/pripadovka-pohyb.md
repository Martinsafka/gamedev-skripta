# Případovka: pohyb a ovládání

Od téhle kapitoly jde sekce jinou cestou. Místo návodů sledujeme **jeden projekt** — 2D akční platformer *Isadora's Edge* inspirovaný Symphony of the Night, Hollow Knight a Mega Man X — a to, jak se v něm rozhodovalo. Autor natáčí devlogy roky a má vzácnou vlastnost: **mluví i o tom, co nevyšlo**, včetně věcí, které nakonec vyhodil.

Případovka není návod. Je to materiál na otázku *„jak se k takovému rozhodnutí došlo"*, a proto se z ní bere jinak: ne postup, ale **kritéria**. Začínáme u pohybu, protože tam se u platformeru rozhoduje všechno ostatní.

---

## Rozdělit vstup od provedení: dash jako důkaz

**Zdroj:** [Perfecting MOVEMENT for my Indie Game | Devlog](https://www.youtube.com/watch?v=EQxcdftp_eQ) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~19 min, devlog

**Shrnutí:** Autor přepsal player controller z game-jamové verze a rozdělil ho na dvě části: jedna **čte vstup a nastavuje stav**, druhá se na ten stav dívá a **provádí ho**. To je běžné doporučení — zajímavý je až důkaz, že fungovalo: **dash byl cítit dobře, aniž by ho ladil.** V předchozí, propojené verzi *„jsem se trápil, abych dash rozchodil, protože jsem ho nedokázal izolovat"*. Háček, který stojí za převzetí: dobrá architektura se nepozná na diagramu, ale na tom, **jak levně se dá ladit jedna věc**.

### Rozpad myšlenky

**Mechanismus** je krátký [(0:01)](https://www.youtube.com/watch?v=EQxcdftp_eQ&t=1s): komponenta vstupu přeloží stisky na **záměr** („chce se pohybovat doprava", „chce dashovat") a uloží ho jako stav. Druhá komponenta se ptá jen na stav a řeší, **jak** se to udělá. Autorovo zdůvodnění je předvídavé — chtěl, aby *„se daly snadno přidávat nové funkce"*, protože ví, co přijde: brnění, útoky, upgrady.

**Důkaz, že rozdělení nebylo kosmetické** [(0:47)](https://www.youtube.com/watch?v=EQxcdftp_eQ&t=47s), je ta část, kterou má smysl si zapamatovat. V jamové verzi bylo všechno propletené — *„bylo to všechno nacpané dohromady ve stylu ‚když zmáčkneš tohle, začni provádět kód dashe'"* — a ladění dashe znamenalo hrabat se v kódu, který dělal deset dalších věcí. Po rozdělení stačilo sáhnout na jednu komponentu a **výsledek byl dobrý napoprvé**. To je měřitelný přínos architektury: ne „je to hezčí", ale **„laděná změna se dotýká jednoho místa"**.

**Animace jako ladicí nástroj** je nečekaný vedlejší efekt [(3:08)](https://www.youtube.com/watch?v=EQxcdftp_eQ&t=188s). Když přidal animační controller, který **sleduje stav postavy** a podle něj přehrává animaci, začal vidět chyby, o kterých nevěděl — *„předčasné opuštění zavěšení na zdi, nespouštění wall jumpu, takové věci"*. Logika ty chyby dělala celou dobu; teprve **zviditelnění stavu** je odhalilo. Zobecnění, které z toho děláme: **animace je vizualizace stavového automatu, jen ji tak nikdo nepoužívá.** Kdo ladí stavový stroj bez obrazu, ladí poslepu.

**Dva snímky, které dělají rozdíl** [(11:38)](https://www.youtube.com/watch?v=EQxcdftp_eQ&t=698s): mezi animací skoku a animací pádu přibyla **dvousnímková přechodová animace**. Autorova reakce stojí za převzetí — *„je šílené, jaký rozdíl udělají ty dva snímky"* — a nejvíc je to znát u **krátkých skoků**, kde se po jump cutu okamžitě přechází do pádu. Bez přechodu to cukne, s přechodem to plyne. Levnější vylepšení pocitu z pohybu než dva nakreslené snímky asi neexistuje.

> **Pozn.:** Tenhle přepis je konkrétní podoba toho, co má sekce popsané obecně u [kompozice](kompozice.md#has-a-misto-is-a-hrdinuv-batoh) a [sobecké komponenty](kompozice.md#komponenta-ma-byt-sobecka-test-kamene) — a jeho hodnota je právě v tom, že přišel **po** špatné zkušenosti, ne z knihy. Za zmínku stojí i to, co autor přiznává mimochodem: *„musel jsem si o to pár dní tlouct hlavu, než to začalo spolupracovat."* Refaktor nebyl zadarmo a on to neschovává. A jedna vlastní poznámka k formátu: autor v tom videu natáčí **každý den** a otevřeně říká, proč — *„vědomí, že to budu nahrávat, mě drží poctivého a nutí mě na hře fakt dělat."* Devlog jako závazek, ne jako marketing; táž mechanika, jakou popisuje [Devlog jako mapa](../zapisky/devlog-jako-mapa.md).

**Souvislosti:** [Komponenta má být sobecká](kompozice.md#komponenta-ma-byt-sobecka-test-kamene) *(týž princip jako pravidlo)* · [Stavový automat](stavy-a-vzory.md#stavovy-automat-stav-je-podminka-plus-chovani) · [Skok, který rozumí hráči](animace-a-pohyb.md#skok-ktery-rozumi-tomu-co-hrac-chtel) *(jump cutting, které tu přibylo)* · [Devlog jako mapa](../zapisky/devlog-jako-mapa.md) · [Rejstřík: Separation of concerns](../rejstrik.md#separation-of-concerns)

---

## Tři tiché opravy pohybu

**Zdroj:** [Game Dev Secret: REAL control over your character?](https://www.youtube.com/watch?v=jd91r5kwdnc) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~1 min · + [Game Dev Secrets: Why am I so heavy?](https://www.youtube.com/watch?v=ZSD2EOBEWlU) · týž kanál · ~1 min · + [How passable (one-way) platforms work in game development!](https://www.youtube.com/watch?v=CZgJgrndt5Q) · [Challacade](https://www.youtube.com/channel/UCeiV3e6Zhppi-oOSfiZo_nA) · ~1 min

**Shrnutí:** Tři minutové klipy, které spolu nesouvisejí obsahem, ale mechanismem: **každý opravuje chování, které je technicky správné a přesto špatné.** Skok bez jump cuttingu je vždycky maximální. Gravitace, která se hromadí na zemi, udělá z chůze přes hranu pád jako kámen. A plošina, kterou nelze podskočit, je technicky vzato zeď. Háček, který je společný: **žádnou z těch tří věcí neuvidíš v kódu — uvidíš je jen tak, že hru hraješ.**

### Rozpad myšlenky

**Jump cutting** [(0:02)](https://www.youtube.com/watch?v=jd91r5kwdnc&t=2s): stisk skoku přidá svislou rychlost — a protože je pokaždé stejná, **není jak udělat malý skok**. Oprava je jedna podmínka: **pustí-li hráč tlačítko, nastav svislou rychlost na nulu.** Tím vzniká plynulé spektrum — krátký ťuk, střední přidržení, plné držení. Autorova formulace toho, co se tím získá, je přesná: *„dává to hráči přesnou kontrolu nad skokem."*

**Gravitace se hromadí, i když stojíš** [(0:02)](https://www.youtube.com/watch?v=ZSD2EOBEWlU&t=2s) je z těch tří nejzáludnější, protože se **projeví až jinde, než vzniká**. Když postava stojí na zemi, gravitace ji dál každý snímek tlačí dolů; nikam se neposune, ale **svislá rychlost roste**. Skočíš-li, rychlost se přepíše silou skoku a problém zmizí. Ale **sejdeš-li z hrany bez skoku, spadneš jako kámen**, protože si s sebou neseš rychlost nasbíranou za celou dobu stání. Oprava je jeden řádek — *„stojíš-li na zemi, nastav svislou rychlost na nulu"* — a autorova poznámka k tomu je cennější než samotný fix: *„na tenhle druh chyby si dávej obzvlášť pozor. Je to drobná fyzikální chyba, která se snadno schová pod povrch a bez pečlivého testování projde."* Přidává i praktický dodatek, na který se zapomíná: **oprav to i nepřátelům.**

**Jednosměrné plošiny** [(0:01)](https://www.youtube.com/watch?v=CZgJgrndt5Q&t=1s) řeší jediný autor mimo tenhle projekt a řešení je hezky minimalistické: plošina **průběžně kontroluje, jestli je hráč nad ní**, a podle toho se přepíná mezi „normální kolize" a „ignoruj". Nejde tedy o speciální typ tělesa, ale o **kolizi řízenou vztahem k hráči**. A poslední věta je ta zajímavá: *„u nepřátel to funguje pořád — je jim jedno, jestli je plošina průchozí, berou ji vždycky jako normální."* Tedy **pravidlo platí jen pro hráče**, což je designové rozhodnutí, ne technický kompromis: prostupnost je hráčova výsada.

> **Pozn.:** Všechny tři opravy patří do téže rodiny jako [tiché úlevy z Celeste](../teorie/game-feel.md#celeste-krivky-v-snimcich-a-hrst-tichych-ulev) — pracují se **záměrem hráče**, ne s doslovnou fyzikou. Godot má mimochodem [jednosměrnou kolizi](prvni-hra.md#znovupouzitelna-scena-jedna-kill-zone-pro-propast-i-pro-slimaka) jako zaškrtávátko na collision shapu, takže tenhle konkrétní problém řešit nemusíš — zajímavý na tom klipu je **mechanismus**, ne implementace. A ta hromadící se gravitace je učebnicová ukázka bugu, který **nemá symptom v místě příčiny**: hledáš ho v kódu pádu, a on vzniká, když postava stojí.

**Souvislosti:** [Skok, který rozumí hráči](animace-a-pohyb.md#skok-ktery-rozumi-tomu-co-hrac-chtel) *(tytéž opravy systematicky)* · [Celeste: tiché úlevy](../teorie/game-feel.md#celeste-krivky-v-snimcich-a-hrst-tichych-ulev) · [Delta a physics process](prvni-hra.md#delta-a-physics-process-proc-se-rychlost-nasobi-casem) · [Rejstřík: Game feel](../rejstrik.md#game-feel) · [Rejstřík: Coyote time](../rejstrik.md#coyote-time)

---

## Proč vyhodil všechny šikmé plochy

**Zdroj:** [Why Slopes are Shockingly Difficult for Indie Game Devs](https://www.youtube.com/watch?v=rHMJccb5IOM) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~17 min, případovka

**Shrnutí:** Autor šikmé plochy miluje, měl je ve hře roky a **všechny je smazal**. Ne kvůli jednomu problému, ale kvůli třem vrstvám nákladů, které se sčítaly: **fyzika** (každá oprava odhalí další problém), **výtvarno** (šikmé plochy si vynutí perspektivní dlaždice, a to omezuje celý styl) a **level design** — kde přišel na to nejnepříjemnější: *„nedokázaly mi pomoct, spíš mi to komplikovaly."* Háček, kvůli kterému stojí ta případovka za čtení, i když šikmé plochy nikdy dělat nebudeš: **je to učebnicová ukázka toho, jak se rozhoduje o odstranění funkce.**

### Rozpad myšlenky

**Vrstva jedna: fyzika.** Autor to shrnuje s nadsázkou, která podle něj *„není tak daleko od pravdy"* — enginy šikmé plochy nesnášejí [(1:33)](https://www.youtube.com/watch?v=rHMJccb5IOM&t=93s). Řetěz oprav, který popisuje, stojí za sledování celý, protože každá oprava rodí další problém:

1. Postava po svahu **klouže dolů** → zapnout přichytávání k podlaze.
2. Přichycená postava **nemůže skočit** → při přechodu do skoku přichytávání vypnout.
3. Postava jde **rychleji z kopce a pomaleji do kopce**, protože se do pohybu přimíchá gravitace → změřit normálu svahu, spočítat úhel a **kompenzovat**.
4. Totéž se opraví nepřátelům. Jenže **nepřátelé pak nechtějí jít z kopce**: paprsek hledající zem pod nimi na dost strmém svahu **nedosáhne** a oni to vyhodnotí jako díru [(3:07)](https://www.youtube.com/watch?v=rHMJccb5IOM&t=187s). Prodloužit paprsek nejde (viděl by dlaždici přes propast), takže **druhý paprsek** hledá zvlášť svah.
5. A nepřátelé **nechtějí ani do kopce**, protože paprsek na detekci zdi svah považuje za zeď → při zásahu si vyžádat **normálu** a podle úhlu rozhodnout, jestli je to zeď, nebo schůdný svah.

Autorův závěr té sekce je poctivý: *„a to jsou jen hráč a nepřátelé — ani jsme nezačali s fyzikou projektilů."* Sám dodává, že tohle by ho samo o sobě nezastavilo, *„protože většinu těch problémů jsem už vyřešil."*

**Vrstva dvě: výtvarno** [(6:14)](https://www.youtube.com/watch?v=rHMJccb5IOM&t=374s), a tady je argument silnější, než čekáš. Postava stojící na svahu **vypadá špatně** — idle animace má nohy rozkročené pro rovnou zem. Řešení „udělat druhou sadu animací pro svahy" nefunguje, protože se problém opakuje u každého nepřítele a **u širokých nepřátel je nejhorší**: *„sotva to vypadá, že je vůbec na zemi — jako by vedle ní jen tak plul."*

Skutečná příčina je hlubší: **dlaždice nemají perspektivu.** Aby postava mohla stát *na* svahu a ne *vedle* něj, musí dlaždice ukazovat i horní plochu — tedy mít **hloubku v Z**. Autor to demonstruje srovnáním: Hollow Knight má dlaždice čelně a postava stojí na horní hraně; Mega Man X4 má perspektivu a postava stojí **uprostřed horní plochy**. Jenže perspektiva má vlastní cenu [(9:18)](https://www.youtube.com/watch?v=rHMJccb5IOM&t=558s): **extrémní úhly nepodporují lezení po zdi** (z jedné strany by byla postava schovaná za zdí) a „falešná perspektiva", která to obchází, *„vypadá divně"*. A pak je tu potvrzení zvenčí, které váží nejvíc — mluvil o tom s environment artisty a slyšel: *„fakt ty svahy potřebuješ? Protože ten Z index je těžkej."*

**Vrstva tři: level design**, a tohle je ta, která rozhodla [(11:37)](https://www.youtube.com/watch?v=rHMJccb5IOM&t=697s). Šikmé plochy **ruší ledge guarding** — situaci, kdy nepřítel stojí nad hranou a ty se k němu musíš dostat skokem, tedy z nevýhody. *„Svah znamená, že k vyvýšenému nepříteli prostě dojdeš. Změna výšky přestane být sama o sobě výhodou nebo nevýhodou."* Námitka „tak tam ten svah nedávej" vede na dilema, ze kterého není cesta ven: chceš-li výzvu, uděláš hranu; chceš-li jen změnu výšky bez výzvy, taky nepotřebuješ svah. Autorův okamžik pravdy přišel, když **konečně našel použití** — past s laserem, kde svah trochu usnadnil stavbu jedné místnosti — a došlo mu, že *„když je takhle těžké najít pro to použití, možná to nepotřebuju."*

**A nakonec obrat, který je nejcennější** [(13:56)](https://www.youtube.com/watch?v=rHMJccb5IOM&t=836s): *„intuitivně bys čekal, že víc možností dělá level design snazší. Já ale zjišťuju, že kreativitu často plodí omezení."* Míň nástrojů mu dalo **víc nápadů**, protože musel ty zbývající použít vynalézavě. Otázka, kterou si nakonec položil, je přenositelná na jakoukoli funkci: **„usnadňuje mi tahle věc stavbu levelů, nebo mi ji ztěžuje?"** Odpověď ho překvapila.

> **Pozn.:** Za pozornost stojí, jak dlouho to trvalo — autor přiznává, že *„jsem si mnohokrát řekl, že bych je měl vyhodit, a pak nikdy"*, a že mu je těžké to i teď říct nahlas. **Emoční investice do vlastní funkce je náklad, který v rozpočtu nikdy není** a přesto rozhoduje. Zároveň je poctivý v tom, kdy jeho závěr **neplatí**: máš-li mechaniku, která svahy potřebuje (klouzání, setrvačnost), nebo prostě nevadí, že to bude práce navíc — dělej je. To je správný tvar takového doporučení: **není to pravidlo, je to účet.** A jeho poslední argument je nejlevnější možný důkaz: *„Hollow Knight je skvělá hra a žádné svahy tam nejsou."*

**Souvislosti:** [Design by constraint](../teorie/scope.md#design-by-constraint-krabice-napred-napad-dovnitr) *(omezení jako zdroj nápadů — tady doložené praxí)* · [Scope creep: nápad zaparkuj](../teorie/scope.md#scope-creep-napad-zaparkuj-nezabijej) · [Cut line](../zapisky/cut-line.md) *(rozhodování o tom, co ze hry vypadne)* · [Prostor a hranice](../teorie/prostor-a-hranice.md) · [2D vizuál: izometrie a její kompromisy](../teorie/2d-vizual.md#izometrie-perspektiva-bez-perspektivy-a-jeji-kompromisy) *(táž otázka perspektivy dlaždic)* · [Rejstřík: Z index](../rejstrik.md#z-index) · [Rejstřík: Constraints](../rejstrik.md#constraints)

---

## Útočit v pohybu, nebo se zastavit

**Zdroj:** [Perfecting MOVEMENT for my Indie Game | Devlog](https://www.youtube.com/watch?v=EQxcdftp_eQ) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~19 min, devlog · + [Game Dev Secrets: How to make your Aerial Attacks feel SUPER smooth!](https://www.youtube.com/watch?v=kYPMIfROc_A) · týž kanál · ~1 min

**Shrnutí:** Klasické dilema 2D platformeru, na které podle autora *„jsem nenašel nikoho, kdo by ho opravdu vyřešil"*: má se postava při útoku zastavit? **Pohyb při útoku působí plynule, zastavení působí zvážené a opatrné** — a obojí má cenu. Jeho řešení je kompromis vázaný na combo: první rány jdou v pohybu, poslední tě zastaví. K tomu jedna technická drobnost, která otevírá celou vrstvu mechanik: **oddělit animaci efektu od animace postavy.**

### Rozpad myšlenky

**Proč to není maličkost** [(13:58)](https://www.youtube.com/watch?v=EQxcdftp_eQ&t=838s): autor chce **tříranné combo se stoupajícím poškozením** (zhruba 100 / 150 / 200 %), aby hráče motivoval **zůstat v souboji** místo taktiky „přiběhni, sekni, uteč". Jenže combo dělané za pohybu se pere s pocitem váhy.

**Tři možnosti a jejich ceny:**

- **Útok jen v horní půlce spritu**, zatímco nohy dál běží. Nejlevnější a podle autora *„nikdy to nepůsobí dobře — není za tím cítit váha."*
- **Zastavit postavu při útoku.** Funguje, ale *„zamrznout na místě uprostřed pohybu je dost rušivé, není to zábavný zážitek."*
- **Kompromis:** první (nebo první dvě) rány comba jdou v pohybu, **třetí tě zastaví**, protože právě u ní má být cítit váha.

Zobecnění, které z toho děláme: to není hledání „správné" odpovědi, ale **rozdělení jedné akce na fáze s různými pravidly**. Combo přestalo být třemi kopiemi téhož útoku a stalo se **eskalací**, kde poslední rána stojí víc — pohybem, který jí obětuješ.

**Rozdíl v pocitu** autor pojmenovává přesně [(15:31)](https://www.youtube.com/watch?v=EQxcdftp_eQ&t=931s): pohyb při útoku dělá hru **plynulou**, zastavení ji dělá **zváženou a opatrnou** — *„protože nemůžeš dál poskakovat kolem, musíš se zastavit a udeřit."* To je designová páka, ne technický detail: týmž přepínačem se z akční hry stane hra o načasování.

**A ta technická drobnost, která otevírá dveře** [(0:02)](https://www.youtube.com/watch?v=kYPMIfROc_A&t=2s). Vzdušný útok kreslí za mečem **smear** — rozmazaný pruh, který nese většinu vizuálního dojmu. Když se ale útok zruší (třeba dopadem na zem), **smear se usekne uprostřed** a vypadá to špatně. Oprava je jedna: **přehrávat smear jako samostatnou animaci**, ne jako součást postavy. Postava se může přerušit, smear dohraje.

A teď to, kvůli čemu ta minuta stojí za samostatnou zmínku: *„otevře ti to celou škálu mechanik na rušení animací — dashování z útoku, skákání z útoku, dokonce combo přes zrušení dopadem."* Z opravy vizuální vady se stal **prostor pro dovednost**: hráč, který se naučí útok zrušit ve správný okamžik, získá tempo. Přesně takhle v bojovkách vznikla polovina pokročilých technik.

> **Pozn.:** Dvě věci k doplnění. **Zaprvé** — autor v tom videu otevřeně sbírá zpětnou vazbu (*„rád bych slyšel, jak to řešili jiní"*), což je zdravější postup než tiché rozhodnutí; komentáře pod devlogem jsou u něj doložitelně zdroj změn ve hře. **Zadruhé** — oddělení smearu je konkrétní podoba obecnějšího pravidla: **efekt, který má dohrát, nesmí být dítětem věci, která se může přerušit.** Totéž platí pro zvuk sebrané mince, částice výbuchu i UI hlášku; v sekci to má obecnou podobu u [AnimationPlayeru jako časovače](prvni-hra.md#animationplayer-jako-casovac-sekvence-bez-jedineho-radku-kodu).

**Souvislosti:** [Combo a hit stop](pripadovka-nepratele.md#combo-a-hit-stop-dva-casovace-a-ctvrt-sekundy) *(jak se to combo technicky staví)* · [Rozdělit vstup od provedení](#rozdelit-vstup-od-provedeni-dash-jako-dukaz) · [Game feel: combat je rytmus](../teorie/game-feel.md#combat-je-rytmus-kazdy-utok-ma-ucel-a-placeholder-je-nastroj) · [AnimationPlayer jako časovač](prvni-hra.md#animationplayer-jako-casovac-sekvence-bez-jedineho-radku-kodu) · [Rejstřík: Animation cancel](../rejstrik.md#animation-cancel) · [Rejstřík: Skill ceiling](../rejstrik.md#skill-ceiling)
