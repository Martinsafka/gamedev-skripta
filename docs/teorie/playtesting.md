# Playtesting: hra je skutečná až před hráči

Jedno dlouhé video Indie Game Clinic postavené neobvykle: kolem tuctu vývojářů z komunity kanálu vysvětluje vlastní playtestovací postupy — a moderátor je lepí dohromady tezí, že playtesting je výzkum. Nejde o to převzít cizí checklist, ale pochopit zdůvodnění (metodologii) a poskládat si vlastní. Kapitola drží strukturu videa: proč testovat, jak testovat zblízka, jak z testů udělat motor iterace a jak testy škálovat, když hra roste.

---

## Proč testovat: nespolehlivý svědek vlastní hry

**Zdroj:** [The ULTIMATE Playtest Guide](https://www.youtube.com/watch?v=zXNRJuc48Ek) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · ~38 min, hlasy komunity + syntéza

**Shrnutí:** Jako vývojář si z principu neumíš dát zážitek hráče, který hru vidí poprvé — musíš ho získat z druhé ruky. Po měsících na projektu jsi **nespolehlivý pozorovatel**: „hry jsou dokonalé v našich hlavách a v dev prostředí — skutečné jsou až před hráči." A testovat znamená víc než hledat bugy: nejranější playtest validuje, jestli má nápad vůbec publikum.

### Rozpad myšlenky

Základní otázky, na které odpoví jen cizí člověk s ovladačem [(0:49)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=49s): baví to? rozumí tomu? kde se zasekávají? dojdou do konce? A nepříjemná asymetrie [(1:36)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=96s): hra může mít deset skvělých částí — a **pár frustrujících prvků zničí celý zážitek**. Méně čekaný přínos: **motivace** [(2:22)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=142s) — ke své práci jsi přehnaně kritický, a vidět cizí radost („please, can I have more video game?") je palivo, které jinde neseženeš.

**Validace nápadu je první playtest** [(4:43)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=283s). Vývojář z komunity na vlastních vydáních: první hra uspěla skoro bez testování — „měli jsme kliku"; druhá byla totální flop, který zpětně přičítá pozdní validaci [(5:30)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=330s). Klíčový detail: na flop hru **bylo těžké playtestery vůbec sehnat — a to byl sám o sobě red flag** („moc mobilní" pro Steam). Třetí projekt proto validoval obráceně: co nejdřív něco na itch, na Reddit, na YouTube — a teprve zájem a diskuze řekly, že hra má nohy [(6:18)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=378s). Syntéza moderátora: **když testery neseženeš, možná nápad nikoho neláká** [(7:05)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=425s).

**Strach z předčasného testu je obrácené riziko** [(7:05)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=425s): vývojáři odkládají testy, „až bude vize hotová", aby ji feedback nezkazil. Zkušenost říká opak: **vize je mlhavější a tvárnější, než si myslíš, a feedback je brusný kámen, o který se ostří** [(7:51)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=471s). Datové body téhož vývojáře: první hru rok neukázal nikomu → první sekce Metroidvanie se ukázala dlouhá, těžká a bludišťovitá, a předělávat „hotové" bylo zdrcující; na štafetovém jamu naopak nahrával build kamarádům prakticky denně od prvního dne — a za týden měl věc, kterou ostatní vývojáři v řetězu považovali za hotový produkt [(8:38)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=518s).

A rámec, který z „ukážu to lidem" dělá metodu [(3:09)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=189s): každý konkrétní test má mít **cíl** (co v téhle fázi potřebuje validovat — testerů není nazbyt) a z cíle odvozené **indikátory**: co chceš *vidět, že se stane nebo nestane*, nezávisle na tom, co pak tester řekne [(3:57)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=237s). Nejčistší formulace: playtest jako experiment — hypotéza „tenhle moment vyvolá u tohohle typu hráče tuhle emoci/akci" → data → potvrzení; a když se stane něco úplně jiného, je to objev, ne šum [(4:43)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=283s).

> **Pozn.:** Video je sponzorované enginem GameMaker — uprostřed má vyhrazený sponzorský blok [(14:53)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=893s), obsah kolem něj ale sponzora nepropaguje. — „Nespolehlivý pozorovatel" je totéž prokletí, kvůli kterému [mozek je mizerný simulátor her](napad.md#ctyri-zdroje-napadu-a-evaluace-hook-anchor-appeal): prototyp odpovídá na „baví to?", playtest na „baví to *i někoho jiného*?".

**Souvislosti:** [Rady z praxe: the Gap](rady-z-praxe.md#the-gap-rozdil-mezi-to-je-hezky-a-tohle-musim-hrat) · [Scope: malé hry se sčítají](scope.md#male-hry-se-scitaji) *(iteruj s publikem, ne do šuplíku)* · [Produktivita: investice bez validace](produktivita.md#investice-bez-validace-lesteni-systemy-a-optimalizace-predem) · [Rejstřík: playtest](../rejstrik.md#playtest)

---

## Moderovaný playtest: dívej se, co dělají, ne co říkají

**Zdroj:** [The ULTIMATE Playtest Guide](https://www.youtube.com/watch?v=zXNRJuc48Ek) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · sekce o malém testování

**Shrnutí:** Poslat kamarádovi link s prosbou o feedback vrátí „Wow, fun game. Neat." Použitelná data dává **moderovaný playtest**: půl hodiny, kdy se *díváš*, jak člověk hraje — osobně nebo přes videohovor — mlčíš, i když se trápí, a čteš chování místo slov. A protože přihlížení hru mění, doplňuje se to druhým kanálem: širokým testem bez tebe, kde platí jen opakovaná témata.

### Rozpad myšlenky

**Setup je triviální** [(18:44)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=1124s): „dělám hru, hrozně by mi pomohlo dívat se, jak ji někdo hraje — máš příští týden 30 minut?" Osobně, nebo videohovor se sdílenou obrazovkou a zvukem [(19:31)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=1171s); nahrávej. Tester nemusí být vývojář — přátelé a rodina stačí, když z nich umíš dostat data.

**Pravidla vedení** [(20:18)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=1218s): úvodem „neurazíš mě, chci upřímnost"; požádej o **think-aloud** — komentování myšlenek nahlas (chvíli pošťuchuj, návyk naskočí rychle [(21:05)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=1265s)); a hlavně **nezasahuj**: nech je trápit se tutoriálem, i když to bolí — tření je přesně to, co jsi přišel vidět. Zasáhni jen u totálního záseku nebo bugu [(19:31)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=1171s). Výhoda přítomnosti: můžeš kopat přímo v místě tření („právě ukoval meč — jaké to bylo?") — z feedbacku posílaného po hraní by se tahle vteřina nikdy nevynořila [(21:51)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=1311s).

**Čtení chování** [(19:31)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=1171s): osobně vidíš napjatá ramena, těkající oči, zpocené ruce na ovladači; na callu slyšíš nehlídané zvukové reakce; a vždycky vidíš herní chování — bloudí zmateně? čte dialogy? zkouší pohybové mechaniky hned, nebo čeká na dovolení? po smrti to zkusí znovu, nebo hru položí? [(20:18)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=1218s) **Co dělají, přebíjí, co říkají.**

**Druhý kanál: mrak dat** [(21:51)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=1311s): sledovaný hráč hraje jinak (a málokdo ti do očí řekne, že hra nestojí za nic) — proto hru pouštěj i široce, bez sebe. Jednotlivé ohlasy odtud mají nízkou kvalitu (neznáš kontext člověka), ale **opakovaná témata z agregace váží víc než jakýkoli jednotlivý názor** [(22:37)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=1357s). S tím souvisí pravidlo konzistence [(23:24)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=1404s) — historka z komunity: jeden hlas navrhl změnu, vývojář ji implementoval, byla špatně; rada od kamaráda: **jednej jen na feedback, který slyšíš opakovaně — a od lidí, kterým věříš.**

**Briefing rozhoduje o upřímnosti** [(23:24)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=1404s): nejhorší testy jsou ty, kde lidé problémy *vidí a mlčí*, protože hra „vypadá moc hotově, než aby na jejich názoru záleželo". Protilék: dej okatě najevo, že je to prototyp — box na title screenu vysvětlující pre-alphu, schválně ponechané placeholdery a modely bez hlav; nic, co ničí atmosféru, ale stálá připomínka, že projekt je otevřený změnám [(24:11)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=1451s). A někdy testerům neříkej nic: A/B test dvou buildů — puzzle hra řešila, jestli zrušit skok; verze s nízkým skokem sklidila „na co tu je?", ve verzi bez skoku si většina absence ani nevšimla → škrt [(24:59)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=1499s).

Kde brát lidi [(17:11)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=1031s): Discord servery enginů a komunit, game jamy na itch (odevzdané projekty = zlatý důl vzájemného testování) — a vlastní YouTube: i kanál s 83 odběrateli našel testery; publikum devlogů jsou hlavně jiní vývojáři, a **vývojáři jsou skvělí testeři** [(17:58)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=1078s).

> **Pozn.:** „Čti chování, ne slova" je stejný sval jako [the Gap](rady-z-praxe.md#the-gap-rozdil-mezi-to-je-hezky-a-tohle-musim-hrat) — zdvořilé „je to hezký" vs. tester, který si sám řekne o další build. A trik s okázalou nedodělaností je bratranec [ošklivého gameplay prototypu](prototypovani.md#tri-brany-gameplay-prototyp-vertical-slice-produkce): tam ošklivost chrání tebe před zamilovaností, tady testera před zdvořilostí.

**Souvislosti:** [Prototypování: tři brány](prototypovani.md#tri-brany-gameplay-prototyp-vertical-slice-produkce) · [Začátky: sdílení práce](zacatky-bez-zkusenosti.md#sdileni-prace-neni-marketing-je-to-nastroj-uceni) · [Devlogy](devlogy.md) *(kanál jako zdroj testerů)* · [Rejstřík: moderovaný playtest](../rejstrik.md#moderovany-playtest) · [Rejstřík: A/B test](../rejstrik.md#ab-test)

---

## Kadence, vlny a RITE: playtest jako motor iterace

**Zdroj:** [The ULTIMATE Playtest Guide](https://www.youtube.com/watch?v=zXNRJuc48Ek) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · sekce o rytmu a metodách

**Shrnutí:** Kdy testovat? Pravidelně, pořád, znovu — playtest patří do jádra vývojového cyklu jako opakující se rytmus, ne jako událost. Tři konkrétní stroje: pevná kadence (sprint končí testem), třívlnný model (nejdřív 2–3 lidi na očividné problémy, pak masa na vzorce, pak potvrzení oprav) a RITE — rychlá smyčka test → oprava → nový tester.

### Rozpad myšlenky

**Kadence a deadliny** [(9:25)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=565s): udělej z testů součást cyklu — dvoutýdenní sprinty jsou běžné, přizpůsob si délku energii. Vedlejší zisk pro sólo vývojáře: vestavěný deadline. Sám sobě šéfem se termíny vynucují těžko — „v pátek to hraje Katka" funguje líp než „mělo by se" [(10:12)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=612s). A test nehodnotí jen minulý sprint: **říká, co dělat příští** [(12:32)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=752s) — sólo vývojář s milionem front (art, hudba, obsah, marketing) dostane z testu křišťálově jasnou prioritu: společné tření, společnou radost, chybějící obsah [(13:19)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=799s). Moderátorova formulace: designér rozhoduje, co je *důležité* — testeři pomáhají rozhodnout, co je *urgentní* [(14:06)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=846s).

**Tři vlny** (vývojář survival city builderu) [(10:12)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=612s):

1. **2–3 lidi** najdou očividné problémy — „očividné všem kromě mě". Opravit hned, jinak jedna otravnost zabarví všechen další feedback [(10:58)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=658s).
2. **Co nejvíc lidí** — teprve objem umožní vidět **vzorce a opakující se témata** místo názorů jednotlivců [(10:58)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=658s).
3. **Selektivně** — konkrétní kvalitní testeři potvrzují, že opravy sedí; některé problémy padnou až na 3.–5. iteraci [(11:44)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=704s).

Důkaz, že to funguje [(11:44)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=704s): ve druhém kole přišlo mnohem víc feedbacku na late-game features, které se mezi koly *nezměnily* — hráči se k nim díky opravám začátku vůbec poprvé dostali. Dvě pointy z téže zkušenosti: největší dopad testů je na **UX a onboarding** (vlastníma očima netestovatelné); a „hra je moc těžká" často znamená „hráč je zmatený a na výzvu ještě není připravený" — neřeš to zjednodušením [(11:44)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=704s). Plánovací důsledek: úkoly z feedbacku **před** novým obsahem — obsah, který většina hráčů nikdy neuvidí, protože skončí dřív, je mrtvá práce [(12:32)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=752s).

**RITE** — rapid iterative testing and evaluation [(25:46)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=1546s), metoda vypůjčená z UX/web designu, ideální bez velkého poolu testerů: sleduj *jednoho* hráče, zapisuj všechno aspoň trochu pozoruhodné, komunikace na minimu; po sezení projdi poznámky a záznam, **oprav každý vážný problém — a opakuj s novým testerem**, který by na staré problémy už neměl narazit [(26:32)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=1592s). Přesná definice cíle: „RITE nemá udělat hru snadnou *na hraní* — má ji udělat snadnou *na chtění hrát*." Případ z praxe: roguelike chtěl frustraci z omezených zdrojů, ale kouzla na jedno použití dávala jen frustraci (ukovat → jednou seslat → pryč navždy); pár použití místo jednoho = jediná změna, dramaticky lepší přijetí [(27:18)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=1638s).

> **Pozn.:** Extrémní forma kadence je Valve přístup „playtest každý den", který nesl [hru vydanou za měsíc](scope.md#male-hry-v-praxi-hra-na-uceni-a-hra-za-mesic) — tam denní testy dvakrát přestavěly core loop. A „oprav tření dřív, než přidáš obsah" je playtestová verze [investic bez validace](produktivita.md#investice-bez-validace-lesteni-systemy-a-optimalizace-predem).

**Souvislosti:** [Scope: hra za měsíc](scope.md#male-hry-v-praxi-hra-na-uceni-a-hra-za-mesic) · [Plánovací nástroje](planovani-nastroje.md) *(týden playtestů jako závěr měsíčního bloku)* · [Zábava: flow a obtížnost](zabava.md#jak-dostat-ruzne-zdatne-hrace-do-flow) · [Rejstřík: RITE](../rejstrik.md#rite) · [Rejstřík: onboarding](../rejstrik.md#onboarding)

---

## Kdo testuje a jak škálovat: road test před stress testem

**Zdroj:** [The ULTIMATE Playtest Guide](https://www.youtube.com/watch?v=zXNRJuc48Ek) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · sekce o výběru testerů a růstu

**Shrnutí:** Zkušení hráči žánru, nebo úplní nováčci? Odpověď „záleží" dostává strukturu: u každého testera si otevři **okno do subjektivity** (jaké hry miluje a proč), zkušené počítej s předsudky žánru, nováčky čti přes otázky, které kladou. A škáluj po fázích: pár kvalitních očí, pak newsletter, pak veřejná beta jako marketingový beat — „road test before you stress test".

### Rozpad myšlenky

**Okno do subjektivity** [(31:12)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=1872s): zjisti oblíbené hry testera a proč — prozradí jeho primární herní motivace (a jestli se s tvými vůbec protínají) — a nejbližší hry k té tvé, které hrál: to je zkušenost, kterou k tobě přináší.

**Zkušení: jazyk žánru + předsudky k odučení** [(31:58)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=1918s): reprezentují cílovku, ale nesou očekávání. Side-scroll roguelike postavený na reakcích (chytej, odrážej, házej, parry) připomíná Dead Cells a Hades — tak k nepříteli přistoupí a mlátí základním útokem, který je *schválně* slabý. Lekce vývojáře: extra vedení potřebují i veteráni, protože musí přeučit návyky.

**Nováčci: čti jejich otázky** [(32:44)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=1964s): s hratelností se perou, ale feedback míří na art, postavy a příběh — a jejich *otázky* jsou reflektor: ukazují, které háčky narativu táhnou, a **jaké sliby tvůj příběh dává, ať jsi je dát chtěl, nebo ne**. Případ z praxe: anomaly horor pro Steam testovala snoubenka s kamarádem — mobilní hráči bez vztahu k hororu i Steamu; jejich čerstvé oči zlepšily telegrafování věcí, které fanoušek žánru překlikne bez přemýšlení [(32:59)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=1979s).

**Hardcore konec spektra** [(34:18)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=2058s): komunity kompetitivních her mají oddané testery — s postranními motivy: špičkoví hráči **legitimně tají silné věci, které najdou**. Rada z fighting games: high-level hráči nedávají dobré rady — sleduj lidi, kterým věříš, a jejich **chování** (ukážou, jak se hra hraje; co změnit, je tvoje práce) [(35:04)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=2104s).

**Škálování po fázích** [(28:04)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=1684s), příběh jednoho vývojáře na Steamu: friends & family → zájemci z newsletteru (Steam klíče) + **zapnutá analytika** (kam až se hráči dostávají, čeho se dotýkají — bez tvé přítomnosti) [(28:51)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=1731s) → první veřejný test přes Steam playtest feature, **marketovaný jako beta** podle rady Chrise Zukowského: udělej z něj marketingový beat. Vyplatilo se nečekaně — novinář Rock Paper Shotgun zahlédl Reddit posty, napsal článek, přišlo přes tisíc testerů a musel nasadit **waitlist**, aby stíhal opravovat, než mu lidi budou hlásit duplicity [(29:38)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=1778s). Klika — ale bez marketingového rámování by novinář neměl co zahlédnout: „stojí to za to, i když to většinou nikam nevede, protože nikdy nevíš, kdo čte." Po vlně zpátky dolů: uzavřené testy s fokusovanými otázkami (balanc pro hardcore hráče), a až konzistentně pozitivní feedback řekl „čas na demo" [(29:38)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=1778s).

Protipříklad, proč se neškáluje předčasně [(30:25)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=1825s): dedukční hra pozvala najednou 20 lidí z žánrové komunity — a bylo „duše-drtící" slyšet **stejný game-breaking bug dvacetkrát** a nestíhat odpovídat. Závěr vývojáře: v raných fázích stačí dva shodující se hlasy o tom, že něco nefunguje; sto testerů a metriky až po dokončeném slice. **Road test before you stress test.**

Moderátorův závěr [(35:51)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=2151s): playtesting je výzkum — **metoda je způsob, metodologie je zdůvodnění, proč zrovna takhle**; a tu si každý skládá sám podle hry, fáze i vlastních slepých míst. Poslední kalibrace rolí [(37:23)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=2243s): playtest není carte blanche, aby ti hráči řekli, jakou hru máš dělat — jsi expert na svou hru; jenže přesně to expertství je problém: u tutoriálu se vlastní hru nedokážeš odnaučit, u launche zas hardcore testeři najdou exploity, které nevidíš, protože hraješ „správně". Playtest je jediný pohled na hru **bez designérova prokletí znalosti** [(38:09)](https://www.youtube.com/watch?v=zXNRJuc48Ek&t=2289s).

> **Pozn.:** Steam beta jako marketingový beat patří do rodiny beatů ze [Steam stránky](steam-stranka.md) — playtest a marketing tu splývají v jednu událost. A prokletí znalosti je stejný jev, kvůli kterému [první dojem](prvni-dojem.md) testuješ na lidech, ne na sobě.

**Souvislosti:** [Steam stránka](steam-stranka.md) · [První dojem](prvni-dojem.md) · [Sólo vývoj: ukazuj průběžně](solo-vyvoj.md#ukazuj-prubezne-showcase-demo-vertical-slice-launch-bez-skoku-do-tmy) · [Rejstřík: prokletí znalosti](../rejstrik.md#prokleti-znalosti) · [Rejstřík: beta](../rejstrik.md#beta)
