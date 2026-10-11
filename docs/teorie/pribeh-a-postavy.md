# Příběh a postavy: narrative design pro malé týmy

Workshop Indie Game Clinic o postavách a dialozích — vedený člověkem, který narrative design učil na univerzitě a psal pro herní studia. Krédo celé kapitoly: příběh ve hře není „něco, co se dopíše", ale feature s cenovkou, kterou si musíš umět spočítat — a postava není osoba, ale proces, který ji předstírá. Poslední myšlenka přidává pohled scenáristy: [šest otázek](#sest-otazek-bez-kterych-nemas-pribeh), ze kterých se dá postavit jakýkoli příběh.

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

**Souvislosti:** [Základy: engagement a appeal](zaklady.md) · [Rejstřík: cipher](../rejstrik.md#cipher) · [Rejstřík: narrative design](../rejstrik.md#narrative-design) · [Hudba a zvuk: leitmotiv](../hudba/tvorba-soundtracku.md#leitmotiv-hudba-propojuje-svet) *(hudební téma postavy)* · [Šest otázek](#sest-otazek-bez-kterych-nemas-pribeh) *(postava se záměrem a překážkou)*

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

---

## Sedm pater worldbuildingu: šířka není hloubka

**Zdroj:** [The Seven Levels of Worldbuilding](https://www.youtube.com/watch?v=vFMnz75y5y4) · [Large Lads Studios](https://www.youtube.com/channel/UCUMIH5Xhx6fyfGokIxtN70g) · ~30 min, esej

**Shrnutí:** Autor si všímá jevu, který zná každý: **existují světy, které vypadají obrovsky, a když do nich vstoupíš, sahají po kotníky.** Rozdíl mezi šířkou a hloubkou rozloží do sedmi pater — s výslovnou poznámkou, že to nejsou schody a že spousta skvělých příběhů žije na druhém. Háček, kvůli kterému to není jen taxonomie: **každé patro se pozná podle otázky, kterou si klade.**

### Rozpad myšlenky

**Obrázek, kterým to celé otvírá** [(0:49)](https://www.youtube.com/watch?v=vFMnz75y5y4&t=49s), je pro každého, kdo někdy kreslil mapu, nepříjemně známý: nasypeš hory, posadíš města k pobřeží a **nakreslíš řeky tam, kde vypadají dobře** — přes pohoří, rozvětvené do stran, od moře k moři. Pak uvidíš jedno video o tvorbě map a **už to nejde odvidět**.

**Sedm pater**, každé s otázkou, která ho definuje:

| patro | co to je | otázka |
|---|---|---|
| **1. mapa** | terén, který se řídí pravidly (i vlastními) | *proč je tohle město právě tady?* |
| **2. rule of cool** | draci, padlá říše, prokletý les | *co by bylo super?* |
| **3. povrchová identita** | jména, architektura, oblečení, symboly | *poznám podle siluety, odkud to je?* |
| **4. funkční moc** | magie a technologie s pravidly a důsledky | *co to ve světě doopravdy dělá?* |
| **5. hluboká kultura a historie** | víra, tabu, dozvuky válek, protiřečící si výklady | *jak se to stalo takhle?* |
| **6. infrastruktura a instituce** | banky, obchodní cesty, zásobování, komunikace | *když má město 200 tisíc lidí, co jedí?* |
| **7. generativní svět** | svět, který sám plodí příběhy | *co se děje v tomhle přístavu v tomhle století?* |

**Kde je ta hranice, o kterou jde** [(9:20)](https://www.youtube.com/watch?v=vFMnz75y5y4&t=560s). Druhé patro **není chyba** — je zábavné, návykové a je to obvykle to, čím tvůj svět někoho zaujme. Problém nastane, když se **zamění za hloubku**: *„skládání skvělých nápadů na sebe z toho automaticky nedělá vrstevnatou věc. Můžeš přidávat další bohy a další dávné války a bude to působit větší a větší — jenže větší není hlubší."* Test jsou otázky typu „co ten padlý impérium nahradilo?" nebo „je-li ten artefakt tak mocný, proč už dávno všechno nerozvrátil?".

**Nejužitečnější patro pro herní design je čtvrté** [(15:39)](https://www.youtube.com/watch?v=vFMnz75y5y4&t=939s), protože je zároveň o pravidlech systému. *„Přestaneš se ptát ‚je to super?' a začneš se ptát ‚co to dělá?'"* Je-li magie běžná, co to udělá s prací? Existují draci — jak se vede válka? A pointa, která platí i mimo vyprávění: **má-li moc pravidla a důsledky, nemůžeš podvádět.** Problémy musíš řešit uvnitř světa, který jsi postavil — a čtenář či hráč pak přestane mít pocit, že se věci dějí, protože je potřebuje děj.

**Dvě pasti, které jmenuje** [(12:30)](https://www.youtube.com/watch?v=vFMnz75y5y4&t=750s): na třetím patře hrozí **planeta klobouků** — celá kultura zredukovaná na jednu vlastnost (tohle je bojovnická, tohle chytrá, tohle záludná), obvykle proto, že se estetika posiluje tak dlouho, až v ní nezbude místo na výjimky. A na pátém je rozdíl mezi *„mít dávnou lore"* a *„mít historii, která tvaruje svět"*: u toho druhého se rozhodnutí sčítají přes generace a lidé si navzájem odporují ve výkladu, protože **skutečné společnosti si odporují**.

**A závěr, který to celé změkčuje** [(28:23)](https://www.youtube.com/watch?v=vFMnz75y5y4&t=1703s): *„není to o talentu, je to o povědomí. Jakmile si začneš klást lepší otázky — proč je tohle tady, kdo z toho má prospěch, co se stane, když se to změní — tvůj svět zesílí sám."* A druhá půlka: **sedmé patro nepotřebuje většina projektů.**

> **Pozn.:** Pro herní vývoj je z toho žebříku nejcennější, že **hloubka a rozsah jsou různé zdroje** — a že se dají utrácet nezávisle. Malá hra s jedním městem na čtvrtém patře působí věrohodněji než kontinent na druhém, a je **násobně levnější**. To je přesně tentýž argument jako [téma jako nůžky na scope](ludonarativni-soulad.md#tema-jako-nuzky-na-scope-pacific-drive-superhrdinove-a-fireball-wizard), jen aplikovaný na svět místo na funkce. Druhá přenositelná věc je **generativnost jako cíl**: svět, který sám nabízí příběhy, šetří práci — a to je u hry ještě podstatnější než u knihy, protože hra potřebuje **obsah v množství**. Vlastní výhrada: ten žebřík je postavený na epické fantasy a sci-fi, a u her je celé jedno patro potichu jinde — **worldbuilding musí být hratelný**. Instituce, které nejdou nijak potkat, jsou v knize hodnota a ve hře náklad; herní verze šestého patra proto zní spíš „jsou ty instituce vidět v tom, co hráč dělá?". Blízkou českou paralelou je [rešerše slovanské mytologie](slovansky-folklor.md) — tam se hloubka bere z reálné kultury místo z vlastní invence.

**Souvislosti:** [Příběh je feature s cenovkou](#pribeh-je-feature-s-cenovkou) · [Cvičení: nech dvě postavy pohádat se o tvůj svět](#cviceni-nech-dve-postavy-pohadat-se-o-tvuj-svet) · [Prostor vypráví](prostor-vypravi.md) · [Ludotematický soulad](ludonarativni-soulad.md#tema-jako-nuzky-na-scope-pacific-drive-superhrdinove-a-fireball-wizard) · [Rešerše: slovanský folklor](slovansky-folklor.md) · [Rejstřík: Environmental storytelling](../rejstrik.md#environmental-storytelling) · [Rejstřík: Art bible](../rejstrik.md#art-bible)

---

## Šest otázek, bez kterých nemáš příběh

**Zdroj:** [If You Can't Answer These 6 Questions You Don't Have A Story - Glenn Gers](https://www.youtube.com/watch?v=uL0atQFZzL8) · [Film Courage](https://www.youtube.com/channel/UCs8o1mdWAfefJkdBg632_tg) · ~15 min, rozhovor se scenáristou

**Shrnutí:** Scenárista Glenn Gers v rozhovoru pro Film Courage redukuje příběh na jádro: postava se snaží něčeho dosáhnout a něco jí stojí v cestě. Z toho vychází šest otázek. O kom to je, co chce, proč to nemůže mít, co s tím udělá, proč to nefunguje a jak to skončí. Podle Gerse fungují pro film, seriál i videohru. Háček je v poslední otázce: konec je to, co postava udělá poprvé, protože kdyby to zkusila dřív, příběh by skončil dřív.

### Rozpad myšlenky

**Postava, záměr, překážka.** Příběh sleduje postavu, případně víc postav. Jde to i s jedenácti hlavními, jen to dá hodně práce [(0:00)](https://www.youtube.com/watch?v=uL0atQFZzL8&t=0s). Jádrem je vždycky postava se záměrem, která narazí na lidi, kteří jí pomůžou nebo uškodí. Gers to přirovnává ke kulečníkovým koulím, které se valí, dokud do něčeho nenarazí, jen koule na rozdíl od postav nikam nechtějí [(0:48)](https://www.youtube.com/watch?v=uL0atQFZzL8&t=48s). Každá postava si navíc myslí, že je hlavní. Recepční v hotelu je středem vlastního příběhu a hrdina s žádostí o pokoj do toho příběhu jen vstupuje [(1:35)](https://www.youtube.com/watch?v=uL0atQFZzL8&t=95s). Naložit kufr do vlaku bez jakékoli překážky je krátký a nudný příběh. Když kufr někdo ukradne, je zajímavější, a ještě víc, když je v něm něco důležitého [(2:22)](https://www.youtube.com/watch?v=uL0atQFZzL8&t=142s). Překážka nemusí být vnější. Stačí, že se postava bojí nádraží a hlasitých zvuků, a i taková překážka je skutečná [(3:11)](https://www.youtube.com/watch?v=uL0atQFZzL8&t=191s).

**Šest otázek.** Psaní je podle Gerse proces otázek, ne formulář k vyplnění [(3:11)](https://www.youtube.com/watch?v=uL0atQFZzL8&t=191s). Začít jde čímkoli, třeba chutí napsat western nebo něco o tom, jak láska bolí, a každá další otázka je volba [(4:01)](https://www.youtube.com/watch?v=uL0atQFZzL8&t=241s). Kostru tvoří šest otázek: o kom to je, co chce, proč to nemůže mít, co s tím udělá, proč to nefunguje a jak to skončí [(4:47)](https://www.youtube.com/watch?v=uL0atQFZzL8&t=287s). Konec má dvě podoby, postava cíle dosáhne, nebo ne. Rozhoduje to, co udělá poprvé, protože kdyby to zkusila dřív, skončilo by to dřív [(5:33)](https://www.youtube.com/watch?v=uL0atQFZzL8&t=333s). Kostra podle Gerse vydrží tři akty, dvacet sedm i jeden. Pak se ptáš dál: kdo, co, proč, kde. Proč se ten instalatér bojí výšek? Každá odpověď je konkrétní a posune tě blíž ke scéně.

**Proces podle sebe.** Správný proces podle Gerse neexistuje. Existuje jen ten, který jde dělat relativně snadno a který si najdeš pozorováním sebe a zkoušením [(6:22)](https://www.youtube.com/watch?v=uL0atQFZzL8&t=382s). Gers sám píše dobře v krátkých dávkách. Dřít dál po vyčerpané dávce vedlo jen k pochybnostem a k přepisování dobrých pasáží horšími [(7:10)](https://www.youtube.com/watch?v=uL0atQFZzL8&t=430s). Teď přestává, jakmile cítí, že to ztrácí, dá si pauzu nebo procházku a vrátí se k další dávce, a je to produktivnější [(8:00)](https://www.youtube.com/watch?v=uL0atQFZzL8&t=480s). Gers má vlastní pevnou sadu dokumentů, osnovu rozdělenou na scény, poznámky, text a přehled. Každý má svou, důležité je, aby se po otevření myslelo jen na obsah, ne na formu [(9:36)](https://www.youtube.com/watch?v=uL0atQFZzL8&t=576s) [(10:22)](https://www.youtube.com/watch?v=uL0atQFZzL8&t=622s). Do scénáře stačí zapsat cokoli, třeba jen popis scény „přijde domů a je nešťastný". Při dalším čtení přijde otázka, jak poznáme, že je nešťastný, a odpověď už je scéna: večeři z lednice hodí o zeď [(12:01)](https://www.youtube.com/watch?v=uL0atQFZzL8&t=721s) [(12:47)](https://www.youtube.com/watch?v=uL0atQFZzL8&t=767s).

> **Pozn.:** Ve hře se šest otázek dá číst dvakrát. Jednou pro příběh postav, podruhé pro hráče: co chce, co mu brání, co zkusí a proč to selže je kostra questu i stupňování obtížnosti. Věta „každá postava si myslí, že je hlavní" je zase dobrý test pro NPC a sedí s [cvičením, ve kterém se dvě postavy hádají o tvůj svět](#cviceni-nech-dve-postavy-pohadat-se-o-tvuj-svet). Toto čtení je naše. Gers v rozhovoru odkazuje na vlastní video o šesti otázkách na svém kanálu [(4:47)](https://www.youtube.com/watch?v=uL0atQFZzL8&t=287s), takže jde i o promo.

**Souvislosti:** [Postava není osoba, je to proces](#postava-neni-osoba-je-to-proces-a-hracska-postava-ma-ctyri-typy) · [Příběh je feature s cenovkou](#pribeh-je-feature-s-cenovkou) · [Tvůrčí zásek](tvurci-zasek.md) *(proces, který tě nedusí)* · [Rejstřík: Narrative design](../rejstrik.md#narrative-design)
