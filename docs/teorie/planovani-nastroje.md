# Plánovací nástroje: kanban pro gamedev

Jednou přijde bod, kdy „mám to v hlavě" přestane stačit — sólo dřív, než čekáš, v týmu okamžitě. Indie Game Clinic ukazuje na reálném jamovém projektu, jak vede hru přes Trello: nejdřív *co* dělat (karty, sloupce, pravidla), pak *proč* zrovna takhle (kanban jako metodologie, ne jen software). A přidává kariérní poznámku pod čarou: kdo tohle na projektech dělá, dělá práci producenta. Poslední myšlenka jde o krok před board: jak velkou featuru [rozpadnout](#hora-po-kamenech-featuru-rozpadni-dokud-nejde-dokoncit-za-jedno-sezeni), aby se dala dokončit.

---

## Kanban: karty zleva doprava a jeden vlastník na kartu

**Zdroj:** [Manage Your GameDev Projects with Trello/Kanban](https://www.youtube.com/watch?v=-SqcrlAarGo) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · ~22 min, živá ukázka na jamovém projektu

**Shrnutí:** Kanban je systém, Trello jen jedna z jeho aplikací (jde to i v Jira, Notionu…): úkoly zhmotněné do karet, které putují zleva doprava přes **To Do → Doing → Done**. Aby to fungovalo, potřebují karty tři vlastnosti: správnou zrnitost (dost malé, aby šly dokončit), jednoho vlastníka (když jsou zodpovědní dva, není zodpovědný nikdo) a limit rozdělanosti (kdo „dělá" tři věci, nedělá pořádně žádnou).

### Rozpad myšlenky

Video staví board pro skutečný projekt — RPG Maker hru na davidlynchovský game jam [(0:48)](https://www.youtube.com/watch?v=-SqcrlAarGo&t=48s) — takže karty nejsou akademické. Základní mechanika [(1:35)](https://www.youtube.com/watch?v=-SqcrlAarGo&t=95s): To Do = nikdo na tom nedělá; Doing = někdo na tom dělá *a je na kartě podepsaný*; Done. Karty unesou obrázky (WIP screenshot jako obálka dělá board míň odstrašující [(7:46)](https://www.youtube.com/watch?v=-SqcrlAarGo&t=466s)) a checklisty.

**Zrnitost** [(3:07)](https://www.youtube.com/watch?v=-SqcrlAarGo&t=187s): karta „udělej celý level design" se nikdy nedokončí. Úkol zní „vytvoř první drafty klíčových lokací" — a lokace jsou checklist v kartě, nebo samostatné karty; kde je hranice, se ukáže, až se seznam zaplní [(3:54)](https://www.youtube.com/watch?v=-SqcrlAarGo&t=234s). S tím souvisí kvalita zadání [(10:06)](https://www.youtube.com/watch?v=-SqcrlAarGo&t=606s): kanban předpokládá lidi, kteří si práci berou sami — a to jde jen, když karta obsahuje, co je potřeba (velikost spritů, paleta…). Čím granulárnější a lépe popsané karty, tím míň dotazů [(10:54)](https://www.youtube.com/watch?v=-SqcrlAarGo&t=654s).

**Jeden vlastník** [(5:31)](https://www.youtube.com/watch?v=-SqcrlAarGo&t=331s): rozdíl mezi metodou (klikám jako v tutorialu) a metodologií (rozumím pravidlům pod tím). Karta „level design a environmental art" se dvěma lidmi se musí rozpadnout na dvě karty — **když jsou za věc zodpovědní dva, není za ni zodpovědný nikdo** [(6:00)](https://www.youtube.com/watch?v=-SqcrlAarGo&t=360s). Závislosti hlídej stejně věcně: „projdi drafty a urči chybějící tiles" nesmí být v Doing současně s kartou draftů, na které stojí [(6:59)](https://www.youtube.com/watch?v=-SqcrlAarGo&t=419s).

**Limit rozdělanosti** [(11:40)](https://www.youtube.com/watch?v=-SqcrlAarGo&t=700s): prostřední sloupec má mít nejméně karet. „Kdo tvrdí, že právě dělá tři věci, v podstatě lže — jednu dělá a ostatní ignoruje, nebo mezi nimi těká." Pravidlo: jedna, maximálně dvě karty na osobu [(12:26)](https://www.youtube.com/watch?v=-SqcrlAarGo&t=746s). Doing je totiž hlavně **komunikační kanál**: deklaruje, na co se dnes soustředíš — spoluhráč vidí „děláme na stejném, ideální čas na můj dotaz", a naopak Gary s pěti kartami v Doing neříká nikomu nic [(12:26)](https://www.youtube.com/watch?v=-SqcrlAarGo&t=746s). Přepínáš práci? Kartu s 2/15 checklistu klidně vrať do To Do — board má říkat pravdu o dnešku, ne evidovat ambice [(13:12)](https://www.youtube.com/watch?v=-SqcrlAarGo&t=792s).

K tomu barevné **labels** podle kategorií (zelená art, modrá writing — artista skenuje jen zelené; colorblind mode přidá textury [(8:32)](https://www.youtube.com/watch?v=-SqcrlAarGo&t=512s)) a svislá osa jako priorita (nahoře = další na řadě) [(17:52)](https://www.youtube.com/watch?v=-SqcrlAarGo&t=1072s).

> **Pozn.:** „Jedna karta v Doing" je nástrojová verze fokusu ze [žroutů času](produktivita.md#motivace-startuje-disciplina-dokoncuje) — a granularita karet je totéž pravidlo, kterým [minimalistický GDD](gdd.md#gdd-minimalisticky-skica-vsech-oblasti-ne-bible-jedne) drží sekce malé: velké kusy se nedokončují.

**Souvislosti:** [Scope: nápad zaparkuj, nezabíjej](scope.md#scope-creep-napad-zaparkuj-nezabijej) *(odkud se board plní)* · [Produktivita](produktivita.md) · [GDD](gdd.md) *(dokument říká co a proč, board kdo a kdy)* · [Rejstřík: kanban](../rejstrik.md#kanban) · [Rejstřík: WIP limit](../rejstrik.md#wip-limit)

---

## In Review, backlog a role producenta

**Zdroj:** [Manage Your GameDev Projects with Trello/Kanban](https://www.youtube.com/watch?v=-SqcrlAarGo) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · rozšíření a kontext

**Shrnutí:** Tři sloupce stačí, dokud si klademe jen otázku „dělá se na tom?". Dvě situace chtějí čtvrtý a pátý: **In Review** („hotovo" nemá vyhlašovat ten, kdo úkol dělal) a **backlog** (na dlouhém projektu se To Do rozpadne na „všechno, co hru čeká" a „priority tohohle sprintu"). A kdo boardu vládne, dělá — aniž si to možná napsal do CV — produkci.

### Rozpad myšlenky

**In Review** [(14:44)](https://www.youtube.com/watch?v=-SqcrlAarGo&t=884s): když sám prohlásím combat demo za hotové, znamená to jen, že *já* si to myslím — sign-off patří někomu jinému. Čtvrtý sloupec mezi Doing a Done říká „čeká na cizí oči". Kdy se vyplatí: prvky procházející více rukama, junioři, kterým je nepříjemné podepisovat si vlastní práci (nebo jim to ještě nechceš dovolit), a nové týmy, kde se teprve hledá, jak se spolupracuje [(15:30)](https://www.youtube.com/watch?v=-SqcrlAarGo&t=930s) — autor ho na jamu drží právě proto, že se s lidmi zná krátce a role se překrývají [(17:04)](https://www.youtube.com/watch?v=-SqcrlAarGo&t=1024s).

**Backlog + sprint To Do** [(16:17)](https://www.youtube.com/watch?v=-SqcrlAarGo&t=977s): na projektu na měsíce a roky se To Do stane **backlogem** — „všechno, co je potřeba udělat, aby hra byla hotová, navždy" — a mezi něj a Doing se vloží užší seznam: co jsme si na sprint meetingu (týden, dva) vybrali jako priority. Lidi si pak berou práci z priorit, ne z nekonečna. Autor přiznává, že tohle už je „míň kanban, víc agile scrum" [(17:04)](https://www.youtube.com/watch?v=-SqcrlAarGo&t=1024s) — pro měsíční jam zbytečné, pro dlouhý projekt zásadní.

**Tohle je produkce** [(18:38)](https://www.youtube.com/watch?v=-SqcrlAarGo&t=1118s): producent ve hrách = project manager — člověk, který zná timeline, drží velký seznam úkolů a ví, kdo co dělá a kdo je volný. (Titul „producent" znamená v každém médiu něco jiného — ve hrách je to tohle [(19:26)](https://www.youtube.com/watch?v=-SqcrlAarGo&t=1166s).) Důsledek pro samouky: kdo vede boardy na jamech s kamarády, **sbírá reálnou producentskou praxi** — je to role, kterou jde v industry dělat [(19:26)](https://www.youtube.com/watch?v=-SqcrlAarGo&t=1166s). Kdo chce dál: kanban, agile scrum a jejich kříženec scrumban jsou zdokumentované metodologie k dostudování [(20:12)](https://www.youtube.com/watch?v=-SqcrlAarGo&t=1212s) — autor s odzbrojující upřímností dodává, že jeho produkční teorie nudí.

> **Pozn.:** Závěr videa je delší blok podpory kanálu (Patreon, členství, Discord komunita) [(20:58)](https://www.youtube.com/watch?v=-SqcrlAarGo&t=1258s) — ne sponzor, ale promo. — Rytmus „sprint meeting nad backlogem" je tentýž stroj jako měsíční bloky z [obrany proti scope creepu](scope.md#scope-creep-napad-zaparkuj-nezabijej): tam se rozhoduje, *co* si zaslouží práci, tady se to rozhodnutí provádí.

**Souvislosti:** [Scope creep](scope.md#scope-creep-napad-zaparkuj-nezabijej) · [Playtesting: kadence](playtesting.md#kadence-vlny-a-rite-playtest-jako-motor-iterace) *(sprint končí testem)* · [Sólo vývoj](solo-vyvoj.md) · [Rejstřík: backlog](../rejstrik.md#backlog) · [Rejstřík: producent](../rejstrik.md#producent) · [Rejstřík: scrum](../rejstrik.md#scrum)

---

## Nástroje full-time indie vývojáře a jedna věc navíc, která není software

**Zdroj:** [The Tools I Use For Full Time Indie Game Development](https://www.youtube.com/watch?v=mrVM2zehqiw) · [Firebelley Games](https://www.youtube.com/channel/UC89NzFUOsBrjRSJt4Y8s6WQ) · ~12 min, přehled

**Shrnutí:** Autor přešel na plný úvazek a jako důvod, proč si to mohl dovolit, jmenuje něco nečekaného: **usazený set nástrojů a workflow**. Přehled je celý postavený na free a levných věcech (Godot, VS Code, Obsidian, Git, Aseprite, DaVinci Resolve, OBS) a rozpadá se do tří vrstev — vývoj, obsah o hře, a záloha. Háček, na kterém stojí ta poslední: **jediná položka na seznamu, která není software, je redundantní zálohovací řetěz** — a jediná, kterou označuje za nutnost.

### Rozpad myšlenky

**Vývojová vrstva** [(0:46)](https://www.youtube.com/watch?v=mrVM2zehqiw&t=46s): **Godot** (MIT licence, žádné poplatky ani registrace — *„nemáš co ztratit kromě minuty, než se to stáhne"*), **VS Code** místo velkých IDE (*„zkoušel jsem Visual Studio i Rider a vždycky se vracím"*), a **Obsidian** na poznámky, protože **drží soubory u tebe na disku** v Markdownu. Poznámka k Obsidianu je jádro celé rady o poznámkových nástrojích: vlastnictví dat je důležitější než funkce.

**Git jako nesmlouvavá položka** [(4:41)](https://www.youtube.com/watch?v=mrVM2zehqiw&t=281s) a vysvětlení pro člověka, který ho nikdy nepoužil: commit obsahuje **jen změny od minulého commitu**, takže když je děláš často, vzniká historie, do které se dá kdykoli vrátit. Argument, který zabírá nejvíc, je ten o ladění: *„uděláš širokou změnu a něco úplně rozbiješ — můžeš pročesat historii a najít, co to způsobilo. Nebo když to zvoráš pořádně, prostě změny zahodíš."* GitHub k tomu přidává **zálohu a dostupnost odkudkoli**.

**Grafika a zvuk** [(6:15)](https://www.youtube.com/watch?v=mrVM2zehqiw&t=375s): **Aseprite** za ~20 $ (*„za takový software je to lup"*) — vrstvy, animace, palety, export do sprite sheetů i jednotlivých souborů, komunitní skripty. Pro zvuk **Sonniss GDC bundly** (gigabajty efektů zdarma) s praktickou poznámkou, že se v tom **špatně hledá**, takže si na to bere vyhledávací nástroj a přehrává si výsledky rovnou. Dál itch.io s upozorněním, které se opakovat vyplatí: **vždycky zkontroluj licenci a hledej takovou, která výslovně dovoluje komerční užití.** Hudbu si pro vážný projekt nechává složit — *„je to drahé, ale hudba je jádrem identity hry"* — s Fiverrem a Upworkem jako místy, kde hledat, a Beepboxem jako rozpočtovou variantou.

**Marketingová vrstva** [(8:34)](https://www.youtube.com/watch?v=mrVM2zehqiw&t=514s) je ta, na kterou se u „nástrojů pro vývoj" zapomíná, a autor ji bere jako součást práce: **DaVinci Resolve** na dlouhá videa, **OBS** na záznam a stream, **HandBrake** na zmenšení souboru pro sociální sítě a **Lossless Cut** na vyříznutí kousku z delšího záznamu **bez ztráty kvality**. Ta dvojice HandBrake + Lossless Cut je konkrétní workflow: vystřihni klip, zmenši, publikuj.

**A ta jediná nesoftwarová položka** [(10:07)](https://www.youtube.com/watch?v=mrVM2zehqiw&t=607s). Autor předesílá, že se všechno ostatní dá dělat i na slabém stroji, a pak jmenuje **NAS synchronizovaný každou noc do cloudové zálohy**. Zálohuje tam projekty, fotky, dokumenty, assety i syrové video. Formulace, kterou stojí za to vzít doslova: *„je-li tvoje živobytí závislé na produkci digitálních dat, tuhle úroveň redundance chceš — a podle mě potřebuješ."*

> **Pozn.:** Video obsahuje **placený segment o projektovém nástroji** (autor to přiznává) a my ho tu vědomě neopakujeme — kanban jako metoda má v této kapitole [vlastní výklad](#kanban-karty-zleva-doprava-a-jeden-vlastnik-na-kartu), který je na konkrétním softwaru nezávislý. Zajímavější je, co z toho přehledu plyne obecně: **skoro celý seznam je zdarma nebo do dvaceti dolarů.** Bariéra vstupu do vývoje her dnes není v nástrojích — a to znamená, že „nemám na software" je výmluva, kterou je potřeba škrtnout ze seznamu. Zbývají dvě reálné bariéry, čas a znalost, a na ty se hodí [pravidlo o konzistenci](jak-se-ucit-kodovat.md#rozbij-to-schvalne-kdy-je-kod-konecne-tvuj). Za zmínku stojí i shoda dvou nezávislých zdrojů na Asepritu — totéž doporučuje [tutoriál na pixel art pro Godot](../godot/2d-svet.md#pixel-art-do-godotu-paleta-silueta-a-jedno-nastaveni).

**Souvislosti:** [Kanban](#kanban-karty-zleva-doprava-a-jeden-vlastnik-na-kartu) · [Organizace projektu: Git v Unrealu](../praxe/organizace-projektu.md#git-v-unrealu-verzovani-z-editoru-a-cesta-zpet-v-case) *(týž nástroj z enginové strany)* · [Godot: pixel art do Godotu](../godot/2d-svet.md#pixel-art-do-godotu-paleta-silueta-a-jedno-nastaveni) · [Devlogy](devlogy.md) *(k čemu je ta marketingová vrstva)* · [Rejstřík: Version control](../rejstrik.md#version-control) · [Rejstřík: Git LFS](../rejstrik.md#git-lfs)

---

## Hora po kamenech: featuru rozpadni, dokud nejde dokončit za jedno sezení

**Zdroj:** [The Breakdown Method: The Secret to Finishing Your Game](https://www.youtube.com/watch?v=wAe6b3IpSh0) · [Unreal University](https://www.youtube.com/channel/UCQv4mwerZLQVe3wPbsMc-qw) · ~8 min, rada

**Shrnutí:** Unreal University vysvětluje, proč se hry nedodělávají. Problém nebývá nápad, ale velikost úkolu a snaha vzít ho celý najednou. Přehlcený vývojář se zasekne a uteče k novému projektu, který zatím nemá žádné nevyřešené problémy, a celé se to opakuje. Lékem je rozpad: featura se dělí tak dlouho, až jde každý kus dokončit za jedno sezení. Háček: nepomůže to projektu, který pořád roste o nové featury. To je podle videa jiný boj.

### Rozpad myšlenky

**Proč se to zasekne.** Začneš zábavnými částmi, postavou a pohybem, a pak zjistíš, kolik ještě zbývá: souboj, UI, ukládání, nepřátelé [(0:02)](https://www.youtube.com/watch?v=wAe6b3IpSh0&t=2s) [(0:49)](https://www.youtube.com/watch?v=wAe6b3IpSh0&t=49s). Nový nápad láká, protože nemá žádnou zátěž ani nevyřešené problémy. Jenže i ten časem ztěžkne a kolo se točí znovu. Podle videa se nemusí měnit projekt, ale způsob práce [(1:36)](https://www.youtube.com/watch?v=wAe6b3IpSh0&t=96s).

**Rozpad.** Nepracuj na hře, ale na nejmenším možném kusu. Dům se staví cihla po cihle a střecha přijde, až je pod ní pevný základ [(2:23)](https://www.youtube.com/watch?v=wAe6b3IpSh0&t=143s). Souboj se rozpadne na pohyb hráče, animaci úderu a detekci zásahu a každý kus jde dokončit za jedno sezení. Mozek se přestane vypínat, protože úkol před ním je zvládnutelný. Pomáhají menší kusy a soustředění, ne delší sezení [(3:11)](https://www.youtube.com/watch?v=wAe6b3IpSh0&t=191s).

**Příklad s lodí.** Vágní „systém lodi" nejdřív potřebuje přesnou definici: loď, kterou hráč řídí, palivo, a když palivo dojde, vrátí hra hráče na startovní ostrov [(3:11)](https://www.youtube.com/watch?v=wAe6b3IpSh0&t=191s). Pak přijde rozpad na čtyři úkoly. Model lodi ve světě, nastoupení a řízení, palivo ubývající za jízdy a kontrola nuly s teleportem zpět [(3:59)](https://www.youtube.com/watch?v=wAe6b3IpSh0&t=239s). Když je úkol pořád velký, rozpadne se znovu, třeba na widget s palivem a jeho zobrazení po nastoupení. Ze seznamu pak stačí vybrat nejsnazší úkol, protože když jednou začneš, snáz pokračuješ [(4:45)](https://www.youtube.com/watch?v=wAe6b3IpSh0&t=285s).

**Hora.** Po týdnu nebo dvou se podíváš na seznam a začne tě trochu stresovat, kolik zbývá [(5:31)](https://www.youtube.com/watch?v=wAe6b3IpSh0&t=331s). Pohled upřený jen na vrchol pokrok zakrývá, a proto se vyplatí dívat se na další krok. Pomáhá otázka na tento týden: jaká jedna smysluplná věc mě posune? Někdo si řekne „dokončím za šest měsíců", jenže podle videa pak šest měsíců uplyne a neudělá nic [(6:17)](https://www.youtube.com/watch?v=wAe6b3IpSh0&t=377s). Malé výhry se skládají a z nich je nakonec hotová hra [(7:04)](https://www.youtube.com/watch?v=wAe6b3IpSh0&t=424s).

> **Pozn.:** Rozpad je metoda k pravidlu o zrnitosti z [Kanbanu](#kanban-karty-zleva-doprava-a-jeden-vlastnik-na-kartu): karta „udělej celý level design" se nikdy nedokončí, karta „widget s palivem" ano. Na projekt, který pořád bobtná, platí jiná kapitola, [Scope creep](scope.md#scope-creep-napad-zaparkuj-nezabijej). Toto čtení je naše. Video třikrát odkazuje na autorův kurz zdarma [(1:36)](https://www.youtube.com/watch?v=wAe6b3IpSh0&t=96s), takže jde i o promo.

**Souvislosti:** [Kanban: zrnitost karet](#kanban-karty-zleva-doprava-a-jeden-vlastnik-na-kartu) · [Scope: malá hra = jedna mechanika](scope.md#mala-hra-jedna-mechanika-ne-zmenseny-skyrim) · [Rejstřík: Scope creep](../rejstrik.md#scope-creep)
