# Persistence a hydratace: svět, který si pamatuje

Dvě témata, která spolu na první pohled nesouvisejí a v praxi se nedají oddělit. **Persistence** je ukládání stavu světa tak, aby přežil — buď mezi sezeními, nebo jen mezi tím, než se kus mapy odloží z paměti a zase načte. **Hydratace** je držení víc úrovní detailu pro tytéž interaktivní objekty: z instance se stane aktér, když k němu hráč dojde, a zpátky, když odejde.

Souvisejí proto, že **volba reprezentace určuje, jak se ta věc ukládá**. Aktér, instance actor a mass entita se ukládají každý jinak — a kdo si vybere podle výkonu a na ukládání pomyslí až potom, přepisuje.

Nadřazená kapitola bloku je [Velké světy](velke-svety.md); tohle je její gameplay strana.

---

## Zůstanou ty dveře otevřené? Záleží na garbage collectoru

**Zdroj:** [The Player Was Here: Persisting World State and Actor LOD Systems](https://www.youtube.com/watch?v=KBn62trwkLw) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~49 min, Unreal Fest Chicago 2026 (Epic, technical developer relations — gameplay systémy)

**Shrnutí:** Přednášející položí sálu kvíz: otevřu dveře, odejdu tak daleko, že se ta část mapy odstreamuje, vrátím se — budou ty dveře pořád otevřené? Většina sálu hlasuje pro „zavřené". Správná odpověď je **záleží** — konkrétně na tom, jestli mezitím proběhl garbage collector. Háček, kvůli kterému to není jen kuriozita: **z toho plyne, že aktéři mohou začínat a končit hru vícekrát**, a kdo o tom neví, píše `BeginPlay`, který se chová nespolehlivě.

### Rozpad myšlenky

**Ta demonstrace** [(6:15)](https://www.youtube.com/watch?v=KBn62trwkLw&t=375s) je nejlepší část celé přednášky, protože je nezapomenutelná: rychle sem a tam — **dveře zůstanou otevřené**. Ručně spustí garbage collection, jde znovu — **dveře jsou zavřené**.

**Co se za tím děje** [(7:01)](https://www.youtube.com/watch?v=KBn62trwkLw&t=421s): odstreamuje-li se level z world partition, mohou nastat dvě věci. Buď je objekt levelu i s aktéry **pořád v paměti** a při návratu se **znovu použije** — a pak si drží stav. Nebo mezitím proběhl garbage collector, level se načte z disku a všechno má **výchozí hodnoty**.

Z toho plynou dva důsledky. První je čistě programátorský a je vážnější, než vypadá: **aktéři a jejich komponenty mohou projít `BeginPlay` a `EndPlay` opakovaně.** Kdo v `BeginPlay` něco vytváří, dostane crash nebo spawner, který spawnuje dvakrát. Existují konzolové proměnné, které to chování trochu ovlivní, ale *„tohle je realita, se kterou se musí počítat."*

Druhý je návrhový a je to věta, kvůli které tahle myšlenka v knihovně je: *„používáš-li world partition, měl bys o persistenci přemýšlet, i když ve hře nemáš tlačítko uložit."*

> **Pozn.:** Tenhle kvíz je vzácně dobrý didaktický nástroj, protože **celý sál odpoví špatně a přitom to všichni znají** — nedeterministické chování se nedá odhalit hraním, protože se v půlce případů chová „správně". A přesně proto je to nejnepříjemnější druh chyby: **projeví se náhodně, u testera, kterému mezitím sedl GC.** Obecné pravidlo, které z toho plyne a platí i mimo Unreal: **stav, který přežívá jen díky tomu, že se ho nikdo nedotkl, není uložený stav.** Souvisí to přímo s [persistence key](../rejstrik.md#persistence-key) — tam je to popsané jazykem designu (nepřítel obživne, když se vrátíš), tady jazykem enginu. A jedna vlastní poznámka: nejlevnější obrana je **testovat s vynucenou garbage collection** (`gc.CollectGarbageEveryFrame 1`), protože pak se ten „záleží" scénář změní na deterministický a chyby vyplavou hned. Táž technika, jakou používá [hledání memory leaků](gpu-pruchod.md#hodina-v-cizi-scene-co-se-najde-kdyz-se-hleda) — vynutit si nepříjemný stav, aby se dal měřit.

**Souvislosti:** [Ukládání obecně](#ukladani-obecne-identita-stav-a-verze) · [Hydratace](#hydratace-instance-actory-a-mass) · [Ukládání](ukladani.md) · [Levely a streaming](levely-a-streaming.md#open-level-zamrzne-hru-streaming-ji-drzi-zivou) · [Rejstřík: Persistence key](../rejstrik.md#persistence-key) · [Rejstřík: Garbage collection](../rejstrik.md#garbage-collection) · [Rejstřík: World Partition](../rejstrik.md#world-partition)

---

## Ukládání obecně: identita, stav a verze

**Zdroj:** [The Player Was Here: Persisting World State and Actor LOD Systems](https://www.youtube.com/watch?v=KBn62trwkLw) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~49 min, Unreal Fest Chicago 2026

**Shrnutí:** Bool pro jedny dveře funguje. Seznam otevřených dveří taky. Ale jakmile má hra desítky tříd s vlastním stavem, potřebuješ postup, který **nevyžaduje sáhnout do save třídy pokaždé znovu**. Kapitola je ten postup rozložený na tři otázky: **jak objekt poznat, jak uložit jeho stav a jak přežít změnu verze.** Háček, na kterém se to nejčastěji láme: **verzi si musíš uložit sám** — v uloženém stavu není.

### Rozpad myšlenky

**Identita: jak objekt poznat příště** [(9:24)](https://www.youtube.com/watch?v=KBn62trwkLw&t=564s). Tři možnosti a každá má cenu:

| co použít | výhoda | cena |
|---|---|---|
| **path name objektu** | stabilní mezi sezeními téhož buildu | **mění se mezi verzemi hry** — hlavně když aktéra posuneš do jiné streamovací buňky |
| **actor GUID** | přidělí ho editor a nemění se | existuje jen v editoru; některá studia si ho **vystaví i do zabalené hry** |
| vlastní tag či jméno | plná kontrola nad stabilitou | víc práce, náchylnější k chybám — chce to nástroje |

**Stav: dvě cesty** [(10:10)](https://www.youtube.com/watch?v=KBn62trwkLw&t=610s). První je **specifikátor `SaveGame`** na vlastnostech (v blueprintu zaškrtávátko) plus archiv, který objekt serializuje do pole bajtů. Výhoda je, že ten výstup je **jen binární data**, takže jedna save třída zvládne libovolný typ objektu — a je v tom zabudovaná zpětná kompatibilita, protože se ukládají jména a typy vlastností, takže se změněná nebo zmizelá vlastnost přeskočí. Nevýhody: **na enginové vlastnosti (třeba scene component) to nejde bez zásahu do zdrojáků enginu**, metadata něco stojí a **nedá se do toho podívat**, dokud to nedeserializuješ zpátky.

Druhá je **napsat si serializaci sám**: víc kontroly a efektivnější (víš-li, že postava má jen zdraví a pár tagů, napíšeš je bez metadat) — ale zpětná kompatibilita je pak na tobě.

**Verzování a past, kterou přednášející jmenuje výslovně** [(12:28)](https://www.youtube.com/watch?v=KBn62trwkLw&t=748s). Engine má **custom version**: k archivu se dají připojit čísla verzí, každé pod vlastním GUID, a při načtení podle nich přeskočíš nebo povýšíš data. *„Co je velmi důležité vědět: ta čísla verzí musíš sám vytáhnout a uložit, protože nejsou součástí té binární zprávy."* A dodá, proč to říká: *„někteří lidé si prostě vezmou payload a za pár měsíců zjistí, že nemají informaci o verzi."* Hlavička se dá napsat jednou pro víc objektů.

A druhá věc, na kterou se u velkých map nemyslí: **různé části uložených dat mohou být z různých verzí.** Hráč mohl jednu oblast navštívit v poslední verzi a jinou před třemi.

**Kdy to dělat: životní cykly** [(14:01)](https://www.youtube.com/watch?v=KBn62trwkLw&t=841s). Engine má sadu delegátů, které přesně odpovídají potřebným okamžikům:

- **`OnActorsInitialized`** a **`OnWorldBeginPlay`** — dřív, než aktéři v persistentním levelu začnou hrát; ideální chvíle na obnovu.
- **`OnLevelBeginMakingVisible`** — u streamovaných levelů, taky před `BeginPlay` (a ten pak proběhne rozprostřený do víc snímků).
- **`OnWorldBeginTearDown`** — poslední šance uložit při změně mapy nebo ukončení.

**Hotové řešení a jeho poctivý stav** [(17:10)](https://www.youtube.com/watch?v=KBn62trwkLw&t=1030s): **Level Stream Persistence plugin** (od 5.3) hlídá zvolené třídy a jejich vlastnosti sám — označíš je v nastavení projektu a on dělá záznamy při načtení a obnovu při streamování. Umí i respawn zvolených tříd včetně transformu. Jenže: *„je vysoce experimentální, což znamená, že se nepoužívá v žádném titulu Epicu"* a *„nepracujeme na něm už. Berte to jako referenci, ne jako produkční řešení."* Ke známým hranám patří, že **komponenty přidané v blueprintu** (hierarchie i construction script) dostanou hodnoty **až po `BeginPlay`**, takže se pro ně musí použít hák *post restore*, a že respawn dělá všechno **v jednom snímku** — kdo řeší výkon, musí si dopsat rozprostření.

> **Pozn.:** Nejcennější je tady ta trojice **identita → stav → verze**, protože je to úplný seznam a dá se použít jako kontrolní. Většina domácích ukládacích systémů má první dva a na třetí přijde až ve chvíli, kdy uživatelům praskají uložené hry — a to je v tu chvíli neopravitelné zpětně. Nejpřenositelnější varování je proto to o **hlavičce, kterou si musíš uložit sám**: je to přesně ten druh věci, která [selže mlčky](pamet-a-instance.md#drobky-sest-zasahu-na-jedno-odpoledne) a projeví se za měsíce. Vlastní doplněk k tabulce identit: **path name je zrádný právě u velkých světů**, protože ve world partition se cesta odvíjí od streamovací buňky — takže posun aktéra o pár metrů může přepsat jeho identitu. U hry, která bude vycházet v aktualizacích, je tohle argument pro vlastní stabilní klíč, i když je to víc práce. A stojí za ocenění, že přednášející o vlastním enginovém pluginu **řekne nahlas, že se na něm nepracuje** — to je informace, kterou by dokumentace nedala.

**Souvislosti:** [Zůstanou ty dveře otevřené?](#zustanou-ty-dvere-otevrene-zalezi-na-garbage-collectoru) · [Hydratace](#hydratace-instance-actory-a-mass) · [Ukládání](ukladani.md) · [Godot: persistence key](../godot/pripadovka-level-a-mapa.md#persistence-key-svet-ktery-si-pamatuje) · [Rejstřík: SaveGame objekt](../rejstrik.md#savegame-objekt) · [Rejstřík: Persistence key](../rejstrik.md#persistence-key) · [Inventář: stav cestuje jako data](inventar.md#kdyz-stav-opousti-inventar-cestuje-jako-data-ne-jako-objekt) *(totéž v malém: zahozená položka)*

---

## Hydratace: instance actory a mass

**Zdroj:** [The Player Was Here: Persisting World State and Actor LOD Systems](https://www.youtube.com/watch?v=KBn62trwkLw) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~49 min, Unreal Fest Chicago 2026

**Shrnutí:** Aktér je drahý na načtení i na paměť. Instance actor je levný, ale nic neumí. Hydratace je přepínání mezi tím: **v dálce instance, u hráče plnohodnotný aktér** — a když od něj odejdeš, zase zpátky. Přednášející k tomu dá čísla ze skutečného měření a jeden recept, který stojí za zapamatování. Háček, který mění pořadí rozhodování: **jak se ta věc ukládá, závisí na tom, čím právě je.**

### Rozpad myšlenky

**Co to je a odkud** [(33:08)](https://www.youtube.com/watch?v=KBn62trwkLw&t=1988s): plugin **Instance Actors** přišel v 5.4, je pořád značený jako experimentální — *„ale používáme ho už dlouho v našich Lego Fortnite hrách"*, hlavně na sběrná místa a ničitelné objekty se známou pozicí. Vybrané třídy se označí jako instancovatelné, umístí ručně, runtime cell transformerem nebo přes PCG; v dálce se kreslí jako **ISM komponenty** a při přiblížení se **hydratují na aktéry**.

**Čísla, kvůli kterým to stojí za práci** [(35:30)](https://www.youtube.com/watch?v=KBn62trwkLw&t=2130s). Důvod je strukturní: data instance actorů se cookují jako **další transformy pro nějakého vzorového aktéra** — každá instance je jen transform, ne objekt a ne komponenta. Důsledek: kratší asynchronní načítání, míň práce na herním vlákně, míň práce na fyzikálním vlákně (je to jedna ISM komponenta, ne tisíc scene komponent). Naměřený rozdíl: **streamování levelu s tisícem aktérů proti tisíci instancím bylo asi pětkrát rychlejší** včetně navazujících úloh. S výhradou, kterou sám dodá: *„nedívejte se na absolutní čísla, dívejte se na poměr"* a záleží, jak moc se ta věc opakuje.

**Recept, který je na celé myšlence nejcennější** [(37:03)](https://www.youtube.com/watch?v=KBn62trwkLw&t=2223s): věc může začít jako instance actor a v určitou chvíli ji herní kód **vyhodí ze systému** (*eject*) — a od té chvíle je to natrvalo aktér. *„Chceš něco, co je levné na načtení, ale pořád pohyblivé nebo hodně interaktivní."* Ukázka: bedna je instance actor, dehydratuje a hydratuje se, jak kolem ní chodíš — a když jí spadne zdraví na nulu, rozpadne se jako geometry collection a **od té chvíle ji ukládá plugin na persistenci aktérů**.

**A pak ta věc, která určuje pořadí rozhodování**: každá z těch tří reprezentací se ukládá jinak.

- **Aktéři** — přes záznamy vlastností a případný respawn (viz [předchozí myšlenka](#ukladani-obecne-identita-stav-a-verze)).
- **Instance actory** — data se obnovují **do datového objektu manageru**, ne do entit. Důvody jsou dva a oba věcné: datový objekt **existuje už při načtení** (je cookovaný), zatímco mass entity vznikají odloženě a rozprostřeně — a **objekty umí replikovat, mass entity ne**. Právě přes ten datový objekt Lego Fortnite replikuje, které instance jsou zničené a v jakém jsou vizuálním stavu.
- **Mass entity** — ukládají se dotazem přes fragment, který se entitě přidá opt-in vlastností. Časování je choulostivé: **nesmíš sahat na data fragmentu, když běží mass procesor**, takže se poslouchá na konec zpracování snímku. (V 5.8 se to zjednodušilo, protože procesory využívají i herní vlákno.)

**Praktická drobnost, která se snadno přehlédne**: je-li věc zrovna hydratovaná jako aktér, může být **stav aktéra novější než stav entity** — takže se před uložením vyplatí vyvolat událost, na kterou si aktéři svá data doplní.

> **Pozn.:** Nejdůležitější věc téhle myšlenky je **pořadí rozhodování**: reprezentace (aktér / instance / entita) se vybírá kvůli výkonu, ale **rozhoduje o ukládání** — a kdo ji změní v půlce projektu, přepisuje persistenci. Proto ta přednáška obě témata spojuje, i když by se dala vyprávět zvlášť. Za pozornost stojí i recept s *eject*: je to elegantní řešení rozporu „levné na načtení" proti „interaktivní", protože **objekt nemusí být jednou provždy jedním nebo druhým** — přejde jednosměrně ve chvíli, kdy se z kulisy stane součást příběhu hráče. Godotí analogií je [persistence key](../godot/pripadovka-level-a-mapa.md#persistence-key-svet-ktery-si-pamatuje), jen postavená obráceně: tam se pamatuje **změna** mimo objekt, tady se objekt **povýší** a začne se pamatovat sám. Vlastní výhrada: obojí roste. Taška na klíče i seznam vyhozených instancí se v dlouhé hře plní, takže i tady platí, že se musí rozhodnout, **co se do ní vůbec pouští**.

**Souvislosti:** [Ukládání obecně](#ukladani-obecne-identita-stav-a-verze) · [Instanced Actors](instanced-actors.md#swap-podle-vzdalenosti-setup-pres-data-registry) · [Velké světy: odložit místo zlevnit](velke-svety.md#odlozit-misto-zlevnit-skorapka-prvni-interier-na-vyzadani) · [Paměť a instancování: ISM](pamet-a-instance.md#ism-hism-a-merge-draw-cally-podle-geometrie) · [Rejstřík: Instanced Actors](../rejstrik.md#instanced-actors) · [Rejstřík: Mass Entity](../rejstrik.md#mass-entity) · [Rejstřík: Hydratace](../rejstrik.md#hydratace) · [Mass a ECS: jedna implementace místo dvou](mass-ecs.md#jak-s-mass-pracovat-diagram-debugger-a-jedna-implementace-misto-dvou) *(protiargument týmu Mass: hydratace zdvojí vývoj)*
