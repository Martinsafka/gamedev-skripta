# GDD review: co dokument slibuje a technika nedoručuje

**Kontext:** GDD IZBY (v2.0) prošlo v létě 2026 prvním důkladným review. V tom nejdůležitějším koncept obstál — jeden nápad dotažený do všech systémů: Dunning-Krugerova křivka není „inspirace", je to doslovný level design (propad podlahy = pád z Mount Stupid, podzemí = údolí zoufalství, útěk = nabytá kompetence) a říkanka je jediný diegetický quest log. Hodnota konceptu neleží v žánrové slupce slovanského hororu, ale v alegorické vrstvě pod ním — a dokument to drží bez feature creepu. Review přesto přineslo tři nálezy, každý jiný druh téže chyby.

## Co se stalo

**Nález 1: čísla bez zdroje.** Celá herní tenze stojí na přesných oddělených rychlostech (Crouch 150 / Walk 250 / Run 400 / Sprint 650) a stamina matematice nad nimi. Jenže audit komponenty odhalil, že funkce aplikující hodnoty z profilů nemá žádné call sites — **čísla rychlostí v dokumentu jsou přání, ne to, co engine produkuje**, dokud bug není opravený. Přenositelná lekce je větší než ten bug: když design dokument staví na vlastní technologii, komponenta a hra nejsou dva projekty — hotfixy komponenty hru *gatují* a roadmapa technologie patří do závislostí dokumentu explicitně. Jinak vzniká GDD, které slibuje chování, jež nemá kde vzniknout.

**Nález 2: jedna veličina, dvě jednotky.** Hluk je v dokumentu definovaný dvakrát a pokaždé jinak: jedna kapitola ho měří jako poloměr slyšitelnosti v units (Walk na hlíně = 400), jiná spouští AI Investigate na „Noise Event větší než 50" — hodnota z jiné soustavy, která na tabulku poloměrů nijak nesedí. **Každá veličina musí mít právě jednu definici a jednotku.** Dvě definice = dva subsystémy, které si nerozumí, a integrace to zjistí až za běhu. U sólo projektu je to rozpor mezi vlastní kapitolou 4 a 6; v týmu by to byli dva lidé implementující dva neslučitelné systémy v dobré víře.

**Nález 3: spočítaná, ne doufaná.** Přepočet rychlostí ukázal, že hráč na hrubou rychlost strukturálně ztrácí — finále úniku stojí celé na počáteční vzdálenosti a na asymetrii překážek (hráč proleze, AI obchází). To není bug, to je nepojmenovaný designový fakt: **fantazie „těsně unikneš" musí být spočítaná, ne doufaná.** Starting gap a obstacle asymmetry tím přestávají být detaily prostředí — jsou to tuning parametry hry a patří do GDD jako čísla s vlastníkem, jinak je finále náhoda.

K tomu drobnější nálezy téže kategorie, hygiena dokumentu: nekonzistentní odkazy na verzi enginu, zavádějící označení „permadeath", rozbitý cross-reference. Reakce „technická sekce se reviduje až po prototypu" je legitimní priorita — **pokud je to rozhodnutí zapsané v dokumentu, ne tichý stav.** A kontext, který z nálezů dělá kritickou cestu místo kosmetiky: tvrdý termín vydání na podzim 2026, na který je vázaná i roadmapa komponenty.

## Co si z toho beru

- **GDD review nehledá překlepy — hledá místa, kde dokument slibuje něco, co technika nedoručuje:** čísla bez zdroje v enginu, veličiny bez jednotné definice, závislosti bez vlastníka. Koncept může být výborný a dokument přesto neproveditelný; review odděluje tyhle dvě roviny.
- Rychlý autotest na vlastní dokument: **u každého čísla se zeptej, kde vzniká** — asset, funkce, tabulka, tedy adresa v enginu. Číslo bez adresy je přání.
- **Veličiny drž v jedné tabulce s jednotkou v hlavičce.** Próza je místo, kde se definice rozlézají.

> **Pozn.:** Na třídu problémů „jedna veličina, dvě definice" existuje i nástrojová odpověď: když logika mluví jedním slovníkem, dá se z dokumentu vygenerovat graf „kdo zapisuje, kdo čte" — dokument, který se umí sám zauditovat (viz [devlog jako mapa](devlog-jako-mapa.md)). GDD v próze tohle neumí, o důvod víc mu pomáhat strukturou.

**Souvislosti:** [Dokumentace jako audit](dokumentace-jako-audit.md) *(bug s nulou call sites technicky; tady jeho designový dopad)* · [Derivační řetěz IZBY](derivace-izby.md) *(koncept, který review četlo — a proč drží pohromadě)* · [Cut line](cut-line.md) *(navazující krok: slice, který sliby dokumentu ověří v buildu)* · [Nářadí, ne archiv](naradi-ne-archiv.md) *(audit jako opakovaná událost, ne jednorázovka)* · [Rejstřík: Game Design Document](../rejstrik.md#game-design-document) · [Rejstřík: vertical slice](../rejstrik.md#vertical-slice)
