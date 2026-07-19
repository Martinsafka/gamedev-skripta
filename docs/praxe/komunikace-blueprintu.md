# Komunikace Blueprintů: cast, interface, dispatcher

Jak spolu mají Blueprinty mluvit je nejčastější architektonická otázka v UE — a odpověď má tři (a půl) podoby. Tahle kapitola dává vedle sebe mechaniku všech metod z tutoriálu Unreal University a doplňuje ji rozhodovacím pravidlem, kdy kterou sáhnout; čtvrtou cestu (broadcast kanály) přidává krátký klip Taken Grace.

Druhá polovina kapitoly jde od mechaniky k **vzorům**: série Aliho Elzoheiryho o návrhových vzorech v UE ukazuje tytéž nástroje jako řešení pojmenovaných problémů — observer, mediator — a nakonec vyvrací nejrozšířenější mýtus o castování měřením v Size Mapu.

---

## Tři kanály a kdy který: cast, interface, event dispatcher

**Zdroj:** [All 3 Blueprint Communication Methods in Unreal Engine Explained in Under 18 Minutes](https://www.youtube.com/watch?v=ZSRSktpezII) · [Unreal University](https://www.youtube.com/channel/UCQv4mwerZLQVe3wPbsMc-qw) · ~18 min, tutoriál (pes, papoušek, kostka)

**Shrnutí:** **Casting** ověří, že neznámý objekt je konkrétní třída, a zpřístupní všechno, co v ní je [(1:08)](https://www.youtube.com/watch?v=ZSRSktpezII&t=68s). **Interface** je sada funkcí bez implementace — každý blueprint si je naplní po svém [(6:04)](https://www.youtube.com/watch?v=ZSRSktpezII&t=364s). **Event dispatcher** je rádio: jeden vysílá, kdokoli přihlášený slyší [(11:44)](https://www.youtube.com/watch?v=ZSRSktpezII&t=704s). Mechanicky je zvládneš za odpoledne; architektonicky rozhodují o tom, kdo na kom závisí.

### Rozpad myšlenky

**Cast** [(1:27)](https://www.youtube.com/watch?v=ZSRSktpezII&t=87s): `Cast To BP_Dog` na actor z overlapu/hitu — uspěje-li, máš k dispozici funkce i proměnné psa (zavolej `Bark`, přečti jméno). Neuspěje-li (trefil jsi papouška), jede větev Failed [(3:16)](https://www.youtube.com/watch?v=ZSRSktpezII&t=196s). Legitimní použití: když cílovou třídu *z podstaty znáš* — `Get Player Character → Cast To BP_PlayerCharacter` [(4:41)](https://www.youtube.com/watch?v=ZSRSktpezII&t=281s) je v pořádku, hráčova třída je jistota. Past: cast vytváří tvrdou závislost a řetěz „zkus psa, zkus papouška, zkus dveře…" neškáluje — viz [Reference Viewer diagnóza](principy-architektury.md#tri-principy-skalovatelnosti-separace-volne-vazby-data).

**Interface** [(6:04)](https://www.youtube.com/watch?v=ZSRSktpezII&t=364s): vytvoř `BPI_Interact` s funkcí `Interact`, implementuj v `Class Settings → Interfaces` u psa i papouška [(7:05)](https://www.youtube.com/watch?v=ZSRSktpezII&t=425s) — každý reaguje po svém (pes si sedne, papoušek mluví). Volající se ptá `Does Object Implement Interface` [(9:55)](https://www.youtube.com/watch?v=ZSRSktpezII&t=595s) a volá message — bez znalosti třídy, bez závislosti; kdo neimplementuje, prostě nereaguje. Interface funkce umí vstupy i výstupy [(11:00)](https://www.youtube.com/watch?v=ZSRSktpezII&t=660s). Typické použití: interakční systémy — jeden volající, mnoho různých příjemců.

**Event dispatcher** [(11:44)](https://www.youtube.com/watch?v=ZSRSktpezII&t=704s): vlastník (hráč) deklaruje dispatcher a v pravou chvíli ho `Call`ne [(12:12)](https://www.youtube.com/watch?v=ZSRSktpezII&t=732s); posluchači se na BeginPlay `Bind`nou [(13:14)](https://www.youtube.com/watch?v=ZSRSktpezII&t=794s) a dodají vlastní custom event. Posluchačů může být libovolně mnoho [(14:55)](https://www.youtube.com/watch?v=ZSRSktpezII&t=895s) (kostka mění barvu, level blueprint loguje — každý nezávisle), jde se odhlásit (`Unbind` [(15:51)](https://www.youtube.com/watch?v=ZSRSktpezII&t=951s)) a dispatcher umí nést parametry [(16:57)](https://www.youtube.com/watch?v=ZSRSktpezII&t=1017s). Typické použití: „stalo se X, koho to zajímá" — jeden vysílá, N poslouchá, vysílač o posluchačích neví.

> **Pozn.:** Rozhodovací zkratka, kterou video neříká explicitně, ale plyne z [loose couplingu](principy-architektury.md#tri-principy-skalovatelnosti-separace-volne-vazby-data): **cast**, když třídu garantuješ (vlastní player, GameMode); **interface**, když se ptáš cizího „umíš tohle?"; **dispatcher**, když oznamuješ „stalo se tohle" a nechceš vědět komu. Směr závislosti: cast váže volajícího na třídu, interface na smlouvu, dispatcher nikoho na nic — posluchač závisí na vysílači, ne obráceně.

**Souvislosti:** [Principy architektury](principy-architektury.md) · [Interakce bez Event Ticku](interakce-bez-event-ticku.md) · [Design patterns: strategy a observer](../teorie/design-patterns.md#strategy-a-observer-dva-vzory-ktere-v-ue-pouzivas-denne) *(dispatcher je observer pattern jménem)* · [Rejstřík: Cast](../rejstrik.md#cast) · [Rejstřík: Blueprint Interface](../rejstrik.md#blueprint-interface) · [Rejstřík: event dispatcher](../rejstrik.md#event-dispatcher)

---

## Čtvrtý kanál: broadcast přes subsystem s payloady

**Zdroj:** [Unreal Engine: Boost Game Perf with Smart Broadcasts! #shorts](https://www.youtube.com/watch?v=dIXGXiB9Okc) · [Taken Grace](https://www.youtube.com/channel/UCLagdpQoUG-jtyH8bF0IGZg) · ~1,5 min, výřez z delšího videa

**Shrnutí:** Nad třemi klasikami existuje ještě messagingový vzor: **broadcast kanály** přes game instance subsystem — vysílač pošle zprávu na pojmenovaný kanál s payloadem (struct) a subsystem ji doručí všem posluchačům kanálu [(0:01)](https://www.youtube.com/watch?v=dIXGXiB9Okc&t=1s). Na nanosekundy je to *pomalejší* než dispatcher — a přesto to v součtu šetří výkon.

### Rozpad myšlenky

Mechanika: posluchač se „naladí" na kanál (např. `GoldCollector`) a deklaruje očekávaný **payload typ** — struct, který se musí shodovat přesně, jinak zpráva nedorazí [(0:48)](https://www.youtube.com/watch?v=dIXGXiB9Okc&t=48s); on message received pak spustí vlastní logiku. Vysílač jen broadcastne kanál + payload a nikoho nezná.

Proč je to výhra, když je samotné volání pomalejší: **žádné hard reference** [(0:01)](https://www.youtube.com/watch?v=dIXGXiB9Okc&t=1s). Dispatcher vyžaduje, aby posluchač měl referenci na vysílač (bind na konkrétní objekt) — a reference znamená, že se s levelem nahrává i všechno navázané. Kanálový messaging přes subsystem (žije po celou dobu běhu aplikace) obě strany úplně odpojí: level se načte bez tahání závislostí. Klasický trade-off mikrovýkon vs. architektura — a druhý vyhrává.

> **Pozn.:** Tohle je Blueprint podoba vzoru, který [ability systém](principy-architektury.md#tri-principy-skalovatelnosti-separace-volne-vazby-data) řešil event manager subsystémem a který v Lyře žije jako Gameplay Message Subsystem. Klip je výřez (~1,5 min) — kompletní stavbu systému má autor na kanále; pro nás je podstatný princip. Kombinuje se skvěle s [gameplay tagy](gameplay-tags.md) jako názvy kanálů/eventů.

**Souvislosti:** [Principy architektury](principy-architektury.md) · [Gameplay Tags](gameplay-tags.md) · [Rejstřík: subsystem](../rejstrik.md#subsystem) · [Rejstřík: hard reference](../rejstrik.md#hard-reference)

---

## Observer pattern: nejčastější chyba začátečníků a její oprava

**Zdroj:** [The Most Common Mistake Beginners Make in Unreal Engine | UE5 Observer Pattern Explained](https://www.youtube.com/watch?v=YFtLd-bKl-U) · [Ali Elzoheiry](https://www.youtube.com/channel/UCrrZx9bh7RMYhXvaN8BrbNg) · ~12 min, tutoriál (série o návrhových vzorech)

**Shrnutí:** Widget má ukazovat počet zbývajících nepřátel, dveře se mají otevřít, až všichni padnou. **Nejčastější chyba: v death funkci nepřítele si vzít referenci na widget a přepsat číslo.** Tím jsi právě do třídy nepřítele umístil logiku widgetu — a příště, až budeš měnit jedno, budeš muset sáhnout i na druhé. Oprava se jmenuje observer a v Blueprintech je to prostě **event dispatcher použitý jako vzor**, ne jako uzel.

### Rozpad myšlenky

**Proč je přímá reference dražší, než vypadá** [(0:49)](https://www.youtube.com/watch?v=YFtLd-bKl-U&t=49s): *„teď je logika widgetu uvnitř třídy nepřítele. Když budeš později měnit widget, musíš měnit i nepřítele a naopak — a když těch závislostí nasekáš dost, znamená jedna jednoduchá změna přepsat obrovský kus hry."* Klíčové slovo je **coupling**: nejde o to, že to nefunguje, ale o to, kolik stojí příští změna.

**Vzor sám** [(1:35)](https://www.youtube.com/watch?v=YFtLd-bKl-U&t=95s): publisher/subscriber. Objekt **vyšle signál**, když nastane událost; kdokoli jinde ho **odebírá** a reaguje po svém. Podstatná je asymetrie: **„jeden objekt vysílá signál a nezajímá ho, co se s ním stane."** V Blueprintech to je event dispatcher, v C++ delegate [(2:21)](https://www.youtube.com/watch?v=YFtLd-bKl-U&t=141s).

**Publisher** [(3:08)](https://www.youtube.com/watch?v=YFtLd-bKl-U&t=188s): dispatcher se pojmenuje **„on něco"** — *„protože je to spouštěč něčeho, co se stalo"* — a na konci death eventu se `Call`ne. Volitelně nese vstupy pro předání dat. To je celý publisher; víc nepřítel dělat nemusí.

**Subscriber a past on Ticku** [(4:41)](https://www.youtube.com/watch?v=YFtLd-bKl-U&t=281s): na námitku „nemůžu prostě kontrolovat počet na ticku?" odpovídá čísly: *„jo, můžeš — ale kontroloval bys to zhruba šedesátkrát za sekundu úplně zbytečně, protože se to mění jednou za pár sekund nebo minut."* Tatáž logika jako u [interakce bez Event Ticku](interakce-bez-event-ticku.md#overlap-trigger-misto-trasovani-v-ticku).

**Bind potřebuje instanci, ne třídu** [(4:41)](https://www.youtube.com/watch?v=YFtLd-bKl-U&t=281s): **každý nepřítel vysílá vlastní on-death**, takže se odebírá per instance — for each přes pole nepřátel → `Bind on death`. Zkratka `Assign` [(8:50)](https://www.youtube.com/watch?v=YFtLd-bKl-U&t=530s) udělá bind a rovnou vytvoří custom event. (Právě tahle nutnost mít referenci je slabina, kterou opravuje [mediator](#mediator-koordinator-uprostred-a-event-manager-v-game-state).)

**Kde má logika bydlet** [(7:14)](https://www.youtube.com/watch?v=YFtLd-bKl-U&t=434s) je nejcennější věta celého videa a týká se dveří, ne dispatcherů: *„můžu mít víc dveří, které se otvírají z různých důvodů, takže to nedám do blueprintu dveří — ale v tomhle konkrétním levelu se tyhle dveře otvírají po zabití všech nepřátel, takže to dám do level blueprintu."* Kritérium tedy není „kam se to hodí", ale **jak obecné to pravidlo je**: chování dveří patří dveřím, pravidlo tohohle levelu patří levelu.

> **Pozn.:** Elzoheiryho videa jsou z roku 2024, ale vzory stárnou pomalu — uzly i názvy sedí i v současných verzích. Napříč sérií autor propaguje **Patreon (projektové soubory) a vlastní chatbota trénovaného na svých videích a komentářích**; obsah tutoriálů to nijak neposouvá, ale patří to k obrázku. Vzor sám je ten, který [teoretická kapitola o design patterns](../teorie/design-patterns.md#strategy-a-observer-dva-vzory-ktere-v-ue-pouzivas-denne) popisuje pod jménem observer.

**Souvislosti:** [Design patterns: strategy a observer](../teorie/design-patterns.md#strategy-a-observer-dva-vzory-ktere-v-ue-pouzivas-denne) · [Tři kanály a kdy který](#tri-kanaly-a-kdy-ktery-cast-interface-event-dispatcher) · [Interakce bez Event Ticku](interakce-bez-event-ticku.md#overlap-trigger-misto-trasovani-v-ticku) · [Principy architektury: volné vazby](principy-architektury.md#tri-principy-skalovatelnosti-separace-volne-vazby-data) · [Rejstřík: Observer pattern](../rejstrik.md#observer-pattern) · [Rejstřík: event dispatcher](../rejstrik.md#event-dispatcher)

---

## Mediator: koordinátor uprostřed a event manager v Game State

**Zdroj:** [Why Dependencies are Bad and How To Avoid Them In Unreal Engine | UE5 Mediator Pattern Explained](https://www.youtube.com/watch?v=y4fE2JdFdvY) · [Ali Elzoheiry](https://www.youtube.com/channel/UCrrZx9bh7RMYhXvaN8BrbNg) · ~27 min, tutoriál

**Shrnutí:** Deset nepřátel chce útočit, ale najednou smí jen tři; když jeden padne, nastoupí čekající; když hráč zemře, všichni se vrátí. **Jak to udělat, aniž by se nepřátelé domlouvali mezi sebou?** Mediator říká: nekomunikují spolu, komunikují **jen s prostředníkem**. Druhá polovina videa pak stejným trikem opravuje slabinu observeru — dispatcher se přesune do Game State a stane se z něj **event manager**.

### Rozpad myšlenky

**Analogie, která to vysvětlí za deset sekund** [(2:21)](https://www.youtube.com/watch?v=y4fE2JdFdvY&t=141s): *„letadla spolu nekomunikují ‚ty si vezmi dráhu jedna, já dvojku' — to by způsobilo spoustu nehod. Komunikují přes věž, která sedí uprostřed."* Aktéři pak závisí na jediné třídě a je jim jedno, co se děje na druhém konci.

**Combat manager** [(3:54)](https://www.youtube.com/watch?v=y4fE2JdFdvY&t=234s) je aktér v levelu a drží tři věci: `AttackTarget`, pole `Attackers` a pole `WaitingAttackers`. Detail, který autor sám označí za zásadní: **všechno jsou Actor reference, ne `BP_Enemy` a `BP_Player`.** Proč, se ukáže až na konci.

**Rozhraní jako protokol** [(4:40)](https://www.youtube.com/watch?v=y4fE2JdFdvY&t=280s): `BPI_Attacker` (attack / wait / retreat) a `BPI_AttackTarget` (`GetMaxAttackersCount → int`). **Mediátor definuje, co od aktérů potřebuje; implementaci nechává na nich** — u nepřítele všechny tři funkce jen přepnou stavovou proměnnou v AI controlleru, kterou čte behavior tree se čtyřmi stavy (passive / wait / attack / dead) [(7:48)](https://www.youtube.com/watch?v=y4fE2JdFdvY&t=468s).

Logika `HandleAttackRequest` [(6:12)](https://www.youtube.com/watch?v=y4fE2JdFdvY&t=372s) je triviální — ověř, že žadatel není zároveň cíl, porovnej počet s maximem, zařaď do útočníků nebo čekajících, zavolej `Attack` nebo `Wait`. Zajímavá je jedna věta u toho [(7:00)](https://www.youtube.com/watch?v=y4fE2JdFdvY&t=420s): **„nemusel jsem castovat z Actor na BP_Enemy, protože attack a wait jsou interface funkce, které jdou zavolat na jakémkoli objektu — a neudělají nic, když objekt rozhraní neimplementuje."** Doplňkově `HandleDeath` [(9:41)](https://www.youtube.com/watch?v=y4fE2JdFdvY&t=581s) rozlišuje tři případy (zemřel cíl → všichni retreat a obě pole vyprázdnit; zemřel útočník → nastoupí čekající; zemřel čekající → jen ho odeber).

**Odměna za ta Actor reference** [(12:48)](https://www.youtube.com/watch?v=y4fE2JdFdvY&t=768s) přijde na konci a je to nejlepší důkaz volných vazeb v celé dávce: attack target lze v levelu přepnout **na jakéhokoli aktéra**. Jiný nepřítel? Funguje — a může mít vlastní `MaxAttackers` vystavený jako Exposed on Spawn, takže jeden má tři útočníky a druhý pět. Aktér, který rozhraní neimplementuje? Max se vrátí jako nula a nikdo neútočí. *„Můžu udělat attack targetem i tuhle ubohou kostku."*

**Druhá půlka: event manager** [(15:10)](https://www.youtube.com/watch?v=y4fE2JdFdvY&t=910s) opravuje to, co observeru zbylo: *„pořád potřebuju referenci na nepřítele, abych se navázal na jeho on-death. A to není ideální — jako odběratele mě nezajímá, kdo to vysílá, chci jen vědět, že se to stalo."* Řešení: dispatcher přesunout do **vlastního Game State** [(15:58)](https://www.youtube.com/watch?v=y4fE2JdFdvY&t=958s), *„protože je globálně dostupný a replikovaný na serveru i klientovi"*. Widget i level se pak vážou na Game State a o nepříteli nevědí vůbec nic.

K tomu tři praktické detaily, které stojí za zapamatování:

- **Počítej událostmi, ne dotazem** [(18:00)](https://www.youtube.com/watch?v=y4fE2JdFdvY&t=1080s): přidat i `OnEnemySpawned` a inkrementovat, místo abys na začátku volal `GetAllActorsOfClass`. Tím zmizí i poslední hard reference.
- **Past dispatche v BeginPlay** [(18:00)](https://www.youtube.com/watch?v=y4fE2JdFdvY&t=1080s): *„pozor při vysílání eventů v begin play — odběratelé ještě nemusí být inicializovaní. Přidej delay until next tick."*
- **Duplikace jako záměr** [(20:40)](https://www.youtube.com/watch?v=y4fE2JdFdvY&t=1240s): tentýž počítací kód je ve widgetu i ve dveřích. *„Spousta lidí se ptá, proč to duplikuju. Je to proto, aby widget a dveře byly nezávislé — kdybych to sdílel, spojím je, a přesně tomu se snažíme vyhnout."* Užitečná připomínka, že **DRY má hranici tam, kde by odstranění duplikace vyrobilo vazbu.**

> **Pozn.:** Interface nad event managerem [(22:13)](https://www.youtube.com/watch?v=y4fE2JdFdvY&t=1333s) (`PublishEnemyDeath`) zbaví **publishera** nutnosti castovat na Game State, ale **subscriber castovat musí dál** — *„protože potřebuješ referenci na skutečný published event a ten v blueprintech do interface dát nejde"*. Autor tu cenu přiznává rovnou. A závěr o smyslu celé série stojí za citaci [(25:23)](https://www.youtube.com/watch?v=y4fE2JdFdvY&t=1523s): *„programátoři netráví většinu času zběsilým psaním na klávesnici. Většinu času čteš a přemýšlíš o svém kódu — a ať jsi jakkoli chytrý, do hlavy se ti najednou vejde jen omezené množství informací. Proto jsou zdatní programátoři ti, kdo píšou software, o kterém se snadno uvažuje."*

**Souvislosti:** [Observer pattern](#observer-pattern-nejcastejsi-chyba-zacatecniku-a-jeji-oprava) *(vzor, jehož slabinu tenhle opravuje)* · [Čtvrtý kanál: broadcast přes subsystem](#ctvrty-kanal-broadcast-pres-subsystem-s-payloady) *(tentýž nápad postavený nad subsystémem místo Game State)* · [Design patterns: tři rodiny vzorů](../teorie/design-patterns.md#tri-rodiny-vzoru-tvorba-struktura-chovani) · [Principy architektury: volné vazby](principy-architektury.md#tri-principy-skalovatelnosti-separace-volne-vazby-data) · [Rejstřík: Mediator pattern](../rejstrik.md#mediator-pattern) · [Rejstřík: Game State](../rejstrik.md#game-state)

---

## Interface, nebo dispatcher — a kolik doopravdy stojí cast

**Zdroj:** [Why Use "Interfaces" & "Event Dispatchers" in Unreal Engine | UE5 Explained](https://www.youtube.com/watch?v=EQfml2D9hwE) · [Ali Elzoheiry](https://www.youtube.com/channel/UCrrZx9bh7RMYhXvaN8BrbNg) · ~22 min, vysvětlující video

**Shrnutí:** Otázka „interface, nebo dispatcher?" je podle autora špatně položená: **slouží k různým věcem a mají se používat spolu.** Interface sdílí **strukturu** („zavazuješ se mít tyhle funkce"), dispatcher sdílí **událost** („stalo se tohle"). Uprostřed videa je ale ještě cennější věc — **změření toho, co stojí jediný cast uzel**, které mýtus „castování je zlo" zároveň potvrdí i vyvrátí.

### Rozpad myšlenky

**Interface není sdílení implementace** [(1:36)](https://www.youtube.com/watch?v=EQfml2D9hwE&t=96s): *„definuje sadu funkcí popisujících, jak se má třída chovat, bez implementace. Není to metoda sdílení implementace funkcí — na to jsou jiné způsoby. Je to metoda sdílení struktury mezi třídami."* Interakce s NPC dělá něco jiného než interakce s předmětem; společné je jen to, že **oba to umí**.

**Proč to volajícímu tak pomáhá** [(6:21)](https://www.youtube.com/watch?v=EQfml2D9hwE&t=381s): po sphere trace drží hráč jenom `Actor`. *„Nevím, že na NPC existuje interact, který otevře quest menu; nevím, že na pickupu existuje interact, který přidá věc do inventáře. Vím jen, že jsem trefil aktéra."* Zavolá interface funkci — a uzel sám nese poznámku **„this does nothing if the target does not implement the required interface"**. Bezpečné selhání je součást návrhu.

**Protipříklad, který to dokáže** [(7:56)](https://www.youtube.com/watch?v=EQfml2D9hwE&t=476s): tatáž funkce `CanInteract` implementovaná přímo v obou třídách, bez interface. Volající pak musí castovat na NPC, při selhání castovat na pickup, u třetího typu přidat třetí cast… *„tohle prostě neškáluje a je to hrozný nepořádek."*

**Kolik stojí cast — měřením, ne dojmem** [(10:16)](https://www.youtube.com/watch?v=EQfml2D9hwE&t=616s) je ta část, kvůli které se video vyplatí. Pravý klik na asset → **Size Map → Memory Size**. Hráčova třída sama: **65 MB**. Pak autor přidá do grafu **jediný cast uzel na NPC — ani ho nepřipojí** — zkompiluje a změří znovu: **velikost se zdvojnásobí**, protože se s hráčem nahraje i všechno z NPC. *„Castem říkáš enginu, že tahle třída závisí na existenci NPC, takže když se načte jedna, musí se načíst i druhá."*

A hned nato přijde korekce, kterou většina obsahu o UE vynechává [(11:02)](https://www.youtube.com/watch?v=EQfml2D9hwE&t=662s): **„castování není vždycky špatné — buď chytrý."** Castovat na třídy, které se stejně načítají spolu, nic nestojí: hráč, který vždycky drží sekeru, na kameru, AI controller na pawna, kterého ovládá. *„A vlastně bys na ně castovat měl, protože tím říkáš, že ty dvě třídy na sobě závisí."* Pravidlo tedy nezní „necastuj", ale **„necastuj mezi třídami, které na sobě nezávisí"**.

**Kdy dispatcher** [(12:34)](https://www.youtube.com/watch?v=EQfml2D9hwE&t=754s): když chceš **počkat**, až se něco stane — *„místo abys se pořád ptal ‚už hráč sebral předmět? už?'"*. Autorův oblíbený případ jsou **modulární actor komponenty**: health komponenta jen dispatchne `OnDeath` a **nepředpokládá, kdo ji používá**.

**Přímé srovnání na jednom úkolu** [(17:11)](https://www.youtube.com/watch?v=EQfml2D9hwE&t=1031s) je nejpoctivější část: tentýž „on death" jde udělat i interfacem — komponenta si vezme `GetOwner` a zavolá `Death` z `BPI_Damageable`. Autor preferuje dispatcher a důvod je konkrétní [(18:45)](https://www.youtube.com/watch?v=EQfml2D9hwE&t=1125s): *„s interfacem komponenta pořád dělá předpoklad — že vlastník to rozhraní implementuje a má death funkci, a nedovolí mu nic jiného. S dispatcherem může komponentu použít i předmět, který žádnou smrt nemá."* A uzavře to férově: *„jako u všeho v softwaru má každý přístup plusy i minusy. Není správně a špatně, záleží na použití."*

> **Pozn.:** Drobnost, která se hodí vědět: **bind přes ikonu plus** v detailech komponenty a **ruční `Bind`** jsou funkčně identické — jen ručně navázaný event jde později **odvázat (`Unbind`)**, přes plus ikonu ne [(15:38)](https://www.youtube.com/watch?v=EQfml2D9hwE&t=938s). A jedna věta na závěr, která popisuje interface líp než definice: *„je to jako podepsat smlouvu — třída se zavazuje dodržet určitou strukturu."*

**Souvislosti:** [Tři kanály a kdy který](#tri-kanaly-a-kdy-ktery-cast-interface-event-dispatcher) *(mechanika týchž nástrojů)* · [Principy architektury: komponenty místo dědičnosti](principy-architektury.md#komponenty-misto-dedicnosti-skladej-misto-vetveni) · [Interakce bez Event Ticku: interface bez castů](interakce-bez-event-ticku.md#blueprint-interface-volani-bez-castu) · [Rejstřík: hard reference](../rejstrik.md#hard-reference) · [Rejstřík: Size Map](../rejstrik.md#size-map) · [Rejstřík: Blueprint Interface](../rejstrik.md#blueprint-interface)
