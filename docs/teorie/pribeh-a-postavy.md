# Příběh a postavy: narrative design pro malé týmy

Workshop Indie Game Clinic o postavách a dialozích — vedený člověkem, který narrative design učil na univerzitě a psal pro herní studia. Krédo celé kapitoly: příběh ve hře není „něco, co se dopíše", ale feature s cenovkou, kterou si musíš umět spočítat — a postava není osoba, ale proces, který ji předstírá.

---

## Příběh je feature s cenovkou

**Zdroj:** [Story in Games: Characters & Dialogue](https://www.youtube.com/watch?v=orvZIxC54NU) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · ~40 min, workshop

**Shrnutí:** Než hře přidáš postavy a dialogy, projdi tři brány: kolik *implementace* to znamená, jaká je tvoje *spisovatelská kariéra* doteď a jaké příběhy ti *nástroje* přirozeně nabízejí. A pamatuj, že hry mají vyprávěcí prostředky, které film ani kniha nemají — příběh nemusí téct dialogem.

### Rozpad myšlenky

**Narrative design** [(0:33)](https://www.youtube.com/watch?v=orvZIxC54NU&t=33s) vznikl jako pojem přesně proti modelu „designér řekne ‚tady budou cutscény' a spisovatel je dopíše" — vyprávění se navrhuje *spolu* s herním designem.

**Brána 1 — implementační náklad** [(5:34)](https://www.youtube.com/watch?v=orvZIxC54NU&t=334s) roste po schodech: postavy, které mluví, je jedna úroveň; možnost odpovídat druhá; postavy, které si odpovědi *pamatují* a mění chování, třetí [(5:55)](https://www.youtube.com/watch?v=orvZIxC54NU&t=355s). Každý schod je systém, UI a obsah navíc (a často důvod koupit hotové řešení — autor pro visual-novel sekci v Unity licencoval hotový balík).

**Brána 2 — spisovatelská kariéra** [(6:52)](https://www.youtube.com/watch?v=orvZIxC54NU&t=412s): psal jsi už někdy příběh? Umíš posoudit, jestli je tvůj dialog dobrý? Skvělá akční hra se dá *zhoršit* naroubovaným příběhem, který autor neumí napsat ani ohodnotit. (Stejná řemeslnická upřímnost jako v [rozpočtu pozornosti](scope.md#proc-male-rozpocet-pozornosti-ne-jen-dokoncitelnost).)

**Brána 3 — nástroj tvaruje příběh** [(8:05)](https://www.youtube.com/watch?v=orvZIxC54NU&t=485s): Twine předpokládá prózu (musíš umět *psát*), Ren'Py dialogy postav (stačí umět *mluvit*), 3D engine tě táhne k environmentálnímu vyprávění [(3:59)](https://www.youtube.com/watch?v=orvZIxC54NU&t=239s). Autor učil studenty dialogy dřív než prózu — dialog je přenositelnější dovednost: postavy mluví skoro v každé hře, próza skoro v žádné.

A úniková cesta, kterou hry mají navíc [(4:35)](https://www.youtube.com/watch?v=orvZIxC54NU&t=275s): flavor texty, mechaniky, rozhraní, prostředí. Když ti po třech branách vyjde, že dialogy nejsou tvoje parketa, není to konec příběhu ve hře — je to začátek vyprávění jinými prostředky.

**Souvislosti:** [Scope: řemeslnické otázky](scope.md#proc-male-rozpocet-pozornosti-ne-jen-dokoncitelnost) · [Žrouti času: world building](produktivita.md#unik-k-snadne-tvorbe-world-building-a-dokonaly-toolset) · [Rejstřík: narrative design](../rejstrik.md#narrative-design)

---

## Postava není osoba, je to proces — a hráčská postava má čtyři typy

**Zdroj:** [Story in Games: Characters & Dialogue](https://www.youtube.com/watch?v=orvZIxC54NU) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · stejný workshop

**Shrnutí:** Postava „nemá psychiku ani osobnost — jen vlastnosti, kvůli kterým jí je čtenář přisoudí" (naratoložka Mieke Bal [(10:43)](https://www.youtube.com/watch?v=orvZIxC54NU&t=643s)). Charakterizace je řemeslný proces záměrných voleb. A hry přidávají vlastní zvláštnost: hráčská postava leží na škále od prázdné nádoby po plně napsaného člověka — a každá poloha znamená jinou práci pro vývojáře.

### Rozpad myšlenky

Charakterizační stavebnice [(10:18)](https://www.youtube.com/watch?v=orvZIxC54NU&t=618s): vzhled, původ (background — ve fantasy/sci-fi přirozeně napojený na world building: „trpaslík, který nesnáší elfy"), osobnost, vztahy, motivace (zdroj konfliktů: postavy, které sdílejí cíl, ale neshodnou se na cestě), řečové a behaviorální vzorce. Čím vědoměji tyhle volby děláš, tím líp se dělají.

Kontinuum hráčských postav — od Trevora z GTA V (plně napsaný, na hráči nezávislý [(11:32)](https://www.youtube.com/watch?v=orvZIxC54NU&t=692s)) po Chell z Portalu (chodí jako člověk, osobnost žádná [(11:57)](https://www.youtube.com/watch?v=orvZIxC54NU&t=717s)) — video krájí na **čtyři typy**, každý s vlastní cenovkou:

- **Cipher** [(15:40)](https://www.youtube.com/watch?v=orvZIxC54NU&t=940s): prázdná nádoba bez hlasu a motivací; hráč si ji oživí sám. „Bez osobnosti" není vada [(16:20)](https://www.youtube.com/watch?v=orvZIxC54NU&t=980s) — Tunic i Half-Life jsou mlčením protagonisty *lepší* [(16:37)](https://www.youtube.com/watch?v=orvZIxC54NU&t=997s): v puzzle hrách má znít hlas v hráčově hlavě, ne komentář postavy. Cena: veškerá tíha jde do vizuální komunikace — jak postava vypadá a co reprezentuje.
- **Fixní postava** (Alan Wake) [(17:37)](https://www.youtube.com/watch?v=orvZIxC54NU&t=1057s): autorsky napsaná, hráč ji řídí jen v akci. Cena: musíš být opravdu dobrý spisovatel [(18:08)](https://www.youtube.com/watch?v=orvZIxC54NU&t=1088s) — žádáš hráče, aby přestal hrát a poslouchal.
- **Plně customizovatelná** [(18:25)](https://www.youtube.com/watch?v=orvZIxC54NU&t=1105s): osobnost skládá hráč. Cena: systémy a obsah — možnosti vzhledu, dialogové volby, větvení.
- **Customizovatelná s fixním základem** (Shepard: jméno, role kapitána, mantinely „nic vyloženě zlého") [(18:58)](https://www.youtube.com/watch?v=orvZIxC54NU&t=1138s): BioWare kompromis, mix obou cen.

Praktické pravidlo z videa: umíš psát → fixní postava; neumíš psát, ale umíš vyrobit cool věci → cipher. A hlavně: **vyber si polohu vědomě** — hra, která mezi typy nerozhodně pluje, působí zmateně.

**Souvislosti:** [Základy: engagement a appeal](zaklady.md) · [Rejstřík: cipher](../rejstrik.md#cipher) · [Rejstřík: narrative design](../rejstrik.md#narrative-design) · [Hudba a zvuk: leitmotiv](../hudba/tvorba-soundtracku.md#leitmotiv-hudba-propojuje-svet) *(hudební téma postavy)*

---

## Jak postavy mluví: rejstříky, směr dialogu a test začerněných jmen

**Zdroj:** [Story in Games: Characters & Dialogue](https://www.youtube.com/watch?v=orvZIxC54NU) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · stejný workshop

**Shrnutí:** Tři praktické nástroje pro dialogy: zvol **rejstřík** (civilní naturalismus vs. divadelní melodrama — a odděl od obojího hlas tutoriálu), zvol **směr** dialogu (kdo mluví na koho a kolik to stojí) a ověř **rozlišitelnost hlasů** testem začerněných jmen.

### Rozpad myšlenky

**Rejstříky** [(25:18)](https://www.youtube.com/watch?v=orvZIxC54NU&t=1518s): Night in the Woods mluví jako skuteční mladí lidé (naturalismus); temné fantasy a epické sci-fi mluví divadelně, přes obraz [(25:49)](https://www.youtube.com/watch?v=orvZIxC54NU&t=1549s). Oba rejstříky fungují; vědomé přeskoky mezi nimi jsou zdroj komiky (patetik, který náhle řekne něco přízemního). Zvláštní kaz her: **hlas tutoriálu** [(27:08)](https://www.youtube.com/watch?v=orvZIxC54NU&t=1628s). Když instrukcím vnutíš „osobnost", hráč přestane poznávat, kdy hra vypráví a kdy radí — Darkest Dungeon proto vede narativní texty pateticky a strategické rady stroze [(27:40)](https://www.youtube.com/watch?v=orvZIxC54NU&t=1660s).

**Směr dialogu** [(28:09)](https://www.youtube.com/watch?v=orvZIxC54NU&t=1689s) je zároveň rozpočtové rozhodnutí: jednosměrný dialog s němým protagonistou (stará JRPG, Zelda) = napsat trochu textu pro hodně NPC, žádné větvení; protagonista mluví sám, hráč nevolí (Celeste [(28:40)](https://www.youtube.com/watch?v=orvZIxC54NU&t=1720s)) = potřebuješ sympatickou psanou postavu; obousměrný dialog s volbami (Mass Effect [(28:56)](https://www.youtube.com/watch?v=orvZIxC54NU&t=1736s)) = plná cena systémů i psaní. U voleb pomáhá vzorec s čitelným očekáváním — klasické Fallout trio hodný / hajzl / pragmatik [(22:04)](https://www.youtube.com/watch?v=orvZIxC54NU&t=1324s) — a rozmysl, jestli chceš předvídatelnost (RPG questy), nebo sociální realismus, kde vyptávání může mít následky.

**Test začerněných jmen** [(30:51)](https://www.youtube.com/watch?v=orvZIxC54NU&t=1851s): vezmi scénu, smaž jména mluvčích — poznáš, kdo mluví? Když ne, postavy nemají hlasy, jen repliky. Hlasy se liší vzorci (slovní vata, délka vět, slovník podle původu: mág nemluví jako barbar) a hry umí i vlastní triky [(30:25)](https://www.youtube.com/watch?v=orvZIxC54NU&t=1825s): rychlost vypisování textu, zvuk, font (Smrť v Zeměploše mluví KAPITÁLKAMI [(30:32)](https://www.youtube.com/watch?v=orvZIxC54NU&t=1832s)).

**Souvislosti:** [Zápisky: oblouk se potvrzuje formou](../zapisky/oblouk-formou.md) *(posun rejstříku řeči jako důkaz oblouku)* · [Rejstřík: narrative design](../rejstrik.md#narrative-design) · budoucí kapitoly o dialozích v praxi (UE)

---

## Cvičení: nech dvě postavy pohádat se o tvůj svět

**Zdroj:** [Story in Games: Characters & Dialogue](https://www.youtube.com/watch?v=orvZIxC54NU) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · závěrečné cvičení workshopu

**Shrnutí:** Napiš hádku dvou postav *z tvého světa* o něčem *z tvého světa* [(33:31)](https://www.youtube.com/watch?v=orvZIxC54NU&t=2011s). Ne o ananasu na pizze [(33:53)](https://www.youtube.com/watch?v=orvZIxC54NU&t=2033s) — o věci, kterou se tvůj svět liší od našeho. Jedno cvičení, tři výstupy: postavy dostanou hlasy, vztah a názory; svět dostane význam; a ty zjistíš, jestli tvůj lore vůbec unese konflikt.

### Rozpad myšlenky

Proč to funguje [(34:50)](https://www.youtube.com/watch?v=orvZIxC54NU&t=2090s): hráče nezajímá lore dump — svět začne zajímat teprve tehdy, když je vidět, že na něm *záleží postavám*. A nejrychlejší způsob, jak to ukázat, je neshoda: o minulé události, o probíhající válce (nebo supermarketu, co se stěhuje do městečka — funguje to i v cozy měřítku), o správném dalším kroku. Učebnicový příklad z videa: X-Meni [(37:48)](https://www.youtube.com/watch?v=orvZIxC54NU&t=2268s) — „existují mutanti" je kulisa, ne konflikt; příběh dělá spor Xaviera s Magnetem o to, *co s tím*. Světy nejsou zajímavé svými fakty, ale interpretacemi, které postavy reprezentují.

Forma je volná: scénář, tabulka, první hodina v Twine/Ren'Py, klidně samomluva v tramvaji. Podstata je jinde — je to **psací obdoba concept artu** [(37:09)](https://www.youtube.com/watch?v=orvZIxC54NU&t=2229s): výstup možná nikdy neskončí ve hře, ale ty po něm víš, kdo jsou tvoje postavy, jak se hádají (každá jinak — viz test začerněných jmen výše) a co je ve tvém světě skutečně v sázce.

> **Pozn.:** Pro projekt se slovanskou mytologií v zásobníku je tohle cvičení připravené k okamžitému použití: dvě postavy se přou, jestli se má vesnice držet starých rituálů — a najednou víš, jak se v tom světě mluví o bozích, kdo věří, kdo se bojí, a o čem vlastně hra je.

**Souvislosti:** [Základy: appeal — testuj koncepty brzy](zaklady.md#appeal-centralni-fantazie-a-mix-ktery-nejde-zaradit) · [Rešerše: Vasilisa a Baba Jaga](slovansky-folklor.md) · [Rejstřík: narrative design](../rejstrik.md#narrative-design)
