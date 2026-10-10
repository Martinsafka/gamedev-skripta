# Resource: data mimo kód

`Resource` je v Godotu všechno, co má vlastní soubor a dá se načíst — textura, zvuk, font, materiál. Zajímavé začne být ve chvíli, kdy si **vyrobíš vlastní typ**: soubor, ve kterém bydlí statistiky nepřítele, definice zbraně nebo obsah jednoho levelu. Kapitola vysvětluje, proč se to vyplatí (a kdy ne), ukazuje past, na kterou doplatí každý, kdo si nepřečte jednu větu v dokumentaci, a uzavírá se rozhodovacím pravidlem mezi resourcem a slovníkem.

Navazuje na [kompozici](kompozice.md): komponenty rozdělují **chování**, resources rozdělují **data**. Teprve dohromady dávají hru, která se dá balancovat, aniž bys otevřel skript.

---

## Data ven ze skriptu: skript řídí chování, resource popisuje, co ta věc je

**Zdroj:** [Stop Copying Code! Learn Custom Resources in Godot 4](https://www.youtube.com/watch?v=7dzrc7pEAwE) · [DeeRaghooGames](https://www.youtube.com/channel/UC-KLgU0nzoCCEU6W16CS3vQ) · ~14 min, tutoriál · + [Godot 4.6 Tips: 7 Features I Wish I Used Sooner](https://www.youtube.com/watch?v=z-9AI9ZPiLM) · týž kanál · ~13 min, tipy

**Shrnutí:** Máš goblina, kostlivce a obra a každý má život, rychlost a poškození uvnitř svého skriptu. Balancování pak znamená **otevřít každý skript zvlášť** a ručně přepsat čísla. Custom resource ty hodnoty vytáhne do samostatného souboru a nechá skript dělat jen to, co umí — chování. Pravidlo, které si z toho vezmi doslova: **resource popisuje, *co ta věc je*; skript řídí, *co ta věc dělá*.**

### Rozpad myšlenky

**Kontext problému** je nenápadný, protože se objeví až s velikostí [(0:39)](https://www.youtube.com/watch?v=7dzrc7pEAwE&t=39s). U tří nepřátel je čtení hodnot ze skriptu naprosto v pořádku — autor to sám zdůrazňuje. Bolet to začne u deseti, dvaceti, padesáti typů, kdy „nepřátelé dávají moc damage" znamená projít padesát souborů. Diagnóza je čistá [(2:42)](https://www.youtube.com/watch?v=7dzrc7pEAwE&t=162s): **skript má být zodpovědný za to, co věc dělá** — pohyb, útok, příjem zásahu, AI. **Hodnoty, které tu věc definují, jsou data**, a data nemají v kódu co dělat.

**Mechanismus** má tři kroky [(4:46)](https://www.youtube.com/watch?v=7dzrc7pEAwE&t=286s):

1. Nový skript, ale **nepřipojí se k nodu**. Nahoře `extends Resource` a `class_name EnemyData`.
2. `@export` proměnné (`health`, `speed`, `damage`). Bez `@export` by hodnoty existovaly jen v kódu a celý smysl by padl.
3. V průzkumníku *Create New → Resource → EnemyData*, uložit jako `goblin.tres`. Struktura se napsala **jednou**; každý další nepřítel je jen nový soubor s jinými čísly.

Na straně nepřítele pak zbude jediný řádek `@export var enemy_data: EnemyData` a v inspektoru zásuvka, do které se `.tres` přetáhne [(7:06)](https://www.youtube.com/watch?v=7dzrc7pEAwE&t=426s). A tady je ten výsledek, kvůli kterému se to dělá [(7:52)](https://www.youtube.com/watch?v=7dzrc7pEAwE&t=472s): *„skript samotný se už nikdy nemusí měnit. Chceš orka? Nekopíruješ skript ani netvoříš novou třídu — vytvoříš `orc.tres`, změníš čísla a přiřadíš ho téže scéně. Chování zůstává, mění se jen data."*

**Kde všude se to hodí** [(8:48)](https://www.youtube.com/watch?v=7dzrc7pEAwE&t=528s) je vlastně jediná otázka: zbraně (damage, kadence, zásobník, ikona, cena, vzácnost), předměty (jméno, popis, ikona, hodnota, váha, efekty), povolání pro výběr postavy. Autorovo shrnutí je použitelné jako detektor: **kdykoli vyrábíš spoustu objektů, které mají stejnou strukturu, ale jiné hodnoty, je to signál pro custom resource.**

**Tři chyby**, které autor jmenuje a které stojí za převzetí beze změny [(10:20)](https://www.youtube.com/watch?v=7dzrc7pEAwE&t=620s):

- **Herní logika v resourcu.** `EnemyData` má nést život a rychlost, ne AI. *„Resources ukládají informace, skripty řídí akci."*
- **Resource jako náhrada skriptu.** Nenahrazuje. Spolupracují: skript řídí, co postava dělá, resource definuje, co postava je.
- **Jeden obří resource na všechno.** `GameData` s nepřáteli, zbraněmi, předměty, questy i statistikami hráče se zvrhne stejně jako God class. Jeden datový typ, jeden resource.

> **Pozn.:** Tenhle vzor má v Unity zavedené jméno **ScriptableObject** a Bitlytic ho v jiném videu z playlistu takhle rovnou představuje. Kdo přichází z Unrealu, potká nejbližšího příbuzného v [Data assetu](../rejstrik.md#data-asset) — a stojí za to všimnout si, že **cesta je vždycky stejná: vytáhnout ladicí čísla z kódu do souboru, který se dá otevřít v editoru.** Rozdíl je jen v tom, jak snadno to engine dovolí; Godot je v tomhle nejlevnější — dvě řádky a máš nový datový typ.

**Souvislosti:** [Sdílený ve výchozím stavu](#sdileny-ve-vychozim-stavu-past-jednoho-dina) *(past, která na tebe čeká hned potom)* · [Kdy scéna a kdy resource](#kdy-scena-a-kdy-resource-prestavena-hra-jako-dukaz) · [Ukládání v UE](../praxe/ukladani.md#save-system-ktery-prezije-druhy-projekt-struktury-interface-a-async) *(data-driven přístup z druhé strany)* · [Rejstřík: Data asset](../rejstrik.md#data-asset) · [Rejstřík: Data-driven design](../rejstrik.md#data-driven-design) · [Rejstřík: Custom resource](../rejstrik.md#custom-resource)

---

## Sdílený ve výchozím stavu: past jednoho dina

**Zdroj:** [How to use Resources in Godot 4](https://www.youtube.com/watch?v=h5vpjCDNa-w) · [Bitlytic](https://www.youtube.com/channel/UCOlPBtGeh1YGL_rWpOLgLyg) · ~8 min, tutoriál

**Shrnutí:** Resource je soubor — a soubor je **jeden**. Když ho přiřadíš deseti nepřátelům, mají všichni **tentýž objekt**, ne deset kopií. Přidáš-li jednomu modrému dinovi 15 životů navíc, dostanou je **všichni modří dinové naráz**. To je občas přesně to, co chceš (globální nastavení obtížnosti), a mnohem častěji to, co tě dostane. Lék je jedna metoda: `duplicate()`.

### Rozpad myšlenky

**Mechanismus pasti** [(1:34)](https://www.youtube.com/watch?v=h5vpjCDNa-w&t=94s): *„s načítáním musíme být opatrní, protože resources jsou ve výchozím stavu sdílené."* Instance ve scéně nedrží data — drží **odkaz na soubor**. Zápis do toho odkazu je zápis do souboru, tedy do všech, kdo ho používají. Autor to nestaví jako chybu enginu: *„tohle možná chceš, ale pravděpodobně budeš chtít resource naklonovat"* — a klon dělá `duplicate()`.

Prakticky z toho plyne rozhodnutí, které je dobré udělat vědomě u každého resourcu: **je tohle šablona, nebo stav?** Šablona (statistiky typu nepřítele, definice zbraně, recept) se sdílí a nikdo do ní za běhu nepíše. Stav (aktuální život téhle konkrétní instance) do resourcu nepatří — nebo do něj patří jen jako klon.

**Proč se to vůbec vyplatí,** ukazuje autor na nepříteli [(0:48)](https://www.youtube.com/watch?v=h5vpjCDNa-w&t=48s): modrý dino má 50 HP a rychlost 25, červený 40 a 30. Přirozený tah je scénu zkopírovat. Jenže *„jsou to tytéž věci až na pár čísel — bylo by fajn sdílet stejnou scénu."* S resourcem `EnemyStats` (život, rychlost, textura) je nový nepřítel **jeden soubor**, ne nová scéna: autor v ukázce vytvoří zeleného dina za pár vteřin a jediná další úprava je zapsat ho do spawneru [(3:55)](https://www.youtube.com/watch?v=h5vpjCDNa-w&t=235s).

**Resources se dají dědit** [(2:21)](https://www.youtube.com/watch?v=h5vpjCDNa-w&t=141s), což je věc, kterou tutoriály obvykle vynechají — a otevírá to slušně velké systémy. `Item` má jméno a texturu; `ToolItem` z něj dědí a přidá „dá se vybavit". Inventář je pak **pole `Item`ů**, přičemž jednotlivé položky bydlí v `ItemStack` (odkaz na item + počet kusů) [(4:43)](https://www.youtube.com/watch?v=h5vpjCDNa-w&t=283s). A crafting je totéž o patro výš: `CraftingIngredient` (item + počet), `CraftingRecipe` (pole ingrediencí + výstup). Recept „krumpáč = 25 klacků + 30 kamenů" je pak **soubor, ne kód** — a změnit ho na rybu je otázka přetažení jiného `.tres`.

> **Pozn.:** Sdílení resourců je táž past, na kterou v [beginner průvodcích](zaklady.md#co-si-prinest-nez-otevres-editor) upozorňuje rada „u duplikovaných nodů použij *make unique*" — jen viděná z druhé strany. Tam byl sdílený collision shape, tady sdílená datová šablona; mechanismus je stejný a stejný je i signál, který od 4.6 dává editor (**ikona řetězu** u sdíleného resourcu). Nejjednodušší obrana je návyk, ne pravidlo: **rozhodni u každého resourcu, jestli se do něj bude za běhu psát, a když ano, klonuj ho hned při načtení**, ne až ve chvíli, kdy zjistíš proč.

**Souvislosti:** [Data ven ze skriptu](#data-ven-ze-skriptu-skript-ridi-chovani-resource-popisuje-co-ta-vec-je) · [Co si přinést, než otevřeš editor](zaklady.md#co-si-prinest-nez-otevres-editor) *(„make unique" jako tatáž past)* · [Strategy: chování jako vyměnitelný resource](stavy-a-vzory.md#strategy-chovani-jako-vymenitelny-resource) *(týž autor, resource nesoucí chování)* · [Rejstřík: Custom resource](../rejstrik.md#custom-resource) · [Rejstřík: Pass by reference](../rejstrik.md#pass-by-reference) · [UE: definice popisuje druh, instance nese kus](../praxe/inventar.md#definice-popisuje-druh-instance-nese-kus) *(tatáž hranice šablona/stav v inventáři)*

---

## Kdy scéna a kdy resource: přestavěná hra jako důkaz

**Zdroj:** [I Rebuilt My Godot Game Using Custom Resources (Here's Why)](https://www.youtube.com/watch?v=uMyxxsMtiOQ) · [DeeRaghooGames](https://www.youtube.com/channel/UC-KLgU0nzoCCEU6W16CS3vQ) · ~13 min, případovka

**Shrnutí:** Autor postavil **tutéž hru dvakrát** — jednou přes duplikované scény, jednou přes custom resources — a rozdíl popsal jednou větou, která je jádrem celé kapitoly: *„nevytvářel jsem novou hratelnost. Vytvářel jsem nová data."* To je ten test, který ti řekne, kdy scénu duplikovat a kdy sáhnout po resourcu. A poctivá výhrada, kterou video samo dodává: **u malého počtu úrovní jsou scény úplně v pořádku.**

### Rozpad myšlenky

**Hra je hádanka z emoji**: na obrazovce je sada emoji, moderátor po jednom odkrývá nápovědy pod nimi a nakonec se ukáže odpověď. **První verze** měla scénu na otázku — `question_1.tscn`, `question_2.tscn` [(1:39)](https://www.youtube.com/watch?v=uMyxxsMtiOQ&t=99s). Nová otázka = zkopírovat scénu, vyměnit emoji, přepsat texty. *„Skript logiky zůstává stejný. Tlačítka jsou identická. Emoji se dělají identicky. Měnil se jenom obsah."*

**Test, který z toho plyne** [(2:30)](https://www.youtube.com/watch?v=uMyxxsMtiOQ&t=150s): u deseti úrovní to bylo únosné, u padesáti nebo sta ne. Otázka, kterou si autor položil, je přenositelná na cokoli — **„když se mění jen obsah a nikdy ne chování, opravdu potřebuju novou scénu?"** Když se mění chování, potřebuješ scénu. Když se mění hodnoty, potřebuješ resource.

**Jak vypadá druhá verze.** Resource `LevelData` nese pole `PackedScene` s emoji, pole scén nápovědových popisků, **pole řetězců s texty** (aby texty nebyly natvrdo ve scénách), číslo otázky a odpověď jako `PackedScene` [(3:17)](https://www.youtube.com/watch?v=uMyxxsMtiOQ&t=197s). Klíčová věta o tom, co v resourcu **není**: *„neobsahuje žádnou herní logiku. Jen popisuje data jedné otázky."*

Skript levelu má pak jediný vstup — `@export var data: LevelData` — a **nic neví o konkrétních otázkách** [(7:49)](https://www.youtube.com/watch?v=uMyxxsMtiOQ&t=469s). Čte, co v resourcu stojí, a staví z toho scénu: `Marker2D` nody slouží jako pozice, kam se emoji a popisky instanciují, a smyčka je rozmístí podle pořadí v poli. Autor na to upozorňuje jako na past, která nikoho nenapadne: **na pořadí v poli záleží** — první emoji v poli je první na obrazovce [(6:16)](https://www.youtube.com/watch?v=uMyxxsMtiOQ&t=376s).

**A nad tím sedí správce** [(11:02)](https://www.youtube.com/watch?v=uMyxxsMtiOQ&t=662s): `LevelManager` drží **pole resourců otázek** a index. Postupuje polem, po každé otázce vyčistí staré instance, nastaví nová data a scénu přestaví — a když index dojede na konec pole, přepne na výherní obrazovku. Přidání dvaceti otázek je pak dvacet `.tres` souborů zapsaných do jednoho pole; kódu se to netýká.

> **Pozn.:** Za tímhle případem stojí obecnější rozdíl, který se vyplatí umět pojmenovat: **scéna je forma, resource je obsah.** Duplikovaná scéna kopíruje obojí, takže každá oprava formy se musí udělat tolikrát, kolik máš kopií — což je táž bolest, jakou v Godotu řeší [dědičnost scén](zaklady.md#editor-se-prohledava-ne-prochazi), jen resource jde o krok dál a formu **nekopíruje vůbec**. Zároveň platí autorova výhrada: u pěti úrovní je zavádění datové vrstvy práce navíc bez užitku. Rozhodovací hranice není počet, ale **očekávaný počet změn** — a ten už při psaní prototypu obvykle tušíš.

**Souvislosti:** [Data ven ze skriptu](#data-ven-ze-skriptu-skript-ridi-chovani-resource-popisuje-co-ta-vec-je) · [Resource, nebo dictionary?](#resource-nebo-dictionary-soubor-versus-radek-ve-skriptu) · [Editor se prohledává](zaklady.md#editor-se-prohledava-ne-prochazi) *(dědičnost scén jako slabší varianta téhož)* · [Rejstřík: Custom resource](../rejstrik.md#custom-resource) · [Rejstřík: Data-driven design](../rejstrik.md#data-driven-design)

---

## Resource, nebo dictionary? Soubor versus řádek ve skriptu

**Zdroj:** [Using Resources and Dictionaries for Godot Game Development](https://www.youtube.com/watch?v=D0uGtnMhB-E) · [DevWorm](https://www.youtube.com/channel/UCSehnx-yuPok8rOWlPIGGOQ) · ~6 min, esej

**Shrnutí:** Obojí drží data, obojí se dá exportovat — a rozdíl je v tom, **kde ta data bydlí**. Resource je samostatný soubor, který se dá načíst kdekoli; dictionary je struktura uvnitř skriptu, která žije jen tam. Z toho plyne celé rozhodovací pravidlo: **znovupoužitelná data → resource; jednorázová data v jednom skriptu → dictionary.** Autorův odhad poměru v praxi: resource asi v devíti případech z deseti.

### Rozpad myšlenky

**Tři rozdíly, ze kterých plyne všechno ostatní** [(1:33)](https://www.youtube.com/watch?v=D0uGtnMhB-E&t=93s):

- **Soubor versus vnitřek skriptu.** Resource se dá načíst do libovolného počtu nodů; dictionary je *„v podstatě zaseknutý tam, kde je definovaný."*
- **Víc souborů téže struktury.** Protože je resource soubor, můžeš mít deset souborů stejného typu s jinými hodnotami — a načtením jednoho z nich vyměníš celou sadu hodnot naráz. Autorův příklad je pěkný [(2:20)](https://www.youtube.com/watch?v=D0uGtnMhB-E&t=140s): různé `level` resources načítané do goblina za běhu dají levelovací efekt bez jediné podmínky.
- **Resource unese i funkce**, například gettery a settery, které ta data hlídají. Dictionary funkci sice odkazovat umí, ale *„není to ideální"*.

**Kdy naopak dictionary** [(3:07)](https://www.youtube.com/watch?v=D0uGtnMhB-E&t=187s) — a jsou to dvě situace, ne jedna:

1. **Struktura se mění za běhu.** Do dictionary jde přidávat a odebírat položky během hry, což resource neumí; k tomu má levné dotazy „je tohle uvnitř?" a „kolik toho je". Klíč nesmí být duplicitní, ale **klíč i hodnota můžou být libovolného typu** — takže dictionary umí spárovat dvě věci, které spolu jinak nesouvisejí (node → Vector2, resource → int).
2. **Jednorázový kontejner na uklizení jednoho skriptu** [(3:53)](https://www.youtube.com/watch?v=D0uGtnMhB-E&t=233s). Tady je autorův argument čistě ekonomický a proto správný: *„je snazší napsat dictionary přímo v tom skriptu, než definovat celou novou resource třídu."* Když víš, že data nikdy neopustí ten jeden soubor, resource je zbytečná ceremonie.

**A pak je tu odpověď, kterou lidé nečekají** [(4:40)](https://www.youtube.com/watch?v=D0uGtnMhB-E&t=280s): nejsou to konkurenti. **Resources se dají ukládat do dictionary a dictionary se dají definovat uvnitř resourců** — a spousta inventářových systémů dělá přesně to. Autorova rada, když si nejsi jistý, je metodická: rozbij funkci na menší úlohy a rozhodni se u každé zvlášť; často vyjde kombinace.

> **Pozn.:** Doplníme jedno rozlišení, které video nemá a které rozhoduje častěji než „bude se to znovupoužívat": **resource se dobře edituje myší, dictionary ne.** Jakmile má na data sáhnout designér — tedy i ty, ale v jiné roli než programátorské — patří to do inspektoru, protože ladit čísla v kódu je pomalé a chybové. Dictionary naopak vyhrává tam, kde s daty pracuje **jen program**: mapy, cache, vyhledávací tabulky. Slovník jako datová struktura má vlastní výklad v [Programátorském myšlení](../teorie/programatorske-mysleni.md#slovnik-vztahy-misto-indexu).

**Souvislosti:** [Data ven ze skriptu](#data-ven-ze-skriptu-skript-ridi-chovani-resource-popisuje-co-ta-vec-je) · [Kdy scéna a kdy resource](#kdy-scena-a-kdy-resource-prestavena-hra-jako-dukaz) · [Programátorské myšlení: slovník](../teorie/programatorske-mysleni.md#slovnik-vztahy-misto-indexu) · [Rejstřík: Map (dictionary)](../rejstrik.md#map-dictionary) · [Rejstřík: Custom resource](../rejstrik.md#custom-resource)
