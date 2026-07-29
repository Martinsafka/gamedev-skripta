# Případovka: vizuál a zvuk

Vizuální stránka projektu je zajímavá tím, jak často se v ní **správné řešení najde až po sérii špatných**. Autor se pokouší o glow efekt čtyřmi způsoby (a při jednom z nich shodí celý počítač), redesignuje hlavní postavu přes pět kol návrhů a nakonec zjistí, že rozhodujícím kritériem nebyla kresba, ale **silueta**.

Kapitola končí dvěma věcmi, které stojí pár řádků a jsou vidět (respektive slyšet) okamžitě: měřítko pixel artu a náhodná výška tónu.

---

## Světlo: normal mapy a cesta k nim

**Zdroj:** [Lighting VFX Completely Changed my Game!](https://www.youtube.com/watch?v=TS0hP7wX-zI) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~16 min, devlog

**Shrnutí:** Cíl byl „retro pixel art s moderním osvětlením" a cesta k němu vedla přes **čtyři nepovedené pokusy o glow**. Poučení je v tom, kde ta chyba byla: autor vzorkoval **obrazovku ve 2K** místo interního obrazu ve 640 × 360, takže efekt buď nebyl vidět, nebo stál tolik, že spadl počítač. Dynamické osvětlení pak vyřešily **normal mapy** vygenerované nástrojem — a jedna nečekaná vlastnost jeho vrstvené kamery se ukázala jako výhoda.

### Rozpad myšlenky

**Zadání přišlo od výtvarníka** [(1:37)](https://www.youtube.com/watch?v=TS0hP7wX-zI&t=97s) a je to hezký příklad toho, že technická rozhodnutí mají termín: výtvarník potřeboval vědět, jestli má do konceptů kreslit **gradienty, mlhu a záři**, nebo držet čistě retro. Odpověď „chci retro s moderními efekty" znamenala, že se to **musí naprogramovat dřív**, než začne kreslit.

**Čtyři pokusy o glow**, každý s vlastním poučením [(3:57)](https://www.youtube.com/watch?v=TS0hP7wX-zI&t=237s):

1. **Vzorkuj sousední pixely na obrazovce.** Výsledek: *„vypadá to jako jednopixelový červený obrys, nedává to smysl"* — protože při 2K rozlišení je okolí jednoho pixelu mikroskopické.
2. **Vzorkuj do vzdálenosti 15 pixelů ve čtyřech směrech.** Vznikne **hvězda**, protože se vzorkuje jen po osách. Autor je férový: *„kdyby takhle zářilo všechno, vypadalo by to blbě — ale u hvězd na noční obloze by to mohlo být super."*
3. **Vzorkuj v bloku s útlumem podle vzdálenosti.** Fungovalo, vypadalo *„ne moc dobře"*, a při pokusu zvětšit poloměr *„jsem shodil nejen editor, ale celý počítač."* Jeho vlastní shrnutí je nejlepší formulace toho problému: *„nenech každý pixel na obrazovce vzorkovat padesát tisíc jiných pixelů každý snímek."*
4. **Zesil vliv zářících pixelů.** Vznikl *„mega glow"*, kde září všechno.

**Až pak přišlo to správné** [(7:02)](https://www.youtube.com/watch?v=TS0hP7wX-zI&t=422s): *„vzorkovat obrazovku pro pixel-artovou hru vlastně vůbec nedává smysl"* — a vzorkovat se má **textura viewportu**, která má 640 × 360. Menší obraz znamená, že se dá vzorkovat pořádně, a navíc se dá **zmenšit ještě víc** a získat rozostření zadarmo. Efekt je nakonec jemný a autor to bere: *„byl jsem už unavený z ladění glow efektů, a fungující glow mi stačí."*

**Dynamické světlo přes normal mapy** [(8:35)](https://www.youtube.com/watch?v=TS0hP7wX-zI&t=515s) je druhá polovina. Normal mapa je *„druhý obrázek, který spritu říká, jak má reagovat na světlo"* — autor to vysvětluje na vlastní paži nasvícené z jedné strany. Vygeneroval je nástrojem přímo ze sprite sheetů, s nastavitelnou „hrbolatostí" a plynulostí přechodu. Rozdíl před a po je podle něj zásadní: bez normal map se na postavu *„jen přemaluje jas"*, s nimi *„je vidět, jak světlo padá do listí a osvětluje kmen"*.

**A ta nečekaná výhoda** [(10:57)](https://www.youtube.com/watch?v=TS0hP7wX-zI&t=657s): protože jeho kamera renderuje do [několika vrstev](pripadovka-kamera.md#lasagna-kamera-subpixelovy-posun-v-shaderu), světlo z jedné vrstvy neovlivňuje sprity na jiné — takže **každé světlo se musí naklonovat do všech viewportů**. Zní to jako komplikace a autor z toho udělal nástroj: světlo v pozadí **při průchodu vrstvami slábne**, takže lampa daleko vzadu neosvětluje postavu v popředí. Omezení se stalo hloubkovým efektem.

**Den a noc jedním posuvníkem** [(12:29)](https://www.youtube.com/watch?v=TS0hP7wX-zI&t=749s): `CanvasModulate` ztlumí celou scénu do noci a lampy pak scénu prosvítí — a protože je to jen barva, dá se **plynule přejít** z dne do noci a nechat lampy „naskočit". To je táž trojice nodů, jakou má sekce popsanou u [2D světla](2d-svet.md#tri-nody-na-svetlo-ztmavit-prosvitit-zaclonit), jen použitá dramaturgicky místo staticky.

> **Pozn.:** Nejcennější kus je ta chyba s měřítkem, a stojí za zobecnění: **efekt musí pracovat v rozlišení, ve kterém je hra navržená, ne v rozlišení monitoru.** Sedmnáctka pixelů kolem spritu je v 640 × 360 znatelný halo, ve 2K je to neviditelná linka — a mezi tím je faktor, kterým se násobí i cena výpočtu. Kdo pracuje v pixel artu, má tenhle přepočet dělat u každého efektu, který se počítá „na pixel". A jedna poctivá poznámka k celému postupu: autor sám přiznává, že s vestavěným řešením záře **narazil na chybu, kterou nerozluštil**, a vlastní systém psal částečně proto — což je legitimní důvod, ale ne důvod ho doporučovat ostatním.

**Souvislosti:** [Tři nody na světlo](2d-svet.md#tri-nody-na-svetlo-ztmavit-prosvitit-zaclonit) *(tytéž nody jako návod)* · [Lasagna kamera](pripadovka-kamera.md#lasagna-kamera-subpixelovy-posun-v-shaderu) *(proč se světla klonují)* · [Osvětlení v UE](../praxe/osvetleni.md) · [Rejstřík: Normal mapa](../rejstrik.md#normal-mapa) · [Rejstřík: Render target](../rejstrik.md#render-target)

---

## Redesign postavy: rozhoduje silueta

**Zdroj:** [Redesigning the Main Character of my Indie Game! | Devlog](https://www.youtube.com/watch?v=HsWnv6rCiJ4) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~25 min, devlog

**Shrnutí:** Autor kreslil hlavní postavu sám a byl s ní spokojený — dokud do projektu nepřišel lepší výtvarník. Redesign proběhl v pěti kolech (velikost spritu, póza, účes, oblek, barvy) a je poučný ve dvou věcech: kritériem, které nakonec rozhodlo, byla **čitelnost siluety**, a autor při tom naráží na problém, který má každý iterativní návrh — **po pátém kole jsou všechny varianty dobré a přestává se dát rozhodovat**.

### Rozpad myšlenky

**Proč vůbec** [(0:50)](https://www.youtube.com/watch?v=HsWnv6rCiJ4&t=50s), a je to poctivé: jeho vlastní pixel art byl *„vrchol mých schopností"* a *„problém je, že to není zas tak dobré"*. Když většinu grafiky přebírá někdo lepší, **hlavní postava musí odpovídat zbytku**. K tomu si autor bere za cíl historku o Mario 64: *„chci, aby bylo zábavné jen tak s Isadorou pobíhat dokola"* — tedy aby postava obstála i bez levelu kolem sebe. To je táž laťka, jakou nastavují [autoři Celeste](../teorie/game-feel.md#celeste-krivky-v-snimcich-a-hrst-tichych-ulev).

**První rozhodnutí je technické, ne výtvarné** [(2:23)](https://www.youtube.com/watch?v=HsWnv6rCiJ4&t=143s): **32 × 32, nebo 48 × 48?** Menší je *„retro, snáz se animuje"*, větší dá *„víc výrazu a možností"*. Autor volí větší — a rovnou tuší cenu: *„to bude pro projekt problém, ale vyřeším ho, až na něj dojde."* Dojde na něj o dva dny později [(16:24)](https://www.youtube.com/watch?v=HsWnv6rCiJ4&t=984s): větší postava znamená **změnit rozlišení hry** ze 480 × 270 na **640 × 360**, jinak by najednou zabírala moc obrazovky. Rozhodnutí o velikosti spritu je tedy **rozhodnutí o rozlišení hry** — a to je [jednosměrné dveře](projekt-a-vykon.md#vizualni-pohodli-nesmi-diktovat-fyzikalni-pravdu).

**Silueta jako rozhodovací kritérium** [(7:05)](https://www.youtube.com/watch?v=HsWnv6rCiJ4&t=425s) je nejcennější věta celého videa: mezi pěti návrhy má nejradši jeden, *„ale ze všech má nejsilnější siluetu ta druhá — je čitelná i z dálky, poznáš, co se s postavou děje, takže by animace vypadaly mnohem líp."* Řešení, ke kterému směřuje, je typicky iterační: **vzít siluetu z jednoho návrhu a zbytek z druhého**. U účesu volí podobně [(11:43)](https://www.youtube.com/watch?v=HsWnv6rCiJ4&t=703s): vybraný cop *„dělá zajímavější siluetu, protože nahoře je jeden špičatý kus místo culíku, jaký jsi viděl ve stu milionech postav"*.

**A ta past iterativního návrhu** [(11:43)](https://www.youtube.com/watch?v=HsWnv6rCiJ4&t=703s), kterou pojmenovává přesně: *„narážíme na problém, že všechny návrhy jsou docela dobré, a je čím dál těžší mezi nimi smysluplně rozlišovat."* Jeho východisko není estetické, ale obsahové — **klonit se k tomu, co nejvíc sedí postavě a jejímu příběhu**. Když přestane fungovat „co je hezčí", musí nastoupit „co je pravdivější". Finální volbu popisuje testem, který je použitelný obecně [(23:23)](https://www.youtube.com/watch?v=HsWnv6rCiJ4&t=1403s): *„když se na ten návrh podívám, řeknu si ‚to je ona' — ne ‚kterými způsoby by to mohla být ona'."*

**Komunita jako spolurozhodující** je u něj systém, ne gesto: každé kolo návrhů **ukáže divákům dřív, než řekne svůj názor** (*„než ty vody otrávím vlastním názorem"*), a u mečů rovnou přiznává, že názor nemá a chce ho odjinud [(21:04)](https://www.youtube.com/watch?v=HsWnv6rCiJ4&t=1264s). To je levný způsob, jak si rozšířit vzorek — a zároveň se z toho stává obsah.

> **Pozn.:** Za pozornost stojí, jak dlouho ten redesign **blokoval jinou práci**: autor odkládá přepis pohybového systému, dokud nebude postava hotová, *„protože chci mít v enginu její nový sprite s běžeckou animací, abych viděl, jak to ovlivní zbytek"*. To je rozumné — ale znamená to, že **výtvarné rozhodnutí drží technický plán**, a stojí za to to při plánování vědět. Silueta jako hlavní kritérium má v knihovně vlastní výklad v [art pipeline](../teorie/art-pipeline.md) a u [vizuální komunikace](../teorie/vizualni-komunikace.md); tady je hezky vidět, proč platí obzvlášť v pixel artu — při 48 pixelech výšky **není na čitelnost detailu místo** a tvar je skoro všechno, co zbývá.

**Souvislosti:** [Pixel art má měřítko](#pixel-art-ma-meritko-mixely-a-velikost-platna) *(důsledky té volby velikosti)* · [Vizuální pohodlí nesmí diktovat fyzikální pravdu](projekt-a-vykon.md#vizualni-pohodli-nesmi-diktovat-fyzikalni-pravdu) *(rozlišení jako one-way door)* · [Herní art: pipeline](../teorie/art-pipeline.md) · [Vizuální komunikace](../teorie/vizualni-komunikace.md) · [Rejstřík: Silueta](../rejstrik.md#silueta) · [Rejstřík: Shape language](../rejstrik.md#shape-language)

---

## Barvy: hue shifting a palette swap přes shader

**Zdroj:** [Game Dev Secrets: The Key to Colors!](https://www.youtube.com/watch?v=x8EGyYUELUw) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~2 min · + [Game Dev Secrets: Palette Swaps!](https://www.youtube.com/watch?v=7joIPGLcWHY) · týž kanál · ~1 min

**Shrnutí:** Dvě techniky práce s barvou, obě levné a obě s okamžitě viditelným výsledkem. **Hue shifting**: stíny a světla se nedělají ztmavením a zesvětlením, ale **posunem odstínu** — světlo k barvě zdroje, stín od ní. **Palette swap**: druhá barevná varianta nepřítele se nekreslí znovu, ale **vyrobí shaderem**, který přemapuje jednu paletu na druhou.

### Rozpad myšlenky

**Proč nestačí přidat jas** [(0:48)](https://www.youtube.com/watch?v=x8EGyYUELUw&t=48s): sprite, kde jsou světla jen zesvětlená a stíny ztmavené základní barvy, působí *„vybledle"*. Postup, který to opraví:

- **Světlo** — zvyš jas, **posuň odstín k barvě světla** (většinou k žluté, protože slunce) a **sniž sytost**, aby se napodobilo vyblednutí od světla.
- **Stín** — sniž jas, **posuň odstín pryč od světla** (typicky k fialové) a **zvyš sytost**. Přesný opak.

Autorovo shrnutí je věrohodné právě tou skromností: *„zní to jednoduše, a taky to jednoduché je — ale i malý posun odstínu dokáže spritu dodat spoustu života."*

**Palette swap** [(0:01)](https://www.youtube.com/watch?v=7joIPGLcWHY&t=1s) řeší jinou otázku: dva stejní nepřátelé na obrazovce se **špatně rozlišují**. Ruční přebarvení každého snímku je *„nesmírně otravné"* a navíc znamená druhou sadu souborů pro tutéž postavu. Shaderové řešení je čisté: dostane **vstupní paletu** (původní barvy) a **výstupní paletu**, projde každý pixel, najde jeho barvu ve vstupní a nahradí ji odpovídající z výstupní.

Zisk není jen v ušetřené práci. **Varianta přestane být assetem a stane se datem** — a data se dají generovat, náhodně vybírat, vázat na obtížnost nebo na region. Ta cesta „z assetu do dat" je přesně to, o čem je [kapitola o Resourcech](resources.md#data-ven-ze-skriptu-skript-ridi-chovani-resource-popisuje-co-ta-vec-je).

> **Pozn.:** Hue shifting je zároveň důvod, proč se v pixel artu doporučuje **malá paleta** — kdo míchá barvy volně, k posunu odstínu se nedostane, protože nemá řád, ve kterém by ho dělal. Souvislost s [paletou jako prvním rozhodnutím](2d-svet.md#pixel-art-do-godotu-paleta-silueta-a-jedno-nastaveni) je tedy věcná, ne asociativní. A k palette swapu jednu výhradu, kterou video nezmiňuje: **funguje jen tak dobře, jak dobře je paleta oddělená.** Sdílí-li kůže a oblek tentýž odstín, přebarvíš i to, co jsi přebarvit nechtěl — takže se vyplatí navrhovat sprity s vědomím, že se budou swapovat. Historicky je to mimochodem technika z dob, kdy se šetřilo pamětí; dnes se dělá ze stejného důvodu jako tehdy — **odlišit variantu, aniž bys platil za druhý asset**.

**Souvislosti:** [Pixel art do Godotu: paleta](2d-svet.md#pixel-art-do-godotu-paleta-silueta-a-jedno-nastaveni) *(proč malá paleta)* · [Data ven ze skriptu](resources.md#data-ven-ze-skriptu-skript-ridi-chovani-resource-popisuje-co-ta-vec-je) *(varianta jako data)* · [2D vizuál](../teorie/2d-vizual.md#pixel-art-je-rozhodnuti-ne-nouzove-reseni) · [Rejstřík: Palette swap](../rejstrik.md#palette-swap)

---

## Pixel art má měřítko: mixely a velikost plátna

**Zdroj:** [Game Dev Secrets: The Most Common Beginner Mistake!](https://www.youtube.com/watch?v=OQzApE2FXmI) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~1 min · + [Game Dev Secrets: It's definitely not built to scale…](https://www.youtube.com/watch?v=4_v6vw7DFus) · týž kanál · ~1 min

**Shrnutí:** Dvě strany téhož pravidla, které v pixel artu neplatí jinde: **grafiku nejde škálovat.** Z toho plyne (a) že smíchání různě velkých pixelů na obrazovce — *mixels* — vypadá vždycky špatně, a (b) že **velikost plátna určuje velikost objektu ve hře**, takže se nevolí podle toho, kolik detailu chceš, ale **podle hlavní postavy**.

### Rozpad myšlenky

**Mixely** [(0:02)](https://www.youtube.com/watch?v=OQzApE2FXmI&t=2s): scéna, kde postava, nepřítel a pozadí mají stejně velké pixely, sedí. Jakmile jednu věc **zvětšíš v enginu** — třeba abys udělal většího bosse — má najednou její pixel jinou velikost než všechno ostatní a *„míchání velikostí pixelů takhle vypadá skoro vždycky opravdu špatně"*. Doporučení je jednoznačné: **neškáluj v enginu vůbec**; zvětši sprite v kreslicím programu a **výsledek uklid**, aby velikost pixelu zůstala konstantní. Je to víc práce, protože je to nový sprite — a vypadá to nesrovnatelně líp.

**Velikost plátna** [(0:02)](https://www.youtube.com/watch?v=4_v6vw7DFus&t=2s) je tatáž věc viděná při kreslení. Autor předvede chybu, kterou dělá každý: chce **ozdobnou vázu**, takže chce hodně detailu, takže zvolí plátno **60 × 100** — a ve hře je váza *„obrovská, dvakrát větší, než jsem chtěl"*. U 2D ilustrace nebo 3D by ji zmenšil; v pixel artu **nemá jak**. Poučení je jedna věta, kterou stojí za to mít napsanou u monitoru: *„protože pixel art nejde škálovat, velikost plátna určuje velikost spritu ve hře — takže se volí relativně k hlavní postavě."* Postava má padesát pixelů, tak má váza podobné výšky plátno kolem padesáti.

**Co to znamená prakticky:** rozhodnutí o velikosti hlavní postavy je **jednotka, ve které se měří celá hra**, a mění se draho — jak je vidět na [redesignu](#redesign-postavy-rozhoduje-silueta), kde posun z 32 na 48 pixelů vynutil změnu rozlišení celé hry.

> **Pozn.:** Obě pravidla vyplývají z jediné vlastnosti média: **pixel je jednotka, ne vzorek.** V rastrové grafice je pixel technický detail, který se dá interpolovat; v pixel artu je to **záměrně umístěný prvek**, a interpolace ho zničí. Odtud plyne i [nearest filtrování](../rejstrik.md#nearest-neighbor-filtering), [integer scaling](../rejstrik.md#integer-scaling) i tahle dvě pravidla — je to pořád jedna a tatáž věc řečená na čtyřech místech. A malá výjimka pro úplnost: **zvětšení celočíselným násobkem** (2×, 3×) mixely nedělá, protože zachová mřížku — proto se dá jedna sada dlaždic použít ve dvou měřítkách, pokud jsou ta měřítka celá čísla.

**Souvislosti:** [Redesign postavy](#redesign-postavy-rozhoduje-silueta) *(kde ta velikost rozhodla o rozlišení hry)* · [Pixel art do Godotu](2d-svet.md#pixel-art-do-godotu-paleta-silueta-a-jedno-nastaveni) · [Čtyři vady pixelové kamery](pripadovka-kamera.md#ctyri-vady-pixelove-kamery-a-rozliseni-ktere-polovinu-z-nich-resi) · [Rejstřík: Mixels](../rejstrik.md#mixels) · [Rejstřík: Integer scaling](../rejstrik.md#integer-scaling) · [Rejstřík: Pixel-perfect](../rejstrik.md#pixel-perfect)

---

## Jeden zvuk, který nezevšední

**Zdroj:** [Game Dev Secrets: Sound Effect Magic!](https://www.youtube.com/watch?v=ZYZRr05AMNE) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~1 min

**Shrnutí:** Jeden zvuk máchnutí mečem přehrávaný pokaždé stejně **zleze na nervy** — a shánět tucet variant každého zvuku ve hře je nesmyslně drahé. Lék stojí jeden řádek: při každém přehrání **náhodně posuň výšku tónu** v úzkém rozmezí, autor používá **90 až 110 %**. Efekt je nepřiměřeně velký k vynaložené práci.

### Rozpad myšlenky

**Problém je kumulativní, ne okamžitý** [(0:02)](https://www.youtube.com/watch?v=ZYZRr05AMNE&t=2s), a autor to podává poctivě: jednotlivé přehrání *„není zas tak zlé — ale za celou hru to spoustě hráčů poleze na nervy."* To je vlastnost, kvůli které se takové věci špatně odhalují při testování: **v pěti minutách vývoje ti to nevadí, ve dvacáté hodině hraní ano.**

**Mechanismus** je triviální: při každém přehrání se výška tónu nastaví na náhodnou hodnotu mezi 0,9 a 1,1 násobku původní. Autorovo hodnocení výsledku sedí — *„je to mnohem míň repetitivní, i když se pořád používá jediný zvuk"*, a *„i ten nejmenší posun výšky ten problém úplně odstraní."*

**A doporučení na závěr** je to, co z triku dělá metodu: **zkombinuj posun výšky s několika variantami u nejdůležitějších zvuků.** Výsledek je *„plný a zajímavý zvukový svět bez velkého úsilí navíc"* — protože se tím variabilita násobí: tři varianty × plynulý posun výšky dá zvuk, který se v praxi nikdy neopakuje identicky.

> **Pozn.:** Za tím trikem stojí obecnější pravidlo, které se vyplatí znát mimo zvuk: **opakování se nepozná podle četnosti, ale podle přesnosti.** Deset identických zvuků vnímáš jako opakování; deset mírně odlišných jako jeden zvuk s texturou. Přesně proto se náhodně rozptylují i **částice**, **doby prodlev** a **rozmístění dekorací** — a proto v pixel artu vzniká „opakuj a rozbij opakování drobností", jak to má knihovna popsané u [instancovaného města](../praxe/env-breakdowny.md#san-francisco-11-mesto-od-jednoho-cloveka). Hudební stránku toho tématu (a proč zrovna ±10 %) rozvíjí sekce [Hudba a zvuk](../hudba/sound-design-ve-hre.md).

**Souvislosti:** [Sound design ve hře](../hudba/sound-design-ve-hre.md) *(zvuk jako cue, feedback a emoce)* · [Katalog juice](../teorie/game-feel.md#katalog-juice-deset-detailu-ktere-prodavaji-tutez-mechaniku) · [Breakdowny: San Francisco](../praxe/env-breakdowny.md#san-francisco-11-mesto-od-jednoho-cloveka) *(opakování rozbité drobností)* · [Rejstřík: Random pitch variation](../rejstrik.md#random-pitch-variation)
