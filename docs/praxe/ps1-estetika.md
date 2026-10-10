# PS1 estetika: dělat věci schválně hůř

Retro low-poly styl není nostalgická lenost — je to **sada omezení, která se dá vyrobit záměrně** a která šetří práci na místech, kde by realistický vzhled stál nejvíc. Kapitola shrnuje, co konkrétně dělá PS1 vzhled PS1 vzhledem: **malé textury, tvrdé filtrování, žádné odlesky, ruční UV po jednotlivých stěnách** — a na straně enginu **mlha a nízké rozlišení**. Jak mlhu a pixely postavit v Unrealu, ukazuje [poslední myšlenka](#ps1-v-enginu-mlha-jako-post-process-material-a-pixely-z-uv).

Sousední kapitola [Z fotky herní asset](foto-do-assetu.md) řeší tutéž otázku z opačné strany: jak z jedné textury vytěžit co nejvíc věrnosti.

---

## Textura dělá styl: rozlišení, kontrast a nearest

**Zdroj:** [How to make PS1 style models in Blender | Part 1: Textures and UV Mapping](https://www.youtube.com/watch?v=8--xYWCY_bc) · [hacktic](https://www.youtube.com/channel/UCrevRFc9aHBKmXBaxAxa1wg) · ~5 min · + [How to make PS1 Graphics in 4 minutes](https://www.youtube.com/watch?v=A25NTdPGNaw) · [binbun3D](https://www.youtube.com/channel/UCzxuU3cQWI_J79_47Z1OnvA) · ~4 min, tutoriály

**Shrnutí:** Charakteristický vzhled nevzniká v modelu, ale v textuře a v tom, jak se vykresluje. Čtyři konkrétní rozhodnutí ho udělají skoro celý: **rozlišení kolem 128×128**, **zvýšit kontrast dřív, než texturu zmenšíš**, **indexovat barvy** a **přepnout filtrování na nearest**. K tomu vypnuté odlesky — protože konzole tehdy žádné neuměla.

### Rozpad myšlenky

**Rozlišení jako historická hranice** [(0:48)](https://www.youtube.com/watch?v=8--xYWCY_bc&t=48s): *„největší textury, které se na PlayStationu 1 běžně používaly, byly 128×128."* A hned praktický důsledek — velikost se volí podle objektu, ne paušálně: bedna je malá věc, takže dostane **32×32**. Druhý autor to potvrzuje a přidává organizační vrstvu [(0:57)](https://www.youtube.com/watch?v=A25NTdPGNaw&t=57s): pracuje se stejným limitem, ale všechny textury domu **zabalí do jediného atlasu 256×256**.

**Kontrast napřed, zmenšení potom** [(0:48)](https://www.youtube.com/watch?v=8--xYWCY_bc&t=48s) je ta rada, kterou by člověk sám nevymyslel: *„textury mi po zmenšení začnou vypadat rozmazaně, tak nejdřív trochu zvýším kontrast."* Zmenšení je průměrování — a průměrování ubírá kontrast. Když ho dodáš předem, přežije redukci to, co má.

**Indexování barev** [(1:44)](https://www.youtube.com/watch?v=A25NTdPGNaw&t=104s): *„k autentičnosti kromě snížení rozlišení patří i indexování barev textury."* Omezená paleta je druhá polovina toho, proč staré textury vypadaly, jak vypadaly — bez ní má výsledek správné rozlišení, ale moderní barevnost.

**Nastavení materiálu** [(1:34)](https://www.youtube.com/watch?v=8--xYWCY_bc&t=94s) je krátký seznam se zdůvodněním: **specular na 0 a roughness na 1**, aby zmizely odlesky, a **filtrování na Closest** — *„protože PlayStation 1 nepodporovala filtrování textur."* Tenhle poslední bod je ten nejviditelnější: bez něj dostaneš rozmazanou nízkorozlišenou texturu, což je jen ošklivé; s ním ostré pixely, což je styl.

**Na straně enginu** [(2:42)](https://www.youtube.com/watch?v=A25NTdPGNaw&t=162s) pak platí totéž a ještě dvě věci navíc. **Sampling na nearest** (v některých enginech „point sampling") je nutnost. **Mlha** je podle autora *„pilíř moderního PS1 stylu"* a rozdíl je *„jasně vidět"* — mimochodem přesně z téhož důvodu, z jakého ji tehdejší hry měly: **krytí krátké dohledové vzdálenosti**. A nakonec **snížení rozlišení celé hry**, *„aby to mělo autentický PS1 pocit"*.

> **Pozn.:** Za pozornost stojí, že žádné z těch rozhodnutí není o modelu — a přesto dohromady dělají styl. Prakticky z toho plyne užitečná rada pro vlastní projekt: **než začneš stylizovat geometrii, vyzkoušej stylizovat vykreslování.** Tři přepínače (filtrování, rozlišení, mlha) ti ukážou, jestli směr sedí, dřív než na něm postavíš hodiny modelování. Mimochodem je to táž disciplína jako u [pixel artu](../teorie/2d-vizual.md#pixel-art-je-rozhodnuti-ne-nouzove-reseni): retro vzhled je rozhodnutí s pravidly, ne absence rozhodnutí.

**Souvislosti:** [Model a UV po stěnách](#model-a-uv-po-stenach-krychle-quady-a-fotky-narovnane-do-obdelniku) *(druhá polovina postupu)* · [2D vizuál: pixel art je rozhodnutí](../teorie/2d-vizual.md#pixel-art-je-rozhodnuti-ne-nouzove-reseni) · [Horor design: retro styly a konzistence](../teorie/horor-design.md) · [Osvětlení: mlha ze Silent Hill 2](osvetleni.md#mlha-ze-silent-hill-2-volumetricky-material-kolem-postavy) *(tatáž mlha jako percepční hranice)* · [Rejstřík: mip mapa](../rejstrik.md#mip-mapa) · [Rejstřík: texture atlas](../rejstrik.md#texture-atlas) · [PS1 v enginu](#ps1-v-enginu-mlha-jako-post-process-material-a-pixely-z-uv) *(mlha a pixely jako materiály)*

---

## Model a UV po stěnách: krychle, quady a fotky narovnané do obdélníku

**Zdroj:** [How to make PS1 style models in Blender | Part 1: Textures and UV Mapping](https://www.youtube.com/watch?v=8--xYWCY_bc) · [hacktic](https://www.youtube.com/channel/UCrevRFc9aHBKmXBaxAxa1wg) · ~5 min · + [How to make PS1 Graphics in 4 minutes](https://www.youtube.com/watch?v=A25NTdPGNaw) · [binbun3D](https://www.youtube.com/channel/UCzxuU3cQWI_J79_47Z1OnvA) · ~4 min, tutoriály

**Shrnutí:** Modelování se řídí jedinou zásadou — *„drž to co nejjednodušší; spousta objektů se dá reprezentovat v podstatě texturovanou krychlí"* — a všechna práce se přesouvá do **ručního rozmisťování UV po jednotlivých stěnách**. Nejcennější kus je návod, jak si vyrobit **rozbalenou texturu z běžné fotky**, když žádná hotová neexistuje.

### Rozpad myšlenky

**Krychle jako výchozí bod** [(0:01)](https://www.youtube.com/watch?v=8--xYWCY_bc&t=1s): bedna je krychle, na které se nemění vůbec nic — jen se na ni namapuje textura. Kontejner je tatáž krychle přeškálovaná do jiného poměru. Model se tedy nedělá „jednoduchý", model se **nedělá vůbec**, dokud si to tvar nevynutí.

**Když už modeluješ, dělej quady** [(0:02)](https://www.youtube.com/watch?v=A25NTdPGNaw&t=2s): dům vzniká extruzí z výchozí krychle a autor u toho dává dvě rady, které spolu souvisí. *„Je důležité, aby většina polygonů byly quady, tedy stěny ze čtyř hran — usnadní ti to subdivisiony a loop cuty, kdybys je někdy potřeboval."* A hned nato **rozbití symetrie**, aby model nebyl nudný. Doplňkově dělá **subdivisiony ve stěnách jako přípravu na mapování různých textur na různé části** a označuje **seamy** pro rozbalení.

**Ruční UV po stěnách** [(1:34)](https://www.youtube.com/watch?v=8--xYWCY_bc&t=94s): UV editing, edit mode, **face select**, material preview — a pak už jen klikat. Vybereš stěnu a rovnou vidíš, která část textury na ni padne; vybereš všechny stěny krychle, naškáluješ mapu na celou texturu a zarovnáš. Je to práce, kterou u realistického assetu dělá automatické rozbalení — tady je **ruční umístění samotný design**.

**A teď ta nejužitečnější část** [(3:07)](https://www.youtube.com/watch?v=8--xYWCY_bc&t=187s), protože řeší problém, na který narazíš hned: *„hezky rozbalené textury objektů online nenajdeš, takže si je musíš udělat sám."* Postup z obyčejné fotky kontejneru: **free select vybere jednu stěnu → perspective tool ji narovná do obdélníku** → *„vypadá to trochu protažené, ale po zmenšení už to nepoznáš"* → zkopírovat na samostatný obrázek a zopakovat pro každou stranu. Na tom je hezké, že **cílová nízká kvalita je zároveň tolerance metody**: čím míň pixelů, tím míň vadí, že narovnání není přesné.

**Variace levně** [(3:07)](https://www.youtube.com/watch?v=8--xYWCY_bc&t=187s): jednu boční texturu použil na všechny čtyři dlouhé stěny a **heal toolem odstranil logo**, aby vznikl rozdíl. Táž logika jako u [instancovaného města](env-breakdowny.md#san-francisco-11-mesto-od-jednoho-cloveka) — opakuj a rozbij opakování drobností.

**Vegetace za nic** [(2:42)](https://www.youtube.com/watch?v=A25NTdPGNaw&t=162s): kmen je válec, koruna **dvě zkřížené plochy**. Je to trik starý jako 3D grafika a v tomhle stylu není náhražkou, ale správným řešením.

> **Pozn.:** Oba návody jsou z roku 2023 a jsou to krátká, poctivá videa bez ambicí — hodnota je v tom, že se **shodují**, takže z nich jde poskládat úplný postup. Jako vizuální reference k nim patří i **timelapse stavby celého PS1 prostředí** od [Summer 85](https://www.youtube.com/watch?v=d9GUXlnwRGk), který je ovšem bez komentáře (autor sám v popisu píše, že neměl jasnou představu a šel po citu) — dá se z něj číst tempo a rozsah práce, ne postup. Pro sólo projekt je tenhle styl reálná varianta: **omezení jsou tvrdá, ale jsou to omezení, ne nedostatky**, a scope se s nimi počítá mnohem líp než s realismem.

**Souvislosti:** [Textura dělá styl](#textura-dela-styl-rozliseni-kontrast-a-nearest) *(první polovina postupu)* · [Z fotky herní asset](foto-do-assetu.md#narovnat-obtahnout-promitnout) *(narovnávání fotky v plné podobě)* · [Breakdowny: San Francisco](env-breakdowny.md#san-francisco-11-mesto-od-jednoho-cloveka) *(opakování rozbité detailem)* · [Scope: design by constraint](../teorie/scope.md#design-by-constraint-krabice-napred-napad-dovnitr) *(styl jako vědomě zvolená krabice)* · [Rejstřík: UV mapping](../rejstrik.md#uv-mapping) · [Rejstřík: texture atlas](../rejstrik.md#texture-atlas)

---

## PS1 v enginu: mlha jako post-process materiál a pixely z UV

**Zdroj:** [How to Make PSX-Style Fog in Unreal Engine 5](https://www.youtube.com/watch?v=6i5hk_9whpE) · [Eremental Studios](https://www.youtube.com/channel/UC88Io71mvrSSBEOTekJydLQ) · ~15 min, tutoriál ·
[Pixelated Effect on Any Material in Unreal Engine 5 | Material Tutorial](https://www.youtube.com/watch?v=UFX-DwosKUM) · [Zima Env](https://www.youtube.com/channel/UC1Ob_PAPVw5dL6XlpCfXuKg) · ~2 min, tutoriál

**Shrnutí:** Mlhu, kterou [první myšlenka](#textura-dela-styl-rozliseni-kontrast-a-nearest) označuje za pilíř stylu, i kostičkovaný vzhled jde v Unrealu postavit z materiálů:
- **mlha** jako post-process materiál, který podle vzdálenosti od kamery přimíchá barvu mlhy a rozpohybuje ji šumem. Nepoužívá volumetriku ani exponential height fog, takže skoro nic nestojí;
- **pixelizace** zaokrouhlením UV, které dá kostičky jakékoli textuře, i v Niagaře.

Háček: obojí řídí parametry, mlhu v material instanci, pixelizaci jediný parametr velikosti pixelu. Styl se tak dá doladit až ve scéně, ne předem v textuře.

### Rozpad myšlenky

**Mlha z post-processu.** Materiál má doménu Post Process a z uzlu SceneTexture bere PostProcessInput0, tedy hotový obraz scény [(1:35)](https://www.youtube.com/watch?v=6i5hk_9whpE&t=95s), [(2:21)](https://www.youtube.com/watch?v=6i5hk_9whpE&t=141s). Lerp míchá obraz s barvou mlhy a výsledek jde do emisivu. Alfa lerpu se skládá ze dvou částí:
- **vzdálenost:** délka rozdílu mezi pozicí ve světě a pozicí kamery, minus parametr začátku mlhy (výchozí 50), vydělená parametrem vzdálenosti (2500) a ořezaná uzlem Saturate [(6:41)](https://www.youtube.com/watch?v=6i5hk_9whpE&t=401s), [(7:27)](https://www.youtube.com/watch?v=6i5hk_9whpE&t=447s), [(10:26)](https://www.youtube.com/watch?v=6i5hk_9whpE&t=626s);
- **šum:** absolutní pozice ve světě násobená měřítkem šumu, k ní čas násobený směrem pohybu, celé to přes Vector Noise a parametr síly [(3:55)](https://www.youtube.com/watch?v=6i5hk_9whpE&t=235s), [(4:48)](https://www.youtube.com/watch?v=6i5hk_9whpE&t=288s), [(5:08)](https://www.youtube.com/watch?v=6i5hk_9whpE&t=308s), [(5:54)](https://www.youtube.com/watch?v=6i5hk_9whpE&t=354s).

Aby mlha fungovala, je potřeba v jednom z lerpů změnit hodnotu z 1 na 0 a Vector Noise přepnout z cell noise na Perlin 3D, jinak je mlha kostičkovaná. Blendable location video nakonec mění na Scene Color After DOF jako doladění, které se k materiálu hodí víc [(11:13)](https://www.youtube.com/watch?v=6i5hk_9whpE&t=673s). Parametry se pak ladí v material instanci [(12:00)](https://www.youtube.com/watch?v=6i5hk_9whpE&t=720s). Mlha se zapne přes post-process volume s neomezeným rozsahem (Infinite Extent), kde je materiál v seznamu Post Process Materials [(12:47)](https://www.youtube.com/watch?v=6i5hk_9whpE&t=767s), [(13:34)](https://www.youtube.com/watch?v=6i5hk_9whpE&t=814s). Nakonec přibude parametr rychlosti, protože výchozí pohyb je moc rychlý [(13:34)](https://www.youtube.com/watch?v=6i5hk_9whpE&t=814s), [(14:22)](https://www.youtube.com/watch?v=6i5hk_9whpE&t=862s).

**Pixely z UV** [(0:02)](https://www.youtube.com/watch?v=UFX-DwosKUM&t=2s):
1. Texture Coordinate se vynásobí parametrem velikosti pixelu,
2. uzel Floor souřadnice zaokrouhlí dolů, a tím vzniknou kostičky,
3. výsledek se vydělí stejným parametrem a jde do UV všech texture samples v materiálu.

Video to dělá přímo v master materiálu. Na pixelizaci celého projektu to podle něj není nejlepší cesta, na pár materiálů v pixelovém stylu vedle běžných ale stačí. Stejně jde pixelizovat i Niagara efekt s texturou, který pak připomíná Minecraft [(0:50)](https://www.youtube.com/watch?v=UFX-DwosKUM&t=50s).

> **Pozn.:** Zaokrouhlené UV a [nearest filtrování](#textura-dela-styl-rozliseni-kontrast-a-nearest) nejsou totéž. Nearest ukáže ostré texely v rozlišení textury, zaokrouhlené UV dělá kostičky v hustotě, kterou nastavíš parametrem, nezávisle na textuře. Post-process mlha nepočítá se světlem, a proto je levná. Světla v ní ale nezáří jako ve volumetrické mlze. Obojí je naše vysvětlení. Skutečné PS1 mělo ještě dvě typické vady: textury se deformovaly, protože jim chyběla perspektivní korekce, a vrcholy se třásly. Na ty korpus zatím zdroj nemá. Eremental Studios ve videu propaguje vlastní projekty na Fabu, Gumroad a Discord [(0:49)](https://www.youtube.com/watch?v=6i5hk_9whpE&t=49s), [(14:22)](https://www.youtube.com/watch?v=6i5hk_9whpE&t=862s).

**Souvislosti:** [Textura dělá styl](#textura-dela-styl-rozliseni-kontrast-a-nearest) *(mlha jako pilíř stylu)* · [Rejstřík: Post-process material](../rejstrik.md#post-process-material) · [Rejstřík: Nearest-neighbor filtering](../rejstrik.md#nearest-neighbor-filtering) · [Mlha ze Silent Hill 2](osvetleni.md#mlha-ze-silent-hill-2-volumetricky-material-kolem-postavy) *(mlha jako volumetrický materiál)*
