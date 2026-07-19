# Vydání hry: demo, launch a co přijde potom

O tom, jak hru udělat, existují tisíce videí. O tom, co se děje ve chvíli, kdy je hotová, skoro žádná — a přitom právě tam se rozhoduje, jestli si jí někdo všimne. Tahle kapitola spojuje dva zdroje, které tu mezeru zaplňují z opačných stran: Indie Game Clinic vysvětluje, **co má demo dělat a proč většina dem nefunguje**, a BiteMe Games rozebírají **prvních pár týdnů po vydání** — včetně toho, kolik z hrubé tržby vývojáři reálně zůstane.

---

## Demo prodává, prototyp validuje

**Zdroj:** [Most Steam Demos Suck; Here's Why](https://www.youtube.com/watch?v=1vtqBTX2Lzc) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · ~19 min, esej

**Shrnutí:** Jedno rozlišení pročistí většinu zmatků kolem dem: **demo je tu, aby hru prodalo; playtestovací build je tu, aby ověřil, jestli má hra vůbec být produkt.** Z toho plyne všechno ostatní — kdy co zveřejnit, co v demu musí být a proč je předčasné demo horší než žádné.

### Rozpad myšlenky

Video začíná vzorovým postupem [(0:45)](https://www.youtube.com/watch?v=1vtqBTX2Lzc&t=45s): jedna hra měla dřívější build na itch.io **pod jiným brandingem** jako testovací půdu a na Steam šla teprve potom. Proč je to dobře: **je tam jasná hranice mezi fází „chci, aby to lidi hráli a řekli mi, jestli to stojí za to" a fází „tohle prodávám"**. Nikdo nesbírá wishlisty dřív, než je jasné, že hra baví.

Odtud plyne, co vlastně dostáváš od prvních hráčů [(2:26)](https://www.youtube.com/watch?v=1vtqBTX2Lzc&t=146s): **ne peníze, ale výzkumný čas**. „Lidé, kteří to hrají v mizerném raném stavu, ti dělají laskavost — a to je hodnota, kterou tvé hře poskytují." K tomu praktické pravidlo pro playtest [(3:12)](https://www.youtube.com/watch?v=1vtqBTX2Lzc&t=192s): **čím víc známých problémů v buildu necháš, tím víc zpětné vazby dostaneš o věcech, které už dávno víš** — takže oprav, co víš, a teprve pak testuj.

Historický kontext pomůže pochopit, proč se pojem rozostřil [(3:32)](https://www.youtube.com/watch?v=1vtqBTX2Lzc&t=212s): v devadesátých letech bylo demo **kus hotové hry**, vyříznutý a rozdaný zdarma — to, co jsi hrál v demu, bylo přesně to, co jsi dostal v plné verzi. Dnešní ekosystém tenhle význam smíchal s ranými buildy, early accessem a playtesty, a vývojáři z toho mají zmatek.

Klíčová věta, kolem které je postavené celé video [(5:07)](https://www.youtube.com/watch?v=1vtqBTX2Lzc&t=307s): **„nejsem jazyková policie, ale staneš se lepším vývojářem, když ten rozdíl uvidíš."** Protože prodáváme hry, o kterých **víme**, že baví — a z toho plyne nepříjemný důsledek: **nepředpokládej, že každý projekt, který začneš, má kapacitu být komerčně vydanou hrou** [(5:54)](https://www.youtube.com/watch?v=1vtqBTX2Lzc&t=354s). Video k tomu přidává poznámku o rozšířené záměně [(5:54)](https://www.youtube.com/watch?v=1vtqBTX2Lzc&t=354s): část lidí má v hlavě, že **hra je cokoli, co udělají v enginu** („udělal jsem to v Unity, takže je to hra"). Vývoj hry je ale postupné tvarování kódu, artu a nápadů **ve hru — a to se dělá tím, že to dáváš hráčům**, protože sám ji vždycky testuješ tak, jak má být hraná.

Vlastní praxe autora tuhle logiku ilustruje [(4:20)](https://www.youtube.com/watch?v=1vtqBTX2Lzc&t=260s): hráč z jeho testu **nepochopil vztah mezi utrácením klíčů a otevíráním dveří** — a tak přidal animaci, která tu vazbu ukáže. Podstatné je, kdy: **„nečekal jsem půl roku; jakmile byla hra pár minut zábavná, hned jsem ji dal lidem testovat."**

> **Pozn.:** Tohle je přesně ta fáze, kterou popisuje [validace nápadu playtestem](playtesting.md#proc-testovat-nespolehlivy-svedek-vlastni-hry) — a spolu s ní dává jednoduché pořadí: nejdřív ověř, že hra baví (playtest), pak teprve stav něco, co má přesvědčit cizí lidi (demo). Kdo to prohodí, dělá marketing hře, o které ještě neví, jestli má být vydaná.

**Souvislosti:** [Playtesting: proč testovat](playtesting.md#proc-testovat-nespolehlivy-svedek-vlastni-hry) · [Prototypování: tři brány](prototypovani.md#tri-brany-gameplay-prototyp-vertical-slice-produkce) · [Rejstřík: demo](../rejstrik.md#demo) · [Rejstřík: vertical slice](../rejstrik.md#vertical-slice)

---

## Vertikální a horizontální řez: jak vybrat, co do dema dát

**Zdroj:** [Most Steam Demos Suck; Here's Why](https://www.youtube.com/watch?v=1vtqBTX2Lzc) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · druhá půlka eseje

**Shrnutí:** Většina hráčů čeká od dema **vertical slice** — kousek hry v cílové kvalitě. Nejčastější chyba není špatná kvalita, ale **příliš úzký řez**: demo z tutoriálu naznačí systémy, které pak neukáže. A pro některé žánry je vertical slice špatný nástroj — pomalé hry o odemykání potřebují **horizontal slice**: celou hru, ale skrz zlomek jejích systémů.

### Rozpad myšlenky

Nejdřív upřesnění, které se hodí znát [(6:41)](https://www.youtube.com/watch?v=1vtqBTX2Lzc&t=401s): v průmyslové terminologii **vertical slice není totéž co veřejné demo** — je to **stav, ve kterém build může být**, používaný pro interní kontrolu kvality nebo pro publishera. Ale protože hráči od dema čekají právě tohle, splývá to. Definice sama je prostorová [(7:27)](https://www.youtube.com/watch?v=1vtqBTX2Lzc&t=447s): hra je **vodorovná časová osa zážitku**; vertical slice ji **přeřízne napříč** a vezme třeba pět procent hry — ale ta část **působí v kvalitě, art stylu a pocitu jako hotová hra**.

Chyba, kterou video pojmenovává jako „diagonální řez" [(9:02)](https://www.youtube.com/watch?v=1vtqBTX2Lzc&t=542s), je zákeřná právě proto, že vzniká z rozumného rozhodnutí: vezmeš první level, protože je hotový nejdřív. Jenže v tom levelu **jsou v rozhraní naznačené systémy, které hra potřebuje — inventář, magie, crafting — a demo je jen odmávne**. Z pohledu hráče popáleného early accessem to nevypadá jako „tohle přijde později", ale jako „tohle možná neexistuje". Pravidlo z toho plyne tvrdé [(9:48)](https://www.youtube.com/watch?v=1vtqBTX2Lzc&t=588s): **je-li tvým demem první level, musí obsahovat všechno, čím hra je**. Má-li hra dvě poloviny — třeba souboj a budování základny — a druhá přijde až za tři hodiny, **hráč z dema nepochopil, co tvoje hra vlastně je**.

Pozitivní protipříklad [(10:35)](https://www.youtube.com/watch?v=1vtqBTX2Lzc&t=635s): demo, které bylo dost dlouhé na to, aby přesvědčilo o neobvyklé kombinaci útulnosti a hororu. Autor to formuluje jako definici úspěchu: **„demo dělá svou práci: najde člověka, který může být ideálním publikem, a dokáže mu, že hra je to, co slibuje."**

**Horizontal slice** [(12:08)](https://www.youtube.com/watch?v=1vtqBTX2Lzc&t=728s) je odpověď pro žánry, kde vertical slice selhává. Vertikální řez totiž předpokládá, že se **všechny podstatné části hry vejdou do jednoho úseku** — hodina, ve které stihneš boss fight i crafting. U pomalé hry o postupném odemykání to neplatí. Horizontální řez proto **řízne napříč, ale odřízne obsah z obou stran: dá ti celou hru, jen skrz třicet až čtyřicet procent jejích systémů** [(12:55)](https://www.youtube.com/watch?v=1vtqBTX2Lzc&t=775s). Historický příklad: Prison Architect šel do early accessu **jen se sandboxem, bez kampaně**.

Kdy po něm sáhnout [(13:42)](https://www.youtube.com/watch?v=1vtqBTX2Lzc&t=822s): u manažerských her, budovatelských strategií a 4X, kde si člověk sedne na několik hodin a odehraje jeden scénář. **Aby hráč pochopil, jaká ta hra je, musí odehrát celou seanci — tak mu ji dovol, jen mu nedávej celý strom technologií.** Prakticky: strategie s jedinou hratelnou frakcí, survival bez některých větví craftingu. A co vynecháš, **naznač jako slib do plné verze** — rozdíl proti „diagonálnímu řezu" je v tom, že **hráč odehrál všechny základní mechaniky** a chybí mu jen obsah, který je používá dál [(14:28)](https://www.youtube.com/watch?v=1vtqBTX2Lzc&t=868s).

Nakonec test, který shrnuje celou kapitolu do jedné otázky [(11:22)](https://www.youtube.com/watch?v=1vtqBTX2Lzc&t=682s): **„představ si někoho, komu se líbí jádro tvého nápadu — ale má pochybnosti. Jaké? A co mu můžeš ukázat, abys je rozptýlil? To je vlastně celý design."** Dobré demo tedy **odpovídá na pochybnosti jádrového publika** a dává důvěru, že hru dokážeš dokončit, i když hotová ještě není.

> **Pozn.:** Video zavírá varováním, které stojí za zapamatování [(16:02)](https://www.youtube.com/watch?v=1vtqBTX2Lzc&t=962s): **fanoušci tvého žánru odehráli víc her toho žánru než ty** — „logistická realita: čas, který ty trávíš tvorbou, oni tráví hraním". Působí-li tvoje demo, že v tom žánru nejsi doma a něco skrýváš, poznají to. A jsou to zrovna oni, kdo o hrách píší a natáčejí: **„cokoli, co působí, že se je snažíš ošidit, je pro tvou hru rozsudek smrti."**

**Souvislosti:** [Prototypování: vertical slice](prototypovani.md#tri-brany-gameplay-prototyp-vertical-slice-produkce) · [Playtesting: škálování po fázích](playtesting.md#kdo-testuje-a-jak-skalovat-road-test-pred-stress-testem) · [Steam stránka](steam-stranka.md#tvar-stranky-capsule-a-short-description) · [Rejstřík: horizontal slice](../rejstrik.md#horizontal-slice) · [Rejstřík: early access](../rejstrik.md#early-access)

---

## Prvních deset recenzí a rytmus slev

**Zdroj:** [What nobody tells you about releasing a game on Steam...](https://www.youtube.com/watch?v=uQnIkK6BOLQ) · [BiteMe Games](https://www.youtube.com/channel/UCHUgO0pyXWkGnQUYp5JgoUg) · ~22 min, z první ruky

**Shrnutí:** Po vydání přestává platit skoro všechno, co jsi dělal předtím — a nastupují dvě mechaniky, které rozhodují o viditelnosti: **prvních deset recenzí** (dokud je nemáš, algoritmus tě prakticky nevidí) a **naplánované slevy** (hlavní zdroj návštěvnosti po prvních týdnech). K tomu jedno varování: se Steam kurátory nekomunikuj.

### Rozpad myšlenky

Video vzniklo z otázky, která se na fórech opakuje každý týden — „zaplavili nás kurátoři žádostmi o klíče, co je standardní praxe?" — a shrnuje mezeru v obsahu o vývoji her [(0:01)](https://www.youtube.com/watch?v=uQnIkK6BOLQ&t=1s): **„spousta videí ‚jak udělat hru' a málo ‚udělal jsem hru, co se teď sakra děje'."**

**Kurátoři: nekomunikuj** [(0:47)](https://www.youtube.com/watch?v=uQnIkK6BOLQ&t=47s). Autor má firemní pravidlo, že e-mail obsahující slovo „curator" jde rovnou do koše, a doloží obě varianty, jak to dopadá. Když jim pošleš **klíče**, skončí v přeprodeji — a má to ověřené: klíč, který kurátorovi dal, později **našel v prodeji, koupil ho a nechal si vrátit peníze**. Když použiješ **Curator Connect** (kde klíč nedostanou), přijde druhá past [(1:33)](https://www.youtube.com/watch?v=uQnIkK6BOLQ&t=93s): **oprávnění nejde odebrat**, takže jakmile mají build, můžou **pirátskou verzi donekonečna aktualizovat**, aniž by hru kdy koupili.

**Deset recenzí je práh viditelnosti** [(6:58)](https://www.youtube.com/watch?v=uQnIkK6BOLQ&t=418s). Video to ukazuje na vlastním grafu: po vydání malý vrchol návštěvnosti, který rychle opadl — a **výrazně větší vrchol přesně v den, kdy hra získala desátou recenzi**. Formulace je jednoznačná: **„dokud nemáš deset recenzí, pro algoritmus skoro neexistuješ."** Praktické důsledky:

- Požádej lidi, kteří hru už znají — **playtestery z Discordu, kamarády, kolegy** — ať recenzi napíšou hned po vydání [(8:31)](https://www.youtube.com/watch?v=uQnIkK6BOLQ&t=511s).
- **Darované kopie a klíče se nepočítají**: recenze je platná, jen když si hru člověk sám koupil [(8:31)](https://www.youtube.com/watch?v=uQnIkK6BOLQ&t=511s).
- Na tom, jestli jsou první recenze pozitivní, autorovi tolik nezáleží — **jde o překročení prahu**. „Trvá-li to víc než den, hra není mrtvá, ale růst je extrémně zakrnělý."

**Slevy naplánuj hned** [(1:33)](https://www.youtube.com/watch?v=uQnIkK6BOLQ&t=93s). Po prvních týdnech jsou slevy hlavní způsob, jak se ke hře dostane návštěvnost: **„tři měsíce po vydání prodáš víc za ten jeden týden ve slevě než za zbylých pět týdnů pauzy."** Důvod je prostý — lidé s hrou na seznamu přání čekají na vhodný okamžik. V nastavení obchodu se dají **naplánovat všechny termíny dopředu, klidně na rok** [(2:20)](https://www.youtube.com/watch?v=uQnIkK6BOLQ&t=140s), a systém sám hlásí kolize s festivaly. Dvě pravidla, která u toho platí:

1. **Kromě uvítací slevy vždycky aspoň dvacet procent** [(3:06)](https://www.youtube.com/watch?v=uQnIkK6BOLQ&t=186s). Steam totiž **pošle e-mail lidem se hrou na seznamu přání jen tehdy, když sleva dosáhne dvaceti procent** (na launchi přijde vždy). **Patnáctiprocentní sleva proto nemá skoro žádný dopad — nikdo se o ní nedozví.**
2. **Nepanikař s tempem** [(4:40)](https://www.youtube.com/watch?v=uQnIkK6BOLQ&t=280s). Doporučená posloupnost: dvakrát dvacet procent, dvakrát dvacet pět, teprve pak třicet a výš. **„Někdo koupí až při padesáti procentech, ale není důvod tam skákat hned, když spousta lidí koupí při dvaceti — takhle jen ztrácíš peníze."** A důležitá korekce očekávání: **hlubší sleva nespraví špatné recenze.**

> **Pozn.:** Detail, který se v návodech objevuje málokdy [(6:12)](https://www.youtube.com/watch?v=uQnIkK6BOLQ&t=372s): **dvoutýdenní slevy místo jednotýdenních**. Pauza mezi slevami je stejně dlouhá tak jako tak, takže při delší slevě dostaneš stejnou viditelnost a víc prodejů. Autor to sám nezkusil, ale slyší to od kolegů — a poctivě to jako neověřené označuje.

**Souvislosti:** [Steam stránka](steam-stranka.md#neviditelna-masinerie-embeds-lokalizace-tagy-datum) · [Playtesting: kde brát testery](playtesting.md#moderovany-playtest-divej-se-co-delaji-ne-co-rikaji) *(titíž lidé napíšou první recenze)* · [Postmortem ShantyTown: ticho po launchi](postmortem-shantytown.md#wishlisty-next-fest-a-ticho-po-launchi) · [Přežít jako studio: rychlost jako strategie](prezit-jako-studio.md#rychlost-jako-strategie-mmo-98-za-sest-tydnu) *(NextFest ze strany studia, které stránku pustilo čtyři dny předem)* · [Rejstřík: wishlist](../rejstrik.md#wishlist)

---

## Po vydání: recenze, past updatů a co ti reálně zbyde

**Zdroj:** [What nobody tells you about releasing a game on Steam...](https://www.youtube.com/watch?v=uQnIkK6BOLQ) · [BiteMe Games](https://www.youtube.com/channel/UCHUgO0pyXWkGnQUYp5JgoUg) · druhá půlka videa

**Shrnutí:** Tři věci, o kterých se mluví nejmíň: **na negativní recenze se neodpovídá**, **dlouhé opravování vydané hry je past** (další hra vynese víc než záchrana téhle) a **z hrubé tržby ti zbyde zhruba polovina** — a to ještě před zdaněním. A na konec rada, kterou by si měl přečíst každý, kdo míří k vydání: naplánuj si pauzu.

### Rozpad myšlenky

**Negativní recenze: přečti, nereaguj** [(9:18)](https://www.youtube.com/watch?v=uQnIkK6BOLQ&t=558s). Autor to podává jako dovednost, kterou je potřeba si vypěstovat: **„ty recenze nemíří na tebe jako člověka, ale na hru — a protože jsi hře tak blízko, působí to jako útok na tebe."** Odpovídání podle jeho zkušenosti skoro vždy uškodí: vývojáři reagují emocionálně („takhle jsi to hrát neměl", „to je jen tvůj názor") a **sklidí za to další negativní hodnocení**. Zmiňuje i případ, kdy vývojářské odpovědi lidé přečetli jako **žebrání o kladné recenze**. Taktiku „opravili jsme to, změníte hodnocení?" sami zkusili [(10:50)](https://www.youtube.com/watch?v=uQnIkK6BOLQ&t=650s): **je nepříjemná a má malý účinek, protože většina lidí recenzi nezmění**. Jediná bezpečná verze je **čistě faktická informace** („tenhle problém je vyřešený, tady jsou poznámky k verzi") bez proseb.

**Past post-launch updatů** [(11:36)](https://www.youtube.com/watch?v=uQnIkK6BOLQ&t=696s) je nejcennější část videa, protože jde proti instinktu. Když hra nevyjde podle představ, člověk se ji přirozeně snaží zachránit — a autor viděl vývojáře, kteří v tom uvízli na půl roku. Proti tomu staví fakt: **„tvoje hra už nikdy nebude mít takový zájem jako při vydání."** Doporučený rytmus [(12:22)](https://www.youtube.com/watch?v=uQnIkK6BOLQ&t=742s):

- **První týden hasíš požáry** — chyby v ukládání, otravné drobnosti; shipuj rychle, dokud má každá recenze velkou váhu.
- Pak se provoz uklidní. **Přečti si všechny recenze a diskuze, zjisti, jak lidé hru doopravdy hrají, a naplánuj jeden velký update** [(13:09)](https://www.youtube.com/watch?v=uQnIkK6BOLQ&t=789s) — u nich to byla jedna mechanika navíc plus balík vylepšení pohodlí.
- Ten vydej a **jdi dál**. S jednou sociální poznámkou: **neoznamuj hlasitě, že končíš s podporou** — „když ti zaplatí sedm dolarů, mají pocit, že jim dlužíš celý život" [(13:56)](https://www.youtube.com/watch?v=uQnIkK6BOLQ&t=836s).

Argument, proč jít dál, je ekonomický i lidský: **přínos další, lepší hry — teď, když víš víc — je nesrovnatelně vyšší než záchrana hry, která nezískala trakci**. „Ano, Among Us to dokázal. **Ne, ty nejsi Among Us.**" A navíc **budeš z té hry vyhořelý**, takže i tvoje práce na ní bude horší [(13:56)](https://www.youtube.com/watch?v=uQnIkK6BOLQ&t=836s). Doprovodné měření: takzvaná kola viditelnosti po velkém updatu jim přinesla **2 500 zobrazení a 78 návštěv stránky** [(14:43)](https://www.youtube.com/watch?v=uQnIkK6BOLQ&t=883s) — tedy prakticky nic.

**Kolik ti reálně zbyde** [(15:29)](https://www.youtube.com/watch?v=uQnIkK6BOLQ&t=929s) je pasáž, kterou by si měl přečíst každý, kdo si plánuje život podle čísla na dashboardu. Autor ukazuje rozpad na vlastní hře:

- **Hrubá tržba za dva měsíce: 70 000 dolarů.**
- Po refundacích, třicetiprocentním podílu obchodu a odvedených daních přišla **výplata zhruba 40 000 dolarů** — „třicet tisíc pryč v mžiku" [(16:16)](https://www.youtube.com/watch?v=uQnIkK6BOLQ&t=976s).
- Banka si vzala **48 dolarů za přijetí platby v cizí měně** a **dalších 402 dolarů za převod na eura** — dohromady **450 dolarů jen za pohyb peněz** [(17:02)](https://www.youtube.com/watch?v=uQnIkK6BOLQ&t=1022s). Doporučení: **neobanka to zvládne řádově levněji** (v jeho srovnání zhruba za čtvrtinu).
- **Ze 70 000 dolarů hrubého zbyla po převodu zhruba polovina** — a to **před daní ze zisku firmy a před zdaněním výplaty sobě** [(18:38)](https://www.youtube.com/watch?v=uQnIkK6BOLQ&t=1118s).

Závěr je proto varovný: **„nedělej tu chybu, že se podíváš na celkovou tržbu a začneš si podle hrubého čísla stavět život."**

> **Pozn.:** Poslední rada je nečekaně měkká a stojí za citaci [(19:25)](https://www.youtube.com/watch?v=uQnIkK6BOLQ&t=1165s): **„launch je nejdůležitější událost v životním cyklu hry — víc než kterákoli část vývoje nebo cokoli po něm"**, a proto tě poslední týdny pohltí. Jenže pak **musíš uhasit ještě jeden požár: sám sebe.** Dej si týden — a jsi-li typ, který se z nicnedělání zblázní, ať je to **práce s nízkou sázkou**. A hlavně: **nepovažuj první nápad, který po vydání dostaneš, za hru, které dáš dalšího půl roku života.**

**Souvislosti:** [Žrouti času: motivace a dokončování](produktivita.md#motivace-startuje-disciplina-dokoncuje) · [Scope: malé hry se sčítají](scope.md#male-hry-se-scitaji) *(proč je další hra lepší investice než záchrana téhle)* · [Data o úspěchu: křivka přežití](data-o-uspechu.md#krivka-preziti-proc-se-sance-zlepsuji-s-patou-hrou) · [Postmortem ShantyTown](postmortem-shantytown.md#wishlisty-next-fest-a-ticho-po-launchi) · [Rejstřík: refundace](../rejstrik.md#refundace)
