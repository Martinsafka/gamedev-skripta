# Nody, scény a strom

Godot má malý počet konceptů a všechny se používají pořád dokola. Když pochopíš **node**, **scénu** a **strom**, zbytek enginu je už jen katalog. Tahle kapitola staví ten mentální model, projde mapu 2D nodů (protože výběr správného nodu je první designové rozhodnutí, ne detail), shrne, co si přinést, než editor vůbec otevřeš — a ukáže, proč se editor od verze 4.6 vyplatí prohledávat místo procházet.

---

## Nody a scény: strom, který je zároveň architekturou

**Zdroj:** [Godot in 100 Seconds](https://www.youtube.com/watch?v=QKgTZWbwD1U) · [Fireship](https://www.youtube.com/channel/UCsBjURrPoezykLs9EqgamOA) · ~3 min, přehled · + [How to make a Video Game - Godot Beginner Tutorial](https://www.youtube.com/watch?v=LOhfqjmasi0) · [Brackeys](https://www.youtube.com/channel/UCYbK_tjZ2OrIZFBvU6CCMiA) · 77 min, tutoriál

**Shrnutí:** Godot má jediný stavební prvek — **node**, kostku s jednou prací (zobraz obrázek, přehraj zvuk, počítej fyziku) — a jediný způsob, jak z kostek dělat větší celky: **scénu**, což je strom nodů uložený na disk. Scény se vnořují do jiných scén, takže hra je jeden velký strom. Háček, který stojí za celou kapitolu: **ten strom není jen organizační pomůcka, je to tvoje architektura** — kdo je čí rodič, rozhoduje o tom, kdo koho smí volat, co se s čím hýbe a co se dá znovupoužít.

### Rozpad myšlenky

**Co Godot je**, než se pustíme do konceptů [(0:02)](https://www.youtube.com/watch?v=QKgTZWbwD1U&t=2s): open source engine na 2D i 3D, vzniklý 2007 v Argentině, otevřený od roku 2014, s instalací kolem **35 MB**. Kód se píše v C#, C++ nebo v **GDScript** — vlastním jazyce, který Fireship trefně popisuje jako kříženec mezi TypeScriptem a Pythonem. Export je jednoklikový na desktop, web a mobil; konzole jdou přes třetí strany.

**Node je kostka s jednou prací.** Chceš postavu? Poskládáš ji z nodů. Nepřítele? Z nodů. Menu? Z nodů. Brackeys to formuluje jako celý pracovní postup [(5:16)](https://www.youtube.com/watch?v=LOhfqjmasi0&t=316s): *dělat hru v Godotu znamená kombinovat a rozšiřovat nody, dokud nedostaneš, co chceš.* V praxi to vypadá takhle: `CharacterBody2D` (fyzikální tělo řízené skriptem) dostane dítě `AnimatedSprite2D` (grafika) a dítě `CollisionShape2D` (tvar pro fyziku). Tři nody, každý jednu věc, dohromady hráč.

**Scéna je znovupoužitelný balík nodů** [(6:03)](https://www.youtube.com/watch?v=LOhfqjmasi0&t=363s). A tady se to láme — kdyby všechno žilo v jednom velkém světě, byl by to chaos. Scéna může být cokoli od jedné mince po celý level, uloží se na disk a pak se **vnořuje do jiných scén**. Mince, platforma a hráč se vnoří do scény „level 1". Když potom minci změníš, změní se **všude naráz**. Fireship popisuje tentýž mechanismus ze strany souborů [(0:48)](https://www.youtube.com/watch?v=QKgTZWbwD1U&t=48s): uložíš scénu a používáš ji uvnitř jiných scén.

**A z toho vzniká strom.** Nody a scény dohromady tvoří stromovou strukturu — *scene tree* — a node úplně nahoře se jmenuje **root**. Zdánlivě jen názvosloví, prakticky ale ten strom nese tři věci naráz:

- **Transformace se dědí po hierarchii.** Brackeys řeší kameru, která má následovat hráče, jedním tahem [(22:28)](https://www.youtube.com/watch?v=LOhfqjmasi0&t=1348s): přetáhne `Camera2D` pod hráče a hotovo — dítě se hýbe s rodičem. Žádný kód.
- **Pořadí v stromu určuje pořadí vykreslení.** Když hráč mizel *za* platformou, důvod byl prostý [(25:36)](https://www.youtube.com/watch?v=LOhfqjmasi0&t=1536s): uzly se stejným Z indexem se kreslí v pořadí, v jakém jsou ve stromu. Řešení není přeuspořádat strom (to je křehké), ale nastavit hráči **Z index** výš — explicitní pravidlo místo skryté závislosti na pořadí.
- **Strom je komunikační topologie.** Kdo je nad kým, rozhoduje o tom, kdo koho smí volat — to je pravidlo *call down, signal up*, kterému se věnuje [samostatná myšlenka v kapitole o GDScriptu](gdscript.md#call-down-signal-up-kdo-koho-smi-znat).

> **Pozn.:** Pro člověka z Unrealu je nejrychlejší most tenhle: **scéna ≈ Blueprint třída, node ≈ komponenta, scene tree ≈ hierarchie komponent v Blueprintu**, jenže rozdíl je v tom, že v Godotu je „třídou" doslova tentýž strom, který v editoru vidíš, a **vnoření scény do scény je běžná operace, ne výjimka**. Kde v UE řešíš „bude to actor, nebo komponenta?", tady řešíš „bude to node, nebo vlastní scéna?" — a odpověď je stejně pragmatická: vlastní scéna vždycky, když to chceš použít víc než jednou. Srovnej s [rozhodovacím testem „is it a?"](../praxe/principy-architektury.md#dedicnost-test-is-it-a-a-rodic-jako-smlouva) z Unrealu; Godot tlačí ke skládání spíš než k dědění, i když umí obojí.

**Souvislosti:** [Mapa 2D nodů](#mapa-2d-nodu-vyber-tela-je-prvni-designove-rozhodnuti) *(katalog kostek, které máš k dispozici)* · [První hra: znovupoužitelná scéna](prvni-hra.md#znovupouzitelna-scena-jedna-kill-zone-pro-propast-i-pro-slimaka) *(scéna jako balík v praxi)* · [Principy architektury: komponenty místo dědičnosti](../praxe/principy-architektury.md#komponenty-misto-dedicnosti-skladej-misto-vetveni) *(týž spor v UE)* · [Rejstřík: Scene tree](../rejstrik.md#scene-tree) · [Rejstřík: GDScript](../rejstrik.md#gdscript)

---

## Mapa 2D nodů: výběr těla je první designové rozhodnutí

**Zdroj:** [Every 2D Node Explained in 9 Minutes !](https://www.youtube.com/watch?v=22VYNOtrcgM) · [Lukky](https://www.youtube.com/channel/UCQ8hqAX8i9mdcwrnu8e2sIg) · ~9 min, přehled

**Shrnutí:** Godot nemá jedno univerzální „těleso", které si nakonfiguruješ — má **čtyři různá fyzikální těla** a výběr mezi nimi je návrhové rozhodnutí, které se špatně mění zpětně. Zbytek 2D nodů se dá číst jako pár rodin: vykreslování, fyzika, detekce, světlo, navigace, pomůcky. Kdo tu mapu jednou uvidí, přestane vymýšlet věci, které engine už umí.

### Rozpad myšlenky

Video projede všechny 2D nody popořadě; užitečnější je přeskládat je podle toho, **jaký problém řeší**.

**Základ.** `Node2D` je předek všeho 2D [(0:05)](https://www.youtube.com/watch?v=22VYNOtrcgM&t=5s) — drží pozici, rotaci a měřítko. Nic víc; a přesně proto se hodí jako organizační kontejner (Brackeys ho používá na seskupení všech mincí do jedné složky ve stromu).

**Čtyři fyzikální těla — a tohle je ta část, kterou si zapamatuj:**

| tělo | hýbe se | ovlivňuje ostatní | typické použití |
|---|---|---|---|
| `StaticBody2D` | ne (teleportuje se) | ano, ale netlačí | zdi, podlahy, stropy |
| `AnimatableBody2D` | kódem/animací | **tlačí** ostatní z cesty | pohyblivé plošiny, výtahy |
| `RigidBody2D` | gravitací a nárazy | ano | bedny, sudy, všechno „volné" |
| `CharacterBody2D` | přesně kódem | ano | hráč, nepřátelé |

Rozdíl mezi statickým a animatable tělem je ta past, na kterou se naráží nejčastěji [(1:39)](https://www.youtube.com/watch?v=22VYNOtrcgM&t=99s): **statické tělo se dá hýbat, ale nikoho netlačí — jen se teleportuje** do nové pozice. Plošina ze `StaticBody2D` tedy funguje, dokud na ni někdo nestoupne. `AnimatableBody2D` je tentýž node, jen posun správně propíše do fyziky.

`CollisionShape2D` (nebo `CollisionPolygon2D`) musí být **dítětem** fyzikálního těla — samo o sobě nic nedělá.

**Detekce místo kolize.** `Area2D` má dvě role naráz [(3:14)](https://www.youtube.com/watch?v=22VYNOtrcgM&t=194s): je to (a) detekční pole, které hlásí, že něco vstoupilo nebo vystoupilo, a (b) **kus prostoru s vlastní fyzikou a zvukem** — vlastní gravitací, větrem, audio kanály. Z druhé role plyne, že podvodní oblast nebo beztížný prostor nejsou mechanika, kterou musíš programovat; jsou to nastavení jednoho nodu.

**Klouby** (`DampedSpringJoint2D` pružina, `GrooveJoint2D` píst po jedné ose, `PinJoint2D` volná rotace kolem bodu) spojují dvě fyzikální tělesa [(2:26)](https://www.youtube.com/watch?v=22VYNOtrcgM&t=146s). Kdo v Unrealu stavěl [kabely a lana](../praxe/lana-kabely.md), pozná stejnou rodinu constraintů, jen ve 2D a s jednodušším nastavením.

**Světlo ve 2D funguje obráceně, než čekáš** [(4:01)](https://www.youtube.com/watch?v=22VYNOtrcgM&t=241s). Nejdřív musíš scénu **ztmavit** nodem `CanvasModulate` — teprve pak ji 2D světla mají co rozsvítit. A `PointLight2D` navzdory jménu **potřebuje texturu**: tvar světla dělá ta textura, zatímco stíny se počítají z jednoho bodu ve středu [(4:48)](https://www.youtube.com/watch?v=22VYNOtrcgM&t=288s). Odtud i to matoucí jméno. Stín vrhá `LightOccluder2D`, což je samostatný tvar — ne automatika z grafiky.

**Dotazy do světa** jsou dvě varianty téhož [(7:08)](https://www.youtube.com/watch?v=22VYNOtrcgM&t=428s): `RayCast2D` vystřelí nekonečně tenkou čáru, `ShapeCast2D` vystřelí **tvar** (obdélník, kruh). Druhý jmenovaný je odpověď na klasický problém „paprsek proletěl mezerou, kterou by postava neprošla".

**Optimalizační nody, o kterých se neví.** `MultiMeshInstance2D` vykreslí spoustu meshů blízko sebe efektivně (pole trávy) [(5:35)](https://www.youtube.com/watch?v=22VYNOtrcgM&t=335s). `CanvasGroup` **sloučí všechny své děti do jediného draw callu** — třeba průsvitnou láhev i s obsahem [(7:54)](https://www.youtube.com/watch?v=22VYNOtrcgM&t=474s). `VisibleOnScreenNotifier2D` pošle signál, když je objekt na obrazovce; `VisibleOnScreenEnabler2D` se rovnou sám zapne a vypne. To je culling zabalený do nodu.

**A pár, které ušetří kód.** `RemoteTransform2D` nastavuje transformaci cizímu nodu — *chová se jako rodič, aniž by rodičem byl* [(7:08)](https://www.youtube.com/watch?v=22VYNOtrcgM&t=428s), což řeší přesně ty případy, kdy hierarchie chce jednu věc a logika druhou. `Path2D` + `PathFollow2D` posunou node po křivce. `BackBufferCopy` zkopíruje výřez obrazovky do textury, kterou si pak vyzvedneš v shaderu.

> **Pozn.:** Dvě věci, které video zmiňuje mimochodem a stojí za zapamatování. **Navigace ve 2D je ruční práce** — `NavigationRegion2D` si musíš vymezit sám, zatímco ve 3D existuje nástroj na automatické generování nav meshe [(5:35)](https://www.youtube.com/watch?v=22VYNOtrcgM&t=335s). A **`TileMap` je natolik velký, že se do přehledu nevešel** — autor u něj otevřeně říká „na tohle je dokumentace"; my se k němu vrátíme v kapitole o 2D světě.

**Souvislosti:** [Nody a scény](#nody-a-sceny-strom-ktery-je-zaroven-architekturou) *(proč jsou nody jednotkou)* · [První hra: delta a physics process](prvni-hra.md#delta-a-physics-process-proc-se-rychlost-nasobi-casem) *(RayCast2D v praxi u nepřítele)* · [Kabely, lana a Physics Control](../praxe/lana-kabely.md) *(táž rodina constraintů v UE)* · [Optimalizace scény](../praxe/optimalizace.md) *(draw cally a culling z druhé strany)* · [Rejstřík: Draw call](../rejstrik.md#draw-call) · [Rejstřík: Collision mask](../rejstrik.md#collision-mask)

---

## Co si přinést, než otevřeš editor

**Zdroj:** [Godot Beginner Guide 2026: What I Wish I Knew Before Starting](https://www.youtube.com/watch?v=VwbD5_c7Bq0) · [DeeRaghooGames](https://www.youtube.com/channel/UC-KLgU0nzoCCEU6W16CS3vQ) · ~9 min, esej · + [I Wish I Had Known This Before Starting Godot Game Development](https://www.youtube.com/watch?v=TkvRsGstk-w) · [DevWorm](https://www.youtube.com/channel/UCSehnx-yuPok8rOWlPIGGOQ) · ~6 min, esej

**Shrnutí:** Dva autoři s pětiletou praxí v Godotu natočili nezávisle na sobě skoro totožný seznam. Ta shoda je sama o sobě informace: **existuje krátká sada návyků, jejichž absence stojí měsíce**. Konkrétně — základy programování napřed, dokumentace před tutoriálem, statické typování od začátku, signály dřív než později, a „make unique" u každého duplikátu.

### Rozpad myšlenky

**Mám se učit programovat, nebo skočit rovnou do enginu?** Oba autoři odpovídají stejně a stejně opatrně [(0:49)](https://www.youtube.com/watch?v=VwbD5_c7Bq0&t=49s) / [(0:49)](https://www.youtube.com/watch?v=TkvRsGstk-w&t=49s): **znáš-li proměnné, funkce a smyčky, skoč do enginu** — Godot tě učí za pochodu. Neznáš-li je, projdi napřed cokoli, co je vysvětlí (DevWorm doporučuje jednoduchý průvodce Pythonem, protože GDScript je mu syntakticky blízko). To je přesně hranice, kterou popisuje [Stavebnice o pěti kostkách](../teorie/co-se-ucit.md#stavebnice-o-peti-kostkach-promenne-podminky-funkce-smycky-tridy) — pět konceptů, dál už se učíš doménu, ne jazyk.

**Dokumentace není nouzové řešení, je to primární zdroj.** DevWorm to staví ostře [(2:22)](https://www.youtube.com/watch?v=TkvRsGstk-w&t=142s): *tutoriály můžou být kamarád i nejhorší nepřítel — záleží jak je použiješ; jen opsat tutoriál znamená, že se ti informace neusadí.* Když si nejsi jistý, hledej **napřed v dokumentaci**, až potom v tutoriálech. Přidává dobově specifickou výhradu, která se vyplatí číst obecněji: jazykové modely byly trénované na datech starších než Godot 4, takže radí syntax ze tří — *a hlavně, opisování z nich tě nic nenaučí*. DeeRaghoo míří na totéž místo z druhé strany [(1:35)](https://www.youtube.com/watch?v=VwbD5_c7Bq0&t=95s): projdi sekci *getting started* v oficiální dokumentaci a udělej ukázkový projekt „your first 2D game", protože **učí přesně ty základy, které Godot předpokládá, že už máš**.

**Statické typování od prvního dne.** Místo `var speed = 200.0` piš `var speed: float = 200.0` [(3:10)](https://www.youtube.com/watch?v=VwbD5_c7Bq0&t=190s). Důvod není estetika: **Godot ti nahlásí chybu, aniž bys hru spustil** — nesedící typ, špatný argument, celá třída tichých bugů. DevWorm dodává konkrétní scénář [(3:09)](https://www.youtube.com/watch?v=TkvRsGstk-w&t=189s): předáváš hodnotu do funkce a ta má parametr jiného typu → chyba se objeví přímo v editoru. Podrobně [v kapitole o GDScriptu](gdscript.md#gradual-typing-kolik-bezpecnosti-si-koupis).

**„Make unique" je past, na kterou doplatí každý.** Když duplikuješ node, **některé resources se mezi kopiemi sdílejí** [(3:09)](https://www.youtube.com/watch?v=TkvRsGstk-w&t=189s) — DevWorm jmenuje konkrétně velikost collision shapu. Změníš tvar u jednoho nepřítele a změní se u všech. Řešení je jedna položka v kontextovém menu; problém je, že o ní nevíš, dokud tě nekousne. Godot 4.6 na to konečně upozorňuje vizuálně — viz [Editor se prohledává](#editor-se-prohledava-ne-prochazi).

**Znovupoužitelný prvek = vlastní scéna.** Health bar, střela, UI panel [(4:45)](https://www.youtube.com/watch?v=VwbD5_c7Bq0&t=285s). DevWorm ukazuje konkrétní podobu [(3:56)](https://www.youtube.com/watch?v=TkvRsGstk-w&t=236s): scéna s health barem si tahá proměnné z rodičovské scény, do které je instancovaná, takže ji stačí postavit jednou a použít kdekoli.

**A několik věcí, které si zapiš, i když jim zatím nerozumíš** [(3:57)](https://www.youtube.com/watch?v=VwbD5_c7Bq0&t=237s): **signály** se nauč brzy (jsou důvod, proč je engine flexibilní) · **autoload** je zdejší singleton pro skóre, audio manager, save data · **node groups** ti dovolí adresovat všechny dveře nebo všechny žebříky jedním příkazem · **AnimationPlayer** neumí jen animace, ale i UI přechody a herní sekvence · **debug volby** (zobrazení collision shapů, nav meshů, fyziky) ušetří hodiny hledání · **debugger a profiler** většina začátečníků nikdy neotevře.

Dvě negativní pravidla stojí za samostatnou zmínku, protože jdou proti přirozenému sklonu [(3:10)](https://www.youtube.com/watch?v=VwbD5_c7Bq0&t=190s): **nedávej těžkou logiku do `_process` a `_physics_process`** (co nemusí běžet každý snímek, tam nepatří) a **nestav hluboké hierarchie nodů** — *„node tree je tvoje architektura, tak ji používej rozumně"*.

> **Pozn.:** DevWorm zavírá video citací z Redditu, která podle nás patří k lepším rámcům na celý obor [(4:44)](https://www.youtube.com/watch?v=TkvRsGstk-w&t=284s): **vývoj her je řemeslo jako instalatéřina nebo svařování.** Většina lidí začíná tím, že nezná rozdíl mezi dvěma druhy klíčů; část se naštve a odejde, část se zeptá a zůstane. A truhlář se neučí tak, že postaví jednu dokonalou skříň — postaví dvacet ptačích budek, každou jinak, aby si vyzkoušel jinou techniku. To je totéž doporučení jako [malé projekty jako tělocvična](../teorie/prvni-projekty.md) a [pravidlo dělat malé hry](../teorie/scope.md), jen řečené jazykem, který nedovolí romantizovat si talent.

**Souvislosti:** [GDScript: gradual typing](gdscript.md#gradual-typing-kolik-bezpecnosti-si-koupis) *(statické typování v detailu)* · [Editor se prohledává](#editor-se-prohledava-ne-prochazi) *(4.6 zviditelnil sdílené resources)* · [Co se učit: stavebnice o pěti kostkách](../teorie/co-se-ucit.md#stavebnice-o-peti-kostkach-promenne-podminky-funkce-smycky-tridy) *(kde končí jazyk a začíná doména)* · [Jak se učit kódovat: tutoriál je odrazový můstek](../teorie/jak-se-ucit-kodovat.md#aktivni-sledovani-tutorial-je-odrazovy-mustek-ne-recept) · [Tipy do editoru: jak se učit engine](../praxe/editor-tipy.md#jak-se-ucit-engine-rady-po-peti-letech) *(táž rada z unrealí strany)* · [Rejstřík: Autoload](../rejstrik.md#autoload) · [Rejstřík: Signal](../rejstrik.md#signal)

---

## Editor se prohledává, ne prochází

**Zdroj:** [Before You Use Godot 4.6… Watch This (Beginner Guide 2026)](https://www.youtube.com/watch?v=e5imI_IX6ds) · [DeeRaghooGames](https://www.youtube.com/channel/UC-KLgU0nzoCCEU6W16CS3vQ) · ~10 min, přehled · + [Godot 4.6 Tips: 7 Features I Wish I Used Sooner](https://www.youtube.com/watch?v=z-9AI9ZPiLM) · týž kanál · ~13 min, tipy

**Shrnutí:** Godot 4.6 je podle autora *„workflow upgrade, ne upgrade enginu"* — a jádro té změny se dá shrnout jednou větou: **editor je navržený k prohledávání, ne k proklikávání**. Kolem toho se sesypává pár funkcí, které nejsou nové, jen se konečně dají najít: plovoucí panely, filtry nodů a souborů, klikatelné chyby, viditelnost sdílených resources, dědičnost scén a živý inspektor běžící hry.

### Rozpad myšlenky

**Ta věta stojí za doslovné převzetí, protože mění návyk** [(3:11)](https://www.youtube.com/watch?v=e5imI_IX6ds&t=191s): *Godot je navržený tak, aby se prohledával, ne procházel.* Prakticky to znamená naučit se čtyři zkratky a přestat hledat myší — `Ctrl+A` přidá node, `Alt+Shift+O` vybere resource, `F1` otevře kontextovou nápovědu. K tomu **filtry** v panelu nodů a souborů [(3:53)](https://www.youtube.com/watch?v=z-9AI9ZPiLM&t=233s): začneš psát jméno a strom se ti profiltruje, bez scrollování. V tutoriálovém projektu je to zbytečnost, ve chvíli, kdy projekt přeroste tutoriálovou velikost, je to rozdíl mezi prací a hledáním.

**Plovoucí panely** [(2:23)](https://www.youtube.com/watch?v=e5imI_IX6ds&t=143s): skoro každý dok — strom scény, inspektor, výstup — se dá odepnout a odplout, klidně na druhý monitor. Zavřením plovoucího okna se panel vrátí zpátky na místo. Logika, kterou autor nabízí, je „panel podle činnosti": děláš UI → odepni inspektor, píšeš skripty → roztáhni editor kódu, ladíš → dej výstup dopředu.

**Klikatelná chyba** [(5:30)](https://www.youtube.com/watch?v=e5imI_IX6ds&t=330s) je drobnost s velkým dopadem: cesta k souboru v panelu chyb je od 4.6 odkaz, takže z chyby skočíš rovnou do skriptu.

**Sdílený resource je konečně vidět** [(7:55)](https://www.youtube.com/watch?v=e5imI_IX6ds&t=475s). Když duplikuješ node a některý jeho resource je sdílený i jinde, objeví se u něj **ikona řetězu**; najetím zjistíš, na kolika místech se používá, a kliknutím ho uděláš unikátním. To je přesně ta past z předchozí myšlenky, jen konečně s viditelným indikátorem — dřív ses o sdílení dozvěděl až tím, že ti změna prosákla, kam neměla.

**Náhledy a live preview** [(4:43)](https://www.youtube.com/watch?v=e5imI_IX6ds&t=283s): najetím na asset uvidíš jméno, ID, velikost, typ a rozměry; přes *quick load* se dá zapnout živý náhled, takže vidíš výsledek **před** potvrzením. Autor to rámuje pěkně — méně mýlek znamená míň vracení, a to znamená, že zůstaneš ve flow.

**Nauč se ptát uvnitř editoru** [(6:17)](https://www.youtube.com/watch?v=e5imI_IX6ds&t=377s): *největší chyba začátečníků je, že kvůli každé otázce odejdou z editoru na Google.* Pravý klik na node, vlastnost i signál nabízí kontextovou nápovědu; tooltipy se drží nad vším, na čem chvíli podržíš myš (a nedají se vypnout — jsou v designu).

**Dědičnost scén** [(0:49)](https://www.youtube.com/watch?v=z-9AI9ZPiLM&t=49s) je funkce, kterou většina lidí objeví pozdě, a řeší úplně konkrétní bolest. Chceš rychlého, silného a bossovského nepřítele; přirozený tah je scénu třikrát duplikovat. Cena přijde později [(1:35)](https://www.youtube.com/watch?v=z-9AI9ZPiLM&t=95s): **opravíš-li bug v originále, musíš ho opravit ve všech kopiích.** Dědičná scéna místo toho převezme všechno z rodiče a dovolí přepsat jen to, co se liší — základní nepřítel má rychlost 200, rychlá varianta ji přepíše na 400, zbytek zůstane sdílený a vylepšení základu se propíše do všech potomků. Pozor na jméno: **s dědičností tříd to nesouvisí**, tohle je dědičnost stromu nodů.

**Živý inspektor běžící hry** [(3:07)](https://www.youtube.com/watch?v=z-9AI9ZPiLM&t=187s): *remote scene inspector* ukazuje strom scény **za běhu** — projdeš nody, přečteš hodnoty, uvidíš, které skripty jsou aktivní, a vlastnosti můžeš měnit naživo. Autor sám přiznává, že pořád používá `print`, ale u větších projektů je to slepá ulička.

> **Pozn.:** Dvě poctivé výhrady. **Zaprvé** — než přepneš verzi, zazálohuj projekt; autorovi přenos prošel hladce, ale sám zdůrazňuje, že šlo o malý projekt s minimem závislostí [(0:50)](https://www.youtube.com/watch?v=e5imI_IX6ds&t=50s). **Zadruhé** — tohle je obsah svázaný s verzí. Rozdělili jsme ho tak, že co je vlastnost editoru, zůstává tady; co je architektonické rozhodnutí (Resource jako datový nosič, sub-viewporty, terén v tilemapách), patří do kapitol, které se těm tématům věnují celé. Listy funkcí z release notes stárnou; principy ne.

**Souvislosti:** [Co si přinést, než otevřeš editor](#co-si-prinest-nez-otevres-editor) *(past se sdíleným resourcem)* · [Nody a scény](#nody-a-sceny-strom-ktery-je-zaroven-architekturou) *(co dědičnost scén vlastně dědí)* · [Tipy do editoru](../praxe/editor-tipy.md#vybery-navigace-a-drobna-zrychleni) *(tatáž disciplína v UE)* · [Rejstřík: Scene inheritance](../rejstrik.md#scene-inheritance)
