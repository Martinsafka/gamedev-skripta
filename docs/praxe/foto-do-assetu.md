# Z fotky herní asset: obtahování v Blenderu

Nejlevnější zdroj detailu, jaký existuje, je fotoaparát v kapse. Tahle kapitola ukazuje pipeline, která z jediné fotky udělá nízkopolygonový model s hotovými UV: **narovnat obrázek ve 2D, obtáhnout ho plochou, promítnout texturu z pohledu kamery a pak mu dodat hloubku, aniž bys potřeboval druhou texturu.** Výsledek je levný na výkon, vypadá překvapivě dobře a — což je nejdůležitější — zůstane dál editovatelný.

Sousední kapitola [PS1 estetika](ps1-estetika.md) řeší opačný extrém téhož řemesla: co dělat, když chceš, aby textura vypadala *hůř*.

---

## Narovnat, obtáhnout, promítnout

**Zdroj:** [Turn Any Photo into a Game Asset (Fast & Easy Blender Tutorial)](https://www.youtube.com/watch?v=ZR_X2OhsteQ) · [Grant Abbitt (Gabbitt)](https://www.youtube.com/channel/UCZFUrFoqvqlN8seaAeEwjlw) · ~22 min, tutoriál

**Shrnutí:** Celý postup stojí na jednom uzlu — **Project from View** — který na model promítne přesně ten obrázek, který máš na pozadí. Jenže aby projekce sedla, musí být fotka **plochá**, a to žádná fotka není. První polovina práce se proto odehrává v obrázkovém editoru, ne v Blenderu. Autor to demonstruje na záměrně mizerné fotce fasády focené z bazénu: *„budova je sama o sobě křivá a obrázek je dost špatný, protože je v něm hodně perspektivy a zkreslení objektivu."*

### Rozpad myšlenky

**Narovnání ve 2D** [(0:01)](https://www.youtube.com/watch?v=ZR_X2OhsteQ&t=1s): Edit → Transform → **Warp** a fotka se ručně tahá do pravoúhlosti. Trik, který z toho dělá řemeslo místo hádání [(0:48)](https://www.youtube.com/watch?v=ZR_X2OhsteQ&t=48s): **stáhnout si vodítka** k horním hranám oken a k boční hraně, aby bylo vidět, kde mají rovné linie skutečně být. Laťka je přitom rozumná — *„nemusí to být úplně dokonalé"*. Tenhle krok jde udělat i v bezplatných editorech; podstatný je princip, ne program.

**Import jako podklad** [(1:35)](https://www.youtube.com/watch?v=ZR_X2OhsteQ&t=95s): obrázek se **přetáhne přímo do viewportu** a přijde jako *empty*. Pak `Alt+G` a `Alt+R` (vynulovat posun a rotaci), `R X 90` (postavit), čelní pohled a zarovnat spodek budovy na osu. Odteď je to kreslicí podklad.

**Obtažení** [(1:35)](https://www.youtube.com/watch?v=ZR_X2OhsteQ&t=95s): plane otočený do svislé polohy, edit mode, box select vrcholů a `G Z` / `G X` na rozměr fasády. Praktická drobnost, která šetří nervy: **přepnout do wireframe zobrazení**, jinak nevidíš, co je za plochou.

**Dělení stěny podle otvorů** [(3:08)](https://www.youtube.com/watch?v=ZR_X2OhsteQ&t=188s): `Ctrl+R` klade **loop cuty** podle oken a dveří — první klik určí směr, druhý polohu. Zásadní je pořadí práce: **nejdřív naházej řezy zhruba, přesnou polohu dolaď až potom** pomocí `G X` a `G Z`. Kde by loop cut vyrobil zbytečné vrcholy přes celý model, použije se místo něj **knife tool (`K`)**, který snapuje na existující vrcholy a hrany [(4:40)](https://www.youtube.com/watch?v=ZR_X2OhsteQ&t=280s). Vznikne tím n-gon — a autor rovnou uklidňuje: *„n-gony jsou naprosto v pořádku, pokud jsou na ploché ploše."*

**Materiál dřív než UV** [(6:14)](https://www.youtube.com/watch?v=ZR_X2OhsteQ&t=374s): nový materiál, `Shift+A` → Texture → **Image Texture**, napojit Color na Base Color. A past, na kterou lidé narazí pokaždé [(7:00)](https://www.youtube.com/watch?v=ZR_X2OhsteQ&t=420s): dokud je viewport v **Solid** režimu, nic neuvidíš — texturu ukáže až **Material Preview**.

**A teď ten jediný uzel, o který jde** [(7:46)](https://www.youtube.com/watch?v=ZR_X2OhsteQ&t=466s): edit mode, `A` (vybrat vše), čelní pohled, `U` → **Project from View**. Autor to zdůvodní jednou větou, která vysvětluje celý postup: *„protože chceme přesně zkopírovat pohled, který máme na pozadí."* UV pak už jen naškálovat a posunout tak, aby se model překryl s podkladem — a **na to existuje pěkný trik** [(8:33)](https://www.youtube.com/watch?v=ZR_X2OhsteQ&t=513s): `Shift+pravý klik` postaví 2D kurzor do rohu a přepnutím pivotu na kurzor se dá škálovat přesně od něj. Když se model s podkladem kryje k nerozeznání, **empty se schová** a je hotovo.

> **Pozn.:** Metoda má jasnou hranici použitelnosti a stojí za to ji pojmenovat rovnou: funguje na **ploché věci fotografované zpředu** — fasády, dveře, cedule, vývěsní štíty, průmyslová zařízení. Čím víc má objekt hloubky a čím míň je fotka kolmá, tím víc práce padne na narovnávání a tím hůř drží projekce. U hry s vedeným pohledem je to levná cesta k **rekvizitám a stavbám na pozadí**; hrdinské assety, na které si hráč sáhne, si zaslouží model. Právní drobnost: fotky musí být tvoje nebo licenčně čisté — a u budov v některých zemích platí omezení i na fotografování architektury.

**Souvislosti:** [Hloubka bez druhé textury](#hloubka-bez-druhe-textury) *(pokračování téhož modelu)* · [PS1 estetika: textura dělá styl](ps1-estetika.md#textura-dela-styl-rozliseni-kontrast-a-nearest) · [Breakdowny: trim sheety](env-breakdowny.md#tlou-trim-sheet-ktery-nahradil-tisice-bake) *(druhý způsob, jak z málo textury udělat hodně povrchu)* · [Materiály: master material](materialy.md#master-material-pet-textur-nema-mit-kazdy-mesh) · [Rejstřík: UV mapping](../rejstrik.md#uv-mapping) · [Rejstřík: n-gon](../rejstrik.md#n-gon)

---

## Hloubka bez druhé textury

**Zdroj:** [Turn Any Photo into a Game Asset (Fast & Easy Blender Tutorial)](https://www.youtube.com/watch?v=ZR_X2OhsteQ) · [Grant Abbitt (Gabbitt)](https://www.youtube.com/channel/UCZFUrFoqvqlN8seaAeEwjlw) · druhá polovina tutoriálu

**Shrnutí:** Jakmile plochou fasádu vytáhneš do prostoru, objeví se problém, který zabíjí většinu pokusů o tenhle postup: **boční stěny oken a dveří vypadají jako rozmazané pruhy.** Řešení není další textura, ale **rozbalit ty plochy zvlášť a posadit je na jiné, vizuálně podobné místo téže fotky**. Je to hezký příklad úvahy, která platí i mimo Blender: **UV nejsou popis skutečnosti, ale výběr z toho, co v textuře máš.**

### Rozpad myšlenky

**Vytažení hloubky** [(9:19)](https://www.youtube.com/watch?v=ZR_X2OhsteQ&t=559s): face mode, vybrat okna a dveře, `E` a zatlačit dovnitř. Prostřední dveře extrudovat zvlášť a míň — hloubka nemá být uniformní. Spodní plochy otvorů se rovnou smažou, protože přijde vlastní podlaha. Celá fasáda se pak v edge mode odsadí dozadu (`Alt+klik` na obvodovou hranu, `E` a `Y`), takže vznikne kvádr místo desky.

**Proč jsou boky rozmazané**, vysvětleno přesně [(10:06)](https://www.youtube.com/watch?v=ZR_X2OhsteQ&t=606s): *„ta natažená textura vzniká tím, že se bere tenhle jediný pixel a natahuje se dozadu. Ty plochy jsou rozbalené, ale jsou namačkané do jediného pixelu."* Extruze totiž zdědí UV z hrany, ze které vznikla — a hrana je v UV prostoru **čára bez plochy**.

**Oprava** [(10:52)](https://www.youtube.com/watch?v=ZR_X2OhsteQ&t=652s): vybrat plochu → `U` → **Unwrap Angle Based** → a v UV editoru ji **naškálovat a přesunout na část textury, která vypadá jako to, co ta plocha má představovat**. Ostění okna dostane kus zdi, špaleta dveří kus tmavého dřeva. Občas je potřeba plochu otočit — autor jednu pozná jako převrácenou podle svítidla, které se objevilo nahoře [(12:24)](https://www.youtube.com/watch?v=ZR_X2OhsteQ&t=744s).

**Past, která tě u úklidu zdrží** [(13:10)](https://www.youtube.com/watch?v=ZR_X2OhsteQ&t=790s): když se v UV pokusíš posunout jediný vrchol, hne se i jeho protějšek, protože **sticky selection je propojuje**. Řešení je přepnout ji na **Disabled** a vybírat box selectem [(13:57)](https://www.youtube.com/watch?v=ZR_X2OhsteQ&t=837s) — pak jde vyčistit i ošklivá čára na hraně.

**Kde metoda skřípe — a autor to přizná** [(14:43)](https://www.youtube.com/watch?v=ZR_X2OhsteQ&t=883s): velké boční stěny budovy nemají v textuře odpovídající protějšek. Autor zkouší různá místa, otáčí o 180°, převrací zrcadlově (`S X -1`) a **vědomě hledá oblasti, které vypadají odlišně**, aby výsledek nepůsobil repetitivně — a průběžně komentuje *„není to skvělé"* a *„sotva to prochází"*. Je to poctivější než většina tutoriálů: **tahle část není postup, ale kompromis, který se hledá okem.**

**Co je levnější domodelovat** [(17:02)](https://www.youtube.com/watch?v=ZR_X2OhsteQ&t=1022s): římsa nahoře je prostá krychle, podlaha plane, ale **trubka na fasádě si zaslouží skutečnou geometrii** — bezier křivka, zploštěná (`S Y 0`), doplněná o body přes `subdivide` a zhmotněná posuvníkem **Geometry → Depth**. Materiál dostane barvu **vybranou kapátkem přímo z fotky** a mírně ztmavenou [(18:35)](https://www.youtube.com/watch?v=ZR_X2OhsteQ&t=1115s). Kritérium je jednoduché: **co vyčnívá ze stěny a vrhá stín, to domodeluj; co je plochý detail, to nech na textuře.**

**Trik na závěr, který funguje i v enginu** [(20:09)](https://www.youtube.com/watch?v=ZR_X2OhsteQ&t=1209s): mezi texturu a Base Color se vloží **Ambient Occlusion uzel smíchaný přes Mix Color v režimu Multiply s faktorem 1**. Fotka sama žádné stínění v rozích nemá, tohle jí ho dodá — a rozdíl je okamžitě vidět. Uzly se dají zkopírovat na další materiály (`Ctrl+C` / `Ctrl+V`).

**Skutečná odměna přijde nakonec** [(20:55)](https://www.youtube.com/watch?v=ZR_X2OhsteQ&t=1255s): protože je to obyčejná geometrie s hotovými UV, dá se pár loop cuty **celý dům rozhýbat do křivého tvaru** — a textura drží. *„Je toho spousta, co s tím teď můžeš dělat, když jsou textury na svém místě."* To je rozdíl mezi fotkou nalepenou na kvádr a skutečným assetem: **jedno je hotové, druhé je materiál k další práci.**

> **Pozn.:** Postup končí renderem v Eevee se zapnutým ray tracingem s poznámkou, *„že to bude fungovat i v herních enginech"* — s jednou výhradou, kterou autor zmiňuje mimochodem: **ambient occlusion se v enginu bude muset doladit.** V UE bys tenhle uzel nahradil buď zapečeným AO v textuře, nebo screen-space AO ve scéně; princip „fotka nemá vlastní stínění, dodej ho" ale zůstává. A pro nás z toho plyne obecnější pravidlo, které se hodí i mimo tuhle metodu: **fotografická textura přináší barvu a detail, ale ne hloubku — tu do ní musíš vždycky vrátit** ať už geometrií, normal mapou, nebo právě AO.

**Souvislosti:** [Narovnat, obtáhnout, promítnout](#narovnat-obtahnout-promitnout) *(první polovina postupu)* · [Breakdowny: Naughty Dog](env-breakdowny.md#naughty-dog-shadery-misto-polygonu-a-nastroj-misto-modelovani) *(profesionální verze téhož kompromisu geometrie vs. textura)* · [Optimalizace: Nanite, nebo LODy?](optimalizace.md#nanite-nebo-lody) · [Materiály: master material](materialy.md#master-material-pet-textur-nema-mit-kazdy-mesh) · [Rejstřík: ambient occlusion](../rejstrik.md#ambient-occlusion) · [Rejstřík: UV mapping](../rejstrik.md#uv-mapping)
