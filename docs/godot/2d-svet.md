# 2D svět: dlaždice, světlo a pixel art

Tři vrstvy toho, jak 2D hra vypadá — a všechny tři mají společné to, že se rozhodují **na začátku a špatně se mění**. Dlaždicový systém určí, kolik kreslení tě čeká (a rozdíl mezi dvěma přístupy je řádový). Osvětlení stojí na třech nodech, které dělají tři různé věci a bez sebe nefungují. A pixel art začíná paletou a rozlišením, ne kreslením.

---

## Dual-grid: 16 dlaždic místo 256

**Zdroj:** [Draw fewer tiles - by using a Dual-Grid system!](https://www.youtube.com/watch?v=jEWFSv3ivTg) · [jess::codes](https://www.youtube.com/channel/UCpM7_d4m2g8rSRZMnPgfWWQ) · ~7 min, technika

**Shrnutí:** Autotiling je kompromis mezi počtem dlaždic a tím, jak dobře sedí na mřížku. Klasická patnáctidílná sada je levná na nakreslení, ale hrany vede **středem dlaždic**, takže nesedí na svět. Sedmačtyřicetidílná sedí, ale je jich sedmačtyřicet. **Dual-grid** ten kompromis ruší: dvě mřížky posunuté o půl dlaždice znamenají, že každá dlaždice má **čtyři sousedy místo osmi** — tedy **16 kombinací místo 256**. Háček je jediný a je to práce na hodinu: musíš si to naskriptovat sám.

### Rozpad myšlenky

**Odkud se berou ta čísla** [(0:00)](https://www.youtube.com/watch?v=jEWFSv3ivTg&t=0s): má-li dlaždice osm sousedů a chceš pro každou kombinaci vlastní obrázek, potřebuješ **256 dlaždic**. Nikdo to nedělá; otázka je, kterou zkratku zvolíš.

**Tři obvyklé sady a jejich daň:**

- **15dílná** [(0:46)](https://www.youtube.com/watch?v=jEWFSv3ivTg&t=46s) — málo dlaždic, ale hrany jsou vedené středem, takže **nesedí na herní mřížku**. Vznikají *„nejednoznačné dlaždice"* (je tohle hlína, nebo tráva?) a položení jedné dlaždice ovlivní větší plochu, než čekáš. Použitelné, když je grafika čistě dekorativní.
- **47dílná** — hrany blízko okraje dlaždice, tedy zarovnané se světem. Cena: **47 dlaždic místo 15**.
- **16dílná podmnožina** [(1:33)](https://www.youtube.com/watch?v=jEWFSv3ivTg&t=93s) — rychlá na výrobu a zarovnaná, ale *„nemusí sednout každému výtvarnému stylu, hlavně těm s detailními vnitřními rohy."* Autorka sama musela dlaždice mírně roztáhnout, aby to nebylo tak vidět. A přidává estetickou výhradu, která platí obecně: u posledních dvou variant se **těžko dělají stejně zaoblené vnitřní i vnější rohy**.

**Jak dual-grid funguje** [(2:20)](https://www.youtube.com/watch?v=jEWFSv3ivTg&t=140s): **první mřížka je datová** — drží informaci, co kde je, a **nic nevykresluje**. **Druhá mřížka je zobrazovací** a je **posunutá o půl dlaždice**. Každá zobrazovaná dlaždice se rozhoduje podle **čtyř datových dlaždic, které překrývá**. Čtyři sousedé znamenají 2⁴ = **16 možností**. A pointa, která to celé uzavírá [(2:55)](https://www.youtube.com/watch?v=jEWFSv3ivTg&t=175s): pro tuhle metodu **chceš** hrany kreslené středem dlaždice — po posunutí sednou přesně na svět. Vada 15dílné sady se stala požadavkem.

**Implementace v Godotu** [(2:55)](https://www.youtube.com/watch?v=jEWFSv3ivTg&t=175s) jsou dvě `TileMap` vrstvy (druhá s posunem) a skript, který drží tabulku šestnácti kombinací → souřadnice v atlasu. Nejtrapnější část je podle autorky **znaménko u souřadnic sousedů** [(3:44)](https://www.youtube.com/watch?v=jEWFSv3ivTg&t=224s): z datové mřížky na zobrazovací se sousedé hledají na `(0,0)`, `(1,0)`, `(0,1)`, `(1,1)`, opačným směrem na týchž souřadnicích **se záporným znaménkem**. *„Chvíli mi trvalo, než jsem to pochopila, ale v kódu je to jen plus místo mínus."* Editovat se dá normálně na datové mřížce; zobrazovací se vygeneruje.

**Kolik to reálně ušetří,** ukazuje nejlíp autorčino číslo [(4:32)](https://www.youtube.com/watch?v=jEWFSv3ivTg&t=272s): jedenáctisnímková animace pobřeží by při běžném autotilingu znamenala **507 dlaždic**; s dual-gridem jich nakreslila **155**.

> **Pozn.:** Godot 4.6 mezitím [zpříjemnil terénní malování](zaklady.md#editor-se-prohledava-ne-prochazi) — terrain sety s volbou *match corners and sides* umí autotiling nastavit klikáním a bez skriptu, takže u projektu, kde je grafika dekorativní a dlaždic málo, je vestavěná cesta rychlejší. **Dual-grid se vyplatí přesně tam, kde bolest roste s počtem variant**: víc typů povrchu, náhodné variace, animované přechody. Rozhodovací otázka tedy nezní „která metoda je lepší", ale **„kolik dlaždic budu doopravdy kreslit?"** Autorka mimochodem dodává radu, která platí i pro ty, co u klasického autotilingu zůstanou: **použij generátor sad dlaždic** — *„kéž bych s tím začala mnohem dřív."*

**Souvislosti:** [Pixel art do Godotu](#pixel-art-do-godotu-paleta-silueta-a-jedno-nastaveni) *(jak se ty dlaždice do enginu dostanou)* · [Editor se prohledává](zaklady.md#editor-se-prohledava-ne-prochazi) *(vestavěné terrain malování ve 4.6)* · [Mapa 2D nodů](zaklady.md#mapa-2d-nodu-vyber-tela-je-prvni-designove-rozhodnuti) · [Rejstřík: Tile set](../rejstrik.md#tile-set) · [Rejstřík: Wave Function Collapse](../rejstrik.md#wave-function-collapse)

---

## Tři nody na světlo: ztmavit, prosvítit, zaclonit

**Zdroj:** [How Much Can 2D Lighting Transform a Godot Game?](https://www.youtube.com/watch?v=BXoaRBsmY7o) · [TechDad Impact](https://www.youtube.com/channel/UCRGAMb_zSjT4hBVdB3JNyPw) · ~17 min, tutoriál

**Shrnutí:** 2D osvětlení v Godotu stojí na třech nodech, které se **musí použít dohromady** a každý dělá něco jiného: `CanvasModulate` scénu ztmaví, `PointLight2D` do té tmy vyřízne světlo, `LightOccluder2D` teprve dodá stíny. Nejdůležitější důsledek toho pořadí je nenápadný: **ztmavení se dotkne i věcí, které svítit mají** — výbuchů, laserů, jisker — takže se pro ně musí předem vyrobit „neztmavovaný" materiál.

### Rozpad myšlenky

**Proč vůbec:** autorova úvodní teze je dobrý rám pro celou kapitolu [(0:05)](https://www.youtube.com/watch?v=BXoaRBsmY7o&t=5s) — rozdíl mezi rozdělanou a hotovou hrou často není v kresbě, ale v tom, jak se na obrázek nanese světlo a post-processing. *„Viděl jsi hry, které vizuálně nejsou nic víc než základní tvary, a přesto působí skvěle a tísnivě."*

**`CanvasModulate` je barevný filtr přes celou scénu** [(1:02)](https://www.youtube.com/watch?v=BXoaRBsmY7o&t=62s) a pracuje **násobením**: zvolená barva se vynásobí s tím, co je pod ní. Protože jsou to čísla mezi 0 a 1, výsledek **nikdy nemůže být světlejší** — čistě bílá tedy neudělá nic, černá udělá tmu. Autor u toho ukazuje poctivost, která stojí za citaci [(2:37)](https://www.youtube.com/watch?v=BXoaRBsmY7o&t=157s): *„popravdě jsem netušil, jak filtr násobení funguje, dokud jsem nedělal tohle video. Jako všichni ostatní jsem si to musel vygooglit."* Praktický důsledek — modulate neslouží jen na tmu, ale i na **večerní oblohu nebo barvu západu slunce**.

**Co ze ztmavení vyjmout** [(4:30)](https://www.youtube.com/watch?v=BXoaRBsmY7o&t=270s) je ta část, kterou by člověk sám neřešil, dokud ho to nekousne: oheň, jiskry, výbuchy, laserové paprsky a jasné částice **mají svítit, ne tmavnout**. Postup je krátký — v inspektoru *Canvas Item → Material → New Canvas Item Material* a **Light Mode na *Unshaded***. K tomu se vyplatí zvážit **Blend Mode na *Additive*** (autor ho používá u střel a jisker). Rada, kterou z toho děláme obecnější: **rozhodni o „svítících" assetech dřív, než jich máš padesát**, protože to je hromadná úprava.

**`PointLight2D` potřebuje texturu** [(5:46)](https://www.youtube.com/watch?v=BXoaRBsmY7o&t=346s) — bez ní nedělá nic. Ta textura **je tvar světla**; jde použít vestavěné gradienty, ale autor preferuje vlastní. Užitečnější než to je vlastnost, kterou modulate nemá [(6:32)](https://www.youtube.com/watch?v=BXoaRBsmY7o&t=392s): **u světel se dá řídit, které objekty ovlivňují**. Pozadí tedy může mít vlastní osvětlení, které neprosakuje do popředí — a to je i **designový nástroj**, protože *„pomáhá hráčům oddělit interaktivní objekty v popředí od dekorací v pozadí."*

**`LightOccluder2D` je třetí node a bez něj nejsou stíny** [(8:06)](https://www.youtube.com/watch?v=BXoaRBsmY7o&t=486s). Skládá se z polygonu, který obkreslíš kolem překážky — a autor u toho dvakrát varuje před cenou: *„každý přidaný polygon přidává výpočty"* a stíny v reálném čase *„se dokážou pěkně rychle prodražit."* Zajímavé je, že **ne každé světlo musí stíny vrhat**, i když se occluderu dotkne, a interakce se dají omezit vrstvami.

**A nejcennější věta celého videa** [(7:19)](https://www.youtube.com/watch?v=BXoaRBsmY7o&t=439s), protože jde proti instinktu: *„stíny v reálném čase vypadají hezky a hodně přidají náladě, ale nemyslím si, že hru automaticky zlepší. Vždycky bys měl mít jasno v tom, proč nějakou funkci používáš."* Autor to sám aplikuje — ve svém asteroidovém levelu **stíny nepoužil**, protože se mu na kulatých organických tvarech nelíbily a *„šťáva nestála za mačkání."*

> **Pozn.:** Dvě věci na okraj. **Occludery na dlaždicích** autor nerozchodil — vznikaly mu mezery mezi dlaždicemi, které rozbíjely stíny, tak occluder nakreslil na úrovni scény přes dlaždice. To je dobrý příklad rozhodnutí typu „obejít, ne dořešit", které v malém projektu bývá správné. A **signed distance fields**, o kterých mluví na konci [(11:12)](https://www.youtube.com/watch?v=BXoaRBsmY7o&t=672s), jsou technika, jak dostat měkké stíny a další efekty výrazně levněji — nechává je na jindy, ale stojí za zapamatování jako směr, kam se dívat, až budou stíny drahé. Kdo chce srovnání s tím, jak se týž problém řeší ve 3D, má v knihovně [osvětlení v UE](../praxe/osvetleni.md); a mlha jako **percepční hranice** má v [PS1 estetice](../praxe/ps1-estetika.md) vlastní výklad.

**Souvislosti:** [Mapa 2D nodů](zaklady.md#mapa-2d-nodu-vyber-tela-je-prvni-designove-rozhodnuti) *(proč PointLight2D potřebuje texturu)* · [Osvětlení v UE](../praxe/osvetleni.md) · [Rejstřík: Overdraw](../rejstrik.md#overdraw) · [Rejstřík: Draw call](../rejstrik.md#draw-call)

---

## Pixel art do Godotu: paleta, silueta a jedno nastavení

**Zdroj:** [How To Pixel Art For Godot](https://www.youtube.com/watch?v=q2bPO4K6r_c) · [Sebbyspoons - Game Dev and Pixel Art](https://www.youtube.com/channel/UC9OzL0W6CGcvdHXtpveUXjw) · ~14 min, tutoriál

**Shrnutí:** Autor rámuje pixel art jako nejpřístupnější výtvarnou formu (*„nejsem školený umělec ani nijak zvlášť zručný — je to jen o znalosti triků a praxi"*) a dává tři rozhodnutí, která se dělají **dřív než první tah**: paleta, rozlišení a perspektiva. K tomu jednu techniku, která mění pořadí práce — **silueta napřed, detail potom** — a jedno nastavení v Godotu, bez kterého bude i skvělá kresba vypadat mizerně.

### Rozpad myšlenky

**Paleta jako první rozhodnutí** [(2:20)](https://www.youtube.com/watch?v=q2bPO4K6r_c&t=140s) a diagnóza vlastního začátečnictví, která sedí: *„moje grafika byla vizuálně chaotická, a nebylo to kvůli kresbě — bylo to kvůli barvám."* Používal výchozí paletu editoru a výsledek nestál za nic. Lék: stáhnout hotovou komunitní paletu a **držet se malého počtu barev, 16 až 32**. Argument, který z toho dělá pravidlo, je psychologický: *„omezení dělá barvy v grafice záměrné — a když grafika působí záměrně, působí dobře."* K tomu miniaturní lekce barevné teorie [(3:53)](https://www.youtube.com/watch?v=q2bPO4K6r_c&t=233s): barvy naproti sobě na kruhu dělají **kontrast**, sousední **harmonii**. *„Nevybírej barvy náhodně, začni je vybírat záměrně."*

**Rozlišení a perspektiva** [(3:53)](https://www.youtube.com/watch?v=q2bPO4K6r_c&t=233s): klasika je 8×8, 16×16, 32×32, případně 64×64, a autor doporučuje **16×16** jako rozumný střed — dost pixelů na pohyb, a přitom se kreslí rychleji než 32×32. Perspektivu (boční plošinovka versus pohled shora) je potřeba vybrat **hodně brzy** a pak se jí držet: *„nezkoušej měnit perspektivu uprostřed projektu. Věř mi."*

**Dvě techniky, které stojí za převzetí:**

- **Silueta napřed** [(6:13)](https://www.youtube.com/watch?v=q2bPO4K6r_c&t=373s). Autor rok kreslil od detailu a obestavoval ho — pak slyšel radu, která to obrátila. Zdůvodnění je věcné: v tak malém měřítku **rozpoznáš věc podle tvaru**, takže tvar je to jediné, co musí sedět. To je táž zásada, jakou má knihovna popsanou u [siluety v art pipeline](../teorie/art-pipeline.md).
- **Zoomuj ven** [(5:27)](https://www.youtube.com/watch?v=q2bPO4K6r_c&t=327s), a to průběžně: kreslíš zblízka, hráč se dívá zdaleka — *„a to je ta verze, na které záleží."* V Asepritu je na to náhledové okno pod F7. Bez toho se stane, že se z postavy při oddálení stane blob.

**Konzistence jako pravidlo** [(6:59)](https://www.youtube.com/watch?v=q2bPO4K6r_c&t=419s): buď mají obrysy všechny objekty, nebo žádný. Míchání *„vypadá, jako by grafiku kreslilo několik různých lidí."* Výjimky ano — ale záměrné.

**A ta jedna věc na straně Godotu** [(8:32)](https://www.youtube.com/watch?v=q2bPO4K6r_c&t=512s), kterou autor slibuje hned v úvodu: `Rendering → Textures → Default Texture Filter` přepnout na **Nearest**. Bez toho engine pixel art vyhlazuje a *„i ta nejlepší kresba bude vypadat příšerně."*

**Zbytek pipeline** je krátký a hodí se jako kontrolní seznam: statický obrázek → `Sprite2D` + *edit region* pro výřez ze sprite sheetu · animace → `AnimatedSprite2D`, *add frames from sprite sheet*, nastavit počet sloupců a řádků **přesně podle mřížky** · dlaždice → `TileMapLayer`, velikost dlaždice podle rozlišení kresby, atlas se nakrájí sám · kolize → *physics layer* a klávesa **F** pro automatický obdélník na vybraných dlaždicích [(10:52)](https://www.youtube.com/watch?v=q2bPO4K6r_c&t=652s) · a nakonec terén pro autotiling. Autor u terénů přiznává, že *„v Godotu umí být trochu ošemetné a zaslouží si vlastní video"* — s čímž souhlasíme a nabízíme [alternativní cestu přes dual-grid](#dual-grid-16-dlazdic-misto-256).

> **Pozn.:** Volba nástroje je krátká a upřímná [(1:33)](https://www.youtube.com/watch?v=q2bPO4K6r_c&t=93s): **Piskel** zdarma v prohlížeči na vyzkoušení · **LibreSprite** jako open-source starší verze Asepritu (nutno si ji zkompilovat) · **Aseprite** jako doporučení za ~20 $. Autor přitom **prodává vlastní pixel-artové balíčky** a v závěru na ně odkazuje — což na věcnosti rad nic nemění, ale patří to říct. Zajímavější je, že tytéž nástroje nezávisle doporučuje i [Firebelley ve svém přehledu](../teorie/planovani-nastroje.md#nastroje-full-time-indie-vyvojare-a-jedna-vec-navic-ktera-neni-software) — shoda dvou nezávislých zdrojů je u doporučení nástrojů asi to nejlepší, co se dá dostat.

**Souvislosti:** [Dual-grid](#dual-grid-16-dlazdic-misto-256) *(alternativa k terénům)* · [Nastavení projektu](prvni-hra.md#nastaveni-projektu-je-soucast-hry-ne-administrativa) *(kde to filtrování bydlí)* · [2D vizuál: pixel art je rozhodnutí](../teorie/2d-vizual.md#pixel-art-je-rozhodnuti-ne-nouzove-reseni) · [Herní art: fokus vzniká ubráním](../teorie/art-pipeline.md) · [Rejstřík: Sprite sheet](../rejstrik.md#sprite-sheet) · [Rejstřík: Nearest-neighbor filtering](../rejstrik.md#nearest-neighbor-filtering) · [Rejstřík: Silueta](../rejstrik.md#silueta)
