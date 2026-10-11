# Live coding: hudba jako kód

Poslední téma dokumentu jde jinou cestou než zbytek. Nemá DAW, piano roll ani stopy — má **textový editor v prohlížeči, do kterého píšeš vzory** a ony hned hrají. Nástroj se jmenuje **Strudel**, je zdarma, nic se neinstaluje a běží na `strudel.cc`.

Proč je to tady: je to **nejlevnější způsob, jak se dostat ke zvuku**, jaký tenhle dokument popisuje — a zároveň nejrychlejší cesta k ambientní smyčce, prototypu rytmu nebo generativní hudbě do hry. A hlavně staví na věci, kterou programátor už umí: **na vzoru a opakování** místo na notaci.

Kapitola je z výukového workshopu a z videí dvou live coderek, které v tom vystupují. Jedna z nich to shrnuje větou, kterou stojí za to slyšet dřív, než začneš: *„dělat hudbu s kódem není na začátku intuitivní — ale jakmile se naučíš ty malé stavební kostky, jedeš."*

---

## Co je Strudel a proč se učí jinak

**Zdroj:** [WORKSHOP // Coding Music With Strudel](https://www.youtube.com/watch?v=oqyAJ4WeKoU) · [Creative Code Art](https://www.youtube.com/channel/UCVWW3CvU95_1o0Em5H0qZWw) · ~82 min, záznam dvouhodinového workshopu (dva live codeři)

**Shrnutí:** Záznam workshopu pro úplné začátečníky — a je zajímavý ani ne tak obsahem, jako **formou**: první zvuk mají účastníci vydat do tří minut a většina času je vyhrazená na to, aby si zkoušeli sami. Háček, který ten nástroj definuje: **je to jazyk pro vzory, ne pro noty.**

### Rozpad myšlenky

**Co to technicky je** [(7:47)](https://www.youtube.com/watch?v=oqyAJ4WeKoU&t=467s): **Strudel je JavaScriptová verze TidalCycles**, jazyka pro live coding hudby postaveného na Haskellu. Původní TidalCycles vyžaduje instalaci a *„není to nejintuitivnější věc pro začátečníky"*; Strudel běží **v prohlížeči, bez instalace**, v jazyce, který zná mnohem víc lidí. Jedna z lektorek pro to má srozumitelné přirovnání: *„podle mě je Strudel takové p5.js pro live coding."*

**Nejnižší možný práh** je celý pedagogický záměr. Vestavěné zvuky se jmenují tak, jak znějí — `bd` bass drum, `hh` hi-hat, `cp` clap — a jsou to **zkratky z klasických bicích automatů Roland**, takže kdo je zná, je doma hned. Spouští se `Ctrl`+`Enter`, zastavuje `Ctrl`+`.`. A jedna zvláštnost, kterou lektorky rovnou pojmenují jako sporné místo: **hraje vždycky jen poslední spuštěný blok**, takže se hodně komentuje a odkomentovává. *„To je taková nevýhoda Strudelu — nebo taky výhoda, protože je opravdu snadné projíždět kód shora dolů."*

**Kdo tam sedí** [(0:48)](https://www.youtube.com/watch?v=oqyAJ4WeKoU&t=48s) je na téhle myšlence to nejcennější. Jedna z lektorek popisuje sebe takto: *„nemám technické vzdělání ani formální hudební průpravu, jen mě zajímalo obojí."* A dodává, proč jí ta forma přijde tak nosná: *„myslím, že si z live codingu může něco odnést každý — a přesně proto je pro mě tak přesvědčivý, protože je hodně přístupný."*

Mezi vypsanými cíli workshopu je i jeden, který tam podle nich zůstal z minulého běhu, protože ho navrhl někdo z publika: **„překonat trauma z dělání hudby."**

**Odpověď na otázku, kterou položí každý** [(29:58)](https://www.youtube.com/watch?v=oqyAJ4WeKoU&t=1798s) — *„jak se od hraní si dostanu k písničce, když nemám hudební vzdělání?"* — stojí za převzetí celá: *„zkoušet, dokud to nezní dobře, je podle mě skvělý přístup a sama to tak dělám."* A hned k tomu věcné doplnění, které z toho nedělá výmluvu: **v tomhle jazyce je rytmus podstatnější než tóny.** *„Protože je to jazyk pro vzory, je hodně rytmicky založený. Rozumět tomu, jak dělíš rytmus, je opravdu důležité — ale u zvuku je spousta prostoru na zkoumání."*

> **Pozn.:** Za tímhle materiálem stojíme kvůli **hranici vstupu**. Zbytek dokumentu předpokládá aspoň DAW a nějakou představu o notách; tohle nepředpokládá nic a první zvuk je za tři minuty. Pro vývojáře je v tom navíc **domácí terén**: vzory, opakování a funkce jsou to, co dělá celý den — takže **rytmus se dá stavět, i když člověk neumí hudbu**, což je přesně ta polovina, na které stojí [rytmus jako první vrstva](../teorie/game-feel.md). Za pozornost stojí i to, jak je ten workshop stavěný: **skoro žádný výklad, hodně vlastního zkoušení a na konci sdílení**, co kdo udělal. Je to formát, který se dá převzít i mimo hudbu. Vlastní výhrada: *„hraj si, dokud to nezní dobře"* funguje na první smyčku a **přestane fungovat u skladby** — jakmile potřebuješ, aby něco někam směřovalo, dostaneš se zpátky k [aranžmá](aranz.md) a [harmonii](akordy-a-harmonie.md). Live coding tu potřebu neruší, jen ji odkládá.

**Souvislosti:** [Cyklus jako pizza](#cyklus-jako-pizza-mini-notace) · [Zdarma a rychle: nástroje a game jam](nastroje-zdarma-a-game-jam.md) · [Základy hudební teorie](hudebni-teorie-zaklady.md) · [Rejstřík: Live coding](../rejstrik.md#live-coding) · [Rejstřík: Strudel](../rejstrik.md#strudel)

---

## Cyklus jako pizza: mini notace

**Zdroj:** [STRUDEL FOR BEGINNERS](https://www.youtube.com/watch?v=m7Rp46AU8dw) · [Glossing](https://www.youtube.com/channel/UCHrhiATyh5jAMboL2ywGyJQ) · ~46 min, skladba od nuly s výkladem · + [WORKSHOP // Coding Music With Strudel](https://www.youtube.com/watch?v=oqyAJ4WeKoU) · [Creative Code Art](https://www.youtube.com/channel/UCVWW3CvU95_1o0Em5H0qZWw) · ~82 min

**Shrnutí:** Celý jazyk stojí na jedné představě: **cyklus je jeden takt a všechno, co do něj napíšeš, se do něj musí vejít.** Lektorka z workshopu pro to má obrázek, který se drží: *„já si cyklus vždycky představuju jako pizzu."* Napíšeš-li do závorek čtyři věci, rozkrojíš pizzu na čtyři díly. Háček, na kterém začátečník nutně narazí: **vzory zleva doprava určují, jak často se ten vpravo vůbec vzorkuje.**

### Rozpad myšlenky

**Základní stavební kameny** [(6:03)](https://www.youtube.com/watch?v=m7Rp46AU8dw&t=363s), a je jich překvapivě málo:

| zápis | co dělá |
|---|---|
| `$` | anonymní stopa (nezajímá mě, jak se jmenuje) |
| `s("bd")` | přehraj zvuk |
| `*4` | čtyřikrát za cyklus |
| `[a b]` | **rozděl** jednotku času na víc věcí |
| `~` (nebo `-`) | pomlka |
| `!3` | zopakuj třikrát (zkratka) |
| `<a b>` | **střídej po cyklech** (v jednom cyklu `a`, v dalším `b`) |
| `{a b, c d e}` | **polymetr** — dvě řady, každá jinak dlouhá |

Ukázka, jak z toho vzniká house beat: `s("bd*4")` je kopák na každou dobu; `s("[~ sd]*2")` je snare na druhé a čtvrté — *„závorky mi dovolí rozdělit tu půlovou notu na víc věcí, tady na pomlku a snare."*

**Past, kterou je lepší znát dřív, než na ni narazíš** [(20:12)](https://www.youtube.com/watch?v=m7Rp46AU8dw&t=1212s). Napíšeš `s("saw").note("g1 a1")` a čekáš, že se ty dva tóny vystřídají. Nestane se to. Důvod: *„část, která přišla první — zvuk, který jsi ustavila — má převahu a hraje jednou za takt. Když se to dostane k tomuhle, které má víc událostí, jen si z nich vzorkuje podle precedentu, který nastavila ta dřívější část."* Takže se pořád ozve jen první tón.

Léčba je jedna funkce: **`setDefaultJoin('mix')`** (nebo `set.mix` u konkrétního vzoru) — *„udělá to intuitivnější věc, než když tam není."* Autorka to komentuje s tím, že by to vydalo na vlastní video, a doporučuje si to prostě zapamatovat.

**Střídání a jak se z něj stane struktura** [(37:12)](https://www.youtube.com/watch?v=oqyAJ4WeKoU&t=2232s): lomené závorky `< >` prostřídají věci **po cyklech** místo uvnitř cyklu — a když je vydělíš (`/8`, `/16`), stráví v každé variantě víc cyklů. *„Takhle se to obvykle organizuje: nejdřív bas a po osmi taktech přijdou bicí."* Tím se z mini notace stane **skladební nástroj**, ne jen zápis rytmu.

**A dva pomocníci, které se vyplatí zapnout hned**: `_pianoroll` ukáže, jak se vzory překrývají v čase (nejrychlejší způsob, jak vidět, že něco nesedí na takt), a v nastavení **zvýrazňování aktivního řádku a událostí v kódu** — takže je vidět, co zrovna hraje.

> **Pozn.:** Ta pizza je dobrý obrázek, ale ještě užitečnější je pojmenovat, **v čem se ta představa liší od DAW**: v sekvenceru umisťuješ události **na časovou osu**, tady popisuješ **dělení**. Proto se `*4` nechová jako „opakuj čtyřikrát za sekundu", ale jako „rozkroj na čtvrtiny" — a proto se dá rytmus měnit změnou jednoho čísla, aniž bys cokoli přesouval. Nejcennější je ale ta **past s dominancí zleva**, protože je to jediné místo, kde se jazyk chová proti intuici, a je to zároveň důsledek toho, jak je postavený: vzor není seznam, je to **funkce vzorkovaná v čase**. Kdo tohle jednou pochopí, přestane se divit i u složitějších případů. Souvisí to s tím, co dokument popisuje u [rytmu a synkopy](hudebni-teorie-zaklady.md) — jen se to tady dělá odčítáním a dělením, ne psaním not.

**Souvislosti:** [Co je Strudel](#co-je-strudel-a-proc-se-uci-jinak) · [Euklidovské rytmy a řízená náhoda](#euklidovske-rytmy-a-rizena-nahoda) · [Základy hudební teorie](hudebni-teorie-zaklady.md) · [Rejstřík: Polymetr](../rejstrik.md#polymetr) · [Rejstřík: Strudel](../rejstrik.md#strudel)

---

## Euklidovské rytmy a řízená náhoda

**Zdroj:** [Creating Beats & Rhythms in STRUDEL](https://www.youtube.com/watch?v=sefJz9biLCY) · [Switch Angel](https://www.youtube.com/channel/UCmHz7DQbbkcY_UoWY8bBJLw) · ~15 min, technika · + [WORKSHOP](https://www.youtube.com/watch?v=oqyAJ4WeKoU) · [Creative Code Art](https://www.youtube.com/channel/UCVWW3CvU95_1o0Em5H0qZWw) · ~82 min

**Shrnutí:** Autorka staví bicí stopu a otevřeně říká proč: *„naučila jsem se techniky na tvorbu rytmů, které by mě jinak nenapadly."* To je celá pointa téhle myšlenky — **jazyk ti nabídne rytmy, na které bys sám nepřišel.** Dva nástroje k tomu: euklidovské rytmy a **řízená** náhoda. Háček u toho druhého: **náhoda, kterou nezkrotíš, je k ničemu, protože se nedá zopakovat.**

### Rozpad myšlenky

**Euklidovské rytmy** [(3:37)](https://www.youtube.com/watch?v=sefJz9biLCY&t=217s) se zapisují dvěma čísly: `(4,16)` znamená **rozprostři čtyři hity co nejrovnoměrněji do šestnácti kroků**. Změníš první číslo na pět nebo sedm a dostaneš úplně jiný groove, aniž bys cokoli umisťoval.

A historka za tím, kterou vypráví workshop [(40:41)](https://www.youtube.com/watch?v=oqyAJ4WeKoU&t=2441s), je nečekaně dobrá: algoritmus vznikl **ve fyzice** kvůli otázce, jak v daném časovém okně poslat částice tak, aby byly co nejvíc rozestoupené. *„A když to udělali, zjistili, že to odpovídá spoustě populárních rytmů v hudbě mnoha různých kultur."*

**Tři způsoby, jak zapsat, kde co padne** — a stojí za to je znát všechny, protože se hodí v jiných situacích:

- **`struct("1 0 1 1")`** — jedničky a nuly, tedy hit a ticho. Nejblíž step sekvenceru.
- **`beat("4 11 16")`** — *„divide cycle into 16 parts, just like a 16-step drum sequencer"* a řekni, na kterých krocích to má hrát. Nejlepší, když **přesně víš**, jak to má znít.
- **`(n,k)`** — euklidovský, když **nevíš** a chceš objevovat.

**Řízená náhoda** je druhá polovina a má tři nástroje. **`sometimesBy(0.1, ply(2))`** zdvojí událost v desetině případů (trapové hi-haty). **`?`** za zvukem znamená „polovinu času". **`degrade(0.6)`** naopak **odebere** 60 % událostí.

**A funkce, kvůli které je ta náhoda použitelná** [(7:52)](https://www.youtube.com/watch?v=sefJz9biLCY&t=472s): **`ribbon`**. *„Představ si celý běh času jako stuhu — můžeš z ní vystřihnout kus a ten pořád dokola opakovat."* Napíšeš, od kterého cyklu a jak dlouhý úsek, a náhodné rozhodnutí, které se ti líbilo, se stane **stabilním motivem**. Konkrétně u ní: náhodný výběr vzorku kopáku (`n(irand(5))`) je *„skoro až moc náhodný"*, dokud se stuhou nevystřihne dvoucyklová smyčka — a je z toho pattern, který se dá hrát dokola.

**Dvě drobnosti navrch, které dělají rozdíl:**

- **Groove posunutím z mřížky**: `beat("7.2 ...")` místo `7` — *„teď je to o kousínek posunuté z mřížky"*, a robotický beat začne dýchat.
- **Slider místo čísla**: do `degrade()` se dá vložit posuvník od 0 do 1, takže se **hustota bicích ovládá živě při vystoupení**. Na začátku skladby řídce, s rostoucí energií hustěji.

> **Pozn.:** Nejcennější je tady **`ribbon`**, protože řeší obecný problém generativní tvorby: **náhoda je levný zdroj nápadů a mizerný zdroj skladby.** Vystřižením a zacyklením úseku se z jednorázového překvapení stane materiál, se kterým se dá pracovat — a je to táž myšlenka jako [seed u procedurální generace](../teorie/algoritmy-prehled.md): **náhodu, kterou umíš zopakovat, můžeš vybírat.** Pro hry je to přímo použitelné: generativní ambientní hudba, která se neopakuje a přesto drží charakter, je přesně tohle. Za pozornost stojí i ta věta o rytmech, na které by autorka sama nepřišla — je to argument, který platí i mimo hudbu: **nástroj, který nabízí jiný prostor možností, není jen jiný způsob téhož.** A vlastní výhrada k euklidovským rytmům: jsou návykové a **znějí po chvíli poznatelně** — jako všechno, co má úzký prostor. Dobré na základ, ne na všechno.

**Souvislosti:** [Cyklus jako pizza](#cyklus-jako-pizza-mini-notace) · [Zvuk, efekty a modulace](#zvuk-efekty-a-modulace) · [Základy hudební teorie](hudebni-teorie-zaklady.md) · [Přehled algoritmů](../teorie/algoritmy-prehled.md) · [Rejstřík: Euklidovský rytmus](../rejstrik.md#euklidovsky-rytmus) · [Rejstřík: Synkopa](../rejstrik.md#synkopa)

---

## Zvuk, efekty a modulace

**Zdroj:** [STRUDEL FOR BEGINNERS](https://www.youtube.com/watch?v=m7Rp46AU8dw) a [You Can Modulate ANYTHING in Strudel](https://www.youtube.com/watch?v=11frBA9L638) · [Glossing](https://www.youtube.com/channel/UCHrhiATyh5jAMboL2ywGyJQ) · ~46 + 31 min

**Shrnutí:** Rytmus je půlka; druhá je, **jak to zní**. Strudel má vestavěné bicí automaty, oscilátory a sound fonty, umí nahrát vlastní vzorky a má celý signálový řetězec od filtrů po sidechain. Kapitola je průchod tím, co se používá pořád — a jedna past, která zničí celou skladbu, dokud se nezná. Háček: **dlouhý vzorek se ve výchozím stavu spustí každý cyklus znovu a překrývá se sám se sebou.**

### Rozpad myšlenky

**Odkud brát zvuky** [(1:20)](https://www.youtube.com/watch?v=m7Rp46AU8dw&t=80s): vlastní vzorky se nahrají přes nastavení — **složka se stane jménem, které píšeš do `s()`**, podsložky jsou banky. Autorka na to nedělá vědu: *„napsala jsem pad a bass drum do Splice a vzala prvních deset od každého."* Vestavěné jsou k dispozici klasické bicí automaty, oscilátory (`saw`, `square`, `pink`) a **sound fonty** — *„to jsou ty zvuky, jaké se používaly ve starých videohrách."* Konkrétní vzorek z banky vybere `n(3)`.

**A ta past** [(10:57)](https://www.youtube.com/watch?v=m7Rp46AU8dw&t=657s), kterou autorka označí jako věc, na které se sama opakovaně spálila: **u dlouhých vzorků piš `clip(1)`.** Bez toho Strudel nechá vzorek dohrát celý **a zároveň ho spustí znovu každý takt** — takže se ti pětiminutová stopa začne vrstvit sama na sebe.

**Signálový řetězec**, ve zkratce:

- **`gain` proti `postgain`** — první je na začátku řetězce, druhý na konci. *„Radši používám postgain, protože to znamená, že to nepřebije věci jako zkreslení."*
- **`lpf` (low-pass)** s `lpenv` (obálka — mocnina dvou, o kolik se filtr otevře) a `lpq` (rezonance, *„pro víc acidový zvuk"*).
- **`room`** je reverb, **`delay`** ozvěna; obě berou hodnotu 0–1 jako množství poslané do efektu.
- **ADSR** přímo na zvuku: `decay(0.05)` udělá z hi-hatu těsnější hit.

**Sidechain, který se nejmenuje sidechain** [(13:39)](https://www.youtube.com/watch?v=m7Rp46AU8dw&t=819s): dá se na **orbitu** (skupinu vzorů sdílejících efekty) a pak se z kopáku zavolá **`duck`** s číslem té orbity. `duckattack` řídí, jak dlouho zůstane stažené — *„nula se okamžitě vrátí nahoru, jedna to drží dole pořád; 0,3 dá pěkné pumpování do beatu."*

**Vzorek neznámé délky** [(36:32)](https://www.youtube.com/watch?v=m7Rp46AU8dw&t=2192s) je nejpraktičtější trik celé kapitoly. Máš loop a nevíš, kolik má taktů. Postup: **hádej mocninu dvou** (`/2`, `/4`, `/8`) a přidej **`fit`**. Zní-li to zběsile, je to natlačené do málo času — zkus víc taktů. Zní-li to moc pomalu a nízko, zkus míň. *„Nakonec si vybereš dva z nich a trefíš se."*

**Modulace** [(0:23)](https://www.youtube.com/watch?v=11frBA9L638&t=23s) je ve Strudelu nezvykle pohodlná: napíšeš `.lfo()` a **modulátor se sám podívá, co stojí před ním** — je-li to `s()`, moduluje frekvenci; je-li to `lpf()`, moduluje mez filtru. Nastavuje se objektem, ne řetězem funkcí, a autorka to komentuje prakticky: *„nemusíš je znát všechny. Je jich hodně. Doporučuju je používat, jen když tě to baví a když to slouží zvuku, o který ti jde. Hodně se dá udělat i s LFO úplně bez konfigurace."*

Ze všech parametrů stojí za znalost tři: **`depth`** je ve výchozím stavu **relativní** (o polovinu hodnoty nahoru a dolů) a dá se přepnout na absolutní · **`dc`** posouvá modulaci nahoru nebo dolů, takže jde modulovat jen jedním směrem · a **`sync`** naváže LFO na cyklus, takže **sedí na beat**. *„Někdy je zajímavé, když LFO s ostatními prvky v čase není — dá to tomu život. Ale chceš-li to přesně synchronní, použij sync."*

> **Pozn.:** Nejužitečnější položka je nenápadná: **`clip(1)`**. Je to přesně ten typ chyby, který [selže mlčky](../praxe/pamet-a-instance.md#drobky-sest-zasahu-na-jedno-odpoledne) — nic nespadne, jen se to postupně mění v kaši, a začátečník hledá chybu ve špatném místě. Za pozornost stojí i to, jak je nástroj postavený kolem **odhadu místo přesnosti**: „hádej mocninu dvou a poslouchej" je v DAW nemyslitelný postup (tam se koukneš na délku vzorku), tady je to nejrychlejší cesta. Je to obecnější vlastnost live codingu — **rychlá zpětná vazba nahrazuje přesnou informaci**, a stojí za to vědět, kdy je ten obchod výhodný. A jedna vlastní poznámka k modulaci: rada *„používej to, jen když tě to baví"* zní jako úhyb, a přitom je to nejlepší věta o parametrech vůbec. **Nástroj s padesáti parametry nepotřebuje, abys jich znal padesát** — potřebuje, abys věděl, které tři řeší tvůj problém.

**Souvislosti:** [Euklidovské rytmy a řízená náhoda](#euklidovske-rytmy-a-rizena-nahoda) · [Od smyčky k vystoupení](#od-smycky-k-vystoupeni) · [Syntéza zvuku od nuly](synteza-zvuku.md) · [Sound design ve hře](sound-design-ve-hre.md) · [Rejstřík: LFO](../rejstrik.md#lfo) · [Rejstřík: Sidechain](../rejstrik.md#sidechain) · [Rejstřík: ADSR](../rejstrik.md#adsr)

---

## Od smyčky k vystoupení

**Zdroj:** [STRUDEL DLC](https://www.youtube.com/watch?v=jKkmzWmIyfs) · [Glossing](https://www.youtube.com/channel/UCHrhiATyh5jAMboL2ywGyJQ) · ~14 min · + [STRUDEL FOR BEGINNERS](https://www.youtube.com/watch?v=m7Rp46AU8dw) · ~46 min · + [WORKSHOP](https://www.youtube.com/watch?v=oqyAJ4WeKoU) · [Creative Code Art](https://www.youtube.com/channel/UCVWW3CvU95_1o0Em5H0qZWw) · ~82 min

**Shrnutí:** Poslední kus je o tom, co se stane, když smyčka funguje: **jak z ní udělat skladbu a jak ji hrát před lidmi.** Rozdíl proti DAW je zásadní — kód se mění **za běhu**, takže „aranžmá" a „vystoupení" jsou tady totéž. Háček, který se z toho dá odnést i mimo hudbu: **nástroj, ve kterém se tvoří a hraje současně, tlačí ke stavbě vlastního nářadí.**

### Rozpad myšlenky

**Skladba jako vrstvení a řízení hlasitosti**. Postup, který je v obou videích stejný: přidej vrstvu, sóluj ji (`_` před jménem stopy), doťukej ji, přidej další. Když se to začne rvát, přijde jeden řádek na všechno: `all(x => x.postgain(0.7))` — *„pro každý vzor vezmi jeho postgain a vynásob ho ještě sedmi desetinami."*

Sekce se dělají tím, co už kapitola zná: **lomené závorky vydělené počtem taktů** (`<a b>/8`) a komentování bloků. A jeden trik na dynamiku, který stojí za převzetí [(44:17)](https://www.youtube.com/watch?v=m7Rp46AU8dw&t=2657s): **filtr navázaný na to, kdy hraje zpěv** — když vokál přijde, zavře se pad na 200 Hz, aby se nervaly; když nehraje, otevře se na 2 800.

**Malý trik, který dělá zvuk plným** [(42:54)](https://www.youtube.com/watch?v=m7Rp46AU8dw&t=2574s): `add(note("0,0.3"))`. Čárka je ve Strudelu **stack** — rozdělí vzor na dva. Jeden zůstane, druhý se rozladí o třetinu půltónu, a dohromady to dá **rozladěný unisono**. *„Jedna větev existence, kde se nestalo vůbec nic, a pak ta Schrödingerova, kde jsem to rozladila."*

**Živé hraní** [(0:53)](https://www.youtube.com/watch?v=jKkmzWmIyfs&t=53s) přidá dvě věci. **MIDI klávesy** se připojí jedním řádkem (`await midiKeys(...)`) a hraje se jimi zvuk, který sis nadefinoval. A pak **`scribe`**, který *„přepíše všechny noty, které jsi právě zahrála, do MIDI notace"* — tedy zahraješ frázi rukama a **dostaneš ji jako kód**, který můžeš dál upravovat. Ke `scribe` se zadává, jak dlouho nahrávat a na co kvantizovat.

**A funkce, která ukazuje, čím se live coding liší** [(6:22)](https://www.youtube.com/watch?v=jKkmzWmIyfs&t=382s): **`move`** moduluje parametr, který stojí před ní, **nezávisle na rytmu hlavního vzoru** — napíšeš průběh čísel a ta se plynule vyhladí. Takže se dá živě rozjet zkreslení nebo FM přes několik taktů, aniž bys sáhl na pattern. *„A ta čísla se ti automaticky vyhladí, takže to neskáče."*

**Vlastní nářadí jako norma**: autorka má **vlastní knihovnu skriptů** (kolem 1 900 řádků), kterou nahraje jedním `await import` — a jsou v ní funkce, které si napsala, protože je při hraní potřebovala: kompaktnější zápis akordů, `chorus`, lo-fi `dust`, ghost sidechain (ducking, jako by tam byl kopák, i když tam není) a proměna MIDI kontroleru v bicí pad.

**A poslední věc, kterou má smysl vzít z workshopu** [(6:13)](https://www.youtube.com/watch?v=oqyAJ4WeKoU&t=373s): jeho poslední půlhodina je vyhrazená na to, aby účastníci pustili, co udělali. *„Je to nejúžasnější část toho workshopu — vidíme, co jste vytvořili, a můžeme na to shora jamovat."*

> **Pozn.:** Nejzajímavější je na téhle myšlence to, že **hranice mezi nástrojem a dílem je propustná**. Autorčina knihovna skriptů není vedlejší produkt — je to **její nástroj i její styl** zároveň, protože ty funkce určují, co je při hraní snadné, a tedy co bude hrát. Je to táž věc, jakou knihovna popisuje u [nástrojů, které si napíšeš pro sebe](../godot/projekt-a-vykon.md#nastroje-pro-sebe-editor-script-ktery-ti-usetri-boilerplate) a u [toho, jak nástroj tvaruje level](../teorie/level-design-solo.md#nastroj-tvaruje-level-co-udela-editor-s-tvym-designem) — jen dotažená dál, protože tady se to nářadí mění **během vystoupení**. Pro herní použití je z celé kapitoly nejpřenositelnější **`scribe`**: zahraješ nápad rukama a dostaneš ho jako data, se kterými se dá pracovat — což je přesně to, co v hudbě pro hry chybí nejčastěji, protože **generativní hudba potřebuje motiv, ne jen pravidla**. A vlastní výhrada: všechno v téhle kapitole je vázané na nástroj, který se **rychle mění** (část funkcí je na testovací doméně, část je autorčina vlastní). Ber to tedy jako mapu možností, ne jako referenci — ta je v dokumentaci Strudelu a bude aktuálnější.

**Souvislosti:** [Zvuk, efekty a modulace](#zvuk-efekty-a-modulace) · [Deset minut na track](#deset-minut-na-track-casovany-beh) · [Aranžmá z loopu](aranz.md) · [Tvorba herního soundtracku](tvorba-soundtracku.md) · [Godot: nástroje pro sebe](../godot/projekt-a-vykon.md#nastroje-pro-sebe-editor-script-ktery-ti-usetri-boilerplate) · [Rejstřík: Live coding](../rejstrik.md#live-coding) · [Rejstřík: Seamless loop](../rejstrik.md#seamless-loop)

---

## Deset minut na track: časovaný běh

**Zdroj:** [this tutorial is 10 minutes long.](https://www.youtube.com/watch?v=7GcSgrJRcIw) · [Glossing](https://www.youtube.com/channel/UCHrhiATyh5jAMboL2ywGyJQ) · ~31 min, nesestříhaný záznam s deseti minutami na hodinách

**Shrnutí:** Autorka si dá **deset minut čistého času** a postaví z nich track — s běžícím odpočtem, bez střihu, včetně slepých uliček. Je to nejužitečnější věc v celé kapitole, protože to není výklad funkcí, ale **záznam rozhodování**: co se dělá první, kdy se přestane hledat a co se prostě nechá být. Háček: **to, co ji zdrží nejvíc, není kód — je to výběr zvuku.**

### Rozpad myšlenky

**Pořadí je pevné a stojí za převzetí** [(0:42)](https://www.youtube.com/watch?v=7GcSgrJRcIw&t=42s): tempo a žánr → kopák → snare → hi-haty → bas → akordy → lead → perkuse a ozdoby. Rozhodnutí *„udělám UKG, tedy 133 BPM"* padne v první minutě a všechno další už se jen doplňuje do rámce.

**Kde se ztrácí čas** [(2:33)](https://www.youtube.com/watch?v=7GcSgrJRcIw&t=153s): skoro dvě minuty z deseti stráví hledáním kopáku. Jeden je moc, druhý je *„úplně opačný konec spektra"*, a nakonec to uzavře větou, která by měla viset nad každým sample browserem: *„tenhle je poslední, co zkusím — jinak prostě vezmeme devět set devítku."* **Předem stanovený strop na hledání** je celý ten trik; bez něj se v knihovně vzorků dá strávit celý večer.

**Layerovaný bas** [(7:59)](https://www.youtube.com/watch?v=7GcSgrJRcIw&t=479s) je jediná složitější stavba, kterou v tom limitu udělá, a je to použitelný recept: **sub** (skoro čistý, jen s trochou vyšších harmonických přes `partials`) plus **mid bas** (unison, mírné rozladění, horní propust na 200 Hz, aby nelezl subu do cesty). Nad tím LFO na filtru s `dc 0`, aby modulace šla **jen nahoru**.

**Náhoda, ale zafixovaná** [(25:34)](https://www.youtube.com/watch?v=7GcSgrJRcIw&t=1534s) — přesně to, co [popisuje předchozí myšlenka](#euklidovske-rytmy-a-rizena-nahoda), tady vidíš v běhu: náhodné panorama, náhodný delay, náhodný útok filtru, všechno zaseknuté do **dvoutaktové stuhy** (`rib`). Dvě věci navrch: **`wchoose`** dává jednotlivým možnostem **váhu** (takže „většinou nic, občas výrazný útok") a **`perlin` na jiném semínku** dá plynulý náhodný pohyb, který **nekoreluje** s ostatními náhodami — proto se panorama nehýbe zároveň s filtrem.

**Drobnost na ladění náhody** [(18:42)](https://www.youtube.com/watch?v=7GcSgrJRcIw&t=1122s), kterou by nikdo nevymyslel dopředu: uvozovky kolem jedné z možností, které nic nedělají — *„můžeš některé dát do uvozovek úplně zbytečně, aby bylo poznat, kdy vybírá právě je."* Zvýrazňování v editoru je pak označí a ty **vidíš**, kdy padla ta varianta.

**A dvě věty o tom, co se s výsledkem smí** [(30:23)](https://www.youtube.com/watch?v=7GcSgrJRcIw&t=1823s): hotový track vyvěsí ke stažení a k licenci řekne jen tolik — *„nevydávejte to jako svoje a nedávejte to AI, jinak si dělejte, co chcete."*

> **Pozn.:** Nejsilnější je na tom ta **časová tíseň jako výukový nástroj**. Deset minut zabrání tomu, co začátečníka nejvíc brzdí — donekonečna vylepšovat první osm taktů — a vynutí rozhodnutí, která se jinak odkládají. Je to táž mechanika jako [design by constraint](../teorie/scope.md#design-by-constraint-krabice-napred-napad-dovnitr): **limit není překážka, je to filtr na to, co je opravdu nutné.** Za pozornost stojí i to, že se z toho dá udělat **vlastní cvičení bez ohledu na nástroj**: deset minut na smyčku v DAW, na blockout levelu, na prototyp mechaniky. A jedna vlastní výhrada k té formě: video je poctivé v tom, že *deset minut skládá*, ale trvá půl hodiny — **odpočet se pauzuje**, kdykoli se mluví. Neber ten limit jako doklad rychlosti nástroje, ale jako **cvičení na rozhodnost**.

**Souvislosti:** [Od smyčky k vystoupení](#od-smycky-k-vystoupeni) · [Euklidovské rytmy a řízená náhoda](#euklidovske-rytmy-a-rizena-nahoda) · [Zdarma a rychle: nástroje a game jam](nastroje-zdarma-a-game-jam.md) · [Aranžmá z loopu](aranz.md) · [Rejstřík: Game jam](../rejstrik.md#game-jam) · [Rejstřík: Strudel](../rejstrik.md#strudel) · [Rejstřík: Sidechain](../rejstrik.md#sidechain)
