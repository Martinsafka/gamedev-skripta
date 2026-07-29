# Stavové automaty a vzory

Kompozice řekne, **z čeho** je entita složená. Stavový automat řekne, **co zrovna dělá**. A strategy pattern řekne, **jak to dělá** — s tou zvláštností, že v Godotu se dá vyměnitelné chování uložit do souboru a přetáhnout myší.

Kapitola jde od nejmenšího dílu k největšímu: nejdřív stav jako pojem, pak vzor pro vyměnitelné chování, a nakonec celý přenositelný systém nepřítele, který obojí používá — a který se dá zkopírovat do jiného projektu složkou.

---

## Stavový automat: stav je podmínka plus chování

**Zdroj:** [Finite State Machines in Godot 4 in Under 10 Minutes](https://www.youtube.com/watch?v=ow_Lum-Agbs) · [Bitlytic](https://www.youtube.com/channel/UCOlPBtGeh1YGL_rWpOLgLyg) · ~7 min, tutoriál

**Shrnutí:** Nepřítel má bloudit, dokud někoho nezahlédne, pak ho honit, a je-li dost blízko, útočit. Napsat to podmínkami jde a u tří stavů je to i správně; u šesti je z toho nečitelná změť. **Stav** je definovaný jako *podmínka plus chování, které k ní patří*, a stavový automat je jejich sbírka plus správa přechodů. Háček, který dělá celý návrh: **automat nesmí vědět, jaké stavy v něm jsou** — zná jen ten aktuální a jméno toho, kam se má přepnout.

### Rozpad myšlenky

**Definice napřed** [(0:00)](https://www.youtube.com/watch?v=ow_Lum-Agbs&t=0s), protože bez ní je to jen složitější `if`. Stav bloudění: **podmínka** = není cíl, **chování** = pohybuj se náhodně. Stav honičky: **podmínka** = je cíl a není v dosahu, **chování** = přibližuj se. Ten rozpad na dvojici je celé kouzlo — podmínka rozhoduje o přechodu, chování o tom, co se děje uvnitř.

**Základní třída `State`** má čtyři metody [(0:47)](https://www.youtube.com/watch?v=ow_Lum-Agbs&t=47s):

- `enter()` a `exit()` — volají se při vstupu a odchodu, tedy tam, kde se stav nastavuje a uklízí,
- `update(delta)` — vázané na vykreslovací snímek,
- `physics_update(delta)` — vázané na fyziku.

Každý stav si k tomu drží **vlastní data**: bloudění má náhodný směr, rychlost a odpočet. V `enter()` se náhodně nastaví, v `update()` se odpočítává a v `physics_update()` se skutečně hýbe. To je celý pattern — a jeho hodnota je v tom, že proměnné bloudění **neexistují nikde jinde**, takže je nemůže omylem přepsat útočná větev.

**Automat sám** [(1:35)](https://www.youtube.com/watch?v=ow_Lum-Agbs&t=95s) je překvapivě hloupý, a to je záměr: *„obvykle je stavový automat úplně agnostický k tomu, jaké stavy jsou uvnitř. Potřebuje vědět jen, jaký je aktuální stav a do kterého se chceš přesunout."* Jeho jediné povinnosti jsou **životní cyklus** (zavolat `exit()` na starém, `enter()` na novém) a **evidence aktuálního stavu**.

**Zapojení do stromu** je zdejší specialita [(2:24)](https://www.youtube.com/watch?v=ow_Lum-Agbs&t=144s): automat je node, jednotlivé stavy jsou **jeho děti**. V `_ready()` projde své potomky, a co je `State`, zapíše si do slovníku podle jména. Přidat stav pak znamená přidat node — bez zásahu do automatu. K tomu `@export var initial_state`, aby šlo v inspektoru určit, kde se začíná.

**Přechody přes signál** [(3:10)](https://www.youtube.com/watch?v=ow_Lum-Agbs&t=190s): `State` má signál `transitioned(state, new_state_name)`, automat se při registraci na každý stav připojí. Stav tedy **neví, kam ho automat přepne** — jen řekne „chci pryč, do stavu jménem X". Autor přidává drobnost z praxe: jména normalizuje přes `to_lower()`, aby velikost písmen nedělala problémy.

**Co autor sám na svém řešení kritizuje** [(6:19)](https://www.youtube.com/watch?v=ow_Lum-Agbs&t=379s), a je to poctivější než většina tutoriálů: (a) oba stavy sahají **přímo na nepřítele**, přičemž lepší by byl mezilehlý objekt, který stavy mění a nepřítel z něj každý snímek čte; (b) tři proměnné se mezi stavy **duplikují**, takže by patřily do společné třídy `EnemyState`, ze které by ostatní dědily.

> **Pozn.:** Srovnání s Unrealem se tady vyplatí, protože ukazuje, kde je hranice ručního řešení. UE má [State Tree](../praxe/state-trees.md#kostra-state-tree-ai-komponenta-tasky-a-kontext) a [Behavior Tree](../praxe/ai-zaklady.md#vyssi-liga-ai-controller-behavior-tree-a-blackboard) jako hotové systémy s editorem, kdežto tady si automat píšeš sám za sedm minut. Obojí má svou cenu: **ruční automat je průhledný a laciný, ale nemá vizualizaci ani ladicí nástroje**, takže u dvaceti stavů se v něm ztratíš stejně, jako by ses ztratil v podmínkách. Praktická hranice, kterou z obou světů čteme: do zhruba **pěti šesti stavů** ruční automat vyhrává; nad tím se vyplatí buď stromová struktura, nebo [Utility AI](../praxe/ai-zaklady.md#utility-ai-rozhodovani-podle-skore-misto-vetveni), kde se stavy neřetězí, ale skórují.

**Souvislosti:** [Strategy: chování jako vyměnitelný resource](#strategy-chovani-jako-vymenitelny-resource) *(týž autor, druhá polovina nářadí)* · [Systém místo nepřítele](#system-misto-nepritele-prenositelny-balik) *(automat uvnitř většího celku)* · [State Trees v UE](../praxe/state-trees.md#kostra-state-tree-ai-komponenta-tasky-a-kontext) · [Základy nepřátelské AI](../praxe/ai-zaklady.md#vyssi-liga-ai-controller-behavior-tree-a-blackboard) · [Rejstřík: State machine](../rejstrik.md#state-machine) · [Rejstřík: Behavior Tree](../rejstrik.md#behavior-tree)

---

## Strategy: chování jako vyměnitelný resource

**Zdroj:** [Modular Upgrades Made Easy Using the Strategy Pattern](https://www.youtube.com/watch?v=sZDJJeDNe_M) · [Bitlytic](https://www.youtube.com/channel/UCOlPBtGeh1YGL_rWpOLgLyg) · ~7 min, tutoriál

**Shrnutí:** Vylepšení střelby jde udělat násobiči poškození — rychle a nudně. Strategy pattern nabízí druhou cestu: **vylepšení je objekt s jedinou metodou**, který dostane vzniklou střelu a něco s ní udělá. Hráč si drží seznam takových objektů a při výstřelu jimi střelu prožene jako **montážní linkou**. A protože strategie v Godotu dědí z `Resource`, dá se uložit do souboru, vystavit v inspektoru a **přetáhnout myší**. Háček, který autor přiznává rovnou: na malý případ je to overkill a on to říká nahlas.

### Rozpad myšlenky

**Autor si nejdřív ustřelí nohu, aby ukázal, kdy to nedělat** [(0:00)](https://www.youtube.com/watch?v=sZDJJeDNe_M&t=0s). Máš pole čísel a chceš z něj vyhodit sudá. Napíšeš podmínku ve smyčce. Chceš místo toho záporná? Změníš podmínku. Jeho vlastní hodnocení: *„je to úplně jednoduché a cokoli víc by skoro určitě bylo over-engineering."* Pak to přesto přepíše na třídu `NumFilter` s metodou `is_filtered(number)` a potomky `EvenNumFilter`, `NegativeNumFilter` — a shrne to bez sebeklamu [(2:21)](https://www.youtube.com/watch?v=sZDJJeDNe_M&t=141s): *„je tohle v tomhle případě přehnané? Ano. Z pětiřádkové funkce jsme udělali dvacet."*

**Kde se to obrátí,** je jediná změna v zadání [(1:35)](https://www.youtube.com/watch?v=sZDJJeDNe_M&t=95s): filtrování se přesune **do funkce, která filtr dostává jako argument**. Od té chvíle je smyčka **hotová napořád** — chceš filtrovat násobky pěti? Napíšeš nový filtr a předáš ho. Do existujícího kódu nesaháš. To je celý zisk vzoru: **rozšíření bez zásahu**.

**Herní podoba** [(3:57)](https://www.youtube.com/watch?v=sZDJJeDNe_M&t=237s): `BaseBulletStrategy extends Resource` s metodou `apply_upgrade(bullet)`, která ve výchozím stavu nedělá nic. `DamageBulletStrategy` přičte pět k poškození, `SpeedBulletStrategy` zrychlí, další přidá průraz. Hráč drží **pole strategií** a po vytvoření střely je projde a na každou zavolá `apply_upgrade` — *„jako montážní linka"*. Vylepšení ve světě je `Area2D`, které při dotyku přidá svou strategii do hráčova pole.

**Proč `Resource` a ne obyčejná třída,** je ten praktický rozdíl [(4:44)](https://www.youtube.com/watch?v=sZDJJeDNe_M&t=284s). Kdyby to byla jen třída, musel bys ji sestavovat kódem a znovu nastavovat texturu a popisek u každého výskytu. Jako resource se **uloží do souboru** a v něm bydlí i exportované hodnoty (o kolik zrychlit, jaká ikona, jaký text). Nové vylepšení je pak **nový `.tres`**, který se do sběratelného předmětu přetáhne v inspektoru.

**Vlastní strategie za dvě minuty** [(5:30)](https://www.youtube.com/watch?v=sZDJJeDNe_M&t=330s): nový skript, `class_name ParticleBulletStrategy extends BaseBulletStrategy`, přepsat `apply_upgrade` — vytvořit částice, přidat je střele jako dítě, nastavit pozici. Hotovo; zbraně se to netýká. Autor na konec naznačuje rozšíření, které se hodí znát: **strategie se dá uložit i na střelu samotnou** a vyvolat při každém zásahu, čímž vzniknou on-hit efekty.

> **Pozn.:** Godot **nemá interface** a autor to říká rovnou [(0:47)](https://www.youtube.com/watch?v=sZDJJeDNe_M&t=47s): *„protože pracujeme v GDScriptu, který interface nepodporuje, zůstaneme u tříd — v jazyce jako C# bych rozhodně doporučil interface."* Prakticky to znamená, že „základní strategie, která nedělá nic" **není jen konvence, ale nutnost** — supluje kontrakt, který by jinde vynutil kompilátor. Kdo přichází z Unrealu, potká tentýž vzor pod [Blueprint Interfacem](../rejstrik.md#blueprint-interface) a v teorii ho má popsaný ve [dvou vzorech, které používáš denně](../teorie/design-patterns.md#strategy-a-observer-dva-vzory-ktere-v-ue-pouzivas-denne). A rozhodovací otázka zůstává tatáž jako u [parametrického objektu](gdscript.md#od-tri-parametru-k-jednomu-objektu-vlastni-trida-jako-datovy-kontrakt): **kolik míst musím upravit, když přidám variantu?** Odpověď „žádné" je jediný důvod, proč vzor zavádět.

**Souvislosti:** [Stavový automat](#stavovy-automat-stav-je-podminka-plus-chovani) · [Data ven ze skriptu](resources.md#data-ven-ze-skriptu-skript-ridi-chovani-resource-popisuje-co-ta-vec-je) *(resource jako datový nosič — tady nese chování)* · [Design patterns: strategy a observer](../teorie/design-patterns.md#strategy-a-observer-dva-vzory-ktere-v-ue-pouzivas-denne) · [Rejstřík: Strategy pattern](../rejstrik.md#strategy-pattern) · [Rejstřík: Design pattern](../rejstrik.md#design-pattern)

---

## Systém místo nepřítele: přenositelný balík

**Zdroj:** [Beginner Game Dev? Stop Making Basic Enemies || Build Enemy Systems Instead](https://www.youtube.com/watch?v=QXbgOX5Wl9E) · [DeeRaghooGames](https://www.youtube.com/channel/UC-KLgU0nzoCCEU6W16CS3vQ) · ~16 min, tutoriál

**Shrnutí:** Video odpovídá na otázku od diváka, která je lepší než většina tutoriálových témat: *„stavíš systémy v samostatných projektech a pak je slučuješ do skutečné hry — a jak?"* Odpověď je konkrétní: základní scéna nepřítele + **schopnosti jako komponenty** + jednoduchý stavový automat, celé v jedné složce, kterou lze **zkopírovat do jiného projektu**. Varianty pak vznikají [dědičností scén](zaklady.md#editor-se-prohledava-ne-prochazi). Háček, který o tom rozhoduje: systém nesmí obsahovat **jedinou natvrdo zapsanou cestu ven ze sebe**.

### Rozpad myšlenky

**Rozdělení odpovědností** je to hlavní, co se dá převzít [(2:23)](https://www.youtube.com/watch?v=QXbgOX5Wl9E&t=143s):

- **`enemy_base.gd` je tělo.** Dělá `CharacterBody2D` fyzickým objektem — aplikuje gravitaci, na konci snímku volá `move_and_slide()`, drží reference na sprite a raycasty. A pak jedna pomocná funkce, která se ukáže jako klíčová: **`flip_direction()`** otočí sprite *a zároveň otočí raycasty*, aby ukazovaly novým směrem. Autorova poznámka je přesná: *„tenhle skript nerozhoduje, jak ani kdy se hýbat. Jen dodává fyzické nářadí."*
- **`enemy_states.gd` je mozek** [(5:30)](https://www.youtube.com/watch?v=QXbgOX5Wl9E&t=330s). Drží stavy (patrola, honička, ústup, skok, střelba), má `change_state()`, přepíná animace a v `_physics_process` pouští logiku aktuálního stavu. Sám řeší **jen patrolu** — čte raycasty a při okraji nebo zdi zavolá `flip_direction()`. Cokoli složitějšího **předá schopnosti**.
- **Schopnosti jsou komponenty** [(3:56)](https://www.youtube.com/watch?v=QXbgOX5Wl9E&t=236s) v uzlu `Abilities`: `chase_ability`, `jump_ability`, `shoot_ability`. Každá jednu věc.

**Jak nepřítel vidí,** je detail, který drží celý systém přenositelný [(4:42)](https://www.youtube.com/watch?v=QXbgOX5Wl9E&t=282s): `Area2D` s kruhovým tvarem funguje jako **radar**, a nepřítel se hráče **nikdy nedohledává** — reaguje na to, co do radaru vstoupí, a ověří, jestli to patří do skupiny `player`. Vstup i výstup mají signál, takže „ztratil jsem cíl" je událost, ne dotaz.

**Schopnosti detailně** stojí za zmínku, protože ukazují, jak se drobná pravidla mění v čitelné chování:

- **Honička** [(7:51)](https://www.youtube.com/watch?v=QXbgOX5Wl9E&t=471s) přepne do `chase` při vstupu do radaru, do `retreat` při odchodu, a v ústupu **spočítá cestu zpět na výchozí pozici** a dojde tam — teprve pak se vrátí k patrole. Nepřítel se tedy nezasekne tam, kde ho hráč odlákal.
- **Skok** [(9:25)](https://www.youtube.com/watch?v=QXbgOX5Wl9E&t=565s) má **vlastní raycast** na nízké překážky. Zapamatuje si, co dělal předtím, skočí, ve vzduchu **drží dopředný pohyb** (jinak by skákal na místě), a po dopadu buď pokračuje v původní činnosti, nebo — byla-li překážka moc vysoká — se otočí.
- **Střelba** [(10:59)](https://www.youtube.com/watch?v=QXbgOX5Wl9E&t=659s) je celá o **čitelnosti pro hráče**: nestřílí hned. Chvíli se přibližuje (~2 s), pak se zastaví, otočí se k hráči, vypálí **dávku několika ran s prodlevami** a **musí si počkat**, než smí znovu. Autor to rámuje jako férovost — a je to dobrý příklad toho, že prodleva není technický detail, ale designové rozhodnutí.

**Přenos do jiného projektu** [(12:35)](https://www.youtube.com/watch?v=QXbgOX5Wl9E&t=755s): zkopíruješ složku i se závislostmi, na základní scéně dáš *New Inherited Scene* a upravíš. Střelecký nepřítel = zdůraznit střeleckou schopnost; skákavý = vertikální pohyb. *„Nezačínáme od nuly. Všechno základní chování už tam je."*

**Tři pravidla na závěr** [(13:22)](https://www.youtube.com/watch?v=QXbgOX5Wl9E&t=802s), a jsou to ta správná tři: **soběstačnost** (žádné natvrdo zapsané cesty ven — místo „najdi hráče na téhle cestě" reaguj na to, co vstoupí do radaru, a ověř skupinu) · **nastavitelnost** (`@export` na rychlost, sílu skoku, kadenci, život, ať se ladí v inspektoru) · **modularita** (stavy a schopnosti odděleně, jako kostky).

> **Pozn.:** Jedna terminologická výhrada, protože jde o slovo, které se v knihovně používá jinde: autor označuje „mít všechno v jedné složce" za **encapsulation** [(13:22)](https://www.youtube.com/watch?v=QXbgOX5Wl9E&t=802s). To je nadsazené — zapouzdření znamená skrytí vnitřního stavu za rozhraní, ne uklizené soubory. Co popisuje, je spíš **soběstačný modul** a jeho vlastní analogie to trefuje líp než ten pojem: *stěhování, kde počítač, monitor a kabely jsou v jedné krabici, místo aby byly rozházené po pěti.* Věcně má pravdu, jen si vypůjčil cizí slovo. Mimochodem, tohle video je pokračováním úvahy „nedělej malé hry, dělej systémy", která se v knihovně potkává se [scope](../teorie/scope.md) — a stojí za to číst obojí, protože si částečně protiřečí.

**Souvislosti:** [Komponenta má být sobecká](kompozice.md#komponenta-ma-byt-sobecka-test-kamene) *(schopnosti jako komponenty)* · [Stavový automat](#stavovy-automat-stav-je-podminka-plus-chovani) · [Editor se prohledává](zaklady.md#editor-se-prohledava-ne-prochazi) *(dědičnost scén pro varianty)* · [Základy nepřátelské AI](../praxe/ai-zaklady.md#minimalni-nepritel-pawn-sensing-ai-moveto-a-nav-mesh) *(týž nepřítel v UE)* · [AI vnímání](../praxe/ai-vnimani.md) · [Rejstřík: State machine](../rejstrik.md#state-machine) · [Rejstřík: Scene inheritance](../rejstrik.md#scene-inheritance)
