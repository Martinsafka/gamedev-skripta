# Animace a pohyb

Čtyři nástroje, které spolu na první pohled nesouvisejí a ve skutečnosti řeší jednu věc: **jak dostat chování z kódu do dat, se kterými se dá pracovat myší.** AnimationTree přesouvá výběr animace ze změti podmínek do grafu. Křivka přesouvá nelineární vztah ze vzorce do nakresleného grafu. Navigace přesouvá obcházení překážek z ručního řešení do agenta. A skok — ten je tu proto, že se u něj ta hranice láme opačně: **skok, který je cítit, je z devadesáti procent kód**, a žádný nástroj ho za tebe nevymyslí.

---

## AnimationTree: od stromu podmínek ke stromu stavů

**Zdroj:** [Why Animation Trees in Godot 4 are Unbelievably Useful](https://www.youtube.com/watch?v=iElHZhOxGYA) · [Bitlytic](https://www.youtube.com/channel/UCOlPBtGeh1YGL_rWpOLgLyg) · ~8 min, tutoriál

**Shrnutí:** Typický kód pro čtyřsměrnou postavu vezme poslední směr, **slepí z něj řetězec** a pustí animaci podle jména — funguje to a rozpadne se to při páté animaci. AnimationTree tutéž věc řeší grafem: blend space vybírá směr, stavový automat vybírá činnost a nad tím se dají vrstvit další uzly. Háček, na kterém se zaseknou všichni: výchozí režim míchání je určený pro 3D a ve 2D s ním výsledek **nefunguje mezi krajními body** — musí se přepnout na `discrete` nebo `capture`.

### Rozpad myšlenky

**Kontext problému** je jedna z těch věcí, které vypadají neškodně [(0:00)](https://www.youtube.com/watch?v=iElHZhOxGYA&t=0s): vezmi poslední směr, převeď na text, slož jméno animace, přehraj. Sedm animací a je z toho nečitelná fabrika na řetězce, ve které se překlep pozná až za běhu.

**Blend space jako první patro** [(0:47)](https://www.youtube.com/watch?v=iElHZhOxGYA&t=47s): do dvourozměrného prostoru rozmístíš čtyři animace běhu (nahoru, dolů, doleva, doprava) a engine vybere tu nejbližší podle zadaného vektoru. Tady je ta past — výchozí `continuous` je *„určený pro 3D animace, které se dají navzájem míchat"*, takže mezi dvěma sprite animacemi udělá kaši. Dvě použitelné volby: **`discrete`** přehraje nejbližší animaci **od prvního snímku**, **`capture`** udělá totéž, ale **naváže na snímek, u kterého jsi skončil**. Rozdíl je slyšet u chůze — s `discrete` postava při otočení „cukne", s `capture` plyne.

**Osa Y je obrácená.** Drobnost, která stojí půl hodiny hledání [(1:35)](https://www.youtube.com/watch?v=iElHZhOxGYA&t=95s): ve 2D Godotu je **−1 nahoru**, takže běh nahoru přehraje animaci dolů. Autor doporučuje opravit to **v grafu, ne v kódu** — což je dobrá zásada obecně: převrácení os patří k datům, ne k logice.

**Druhé patro je stavový automat** [(2:21)](https://www.youtube.com/watch?v=iElHZhOxGYA&t=141s). Blend space se dá **uložit jako resource** (*Save As*) a pak načíst dovnitř automatu, takže nepřijdeš o rozmístění. Automat pak drží stavy `Idle`, `Run`, `Attack` — každý sám blend space — a přechody mezi nimi. K řízení jsou dvě cesty:

- **Advance conditions** — pojmenované boolovské podmínky, které nastavuješ z kódu (`tree.set(...)`). Funkční, ale znamená to nastavovat zvlášť `idle` i `run`, což jsou dva zápisy testující totéž.
- **Advance expressions** [(4:39)](https://www.youtube.com/watch?v=iElHZhOxGYA&t=279s) — nastavíš stromu *base node* (typicky hráče) a do přechodu napíšeš výraz, který se proti němu vyhodnocuje: `velocity` pro idle → run, `!velocity` zpátky. Autorova definice je přesná: *„výrazy jsou automatické podmínky vyhodnocované proti základnímu uzlu."* Z kódu pak nenastavuješ nic.

**Třetí patro** je `AnimationNodeBlendTree` [(5:25)](https://www.youtube.com/watch?v=iElHZhOxGYA&t=325s) — nejobecnější uzel, do kterého se dá vložit celý dosavadní automat a protáhnout ho dalšími uzly. Prakticky užitečná ukázka je **TimeScale**: celý automat projde uzlem, který mu zrychlí nebo zpomalí přehrávání, a hodnota se dá nastavovat z kódu podle rychlosti postavy.

**A jedna rada z praxe**, kterou nikdo nepíše do dokumentace [(7:02)](https://www.youtube.com/watch?v=iElHZhOxGYA&t=422s): aktivní AnimationTree v editoru překáží, když na scéně pracuješ. Nech ho vypnutý a zapni ho v `_ready()` (`animation_tree.active = true`) — *„tohle dělám pořád."*

> **Pozn.:** Vrstvení, které tu vidíš (blend space → automat → blend tree), je táž architektura jako [Blend Space a State Machine v Unrealu](../praxe/mm-zaklady.md) — a rozdíl je hlavně v tom, že Godot ti dovolí **každé patro uložit jako samostatný resource** a skládat je jako soubory. Zaslouží si to poznámku: **je to totéž rozhodnutí jako u [Resource obecně](resources.md#data-ven-ze-skriptu-skript-ridi-chovani-resource-popisuje-co-ta-vec-je)** — vzít strukturu z kódu a dát ji do souboru, který se dá otevřít v editoru. Cena je stejná: graf se hůř verzuje a hůř se v něm hledá, takže od určité složitosti se vyplatí část logiky vrátit do kódu.

**Souvislosti:** [Stavový automat](stavy-a-vzory.md#stavovy-automat-stav-je-podminka-plus-chovani) *(týž vzor, ale pro chování — ne pro animace)* · [Data ven ze skriptu](resources.md#data-ven-ze-skriptu-skript-ridi-chovani-resource-popisuje-co-ta-vec-je) · [Motion Matching základy](../praxe/mm-zaklady.md) *(kam se tenhle strom vyvine v 3D)* · [Rejstřík: Blend Space](../rejstrik.md#blend-space) · [Rejstřík: State machine](../rejstrik.md#state-machine)

---

## Skok, který rozumí tomu, co hráč chtěl

**Zdroj:** [I Rebuilt the Default Godot Jump to Feel Amazing](https://www.youtube.com/watch?v=s5XoTDwdjVo) · [Coding Quests](https://www.youtube.com/channel/UC_DV_XlyV-JXmAjUjg68ROg) · ~5 min, případovka

**Shrnutí:** Výchozí skok v šabloně `CharacterBody2D` **není rozbitý** — dělá přesně to, co je v kódu. Jen ignoruje, co hráč zjevně chtěl. Autor ho prohnal pěti testy a přestavěl na sedm doplňků, z nichž ani jeden není složitý: asymetrická gravitace, ovládaná výška, coyote time, jump buffer, vzdušné zrychlování, kontrola u vrcholu a korekce rohu. Věta, kterou si z toho odnes: **„z blbého skoku se nedá vyčásticovat."**

### Rozpad myšlenky

**Výchozí stav a jeho čtyři vady** [(0:02)](https://www.youtube.com/watch?v=s5XoTDwdjVo&t=2s): stiskni, nastav svislou rychlost, přidávej gravitaci, přistaň. Problémy vypadnou postupně.

1. **Jedna gravitace na celý oblouk** znamená, že postava „visí" nahoře déle, než chceš. Oprava: **slabší gravitace při stoupání, silnější při pádu.** Výška zůstane zhruba stejná, návrat je rychlejší.
2. **Klepnutí a podržení dávají identický skok** [(0:48)](https://www.youtube.com/watch?v=s5XoTDwdjVo&t=48s). Mario to vyřešil před desítkami let: **pustíš-li tlačítko dřív, ubereš část zbývající stoupavé rychlosti**. Hráč tím ovládá výšku místo toho, aby se pokaždé upsal ke stejnému skoku.
3. **Skok jde jen v přesný okamžik.** Dvě drobné časovačky: **coyote time** drží „povolení od podlahy" ještě **desetinu sekundy** po opuštění hrany (asi šest snímků při 60 FPS), **jump buffer** si naopak zapamatuje stisk těsně **před** dopadem. Autor si při tom všímá věci, která je na Celeste zajímavější než obtížnost: *„Celeste je známá krutou obtížností, ale přitom hráči takhle potichu pomáhá pořád."*
4. **Ovládání ve vzduchu.** Bez něj je dopad rozhodnutý ve chvíli, kdy opustíš zem; s okamžitým ovládáním *„to není skok, ale řízení nákupního vozíku ve vesmíru"* [(1:35)](https://www.youtube.com/watch?v=s5XoTDwdjVo&t=95s). Volba je designová: Super Meat Boy dává silnou korekci, protože jeho levely vyžadují přesnost; těžší platformery zachovávají setrvačnost. Autorovo řešení je **pomalejší zrychlování ve vzduchu** — dá se opravit špatný dopad, aniž bys smazal veškerou setrvačnost.

**Tři přídavky, které to dolaďují** [(2:22)](https://www.youtube.com/watch?v=s5XoTDwdjVo&t=142s): **pár snímků navíc ovládání u vrcholu** — a autor si dává pozor, aby to nebyl návrat k plovoucímu skoku: *„nechceme, aby celý skok působil plovoucně; chceme tu špetku ovládání přesně v okamžiku, kdy hráč míří na dopad."* Dál **fast fall** (stisk dolů při pádu) a nakonec **korekce rohu** [(3:09)](https://www.youtube.com/watch?v=s5XoTDwdjVo&t=189s): dotkne-li se stropu jen jeden roh postavy, je technicky správné skok zrušit — a vizuálně to vypadá špatně. Řešení: když je blokovaná jen jedna strana, zkontroluj místo na druhé a **posuň postavu o pár pixelů**. Autorova pojistka proti zneužití je důležitá — *„nestačí to na protlačení zdí, jen to opraví drobnou chybu, která už vypadala jako úspěch."*

**Až nakonec zpětná vazba** [(3:09)](https://www.youtube.com/watch?v=s5XoTDwdjVo&t=189s): stlačení před odrazem, protažení při stoupání, prach, zvuk odrazu i dopadu, drobné cuknutí kamery po tvrdém pádu — s poznámkou, kterou by si měl přečíst každý, kdo řeší juice dřív než pohyb: *„zpětná vazba dokáže dobrý pohyb vysvětlit, ale nedokáže ho vytvořit."*

> **Pozn.:** Tohle je celé jedna dlouhá ilustrace pravidla, které GMTK na Celeste formuluje jako **„pracuj se záměrem hráče, ne s přesnou simulací stisků"** — viz [Celeste v kapitole o game feelu](../teorie/game-feel.md#celeste-krivky-v-snimcich-a-hrst-tichych-ulev). Za pozornost stojí, že **žádná z těch sedmi úprav nepřidává mechaniku**; všechny jen posouvají hranici mezi „to hráč nestihl" a „to hra nepochopila". A přesně proto se dají převzít i mimo platformer: buffer vstupu se hodí u comb, coyote time u čehokoli s hranou, korekce rohu všude, kde je kolizní tvar hranatější než grafika.

**Souvislosti:** [Celeste: křivky v snímcích](../teorie/game-feel.md#celeste-krivky-v-snimcich-a-hrst-tichych-ulev) *(tytéž triky rozebrané na hotové hře)* · [Delta a physics process](prvni-hra.md#delta-a-physics-process-proc-se-rychlost-nasobi-casem) *(kam ten kód patří)* · [Game feel: katalog juice](../teorie/game-feel.md#katalog-juice-deset-detailu-ktere-prodavaji-tutez-mechaniku) · [Rejstřík: Input buffering](../rejstrik.md#input-buffering) · [Rejstřík: Coyote time](../rejstrik.md#coyote-time) · [Rejstřík: Squash & stretch](../rejstrik.md#squash-stretch)

---

## Křivka místo kódu: nelineární vztah nakreslený myší

**Zdroj:** [save hours of programming using curves | Godot Tutorial](https://www.youtube.com/watch?v=cTSrjN_2qDI) · [AceSpectre](https://www.youtube.com/channel/UCeC2VYbtkE6a_dYSkx9NU2w) · ~3 min, tip

**Shrnutí:** V hrách pořád definuješ vztah mezi vstupem a výstupem — vzdálenost → poškození, čas → poloha plošiny. Lineární vztahy se píší snadno; **nelineární se v kódu píší mizerně**. `Curve` je resource, do kterého ten vztah **nakreslíš**, a v kódu z něj jen vzorkuješ. Kód se zkrátí a — což je důležitější — **je vidět, co dělá**.

### Rozpad myšlenky

**Kontext problému** je popsaný v jedné větě, která platí obecněji než jen pro Godot [(0:02)](https://www.youtube.com/watch?v=cTSrjN_2qDI&t=2s): *„zatímco lineární vztahy se v kódu vyjadřují snadno, nelineární je vyjádřit dost těžké."* A pak přijde ta pointa: *„místo abys damage drop-off vypisoval, je mnohem snazší podívat se na graf, který chceš — a vzít ho z toho grafu."*

**Dva příklady, které stačí k pochopení celého vzoru:**

- **Pohyblivá plošina** [(1:35)](https://www.youtube.com/watch?v=cTSrjN_2qDI&t=95s). Verze bez křivky je pár řádků: jeď mezi dvěma body a na koncích otoč směr. Verze s křivkou je o **něco delší**, což autor přiznává — ale za tu cenu dostaneš libovolný průběh. Mechanismus: každý fyzikální snímek se poloha nastaví jako interpolace mezi počátkem a koncem dráhy, kde vzorkovací bod **cestuje mezi 0 a 1 a odráží se**. Křivka pak určuje *jak* — zpomalení na koncích, prudký start, prodleva uprostřed.
- **Damage drop-off** [(2:22)](https://www.youtube.com/watch?v=cTSrjN_2qDI&t=142s). Spočítáš vzdálenost k cíli, vydělíš maximálním dosahem zbraně, a tím číslem (0 až 1) vzorkuješ křivku. Výstup je **násobič poškození**, kde 1 je plný zásah nablízko a hodnota klesá s dálkou přesně tak, jak jsi to nakreslil.

**Proč to stojí za samostatnou myšlenku,** i když je video tříminutové: tenhle vzor je **přenositelný na cokoli, co má vstup a výstup**. Hlasitost podle vzdálenosti, síla otřesu kamery podle poškození, hustota částic podle rychlosti, průhlednost podle výšky. Kdykoli přistihneš sám sebe, jak v kódu skládáš tři podmínky, aby výsledek „nějak hezky klesal", je to signál pro křivku.

> **Pozn.:** Skutečná hodnota není v ušetřených řádcích, ale v **ladicí smyčce**. Nakreslenou křivku upravíš a hned vidíš výsledek; vzorec musíš přečíst, pochopit a přepsat. To je táž výhoda, kterou má [Resource nad natvrdo zapsanými hodnotami](resources.md#data-ven-ze-skriptu-skript-ridi-chovani-resource-popisuje-co-ta-vec-je) — a stejná mez: **do křivky nepatří rozhodnutí, jen průběh.** Jakmile by křivka měla mít podmínky („po zásahu se chová jinak"), je to signál, že jsi překročil, k čemu je.

**Souvislosti:** [Data ven ze skriptu](resources.md#data-ven-ze-skriptu-skript-ridi-chovani-resource-popisuje-co-ta-vec-je) *(týž princip o patro výš)* · [Skok, který rozumí hráči](#skok-ktery-rozumi-tomu-co-hrac-chtel) *(asymetrická gravitace je křivka napsaná ručně)* · [Timeline a Curve v UE](../praxe/interakce-bez-event-ticku.md) · [Rejstřík: Lerp](../rejstrik.md#lerp) · [Rejstřík: Timeline](../rejstrik.md#timeline)

---

## Nepřítel, který obchází překážky: navigace ve 2D je ruční práce

**Zdroj:** [Enemy Pathfinding AI in Godot 4](https://www.youtube.com/watch?v=OZCApGqUHGU) · [TheYellowDude](https://www.youtube.com/channel/UCO-wfM9DpFJzlk2IiRMtpuw) · ~3 min, tutoriál

**Shrnutí:** Navigace stojí na dvou nodech: **`NavigationRegion2D`** vymezí, kudy se dá chodit, a **`NavigationAgent2D`** uvnitř nepřítele počítá cestu. Rozdíl proti 3D je ten, který stojí za zapamatování: **ve 2D si navigační polygon musíš obkreslit ručně**, kdežto ve 3D existuje nástroj na jeho generování. Háček, který rozhoduje o tom, jestli se nepřítel zasekne: **agent size** se nastavuje na regionu, ne na agentovi.

### Rozpad myšlenky

**Postup** je krátký [(0:03)](https://www.youtube.com/watch?v=OZCApGqUHGU&t=3s): přidej `NavigationRegion2D`, **přesuň pod něj všechny překážky**, vytvoř navigační polygon a obkresli plochu kolem překážek. Jakmile se tvar uzavře, engine si polygon převezme.

**A teď to jediné číslo, které se dá snadno přehlédnout**: **agent size** v navigačním polygonu. Autor ho nastavuje na 50 s odůvodněním, které je celý smysl toho parametru — *„aby se nepřítel nezasekával mezi překážkami."* Polygon se totiž o tuhle hodnotu **zúží dovnitř**, takže agent nikdy nedostane cestu, do které se fyzicky nevejde. Vede to k pravidlu palce: agent size ≈ poloměr největšího tělesa, které se po té ploše bude pohybovat.

**Uvnitř nepřítele** pak `NavigationAgent2D` [(0:50)](https://www.youtube.com/watch?v=OZCApGqUHGU&t=50s) se zapnutým **avoidance** (vyhýbáním). Smyčka má tři kroky: zjisti současnou pozici, vyžádej si od agenta **další bod cesty** (`get_next_path_position`), spočítej směr mezi nimi a **předej ho agentovi jako požadovanou rychlost**. Cílová pozice se agentovi nastavuje zvlášť — v ukázce každý snímek na pozici hráče.

**Proč se rychlost dává agentovi a nepoužije se rovnou** [(1:37)](https://www.youtube.com/watch?v=OZCApGqUHGU&t=97s): protože se vyhýbáním zapnutým je vypočtená rychlost jen **návrh**. Agent ji porovná s ostatními agenty a vrátí **bezpečnou rychlost** signálem `velocity_computed`; teprve v jeho obsluze se skutečně hýbeš — a to ještě přes `move_toward`, aby postava do nového směru **přecházela plynule** místo lámaných otoček.

> **Pozn.:** Ve srovnání s [nav meshem v Unrealu](../praxe/ai-zaklady.md#minimalni-nepritel-pawn-sensing-ai-moveto-a-nav-mesh) je to znát: tam nav mesh vzniká automaticky z geometrie a `AI MoveTo` schová i tu bezpečnou rychlost, tady si obojí skládáš sám. Jeden důsledek, který video neřekne, ale plyne z toho ručního obkreslování: **změníš-li level, navigace se sama neaktualizuje** — a to je přesně ten druh nesouladu, který se pozná až v testu. Praktická obrana je držet překážky i region v jedné scéně a při editaci levelu si polygon vždy překontrolovat. Zbytek chování nepřítele (kdy vůbec začne hráče honit) řeší [systém nepřítele](stavy-a-vzory.md#system-misto-nepritele-prenositelny-balik) — navigace je jen „jak se tam dostat", ne „proč tam jdu".

**Souvislosti:** [Systém místo nepřítele](stavy-a-vzory.md#system-misto-nepritele-prenositelny-balik) *(rozhodování nad navigací)* · [Mapa 2D nodů](zaklady.md#mapa-2d-nodu-vyber-tela-je-prvni-designove-rozhodnuti) *(navigační nody v přehledu)* · [Základy nepřátelské AI](../praxe/ai-zaklady.md#minimalni-nepritel-pawn-sensing-ai-moveto-a-nav-mesh) · [Rejstřík: Nav Mesh](../rejstrik.md#nav-mesh) · [Rejstřík: Context steering](../rejstrik.md#context-steering)
