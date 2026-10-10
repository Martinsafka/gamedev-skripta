# Případovka: nepřátelé a souboj

Nejsilnější část celé případovky, protože autor u nepřátel prošel **tři úplné přepisy** a všechny tři popsal — včetně toho, proč první dvě verze zahodil. Kapitola jde od mozku (jak se rozhoduje, co má nepřítel dělat) přes tělo (proč létající nepřítel nesmí sdílet fyziku s chodícím) k útoku (jak se definuje, co přesně se stane při zásahu) a končí u bosse, kde se to všechno sejde.

Společná nit, kterou se vyplatí číst napříč: **skoro každý přepis začal tím, že něco „technicky fungovalo" a přitom působilo blbě.**

---

## Tři patra AI: stav, exekutor, controller

**Zdroj:** [Creating SMART Enemies for my Indie Game! | Devlog](https://www.youtube.com/watch?v=4yqg1UEkiZo) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~19 min, devlog

**Shrnutí:** Místo programování každého nepřítele zvlášť postavil autor třípatrový systém: **stavy** (chůze, střelba, smrt), **state executive**, který rozhoduje *jak* se stavy pouštějí (postupně, náhodně), a **AI controller**, který mezi exekutory přepíná podle **priority** — nevšímavý, ohrožený, mrtvý. Háček, který ho stál nejvíc času, není v návrhu, ale v přechodech: **stav se nesmí dát přerušit kdykoli**, jinak nepřítel v půlce skoku začne chodit.

### Rozpad myšlenky

**Proč vůbec systém a ne rychlé řešení** [(0:47)](https://www.youtube.com/watch?v=4yqg1UEkiZo&t=47s). Autor si tu otázku poctivě položil — mohl by na testovací čtverce *„naplácat jakoukoli šmíru"* a hned testovat souboj. Zavrhl to ze dvou důvodů a ten druhý je zajímavější: *„nerad věci zahazuju, takže když začnu stavět nepřátele jeden po druhém, ta krusta tam nejspíš zůstane."* To je realistické sebehodnocení, ne teorie — **prototyp má tendenci se stát produkcí**, a kdo to o sobě ví, rozhoduje se jinak.

**Tři patra** [(2:20)](https://www.youtube.com/watch?v=4yqg1UEkiZo&t=140s):

- **Stavy** — jednotlivá chování, jak je zná každý [stavový automat](stavy-a-vzory.md#stavovy-automat-stav-je-podminka-plus-chovani).
- **State executive** drží skupinu stavů a rozhoduje, **jak** se pouštějí: v pořadí, náhodně, nebo podle vlastního pravidla. Autorova definice je hezká: *„je to ta ‚machine' část ze state machine."*
- **AI controller** dělá totéž, ale **exekutorům**, a zná jejich **prioritu**. Nevšímavý nepřítel patroluje; jakmile se hráč přiblíží, aktivuje se exekutor „ohrožený" s vyšší prioritou a převezme řízení.

Zisk je ten obvyklý a autor ho jmenuje přesně [(4:40)](https://www.youtube.com/watch?v=4yqg1UEkiZo&t=280s): logika sedí na **každém** nepříteli, takže se sdílí fyzika, hitbox, hurtbox i animace, a nový nepřítel se **skládá v editoru** místo psaní kódu — kód se dopisuje jen na skutečně nová chování.

**A teď to, co se rozbilo** [(6:13)](https://www.youtube.com/watch?v=4yqg1UEkiZo&t=373s), popsané na příkladu, který si zapamatuješ. Houbový nepřítel si spokojeně chodí sem a tam. Uvidí hráčku → vyšší priorita → vyskočí a vystřelí. Hráčka **udělá krok zpět** → nepřítel ji nevidí → *„v mém životě nejsou žádné hrozby, měl bych zase chodit sem a tam"* — a začne chodit **uprostřed skoku**. Chození dovnitř a ven z jeho dosahu z něj udělá *„malou rave party"*, protože přeskakuje mezi animacemi.

**Řešení je jeden atribut na stavu** [(8:34)](https://www.youtube.com/watch?v=4yqg1UEkiZo&t=514s), ale ve třech odstínech: stav může být **přerušitelný** (chůze — kdykoli), **nepřerušitelný** (útok se skokem — musí doběhnout, i když už na něj nepřítel „nemá právo") nebo **vynucující přerušení** (smrt — přeruší cokoli). Autorova formulace toho třetího je nejlepší mnemotechnika, jakou v tématu známe: *„když umřeš, všechno ostatní přestane."*

**A pak přijde přiznání, které dělá celý devlog cenným** [(10:08)](https://www.youtube.com/watch?v=4yqg1UEkiZo&t=608s): systém funguje a **pracuje se s ním blbě.** *„Není to intuitivní. Je těžké obalit si hlavou chování, které stavím, a špatně se to ladí — když se ten houbový chlapík chová špatně, není mi zřejmé proč."* Doufá, že se to zlepší, až dostaví výchozí stavy a bude skládat jen v editoru. **Pozdější díly ukazují, že se to nezlepšilo** — u létajících nepřátel na tentýž systém naráží znovu.

> **Pozn.:** Tři patra jsou fakticky **[Behavior Tree](../rejstrik.md#behavior-tree) postavený ručně**, jen bez editoru a bez ladicích nástrojů — a jeho vlastní stížnost („špatně se to ladí, nevidím, co se děje") je přesně ten problém, kvůli kterému vizuální editory stromů existují. To je užitečná lekce pro každého, kdo si chce psát vlastní AI systém: **náklad není v napsání, je v ladění.** Nakreslit tři patra je hodina; koukat se, proč houbový chlapík neposlouchá, jsou týdny. Srovnej s [State Tree](../praxe/state-trees.md#kostra-state-tree-ai-komponenta-tasky-a-kontext) a [Behavior Tree](../praxe/ai-zaklady.md#vyssi-liga-ai-controller-behavior-tree-a-blackboard) v Unrealu, kde je vizualizace součástí balení — a s [Utility AI](../praxe/ai-zaklady.md#utility-ai-rozhodovani-podle-skore-misto-vetveni), ke kterému autor nakonec u bosse sám dojde, aniž by to tak pojmenoval.

**Souvislosti:** [Stavový automat](stavy-a-vzory.md#stavovy-automat-stav-je-podminka-plus-chovani) · [Systém místo nepřítele](stavy-a-vzory.md#system-misto-nepritele-prenositelny-balik) *(týž nápad z jiného kanálu, čistěji)* · [Létající nepřátelé ve třech verzích](#letajici-nepratele-ve-trech-verzich-donut-misto-bodu) *(kde tenhle systém narazil znovu)* · [Základy nepřátelské AI](../praxe/ai-zaklady.md#vyssi-liga-ai-controller-behavior-tree-a-blackboard) · [Rejstřík: State machine](../rejstrik.md#state-machine) · [Rejstřík: Behavior Tree](../rejstrik.md#behavior-tree)

---

## Létající nepřátelé ve třech verzích: donut místo bodu

**Zdroj:** [Making Flying Enemies for my Indie Game! (Isadora's Edge Devlog)](https://www.youtube.com/watch?v=bGET0eZIo9w) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~19 min, devlog

**Shrnutí:** Tři verze létajících nepřátel, tři různé lekce. **První** byla jednoduchá a *„jakmile začala vypadat jako nepřítel, iluze se rozbila"*. **Druhá** kopírovala Hollow Knight — leť k bodu ve vzdálenosti od hráče — a měla vadu, kterou nešlo doladit: nepřítel bod **přeletí**, otočí se, a je z toho poletování. **Třetí** vyměnila bod za **prstenec** a chová se přirozeně. K tomu architektonické zjištění, které je hlavní přínos videa: **létající nepřítel nemá co sdílet fyziku s chodícím.**

### Rozpad myšlenky

**Verze 1: jednoduchá a mrtvá** [(1:35)](https://www.youtube.com/watch?v=bGET0eZIo9w&t=95s). Dva nepřátelé: **věž** (stojí na místě, hází lahvičku, když jsi v dosahu) a **přelétávající** ve stylu Mega Mana (letí přes obrazovku, shodí vejce, letí dál). Implementace triviální — první se ani nepotřebuje hýbat, druhému stačí vypnout gravitaci. A pak přijde diagnóza, která je jádrem celé myšlenky [(4:43)](https://www.youtube.com/watch?v=bGET0eZIo9w&t=283s): dokud to byla **létající krabice**, věž nevadila — *„dávalo smysl, že se nehýbe, působilo to jako věž."* Ale **jakmile dostala postavu a animaci**, začalo být nepřirozené, že nereaguje na zásah a neuhýbá: *„v tu chvíli se iluze rozbije."*

Zobecnění, které z toho děláme: **vizuální věrnost zvyšuje očekávání od chování.** Placeholder si smí dovolit hloupost, hotová postava ne. Prototyp v šedých krabicích tedy neodhalí všechno — část problémů se objeví teprve s grafikou, a je dobré s tím počítat, ne se tím nechat zaskočit.

**Verze 2: opsáno z Hollow Knight** [(5:29)](https://www.youtube.com/watch?v=bGET0eZIo9w&t=329s), a metoda je hodná následování: autor natočil **patnáct minut vlastního hraní**, kde jen uhýbal jednomu létajícímu nepříteli, a z toho **destiloval vzorec chování**: (1) vyber si cíl v určité vzdálenosti od hráče, (2) jsi-li v dosahu a útok není na cooldownu, zaútoč, (3) jsi-li na cíli, „poflakuj se", (4) jinak leť k cíli. Elegance toho vzorce je v tom, že **útěk i pronásledování z něj padají samy**: jsi-li mezi hráčem a cílem, letíš pryč (vypadá to jako útěk); jsi-li dál, letíš k němu (vypadá to jako pronásledování).

**Kde se to rozbilo, je zajímavější než to, že to fungovalo** [(12:41)](https://www.youtube.com/watch?v=bGET0eZIo9w&t=761s). Nepřítel má **zrychlení a zpomalení**, takže cílový bod **přeletí**. Za bodem správně vyhodnotí, že je mezi hráčem a cílem, **otočí se** — a poletuje sem a tam. Autor to obešel „tolerančním pásmem" kolem bodu, čímž vyrobil druhý problém: nepřítel se zastaví **čelem ke špatné straně**. A celé to podle něj působilo přesně tak, jak to bylo: *„je vidět, že letí k bodu kolem hráčky, ne že by mířila na hráčku."*

**Verze 3: donut** [(14:13)](https://www.youtube.com/watch?v=bGET0eZIo9w&t=853s) vymění bod za **mezikruží**. Uvnitř díry = jsi moc blízko → **uteč**. V prstenci = **poflakuj se**, tady jsi správně. Vně = jsi daleko → **leť k hráči**. Klíčová změna oproti verzi 2: **v prstenci se přestane cílit na bod a začne se cílit na hráčku**, čímž zmizí otáčení i špatný směr pohledu. Chování je *„mnohem přirozenější"* právě proto, že **cíl přestal být bod a stal se z něj pásmo** — a pásmo se nedá přeletět.

**A teď to architektonické** [(9:36)](https://www.youtube.com/watch?v=bGET0eZIo9w&t=576s), protože je to nejpřenositelnější kus. Autor létání nejdřív nacpal jako **„směr"** do existujícího systému směrů. Rozbilo se to na detekci zdí: chodící nepřítel u zdi **otočí směr**, což pro letícího nedává smysl — *„co to vůbec znamená ‚otočit se' při letu?"* Přesunul to tedy o patro výš na **stav** (idle / pohyb / let). Pomohlo to, ale narazil na knockback, který taky prochází fyzikou. A pak přišlo to, co říká sám: *„nejspíš vás to napadlo dřív než mě — létající nepřátelé nechodí po zemi a pozemní nepřátelé nelétají."* Chodící potřebuje gravitaci, kolizi pod sebou, tření ve vzduchu a skok; **létající nepotřebuje nic z toho**. Takže: **dva samostatné fyzikální controllery**. A dodává správnou výhradu — kdyby někdy chtěl nepřítele, který obojí umí, dá mu **oba** a bude přepínat, který je aktivní.

> **Pozn.:** Ten postup „směr → stav → vlastní controller" je učebnicová **eskalace abstrakce** a stojí za to si ho pojmenovat: zkusil to nejlevnějším způsobem, narazil, posunul o patro, znovu narazil, a teprve pak rozdělil. To je zdravé pořadí — opačné (rozdělit napřed, protože „to bude potřeba") vyrábí architekturu pro problém, který nemusí nastat. Rozhodovací signál, kdy je čas na rozdělení, dává tenhle případ dost přesně: **musíš-li do sdíleného kódu psát výjimky typu „tohle pro tenhle případ neplatí", sdílený kód už sdílený být nemá.** A jedna drobnost na okraj: video má **placený segment** o projektovém nástroji, který autor přiznává; věcného obsahu se to netýká.

**Souvislosti:** [Tři patra AI](#tri-patra-ai-stav-exekutor-controller) *(systém, do kterého se to nevešlo)* · [Komponenta má být sobecká](kompozice.md#komponenta-ma-byt-sobecka-test-kamene) *(kdy rozdělit a kdy ne)* · [Systém místo nepřítele](stavy-a-vzory.md#system-misto-nepritele-prenositelny-balik) · [AI vnímání](../praxe/ai-vnimani.md) · [Rejstřík: Context steering](../rejstrik.md#context-steering) · [Rejstřík: Boids](../rejstrik.md#boids)

---

## Frame data: definuj systém dřív, než ho postavíš

**Zdroj:** [I made a Fighting Game Frame Data System for my Indie Game!](https://www.youtube.com/watch?v=Dptztdm1rtg) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~32 min, technický devlog

**Shrnutí:** Bojovky popisují útok **po snímcích**: kolik snímků trvá nápřah, které snímky jsou aktivní, jak dlouho je zotavení. Autor si tenhle systém postavil pro 2D platformer — a **nejcennější není výsledek, ale postup**: než začal psát, sepsal **tři požadavky**, které musí systém splnit. Háček, kolem kterého se všechno točí: **data o útoku nesmějí bydlet na dvou místech**, protože pak se rozejdou.

### Rozpad myšlenky

**Tři požadavky, sepsané předem** [(9:17)](https://www.youtube.com/watch?v=Dptztdm1rtg&t=557s), a autor k tomu dodává větu, kterou by si měl přečíst každý, kdo si staví vlastní systém: *„definovat si to takhle je pro tvorbu dobrých systémů strašně důležité — když nevíš, co má tvůj systém dělat, jak bys ho mohl přimět, aby to dělal?"*

1. **Vytvářet hitboxy vizuálně v editoru**, ne psát čísla do konfiguračního souboru.
2. **Být generický** — jeden systém pro všechny útoky ve hře.
3. **Napojit se na AnimationPlayer**, protože animace a hitboxy musí být v čase svázané.

**Proč je třetí bod ten těžký** [(11:38)](https://www.youtube.com/watch?v=Dptztdm1rtg&t=698s). Nabízí se, aby animace při přehrávání „ťukala" na systém frame dat a ten podle čísla snímku aktivoval správný hitbox. Autor tuhle cestu **rozebral a zavrhl** ze dvou důvodů. První je pracnost: musel by u každého hitboxu ručně vyplnit jméno animace a číslo snímku, tedy **odpočítávat snímky** a přepisovat je. Druhý je zásadní [(12:24)](https://www.youtube.com/watch?v=Dptztdm1rtg&t=744s): *„data by žila na dvou místech naráz."* Přejmenuješ animaci → musíš to přepsat i jinde. A ta horší varianta: **animátor přidá jeden snímek doprostřed** — a všechna čísla snímků v systému jsou tiše špatně. *„Vytváří to obrovský prostor pro bugy, kde omylem smažu snímek a útok je rozbitý, aniž bych si toho všiml."* Autor u toho zmiňuje, že takové chyby jsou doložené i ve velkých hrách.

Řešení je proto obrácené: **frame data se ovládají z animace**. V AnimationPlayeru se na příslušných snímcích volá „začni útok", „další snímek", „konec" — a **jediným zdrojem pravdy o časování je animace**.

**Nástroj místo ruční práce** [(19:23)](https://www.youtube.com/watch?v=Dptztdm1rtg&t=1163s) je druhá polovina řešení a hezky navazuje na [editor scripty](projekt-a-vykon.md#nastroje-pro-sebe-editor-script-ktery-ti-usetri-boilerplate). Hitboxy by šlo přidávat ručně, ale autor si udělal **tlačítka v inspektoru** (*přidat jeden snímek*, *přidat snímek se dvěma hitboxy*, *přidat prázdný snímek*, *smazat vše*). Důvod není pohodlí: tlačítka totiž **zároveň udržují vnitřní seřazenou datovou strukturu**, ze které se za běhu čte „další snímek". Ručně by se ta struktura musela plnit taky — *„bylo by to nesmírně otravné, zdlouhavé a náchylné k chybám."* K tomu jedna elegance navíc [(15:32)](https://www.youtube.com/watch?v=Dptztdm1rtg&t=932s): uzel je **tool script**, takže si při vložení do scény **sám nastaví kolizní vrstvy** — *„nemusím se bát, že zapomenu vrstvu přepnout a útok nebude zasahovat."*

**Co se dá u každého hitboxu nastavit** [(22:29)](https://www.youtube.com/watch?v=Dptztdm1rtg&t=1349s) je nakonec ta zábavná část, protože z technického systému dělá **designový nástroj**: **poškození** · **síla odhozu** · **screen shake** · **hit stop** · **stavové efekty** (jed a spol.). A protože jeden snímek animace může mít **víc hitboxů**, dá se útok rozřezat na části: bossův kop má obrovský odhoz **jen na chodidlech**, zatímco zásah nohou tě odhodí normálně; bičem se dá **otrávit jen špička**. Autorovo srovnání sedí: přesně takhle vypadají rozbory frame dat z bojovek, kde je postava rozsekaná na barevné tvary s různými vlastnostmi.

**A jedna poctivá designová pochybnost** [(23:15)](https://www.youtube.com/watch?v=Dptztdm1rtg&t=1395s), kterou by většina devlogů zamlčela: různé poškození na různých částech útoku **motivuje hráče schválně schytat slabší zásah**, aby díky nezranitelnosti přeskočil ten silný. Autor neví, jestli je to vada, nebo zajímavá mechanika, a ptá se diváků. To je správná reakce — **nezamýšlená optimalizace hráčů není automaticky bug**, ale musí se o ní vědět.

> **Pozn.:** Nejpřenositelnější věc z celého videa není frame data, ale ta věta o **definici systému předem**. Tři požadavky sepsané na půl stránky mu daly kritérium, podle kterého poznal, že první nápad (data v obou místech) je špatný — **bez sepsaných požadavků by ho zavrhl až po týdnu práce**. Táž disciplína, jakou popisuje [dokumentace jako audit](../zapisky/dokumentace-jako-audit.md): psaní není záznam rozhodnutí, psaní je nástroj, kterým se rozhoduje. A ten „jeden zdroj pravdy" je přímo [SSOT](signaly.md#jediny-zdroj-pravdy-dva-budiky-ukazuji-ruzny-cas) — jen aplikovaný na časování animací.

**Souvislosti:** [Jediný zdroj pravdy](signaly.md#jediny-zdroj-pravdy-dva-budiky-ukazuji-ruzny-cas) *(týž princip pojmenovaný)* · [Nástroje pro sebe](projekt-a-vykon.md#nastroje-pro-sebe-editor-script-ktery-ti-usetri-boilerplate) *(tool scripty a tlačítka)* · [Combo a hit stop](#combo-a-hit-stop-dva-casovace-a-ctvrt-sekundy) · [Dokumentace jako audit](../zapisky/dokumentace-jako-audit.md) · [Rejstřík: Frame data](../rejstrik.md#frame-data) · [Rejstřík: Hitbox](../rejstrik.md#hitbox) · [Rejstřík: Single source of truth](../rejstrik.md#single-source-of-truth)

---

## Boss se staví z otázek, ne z atributů

**Zdroj:** [Making a BIG BOSS FROG for my indie game! | Devlog](https://www.youtube.com/watch?v=atqSho7wmGE) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~26 min, devlog

**Shrnutí:** Návrh mini-bosse od nápadu po hotový souboj — a co je na tom cenné, je **pořadí otázek**. Nezačíná se u statistik, ale u **kontrastu s ostatními bossy** (tenhle je těžký a zakořeněný, protože ten druhý je vzdušný a teleportuje se), pokračuje se **slovníkem uhýbání** a končí u problémů, které se ukážou až při hraní: *nedá se to přečíst*, *omrzí to* a *působí to hloupě*. Háček, který stojí za převzetí: **snížit bossovi životy je skoro vždycky špatná oprava nudy.**

### Rozpad myšlenky

**První otázka není „jaký boss", ale „vůči čemu"** [(2:22)](https://www.youtube.com/watch?v=atqSho7wmGE&t=142s). Na konci levelu čeká jiný boss — **vzdušný, teleportující se, střílející projektily**. Z toho padá zadání pro tenhle: *„velký a ne vzdušný — velký, těžký a zakořeněný."* Návrh tedy nevychází z toho, co je samo o sobě cool, ale z **místa v sadě**. Autor u toho rovnou definuje, co u bosse vlastně musí vymyslet: **jak se pohybuje po aréně a jaké má útoky.** Zbytek (příběh, vizuál) je oblečení.

**Mechanika vzniká z detailu, ne z tabulky** [(3:55)](https://www.youtube.com/watch?v=atqSho7wmGE&t=235s). Nápad „ať má dva jazyky místo jednoho, je zkažený" nebyl mechanický, ale **vygeneroval mechaniku**: dva jazyky vytvářejí **vzorce, mezi kterými se uhýbá** — oba dole (přeskoč), oba nahoře (podklouzni), jeden a jeden (musíš na zeď). Z jedné estetické myšlenky vznikl **slovník tří situací** — a to je víc, než dá většina statistik.

**Proč nesmí sedět v rohu** [(5:29)](https://www.youtube.com/watch?v=atqSho7wmGE&t=329s): některé Mega Man bossy stojí na místě a jen střílejí, a autorovi *„připadalo, že boss je součást arény místo aby byl živý tvor."* Přidal proto **skákání přes arénu** — a získal tím druhou funkci zdarma: **při přeskoku vzniká uhýbací situace** (podklouzni, nebo počkej a přeskoč).

**Problém jedna: nedá se to přečíst** [(7:03)](https://www.youtube.com/watch?v=atqSho7wmGE&t=423s). Všechny tři varianty jazyků měly **stejný nápřah**, takže útok byl *„zcela neuhnutelný"* — než jazyky vyjely, nešlo poznat, co přijde. Řešení je učebnicové: **různé nápřahy jako tell**. A tady je ta metodologicky nejzajímavější věc celého devlogu: aby si ověřil, že tell vůbec zabere, **nedělal animace** — dal vedle bossovy hlavy **barevný obdélník**. A ještě si k tomu poctivě odpověděl na námitku *„ale já si ty barvy nepamatuju"*: hráč si taky bude muset zapamatovat, který nápřah co znamená, takže **je to férové srovnání**. S obdélníky *„byl ten souboj hodně zábavný"* — a teprve pak se kreslilo.

**Problém dva: omezená sada omrzí** [(8:36)](https://www.youtube.com/watch?v=atqSho7wmGE&t=516s). Dvě možnosti: přidat útoky, nebo **snížit životy**. Autor druhou variantu zavrhuje s dobrým argumentem: kratší souboj *„nepůsobí zdaleka tak působivě a nemusíš se ty jazyky vůbec naučit — dá se to prohrubasit."* Chtěl, aby jádrem zážitku bylo **naučit se uhýbat**, a **méně životů to jádro zabíjí**. Zobecnění: **délka souboje není parametr obtížnosti, je to prostor na učení.** Přidal proto dva útoky — **plivnutí**, které nechá na zemi zpomalující kaluž (a tím **mění řešení skoků**, protože v cestě může být místo, kterým se nedá projet), a **tělesný náraz** krátkého dosahu, aby se nedalo stát před bossem a mlátit do něj.

**Problém tři: boss působí hloupě** [(13:14)](https://www.youtube.com/watch?v=atqSho7wmGE&t=794s) — a tohle je nejlepší část. Původně si házel **kostkou**: na jedničku první jazyk, na dvojku druhý, na trojku třetí, na čtyřku skok… Výsledek: *„vypadá to, že vůbec nereaguje na hráče — klidně by mohl mít všech šest očí zavřených."* Nejhorší na tom je, že **mine i stojícího hráče**, a to je hned vidět.

**Oprava má tři složky** [(16:21)](https://www.youtube.com/watch?v=atqSho7wmGE&t=981s), které dohromady dělají překvapivě chytré chování:

1. **Aréna je rozdělená na zóny** a boss sleduje, ve které je hráč. Ke každé zóně patří **vhodné útoky** — jsi ve vzduchu → jazyky nahoru nebo plivnutí; jsi na zemi → jazyky dolů nebo rázová vlna.
2. Každý útok má **pravděpodobnostní váhu, která po použití klesá.** Zůstáváš pořád na zemi? Boss se toho *„nabaží"* a přeskočí na druhou stranu, aby situaci rozhýbal.
3. **Tvrdý strop na opakování**: po třech stejných akcích za sebou se ta akce **odebere ze seznamu možností**.

Výsledek autor popisuje přesně: *„jeho útoky neminou samy od sebe — minou jen tehdy, když uhnu."*

**A nakonec counter jako rozhodnutí, ne odměna** [(22:33)](https://www.youtube.com/watch?v=atqSho7wmGE&t=1353s): v jednom snímku útoku boss **zezlátne**, a trefíš-li ho právě tehdy, omráčíš ho. Autorův popis toho, proč to funguje, je hezky designérský: *„vzniká tím pěkný hráčský moment, kdy se rozhoduješ, jestli do counteru jít."* Máš-li života dost, riskneš a odměna je velká; jsi-li na dně, **necháš to být**. Není to trik na obtížnost — je to **volba, jejíž cena se mění podle stavu hry**.

> **Pozn.:** Dvě věci, které se z toho dají vzít i mimo bossy. **Zaprvé** ten barevný obdélník: **prototypuj signál dřív než jeho podobu.** Otázka „pozná hráč včas, co přijde?" se dá zodpovědět za pět minut placeholderem; kreslit animaci a *pak* zjistit, že tell nefunguje, stojí dny. **Zadruhé** ten sestupný váhový systém — je to fakticky [Utility AI](../praxe/ai-zaklady.md#utility-ai-rozhodovani-podle-skore-misto-vetveni) postavené intuitivně: skóruj akce podle situace, penalizuj opakování, vyber vážený náhodný výběr. Autor to tak nikde nenazve, ale vyrobil přesně to — a je poučné, že ho k tomu dovedl **pocit z hraní**, ne teorie. Za pozornost stojí i drobná technická poznámka na okraj [(20:12)](https://www.youtube.com/watch?v=atqSho7wmGE&t=1212s): roztahovací jazyk přes **nine-slice** vypadal špatně, takže ho nakonec **nakreslili ručně** — čtyři animace stačily na všechny tři vzorce. Levné technické řešení nebylo dost dobré a oni to poznali včas.

**Souvislosti:** [Tři patra AI](#tri-patra-ai-stav-exekutor-controller) *(systém, na kterém boss běží)* · [Frame data](#frame-data-definuj-system-driv-nez-ho-postavis) *(kde bydlí ten odhoz z kopu)* · [Utility AI](../praxe/ai-zaklady.md#utility-ai-rozhodovani-podle-skore-misto-vetveni) *(pojmenovaná podoba téhož)* · [Obtížnost a výzva](../teorie/obtiznost.md) · [Horor design: pětikrokový cyklus napětí](../teorie/horor-design.md) · [Rejstřík: Tell](../rejstrik.md#tell) · [Rejstřík: Utility AI](../rejstrik.md#utility-ai)

---

## Combo a hit stop: dva časovače a čtvrt sekundy

**Zdroj:** [Game Dev Secrets: About Combo Attacks](https://www.youtube.com/watch?v=GbSTBAI6dJc) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~1 min · + [Game Dev Secrets: Stealing from Fighting Games!](https://www.youtube.com/watch?v=JAW6Zn3rMBk) · týž kanál · ~1 min

**Shrnutí:** Dvě minutové odpovědi, které dohromady tvoří kostru dobrého úderu. **Combo** je otázka dvou časovačů, které se překrývají: kratší brání spamu, delší otevírá okno na navázání. **Hit stop** je krátké zamrznutí hry v okamžiku zásahu — a autor k němu dodává to nejužitečnější, co u takové techniky být může: **konkrétní hodnoty a doporučení, kterou si vybrat.**

### Rozpad myšlenky

**Combo přes dva časovače** [(0:02)](https://www.youtube.com/watch?v=GbSTBAI6dJc&t=2s):

- **Cooldown timer** — kratší. Dokud běží, nemůžeš zaútočit. Bez něj *„bys mohl vlastní útok přerušit vlastním útokem"*.
- **Combo timer** — o něco delší. Spouští se zároveň.

Mezi doběhnutím prvního a druhého vzniká **okno**: cooldown už skončil, takže smíš zaútočit, a combo timer ještě běží, takže se místo základního útoku provede **další rána comba**. K tomu stačí pamatovat si, **kolikátá rána zrovna byla**. Autor to ověřuje pěkně názorně — combo timer prodlouží do absurdna a najednou lze combem **donekonečna cyklovat**, což ukazuje, že celý mechanismus je opravdu jen ten překryv.

Co z toho plyne pro ladění: **délka combo timeru je designový parametr, ne technický.** Krátký = combo pro ty, co trefí rytmus; dlouhý = combo pro každého, kdo mačká. Tímhle jedním číslem se posouvá [skill floor i skill ceiling](../rejstrik.md#skill-ceiling).

**Hit stop** [(0:03)](https://www.youtube.com/watch?v=JAW6Zn3rMBk&t=3s) je *„fakt skvělá technika z bojovek"*: v okamžiku, kdy útok zasáhne, se **hra na zlomek vteřiny zastaví**. Autorovo vysvětlení, proč to funguje, má dvě části a ta druhá se často vynechá: přidává to **váhu**, a **dává hráči okamžik, ve kterém si stihne uvědomit, že trefil**.

**A teď ta čísla**, kvůli kterým klip stojí za citaci [(0:03)](https://www.youtube.com/watch?v=JAW6Zn3rMBk&t=3s). Autor pouští tentýž útok bez hit stopu a pak s **1/20 s**, **1/10 s**, **1/5 s** a **1/4 s**. Jeho doporučení pro běžný sek: **pásmo mezi dvacetinou a desetinou sekundy**. A pravidlo, které z toho dělá systém: **hit stop se škáluje podle síly útoku** — bossův velký kop *„je cítit líp s pořádnou porcí hit stopu"*.

To zapadá do [frame data systému](#frame-data-definuj-system-driv-nez-ho-postavis), kde je hit stop nastavitelný **na každý aktivní snímek zvlášť**: sek špičkou biče dostane skoro nic, závěrečný náraz hodně. Autorova výhrada odtamtud platí i tady: **má-li silný hit stop každý útok, přestane znamenat cokoli.**

> **Pozn.:** Hit stop je jeden z nejlevnějších juice triků vůbec — pár řádků kódu a žádný asset — a přesto se na něj zapomíná, protože není vidět na screenshotu. Patří k [Celeste](../teorie/game-feel.md#celeste-krivky-v-snimcich-a-hrst-tichych-ulev), kde se čtyřsnímková pauza u dashe kombinuje s mikroskopickým otřesem obrazovky, i do [katalogu juice](../teorie/game-feel.md#katalog-juice-deset-detailu-ktere-prodavaji-tutez-mechaniku). Jednu vlastní výhradu doplníme, protože ji ani jeden zdroj neříká: **hit stop zdržuje vstup.** V rychlé hře s přesným časováním je desetina sekundy dost na to, aby hráč zmeškal okno — proto se v bojovkách během hit stopu vstupy **bufferují** místo aby se zahazovaly. Kdo si hit stop přidá, měl by přidat i [input buffering](../rejstrik.md#input-buffering); jinak vyrobí juice za cenu ovladatelnosti.

**Souvislosti:** [Útočit v pohybu, nebo se zastavit](pripadovka-pohyb.md#utocit-v-pohybu-nebo-se-zastavit) *(designová stránka téhož comba)* · [Frame data](#frame-data-definuj-system-driv-nez-ho-postavis) *(kde se hit stop nastavuje per hitbox)* · [Katalog juice](../teorie/game-feel.md#katalog-juice-deset-detailu-ktere-prodavaji-tutez-mechaniku) · [Combat je rytmus](../teorie/game-feel.md#combat-je-rytmus-kazdy-utok-ma-ucel-a-placeholder-je-nastroj) · [Rejstřík: Hit stop](../rejstrik.md#hit-stop) · [Rejstřík: Input buffering](../rejstrik.md#input-buffering) · [Rejstřík: Juice](../rejstrik.md#juice) · [Hit stop v UE přes Custom Time Dilation](../praxe/souboj.md#hit-stop-zastav-oba-ale-kazdeho-jinak) *(útočník zpomalí, zasažený stojí; delší časy)*
