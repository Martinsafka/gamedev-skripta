# Postmortem: tři roky na ShantyTown

Sólo vývojář Eric (Silk Softworks) shrnuje tři roky plné práce na své druhé hře — relaxační stavitelské hře ShantyTown — od výběru prototypu přes designové slepé uličky a shánění peněz až po launch a to, o čem se nemluví: ticho po něm. Postmortemy jsou nejhutnější studijní materiál, jaký gamedev nabízí; tenhle je navíc poctivý v číslech i emocích.

---

## Výběr projektu: tři prototypy, tři váhy

**Zdroj:** [ShantyTown Final Devlog - From Idea to Launch](https://www.youtube.com/watch?v=84biRLlHJMk) · [Silk Softworks](https://www.youtube.com/channel/UCUD1x-oAbmO7N8rPyRRfXsw) · ~29 min, postmortem

**Shrnutí:** Po vydání první hry stál autor bez peněz a potřeboval rychle nový projekt. Místo intuice udělal tabulku: tři prototypy (open-world RPG, real-time tactics karavana, stavitelská hříčka) zvážil podle **feasibility** (zvládnu to?), **marketability** (chce to někdo?) a **fun factoru** (baví to?). Vyhrála hra, u které se testování nedalo rozeznat od hraní.

### Rozpad myšlenky

Tři kritéria [(3:04)](https://www.youtube.com/watch?v=84biRLlHJMk&t=184s) fungují jako filtr proti třem různým smrtím projektu. **Feasibility** [(3:34)](https://www.youtube.com/watch?v=84biRLlHJMk&t=214s): u první hry se autor málem utopil v AI a navigačních systémech, takže tentokrát hledal něco jednoduššího — poučení z vlastních jizev je legitimní designový vstup. **Marketability** [(3:46)](https://www.youtube.com/watch?v=84biRLlHJMk&t=226s): žánr měl čerstvé úspěchy (Tiny Glade, Islanders, Cloud Gardens) a data ukazovala, že je kam růst. **Fun factor** [(3:57)](https://www.youtube.com/watch?v=84biRLlHJMk&t=237s) rozhodl: RPG by bylo dobré, ale ne s omezeným časem a rozpočtem; druhý prototyp byl komplikovaný a otravný na hraní; ShantyTown bavil už jako kostra.

Nejlepší signál celého rozhodování je mimochodná historka [(5:00)](https://www.youtube.com/watch?v=84biRLlHJMk&t=300s): bratr při testování raného prototypu řekl, že si ještě chvíli pohraje — a hrál dál sám od sebe. Když playtester nechce přestat, hra má jádro. Vážit tři kritéria vědomě znamená i umět odložit passion projekt (to RPG), když mu okolnosti nepřejí — odložit není zahodit.

> **Pozn.:** Všimni si pořadí operací: nejdřív tři *prototypy*, pak rozhodnutí. Váhy se přikládají k něčemu hmatatelnému, ne k nápadům na papíře — srovnej s [prototypováním](prototypovani.md).

**Souvislosti:** [Nápad](napad.md) · [Prototypování](prototypovani.md) · [Rejstřík: playtest](../rejstrik.md#playtest)

---

## „Hra ti říká, čím chce být": účel jako designový soudce

**Zdroj:** [ShantyTown Final Devlog - From Idea to Launch](https://www.youtube.com/watch?v=84biRLlHJMk) · [Silk Softworks](https://www.youtube.com/channel/UCUD1x-oAbmO7N8rPyRRfXsw) · stejné video, designová část

**Shrnutí:** Autorova metoda má dvě zásady: vypiluj moment-to-moment gameplay (to, co hráč fyzicky dělá pořád) a všechny ostatní otázky rozhoduj optikou účelu hry. U ShantyTown byl účel „ukázat, jak městská zástavba roste organicky" — a tenhle jediný filtr postupně rozhodl mechaniky, náhodnost, rámec hráčovy role i nejbolestivější škrt.

### Rozpad myšlenky

Moment-to-moment bylo od začátku položit objekt a vybrat další — a bavilo to i v syrové podobě [(7:53)](https://www.youtube.com/watch?v=84biRLlHJMk&t=473s); zbytek designu se hledal. Série experimentů je učebnice sama o sobě: **ekonomika** (kup objekt, vybírej nájem, plať daně) padla jako nudná a otravná [(9:15)](https://www.youtube.com/watch?v=84biRLlHJMk&t=555s). **Adjacency bonusy** vypůjčené z Islanders [(9:35)](https://www.youtube.com/watch?v=84biRLlHJMk&t=575s) padly zajímavěji: ve vertikální, husté zástavbě byly nečitelné a hráči jen vozili kurzorem po mapě za nejvyšším číslem — systém rozhodoval za ně a veškerá rozvaha zmizela. Řešením byla radikální simplifikace [(10:32)](https://www.youtube.com/watch?v=84biRLlHJMk&t=632s): objekty rozdělené do tří kategorií služeb (světlo, utility, dekor) a domy, které si o služby říkají, aby se upgradovaly. Hráč staví kam chce, ale nikdy neztratí vodítko.

Stejná optika rozhodla náhodnost: vážené loot tables dělaly z map guláš, tak je nahradil ručně kurátorovaný balíček karet v polonáhodném pořadí [(12:27)](https://www.youtube.com/watch?v=84biRLlHJMk&t=747s) — mapy šlo skutečně *designovat* a hráč objevuje účel lokace během hraní. A hlavně rozhodla **škrt lidí** [(14:11)](https://www.youtube.com/watch?v=84biRLlHJMk&t=851s): postavičky znamenají animace, pathfinding, kolize, variety jmen, tváří, chování — kaskádu práce [(14:31)](https://www.youtube.com/watch?v=84biRLlHJMk&t=871s) za efekt „hm, milé". Hra je o budovách, ne o lidech — tak se hráč stal vládním zeměměřičem, který čtvrti dokumentuje do složky [(15:34)](https://www.youtube.com/watch?v=84biRLlHJMk&t=934s). Omezení se převléklo za fikci.

> **Pozn.:** „The game tells you what it wants" zní ezotericky, ale je to obyčejná disciplína: pojmenuj účel hry jednou větou a každý spor rozhoduj podle ní. Funguje to i jako obrana proti feature creepu — viz smyčky vs. řetězce, kde podobnou službu dělá otázka „co sytí core loop?".

**Souvislosti:** [Smyčky a řetězce](smycky-a-retezce.md) · [Základy designu: dvě povinnosti hry](zaklady.md) · [Rejstřík: core loop](../rejstrik.md#core-loop)

---

## Kruhy, logaritmický pokrok a systémy, které jen bavilo stavět

**Zdroj:** [ShantyTown Final Devlog - From Idea to Launch](https://www.youtube.com/watch?v=84biRLlHJMk) · [Silk Softworks](https://www.youtube.com/channel/UCUD1x-oAbmO7N8rPyRRfXsw) · stejné video, prostřední léta vývoje

**Shrnutí:** Vývoj hry postupuje logaritmicky: začátek letí a je opojný, pak křivka zplošťuje a týdny práce přestávají být vidět. Přesně v téhle fázi autor „šel rychle nikam" — přepínal art styly, stavěl důmyslné generátory, které pak vyřadil, a naučil se rozeznávat nejzáludnější past sólo vývoje: přesvědčit sám sebe, že důležité je to, co je zábavné dělat.

### Rozpad myšlenky

Logaritmický tvar pokroku [(6:23)](https://www.youtube.com/watch?v=84biRLlHJMk&t=383s) není selhání, je to fyzika vývoje: rané přírůstky (osvětlení, foliage, UI) jsou dramatické, pozdější práce je jemnozrnná a navenek neviditelná. Kdo s tím nepočítá, čte pokles viditelného pokroku jako vlastní neschopnost.

Prostřední fáze ShantyTown je katalog symptomů [(16:13)](https://www.youtube.com/watch?v=84biRLlHJMk&t=973s): opakované tam a zpět s outlines a cel shadingem, dynamické generátory převisů, chodníků a farem — mnohé z toho pro finální hru vyřazené. Diagnóza je vzácně upřímná [(16:45)](https://www.youtube.com/watch?v=84biRLlHJMk&t=1005s): stavěl je, protože *bavilo je stavět*, ne protože hru posouvaly k cíli. Sólo vývojář nemá nikoho, kdo by mu řekl, že na tomhle nezáleží [(16:58)](https://www.youtube.com/watch?v=84biRLlHJMk&t=1018s) — dny řešíš problém, který šlo obejít nebo ignorovat.

Kontrapunkt, aby to nebylo černobílé: rozhodnutí postavit svět za hranicí hratelné plochy [(17:41)](https://www.youtube.com/watch?v=84biRLlHJMk&t=1061s) prodloužilo vývoj minimálně o rok [(18:15)](https://www.youtube.com/watch?v=84biRLlHJMk&t=1095s) — a autor ho zpětně hájí jako skvělou volbu. Ne každá odbočka je plýtvání; rozdíl je v tom, jestli slouží účelu hry (world building a objevování ano, generátor chodníků ne).

A poslední lekce téhle fáze: **sólo neznamená sám** [(19:58)](https://www.youtube.com/watch?v=84biRLlHJMk&t=1198s). Na věci mimo své silné stránky si najal specialisty — capsule art a logo, sound design, lighting, soundtrack na míru, QA. Sólo vývojář je režisér rozpočtu, ne mučedník.

> **Pozn.:** „Bavilo mě to stavět" je pro programátorsky laděné samouky (tj. i pro nás) asi nejnebezpečnější věta v celém videu. Test: kdyby tenhle systém zítra zmizel, všimne si toho hráč prvních dvou hodin?

**Souvislosti:** [Produktivita: žrouti času](produktivita.md) · [Rady z praxe](rady-z-praxe.md)

---

## Wishlisty, Next Fest a ticho po launchi

**Zdroj:** [ShantyTown Final Devlog - From Idea to Launch](https://www.youtube.com/watch?v=84biRLlHJMk) · [Silk Softworks](https://www.youtube.com/channel/UCUD1x-oAbmO7N8rPyRRfXsw) · stejné video, financování a vydání

**Shrnutí:** Byznysová polovina postmortemu: investoři nekousli, hru zafinancovala vládní půjčka; předlaunchový úspěch se měří wishlisty a Steam Next Fest je jejich multiplikátor, který smíš použít jen jednou. A po úspěšném launchi přišlo to, o čem se nemluví — všechno se zastaví a život jde dál.

### Rozpad myšlenky

Peníze: pitch decky pro investory nezabraly — trefil se do post-covidového ochlazení investic — a nakonec hru financovala půjčka od vlády Berlína/Braniborska [(20:54)](https://www.youtube.com/watch?v=84biRLlHJMk&t=1254s); byrokraticky náročná, ale bez nároku na podíl. Evropské regionální programy pro hry reálně existují a stojí za rešerši.

Marketing na Steamu je hra o wishlisty [(21:33)](https://www.youtube.com/watch?v=84biRLlHJMk&t=1293s): pohánějí algoritmus a viditelnost. **Steam Next Fest** [(22:27)](https://www.youtube.com/watch?v=84biRLlHJMk&t=1347s) funguje jako multiplikátor — čím víc wishlistů máš na vstupu, tím víc jich vygeneruje — a každá hra se smí zúčastnit jen jednou. Autor proto dvakrát couvnul (jednou těsně před akcí) a šel tam až napotřetí, po Gamescomu, Tiny Teams a PAX East, s maximem wishlistů na vstupu; jím citované minimum pro smysluplný efekt je ~7 000 [(22:39)](https://www.youtube.com/watch?v=84biRLlHJMk&t=1359s). Druhé prozření: přestat si marketing dělat sám a nechat profesionály převzít otěže [(23:25)](https://www.youtube.com/watch?v=84biRLlHJMk&t=1405s) — publisher udělal trailery, ads a PR, na které by sólo nikdy nedosáhl, a jemu se vrátil čas na hru samotnou.

Launch dopadl dobře: front page Steamu, top 10 % prodejů, 100% pozitivní recenze. A pak pointa celého videa [(24:35)](https://www.youtube.com/watch?v=84biRLlHJMk&t=1475s): launch je nejen stresující, ale i *depresivní* — i ten úspěšný. Tři roky soustředění skončí ze dne na den [(27:01)](https://www.youtube.com/watch?v=84biRLlHJMk&t=1621s) a zbyde jen neodpověditelná otázka, jestli to stálo za to. Autorova odpověď, kterou si z videa odnést [(27:47)](https://www.youtube.com/watch?v=84biRLlHJMk&t=1667s): něco, co jsi vytvořil, mělo pozitivní dopad na cizí život — a to stačí.

> **Pozn.:** Čísla (7k wishlistů, top 10 %) ber jako svědectví jednoho vydání v jednom roce, ne jako věčné konstanty — Steam se hýbe. Mechanismus (wishlisty → algoritmus, Next Fest jednou) je stabilnější než čísla. Marketingu se bude věnovat celé téma „Vydání a marketing" v dalších batchích.

**Souvislosti:** [Proč tvořit](proc-tvorit.md) *(smysl tvorby, když čísla nestačí)* · budoucí téma „Vydání a marketing" · [Rejstřík: wishlist](../rejstrik.md#wishlist) · [Rejstřík: Steam Next Fest](../rejstrik.md#steam-next-fest)
