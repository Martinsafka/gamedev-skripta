# Blockout: polovina projektu, kterou hráč nikdy neuvidí

Blockout je fáze, kdy scéna stojí z jednoduchých tvarů, ještě než přijde art a světlo. Rozhoduje se v ní, jestli prostředí funguje: jestli se dá číst, jestli sedí měřítko a jestli hráč ví, kam jít. Kapitola ho bere z pohledu environment artisty. První myšlenka je o tom, jak blockout myslet (zastav, omez, porovnej), druhá o tom, jak ho dotáhnout dál přes hodnoty a barvu, než vznikne první materiál. Procesní stránku z pohledu level designu, tedy graybox, beautiful corner a první level nakonec, najdeš v [Level designu pro sólo vývojáře](../teorie/level-design-solo.md#graybox-beautiful-corners-a-prvni-level-nakonec). Tvarový jazyk a šerosvit rozebírá [Stavba prostředí](env-tvorba.md#nejdriv-tvary-design-language-a-chiaroscuro) a co se z blockoutu stane potom, [Modulární kity](modularni-kity.md).

---

## Zastav, omez, porovnej: blockout, který se dá přečíst

**Zdroj:** [BLOCKOUT de Escenarios para Videojuegos](https://www.youtube.com/watch?v=VxTQhSr1sbw) · [JaviSkau | Senior Environment Artist](https://www.youtube.com/channel/UCcASeAskcSTPLHo3xx9QC0g) · ~21 min, výklad (španělský originál, přepis z anglického dabingu)

**Shrnutí:** Když scéna nefunguje, je to podle autora obvykle chyba plánu, ne modelování nebo textur. Blockout proto staví na třech krocích:
- **zastav se** a rozlož objekt na jednoduché tvary s hierarchií velikostí,
- **omez se** na jednoduché tvary přímo v enginu, protože čitelnost se pozná na siluetě,
- **porovnej** všechno s postavou, protože měřítko bez reference posoudit nejde.

Háček: v produkci trvá blockout měsíce, někdy i roky, a autor ho proto nazývá polovinou projektu [(0:01)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=1s).

### Rozpad myšlenky

**Proč tolik času.** Blockout je fáze z krabic, ještě před artem a světlem. Dává hrubou představu o scéně a siluetě a ukáže, jestli funguje pohyb prostředím [(0:49)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=49s). Smazat kostku trvá dvě vteřiny, smazat budovu, na které jsi strávil hodiny, je problém. Blockout proto musí být rychlý, snadno upravitelný a dost jednoduchý na to, aby šlo pořád zapracovávat zpětnou vazbu [(2:21)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=141s). Autor uvádí artistu, který na blockout dřív dával nejvýš týden. Na jednom projektu mu dal mnohem víc času a celý projekt se tím posunul na jinou úroveň, takže tak pracuje dál [(1:35)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=95s).

**Zastav.** Nadšení na začátku projektu tě po hodině a půl nechá v situaci, kdy nevíš, co a proč stavíš [(2:21)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=141s). Proto se nejdřív maluje přes referenci, na papíře, v Photoshopu, v Miru nebo v PureRefu [(3:07)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=187s). Autorova analogie je nábytek z IKEA: nedostaneš smontovaný kus, ale návod z dílů a toho, jak do sebe zapadají. Objekt se rozloží na kvádry, koule a válce. **Kdo ho z nich postavit neumí, nerozumí mu dost** [(3:54)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=234s). Oko jde trénovat na fotkách věcí z domu [(4:40)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=280s). Jakmile začneš vidět i tvary, které se opakují, děláš už modulární blockout, tedy díly, ze kterých se skládají další objekty [(5:26)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=326s).

**Hierarchie tvarů.** Autor stojí na lekcích dlouholetého art directora z Pixaru. Velké tvary dávají hlavní objem, střední je podpírají a malé přidávají zájem. V blockoutu jim odpovídají primární, sekundární a terciární tvary. Střední pomáhají i s měřítkem a malé zasadí objekt či postavu do světa a ukážou vztahy k prostředí [(6:15)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=375s), [(7:01)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=421s). Častá chyba je dělit velký tvar napůl: obě poloviny jsou pak stejně velké a žádná nemá větší váhu. Objekty postavené rovně ve stejném měřítku tvoří jen čáru, s různými velikostmi vznikne silueta. Autor tu mluví o poměrech 70/30 nebo 60/40 [(7:48)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=468s). Pro detail uvádí zhruba 40 % plochy s detailem a 60 % klidu, aby si oko odpočinulo [(8:36)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=516s).

**Test přimhouřených očí.** Když přimhouříš oči, detail se rozmaže a zůstanou jen tvary. Pokud odpovídají tvarům z rozkladu, je scéna dobře zablokovaná. Pokud vidíš šum, možná přišel detail příliš brzo. Autor test podle svých slov objevil nedávno a v praxi ho zatím moc nepoužíval, ale pokaždé mu přišel velmi zajímavý [(8:36)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=516s), [(9:22)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=562s). Autor to spojuje s přednáškou designéra z Naughty Dog na GDC: hráč má z blockoutu poznat, kam jít, bez artu, světla a textur. Je to práce level designerů, ale environment artista to má umět taky [(9:22)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=562s), [(10:08)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=608s).

**Omez.** Autorovi studenti nesmějí blockout modelovat v Blenderu. Začínají jednoduchými tvary přímo v Unrealu [(10:55)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=655s). Je to princip z fotografie: s jediným pevným ohniskem se musíš hýbat, a tím se učíš. Oblouk je pár natočených kvádrů [(11:41)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=701s). Environment artista z Naughty Dog tvrdí, že blockout se soudí jako postava, podle siluety. Když nejsou zajímavé velké tvary, nespraví to textura, detail ani postprodukce [(11:41)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=701s). Autor The Level Design Book rozlišuje čitelný prostor, tedy jednoduché tvary pochopitelné na první pohled, a šum z mnoha drobností [(12:28)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=748s). Omezení neznamená dům z jedné kostky. Budova potřebuje okna, dveře a fasádu, jen z jednoduchých tvarů [(13:15)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=795s). Proto šedé materiály: z typů kontrastu je nejsilnější hodnota, šerosvit. Šedý blockout přijde o barvu, ale ten nejsilnější kontrast mu zůstane [(13:15)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=795s), [(14:02)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=842s).

**Porovnej.** Tři stejné kostky vypadají správně, dokud vedle každé nestojí postava. Teprve pak je vidět, která sedí [(14:50)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=890s), [(15:17)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=917s). Měřítko není kontrola na konec, ale věc od prvního dne. Environment artistka ze Santa Monica Studio blokuje rovnou s postavou a nechává ji ve scéně v různých místech a vzdálenostech [(16:04)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=964s).
- Hierarchie měřítek funguje jako hierarchie tvarů. Mohutná budova potřebuje kolem sebe malé věci. Když uděláš velké všechno, nic nevyčnívá a všechno působí obecně [(16:51)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=1011s).
- Správné měřítko neznamená skutečné. Strop ve výšce zhruba 2,5 m, jaký má skutečný dům, působí ve hře stísněně, a hry z pohledu třetí osoby proto mívají dveře, stropy i schody o něco větší [(16:51)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=1011s), [(17:38)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=1058s).
- Oko je ale vycvičené na stůl pod pas nebo na dveře, kterými projdeš [(17:38)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=1058s). Polička o tloušťce 10 cm vypadá v enginu jako špalek [(18:25)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=1105s).
- Proto blockout v enginu: každou půlhodinu pustit hru, projít scénu, udělat screenshot, zakreslit do něj, co nefunguje, a opravit to [(19:11)](https://www.youtube.com/watch?v=VxTQhSr1sbw&t=1151s).

> **Pozn.:** Autorovy poměry (70/30 nebo 60/40 pro velikosti tvarů, 40 ku 60 pro detail a klid) nemají nic společného se dvěma jinými „70/30" v knihovně: s poměrem [kostek a lepidla](principy-architektury.md#znovupouzitelne-kostky-a-lepidlo-70-ku-30) v architektuře Blueprintů, ani se [zápiskem o motion matchingu](../zapisky/pravidlo-70-30.md). Jen se potkala stejná čísla. Myšlenka klidu pro oko je stejná jako [hierarchie, která vzniká ubráním](../teorie/art-pipeline.md#vizualni-hierarchie-fokus-vznika-ubranim-ne-pridanim). Video na začátku zmiňuje autorův mentoring a jména citovaných lidí jsou v dabovaném přepisu zkomolená, proto je tu uvádím jen podle rolí. Jak blockoutem vést hráče, rozebírá [Level design pro sólo vývojáře](../teorie/level-design-solo.md#pet-principu-cil-novost-zadny-prazdny-prostor-tok-a-jazyk-hry).

**Souvislosti:** [Rejstřík: Blockout](../rejstrik.md#blockout) · [Rejstřík: Silueta](../rejstrik.md#silueta) · [Nejdřív tvary: design language a chiaroscuro](env-tvorba.md#nejdriv-tvary-design-language-a-chiaroscuro) *(tentýž princip v hotové scéně)* · [Gestalt a vizuální hierarchie](../teorie/vizualni-komunikace.md#gestalt-a-vizualni-hierarchie-mozek-cte-cely-obraz) · [Cyberpunk 2077](../teorie/vydani-hry.md#cyberpunk-2077-launch-ktery-se-rozbil-a-roky-oprav) *(Night City od urbanistiky přes blockout ke kitům)*

---

## Hybridní blockout: hodnoty a barva dřív než materiály

**Zdroj:** [Why Naughty Dog's 3D Blockouts Are World Class (Hybrid Workflow)](https://www.youtube.com/watch?v=2OBTIFS0PdE) · [EMC3D - Game Art](https://www.youtube.com/channel/UCrgHtScXrxgQMGvdNb04tkA) · ~16 min, výklad (pipeline Naughty Dog z GDC 2014)

**Shrnutí:** Většina začátečníků skončí u šedého blockoutu s rychlým světlem a jde rovnou na materiály. Pipeline Naughty Dog přidává dva kroky:
- **průchod hodnot (value pass):** stěny, podlahy a lišty v různých odstínech šedi, aby se tvary oddělily,
- **průchod barvy:** barva vzorkovaná z konceptu, v mezích PBR.

Háček: scéna pak vypadá skoro jako hotová stylizovaná hra s plochými texturami. Světlo, nálada i kompozice se dají posoudit dřív, než vznikne jediný materiál.

### Rozpad myšlenky

**Odkud to je.** Postup pochází z přednášky na GDC 2014 a z rozhovoru s osvětlovací artistkou Naughty Dog. Autor sám upozorňuje, že se od té doby mohl změnit, ale považuje ho za užitečný i dnes. Je postavený kolem světla [(1:35)](https://www.youtube.com/watch?v=2OBTIFS0PdE&t=95s).

**Pipeline** [(2:21)](https://www.youtube.com/watch?v=2OBTIFS0PdE&t=141s):
1. Koncept.
2. Hrubý mesh od designéra: hlavní cesty, primitivní tvary, v jakémkoli nástroji. Přednáška ho neukazuje. V ukázkách, které autor sehnal jinde, je podrobnější než běžný blockout level designu a finálnímu artu velmi blízko [(4:44)](https://www.youtube.com/watch?v=2OBTIFS0PdE&t=284s).
3. Šedý průchod: 50% šedá a základní světlo. Naughty Dog světla zapékal a stavěl v Mayi [(5:33)](https://www.youtube.com/watch?v=2OBTIFS0PdE&t=333s), [(6:20)](https://www.youtube.com/watch?v=2OBTIFS0PdE&t=380s).
4. Průchod hodnot.
5. Průchod barvy a difuzního stínování.
6. Postprocess. Autor dodává, že dnes jde typicky o expozici, případně o LUT [(3:56)](https://www.youtube.com/watch?v=2OBTIFS0PdE&t=236s).

U třetího kroku většina začátečníků skončí [(3:08)](https://www.youtube.com/watch?v=2OBTIFS0PdE&t=188s).

**Hodnoty.** Průchod hodnot nutí přemýšlet jako artista, ne jako technický modelář [(6:20)](https://www.youtube.com/watch?v=2OBTIFS0PdE&t=380s). Autor k tomu přidává zásadu, kterou se naučil od kolegů: oddělit vodorovné od svislých. Podlaha, lišta u podlahy a lišta nahoře jsou každá světlejší, nebo tmavší než stěna. Tvary pak vystoupí a scéna dostane hloubku [(7:06)](https://www.youtube.com/watch?v=2OBTIFS0PdE&t=426s). Naughty Dog použil kolem deseti odstínů, pro začátek stačí tři nebo čtyři. Při stejném světle je rozdíl proti 50% šedé vidět hned [(7:52)](https://www.youtube.com/watch?v=2OBTIFS0PdE&t=472s).

**Barva.** Do material instancí blockoutu jde hrubá barva, vzorkovaná z konceptu jako průměr [(7:52)](https://www.youtube.com/watch?v=2OBTIFS0PdE&t=472s). Nesmí být moc tmavá, protože PBR má meze jasu a barvy a platí už v blockoutu [(8:38)](https://www.youtube.com/watch?v=2OBTIFS0PdE&t=518s). Světlo barvu odráží po scéně, takže nálada a emoce jsou vidět dřív, než přijdou odlesky nebo opakující se materiály. Podle autora pak scéna působí skoro jako hotová stylizovaná hra s plochými texturami a dobrým světlem [(9:24)](https://www.youtube.com/watch?v=2OBTIFS0PdE&t=564s). Žádná hodnota nemá být čistě černá ani čistě bílá; jestli nejsou hodnoty rozmáčknuté, ukáže histogram [(10:11)](https://www.youtube.com/watch?v=2OBTIFS0PdE&t=611s).

**Proč tak brzy.** Zadavatelé si hru zahrají a vidí zamýšlenou náladu. Osvětlovač, který je u projektu od blockoutu, pozná, kudy může přijít světlo, a přidá okna nebo otvory ve stropě. S Lumenem platí, že čím víc přirozeného světla, tím líp [(10:57)](https://www.youtube.com/watch?v=2OBTIFS0PdE&t=657s).

**Tři úrovně.** Začít rychle a postupně zamykat [(14:51)](https://www.youtube.com/watch?v=2OBTIFS0PdE&t=891s):
- úroveň 0: hrubé tvary jako od designéra, kompozice a zpětná vazba,
- úroveň 1: siluety, aby nic nebylo příliš kostrbaté,
- úroveň 2: hodnoty a barva.

Po každé úrovni přijde zpětná vazba, výsledek se zamkne a teprve pak jde scéna do produkce. Autor k tomu připomíná důležitost kamery a dodává, že tohle není jediný správný způsob [(15:38)](https://www.youtube.com/watch?v=2OBTIFS0PdE&t=938s).

**Ve výuce.** Název „hybridní blockout" je autorův, Naughty Dog ho tak nenazývá [(11:43)](https://www.youtube.com/watch?v=2OBTIFS0PdE&t=703s). Studenti odevzdávali čtyři pohledy: 50% šedou, hodnoty, barvu se světlem a neosvětlený pohled na hodnoty a barvu. Barvu jde i odbarvit a hodnoty tak kontrolovat průběžně [(11:43)](https://www.youtube.com/watch?v=2OBTIFS0PdE&t=703s), [(12:30)](https://www.youtube.com/watch?v=2OBTIFS0PdE&t=750s). Do materiálů pak šlo dalších sto až dvě stě hodin (autor jednou uvádí 100–150, podruhé 100–200), ale na pevném základu [(13:16)](https://www.youtube.com/watch?v=2OBTIFS0PdE&t=796s), [(14:03)](https://www.youtube.com/watch?v=2OBTIFS0PdE&t=843s).

> **Pozn.:** S [první myšlenkou](#zastav-omez-porovnej-blockout-ktery-se-da-precist) si to neodporuje. Obě kladou důraz na hodnotu (šerosvit je pojem z prvního videa). Pipeline Naughty Dog jen přidá barvu dřív, než přijdou materiály: světlo ji odráží po scéně, takže nálada je vidět už bez nich. Fyzikálně věrné hodnoty na straně světla, tedy expozici a intenzity, rozebírá [PBL: svítit podle skutečných hodnot](osvetleni.md#pbl-svitit-podle-skutecnych-hodnot). Video na začátku propaguje autorův Patreon [(0:48)](https://www.youtube.com/watch?v=2OBTIFS0PdE&t=48s).

**Souvislosti:** [Rejstřík: Value pass](../rejstrik.md#value-pass) · [Rejstřík: PBR](../rejstrik.md#pbr) · [Rejstřík: LUT](../rejstrik.md#lut) · [Prostředí je 90 % obrazovky](../teorie/art-pipeline.md#prostredi-je-90-obrazovky-a-musi-mluvit)
