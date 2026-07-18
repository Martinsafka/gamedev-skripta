# Systémy a mechaniky: hra jako stroj

Joe Baxter-Webb (Indie Game Clinic) rozplétá tři pojmy, které se běžně melou dohromady — pravidla, mechaniky, systémy — a staví nad nimi systémové myšlení: hra je stroj se zamýšleným výstupem, kterým jsou pocity hráče. Kapitola navazuje na [Smyčky a řetězce](smycky-a-retezce.md) (tam tvary, tady slovník a stavba) a na [MDA framework](zaklady.md#mda-mechaniky-chovani-pocity) — a končí u dvou podceňovaných druhů mechanik: expresivních a kognitivních.

---

## Pravidla → mechaniky → systémy: slovník s ostrými hranami

**Zdroj:** [Game Mechanics & Systems Thinking](https://www.youtube.com/watch?v=nkLmjJK3vOw) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · ~41 min, video-esej

**Shrnutí:** **Pravidla** jsou logika hry — každé „když tohle, pak tohle"; přesně to, co se při programování překládá do kódu [(0:48)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=48s). **Mechaniky** jsou z pravidel poskládané jednotky gameplaye: slovesa hráče (skoč, seber, unikni) — nástroje, kterými hráč (a stejně tak „protistrana" hry: AI, obtížnost) působí na herní svět [(2:22)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=142s). **Systémy** jsou větší sady pravidel, se kterými hráč interaguje skrze mechaniky [(6:16)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=376s). Videohry mají navíc jednu zvláštnost: na rozdíl od deskovek umí pravidla před hráčem **skrýt** [(1:35)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=95s).

### Rozpad myšlenky

Gramatika, která se dobře pamatuje [(7:51)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=471s): **mechaniky jsou slovesa, systémy dodávají podstatná jména** — útočíš (mechanika) na vlnu nepřátel (objekt ze spawn systému). I ručně postavené levely jsou systém, jen lidský místo procedurálního [(8:38)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=518s). A systém zahrnuje i svou **informační stránku**: menu skill stromu je součást progression systému, dekorace, která říká „po téhle zdi se dá lézt", je součást traversal systému [(7:03)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=423s) — komunikace mechaniky je částí mechaniky.

Dvě praktické věty z toho slovníku. Za prvé: **totéž sloveso s jinými pravidly je jiný pocit** [(3:57)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=237s) — „sebrat" může být přešlápnutí mince, stisk tlačítka nad pytlíkem, nebo úchop ve VR; létající zlaté mince by v drsné detektivce působily absurdně. Pocit jádrové mechaniky je charakter hry, takže **jádro vylaď a zamkni brzo** [(4:44)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=284s) — u hry o skákání je finální kvalita skoku založní kámen (totéž říká [krabice hraček](zaklady.md#engagement-hracky-spojene-zajimavymi-rozhodnutimi)). Za druhé, k ladění pravidel citovaný Sid Meier: **„zdvojnásob, nebo rozpůl"** [(5:30)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=330s) — velká změna ukáže, co pravidlo dělá; opatrné tweaky předpokládají, že je skoro správně, což většinou není. (Stejný návyk učí [Luke Muscat](rady-z-praxe.md#kompilace-od-profiku-cti-problem-za-navrhem-ukazuj-brzy-ozen-se-s-hrou): 10–100× nadoraz.)

A varování pro stavitele: **systémy nestavěj dřív, než víš, co s nimi mechaniky udělají** [(9:24)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=564s). Prototyp deck builderu nepotřebuje skutečnou rotaci decku — systém se dá zfejkovat. Extrémní případ z praxe: stovky hodin na generátoru procedurálních levelů bez existující hry [(10:10)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=610s) — „to je gamedev jako technické hobby; legitimní, ale není to vývoj hry." Procedurální generace odpovídá na otázku „jak vyrobit levely" — a bez mechanik ještě nemáš důvod levely mít. (Knihovna tenhle vzorec zná jako [engines inside your engine](produktivita.md#investice-bez-validace-lesteni-systemy-a-optimalizace-predem).)

**Souvislosti:** [Smyčky a řetězce](smycky-a-retezce.md) · [Žrouti času](produktivita.md#investice-bez-validace-lesteni-systemy-a-optimalizace-predem) · [Rejstřík: Mechanika](../rejstrik.md#mechanika) · [Rejstřík: Core loop](../rejstrik.md#core-loop)

---

## Stroj s účelem: kávovar dělá kávu, horor dělá strach

**Zdroj:** [Game Mechanics & Systems Thinking](https://www.youtube.com/watch?v=nkLmjJK3vOw) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · stejné video, prostřední část

**Shrnutí:** Proč o hrách mluvíme jako o strojích? Ne proto, že jsou technologie (mechaniky mají i deskovky, sporty a slovní hry [(12:34)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=754s)) — ale protože metafora stroje vynucuje otázku **zamýšleného výstupu** [(13:21)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=801s): kávovar vyrábí kávu, horor strach, puzzle pocit chytrosti, akční hra adrenalin. Systémové myšlení = od výstupu zpátky k mechanismům, které ho vyrobí.

### Rozpad myšlenky

**Past realismu** [(15:40)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=940s): „skok bude vysoký, jak by skočil člověk" nemá nic společného s tím, jak se hráč má cítit. Prakticky pro indie: **napřed pár interakcí, které jsou radost, a art se settingem nech srůst kolem nich** [(16:26)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=986s) — ne obráceně (postavit fikční svět a cpát do něj mechaniky simulace života; srovnej [„zábavná na výrobu ≠ na hraní"](solo-vyvoj.md#rozhodnuti-pred-prvnim-radkem-platforma-hrac-ocean)).

**Mechanika nežije izolovaně** [(16:26)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=986s): šroub není stroj a volant se stává dílem auta až v autě — deskovkáři proto rozlišují „mechanismy" (jednotky) a „mechaniku" (celek) [(17:12)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=1032s). Odtud dvě klasické chyby přebírání: (1) navršit mechaniky, které se ti líbí, bez ohledu na to, že se perou o tutéž roli (tři progression systémy v jedné hře [(17:59)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=1079s)); (2) **odstranit „otravné" pravidlo bez pochopení jeho funkce**: deck builder bez odhazování ruky se rozpadne, protože právě discard žene rotaci decku a nové konfigurace karet [(18:45)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=1125s). Žánr je v tomhle čtení **předbalený stroj**: sada mechanik, o kterých víme, že drží pohromadě — a zároveň slib publiku [(19:33)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=1173s); co vyndáš, nahraď něčím stejné hodnoty (FPS bez střelby potřebuje puzzle nebo příběh na jejím místě).

**Gameplay jako řízení auta** [(24:13)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=1453s): přímá kontrola (tvá slovesa) + okolnosti mimo kontrolu (počasí, město, pravidla provozu). Řízení v cizí zemi je zase vzrušující, protože se rekalibruješ — a hra má stejně obměňovat systémy a obsah, aby se z ní nestala automatická cesta do práce [(25:47)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=1547s). Gameplay je **totalita** vozidla, zákonů, geografie i destinací — proto je dobrá hra tak těžká, proto začínej s malým strojem o málo součástkách [(26:33)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=1593s), a proto je legitimní začít u módů a level editorů (menší sada dovedností najednou). A důsledek pro „originalitu": hráči nechtějí učit se úplně nové věci — chtějí **přenést naučené do mírně nového kontextu**; „klonuj malou hru žánru, kterému rozumíš, přidej twist a reflektuj, co udělal" [(27:20)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=1640s).

> **Pozn.:** Boční poznámka videa o studiích jako továrnách [(21:53)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=1313s) stojí za přenos na jednotlivce: tvá „továrna" je nástrojovaná na určité stroje — a rady „dělej, co zrovna trendí" ignorují, že byznys znamená zarovnat díru na trhu s tím, *co umíš vyrobit*. „Instalatéra si na opravu auta nenajmeš."

**Souvislosti:** [Základy: MDA](zaklady.md#mda-mechaniky-chovani-pocity) · [Sólo vývoj](solo-vyvoj.md) · [Zábava a flow](zabava.md) · [Rejstřík: Design pattern](../rejstrik.md#design-pattern) *(tentýž princip v kódu)*

---

## Expresivní a kognitivní mechaniky: rádio v autě a myšlení jako sloveso

**Zdroj:** [Game Mechanics & Systems Thinking](https://www.youtube.com/watch?v=nkLmjJK3vOw) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · stejné video, závěr

**Shrnutí:** Dva druhy mechanik, které v učebnicích zapadají. **Expresivní mechaniky** [(28:52)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=1732s) jsou rádio a klimatizace auta — k dojetí do cíle je nepotřebuješ, ale mění, jak cesta chutná: pohladit kočku, rozbíjet bedny bez lootu, emoty, účesy. **Kognitivní mechaniky** [(33:32)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=2012s) jsou slovesa, která se dějí v hlavě hráče: pozorovat, dedukovat, soudit — aktivita zadaná designérem je mechanika, i když nemá tlačítko.

### Rozpad myšlenky

**Expresivní mechaniky** autor z praxe recenzování označuje za častý rozdíl „mezi docela dobrou a výbornou hrou" [(29:38)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=1778s). Teoretická opora je Cailloisovo spektrum **ludus ↔ paidia** [(30:25)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=1825s): hra podle přísných pravidel vs. volné „blbnutí" — a většina hráčů dnes čeká od videohry obojí; „když hra působí holá, možná má moc ludus a málo paidia." Nepatří do prototypu (jádro první), ale patří do plánu: cokoli, co nechá hráče **nechat ve světě stopu, projevit vkus nebo být chvíli za šaška**, aniž to systém hry musí uznat, vyrábí hravost a paměť. A má to i marketingovou logiku [(31:59)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=1919s): titěrné, funkčně zbytečné interakce čte publikum jako attention to detail — „když si můžou dovolit tohle, jádro bude solidní"; vztah s publikem se staví z malých věcí.

**Kognitivní mechaniky** rehabilitují „walking simy": pozorovateli se zdá, že hráč jen chodí — jenže aktivita běží v hlavě [(34:18)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=2058s). Proto tolik narativních her staví hráče do role **detektiva či novináře**: role primuje k pozorování a souzení [(35:05)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=2105s). Dating sim je hra o souzení postav; strategie mají vysoký poměr myšlení ku konání — mnoho soudů ústí v jediný klik, proto šachy potřebují hodiny [(35:54)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=2154s). Lekce pro každou příběhovou hru: **navrhuj slovesa hráče, i když jsou kognitivní** — kvalita hry stojí na tom, jak dobře je situace k těm slovesům vybízejí. „Nejmocnější slovesa tvé hry nemusí mapovat na tlačítka" [(36:40)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=2200s).

> **Pozn.:** Video se výslovně hlásí k formátu „thought exercises, ne listicle" — indie vývoj je podnikání a chce vůdčí myšlení, ne následování [(36:40)](https://www.youtube.com/watch?v=nkLmjJK3vOw&t=2200s); tentýž postoj rozvíjí [Rady nefungují tam, kde začíná design](rady-z-praxe.md#rady-nefunguji-tam-kde-zacina-design). Pro naše poměry: expresivní mechanika je přesně to, co dělá [imerzi balvanu](game-feel.md#imerze-svet-ktery-na-tebe-odpovida) — zválcovaná tráva nikomu nepřičítá skóre, a přesto nese hru.

**Souvislosti:** [Game feel a imerze](game-feel.md) · [Příběh a postavy](pribeh-a-postavy.md) · [Rejstřík: Expresivní mechanika](../rejstrik.md#expresivni-mechanika) · [Rejstřík: Ludus a paidia](../rejstrik.md#ludus-a-paidia)
