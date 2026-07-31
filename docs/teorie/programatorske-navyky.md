# Programátorské návyky: malé věci, které se skládají

Vedle mentálních modelů ([Programátorské myšlení](programatorske-mysleni.md)) existuje druhá, nenápadnější páka: drobné návyky, které „vypadají moc malé na to, aby byly důležité" — a právě proto je skoro nikdo nedělá. Tahle kapitola destiluje patnáct návyků z videa Manware do tří mechanismů: paměť a důkaz, růstové sázky, tělo a prostředí.

---

## Patnáct malých návyků, tři mechanismy

**Zdroj:** [15 Tiny Coding Hacks That Got Me In Amazon](https://www.youtube.com/watch?v=Z36-xqUv3W8) · [Manware](https://www.youtube.com/channel/UCEihg8EpedxZKQ_Gm1XVedg) · ~10 min, osobní seznam návyků

**Shrnutí:** Žádný jednorázový skok, který tě „instantně předřadí před 99 % programátorů", neexistuje [(0:02)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=2s) — kariéru podle autora změnily mikronávyky s téměř nulovým úsilím, které se rok skládají úrokem. Seznam je psaný pro kariérního programátora, ale mechanismy pod ním jsou stejné pro samouka v gamedevu: zhmotňuj, co ses naučil; sázej na věci, co tě přerostou; a nesabotuj vlastní hardware.

### Rozpad myšlenky

**Paměť a důkaz** — návyky, které učení zhmotňují:

- **Commit každý večer** [(0:48)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=48s): nejde o GitHub trávník pro recruitery, ale o dvojí efekt — hmatatelný „proof of work" a hlavně **vybavovací trénink**: shrnout den do commit message znamená znovu si projít, co jsi vyřešil.
- **TIL.md** [(3:56)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=236s): obyčejný soubor „today I learned", jedna řádka na poznatek. Kondenzace na větu ukládá do dlouhodobé paměti — a zpětné čtení ukazuje ujetou vzdálenost. Žádné notion šablony; prostý append.
- **Vysvětluj druhým** [(3:56)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=236s): autorův učitel to rámoval čísly — poslech ≈ 20 % porozumění, zápis ≈ 40 %, výuka ≈ 90 %. Kdo neumí zjednodušit, nerozumí. (Devlog je přesně tenhle návyk v masce marketingu — viz [Devlogy](devlogy.md).)
- **Mluv o problémech nahlas** [(2:22)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=142s): kamarád vidí z ptačí perspektivy; půlku řešení najdeš už tím, že problém formuluješ — klasická gumová kachna, plus sounáležitost, která drží u řemesla.

**Růstové sázky** — kam mířit úsilí:

- **Stav projekty, které zní nemožně** [(1:34)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=94s): CRUD appka po desáté nenaučí nic; „nevím, jak se staví engine" je dobrý důvod ho zkusit — většina „nemožných" věcí je zdokumentovaný proces krok za krokem. Ne víc úsilí, jiná cesta.
- **Čti denně kus kódu někoho lepšího** [(0:48)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=48s): romanopisec čte bestsellery. Pět minut, sto řádků, tři otázky: jak pojmenovávají? jak řeší chyby? co je ten divný syntax?
- **Pěstuj nespokojenost** [(4:42)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=282s): inženýry podle autora neodděluje IQ ani talent, ale neschopnost nechat věc být, dokud nevíš, **jak funguje pod kapotou**. (Celá kapitola o [Quake 3 odmocnině](matematika-pro-gamedev.md#pripadovka-rychla-inverzni-odmocnina-z-quake-3) je pomník téhle vlastnosti.)
- **Dělej na tom, na čem ti záleží** [(5:28)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=328s): kód jen pro peníze = burnout; kód jako dovednost + zábava + obživa = udržitelnost. Máš-li rád hry, stav hry — programování je nástroj do libovolného oboru.
- **Neporovnávej se** [(8:36)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=516s): každý startuje s jinými buffy; jediná proměnná pod tvou kontrolou je tvůj vlastní skill gap.

**Tělo a prostředí** — hardware, na kterém to celé běží:

- **Spánek** [(7:49)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=469s): 18+ hodin vzhůru ≈ výkon opilého člověka; ponocování není flex, ale „soutěž v hlouposti". Spánek konsoliduje paměť („RAM se zapisuje na SSD") — hodina spánku navíc porazí hodinu nočního učení.
- **Telefon do jiné místnosti** [(4:42)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=282s): přítomnost v místnosti = trvalý debuff vůle; udělej používání *fyzicky* těžké.
- **Plánuj jako senior** [(7:01)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=421s): 80 % plánování, 20 % stavění — rozhodnutí udělaná předem (schéma, rozhraní, pořadí práce) nepřerušují flow a nekončí refactoringem. Srovnej s [devlogem jako mapou](../zapisky/devlog-jako-mapa.md) a [pravidlem 70/30](../zapisky/pravidlo-70-30.md).
- Drobné: klidná nerepetitivní hudba proti kortizolu [(6:15)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=375s), Vim motions jako gamifikace psaní [(2:22)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=142s) („internet křivku učení přehání" — 15 minut základů), a klávesnice, u které tě psaní baví [(8:36)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=516s).

> **Pozn.:** Kontext videa je kariérní sprint do Amazonu — ne gamedev, a je fér to vědět. Mechanismy ale sedí přesně na potíže samouka popsané v [Žroutech času](produktivita.md): práce bez validace je porušený návyk „důkazu", únik k snadné tvorbě je prohraná růstová sázka. A commit-každý-večer + TIL.md je nejlevnější devlog na světě.

**Souvislosti:** [Žrouti času](produktivita.md) · [Devlogy](devlogy.md) · [Zápisek: Devlog jako mapa](../zapisky/devlog-jako-mapa.md) · [Zápisek: Pravidlo 70/30](../zapisky/pravidlo-70-30.md)

---

## Devět chytrých nápadů, které žerou čas

**Zdroj:** [7 Programming myths that waste your time](https://www.youtube.com/watch?v=niWpfRyvs2U) · [Fireship](https://www.youtube.com/channel/UCsBjURrPoezykLs9EqgamOA) · ~6 min, esej

**Shrnutí:** Autor otevírá přiznáním, které dává celému videu váhu: *„většinu dospělého života jsem psal kód — a většina toho kódu je úplný odpad. Nikdy nespatřil produkční server."* A z toho vyvozuje seznam věcí, které **působí produktivně a nikam nevedou**. Háček, který spojuje všech devět: **každá z nich je dobrá rada dovedená za bod, kde přestala platit.**

### Rozpad myšlenky

**1. Nejnovější technologie** [(0:47)](https://www.youtube.com/watch?v=niWpfRyvs2U&t=47s). Lákadlem je FOMO; realita je, že *„většina skutečného světa, kde jsou práce, svůj dinosauří stack jen tak nezmění."* PHP pořád pohání většinu webu, Java podnikový svět, většina databází je SQL. Jeho vlastní příklad selhání: nadšeně přijal novou databázi od bývalých inženýrů Twitteru, firma zkrachovala a servery zhasly — *„byl bys na tom mnohem líp s nudnou SQL databází."*

**2. Programátorské dogma** [(1:33)](https://www.youtube.com/watch?v=niWpfRyvs2U&t=93s). Objektoví puristé, funkcionální extremisté. *„Byl jsem členem obou kultů a hodně jsem se od nich naučil, ale zasvětit život jen jednomu z nich je ztráta času."* Konkrétní vzpomínka: v roce 2018 se ohýbal, aby všechno napsal funkcionálně (*„používals-li třídy, byl jsi doslova Hitler"*), a o pár let později zjistil, že třídy jsou docela užitečné.

**3. Clean code dovedený příliš daleko** [(3:06)](https://www.youtube.com/watch?v=niWpfRyvs2U&t=186s) je nejcennější položka. Většina rad z té knihy je dobrá (smysluplná jména, malé funkce, konzistentní formátování). Problém je **DRY** hnané do konce: *„skončíš s nekonečnou vrstvou obalů, rozhraní a zbytečné indirekce. Je to paralýza z analýzy a strávíš víc času refaktorováním než stavěním funkcí, které někdo chce."* A jeho protinávrh, který se dobře pamatuje: **RUG — repeat until good.** Duplikuj zpočátku a **abstrahuj až ve chvíli, kdy je to opakování otravné.**

**4. Stoprocentní pokrytí testy.** *„Vysoké pokrytí se nerovná vysoká kvalita."* Optimalizace na číslo vede k testům, které se jen dotknou řádků a nechytí skutečné chyby — a horší než ztracený čas je **falešný pocit bezpečí**. Navrch pomalejší CI. *„U pokrytí rozhoduje kvalita, ne kvantita."*

**5. a 6. Předčasná optimalizace a předčasná infrastruktura.** *„Mnohem důležitější je zajistit, že je kód správně, a optimalizovat až ve chvíli, kdy je bolestivě zřejmé, že v produkci stojí za nic."* A totéž o cloudu: *„myslel jsem, že potřebuju serverless mikroslužby s globálním shardingem a edge cachingem — ukázalo se, že jeden malý VPS je pro mých pět uživatelů úplně v pořádku."*

**7. Přehnané spolehnutí na AI** [(4:38)](https://www.youtube.com/watch?v=niWpfRyvs2U&t=278s). Formuluje to jako paradox, ne jako odmítnutí: **jsou to největší zrychlovače, jaké kdy viděl, a při špatném použití největší žrouti času.** Konkrétní past: požádáš o jednoduchý web a dostaneš nový JavaScriptový framework napsaný od nuly — *„a protože jsi zapomněl psát kód, prostě to schválíš a jdeš dál."*

> **Pozn.:** Ten seznam má společného jmenovatele, který autor neřekne přímo a stojí za vytažení: **všechny ty myty jsou způsoby, jak si vyrobit pocit postupu bez postupu.** Refaktorovat, zvyšovat pokrytí, migrovat na novější framework, ladit výkon — to všechno **vypadá jako práce, je to měřitelné a nikdo tě za to nekritizuje**, na rozdíl od psaní funkce, u které nevíš, jestli bude dobrá. Odtud praktický test, který se dá použít na sebe: **kdy jsem naposledy dodal něco, co uživatel poznal?** Nejcennější jednotlivost je **RUG**, protože je to jediná z těch rad, která nabízí náhradní pravidlo místo varování — a je použitelná i v gamedevu, kde se DRY láme obzvlášť často: dvě podobné mechaniky se sjednocují **až potřetí**, ne podruhé. Souvisí to s [premature optimization](../rejstrik.md#premature-optimization) i s [pravidlem 70/30](../zapisky/pravidlo-70-30.md).

**Souvislosti:** [Patnáct malých návyků, tři mechanismy](#patnact-malych-navyku-tri-mechanismy) · [Design patterns](design-patterns.md) · [Programátorské myšlení](programatorske-mysleni.md) · [Učení v éře AI](uceni-v-ere-ai.md#novy-programovaci-jazyk-se-jmenuje-srozumitelnost) · [Rejstřík: Premature optimization](../rejstrik.md#premature-optimization) · [Rejstřík: Separation of concerns](../rejstrik.md#separation-of-concerns)
