# Případovka: systémy a progrese

Nejsilnější designová kapitola případovky, protože se v ní řeší otázka, kterou má každá hra s odměnami a málokdo ji vysloví: **jak odměnit hráče za těžkou výzvu, aniž bys mu zlehčil zbytek hry?** Hráč, který na tu výzvu stačil, totiž posílení nepotřebuje — a ten, kdo ho potřebuje, se k odměně nedostane.

K tomu tři menší, ale velmi praktické věci: proč hráči udělají to, co vede k výhře, i když je to nudné; kde mají čísla v počítači tvrdé meze; a dvě drobnosti, které si hráč všimne dřív než čehokoli jiného.

---

## Odznaky: odměna, která nezlehčí hru

**Zdroj:** [Creating a Game-Changing Badge System for my Indie Game! | Devlog](https://www.youtube.com/watch?v=KtbNdDWi30k) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~37 min, devlog · + [Game Dev Secrets: How to handle Rewards?](https://www.youtube.com/watch?v=tgczIVACFXI) · týž kanál · ~1 min

**Shrnutí:** Problém je formulovatelný ve dvou větách: **za těžkou výzvu chceš dát silnou odměnu, jenže hráč, který ji zvládl, sílu nepotřebuje** — a když mu ji dáš, znehodnotíš mu zbytek hry. Odznaky ten spor řeší elegantně: **odznak dělá silnějším, ale slotů je omezený počet**, takže nový odznak něco jiného vytlačí. *„Hráč má pocit, že zesílil, a opravdu dostal víc možností — ale striktně vzato silnější není."* Háček, který z toho dělá víc než trik: **odznak je zároveň nejlevnější přístupnostní nástroj, jaký hra může mít.**

### Rozpad myšlenky

**Diagnóza** [(2:29)](https://www.youtube.com/watch?v=KtbNdDWi30k&t=149s) je nepříjemná právě tím, jak je jednoduchá. Těžká výzva vyžaduje mistrovství, tak ji chceš odměnit. Jenže *„hráč, který potřebuje něco silnějšího, je ten, co tu výzvu porazit neumí"*. Dáš-li sílu tomu, kdo ji nepotřebuje, buď mu **znehodnotíš pozdější výzvy**, nebo musíš zbytek hry ztížit — a pak se ten, kdo se trápil na začátku, **nikdy nedostane dál**.

**Alternativy bez posílení** shrnuje minutový klip [(0:02)](https://www.youtube.com/watch?v=tgczIVACFXI&t=2s) a stojí za převzetí jako seznam: **odhalení příběhu** (místnost za bossem s deníkem), **kosmetika** (jiný oblek, alternativní hudba, sada zvuků, skiny) a **další výzvy** (klíč, který odemkne jiný těžký souboj). Autor je ale k sobě upřímný, proč mu to nestačí [(3:16)](https://www.youtube.com/watch?v=KtbNdDWi30k&t=196s): *„dostat něco, co tě posílí, je prostě mnohem lepší pocit. Vím, že si tím vlastně beru výzvu — a stejně to miluju."*

**Odznaky jako řešení sporu** [(4:03)](https://www.youtube.com/watch?v=KtbNdDWi30k&t=243s): odměna **je** posílení, ale **rozpočet slotů je pevný**. Za novou schopnost tedy vždycky něco obětuješ. Výsledkem je *„hezká rovnováha: dáváš hráčům možnosti, odměňuješ je za zdolané výzvy — a neznehodnocuješ zbytek hry."* Inspirace je přiznaná: Hollow Knight a Paper Mario, kde se navíc rozpočet slotů dá při postupu zvětšovat, takže vzniká **další volba** (víc života, víc many, nebo víc místa na odznaky?).

**Odznaky jako přístupnost** [(10:14)](https://www.youtube.com/watch?v=KtbNdDWi30k&t=614s) je ta část, kterou by šlo přehlédnout a je nejcennější. Autor navazuje na *assist mode* z Celeste a navrhuje **odznaky, které by běžně byly příliš silné** — víc života, míň poškození, delší vznášení — dostupné po zapnutí režimu pomoci. Argumentuje konkrétně a bez povýšenosti: *„někdo prostě nezvládá mačkat útok dost rychle na to, aby porazil bosse v rozumném čase. Když si nasadí odznak na trojnásobné poškození, je pro něj hra najednou férová vzhledem k tomu, co dokáže."* A přidává rozdíl, na kterém záleží: **není to posuvník obtížnosti**. *„Nedáváš mu ‚hraju na easy a nemám nad tím kontrolu' — dáváš mu kontrolu nad obtížností, což je podle mě přístupnější."* Táž mince má i druhou stranu — odznaky, které hru **ztíží** (umřeš po jednom zásahu) pro ty, co si o to řeknou.

**Jak se odznaky získávají** [(30:27)](https://www.youtube.com/watch?v=KtbNdDWi30k&t=1827s) uzavírá kruh k [mapě](pripadovka-level-a-mapa.md#mapa-metroidvanie-data-pohled-a-jedine-misto-pravdy): skrytí bossové a schovaná místa za rozbitnými zdmi. A drobnost, která se cení: **popisek odznaku nese kus lore**, takže je odměna i vyprávěním.

> **Pozn.:** Táž logika stojí za autorovým rozhodnutím o **vylepšeních brnění** z jiného devlogu [(12:30)](https://www.youtube.com/watch?v=HsWnv6rCiJ4&t=750s): odmítá „vylepšení, které sníží utrpěné poškození o 50 %" slovy *„bude to silné a bude to dobrý pocit, ale není to zajímavé"*, a chce místo toho **další možnosti pohybu a boje** — dvojskok, backdash, nabíjený útok. Princip za obojím se dá vyslovit jednou větou: **odměňuj rozšířením rozhodovacího prostoru, ne posunutím čísel.** Nové možnosti hráče nezlehčí hru, protože se s nimi musí naučit pracovat; větší čísla ji zlehčí vždycky. Souvisí to i s [obtížností jako aspirační versus průběžnou](../teorie/obtiznost.md) a s tím, proč [Celeste má assist mode](../teorie/game-feel.md#celeste-krivky-v-snimcich-a-hrst-tichych-ulev) místo snadné obtížnosti.

**Souvislosti:** [Rychlé ladění je designový nástroj](#rychle-ladeni-je-designovy-nastroj) *(jak se ty odznaky testují)* · [Obtížnost a výzva](../teorie/obtiznost.md) · [Systémy a mechaniky](../teorie/systemy-a-mechaniky.md) · [Engineering experiences](../teorie/engineering-experiences.md) *(rozhodnutí a balanc)* · [Rejstřík: Assist mode](../rejstrik.md#assist-mode) · [Rejstřík: Skill ceiling](../rejstrik.md#skill-ceiling)

---

## Rychlé ladění je designový nástroj

**Zdroj:** [Creating a Game-Changing Badge System for my Indie Game! | Devlog](https://www.youtube.com/watch?v=KtbNdDWi30k) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~37 min, devlog

**Shrnutí:** Systém odznaků je autoload s jedním uzlem na odznak a všemi daty v inspektoru. Zní to nezajímavě, dokud si nevšimneš, co to umožnilo: **změnit číslo a okamžitě to zahrát**, bez sahání do kódu. Díky tomu autor v jednom sezení prototypuje sedm odznaků, dva zavrhne a **u jednoho zjistí, že je zajímavý až po tom, co ho zkusil**. Háček, který stojí za zapamatování: tři z těch odznaků byly „rychleji X" a všechny tři byly nudné — **nuda se nepozná v návrhu, pozná se ve hře**.

### Rozpad myšlenky

**Jak je to postavené** [(7:54)](https://www.youtube.com/watch?v=KtbNdDWi30k&t=474s): scéna `badge system` je autoload; každý odznak je uzel s poli (název, popis, cena v bodech, ikona, **hodnota**). Kdekoli v kódu se pak dá zeptat *„je tenhle odznak aktivní, a jakou má hodnotu?"* — takže odznak na rychlejší útok znamená jednu podmínku v útočném kódu. Přidat odznak = přidat uzel.

**Proč na tom záleží**, je vidět na ladění [(17:15)](https://www.youtube.com/watch?v=KtbNdDWi30k&t=1035s). Autor nastaví dvojnásobnou rychlost útoku, zahraje si, je to moc — a **místo aby to snížil, zkusí trojnásobek**, protože ho to nic nestojí: *„je to doslova otevřít systém odznaků, změnit jedno číslo, a ve hře to hned funguje s novou hodnotou."* Trojnásobek vypadá skvěle a je nepoužitelný, načež se ustálí na **1,25×** s poznámkou *„nejsem si jistý, ale o čtvrtinu rychlejší útok je slušné."* Bez rychlé smyčky by udělal jeden pokus a šel dál.

**A při tom ladění vypadne pozorování, které by v návrhu nevzniklo** [(18:48)](https://www.youtube.com/watch?v=KtbNdDWi30k&t=1128s): při trojnásobné rychlosti *„je fakt těžké mačkat dost rychle na to, abys stihl okno comba"*, takže combo pořád vypadává a opakuje se první rána. **Zvýšení rychlosti útoku tedy paradoxně combo znesnadní** — a to je přesně ten druh zjištění, který se dá získat jen hraním.

**Tři nudné a jeden zajímavý.** Autor sám pojmenuje, kde se to zaseklo [(21:56)](https://www.youtube.com/watch?v=KtbNdDWi30k&t=1316s): *„rychlejší útok, rychlejší běh, rychlejší dash — začínalo to být trochu zatuchlé, moc podobné, nudné."* Tak zkusil něco jiného: **štít, který se dobije po chvíli bez zásahu** a pohltí příští ránu. Ten popisuje úplně jinak — *„funkčně se mi ten odznak fakt líbí"* — a všímá si proč: **neodměňuje sílu, ale to, že se hráč umí vyhýbat**. Rozdíl mezi nudnými a zajímavým je jasný: nudné mění **číslo**, zajímavý mění **způsob hraní**.

**A dvě poctivá přiznání**, která z devlogu dělají použitelný materiál. Zaprvé [(13:25)](https://www.youtube.com/watch?v=KtbNdDWi30k&t=805s): *„nevím, jestli se některý z těchhle odznaků dostane do finální verze"* — prototypuje **systém**, ne obsah. Zadruhé o jednom z nich rovnou řekne, že je *„hloupý, k čemu vlastně je"*, a u vznášení dojde k tomu, že *„je to příliš silné na odznak a ještě by to potřebovalo vlastní animaci — spíš by to mělo být vylepšení brnění."* To je funkční kritérium: **věc, která potřebuje vlastní animaci, už není drobná úprava.**

> **Pozn.:** Ta rychlá smyčka je nejpřenositelnější věc kapitoly a stojí za samostatné vyslovení: **cena jedné iterace určuje, kolik nápadů vyzkoušíš.** Trvá-li úprava minutu, zkusíš dvacet variant; trvá-li půl hodiny, zkusíš dvě — a rozdíl v kvalitě výsledku není v talentu, ale v počtu pokusů. Přesně proto se vyplatí [datová vrstva](resources.md#data-ven-ze-skriptu-skript-ridi-chovani-resource-popisuje-co-ta-vec-je) a [nástroje pro sebe](projekt-a-vykon.md#nastroje-pro-sebe-editor-script-ktery-ti-usetri-boilerplate). Za zmínku stojí i vedlejší efekt, který autor jmenuje: systém odznaků slouží zároveň jako **ladicí přepínače** — rychlejší nebo pomalejší postava se dá zapnout odznakem místo psaní debug kódu. To je táž myšlenka jako [god mode](projekt-a-vykon.md#nastroje-pro-sebe-editor-script-ktery-ti-usetri-boilerplate), jen postavená z existujícího systému.

**Souvislosti:** [Odznaky](#odznaky-odmena-ktera-nezlehci-hru) · [Data ven ze skriptu](resources.md#data-ven-ze-skriptu-skript-ridi-chovani-resource-popisuje-co-ta-vec-je) · [Nástroje pro sebe](projekt-a-vykon.md#nastroje-pro-sebe-editor-script-ktery-ti-usetri-boilerplate) · [Prototypování: iterační spirála](../teorie/prototypovani.md#iteracni-spirala-ke-stredu-nevede-rychly-pruh) · [Rejstřík: Iterace](../rejstrik.md#iterace)

---

## Pobídky: hráč udělá to, co vede k výhře

**Zdroj:** [Game Dev Secrets: Risks and Rewards!](https://www.youtube.com/watch?v=pwUKx1WDsm0) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~1 min

**Shrnutí:** Autor chtěl, aby hráči hráli agresivněji, tak přidal **regeneraci života**. Výsledek byl přesný opak: hráči začali **stát a čekat**, až se doléčí, protože to byla nejjistější cesta k výhře. Věta, kterou si z minuty odnes: **hráči udělají to, co jim dá nejvyšší šanci vyhrát, i když je to nebaví.**

### Rozpad myšlenky

**Záměr a výsledek** [(0:02)](https://www.youtube.com/watch?v=pwUKx1WDsm0&t=2s): riskování je zábava, ale **přimět hráče riskovat je překvapivě těžké**, protože o tom rozhodují pobídky. Regenerace života měla znamenat „nemusíš hrát opatrně, život se vrátí". Znamenala ale *„stůj a čekej, až budeš mít plný život, než cokoli uděláš"* — a to je nuda.

**Mechanismus je obecný** a autor ho formuluje ostře: *„je-li něco nízkorizikové a vysoce výnosné, stane se z toho výchozí nejlepší volba a vysaje to ze hry zábavu."* A tvrdší varianta: *„existuje-li strategie na zaručenou výhru, něco skutečně bezrizikového, tvoji hráči to budou dělat — i když jim to hru zkazí."*

**Praktický dopad**: než něco do hry přidáš, zeptej se ne „co to dělá", ale **„k čemu to hráče motivuje"**. To jsou dvě různé otázky a odpověď na druhou je často nečekaná — jako v tomhle případě, kde funkce navržená pro agresivitu vyrobila pasivitu.

> **Pozn.:** Tohle je [degenerativní strategie](../rejstrik.md#degenerate-strategy) v miniatuře — dominantní taktika, která vytlačí ostatní a přitom není zábavná. Knihovna má tentýž mechanismus popsaný u [rozhodnutí a balance](../teorie/engineering-experiences.md#rozhodnuti-balanc-a-yomi-hra-v-hlave-hrace) a u [obtížnosti](../teorie/obtiznost.md); zajímavé na téhle verzi je, že problém **nevznikl špatným balancem čísel**, ale špatně zvoleným *tvarem* mechaniky. Regeneraci nešlo „doladit" — jakákoli regenerace za stání odměňuje stání. Řešení, ke kterým se sahá jinde, mění tvar: regenerace **jen v pohybu**, **jen po zásahu nepřítele** (agrese se léčí), nebo **omezený počet nabití**. Všechny tři dělají totéž — **berou odměnu za nicnedělání**.

**Souvislosti:** [Odznaky](#odznaky-odmena-ktera-nezlehci-hru) *(týž problém u odměn)* · [Engineering experiences: rozhodnutí a balanc](../teorie/engineering-experiences.md#rozhodnuti-balanc-a-yomi-hra-v-hlave-hrace) · [Obtížnost a výzva](../teorie/obtiznost.md) · [Rejstřík: Degenerate strategy](../rejstrik.md#degenerate-strategy) · [Rejstřík: Yomi](../rejstrik.md#yomi)

---

## Čísla mají meze: overflow a nepřesnost floatů

**Zdroj:** [Game Dev Secrets: Becoming a Billionaire?](https://www.youtube.com/watch?v=NZSJ7n2Ix0A) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~2 min · + [Game Dev Secrets: NUMBER GO UP](https://www.youtube.com/watch?v=kaRyRRHF-5o) · týž kanál · ~2 min

**Shrnutí:** Dvě chyby, které vypadají jako kouzla, dokud nevíš, jak jsou čísla v počítači uložená. **Integer overflow**: nasbíráš přes 2,1 miliardy mincí a stav se **překlopí do velkého záporného čísla**. **Nepřesnost floatů**: odejdeš dost daleko od počátku souřadnic a postava se začne třást, propadat podlahou a nereagovat. Obě mají tutéž příčinu — **konečný počet bitů** — a obě tentýž lék: **drž čísla malá, nebo použij větší typ.**

### Rozpad myšlenky

**Overflow** [(0:49)](https://www.youtube.com/watch?v=NZSJ7n2Ix0A&t=49s): celé číslo je uložené ve 32 bitech, z nichž **jeden nese znaménko** a zbylých 31 se sčítá jako mocniny dvou. Přeteče-li součet přes to, co jde 31 bity vyjádřit, *„počítač vesele překlopí ten poslední bit a číslo se stane záporným."* Odtud ta hranice **2,1 miliardy** — a odtud i řešení: **omez maximum**, které hráč může nasbírat, aby se ke stropu ani nepřiblížil, **nebo použij víc bitů**.

**Nepřesnost floatů** [(0:49)](https://www.youtube.com/watch?v=kaRyRRHF-5o&t=49s) je zajímavější, protože se neprojeví jako přetečení, ale jako **postupný rozpad fyziky**. Autor to vysvětluje mechanikou formátu (a s vtipem o „temné radě početních vládců", který zakrývá, že jde o standard z roku 1985): první bit je znaménko, dalších osm je **exponent** — určí, mezi kterými mocninami dvou číslo leží — a zbylých 23 je **mantisa**, která říká, **kolik kroků po tom rozsahu se má udělat**.

A tady je ta pointa: **velikost kroku roste s velikostí čísla**. U malých čísel je rozsah malý, kroky jemné a přesnost vysoká. U velkých čísel je rozsah široký, **kroky hrubé** — a mantisa už na přesnou hodnotu nedosáhne, takže se zastaví dřív, nebo ji překročí. Ve hře to vypadá takhle [(0:02)](https://www.youtube.com/watch?v=kaRyRRHF-5o&t=2s): *„postava se třese sem a tam, wall jumpy nefungují, občas se prostě zaseknu při chůzi, náhodně jde pozpátku nebo se teleportuje do podlahy."*

**Praktický důsledek** stojí za vyslovení, protože ho video jen naznačí: **nedělej nekonečné světy tak, že hráč jde pořád dál od počátku.** Řešení, která se používají jinde, mění souřadnou soustavu, ne přesnost — svět se **posouvá kolem hráče** (origin shifting), nebo se dělí na dlaždice s vlastním lokálním počátkem.

> **Pozn.:** Obě chyby patří do rodiny „hra funguje, dokud nepřekročíš práh", a to je nejnepříjemnější typ chyby vůbec — **testování je nenajde**, protože v testu se do těch čísel nedostaneš. Proto se vyplatí znát meze dopředu: 32bitové celé číslo končí kolem **2,1 miliardy**, 32bitový float ztrácí celočíselnou přesnost už kolem **16 milionů**. Kdo dělá inkrementální hru nebo cokoli s velkými čísly, potká to první; kdo dělá otevřený svět, to druhé. Zajímavé je, že autor obě videa staví jako **výklad formátu**, ne jako recept — a má pravdu, protože bez pochopení, *proč* to nastane, se práh neodhadne.

**Souvislosti:** [Delta a physics process](prvni-hra.md#delta-a-physics-process-proc-se-rychlost-nasobi-casem) *(kde se ta nepřesnost projeví nejdřív)* · [Programátorské myšlení: hodnota vs. reference](../teorie/programatorske-mysleni.md#hodnota-vs-reference-kopie-nebo-listecek-s-sipkou) · [Matematika pro gamedev](../teorie/matematika-pro-gamedev.md) · [Rejstřík: Integer overflow](../rejstrik.md#integer-overflow) · [Rejstřík: Boolean](../rejstrik.md#boolean)

---

## Dvě drobnosti, které hráč pozná: přemapování a psací stroj

**Zdroj:** [Game Dev Secrets: Keybindings?](https://www.youtube.com/watch?v=b9pl67ZbhX8) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~1 min · + [Game Dev Secrets: An Easy Dialogue Fix!](https://www.youtube.com/watch?v=b_4pEe4chfs) · týž kanál · ~1 min

**Shrnutí:** Dvě věci, které nikdo nepochválí a všichni si jich všimnou, když chybí. **Nastavení nepatří do save souboru** — patří do **samostatného souboru preferencí**, protože přežívá napříč hrami. A **efekt psacího stroje** se nedělá přidáváním písmen, ale **odkrýváním už zalomeného textu**, jinak slova během čtení poskakují na další řádek.

### Rozpad myšlenky

**Přemapování a kde ho uložit** [(0:01)](https://www.youtube.com/watch?v=b9pl67ZbhX8&t=1s). Autor přidal před playtestem hrubé menu na přemapování kláves — a narazil na to, že se nikam neukládá, takže se musí nastavovat po každém spuštění. Nabízí se dát ho do save souboru **a je to špatně**, a jeho argument je nečekaný a přesný: *„zkazilo by to hru speedrunnerům."* Dosud bindingy žily v paměti, takže vydržely, dokud hráč hru nezavřel. V save souboru by se **při každé nové hře smazaly**, takže *„každý pokus o speedrun by začínal speedrunem nastavování kláves."* Změna by tu otravnost jen **přesunula** z načítání na začátek nové hry.

Řešení je **soubor preferencí** — samostatný, mimo save, **nezávislý na průchodu hrou**. Patří tam ovládání, zvuk, grafika a konfigurace gamepadu. A autor přidává hezkou poznámku o tom, co všechno se tam dá schovat: *„nebo, jsi-li jako Toby Fox, si tam uložíš drobnosti o dřívějších rozhodnutích hráče a použiješ je, abys s ním v dalších průchodech vymrdal."*

**Přemapování je navíc bezpečnostní síť**, kterou hra potřebuje z důvodu, o kterém [má sekce vlastní myšlenku](gdscript.md#kdyz-bug-neni-v-kodu-keyboard-ghosting): u některých kombinací kláves **levné klávesnice prostě jeden vstup zahodí**, a proti tomu neexistuje jiná obrana než nechat hráče kombinaci změnit.

**Psací stroj a zalamování** [(0:02)](https://www.youtube.com/watch?v=b_4pEe4chfs&t=2s). Text, který se objevuje po písmenech, působí líp než text, který naskočí najednou — jenže má vadu, kterou autor přesně pojmenovává: **zalamování řádků se přepočítává za chodu**, takže slovo, které právě čteš, **skočí na další řádek**. *„Zní to jako drobnost, a přitom je to při hraní překvapivě rušivé."*

Oprava je obrácení postupu: **vlož do rámečku celý text hned**, ale s **neviditelnými písmeny**. Zalomení se tím spočítá dopředu a **nic už nemůže skočit jinam**; pak se jen odkrývají znaky po jednom. A protože je to častý problém, engine to řeší přímo — textový node má **vlastnost pro počet viditelných znaků**, takže *„žádné programování navíc"*.

> **Pozn.:** Obě věci mají společné, že **náklad chyby nese hráč a autor ji nevidí**. Vývojář si klávesy nepřemapovává (zná je) a dialog čte pomalu (psal ho), takže obojí projde. Odhalí to teprve [playtest](pripadovka-proces.md#playtester-najde-problem-ne-reseni) — a i tam spíš jako nespokojenost než jako hlášení. Praktické zobecnění: **cokoli, co hráč dělá jednou za spuštění hry, si zaslouží zvlášť opatrné zacházení**, protože se to při vývoji dělá tisíckrát a zvyk otupí. Ta hranice mezi save souborem a preferencemi je navíc táž otázka jako u [persistence keys](pripadovka-level-a-mapa.md#persistence-key-svet-ktery-si-pamatuje): **co patří k průchodu hrou a co k hráči.**

**Souvislosti:** [Když bug není v kódu: keyboard ghosting](gdscript.md#kdyz-bug-neni-v-kodu-keyboard-ghosting) *(proč je přemapování nutnost, ne komfort)* · [Persistence key](pripadovka-level-a-mapa.md#persistence-key-svet-ktery-si-pamatuje) *(co patří k průchodu a co k hráči)* · [Ukládání v UE](../praxe/ukladani.md#save-system-ktery-prezije-druhy-projekt-struktury-interface-a-async) · [Kontejnery a UI](ui-control.md#kontejnery-90-ui-jsou-ctyri-nody) · [Rejstřík: Input buffering](../rejstrik.md#input-buffering) · [Rejstřík: SaveGame objekt](../rejstrik.md#savegame-objekt)
