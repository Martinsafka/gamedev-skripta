# Signály do hloubky

Signály jsou důvod, proč se v Godotu dá stavět modulárně — a taky nejrychlejší způsob, jak si vyrobit chaos, když se použijí špatně. Autor série, ze které kapitola čerpá, to formuluje bez příkras: *„používat je nestačí; použiješ-li je špatně, uděláš stejný nepořádek jako přímými referencemi."*

Základní pravidlo **call down, signal up** je popsané [v kapitole o GDScriptu](gdscript.md#call-down-signal-up-kdo-koho-smi-znat); tady na něm stavíme dál — pojmenování, přenášená data, dynamicky vznikající objekty, globální event bus a jeden koncept, který je cennější než všechna pravidla dohromady: **jediný zdroj pravdy**.

---

## Událost, ne příkaz: jméno signálu prozradí, jestli jsi ho pochopil

**Zdroj:** [Stop Making Messy Games: Godot Rules For Scalable Projects | Signals PT1](https://www.youtube.com/watch?v=1rvlexb1fCU) · [DeeRaghooGames](https://www.youtube.com/channel/UC-KLgU0nzoCCEU6W16CS3vQ) · ~14 min, esej

**Shrnutí:** Než signál vytvoříš, polož si jednu otázku: **oznamuju, že se něco stalo, nebo někomu říkám, co má dělat?** Oznámení patří do signálu, příkaz do přímého volání. Test se dá udělat na jméně — `update_score` je instrukce, `coin_collected` je událost. Háček, kvůli kterému na tom záleží víc, než se zdá: špatné jméno **nefunguje hned**, funguje půl roku a rozbije se, až budeš chtít, aby na tutéž věc reagoval ještě někdo další.

### Rozpad myšlenky

**Mechanismus selhání** je názorný [(1:31)](https://www.youtube.com/watch?v=1rvlexb1fCU&t=91s). Sbíráš mince a signál pojmenuješ `update_score`. Dnes to sedí — sebrání mince opravdu jen zvedá skóre. *„Za půl roku se rozhodneš, že sebrání mince má taky přehrát zvuk a vypustit částice — a najednou jméno `update_score` nedává smysl. Proč by se zvukový manažer staral o signál jménem ‚aktualizuj skóre'?"* Signál začal reprezentovat **jednu konkrétní reakci** místo události, která nastala.

Autorův obraz je dobrý a stojí za zapamatování [(3:05)](https://www.youtube.com/watch?v=1rvlexb1fCU&t=185s): **signál je zpravodaj.** Reportér neříká lidem, co mají dělat; hlásí, co se stalo. *Hráč zemřel. Level dokončen. Mince sebrána.* Co s tím kdo udělá, je věc posluchačů.

**Použitelné pravidlo palce** [(3:05)](https://www.youtube.com/watch?v=1rvlexb1fCU&t=185s): *zní-li jméno signálu jako příkaz, který dáváš jinému objektu, je nejspíš moc konkrétní.* Dvojice, které autor uvádí, se dají číst jako převodní tabulka: `update_health_bar` → `health_changed` · `play_death_animation` → `player_died` · `open_shop_ui` → `shop_entered`. Levá strana popisuje **reakce**, pravá **události** — a události přežijí přidání druhého posluchače.

**Druhá půlka pravidla je o čekání** [(9:18)](https://www.youtube.com/watch?v=1rvlexb1fCU&t=558s), a je to ta zajímavější. Vyslal-li node signál, **jeho práce skončila**. Nesmí se spoléhat, že posluchač něco udělá, a už vůbec ne na to čekat. Autor ukazuje nejhorší variantu: tlačítko vyšle `start_requested`, a pak **si samo hlídá globální stav pauzy**, aby vědělo, kdy se má skrýt. *„Tlačítko teď není jednoduchá UI komponenta. Je pevně svázané s chováním UI manažera a se stavem pauzy."* Přitom jeho jediný úkol je oznámit, že hráč chce hru spustit; co to znamená, rozhoduje ten nahoře — může odpauzovat, schovat tlačítko, spustit odpočet nebo načíst level.

**Pravidlo v akci.** Demo z videa je malé a přesně ilustruje [call down, signal up](gdscript.md#call-down-signal-up-kdo-koho-smi-znat) [(4:38)](https://www.youtube.com/watch?v=1rvlexb1fCU&t=278s): `UIManager` (kořen) → `CanvasLayer` → `ButtonControl` → `Button`. Tlačítko **vyšle nahoru** `start_requested`; manažer ho odchytí, odpauzuje hru a **zavolá dolů** `hide_start_button()`. Za zmínku stojí dva technické detaily, které autor přidává mimochodem: `CanvasLayer` má `process_mode` na *always*, aby UI fungovalo i v pauze — a je **dítětem** `UIManager`u schválně, protože Godot načítá strom shora dolů a `@onready` reference na node níž ve stromu by jinak byla prázdná.

> **Pozn.:** Rozdíl „událost vs. příkaz" je táž hranice, kterou v Unrealu vytyčuje volba mezi [interfacem a event dispatcherem](../praxe/komunikace-blueprintu.md#interface-nebo-dispatcher-a-kolik-doopravdy-stoji-cast) — jen se tam projeví jako výběr mechanismu, kdežto tady jako **výběr slova**. To je vlastně praktičtější: jméno vidíš pokaždé, když ten řádek čteš, zatímco mechanismus zapadne. Prakticky se vyplatí přidat si do konvence i to, co [doporučuje style guide](gdscript.md#poradek-jako-nastroj-hlavicka-skriptu-a-inspektor): **signály v minulém čase**. Minulý čas jméno-příkaz skoro znemožní zformulovat.

**Souvislosti:** [Call down, signal up](gdscript.md#call-down-signal-up-kdo-koho-smi-znat) *(pravidlo v základní podobě)* · [Signál nese data](#signal-nese-data-kdo-kolik-a-jaky-typ) · [Komunikace Blueprintů: observer pattern](../praxe/komunikace-blueprintu.md#observer-pattern-nejcastejsi-chyba-zacatecniku-a-jeji-oprava) · [Rejstřík: Signal](../rejstrik.md#signal) · [Rejstřík: Loose coupling](../rejstrik.md#loose-coupling)

---

## Signál nese data: kdo, kolik a jaký typ

**Zdroj:** [Stop Making Messy Games: Godot Rules For Scalable Projects | Signals PT1](https://www.youtube.com/watch?v=1rvlexb1fCU) · [DeeRaghooGames](https://www.youtube.com/channel/UC-KLgU0nzoCCEU6W16CS3vQ) · ~14 min, esej · + [Signals PT2](https://www.youtube.com/watch?v=btCeflqFw4o) · týž kanál · ~15 min

**Shrnutí:** Signál bez parametrů říká „stalo se to". Signál s parametry říká „stalo se to, takhle a tolikrát" — a rozdíl je v tom, že posluchač si už nemusí nic dohledávat. Ke stejné rodině patří i trik, kterým se **stovka mincí připojí jedním cyklem**: dej je do skupiny a projdi ji. Háček, na který se zapomíná: parametry mají popisovat **událost**, ne to, co s ní má posluchač udělat.

### Rozpad myšlenky

**Bez dat to funguje taky, jen hůř** [(11:41)](https://www.youtube.com/watch?v=1rvlexb1fCU&t=701s). Mince vyšle `coin_collected`, správce skóre přičte bod. Problém nastane, jakmile mají mince různou hodnotu — správce se musí ptát zpátky, kdo signál poslal, a vytáhnout si z něj čísla. Tím vzniká přesně ta závislost, které se signály vyhýbají.

**Mechanismus** je jeden řádek [(12:28)](https://www.youtube.com/watch?v=1rvlexb1fCU&t=748s): signál se deklaruje s parametry — `signal coin_collected(points: int, coin_type: String)` — a vysílá se s hodnotami. Místo *„mince byla sebrána"* teď zpráva zní *„byla sebrána mince za 10 bodů, typu base coin"*. Posluchač dostane všechno, co potřebuje, **aniž by musel kamkoli sahat**.

**Skupiny jako hromadné připojení.** Druhá polovina myšlenky řeší otázku, která přijde hned potom: máš tři mince, pak třicet — kdo je připojí? Autorovo řešení je elegantní [(3:14)](https://www.youtube.com/watch?v=btCeflqFw4o&t=194s): všechny mince patří do **skupiny `coins`**, takže `get_tree().get_nodes_in_group("coins")` vrátí pole a jednoduchá smyčka připojí každé z nich tentýž handler. *„Nemusíme spojovat každou minci ručně v editoru. Cokoli patří do skupiny `coins`, se při startu scény napojí samo."*

**Co tím správce skóre získá,** je hezky vidět na tom, co **nemusí umět** [(4:01)](https://www.youtube.com/watch?v=btCeflqFw4o&t=241s): nezná scény mincí, nezná jejich typy, nemá na ně reference. Přijme dvě čísla a aktualizuje dva popisky. To je posluchač, který přežije jakoukoli změnu na straně mincí.

> **Pozn.:** Parametry signálu jsou přesně to místo, kde se vyplatí [statické typování](gdscript.md#gradual-typing-kolik-bezpecnosti-si-koupis) — chyba v pořadí nebo typu argumentů je jinak tichá a projeví se až za běhu, obvykle jako podivné číslo na obrazovce. A jedna vlastní výhrada k té skupinové smyčce: **funguje jen na to, co ve scéně je při startu.** Mince, které vzniknou později (spawner, drop z nepřítele), se do smyčky nechytí a musely by se připojovat při vzniku. To je přesně ten problém, který řeší [event bus](#event-bus-kdyz-se-systemy-nemaji-cim-potkat) — a proto na sebe ty dvě myšlenky navazují.

**Souvislosti:** [Událost, ne příkaz](#udalost-ne-prikaz-jmeno-signalu-prozradi-jestli-jsi-ho-pochopil) · [Event bus](#event-bus-kdyz-se-systemy-nemaji-cim-potkat) *(řešení pro dynamicky vznikající objekty)* · [Gradual typing](gdscript.md#gradual-typing-kolik-bezpecnosti-si-koupis) · [Gameplay Tags](../praxe/gameplay-tags.md#kde-tagy-bydli-a-jak-se-na-ne-ptat-bez-skrytych-bugu) *(skupiny jako chudší příbuzný tagů)* · [Rejstřík: Signal](../rejstrik.md#signal)

---

## Event bus: když se systémy nemají čím potkat

**Zdroj:** [Stop Making Messy Games: Godot Rules For Scalable Projects | Signals PT2](https://www.youtube.com/watch?v=btCeflqFw4o) · [DeeRaghooGames](https://www.youtube.com/channel/UC-KLgU0nzoCCEU6W16CS3vQ) · ~15 min, esej

**Shrnutí:** Skupinová smyčka z předchozí myšlenky má strop: připojí to, co ve scéně je, a nic z toho, co teprve vznikne. **Event bus** — v Godotu autoload se sadou signálů — ten strop odstraní: signál žije globálně, mince ho jen vysílá a správce skóre se připojí **jednou, bez ohledu na to, kolik mincí kdy vznikne**. Cena je ta, kterou má každý globální stav: jednoduchost výměnou za viditelnost.

### Rozpad myšlenky

**Co je autoload** [(4:52)](https://www.youtube.com/watch?v=btCeflqFw4o&t=292s): skript nebo node, který Godot založí **nad kořenem stromu ještě před načtením první scény**, a který proto žije po celou dobu běhu hry i přes výměny scén. Typická použití, která autor jmenuje: trvalá data (skóre, inventář, život), globální systémy (audio manažer, správce questů, dialogy), přechody mezi scénami, save/load a načítací obrazovky.

**Event bus je jedno konkrétní použití**: autoload, který **neobsahuje logiku, jen signály** [(5:39)](https://www.youtube.com/watch?v=btCeflqFw4o&t=339s). Postup je krátký — složka `autoloads`, skript `signal_hub.gd`, do něj deklarace `signal coin_collected(points, coin_type)`, a v *Project Settings → Globals → Autoload* přidat. Autor přidává praktickou drobnost: k signálům patří anotace potlačující varování o nepoužitých signálech, protože v tom souboru je nikdo nevysílá.

**Co se tím změní**, je vidět nejlíp na tom, co zmizí [(7:13)](https://www.youtube.com/watch?v=btCeflqFw4o&t=433s). Mince už **nedeklaruje vlastní signál** — vysílá sdílený (`SignalHub.coin_collected.emit(points, type)`). A správce skóre **přestane potřebovat celý blok**, který procházel skupinu a připojoval každou minci zvlášť; zbude jediný řádek `SignalHub.coin_collected.connect(_on_coin_collected)`. Zbytek skriptu se nemění.

**Kdy tedy autobus a kdy ne.** Video ho doporučuje pro **systémy, které spolu blízko nesouvisejí** — a to je ta správná hranice. Mince a UI skóre nemají ve stromu žádný společný bod, který by je rozumně propojil; protahovat signál přes tři patra hierarchie by bylo horší než globální kanál. Naopak tlačítko a jeho UI manažer společný bod mají (rodiče), takže tam je autobus zbytečný a škodlivý: schoval by závislost, která je jinak vidět na první pohled.

> **Pozn.:** Cena globálního kanálu není výkon, ale **dohledatelnost**. U přímého připojení vidíš ve stromu, kdo koho poslouchá; u autobusu se musíš ptát fulltextem, kdo se na daný signál napojil — a čím víc signálů tam nasypeš, tím spíš se z „hubu" stane [God class](../rejstrik.md#god-class) bez chování. Praktická pojistka, kterou video nemá: **do autobusu patří jen události, které opravdu zajímají víc nepříbuzných systémů** (hráč zemřel, level dokončen, nastavení změněno). Cokoli, co má právě jednoho posluchače, tam nepatří. Unreal má na tentýž problém [subsystémy s broadcast kanály](../praxe/komunikace-blueprintu.md#ctvrty-kanal-broadcast-pres-subsystem-s-payloady) a [mediator/event manager](../praxe/komunikace-blueprintu.md#mediator-koordinator-uprostred-a-event-manager-v-game-state) — a výhrady jsou tam popsané tytéž.

**Souvislosti:** [Signál nese data](#signal-nese-data-kdo-kolik-a-jaky-typ) *(strop, který autobus odstraňuje)* · [Jediný zdroj pravdy](#jediny-zdroj-pravdy-dva-budiky-ukazuji-ruzny-cas) · [Komunikace Blueprintů: broadcast přes subsystem](../praxe/komunikace-blueprintu.md#ctvrty-kanal-broadcast-pres-subsystem-s-payloady) *(týž vzor v UE)* · [AnimationPlayer jako časovač](prvni-hra.md#animationplayer-jako-casovac-sekvence-bez-jedineho-radku-kodu) *(autoload na hudbu)* · [Rejstřík: Event bus](../rejstrik.md#event-bus) · [Rejstřík: Autoload](../rejstrik.md#autoload) · [Rejstřík: Singleton](../rejstrik.md#singleton)

---

## Jediný zdroj pravdy: dva budíky ukazují různý čas

**Zdroj:** [Stop Making Messy Games: Godot Rules For Scalable Projects | Signals PT2](https://www.youtube.com/watch?v=btCeflqFw4o) · [DeeRaghooGames](https://www.youtube.com/channel/UC-KLgU0nzoCCEU6W16CS3vQ) · ~15 min, esej

**Shrnutí:** Nejcennější věc v celé sérii není o signálech — je to koncept **single source of truth**: jedna informace má existovat na jednom místě. Autor ho předvádí na duchové minci, jejíž stav *není uložený v proměnné*, ale je **odvozený z toho, jestli je signál připojený**. Přínos není úspora řádku; je to nemožnost, aby se dvě kopie téhož stavu rozešly. A poctivá výhrada, kterou video samo přidává: pro tenhle konkrétní případ by bylo jednodušší vypnout collision shape.

### Rozpad myšlenky

**Případ**: mince, která se v cyklu objevuje a mizí [(8:01)](https://www.youtube.com/watch?v=btCeflqFw4o&t=481s). Časovač každých 2,5 s spustí tween, který přepne průhlednost mezi 1,0 a 0,2. Ve vybledlém stavu se nesmí dát sebrat.

**Přirozené řešení** je proměnná `is_ghost` a podmínka v handleru. **Autorovo řešení** [(10:22)](https://www.youtube.com/watch?v=btCeflqFw4o&t=622s): při vyblednutí se **odpojí signál** `body_entered` a při návratu se zase připojí. Stav mince pak není nikde uložený — **je to samotná existence spojení**. Detail, který je nutný, aby to nespadlo: `disconnect` na nepřipojeném signálu je runtime chyba, takže se před ním ptá `is_connected()`.

Zajímavý technický důsledek stojí za zmínku [(10:22)](https://www.youtube.com/watch?v=btCeflqFw4o&t=622s): `Area2D` hráče **pořád detekuje** — kolize se dějí dál. Vypnutá je jen *reakce na ně*. To je rozdíl, který se hodí znát u ladění: „nic se neděje" může znamenat „nedetekuje" i „detekuje a nikdo neposlouchá".

**Proč to není jen elegance** [(11:09)](https://www.youtube.com/watch?v=btCeflqFw4o&t=669s). Analogie z videa je dobrá: **dvoje hodiny v domě** — jedny na zdi, jedny na mikrovlnce. Ukazují-li různý čas, kterým věříš? Bez jednoho zdroje pravdy nevíš.

A pak přijde scénář, který ten princip prodá lépe než jakákoli definice [(12:42)](https://www.youtube.com/watch?v=btCeflqFw4o&t=762s). Představ si, že později přidáš **kouzlo, které všechny duchové mince zhmotní**. Skript kouzla udělá to jediné rozumné — připojí signál zpátky. Mince je sebratelná. Jenže `is_ghost` je pořád `true`, protože o něm kouzlo neví. **Dva zdroje pravdy se rozešly** a při dalším tiknutí časovače se spustí špatná větev. Autorův závěr sedí: *„čím víc míst tutéž informaci ukládá, tím větší šance, že jedno z nich někdo aktualizuje a na druhé zapomene."*

> **Pozn.:** Autor je k vlastnímu příkladu férový a přiznává, že by v ostrém projektu *„nejspíš prostě vypnul collision shape"* — a má pravdu, protože to je jednodušší. Jenže tím se princip neztrácí, jen se přesune: **vypnutý collision shape je taky jediný zdroj pravdy**, jen jiný. Poučení tedy nezní „odpojuj signály", ale **„vyber si jedno místo, kde stav bydlí, a všichni ostatní ať se ptají jeho"** — ať už je to spojení, vlastnost nodu, nebo proměnná. Ta chyba, kterou to má vyloučit, je jinak neviditelná: hra funguje, dokud se dvě kopie neshodnou, a pak se chová nepředvídatelně bez chybové hlášky. Příbuzné je to [invariantu](../rejstrik.md#invariant) a tomu, proč [gameplay tagy](../praxe/gameplay-tags.md#hierarchie-misto-booleanu-proc-statusmovementblocked-vyhrava) vytlačují booleanovou špagetu.

**Souvislosti:** [Event bus](#event-bus-kdyz-se-systemy-nemaji-cim-potkat) · [Gameplay Tags: hierarchie místo booleanů](../praxe/gameplay-tags.md#hierarchie-misto-booleanu-proc-statusmovementblocked-vyhrava) *(týž problém, jiný lék)* · [Vlastnictví napřed, složky potom](projekt-a-vykon.md#vlastnictvi-napred-slozky-potom-main-game-jako-koordinator) *(jediný vlastník na úrovni scén)* · [Rejstřík: Single source of truth](../rejstrik.md#single-source-of-truth) · [Rejstřík: Invariant](../rejstrik.md#invariant)
