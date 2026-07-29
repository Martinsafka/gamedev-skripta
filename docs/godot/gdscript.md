# GDScript

GDScript se dá popsat jako „Python pro hry" a bude to napůl pravda. Užitečnější je číst ho jako **sadu rozhodnutí o tom, kolik bezpečnosti si za kolik psaní koupíš**: typovat, nebo netypovat; volat přímo, nebo poslat signál; nacpat data do slovníku, nebo si na ně udělat třídu. Jazyk ti nechá obojí a nechá to na tobě.

Kapitola proto není referenční příručka syntaxe — tu má oficiální dokumentace a je dobrá. Je to výběr rozhodnutí, která se špatně mění zpětně. Na konci je bonus: jeden bug, který v kódu není a stejně tě bude stát odpoledne.

---

## Gradual typing: kolik bezpečnosti si koupíš

**Zdroj:** [How to program in Godot - GDScript Tutorial](https://www.youtube.com/watch?v=e1zJS31tr88) · [Brackeys](https://www.youtube.com/channel/UCYbK_tjZ2OrIZFBvU6CCMiA) · 58 min, tutoriál

**Shrnutí:** GDScript je **gradually typed** — typy jsou volitelné a můžeš je přidávat po jedné proměnné. To vypadá jako pohodlí a je to spíš past: dynamický zápis je rychlejší napsat, ale chyby vyplavou až za běhu a je pomalejší. Statický zápis je o dvě slova delší a **chyby hlásí, aniž bys hru spustil**. Háček, který se v tutoriálech nedozvíš: existuje třetí varianta `:=`, která typ odvodí a je pořád statická — takže „nechci psát typy" přestává být argument.

### Rozpad myšlenky

**Výchozí stav je dynamický** [(16:33)](https://www.youtube.com/watch?v=e1zJS31tr88&t=993s): `var health = 100` a `var is_alive = true` se zakládají úplně stejně a **typ se dá kdykoli přepsat na jiný**. Autor to shrnuje férově: *rychlé na psaní a flexibilní, protože můžeš libovolně přiřadit data jiného typu — ale náchylnější k chybám a méně výkonné než statické typování.*

**Tři způsoby zápisu, tři různé ceny:**

| zápis | typ | kdy se chyba pozná |
|---|---|---|
| `var damage = 15` | dynamický | za běhu, možná až u hráče |
| `var damage: int = 15` | statický, explicitní | v editoru, před spuštěním |
| `var damage := 15` | statický, odvozený | v editoru, před spuštěním |

Ten třetí řádek je ta zajímavá věc [(16:49)](https://www.youtube.com/watch?v=e1zJS31tr88&t=1009s): Godot pozná, že 15 je celé číslo, a proměnnou **staticky** nastaví na `int`. *Výsledek je přesně stejný* jako u explicitního zápisu — přiřadit do ní později řetězec je chyba.

**Typovat jde i funkce** [(21:19)](https://www.youtube.com/watch?v=e1zJS31tr88&t=1279s): parametry stejnou dvojtečkou a **návratový typ šipkou** `-> int`. Tím se funkce stane smlouvou, kterou editor vynucuje.

**Konstanty jsou samostatná kategorie** [(17:36)](https://www.youtube.com/watch?v=e1zJS31tr88&t=1056s): `const GRAVITY = -9.81` se nedá přepsat vůbec, a konvence je psát je velkými písmeny. A `@export` [(17:36)](https://www.youtube.com/watch?v=e1zJS31tr88&t=1056s) proměnnou vystaví do inspektoru — hodnota ve skriptu se stane výchozí a v editoru se dá přenastavit pro každou instanci zvlášť, s tlačítkem na návrat k default hodnotě.

**Scope je místo, kde začátečníci chybují nejčastěji** [(13:52)](https://www.youtube.com/watch?v=e1zJS31tr88&t=832s): proměnná deklarovaná uvnitř `if` existuje jen uvnitř toho `if`. Chceš-li ji všude ve skriptu, patří nahoru, mimo funkce.

**A pak jsou tu tiché pasti při převodu typů** [(15:28)](https://www.youtube.com/watch?v=e1zJS31tr88&t=928s). Casting z celého čísla na řetězec (`str(x)`) potřebuješ pokaždé, když skládáš text z čísel. Opačným směrem je to horší: **`int(3.9)` je 3, ne 4** — převod desetinné čárky na celé číslo *usekává, nezaokrouhluje*. To je klasický zdroj chyb o jedničku a stojí za to si ho zapamatovat dřív, než na něj narazíš v počítání skóre.

> **Pozn.:** Rada „typuj od začátku" zaznívá napříč celým Godot playlistem — nezávisle ji dávají [oba autoři beginner průvodců](zaklady.md#co-si-prinest-nez-otevres-editor) i Brackeys. Sluší se ale dodat, co se z videí nedozvíš: **gradual typing má smysl právě proto, že se dá nasadit postupně.** Nemusíš přepsat celý projekt naráz; vyplatí se typovat nejdřív **hranice** — parametry a návratové typy funkcí, `@export` proměnné, veřejné API komponent — protože právě tam se chyby předávají mezi částmi kódu. Vnitřek krátké funkce typovat nemusíš, tam si chybu najdeš i tak.

**Souvislosti:** [Od tří parametrů k jednomu objektu](#od-tri-parametru-k-jednomu-objektu-vlastni-trida-jako-datovy-kontrakt) *(typování povýšené na návrh)* · [Pořádek jako nástroj](#poradek-jako-nastroj-hlavicka-skriptu-a-inspektor) *(kde v hlavičce co bydlí)* · [Co si přinést, než otevřeš editor](zaklady.md#co-si-prinest-nez-otevres-editor) · [Programátorské návyky](../teorie/programatorske-navyky.md#patnact-malych-navyku-tri-mechanismy) *(návyky, které mají tentýž mechanismus)* · [Rejstřík: Gradual typing](../rejstrik.md#gradual-typing) · [Rejstřík: GDScript](../rejstrik.md#gdscript)

---

## Call down, signal up: kdo koho smí znát

**Zdroj:** [How to program in Godot - GDScript Tutorial](https://www.youtube.com/watch?v=e1zJS31tr88) · [Brackeys](https://www.youtube.com/channel/UCYbK_tjZ2OrIZFBvU6CCMiA) · 58 min, tutoriál

**Shrnutí:** Signál je zpráva, kterou node vyšle do prázdna — **odesílatel neví, kdo ji poslouchá**, a přesně to z něj dělá nástroj na rozpojování závislostí. Kolem signálů stojí zdejší pravidlo palce: **volej dolů, signalizuj nahoru.** Rodič smí volat funkce na dětech, dítě se nemá dožadovat rodiče přímo — má vyslat signál a nechat rodiče rozhodnout. Sourozenci se propojují přes společného rodiče.

### Rozpad myšlenky

**Mechanismus** je jednoduchý [(40:18)](https://www.youtube.com/watch?v=e1zJS31tr88&t=2418s): node má signály (vestavěné i vlastní), na signál se připojí funkce a při vyslání se **zavolají všechny připojené naráz**. Vlastní signál se deklaruje řádkem `signal leveled_up` a vysílá `leveled_up.emit()` [(42:41)](https://www.youtube.com/watch?v=e1zJS31tr88&t=2561s). Připojit se dá myší v editoru nebo kódem — `leveled_up.connect(_on_leveled_up)`, a `disconnect()` stejně snadno [(43:28)](https://www.youtube.com/watch?v=e1zJS31tr88&t=2608s). Signály **umí nést parametry**, takže se s událostí posílá i kontext (dosažená úroveň, nová hodnota života).

**Kontext problému** ilustruje autor příkladem, který zná každý [(41:53)](https://www.youtube.com/watch?v=e1zJS31tr88&t=2513s): postava získá level. Aktualizovat se musí UI, statistiky hráče, možná kouzla a achievementy. Kdyby to všechno řídil hráč, vznikne z něj rozcestník, který zná půlku hry. Se signálem hráč jen **oznámí, že se něco stalo**, a systémy se připojí samy. Autorova formulace stojí za zapamatování: *button vůbec netuší, které funkce jsou na signál připojené — jen řekne emit.* To je decoupling v jedné větě.

**Pravidlo „call down, signal up"** [(55:12)](https://www.youtube.com/watch?v=e1zJS31tr88&t=3312s) z toho dělá použitelnou heuristiku pro celý strom scény. Rodič je nad dítětem, takže **rodič smí volat funkce na dítěti**. Opačně ne — dítě má vyslat signál a rodič se rozhodne, co s tím. Analogie z videa je názorná (a autor sám ji uzavírá poznámkou, že jde o radu pro kód, ne pro výchovu): rodiče můžou dětem říkat, co dělat; děti signalizují potřeby a rodič volí další krok.

**Sourozenci** — dva nody na téže úrovni — jsou zajímavější případ [(56:47)](https://www.youtube.com/watch?v=e1zJS31tr88&t=3407s): **propojení dělá společný rodič**, obvykle ve `_ready()`. Ani jeden ze sourozenců tedy o tom druhém nemusí vědět; ví to jen ten, kdo je oba vlastní. Tím se drží platné to, co dělá strom čitelným — **závislosti kopírují hierarchii**.

**Getters a setters** patří do téže rodiny, protože dovolí navěsit chování na změnu proměnné [(44:17)](https://www.youtube.com/watch?v=e1zJS31tr88&t=2657s). Kanonický příklad je život: setter hodnotu **ořízne do rozsahu** (`clamp(value, 0, 100)`) a rovnou **vyšle signál `health_changed`**. Volající kód pak jen přiřadí `health = -150` a nemusí nic hlídat — ořez i notifikace se stanou samy. Gettery se používají spíš na převody: `chance_pct` počítaný z `chance * 100` je vždycky konzistentní, protože není uložený, ale odvozený.

> **Pozn.:** Pro člověka z Unrealu je mapování téměř doslovné: **signál ≈ event dispatcher**, a pravidlo „call down, signal up" je zdejší, tvrdší formulace téhož, co v UE stojí za volbou mezi [interfacem a dispatcherem](../praxe/komunikace-blueprintu.md#interface-nebo-dispatcher-a-kolik-doopravdy-stoji-cast). Godot má oproti UE výhodu, že strom scény je **jediná hierarchie** — v Unrealu se orientace „nahoru/dolů" ztrácí mezi levelem, actorem a komponentou. A rozdíl mezi „nejčastější chybou začátečníků" [popsanou u Unrealu](../praxe/komunikace-blueprintu.md#observer-pattern-nejcastejsi-chyba-zacatecniku-a-jeji-oprava) a tímhle textem je jen v názvosloví: [observer pattern](../teorie/design-patterns.md#strategy-a-observer-dva-vzory-ktere-v-ue-pouzivas-denne) je totéž, co Godot zabudoval přímo do nodů.

**Souvislosti:** [Nody a scény](zaklady.md#nody-a-sceny-strom-ktery-je-zaroven-architekturou) *(strom jako komunikační topologie)* · [Komunikace Blueprintů: observer pattern](../praxe/komunikace-blueprintu.md#observer-pattern-nejcastejsi-chyba-zacatecniku-a-jeji-oprava) *(týž vzor v UE)* · [Design patterns: strategy a observer](../teorie/design-patterns.md#strategy-a-observer-dva-vzory-ktere-v-ue-pouzivas-denne) *(teoretické pozadí)* · [Principy architektury: volné vazby](../praxe/principy-architektury.md#tri-principy-skalovatelnosti-separace-volne-vazby-data) · [Rejstřík: Signal](../rejstrik.md#signal) · [Rejstřík: Call down, signal up](../rejstrik.md#call-down-signal-up) · [Rejstřík: Loose coupling](../rejstrik.md#loose-coupling)

---

## Od tří parametrů k jednomu objektu: vlastní třída jako datový kontrakt

**Zdroj:** [Maximize Your Game Development Potential with Classes in Godot (class_name is OP)](https://www.youtube.com/watch?v=y3faMdIb2II) · [Bitlytic](https://www.youtube.com/channel/UCOlPBtGeh1YGL_rWpOLgLyg) · ~5 min, tutoriál · + [How to program in Godot - GDScript Tutorial](https://www.youtube.com/watch?v=e1zJS31tr88) · [Brackeys](https://www.youtube.com/channel/UCYbK_tjZ2OrIZFBvU6CCMiA) · 58 min, tutoriál

**Shrnutí:** Funkce `damage(amount)` vypadá nevinně, dokud k ní nepřidáš odhoz a pozici útoku. Pak musíš parametry doplnit **do každé implementace**, včetně stromu a bedny, které o odhozu nechtějí vědět — a když je nedoplníš, hra spadne. Oprava je jedna třída: **udělej z parametrů objekt**. Nová vlastnost útoku se pak přidá na jednom místě a nic ostatního se nemusí měnit. Háček, kvůli kterému to není jen kosmetika: `class_name` z toho udělá **typ**, který editor umí napovídat a vynucovat.

### Rozpad myšlenky

**Kontext problému** je ukázkový příklad křehkého API [(0:47)](https://www.youtube.com/watch?v=y3faMdIb2II&t=47s). Ve hře je zbraň, která volá `damage()` na všem, do čeho trefí. Přidání odhozu znamená dva nové parametry — sílu a pozici útoku. Kráva je použije, jenže **strom a bedna mají tutéž funkci a ty parametry teď musí přijmout taky**, jinak hra při zásahu spadne [(1:33)](https://www.youtube.com/watch?v=y3faMdIb2II&t=93s). Autor je v hodnocení poctivý: u malého projektu, kde se `damage()` nebude měnit, je to úplně v pořádku. *Ale představ si dvacet skriptů, které s tou funkcí dělají různé věci* — pak je každá změna signatury dvacet zásahů.

**Mechanismus** je krátký [(2:21)](https://www.youtube.com/watch?v=y3faMdIb2II&t=141s): nový skript `attack.gd`, první řádek `class_name Attack`, uvnitř tři proměnné (`attack_damage`, `knockback_force`, `attack_position`). Funkce se změní na `damage(attack: Attack)`. Zbraň si objekt sestaví a předá; příjemci si vytáhnou, co potřebují.

**Dva zisky z anotace typem**, které autor jmenuje výslovně [(2:21)](https://www.youtube.com/watch?v=y3faMdIb2II&t=141s): **našeptávání** (napíšeš `attack.` a editor nabídne, co objekt umí) a **záruka**, že funkci nikdo nepředá něco jiného — jinak chyba.

**Důkaz, že to opravdu odstranilo tu bolest** [(3:07)](https://www.youtube.com/watch?v=y3faMdIb2II&t=187s): autor přidá do třídy `stun_time`, upraví nepřítele a zbraň — a **stromu ani bedny se nedotkne**, protože je omráčení nezajímá. Tam, kde dřív byla změna signatury, je teď přidání pole. Zároveň ukazuje detail, který mnoho lidí přehlédne: bedna **nemusí mít o odhozu ani zmínku**, i když ho objekt nese.

**Kde to sedí v širším obrázku.** Brackeys popisuje třídy jako plán, ze kterého se dělají instance [(47:07)](https://www.youtube.com/watch?v=e1zJS31tr88&t=2827s) — a upozorňuje na věc, která Godot definuje: **všechny vestavěné nody jsou třídy**, takže přidáním sprite instancuješ třídu Sprite [(47:56)](https://www.youtube.com/watch?v=e1zJS31tr88&t=2876s). Když skriptu dáš `class_name`, **objeví se v dialogu na přidání nodu vedle vestavěných** [(53:37)](https://www.youtube.com/watch?v=e1zJS31tr88&t=3217s) — fakticky jsi rozšířil engine o nový typ nodu.

**Vnitřní třídy jako bezpečnější slovník.** Poslední kus skládačky [(51:15)](https://www.youtube.com/watch?v=e1zJS31tr88&t=3075s): třída deklarovaná uvnitř jiné, dobrá na sbalení pár hodnot k sobě. Autor ji staví přímo proti slovníku a dává důvod, který se počítá [(52:01)](https://www.youtube.com/watch?v=e1zJS31tr88&t=3121s): **sáhneš-li na neexistující klíč slovníku, dozvíš se to až v běhu; u třídy to editor hlásí předem.** Slovník je flexibilní a levný na napsání; třída je type-safe. Táž volba jako u typování, o patro výš.

> **Pozn.:** Tenhle refaktor má jméno, které video neuvádí — **parameter object**. Stojí za to ho znát, protože se s ním potkáš i mimo hry, a stojí za to znát i jeho cenu: **vytváříš objekt, aby ses vyhnul změnám signatury**, což je výhodné právě tehdy, když je implementací hodně a mění se často. U jedné implementace je to zbytečná vrstva. Rozhodovací otázka není „je to hezčí?", ale **„kolik míst musím upravit, když přidám vlastnost?"** — a jakmile je odpověď „všechna", je čas na objekt. Souvisí to i s [datovou vrstvou](../praxe/principy-architektury.md#tri-principy-skalovatelnosti-separace-volne-vazby-data): útok jako objekt je krok od kódu k datům.

**Souvislosti:** [Gradual typing](#gradual-typing-kolik-bezpecnosti-si-koupis) *(tatáž volba na úrovni proměnné)* · [Principy architektury: separace, volné vazby, data](../praxe/principy-architektury.md#tri-principy-skalovatelnosti-separace-volne-vazby-data) · [Design patterns: tři rodiny vzorů](../teorie/design-patterns.md#tri-rodiny-vzoru-tvorba-struktura-chovani) · [Rejstřík: Struct](../rejstrik.md#struct) · [Rejstřík: Gradual typing](../rejstrik.md#gradual-typing)

---

## Pořádek jako nástroj: hlavička skriptu a inspektor

**Zdroj:** [1 Easy Habit To Level Up Your Godot Game](https://www.youtube.com/watch?v=Ez6BEiGOMCc) · [StayAtHomeDev](https://www.youtube.com/channel/UCDshKIMtFjYreCzApleuV8w) · ~3 min, tip · + [5 Tricks For Better GDScript in Godot](https://www.youtube.com/watch?v=p_IvmDm-Ywk) · týž kanál · ~3 min, tipy

**Shrnutí:** Existuje **standardní pořadí** deklarací v hlavičce GDScript souboru a existují **anotace, které srovnají inspektor**. Obojí je práce na minuty a obojí má tentýž efekt: přestaneš hledat. Nejužitečnější kus je ten, o kterém se neví — `@export_group`, `@export_category` a `@export_range` dělají z nekonečného seznamu vlastností použitelný panel.

### Rozpad myšlenky

**Pořadí v hlavičce** [(0:01)](https://www.youtube.com/watch?v=Ez6BEiGOMCc&t=1s) není libovolné, konvence zní: **signály → enumy → proměnné**. A proměnné se dál řadí podle druhu [(0:47)](https://www.youtube.com/watch?v=Ez6BEiGOMCc&t=47s): **konstanty → export proměnné → veřejné → privátní → `@onready`**. Užitek není v estetice, ale v tom, že **víš, kam nový kód patří** — a čtenář (často ty za rok) ví, kde ho hledat. Autor doporučuje doplnit komentářové oddělovače, aby se v hlavičce dalo skákat.

**Inspektor se srovnává anotacemi** [(1:34)](https://www.youtube.com/watch?v=Ez6BEiGOMCc&t=94s), a tohle je ta část, která má největší poměr užitku k práci:

- `@export_group` složí související vlastnosti do rozbalovací skupiny, **a skupiny se dají vnořovat** do podskupin,
- `@export_category` vytvoří nadřazenou kategorii nebo přejmenuje hlavní,
- `@export_range(0, 100, 1)` omezí číselnou hodnotu na rozsah a krok — v příkladu 0 až 100 po jedné.

Ten poslední bod je zajímavější, než vypadá: **není to jen UI**, je to zapsané omezení. Hodnota, která nikdy nesmí přesáhnout 100, se dá ohlídat na třech místech — v setteru (`clamp`), v kódu, který ji nastavuje, nebo **v deklaraci**. Poslední varianta je jediná, kterou nejde obejít omylem v editoru.

**Formátování** [(0:02)](https://www.youtube.com/watch?v=p_IvmDm-Ywk&t=2s): dlouhá pole, slovníky a enumy rozepiš na víc řádků — čte se to líp a chyby jsou vidět dřív. Bonus, který stojí za převzetí: **nechávej za posledním prvkem čárku**, ať se další položka přidává o jednu editaci levněji.

**Tři druhy hashtagů**, které vypadají stejně a znamenají různé věci [(0:49)](https://www.youtube.com/watch?v=p_IvmDm-Ywk&t=49s): `# ` s mezerou je **komentář**, `#` bez mezery je **zakomentovaný kód**, a `## ` se dvěma mřížkami je **dokumentační komentář**, ze kterého Godot umí vygenerovat dokumentaci k vlastním skriptům. Rozlišení není formalita — poznáš z něj, jestli za hashtagem stojí vysvětlení, nebo něco, co se má vrátit do provozu.

**Pojmenování** má konvenci pro každou kategorii [(1:36)](https://www.youtube.com/watch?v=p_IvmDm-Ywk&t=96s): soubory `snake_case` · třídy a nody `PascalCase` · funkce a proměnné `snake_case` · **signály `snake_case` a v minulém čase** (protože oznamují, co se stalo) · konstanty `CONSTANT_CASE` · enumy `PascalCase` pro jméno a `CONSTANT_CASE` pro členy, protože členy jsou konstanty.

**A dvě drobnosti navíc.** Kolem operátorů a za čárkami patří mezera — ale **nezarovnávej výrazy svisle**, protože každé nové delší jméno pak znamená přeformátovat celý blok [(1:36)](https://www.youtube.com/watch?v=p_IvmDm-Ywk&t=96s). A řádek přes 100 znaků se **nezalamuje Enterem** (to je nový příkaz), ale **obalí do závorek a odsadí dvakrát** [(2:22)](https://www.youtube.com/watch?v=p_IvmDm-Ywk&t=142s).

> **Pozn.:** Za tím vším je jeden mechanismus, který stojí za pojmenování: **konvence šetří rozhodování, ne psaní.** Když je pořadí dané, nemusíš u každé nové proměnné přemýšlet, kam ji dát — a ušetřená pozornost jde do věcí, které za pozornost stojí. Přesně tenhle mechanismus popisuje [Patnáct malých návyků](../teorie/programatorske-navyky.md#patnact-malych-navyku-tri-mechanismy) a stojí i za doporučením obou beginner průvodců „piš čitelný kód, protože ten někdo za rok jsi ty".

**Souvislosti:** [Gradual typing](#gradual-typing-kolik-bezpecnosti-si-koupis) *(typ jako druhá polovina téhož zápisu)* · [Co si přinést, než otevřeš editor](zaklady.md#co-si-prinest-nez-otevres-editor) *(čitelný kód jako první návyk)* · [Programátorské návyky](../teorie/programatorske-navyky.md#patnact-malych-navyku-tri-mechanismy) · [Devět tipů proti špagetám](../praxe/organizace-projektu.md#devet-tipu-proti-spagetam-v-grafech) *(táž disciplína ve vizuálním skriptování)*

---

## Když bug není v kódu: keyboard ghosting

**Zdroj:** [Why Your Godot Code Isn't Actually Broken (Keyboard Ghosting)](https://www.youtube.com/watch?v=qA3dnGGC3ow) · [DeeRaghooGames](https://www.youtube.com/channel/UC-KLgU0nzoCCEU6W16CS3vQ) · ~11 min, případovka

**Shrnutí:** Autor strávil tři hodiny laděním super-skoku, který fungoval při běhu doprava a nefungoval doleva. Chyba nebyla v Godotu, ve skriptu ani ve hře — **byla v klávesnici**. Levné membránové klávesnice u některých trojkombinací prostě jeden vstup zahodí a hra ho nikdy nedostane. Kód se tím opravit nedá; opravit jde jen **design ovládání**, a to je věc, kterou musíš udělat dřív, než ti ji nahlásí hráči.

### Rozpad myšlenky

**Symptom** je hezky konkrétní [(5:10)](https://www.youtube.com/watch?v=qA3dnGGC3ow&t=310s): super-skok se pouští držením šipky nahoru a stiskem mezerníku. Při pohybu **doprava** funguje bez problému. Při pohybu **doleva** se nestane nic — a na vizualizaci klávesnice, kterou si autor postavil, je vidět, že **mezerník do hry nikdy nedorazil**. Logika skriptu je přitom triviální: při stisku mezerníku ověř, jestli je držená šipka nahoru.

**Mechanismus** je hardwarový [(5:57)](https://www.youtube.com/watch?v=qA3dnGGC3ow&t=357s). Klávesnice nemá po drátu na klávesu — má **matici řádků a sloupců** a ze zkratovaného průsečíku odvodí, co jsi zmáčkl. Při více současných stiscích může elektrický signál projít matricí **neočekávanou cestou** a vypadat jako stisk klávesy, kterou nikdo nezmáčkl. Tomu falešnému vstupu se říká **ghosting** — duch. Moderní klávesnice mu předcházejí tak, že místo vymyšlené klávesy **jednu skutečnou zahodí** [(6:44)](https://www.youtube.com/watch?v=qA3dnGGC3ow&t=404s); tomu se říká **key jamming** a přesně to se stalo tady.

**Rozsah problému je tím nejnepříjemnější** [(7:30)](https://www.youtube.com/watch?v=qA3dnGGC3ow&t=450s): **které kombinace selžou, závisí na konkrétní klávesnici** — značce, modelu i vnitřním zapojení. Kombinace, která ti bezvadně funguje, může u hráče selhat úplně. Dražší klávesnice mají navíc izolační diody, a přesně proto se u herních klávesnic inzeruje **anti-ghosting** a **N-key rollover**.

**Opravit se to nedá.** Autor to říká rovnou [(8:08)](https://www.youtube.com/watch?v=qA3dnGGC3ow&t=488s): *nenašel jsem způsob, jak detekci té kombinace vynutit; tohle se kódem neopraví, je to hardwarové omezení.* U sebe to vyřešil přesunem ovládání na WASD.

**Co s tím tedy jako vývojář** [(9:20)](https://www.youtube.com/watch?v=qA3dnGGC3ow&t=560s) — pět opatření, seřazených podle toho, kolik ti koupí:

1. **Vždycky nech hráče přemapovat ovládání.** Různé klávesnice selhávají na různých kombinacích; volba kláves je proto jediná obecná obrana.
2. **Nabídni víc výchozích rozložení** — WASD, šipky, ESDF.
3. **Podporuj gamepad**, kterého se ghosting netýká vůbec.
4. **Nestav kritické akce na třech a víc současně držených klávesách.**
5. **Testuj na levné membránové klávesnici**, ne jen na té své.

Šestý bod je návrhový, a je nejzajímavější [(10:07)](https://www.youtube.com/watch?v=qA3dnGGC3ow&t=607s): **přepínač místo držení**. Místo „drž sprint, zároveň běž a skákej" nabídni sprint jako toggle. Tím se počet současně držených kláves sníží o jednu a problém zmizí ještě předtím, než vznikne.

> **Pozn.:** Tohle je učebnicová ukázka toho, proč je [test na cizím hardwaru](../teorie/playtesting.md#kdo-testuje-a-jak-skalovat-road-test-pred-stress-testem) něco jiného než test na vlastním stroji — a proč se u chyby, kterou nedokážeš reprodukovat, vyplatí ptát „co je jinak na *jeho* sestavě?" dřív než „co je špatně v mém kódu". Zobecnění, které si z toho bereme: **než tři hodiny hledáš bug ve svém kódu, ověř, že vstup vůbec dorazil.** Vizualizace stisků, kterou si autor postavil, je pět minut práce a odpověděla na otázku okamžitě — a je to táž disciplína jako [Print String jako první nástroj](../praxe/editor-tipy.md#jak-se-ucit-engine-rady-po-peti-letech): udělej neviditelné viditelným, než začneš uvažovat.

**Souvislosti:** [Delta a physics process](prvni-hra.md#delta-a-physics-process-proc-se-rychlost-nasobi-casem) *(input action systém, bez kterého přemapování nejde)* · [Playtesting: road test před stress testem](../teorie/playtesting.md#kdo-testuje-a-jak-skalovat-road-test-pred-stress-testem) · [Tipy do editoru: jak se učit engine](../praxe/editor-tipy.md#jak-se-ucit-engine-rady-po-peti-letech) *(udělej neviditelné viditelným)* · [Rejstřík: Keyboard ghosting](../rejstrik.md#keyboard-ghosting) · [Rejstřík: N-key rollover](../rejstrik.md#n-key-rollover)
