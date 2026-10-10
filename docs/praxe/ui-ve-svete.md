# UI ve světě: menu v televizi a health bary nad hlavou

První kapitola tématu **UI a rozhraní** a zatím jen jeho okraj: rozhraní, které žije ve 3D světě. Menu na obrazovce televize uprostřed scény, ukazatele zdraví nad nepřáteli i nad jejich končetinami, a cena, kterou za stovky takových widgetů platí výkon. Společné mají jednu komponentu, [Widget Component](../rejstrik.md#widget-component), a otázku, ve kterém prostoru se widget kreslí. Jádro [UMG](../rejstrik.md#umg) — layout, Common UI, navigaci gamepadem a fokus — knihovna zatím nemá, protože k němu chybí zdroje. Proč na ukazatelích záleží pro pocit z boje, vysvětluje [souboj](souboj.md#rana-ktere-hrac-uveri-pet-potvrzeni-kazde-o-necem-jinem).

---

## Menu jako předmět ve scéně: widget na televizi a virtuální myš

**Zdroj:** [Interactive Horror Menu in Unreal Engine 5](https://www.youtube.com/watch?v=CDf-5lp4yxQ) · [Houman Creates](https://www.youtube.com/channel/UCB1r8NTUASWOScq7CLjJ32Q) · ~13 min, tutoriál

**Shrnutí:** Hlavní menu nemusí ležet přes obrazovku. Tady je to UMG widget na obrazovce staré televize v temném pokoji, se šumem a s klikáním myší. Drží to pohromadě dva díly: **Widget Component** promítne widget na plochu ve světě a **Widget Interaction Component** funguje jako virtuální myš, která do něj střílí paprsek a posílá mu najetí a klik. Háček: paprsek se zastaví o první kolizi, takže dokud má kolizi televize, na tlačítka se kliknout nedá.

### Rozpad myšlenky

**Televize jako aktér.** Model televize je v blueprintu jako mesh a obrazovka je zvláštní plocha přes něj [(1:41)](https://www.youtube.com/watch?v=CDf-5lp4yxQ&t=101s), [(2:29)](https://www.youtube.com/watch?v=CDf-5lp4yxQ&t=149s). Při importu modelu autor zaškrtne Combine Static Meshes a vypne Nanite [(0:49)](https://www.youtube.com/watch?v=CDf-5lp4yxQ&t=49s). Šum na obrazovce je materiál. Šumovou texturu posouvá panner a otáčí rotator, výsledek se zaokrouhlí, vynásobí parametrem síly a jde do emise na černém základu [(3:16)](https://www.youtube.com/watch?v=CDf-5lp4yxQ&t=196s), [(4:07)](https://www.youtube.com/watch?v=CDf-5lp4yxQ&t=247s).

**Widget na ploše.** Menu je obyčejný widget blueprint: canvas a v něm vertikální box ukotvený na střed s alignmentem 0,5. V boxu jsou tři tlačítka s průhledným pozadím a vlastním fontem [(4:07)](https://www.youtube.com/watch?v=CDf-5lp4yxQ&t=247s), [(4:54)](https://www.youtube.com/watch?v=CDf-5lp4yxQ&t=294s), [(5:40)](https://www.youtube.com/watch?v=CDf-5lp4yxQ&t=340s). Na televizi ho nese Widget Component. Když je obsah oříznutý, spraví to `Draw at Desired Size` [(5:40)](https://www.youtube.com/watch?v=CDf-5lp4yxQ&t=340s).

**Virtuální myš.** Aby šlo do widgetu ve 3D klikat, musí engine trasovat od kurzoru k widgetu. To dělá Widget Interaction Component, paprsek, který widgetu posílá události myši [(6:32)](https://www.youtube.com/watch?v=CDf-5lp4yxQ&t=392s). Komponentu nese pawn, který se na televizi dívá. Má `Auto Possess` nastavené na hráče 0 a je natočený na televizi; na komponentě je Interaction Source = Mouse a zapnutý debug [(7:18)](https://www.youtube.com/watch?v=CDf-5lp4yxQ&t=438s), [(7:44)](https://www.youtube.com/watch?v=CDf-5lp4yxQ&t=464s). Level blueprint přepne input mode na Game and UI a ukáže kurzor [(8:30)](https://www.youtube.com/watch?v=CDf-5lp4yxQ&t=510s).

**Dvě věci, na které se zapomene.**
- Debugová tečka se na tlačítkách neukáže, protože paprsek trefí kolizi televize dřív než widget. Musí se vypnout kolize obrazovky i televize [(8:47)](https://www.youtube.com/watch?v=CDf-5lp4yxQ&t=527s), [(9:17)](https://www.youtube.com/watch?v=CDf-5lp4yxQ&t=557s).
- Kliknutí se do komponenty musí předat ručně: levé tlačítko myši → `Press Pointer Key` a `Release Pointer Key`. Teprve pak tlačítka reagují [(9:51)](https://www.youtube.com/watch?v=CDf-5lp4yxQ&t=591s).

**Scéna kolem.** Pokoj je z kostek, se stolem, postelí a komodou [(10:39)](https://www.youtube.com/watch?v=CDf-5lp4yxQ&t=639s). Světla ze scény autor odstraní a jediné obdélníkové světlo dá do blueprintu televize; post-process sníží expozici [(12:15)](https://www.youtube.com/watch?v=CDf-5lp4yxQ&t=735s), [(12:47)](https://www.youtube.com/watch?v=CDf-5lp4yxQ&t=767s). Místnost tak osvětluje jen televize.

> **Pozn.:** Menu, které je předmětem v herním světě, je diegetic UI. Video ten pojem nepoužívá, ale staví učebnicový příklad. Výhodou je [imerze](../teorie/game-feel.md#imerze-svet-ktery-na-tebe-odpovida): hra začíná už v menu a [horor](../teorie/horor-design.md#zvuk-tma-a-prostredi-atmosfera-jako-system) tím získá první minutu atmosféry. Cenou je ovládání. Tohle menu umí jen myš, protože gamepad a klávesnice potřebují fokus a navigaci, které video neřeší a které v knihovně zatím chybějí.

**Souvislosti:** [Rejstřík: Widget Component](../rejstrik.md#widget-component) · [Rejstřík: Widget Interaction Component](../rejstrik.md#widget-interaction-component) · [Rejstřík: Diegetic UI](../rejstrik.md#diegetic-ui) · [Rejstřík: Widget Blueprint](../rejstrik.md#widget-blueprint) · [Rejstřík: Anchor (UI)](../rejstrik.md#anchor-ui)

---

## Health bar nad hlavou: screen space, ukazatel z materiálu a dojezd poškození

**Zdroj:** [How to Make a Combat System in UE5](https://www.youtube.com/watch?v=4omEu9N9WIE) · [Evans Bohl](https://www.youtube.com/channel/UC36uolRnnwoMMH27vzecLBg) · ~3 h 49 min, tutoriál (úsek o health baru) ·
[Limb Health + Breakable Limbs in Unreal Engine 5](https://www.youtube.com/watch?v=Mv1LGtQRVls) · [Tank Control Games](https://www.youtube.com/channel/UCoHLpKMSi5LlOMFlxuoR1rA) · ~22 min, tutoriál (UE 5.7) ·
[5 Ways to Improve Game Feel In Unreal Engine](https://www.youtube.com/watch?v=78MBe46IBrQ) · [Unreal University](https://www.youtube.com/channel/UCQv4mwerZLQVe3wPbsMc-qw) · ~9 min, přehled technik

**Shrnutí:** Ukazatel zdraví nad nepřítelem je widget na Widget Componentě ve **screen space**. Kreslí se vždy čelem ke kameře a v pevné velikosti na obrazovce. Zdroje k němu dojdou různými cestami: ukazatel z materiálu se dvěma parametry, obyčejný Progress Bar a ukazatel, který skočí na zasaženou končetinu. Háček je ve druhém, pomalejším pruhu. Dojíždějící červená ukáže, **kolik ubrala poslední rána**, a právě tahle informace dělá z ukazatele zpětnou vazbu, ne jen stav.

### Rozpad myšlenky

**Kde visí.** Evans ukazatel nejdřív zkusí jako Widget Component přímo v postavě. Space = Screen zajistí, že se vždy dívá do kamery, a velikost je 80 × 10 [(2:19:28)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=8368s), [(2:20:15)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=8415s). Pak ho přestěhuje do zdravotní komponenty. Ta widget vytvoří a postavě přidá Widget Component přes `Add Component by Class`, 30 jednotek nad vrchem kapsle (polovina její výšky + 30). Nastaví mu screen space, widget i velikost [(2:21:01)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=8461s), [(2:21:48)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=8508s), [(2:23:22)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=8602s). Offset i velikost jsou parametry komponenty; u jiné postavy Evans offset zvedne na 50 [(3:47:44)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=13664s).

**Ukazatel z materiálu.** Materiál je v doméně User Interface a translucentní [(2:13:11)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=7991s). Staví se takto:
1. Texture coordinate s maskou na kanál R dá vodorovný gradient od 0 do 1 [(2:13:57)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=8037s).
2. `Step` s parametrem Fill Level z gradientu udělá ostrou hranu [(2:14:43)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=8083s).
3. Lerp mezi šedou a zelenou z hrany udělá barvy [(2:16:17)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=8177s).
4. Druhý step s parametrem Hit Level a červenou barvou přidá pruh poškození [(2:17:51)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=8271s).

Widget je pak jen obrázek s tímhle materiálem [(2:18:38)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=8318s). V Event Construct si vezme dynamický materiál a parametry nastavují dvě události; jména parametrů musí sedět přesně [(2:24:54)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=8694s), [(2:25:42)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=8742s). Hodnota je **aktuální zdraví / maximum**, tedy číslo normalizované na 0–1, a po smrti se ukazatel skryje [(2:27:14)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=8834s), [(2:28:02)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=8882s).

**Dojezd poškození.** Hit Level každý snímek dohání Fill Level přes `FInterp To` s rychlostí 5 [(2:28:48)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=8928s), [(2:29:34)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=8974s). Zelená tak spadne hned a červená dojede za ní. Unreal University dělá totéž bílým pruhem, který klesá pomalu, aby bylo vidět, kolik zásah ubral [(6:59)](https://www.youtube.com/watch?v=78MBe46IBrQ&t=419s), [(7:46)](https://www.youtube.com/watch?v=78MBe46IBrQ&t=466s). Jak tenhle tick neplatit u každého nepřítele, řeší [další myšlenka](#sto-health-baru-logika-na-ticku-a-prekresleni-jsou-dve-ruzne-ceny).

**Progress Bar a ukazatel na končetině.** Tank Control Games skládá ukazatel z UMG prvků: overlay, border se zaobleným obrysem a Progress Bar, jehož procento nastavuje jedna událost [(3:54)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=234s), [(4:41)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=281s), [(7:00)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=420s). Widget Component na nepříteli je ve screen space, má velikost 100 × 25 a **ve výchozím stavu je skrytý** [(14:00)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=840s). Při zásahu se zobrazí a `Set World Location` ho přesune na socket kosti zasažené končetiny, takže ukazatel skáče tam, kam hráč střílí [(14:46)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=886s), [(15:32)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=932s). Procento je opět aktuální zdraví / maximum [(16:20)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=980s) a po zlomení končetiny ukazatel zmizí [(17:53)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=1073s).

> **Pozn.:** Materiálová cesta je pracnější, ale dá dva pruhy v jednom obrázku a vzhled celý v rukou shaderu. Progress Bar se postaví rychleji a styl se nastavuje v Details. Obě řešení mají společný základ: ukazatel dostává normalizované číslo, ne body zdraví. Je to stejný princip jako u [normalizovaných křivek v montáži](interakcni-animace.md#animace-ridi-svet-normalizovane-krivky-v-montazi). Kdo staví ukazatel jen pro nepřítele, kterého zrovna trefil, může od Tank Control Games převzít i skrytí ve výchozím stavu. Ukazatel, který není vidět, nezaclání ve scéně a hráči nic nehlásí, dokud nemá co.

**Souvislosti:** [Rejstřík: Widget Component](../rejstrik.md#widget-component) · [Rejstřík: Dynamic Material Instance](../rejstrik.md#dynamic-material-instance) · [Rejstřík: HUD](../rejstrik.md#hud) · [Terč: směr rány, zdraví a smrt](souboj.md#terc-smer-rany-zdravi-a-smrt-bez-radku-v-postave) · [Zdraví po končetinách](souboj.md#zdravi-po-koncetinach-physical-material-jako-adresa-struct-jako-stav)

---

## Sto health barů: logika na ticku a překreslení jsou dvě různé ceny

**Zdroj:** [How I Optimized My Game to Over 200 FPS in UE5](https://www.youtube.com/watch?v=xr-2TrMUd9w) · [Procedural Minds](https://www.youtube.com/channel/UCkfvcZJ6dGNUSCWOCVQnkXw) · ~23 min, devlog (úsek o in-world widgetech) ·
[How to Make a Combat System in UE5](https://www.youtube.com/watch?v=4omEu9N9WIE) · [Evans Bohl](https://www.youtube.com/channel/UC36uolRnnwoMMH27vzecLBg) · ~3 h 49 min, tutoriál (úsek o optimalizaci ukazatele)

**Shrnutí:** Ukazatel nad hlavou stojí dvakrát. Jednou za **logiku**, která ho každý snímek aktualizuje, podruhé za **překreslení** widgetu, které se ve výchozím stavu děje každý snímek u každého nepřítele. Evans šetří první cenu: dojezd poškození se k ticku přihlásí jen na dobu, kdy se pruh hýbe. Procedural Minds šetří druhou: s `Redraw Time` 0,1 s se ukazatel překreslí nanejvýš desetkrát za sekundu. Háček: vypnout widget komponentě tick vypadá jako nejjednodušší řešení, ale autorovi se pak ukazatele přestaly kreslit úplně.

### Rozpad myšlenky

**Cena v profileru.** Každý nepřítel s ukazatelem má v profilu vlastní položku vykreslení widgetu, řádově setiny milisekundy, a dohromady to dělá znatelnou část snímku [(10:59)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=659s), [(11:45)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=705s). U hry, která běží na 150–200 FPS, je aktualizace v každém snímku zbytečná, protože hodnota se mění jen při zásahu [(12:32)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=752s).

**Proč ne vypnout tick.** S vypnutým tickem se autorovi ukazatele přestaly aktualizovat i kreslit. Nepomohlo ani tick zapnout jen kvůli změně hodnoty a pak ho zase vypnout [(11:45)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=705s), [(12:32)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=752s). Při natáčení videa to najednou fungovalo. Autor to přičítá tomu, že nepřátelé teď vznikají přes actor pooling, a před ním se ukazatele s vypnutým tickem neobjevily [(13:19)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=799s). Komu vypnutý tick funguje, může ho použít. Komu ne, ten má náhradu.

**Redraw Time.** Na Widget Componentě je v sekci User Interface čas mezi dvěma překresleními: 0 znamená každý snímek, 1 jednou za sekundu [(13:19)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=799s), [(14:06)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=846s). Je to strop, ne interval: hodnota 0,1 znamená nanejvýš desetkrát za sekundu, nic se neopakuje častěji [(15:40)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=940s). Nastavit jde i uzlem `Set Redraw Time`. V autorově měření spadla souhrnná položka zhruba z 0,46 na 0,09–0,1 ms [(14:53)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=893s). Pro zdraví je deset překreslení za sekundu dost, aby hráč na nic nečekal. Kompetitivní hra by podle autora možná chtěla víc, třeba 0,05 [(14:53)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=893s), [(15:40)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=940s).

**Logika jen po dobu pohybu.** Evansův dojezd poškození, tedy `FInterp To` v ticku widgetu, by běžel každý snímek i u nepřátel, kteří žádnou ránu nedostávají. Při mnoha postavách je to vážná režie [(2:31:07)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=9067s). Tick proto jen zavolá event dispatcher. Evans ho přirovnává k newsletteru: když ho nikdo neodebírá, rozeslat ho nestojí skoro nic [(2:31:55)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=9115s), [(2:32:41)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=9161s). Dojezd se k dispatcheru přihlásí, když se změní zdraví, a odhlásí se, jakmile červená dožene zelenou [(2:33:31)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=9211s), [(2:34:19)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=9259s), [(2:35:05)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=9305s).

> **Pozn.:** Obě páky míří jinam a dají se kombinovat. Evansův trik šetří práci Blueprintu v ticku, ale tick widgetu i jeho kreslení běží dál. Redraw Time podle videa šetří překreslování. Která cena u tebe převažuje, řekne až [profiler](profiling.md#rozhodovaci-strom-stat-unit-rekne-kterym-nastrojem-pokracovat). Do téže rodiny patří [UMG bindings](rozpocet-snimku.md#prvnich-1666-ms-se-rozdava-v-cl1), které se spouštějí každý snímek a které Epic radí v projektu rovnou zakázat. Celá optimalizace hry, ze které čísla pocházejí, je ve [Ze 100 na 200 FPS](lehky-render.md#ze-100-na-200-fps-co-stalo-za-vypnuti-ve-skutecne-hre).

**Souvislosti:** [Rejstřík: Widget Component](../rejstrik.md#widget-component) · [Rejstřík: Event dispatcher](../rejstrik.md#event-dispatcher) · [Rejstřík: Event Tick](../rejstrik.md#event-tick) · [Observer pattern](komunikace-blueprintu.md#observer-pattern-nejcastejsi-chyba-zacatecniku-a-jeji-oprava) *(přihlášení a odhlášení jako vzor)*
