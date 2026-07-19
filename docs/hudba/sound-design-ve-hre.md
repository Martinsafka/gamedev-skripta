# Sound design ve hře

Zvuk se ve hře snadno přehlíží — dokud nechybí. Přitom i jediný zvuk umí nastavit náladu scény a jasný zvukový feedback drží celou hratelnost pohromadě. Tahle kapitola slučuje dva pohledy: profesionální rámec od Riotu (na co zvuk ve hře je a jaké má nástroje) a indie filozofii Marshalla McGeeho (proč nejlepší herní zvuk často vzniká *ubíráním*, ne přidáváním).

Praktickou implementaci v enginu (physical materials, MetaSounds, kroky) najdeš v [Kroky a povrchy](../praxe/footsteps.md); tady jde o principy.

---

## Tři úkoly herního zvuku

**Zdroj:** [So You Wanna Make Games?? | Episode 8: Sound Design](https://www.youtube.com/watch?v=KcorIwJscFA) · [Riot Games](https://www.youtube.com/channel/UCJEGvSZnQ1pkVfHO8s5G8hA) · ~15 min, tutoriál

**Shrnutí:** Herní zvuk dělá tři konkrétní věci: dává **cues** (co se děje se mnou a kolem mě), dává **feedback** (bylo moje rozhodnutí dobré, nebo špatné) a nese **emoci** (táhne tě do zážitku). Když navrhuješ zvuk, ptej se, který z těch tří úkolů zrovna plní — jinak přidáváš ruch.

### Rozpad myšlenky

Tři role rozdělené podle účelu [(1:07)](https://www.youtube.com/watch?v=KcorIwJscFA&t=67s):

- **Cues** [(1:53)](https://www.youtube.com/watch?v=KcorIwJscFA&t=113s) — zvuk zpřehledňuje, co se děje: je schopnost nabitá? bereš poškození? spatřil tě nepřítel? Informace uchem, kterou nemusíš číst očima z UI.
- **Feedback** [(2:18)](https://www.youtube.com/watch?v=KcorIwJscFA&t=138s) — zvuk potvrzuje hráčova rozhodnutí, dobrá i špatná. Je to jeden z nejsilnějších kanálů, jak hráči říct „ano, tohle fungovalo" bez jediného slova.
- **Emoce** [(2:36)](https://www.youtube.com/watch?v=KcorIwJscFA&t=156s) — zvuk je jádrový emoční tahoun: bezútěšná atmosféra *Papers, Please*, děsivý krok pronásledovatele v *Outlast*. Nálada scény často stojí a padá se zvukem víc než s obrazem.

Pro herní hudbu z toho plyne to samé co pro efekty: než něco přidáš, urči úkol. Bojová hudba je emoce a cue zároveň (spustí se při vstupu do soubuje); zvuk sebrání předmětu je feedback. Zvuk bez úkolu je jen hluk.

**Souvislosti:** [Slovník sound designera](#slovnik-sound-designera) · [Herní art: tři úkoly artu](../teorie/art-pipeline.md#art-ma-tri-ukoly-clarity-satisfaction-style) *(tentýž rámec z téže série, aplikovaný na obraz)* · [Fyzika souzvuku: disonance jako emoce](fyzika-souzvuku.md#jine-alikvoty-jine-stupnice) · [Game feel a imerze](../teorie/game-feel.md) · [Kroky a povrchy](../praxe/footsteps.md)

---

## Slovník sound designera

**Zdroj:** [So You Wanna Make Games?? | Episode 8: Sound Design](https://www.youtube.com/watch?v=KcorIwJscFA) · [Riot Games](https://www.youtube.com/channel/UCJEGvSZnQ1pkVfHO8s5G8hA) · ~15 min, tutoriál

**Shrnutí:** Abys o zvuku mohl přemýšlet a mluvit, hodí se pět pojmů: **frekvence**, **envelope (ADSR)**, **attenuation**, **EQ** a **reverb**. Nejsou to abstrakce — každý je páka, kterou zvuku měníš charakter i funkci ve hře.

### Rozpad myšlenky

- **Frekvence** [(3:48)](https://www.youtube.com/watch?v=KcorIwJscFA&t=228s) — jako spektrum barev: pomalé kmitání = nízký tón, rychlé = vysoký. Reálný zvuk obsazuje celé pásmo frekvencí, ne jednu.
- **Envelope / ADSR** [(4:59)](https://www.youtube.com/watch?v=KcorIwJscFA&t=299s) — vizualizace zvuku od začátku do konce: attack, decay, sustain, release. Prodloužíš-li attack úderu, získáš víc anticipace; prodloužíš-li release, zní, jako by prorazil zeď. (Je to týž ADSR jako v [syntéze zvuku](synteza-zvuku.md#amp-controlled-zvuky-a-bas) — jen aplikovaný na zvukový efekt místo na notu.)
- **Attenuation** [(6:36)](https://www.youtube.com/watch?v=KcorIwJscFA&t=396s) — útlum se vzdáleností. Ve hrách často vizualizovaný ve stealth UI. Chytrý trik: dej vysokým frekvencím krátký útlum a nízkým dlouhý — zblízka je výstřel ostrý, z dálky jen temné dunění. Jeden zvuk, různý útlum podle frekvence.
- **EQ (equalizace)** [(8:08)](https://www.youtube.com/watch?v=KcorIwJscFA&t=488s) — zesílení nebo potlačení konkrétních frekvencí: čištění šumu, zvýraznění či ztlumení tónů.
- **Reverb** [(8:57)](https://www.youtube.com/watch?v=KcorIwJscFA&t=537s) — odraz zvuku od prostředí. Slouží dvěma věcem: **slepit** zvuky dohromady, nebo **vyjádřit prostor** (chodba, koupelna, kaňon).

To celé se pak **navěsí na herní události** [(9:45)](https://www.youtube.com/watch?v=KcorIwJscFA&t=585s): postava vstoupí do vody, začne souboj, spící nepřítel vyletí do vzduchu. A co knihovny nepokryjí, vyrobíš ve **foley** — Riot pro postavu Iverna sroubil „The Creaker" ze dvou prken, dvou pantů a provazu [(11:02)](https://www.youtube.com/watch?v=KcorIwJscFA&t=662s), aby vrzání dodalo napětí před prasknutím štítu.

**Souvislosti:** [Tři úkoly herního zvuku](#tri-ukoly-herniho-zvuku) · [Syntéza zvuku: ADSR](synteza-zvuku.md#amp-controlled-zvuky-a-bas) · [Kroky a povrchy](../praxe/footsteps.md) · [Rejstřík: attenuation](../rejstrik.md#attenuation) · [Rejstřík: EQ](../rejstrik.md#eq) · [Rejstřík: reverb](../rejstrik.md#reverb) · [Rejstřík: foley](../rejstrik.md#foley)

---

## Nepředesignovat: méně je víc

**Zdroj:** [Why Indie Games Always Seem To Have The Best Sound Design](https://www.youtube.com/watch?v=VJ6ENLakB2g) · [Marshall McGee](https://www.youtube.com/channel/UCIoNgwHpavUi2UnC68cKgbw) · ~10 min, esej

**Shrnutí:** Nejčastější chyba není málo dovednosti, ale **přílišná snaha**. Zkušenější sound designer má nutkání předvést každý trik, který umí — a přesně to zvuk zabíjí. Nejlepší indie zvuky jsou minimalistické a interaktivní: pár prvků správně, s náhodou v pitchi, ne knihovna navrstvená na jeden úder.

### Rozpad myšlenky

Autorova klíčová lekce zní **nepředesignovat** [(3:20)](https://www.youtube.com/watch?v=VJ6ENLakB2g&t=200s). Krumpáč ve Stardew Valley by nováček nejspíš udělal líp než ostřílený designer, protože ostřílený začne hledat „zvuky krumpáče" v knihovně, přidávat pády kamení a praskání — a nic z toho nepomáhá. Ten zvuk potřebuje jen dva prvky: **nízký thump** (podprahově říká „tohle má váhu a stojí to energii") a **materiálový zvuk kamene** (říká, co těžíš). Nemusí to znít jako krumpáč vůbec.

Druhý trik proti mechaničnosti: **náhodná variace pitche** [(2:48)](https://www.youtube.com/watch?v=VJ6ENLakB2g&t=168s). Zvuk sebrání předmětu ve Stardew je jen mlasknutí pusou — ale s náhodným posunem výšky přestane znít digitálně a otravně a začne být hravý. Často je *způsob implementace* (náhodný pitch) důležitější než samotný zvuk.

A proč zrovna indie [(0:04)](https://www.youtube.com/watch?v=VJ6ENLakB2g&t=4s): v malých hrách je interakce jádrem, ne položkou v menu. V *Potion Craft* fyzicky mícháš ingredience a každý krok zní — vzniknou krásné zvukové momenty, které velká hra schová do „klikni v menu" (tentýž recept v *Tears of the Kingdom* přehraje pokaždé jeden a týž zvuk). Interaktivita je půda, na které dobrý zvuk roste.

> **Pozn.:** Tohle je přímý příbuzný „nepředesignuj" z herního designu vůbec — leštit jen to, co sytí hlavní fantazii. Tady: víc vrstev ≠ lepší zvuk. Umět *ubrat* a *nechat jeden zvuk dýchat s náhodou* je těžší dovednost než navršit deset vrstev.

**Souvislosti:** [Hledej správný zvuk a cti styl](#hledej-spravny-zvuk-a-cti-styl) · [Game feel a imerze](../teorie/game-feel.md) · [Rejstřík: random pitch variation](../rejstrik.md#random-pitch-variation)

---

## Hledej správný zvuk a cti styl

**Zdroj:** [Why Indie Games Always Seem To Have The Best Sound Design](https://www.youtube.com/watch?v=VJ6ENLakB2g) · [Marshall McGee](https://www.youtube.com/channel/UCIoNgwHpavUi2UnC68cKgbw) · ~10 min, esej

**Shrnutí:** Dvě dovednosti, které odlišují dobrý herní zvuk: umět **hledat ten správný zvuk** (ne první nalezený) a **ctít výtvarný styl** hry, aby zvuk vyvolával tentýž pocit jako obraz. Práce sound designera je z velké části podpořit to, co udělali výtvarníci.

### Rozpad myšlenky

**Hledání je často nejdůležitější krok** [(6:20)](https://www.youtube.com/watch?v=VJ6ENLakB2g&t=380s). Hra *Dredge* (hororový rybaření) nevybírá jen dobré zvuky, ale jejich *nejděsivější verze*: řetěz, který zní zrezivěle a nepravidelně; rybářský vlasec napjatý těsně před prasknutím. Když hledáš „zvuk deště", věnuj těch pár minut navíc a projdi desítky variant, než najdeš tu se správnou náladou.

**Cti výtvarný styl** [(7:10)](https://www.youtube.com/watch?v=VJ6ENLakB2g&t=430s). V *Tunic* je grafika rigidní a geometrická, ale zároveň přírodní — a zvuk to zrcadlí: děsivá dávná technologie stojí na syntéze a bitcrushingu, magické a přírodní prvky na bohatých ambientních zvucích. Autor jde tak daleko, že „dobrý zvuk dělá grafiku lepší". Ve většině případů zvuk přichází *až po* obrazu a jeho úkolem je podpořit práci výtvarníků, animátorů a programátorů co nejlíp.

> **Pozn.:** „Cti styl" je zvuková obdoba percepčních hranic z designu — dojem vzniká souladem smyslů. Pro herní hudbu i efekty platí: nejdřív si pojmenuj, jaký *pocit* má scéna vyvolávat (a jaký má výtvarný jazyk), a teprv pak vybírej zvuky, které ten pocit zrcadlí. Disonance a syntéza pro hrůzu, čisté alikvóty a akustické nástroje pro klid — viz [fyzika souzvuku](fyzika-souzvuku.md#jine-alikvoty-jine-stupnice).

**Souvislosti:** [Nepředesignovat: méně je víc](#nepredesignovat-mene-je-vic) · [Fyzika souzvuku](fyzika-souzvuku.md#jine-alikvoty-jine-stupnice) · [Tvorba herního soundtracku](tvorba-soundtracku.md) (leitmotiv jako emoční pojivo) · [Game feel a imerze](../teorie/game-feel.md)

---

## Attenuation v praxi: zvuk, který má místo

**Zdroj:** [How to Make a 3D Sound in Unreal Engine 5](https://www.youtube.com/watch?v=dttUv6--1nA) · [Gorka Games](https://www.youtube.com/channel/UCv_n9oioNF6OpzR2dt6E4xg) · ~4 min, tutoriál

**Shrnutí:** [Slovník sound designera](#slovnik-sound-designera) zavádí attenuation jako pojem — útlum se vzdáleností. Tohle je jeho mechanická polovina v Unrealu, a je krátká: **attenuation není nastavení zvuku, ale samostatný asset**, který se zvukům přiřazuje. Dokud ho nepřiřadíš, hraje všechno stejně hlasitě odkudkoli — a to je nejčastější důvod, proč zvuk ve hře „nemá místo".

### Rozpad myšlenky

**Asset, ne parametr** [(0:02)](https://www.youtube.com/watch?v=dttUv6--1nA&t=2s): vytvoří se **Sound Attenuation** asset, ve kterém se nastavuje dosah, náběh útlumu a **tvar křivky (attenuation function)** — autor volí *Natural Sound*, tedy průběh odpovídající tomu, jak hlasitost klesá ve skutečnosti. Že je to samostatný asset, má praktický důsledek: **jeden dosah se sdílí mezi mnoha zvuky** a mění se na jednom místě, přesně jako [master material](../praxe/materialy.md#master-material-pet-textur-nema-mit-kazdy-mesh) u textur.

**Zvuk umístěný v levelu** [(0:49)](https://www.youtube.com/watch?v=dttUv6--1nA&t=49s): audio soubor se přetáhne do scény a v jeho **Attenuation Settings** se vybere vytvořený asset. Editor pak dosah rovnou **vykreslí jako kouli** — což je ta nejužitečnější drobnost z celého videa, protože slyšitelnost se najednou dá **rozvrhnout očima jako cokoli jiného v levelu**.

**Zvuk spuštěný z blueprintu** [(1:49)](https://www.youtube.com/watch?v=dttUv6--1nA&t=109s) má vlastní past. Existují dva různé uzly — **Play Sound 2D** a **Play Sound at Location** — a i ten druhý hraje bez přiřazené attenuation všude stejně: autor to demonstruje tak, že se od místa spuštění vzdaluje a hlasitost se nemění [(2:35)](https://www.youtube.com/watch?v=dttUv6--1nA&t=155s). Teprve po dosazení attenuation assetu do parametru uzlu začne zvuk **patřit místu**.

> **Pozn.:** Video je z roku 2022 a je to nejzákladnější možný průchod — moderní UE má pro zvuk podstatně bohatší nástroje ([MetaSounds](../praxe/footsteps.md), spatializace, occlusion, submixy) a u větší hry se attenuation nastavuje spíš v Sound Cue nebo přímo v MetaSoundu. Základní model ale platí dál a stojí za zapamatování hlavně proto, že **spojuje teorii z předchozí myšlenky s tím, kde se to v enginu skutečně nastavuje**. Za doladění stojí jedna věc, kterou tutoriál nezmiňuje: samotný útlum hlasitosti nestačí — **vzdálený zvuk má být i tlumenější ve výškách**, jinak zní jako blízký zvuk ztlumený knoflíkem. Přesně o tom mluví frekvenčně závislý trik ve [slovníku](#slovnik-sound-designera).

**Souvislosti:** [Slovník sound designera](#slovnik-sound-designera) *(attenuation jako pojem)* · [Kroky a povrchy: MetaSounds](../praxe/footsteps.md) · [Tři úkoly herního zvuku](#tri-ukoly-herniho-zvuku) · [Rejstřík: attenuation](../rejstrik.md#attenuation) · [Rejstřík: Sound Cue](../rejstrik.md#sound-cue)
