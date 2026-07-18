# Plánovací nástroje: kanban pro gamedev

Jednou přijde bod, kdy „mám to v hlavě" přestane stačit — sólo dřív, než čekáš, v týmu okamžitě. Indie Game Clinic ukazuje na reálném jamovém projektu, jak vede hru přes Trello: nejdřív *co* dělat (karty, sloupce, pravidla), pak *proč* zrovna takhle (kanban jako metodologie, ne jen software). A přidává kariérní poznámku pod čarou: kdo tohle na projektech dělá, dělá práci producenta.

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
