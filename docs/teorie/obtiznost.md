# Obtížnost a výzva: co testuješ a jak moc

Padesátiminutová esej Indie Game Clinic rozsekává dvojici pojmů, které se běžně slévají: **challenge** (kvalitativní — *jaké dovednosti* hra testuje) a **difficulty** (kvantitativní — *jak moc*). Z toho rozlišení padá překvapivě praktická agenda: kdy je ladění obtížnosti předčasné, co jsou bariéry hraní, jak zvedat obtížnost třemi různými cestami — a proč „casual" není urážka, ale technický termín. Případovka Octojump nakonec ukazuje obtížnost jako službu, kterou si hráč dávkuje sám.

---

## Challenge je co, difficulty je kolik

**Zdroj:** [Challenge & Difficulty in Game Design](https://www.youtube.com/watch?v=FLCet4Z7zew) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · ~50 min, esej z profesionální praxe

**Shrnutí:** **Difficulty je otázka „jak moc"** — čísla, slidery, globální proměnná, která přenastaví ostatní [(4:45)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=285s). **Challenge je otázka „co za dovednosti"** — jaký typ myšlení a reakcí hra zkouší [(5:32)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=332s). Vývojáři podle autora řeší chronicky první dřív než druhé — ladí obtížnost hry, u které ještě nevědí, co vlastně testuje.

### Rozpad myšlenky

**Kdy obtížnost vůbec řešit:** balancovací tabulky (autorova první komerční hra měla spreadsheet s limity a prahy exportovaný do CSV [(6:19)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=379s)) patří do produkce. V pre-produkci hledáš, *jaká hra to je* a jestli ji vůbec dělat — „finding the fun" [(13:17)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=797s); ladit difficulty slidery před greenlightem je stavění vodovodu v domě bez základů [(10:58)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=658s). Užitečný nástroj, až čas přijde: **progression currency** — jediná globální proměnná postupu. V autorově Golem Gourmet je to hvězda za každé doručené jídlo [(7:52)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=472s): challenge room za creepy dveřmi se neukáže prvních 30 minut, těžší recepty až od 30 či 60 hvězd — jeden číselník řídí celý onboarding [(9:24)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=564s).

**Bariéry hraní ≠ výzva** [(14:24)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=864s): když hráč zápasí s něčím, co jsi testovat *nechtěl* — barvoslepý s informací kódovanou jen barvou, kdokoli s překombinovaným ovládáním — neměříš obtížnost, měříš překážku. Derek Yu to v knize o Spelunky popsal nezapomenutelně: hráč chtěl „odstranit síť", protože nepřehodil míč — a přitom dostal „raketu s prasklým výpletem" [(15:11)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=911s). **Dokud má hra bariéry, nemá smysl ladit obtížnost** — a nejde ani poznat, jestli výzva baví [(15:57)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=957s).

**Tři páky na goblinech** [(19:33)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=1173s): místnost s pěti gobliny jde ztížit (a) *více stejnými* gobliny — dovednosti se netestují víc, vhodné pro schválně pohodové pasáže; (b) *smrtonosnějšími* gobliny — stávající dovednosti (blok, úhyb) se testují víc; (c) *pestřejšími* gobliny (ranger, mág, healer) — testují se **nové** dovednosti: čtení situace, prioritizace cílů, práce s prostorem [(21:06)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=1266s). Žádná cesta není „správně" — každá je jiný designový záměr. Cesta (c) zvedá **cognitive load** [(22:38)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=1358s): kolik mozku aktivita žere. Učení nové dovednosti je vědomé a drahé (vzpomeň si na první hodiny řízení auta); moc nízká zátěž nudí — onboarding je řízení komplexity vůči fázi učení [(23:24)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=1404s).

> **Pozn.:** K tomu jedna profesní teze, kterou video říká natvrdo: **hraní žánru, který děláš, je pracovní povinnost** [(25:46)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=1546s) — studia na research play alokují čas; „produktivita ≠ hodiny s otevřeným enginem". Design naslepo v žánru, kterému nerozumíš, stojí víc než těch 10–30 hodin hraní. Stejnou tezi z jiné strany říká [empatie fanouškovských komunit](rady-z-praxe.md#rady-nefunguji-tam-kde-zacina-design).

**Souvislosti:** [Zábava a flow](zabava.md) · [Prototypování](prototypovani.md) · [Rejstřík: Cognitive load](../rejstrik.md#cognitive-load) · [Rejstřík: Barrier to play](../rejstrik.md#barrier-to-play) · [Rejstřík: Difficulty curve](../rejstrik.md#difficulty-curve)

---

## Aspirační vs. průběžná obtížnost — a pocity, které z nich rostou

**Zdroj:** [Challenge & Difficulty in Game Design](https://www.youtube.com/watch?v=FLCet4Z7zew) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · stejné video, druhá polovina

**Shrnutí:** Dvě osy, na které jde namapovat skoro každý žánr [(36:46)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=2206s): **průběžná obtížnost** — jak moc tě hra aktivně tlačí k prohře; **aspirační obtížnost** — jak těžké je uspět *dobře* (lepší cesta, víc bodů, volitelná hloubka). Průběžná vyrábí stres a úlevu, aspirační pocit dobře odvedené práce [(42:10)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=2530s) — a volba mixu je volba publika.

### Rozpad myšlenky

**Skill floor a ceiling** [(32:51)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=1971s): floor = minimum, bez kterého nehraješ vůbec (dítě s ovladačem „hraje" jen zdánlivě; komplexita ovládání je floor sama o sobě), ceiling = maximální dosažitelná úroveň. Casual hry mají nízký floor (Wii, touchscreeny); „easy to learn, hard to master" je drahý ideál, ne default [(34:26)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=2066s). Rage hry jdou opačně: úzké pásmo exprese, binární postup/selhání — frustrace je záměr.

**Stupně úspěchu** [(34:26)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=2066s): známky v Hotline Miami, hvězdy v Overcooked = dvě úrovně („dokončit" a „dokončit dobře"). Řeší dvě věci najednou: slabší hráči postupují bez zásek — a vzniká ekonomika návratů (grind hvězd odemyká další obsah), tedy opakování bez „get good" zdi Dark Souls [(35:58)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=2158s). Nejelegantnější příklad aspirační obtížnosti: **jahody v Celeste** [(37:33)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=2253s) — místo hard módu zvoleného předem se hráč rozhoduje **v každém okamžiku**, jestli si dnes troufá na těžší verzi místnosti; flexibilita mezi zvědavostí (chci dál) a completionismem (chci všechno). A hráči si aspirační výzvy vyrábějí i sami: v Golem Gourmet lze položit předmět na tlačítko sýrostroje a automatizovat ho [(39:06)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=2346s) — objevená efektivita je pocit růstu zadarmo.

**Trest jako koření** [(28:53)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=1733s): souls-like corpse run je *dvojitý* trest — ztrácíš nejen čas pokusu, ale i čas investovaný do sběru před ním; Darkest Dungeon má následky špatných rozhodnutí s ocasem 30–40 hodin; Hades ti po smrti nechá část zdrojů, a proto je „roguelite" vnímán přístupněji [(31:58)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=1918s) — každý upgrade zdraví ostatně *snižuje* průběžnou obtížnost. **Casual/hardcore** jsou v průmyslu technické termíny, ne nadávky [(42:57)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=2577s): intuitivní vs. komplikované, přerušitelné vs. náročné na bloky času (pauza, save pointy), non-threatening vs. edgy estetika — a historicky se s designem svezl i tón marketingu (video připomíná nechvalný slogan Daikatany z roku 2000 [(45:15)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=2715s)). Volby obtížnosti provázané s estetikou hráči *dopředu říkají, jaké pocity čekat* — a to je celá pointa: „lidi hrají hry, aby cítili pocity; když nevíš, jaké pocity tvá hra vyrábí, není pro nikoho — a ztrácíš právo si stěžovat" [(46:47)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=2807s).

> **Pozn.:** Osy dávají rychlou mapu žánrů [(40:38)](https://www.youtube.com/watch?v=FLCet4Z7zew&t=2438s): hračky (nic z obojího), bullet hell a akční roguelike (obojí vysoko), Hades kousek pod nimi, cozy simy a idle hry vpravo dole (grind, ale hra tě nezabíjí). Užitečný test vlastního konceptu: kam na téhle mapě míříš — a sedí k tomu tvůj art a tón? Přesně tenhle typ otázky klade i [audit konceptu](../zapisky/gdd-review.md).

**Souvislosti:** [Zábava: jak dostat hráče do flow](zabava.md#jak-dostat-ruzne-zdatne-hrace-do-flow) · [Rejstřík: Aspirační obtížnost](../rejstrik.md#aspiracni-obtiznost) · [Rejstřík: Průběžná obtížnost](../rejstrik.md#prubezna-obtiznost) · [Rejstřík: Skill floor](../rejstrik.md#skill-floor) · [Rejstřík: Skill ceiling](../rejstrik.md#skill-ceiling)

---

## Případovka Octojump: obtížnost jako služba per level

**Zdroj:** [This Puzzle Platformer Has a Unique Approach to Difficulty [Octojump]](https://www.youtube.com/watch?v=IcSD7w-fdJ8) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · ~6 min, stream highlight (feedback na nevydanou hru)

**Shrnutí:** Puzzle platformer s chobotnicí, kde si hráč za nasbíraný inkoust přikoupí skoky navíc nebo delší vznášení — **pro jeden konkrétní level** [(0:47)](https://www.youtube.com/watch?v=IcSD7w-fdJ8&t=47s). Drobná hra, ale učebnicová ukázka, jak se dá obtížnost servírovat jako momentální služba místo globálního režimu.

### Rozpad myšlenky

Proč to funguje lépe než easy mode [(2:08)](https://www.youtube.com/watch?v=IcSD7w-fdJ8&t=128s): „kdyby sis snížení obtížnosti volil jako trvalý stav, lidi by ho nepoužili" — tady level dvakrát zkusíš, řekneš si „nemám nervy", boostneš se, projdeš a **vrátíš se později**. Ego zůstane celé, postup se nezastaví. Přesně mechanismus jahod z Celeste, jen obráceně — místo volitelné vyšší výzvy volitelná nižší. A upgrade dělá level *snazší, ne snadný* [(2:50)](https://www.youtube.com/watch?v=IcSD7w-fdJ8&t=170s): hráč s boostem zrychlí, zpychne a stejně musí hrát.

Tři vedlejší pozorování ze streamu: **duální měna** odděluje pomoc od odměny (inkoust = obtížnostní servis, zelené mince za „poctivé" dokončení = kosmetika [(2:08)](https://www.youtube.com/watch?v=IcSD7w-fdJ8&t=128s)); **téma to celé lepí** — inkoust je schopnost, měna i fikce chobotnice v jednom [(3:37)](https://www.youtube.com/watch?v=IcSD7w-fdJ8&t=217s), viz [ludotematický soulad](ludonarativni-soulad.md); a **vizuální tutoriál** (inkoustové značky se objeví jen, když jsou potřeba, a zase vyblednou [(0:01)](https://www.youtube.com/watch?v=IcSD7w-fdJ8&t=1s)) drží obrazovku čistou. Mechanismus slouží dvěma publikům najednou [(3:37)](https://www.youtube.com/watch?v=IcSD7w-fdJ8&t=217s): hráčům, kteří na hru celkově nestačí, i těm, kteří jen nechytli grif jediného levelu.

**Souvislosti:** [Ludotematický soulad](ludonarativni-soulad.md) · [Případovky designu](pripadovky-designu.md) *(další hry na operačním stole)* · [Zábava: rubber banding](zabava.md#jak-dostat-ruzne-zdatne-hrace-do-flow) · [Rejstřík: Rubber banding](../rejstrik.md#rubber-banding)
