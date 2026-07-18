# První projekty: tři hry, které tě naučí základy

Univerzitní game design kurz řešil problém, který má každý samouk: jak se naučit *najednou* trochu programovat, trochu dělat vizuál a hlavně designovat — aniž by ses utopil v jedné velké hře. Odpověď byla tři malé projekty s krutě chytrými omezeními: hra, která je jen interface; hra, která je jen akce; a hra ve dvou z nůžek a lepidla. Celý výklad běží nad skutečným portfoliem bývalého studenta.

---

## Hra, která je jen interface: virtuální mazlíček

**Zdroj:** [3 Projects for Beginners: Game Design and Art Fundamentals](https://www.youtube.com/watch?v=cf9xDdPXOA0) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · ~37 min, průvodce výukovým modulem

**Shrnutí:** První projekt: Tamagotchi — postavička se třemi potřebami, třemi tlačítky a vizuálními stavy [(5:36)](https://www.youtube.com/watch?v=cf9xDdPXOA0&t=336s). Schválně to není zábavná hra. Je to hra **složená výhradně z interface** — a interface je přesně to, co začátečníci fatálně podceňují, když si za první projekt zvolí „farmařskou hru jako Stardew" [(11:23)](https://www.youtube.com/watch?v=cf9xDdPXOA0&t=683s).

### Rozpad myšlenky

**Proč zrovna interface:** dialogová okna, inventáře, obchody — žánrové samozřejmosti, které hráč nevnímá, znamenají pro nového programátora **týdny práce** [(12:14)](https://www.youtube.com/watch?v=cf9xDdPXOA0&t=734s); textbox s volbami a pamětí rozhodnutí je malý systém sám o sobě. Projekt, kde je interface celou hrou (svět vidíš oknem, interaguješ jen tlačítky), tyhle dovednosti izoluje — učíš se je samostatně, ne uprostřed větší hry, kterou každý zásah rozbíjí [(13:52)](https://www.youtube.com/watch?v=cf9xDdPXOA0&t=832s). Laťka kvality je konkrétní: čitelné ikony a **tlačítka se stavem stisknuto/nestisknuto** — detail, který chybí i hrám s léty vývoje [(9:45)](https://www.youtube.com/watch?v=cf9xDdPXOA0&t=585s).

**Vizuální omezení jako učebnice:** dvě barvy, jen základní tvary [(6:25)](https://www.youtube.com/watch?v=cf9xDdPXOA0&t=385s) — kdo přeskočí stylizaci a jde rovnou na realismus, vyrábí „derpy" výsledky; fundamenty tvarů jsou rychlejší cesta k hezkému. Doplňkové cvičení: nakresli svého mazlíčka jen z kruhů, pak jen z trojúhelníků [(15:29)](https://www.youtube.com/watch?v=cf9xDdPXOA0&t=929s) — verze děláš rychle a opakovaně, jako grafik skicuje tucty miniatur, než se upíše k inkoustu.

**Designová vrstva — subverze tématu:** mazlíček nesměl být zvíře, běžné ani exotické [(9:45)](https://www.youtube.com/watch?v=cf9xDdPXOA0&t=585s) — démon, Terminátor, elektrárna. Tím se ze skinu stává design: **jaké tři potřeby má elektrárna a jaké akce je sytí?** Student najednou přemýšlí o proměnných a slovesech hráče [(10:35)](https://www.youtube.com/watch?v=cf9xDdPXOA0&t=635s), a mimochodem zjišťuje, že žánr + jiné téma = dramaticky jiná hra (Tamagotchi se prodává dětem — nic ale nebrání udělat totéž jako horor).

> **Pozn.:** Za pozornost stojí i školní mechanismus okolo: hodnotí se **reflektivní psaní** („co bylo těžké, co příště jinak"), ne krása výsledku — protože jinak známkuješ vstupní úroveň, ne naučené [(8:05)](https://www.youtube.com/watch?v=cf9xDdPXOA0&t=485s). Pro samouka je to argument pro devlog: [zápis je důkaz učení](../zapisky/devlog-jako-mapa.md), výsledek je jen jeho vedlejší produkt.

**Souvislosti:** [Kolik kódu na start](co-se-ucit.md) · [Zápisek: Devlog jako mapa](../zapisky/devlog-jako-mapa.md) · [Rejstřík: Placeholder](../rejstrik.md#placeholder)

---

## Hra, která je jen akce: shmup bez levelů

**Zdroj:** [3 Projects for Beginners: Game Design and Art Fundamentals](https://www.youtube.com/watch?v=cf9xDdPXOA0) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · stejné video, druhý projekt

**Shrnutí:** Druhý projekt je zrcadlo prvního: sidescrollová střílečka na jedné obrazovce — čistý pohyb a akce, skoro žádný interface a hlavně **žádné levely** [(19:31)](https://www.youtube.com/watch?v=cf9xDdPXOA0&t=1171s). Věci se spawnují, obtížnost se ladí frekvencí — na rozdíl od platformeru, jehož level design je pro začátečníka nečekaně těžká disciplína [(21:10)](https://www.youtube.com/watch?v=cf9xDdPXOA0&t=1270s).

### Rozpad myšlenky

**Vizuální eskalace:** z monochromu na gradace jedné barvy [(21:59)](https://www.youtube.com/watch?v=cf9xDdPXOA0&t=1319s); rychlé opakované skici řeší otázku **čitelnosti** — který prvek z obrazu „vyskočí", jakou barvou oddělit pohyblivé od pozadí, které tvary působí výhrůžně a které evokují přírodu (hexagony → včely) [(22:45)](https://www.youtube.com/watch?v=cf9xDdPXOA0&t=1365s). Pořadí je pozoruhodné: napřed abstraktní tvar a barva, **téma až potom** — vizuální jazyk se hledá dřív, než se rozhodne, čí je.

**Subverze podruhé a tenis mechanik s tématem:** hráč nesmí být letadlo ani vesmírná loď [(19:31)](https://www.youtube.com/watch?v=cf9xDdPXOA0&t=1171s) — ponorky, čarodějnice na koštěti, pavouci. Základní funkčnost dostali studenti „nalžíci" (video + kód s dírami); jejich úkol byl **specifikovat jednu mechaniku, která hru přiblíží tématu** [(24:22)](https://www.youtube.com/watch?v=cf9xDdPXOA0&t=1462s). Nejlepší příklad za celý modul: torpédo, které vyletí pomalu a zrychluje — jediný tweak, a střela *je* najednou torpédo s lodním šroubem [(25:11)](https://www.youtube.com/watch?v=cf9xDdPXOA0&t=1511s). Tenhle „tenis" mezi mechanikou a tématem [(26:01)](https://www.youtube.com/watch?v=cf9xDdPXOA0&t=1561s) je základní pohyb game designu — zkušení ho dělají bezděčně, začátečník ho potřebuje pojmenovat. (Souvisí s [game feel](game-feel.md): pocit se vyrábí přesně takovými tweaky.)

**Souvislosti:** [Game feel a imerze](game-feel.md) · [Prostor a hranice](prostor-a-hranice.md) *(protipól: tady levely schválně nejsou)* · [Rejstřík: Game feel](../rejstrik.md#game-feel)

---

## Hra ve dvou a z nůžek: historické místo, analogové assety

**Zdroj:** [3 Projects for Beginners: Game Design and Art Fundamentals](https://www.youtube.com/watch?v=cf9xDdPXOA0) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · stejné video, třetí projekt a závěr

**Shrnutí:** Finále: skórovací hra na jedné obrazovce, ve dvojici, s dvěma zlomyslnými omezeními — děj musí sedět do **konkrétního historického místa a času** [(26:43)](https://www.youtube.com/watch?v=cf9xDdPXOA0&t=1603s) a veškerý vizuál musí pocházet z **analogových zdrojů**: kresba, modelína, fotky, skeny — nic vyrobeného od nuly na počítači [(31:30)](https://www.youtube.com/watch?v=cf9xDdPXOA0&t=1890s).

### Rozpad myšlenky

**Proč historie:** „konkrétní místo a čas" blokuje tři únikové defaulty — sci-fi, fantasy, zombie město [(26:43)](https://www.youtube.com/watch?v=cf9xDdPXOA0&t=1603s) — a nutí k vizuální rešerši. Vedlejší lekce na celý život: fantazijní světy stojí na reálných; kdo neumí čerpat z reality, nemá z čeho stavět ani fikci [(30:42)](https://www.youtube.com/watch?v=cf9xDdPXOA0&t=1842s). (Přesně role, kterou v téhle knihovně hraje [rešerše slovanské mytologie](slovanska-monstra.md).)

**Proč analog:** nová média nutí experimentovat a materiál sám napovídá — „tohle vypadá jako koberec" vede k rozhodnutím, která by ilustrátor u prázdného plátna neudělal [(33:58)](https://www.youtube.com/watch?v=cf9xDdPXOA0&t=2038s). Výsledky jsou scrappy a právě proto osobité; a zkušenost „umím vyrobit asset z čehokoli" se hodí navždycky. **Proč pár:** kolaborace je vlastní dovednost a většina škol ji neučí — prostě tě do ní hodí [(27:31)](https://www.youtube.com/watch?v=cf9xDdPXOA0&t=1651s). Tady se dělení práce, komunikace a produktivní nesouhlas učily explicitně, plus Trello kanban se třemi sloupci [(29:05)](https://www.youtube.com/watch?v=cf9xDdPXOA0&t=1745s). U třetího projektu se proto záměrně nezvedala technická laťka: nové bylo „spolu", ne „víc".

**Meta-lekce celého modulu** [(35:33)](https://www.youtube.com/watch?v=cf9xDdPXOA0&t=2133s), a je to nejlepší argument pro malé hry v celé knihovně: rada „dělej malé hry" se obvykle prodává přes dokončování — tady je hlubší verze. **U příliš velké hry klesá relativní kvalita každé její části** — neumíš ještě nic z toho, co děláš, a děláš toho moc; ani deset let práce to nespraví. Malé projekty s konkrétním učebním cílem („teď se učím interface") dovednosti oddělují, brousí — a skládat je budeš potom. „Hrát si na profesionálního vývojáře s vydáním na krku" není učení [(36:19)](https://www.youtube.com/watch?v=cf9xDdPXOA0&t=2179s).

> **Pozn.:** Tři hry, které by si podle videa měl dát každý: (1) čistě interfaceová hra, (2) akční hra na jedné obrazovce bez levelů, (3) kolážový experiment z posbíraných assetů. Dobrý roční plán samouka — a mimochodem přesně v duchu [malých projektů jako tělocvičny](proc-tvorit.md#male-projekty-jsou-telocvicna-ne-ustupek).

**Souvislosti:** [Scope a malé hry](scope.md) · [Proč tvořit](proc-tvorit.md) · [Zápisek: Pravidlo 70/30](../zapisky/pravidlo-70-30.md) · [Rejstřík: Blockout](../rejstrik.md#blockout)
