# Modulární kity a trim sheety

Velký svět se nestaví z unikátních objektů, ale z dílů, které se opakují v nových kombinacích, a z textur, které sdílí co nejvíc assetů. Kapitola tu cestu skládá ve čtyřech krocích. Nejdřív kit: jak ho naplánovat, postavit a otestovat. Pak textury: tilery, trim sheety a masky, díky kterým stačí na jeden kámen dvě textury. Pak organický kit a spoje, které schovají švy. A nakonec dvě případovky: Beauclair z Witcher 3, celé město v rozpočtu 500 MB textur, a Mortal Shell 2, jehož vzhled podle autora rozboru patří k nejlepším roku, přestože na něm dělalo kolem třiceti lidí. Páteří je 87minutový workshop environment artisty ze Santa Monica Studio. Z čeho kit vzniká, popisuje [Blockout](blockout.md), jak trim sheet vypadá v The Last of Us, [Breakdowny](env-breakdowny.md#tlou-trim-sheet-ktery-nahradil-tisice-bake) a sdílený master materiál v UE [Materiály](materialy.md#master-material-pet-textur-nema-mit-kazdy-mesh).

---

## Kit jako lego: co nejméně kusů, mřížka v metrech a zoo na zkoušku

**Zdroj:** [The easiest Way to Create Modular 3D Kits Without Stress](https://www.youtube.com/watch?v=77xPHfzciiY) · [Beyond Extent](https://www.youtube.com/channel/UCPHrTip4HJDajQG3eTKhAqQ) · ~87 min, workshop (environment artist ze Santa Monica Studio)

**Shrnutí:** Kit je lego: tytéž kusy se znovu a znovu skládají novými způsoby, ze scény ve svět. Autor ho plánuje podle několika zásad:
- začít s co nejmenším počtem kusů, který ustaví vzhled,
- kusy přidávat hlavně v konkrétních situacích (opakování na obrazovce, detail, nový prvek, destrukce),
- všechno stavět na mřížce v metrech, aby kusy zacvakly a texturovalo se snáz.

Háček: velikost kusu se řídí velikostí prostředí. Pro velké město nedává smysl dělat jedno okno, ale celé patro nebo budovu.

### Rozpad myšlenky

**Proč kit.** Autor se ke kitům dostal na MMO: to je podle něj asi největší hra, jakou můžeš zkusit udělat, a kity při takovém rozsahu hodně pomáhají s výrobou obsahu i s optimalizací [(2:31)](https://www.youtube.com/watch?v=77xPHfzciiY&t=151s), [(3:17)](https://www.youtube.com/watch?v=77xPHfzciiY&t=197s). Kit je jako lego: z kousků scéna, ze scén prostředí, z prostředí svět [(5:37)](https://www.youtube.com/watch?v=77xPHfzciiY&t=337s). Pomáhá tvořivosti, iteraci a sdílení assetů mezi projekty i lidmi. A hlavně konci produkce, o kterém se moc nemluví: na všechen art budeš sahat znovu a znovu a nedestruktivní postup ti to usnadní [(6:23)](https://www.youtube.com/watch?v=77xPHfzciiY&t=383s).

**Plánování.**
- Rozlišit pevný (hard surface) a organický kit. Pevný je architektura, kusy do sebe zapadají a řeší se švy. Organický snese kusy zabořené do sebe [(7:09)](https://www.youtube.com/watch?v=77xPHfzciiY&t=429s).
- Čím větší prostředí, tím větší kusy. U velkého města se nevyplatí dělat jednotlivé okno, kusem je celé patro nebo budova [(7:09)](https://www.youtube.com/watch?v=77xPHfzciiY&t=429s), [(7:56)](https://www.youtube.com/watch?v=77xPHfzciiY&t=476s).
- Velké, střední a malé kusy jako při malování: nejdřív velké a střední, protože jednotlivé cihly tě zahltí [(7:56)](https://www.youtube.com/watch?v=77xPHfzciiY&t=476s).
- Sepsat všechny textury, které kit potřebuje. Potřebuje dřevěný kit opravdu celý 2K tiler kovu, nebo stačí trim či atlas [(8:42)](https://www.youtube.com/watch?v=77xPHfzciiY&t=522s)?

**Jediná nevýhoda.** Kit znamená hodně objektů a draw callů ve scéně. Ani instancovaná tráva umístěná stotisíckrát nemusí být levná, protože se může kreslit tisíckrát [(9:28)](https://www.youtube.com/watch?v=77xPHfzciiY&t=568s). Ve studiu se proto na konci, až je prostředí hotové, kusy sloučí do jednoho modelu: tisíc objektů a tisíc draw callů se změní v jeden. Je to ale spíš trvalý stav, po kterém se obvykle už neiteruje [(10:14)](https://www.youtube.com/watch?v=77xPHfzciiY&t=614s).

**Co nejméně kusů.** Méně je víc. Autor začíná minimem, které ustaví vzhled scény: jedna stěna, jeden sloup, jedna podlaha [(10:14)](https://www.youtube.com/watch?v=77xPHfzciiY&t=614s), [(11:00)](https://www.youtube.com/watch?v=77xPHfzciiY&t=660s). Pět set kamenů, ze kterých nakonec použiješ tři nebo čtyři, je spíš ztracený čas, ledaže jen experimentuješ a plánuješ [(11:47)](https://www.youtube.com/watch?v=77xPHfzciiY&t=707s). Kit autor rozšiřuje hlavně ve čtyřech situacích [(12:33)](https://www.youtube.com/watch?v=77xPHfzciiY&t=753s), [(13:19)](https://www.youtube.com/watch?v=77xPHfzciiY&t=799s):
- **opakování:** vidíš tutéž stěnu sedmkrát vedle sebe na obrazovce, je čas na varianty,
- **detail:** hrany a lemy střechy zajímavější silueta,
- **nový prvek:** okapové roury jako samostatný malý kit,
- **destrukce:** hromádky sutin, cihly a třísky.

Čím víc kit používáš, tím víc se rozrůstá: výměny materiálu, sada budov A a k ní sada B [(14:05)](https://www.youtube.com/watch?v=77xPHfzciiY&t=845s). Stejná logika platí i pro jednotlivý kus. Obložení u stěny autor neodděluje. Ptá se, jestli ho někdy použije bez stěny, a to se skoro nestává, takže zůstane jeden kus, se kterým se líp skládá. Rozbitá verze vznikne, až bude potřeba [(30:30)](https://www.youtube.com/watch?v=77xPHfzciiY&t=1830s), [(31:16)](https://www.youtube.com/watch?v=77xPHfzciiY&t=1876s).

**Mřížka v metrech.** Na Call of Duty i God of War se myslí v metrech, protože se v nich dobře nastavuje texel density i počet pixelů na metr. Kusy na mřížce pak zacvaknou v enginu a texturují se mnohem snáz [(14:51)](https://www.youtube.com/watch?v=77xPHfzciiY&t=891s), [(15:37)](https://www.youtube.com/watch?v=77xPHfzciiY&t=937s). Autor pracuje s 512 px na metr: kus o délce 1 m odpovídá textuře 512, 2 m textuře 1024 a 4 m 2K. Stěny proto staví zhruba čtyřmetrové [(22:42)](https://www.youtube.com/watch?v=77xPHfzciiY&t=1362s), [(23:29)](https://www.youtube.com/watch?v=77xPHfzciiY&t=1409s). Mřížka má přednost i před skutečnými rozměry. U propů a dveří se autor snaží o reálnou velikost, ale i dveře raději natáhne nebo posune, než aby kus vypadl z mřížky [(21:08)](https://www.youtube.com/watch?v=77xPHfzciiY&t=1268s), [(28:11)](https://www.youtube.com/watch?v=77xPHfzciiY&t=1691s).
- **Pivoty:** architektura je má tam, kde kusy zacvaknou, organické kusy uprostřed, aby se daly volně otáčet [(15:37)](https://www.youtube.com/watch?v=77xPHfzciiY&t=937s), [(16:24)](https://www.youtube.com/watch?v=77xPHfzciiY&t=984s).
- **Pojmenování písmeny, ne čísly:** `wall_window_A`, `B`, `C`. U stěny 37 nikdo neví, jestli je variantou dvojky, nebo jedničky [(17:11)](https://www.youtube.com/watch?v=77xPHfzciiY&t=1031s), [(17:58)](https://www.youtube.com/watch?v=77xPHfzciiY&t=1078s).
- **Zadní strany:** kusy dostanou tloušťku, aby se dobře osvítily bez oboustranných materiálů. Smazat je jde i později, kdyby polygony došly [(26:37)](https://www.youtube.com/watch?v=77xPHfzciiY&t=1597s), [(27:25)](https://www.youtube.com/watch?v=77xPHfzciiY&t=1645s).

**Od blockoutu ke kitu.** Blockout autor modeluje bez zábran a nebojí se přemodelovat. Detail se dá vždy zjednodušit nebo převést do textury [(19:33)](https://www.youtube.com/watch?v=77xPHfzciiY&t=1173s). Celý ho exportuje do enginu jako šablonu a pak z něj vytahuje kusy kitu i propy [(20:21)](https://www.youtube.com/watch?v=77xPHfzciiY&t=1221s). Prop, který se bude texturovat zvlášť, jde do vlastní složky. Začíná stěnami a podlahami [(21:55)](https://www.youtube.com/watch?v=77xPHfzciiY&t=1315s), [(22:42)](https://www.youtube.com/watch?v=77xPHfzciiY&t=1362s). Mezi opakující se plochy přidá mezikus, třeba sloup, který přeruší jednotvárnost tileru: technika „sendviče" [(32:49)](https://www.youtube.com/watch?v=77xPHfzciiY&t=1969s), [(33:35)](https://www.youtube.com/watch?v=77xPHfzciiY&t=2015s).

**Zoo na zkoušku.** Kusy se netestují rovnou ve scéně, ale v „zoo", playground souboru, kde leží všechny vedle sebe [(36:42)](https://www.youtube.com/watch?v=77xPHfzciiY&t=2202s). Zoo slouží jako checklist (co ještě nemá UV, co chce variantu), jako knihovna a jako předávka jinému artistovi [(37:28)](https://www.youtube.com/watch?v=77xPHfzciiY&t=2248s). Scéna se pak znovu postaví přes importovaný blockout jako šablonu, s přichytáváním na mřížku [(38:14)](https://www.youtube.com/watch?v=77xPHfzciiY&t=2294s), [(39:00)](https://www.youtube.com/watch?v=77xPHfzciiY&t=2340s). Cílem není kopírovat blockout jedna ku jedné, ale aby to dobře vypadalo s kitem. Autor dveře upravil, až když je viděl v celku [(39:47)](https://www.youtube.com/watch?v=77xPHfzciiY&t=2387s).

> **Pozn.:** Slučování v UE rozebírá [ISM, HISM a merge](pamet-a-instance.md#ism-hism-a-merge-draw-cally-podle-geometrie): méně draw callů, ale co se s čím sloučí, je potřeba plánovat dopředu. Autor proto slučuje až na úplném konci, kdy se už obvykle neiteruje. Mřížka v metrech zase usnadní, aby tileable textury mezi kusy navázaly, viz [další myšlenka](#textury-pro-kit-tilery-trimy-a-masky-dve-textury-na-kamen). Video natáčel komunitní projekt, který na konci propaguje své placené členství [(1:25:41)](https://www.youtube.com/watch?v=77xPHfzciiY&t=5141s).

**Souvislosti:** [Rejstřík: Modular kit](../rejstrik.md#modular-kit) · [Rejstřík: Texel density](../rejstrik.md#texel-density) · [Rejstřík: Pivot](../rejstrik.md#pivot) · [Blockout](blockout.md) *(odkud kit vzniká)* · [Pivot bez Blenderu](editor-tipy.md#pivot-bez-blenderu-a-rozmisteni-fyzikou) *(pivot opravený přímo v UE)*

---

## Textury pro kit: tilery, trimy a masky, dvě textury na kámen

**Zdroj:** [The easiest Way to Create Modular 3D Kits Without Stress](https://www.youtube.com/watch?v=77xPHfzciiY) · [Beyond Extent](https://www.youtube.com/channel/UCPHrTip4HJDajQG3eTKhAqQ) · ~87 min, workshop (část o texturování)

**Shrnutí:** Úzkým hrdlem prostředí dnes podle autora nejsou polygony, ale textury, protože rozpočet sdílí s postavami, efekty i animacemi. Autor proto kit texturuje v tomto pořadí:
1. sdílené tileable textury, kde to jde,
2. trim sheet tam, kde je potřeba detail,
3. unikátní normal mapa s maskami tam, kde ani to nestačí.

Háček je v tom posledním kroku. Sochaný kámen nepotřebuje vlastní barvu ani roughness, jen normal mapu a jednu texturu s maskami, a zbytek si vezme ze sdílených tilerů. Nový vzhled stejného kamene je pak výměna tileru v materiálu.

### Rozpad myšlenky

**Proč tilery.** S Nanitem a LODy přestaly být polygony hlavní starostí, úzkým hrdlem prostředí je texturování [(48:17)](https://www.youtube.com/watch?v=77xPHfzciiY&t=2897s), [(49:03)](https://www.youtube.com/watch?v=77xPHfzciiY&t=2943s). Na obrazovce jsou i postavy, efekty a animace a všichni sdílí jeden rozpočet. Proto se pořád stavějí kity a nestačí něco naskenovat a hotovo [(49:03)](https://www.youtube.com/watch?v=77xPHfzciiY&t=2943s), [(49:50)](https://www.youtube.com/watch?v=77xPHfzciiY&t=2990s). Autor používá 1024 textury, aby jich bylo málo, i za cenu častějšího opakování. Přechod na 2K zvedne hustotu z 512 na 1024 px na metr [(51:23)](https://www.youtube.com/watch?v=77xPHfzciiY&t=3083s). Autorovo pořadí bývá stejné: tilery, pak trimy, a když ani to nestačí, pečení s maskami [(52:10)](https://www.youtube.com/watch?v=77xPHfzciiY&t=3130s).

**Tilery na mřížce.** Kus postavený na metrové mřížce stačí rozbalit automaticky nebo planárně a nastavit texel density na 512 px na metr. Švy textury pak většinou navážou bez starostí, protože hrany kusů leží na mřížce [(52:56)](https://www.youtube.com/watch?v=77xPHfzciiY&t=3176s), [(53:43)](https://www.youtube.com/watch?v=77xPHfzciiY&t=3223s), [(54:31)](https://www.youtube.com/watch?v=77xPHfzciiY&t=3271s). Opakování tileru se pak rozbíjí vertex paintem a decaly [(55:17)](https://www.youtube.com/watch?v=77xPHfzciiY&t=3317s).

**Trim sheet z vlastní geometrie.** Autor staví trim sheet z kusů, které už v kitu má: lišty, obložení a pruhy dřeva vystřihne z geometrie a poskládá na plochu textury. Proto se pak všechno na trimu opravdu použije [(56:03)](https://www.youtube.com/watch?v=77xPHfzciiY&t=3363s), [(56:50)](https://www.youtube.com/watch?v=77xPHfzciiY&t=3410s). Celý oblouk by autor na trim asi nedával, stačí mu pruh dřeva [(57:36)](https://www.youtube.com/watch?v=77xPHfzciiY&t=3456s). Při rozbalování na trim jdou první na řadu hrany a zastíněná místa, protože tam detail rozhoduje. UV ostrůvek se položí tam, kde to na geometrii vypadá dobře, a když se detail trimu nevejde, přidá se do modelu edge loop [(59:09)](https://www.youtube.com/watch?v=77xPHfzciiY&t=3549s), [(59:55)](https://www.youtube.com/watch?v=77xPHfzciiY&t=3595s), [(1:00:47)](https://www.youtube.com/watch?v=77xPHfzciiY&t=3647s). Malé zmenšení, třeba z 512 na zhruba 480 px na metr, si nikdo nevšimne [(1:01:33)](https://www.youtube.com/watch?v=77xPHfzciiY&t=3693s). Sendvič pak střídá trim jako detail a tiler jako klidnou plochu, kterou se později „uzemní" sukněmi a decaly. Trim má navíc informaci o dutinách a usazeném prachu, a proto ho autor používá často. Když ale stačí tiler, vezme tiler [(1:04:45)](https://www.youtube.com/watch?v=77xPHfzciiY&t=3885s), [(1:05:32)](https://www.youtube.com/watch?v=77xPHfzciiY&t=3932s).

**Organický kus: dvě textury.** Kámen autor rozbalil v ZBrushi. Lepší cesta je podle něj rozbalit zjednodušený model a UV přenést na detailní přes Transfer Attributes v Mayi [(1:06:20)](https://www.youtube.com/watch?v=77xPHfzciiY&t=3980s), [(1:07:07)](https://www.youtube.com/watch?v=77xPHfzciiY&t=4027s). Na směru UV záleží jen u materiálů s vláknem, jako je dřevo [(1:07:53)](https://www.youtube.com/watch?v=77xPHfzciiY&t=4073s). Materiál kamene v UE skládá sdílené textury s unikátními [(1:08:39)](https://www.youtube.com/watch?v=77xPHfzciiY&t=4119s), [(1:09:26)](https://www.youtube.com/watch?v=77xPHfzciiY&t=4166s):
- sdílený tiler kamene a jeho odbarvená varianta, s kanály roughness, AO a height zabalenými do jedné textury,
- unikátní normal mapa kamene,
- unikátní textura se třemi maskami: opotřebení hran, dutiny s prachem a obecné rozbití povrchu.

Materiál má čtyři vrstvy jako material functions a výměnou tileru vznikne z téže sochy bílý kámen nebo obsidián [(1:10:12)](https://www.youtube.com/watch?v=77xPHfzciiY&t=4212s), [(1:11:00)](https://www.youtube.com/watch?v=77xPHfzciiY&t=4260s). Každý kámen tak potřebuje dvě textury místo obvyklých tří nebo čtyř [(1:12:33)](https://www.youtube.com/watch?v=77xPHfzciiY&t=4353s), [(1:13:19)](https://www.youtube.com/watch?v=77xPHfzciiY&t=4399s). Hustotu, kterou má unikátní textura nízkou (kámen kolem 64 px na metr proti cílovým 512), dorovná opakování tileru v materiálu. Autor 2K tiler opakuje zhruba čtyřikrát a přidá mikrodetail [(1:14:51)](https://www.youtube.com/watch?v=77xPHfzciiY&t=4491s), [(1:15:37)](https://www.youtube.com/watch?v=77xPHfzciiY&t=4537s).

**Proč ne samé unikáty.** Totéž platí pro sloupy a architekturu: čím méně materiálů, tím líp. Unikátní propy berou flexibilitu, protože nejde jedním parametrem přebarvit špínu v celé scéně, a tlačí texturní paměť nad limit, protože každý přinese vlastní textury [(1:16:23)](https://www.youtube.com/watch?v=77xPHfzciiY&t=4583s).

> **Pozn.:** Zabalené kanály a sdílené tilery jsou v UE vzor [master materiálu](materialy.md#master-material-pet-textur-nema-mit-kazdy-mesh). Číslo „dvě textury na kámen" platí pro autorův setup, ne obecně. Jde o princip: unikátní je jen to, co unikátní být musí.

**Souvislosti:** [Rejstřík: Tileable texture](../rejstrik.md#tileable-texture) · [Rejstřík: Trim sheet](../rejstrik.md#trim-sheet) · [Rejstřík: Channel packing](../rejstrik.md#channel-packing) · [Rejstřík: Material function](../rejstrik.md#material-function)

---

## Trim sheet jako systém: jedna textura, mnoho assetů, a kdy ne

**Zdroj:** [How AAA Studios Texture Huge Worlds | The Last of Us & Valorant Trim Sheet Workflows](https://www.youtube.com/watch?v=Jn9Zl5SO4EU) · [Class Creatives](https://www.youtube.com/channel/UCMY3Hz9bW0m6ERa6G4FNosg) · ~19 min, rozbor a ukázka ·
[Why AAA Games Use Trim Sheets (And How They Actually Work)](https://www.youtube.com/watch?v=Jw9X4HjlFpI) · [Zeref3DForge](https://www.youtube.com/channel/UCZYfkOHp8e_lHbRtR1cGYxQ) · ~5 min, výklad

**Shrnutí:** Trim sheet je textura s pruhy materiálů, například prken, kamene nebo kovových lišt, na kterou se UV různých assetů skládají po kouscích. Jedna textura tak obslouží celý kit a změna trimu se propíše do všech assetů najednou. Detail se přitom neztrácí ani na obřích plochách, protože pruh se opakuje podél své osy. Háček: trim sheet není jen textura, ale **systém**. Textura, UV a kusy kitu se navrhují dohromady. Pro unikátní hero asset nebo nepravidelné organické tvary obvykle dává větší smysl vlastní textura.

### Rozpad myšlenky

**Problém, který řeší.** Začátečnický postup „model, UV, bake, textura, hotovo" funguje pro jeden prop [(0:47)](https://www.youtube.com/watch?v=Jw9X4HjlFpI&t=47s). Prostředí ale tvoří stovky assetů. Když po třech týdnech na středověké vesnici vedoucí řekne „změňme dřevo", znamená to dvacet souborů, dvacet úprav a nový export i import. To podle autora není problém texturování, ale postupu [(0:47)](https://www.youtube.com/watch?v=Jw9X4HjlFpI&t=47s). Profesionálové se proto ptají, kolik assetů může použít stejné řešení, aby byl zítřejší asset snazší [(1:33)](https://www.youtube.com/watch?v=Jw9X4HjlFpI&t=93s). Jeho scéna stojí na dvou hlavních texturách, bezešvé stěně a jednom trim sheetu. Trámy, sloupy, dveře, okna i kovové kusy jsou z malého kitu nad stejným trimem [(2:19)](https://www.youtube.com/watch?v=Jw9X4HjlFpI&t=139s). Když se upraví trim, změní se všechno, co ho používá, a udržuje se jedna textura místo dvaceti [(3:53)](https://www.youtube.com/watch?v=Jw9X4HjlFpI&t=233s).

**Jak vzniká.** Detail se vymodeluje ve vysokém rozlišení a zapeče na jednoduchou plochu s vodorovnými pruhy. Color ID rozliší materiály, třeba kámen, dřevo a kov [(3:06)](https://www.youtube.com/watch?v=Jw9X4HjlFpI&t=186s), [(3:14)](https://www.youtube.com/watch?v=Jn9Zl5SO4EU&t=194s). Trimy jde dělat procedurálně v Substance Designeru i modelováním v jakémkoli DCC [(4:01)](https://www.youtube.com/watch?v=Jn9Zl5SO4EU&t=241s). Stěna se pak poskládá z pruhů: zkopírovat proužek geometrie, oddělit ho, nechat ho zopakovat array modifierem a posunout UV na jiný pruh. Roztažením ve směru pruhu se zvedne texel density [(4:47)](https://www.youtube.com/watch?v=Jn9Zl5SO4EU&t=287s), [(5:34)](https://www.youtube.com/watch?v=Jn9Zl5SO4EU&t=334s). Místo spousty materiálů s vlastními sadami textur je všechno v jedné sadě: kvalita i optimalizace zároveň [(5:34)](https://www.youtube.com/watch?v=Jn9Zl5SO4EU&t=334s).

**Hrany, které navazují.** Ukázka s fontánou ukazuje, proč trim drží detail lépe než klasická textura objektu. Kulatý objekt s texturou přes celý povrch, i když je UV čtvrtiny opakované, dá při 4K jen průměrnou hustotu. Trim ze čtyř pruhů se zkosenými hranami pod 45° drží detail i zblízka [(12:37)](https://www.youtube.com/watch?v=Jn9Zl5SO4EU&t=757s), [(13:24)](https://www.youtube.com/watch?v=Jn9Zl5SO4EU&t=804s), [(17:18)](https://www.youtube.com/watch?v=Jn9Zl5SO4EU&t=1038s). Aby zkosení pokračovalo, musí na sebe navazovat hrany stejného druhu. Když se setká špatná dvojice, místo zkosení vznikne důlek a ostrůvek se musí otočit o 180° [(14:11)](https://www.youtube.com/watch?v=Jn9Zl5SO4EU&t=851s), [(15:44)](https://www.youtube.com/watch?v=Jn9Zl5SO4EU&t=944s), [(16:30)](https://www.youtube.com/watch?v=Jn9Zl5SO4EU&t=990s). Zarovnání na pruhy urychlí bezplatný skript pro rozbalování na trim [(14:58)](https://www.youtube.com/watch?v=Jn9Zl5SO4EU&t=898s).

**Jak to dělají velké hry.**
- **Assassin's Creed Mirage:** trim se opakuje přes velké plochy bez ztráty kvality. Loď s dřevěnými panely i dveře zhruba desetkrát větší než postava jsou ostré a opakování rozbíjí špína a pravděpodobně vertex blending a decaly [(1:40)](https://www.youtube.com/watch?v=Jn9Zl5SO4EU&t=100s), [(2:26)](https://www.youtube.com/watch?v=Jn9Zl5SO4EU&t=146s).
- **The Last of Us:** jeden asset používá tři sady trimů a tentýž kamenný trim se vrací po celém prostředí. Mech přes vertex blending a geometrie popínavých rostlin skryjí opakování [(6:22)](https://www.youtube.com/watch?v=Jn9Zl5SO4EU&t=382s), [(7:08)](https://www.youtube.com/watch?v=Jn9Zl5SO4EU&t=428s). Vertex color potřebuje vrcholy, takže i plochá stěna má kolem osmi ploch [(7:54)](https://www.youtube.com/watch?v=Jn9Zl5SO4EU&t=474s).
- **Valorant:** budovy a velké stavby texturuje hlavně tilery a trimy, vlastní textury mají propy podle potřeby, třeba kávovar nebo vysokozdvižný vozík. Blockout přitom slouží souběžně, aby neblokoval ostatní vývojáře ani osvětlovače [(9:27)](https://www.youtube.com/watch?v=Jn9Zl5SO4EU&t=567s), [(10:14)](https://www.youtube.com/watch?v=Jn9Zl5SO4EU&t=614s). Stejný postup, úplně jiný styl [(11:02)](https://www.youtube.com/watch?v=Jn9Zl5SO4EU&t=662s).

**Kdy ne.** Trim sheet patří tam, kde víc assetů sdílí stejnou materiálovou informaci: stěny, trámy, sloupy, dveře a jiná modulární architektura. Unikátní hero asset a nepravidelné organické tvary obvykle potřebují vlastní texturu. Pravidlo zní: když assety můžou sdílet materiál, použij trim, a když asset potřebuje vlastní povrch, necpi ho do trimu [(4:39)](https://www.youtube.com/watch?v=Jw9X4HjlFpI&t=279s).

> **Pozn.:** Zeref3DForge a workshop z [první myšlenky](#kit-jako-lego-co-nejmene-kusu-mrizka-v-metrech-a-zoo-na-zkousku) se potkávají v jedné větě: trim se navrhuje s kitem, ne po něm. Workshop ho rovnou staví z geometrie kitu. Zapečená zkosení, díky kterým jdou modely stavět s ostrými hranami, popisuje [TLOU trim sheet](env-breakdowny.md#tlou-trim-sheet-ktery-nahradil-tisice-bake). Video Class Creatives je zčásti ukázkou z jejich kurzu (masterclass) [(11:51)](https://www.youtube.com/watch?v=Jn9Zl5SO4EU&t=711s) a lektor kurzu staví packy nejdřív v UE4 kvůli kompatibilitě.

**Souvislosti:** [Rejstřík: Trim sheet](../rejstrik.md#trim-sheet) · [Rejstřík: Texel density](../rejstrik.md#texel-density) · [Rejstřík: Vertex painting](../rejstrik.md#vertex-painting) · [Rejstřík: Decal](../rejstrik.md#decal)

---

## Organický kit a spoje: zabořit, nechat růst od zdroje, zakrýt šev

**Zdroj:** [The easiest Way to Create Modular 3D Kits Without Stress](https://www.youtube.com/watch?v=77xPHfzciiY) · [Beyond Extent](https://www.youtube.com/channel/UCPHrTip4HJDajQG3eTKhAqQ) · ~87 min, workshop (části o organickém kitu, blendování a kitbashingu)

**Shrnutí:** Organický kit, tedy skály, kameny nebo rostliny, se nezacvakává do mřížky. Kusy se zabořují do sebe, pootáčejí mimo pravý úhel a rozmisťují od největšího k nejmenšímu, jako by se šířily od zdroje. Švy mezi kusy i mezi kity skrývají spoje: čtyři texturové (vertex blending, decaly, sukně, světová projekce) a k nim geometrické (zabořené kusy, sutiny a úlomky, vegetace). Háček: ani organické kusy se nesmějí libovolně škálovat. Zapečené textury i tilery jsou dělané pro určitou texel density a ta by se rozbila.

### Rozpad myšlenky

**Velké, střední, malé.** Organický kit má pivoty uprostřed a kusy ve třech velikostech, k tomu tvarově jednoduchou „kupku", která se zaboří mezi jiné kusy a přemostí mezeru [(40:33)](https://www.youtube.com/watch?v=77xPHfzciiY&t=2433s), [(41:19)](https://www.youtube.com/watch?v=77xPHfzciiY&t=2479s). V ukázce kaňonu se velké skály pootáčejí mimo 90°, protože skály rostou směrem a mají pohyb [(42:06)](https://www.youtube.com/watch?v=77xPHfzciiY&t=2526s). Střední balvany se zaboří do země nebo do stěny a sdílené materiály pomůžou, aby k sobě pasovaly; přechod případně dorovná sukně nebo další kus [(42:52)](https://www.youtube.com/watch?v=77xPHfzciiY&t=2572s). Škálování ale autor nedoporučuje. Kusy mají mít tři velikosti právě proto, aby neutrpěla texel density, na kterou jsou zapečené textury a tilery dělané [(43:38)](https://www.youtube.com/watch?v=77xPHfzciiY&t=2618s), [(44:25)](https://www.youtube.com/watch?v=77xPHfzciiY&t=2665s).

**Šíření od zdroje.** Organická scéna podle autora roste jako virus. Od zdroje, třeba obří skály, přes velké kameny až po malé kousky, které „vykrvácí" do okolí. Stejně funguje vegetace: uprostřed původní trs, na okrajích menší a mladší rostliny [(45:12)](https://www.youtube.com/watch?v=77xPHfzciiY&t=2712s), [(45:59)](https://www.youtube.com/watch?v=77xPHfzciiY&t=2759s). U vegetace to znamená velké rostliny, pak kapradiny, tráva a nakonec mech a květiny [(47:31)](https://www.youtube.com/watch?v=77xPHfzciiY&t=2851s). Drobné kusy se dají poskládat do hezkého shluku a ten pak umisťovat a otáčet jako skupinu, takže vypadá dobře z jakéhokoli úhlu [(44:25)](https://www.youtube.com/watch?v=77xPHfzciiY&t=2665s), [(45:12)](https://www.youtube.com/watch?v=77xPHfzciiY&t=2712s). Jako reference pro tvary kupek poslouží organické assety z Megascans [(46:45)](https://www.youtube.com/watch?v=77xPHfzciiY&t=2805s).

**Čtyři spoje texturou** [(1:17:09)](https://www.youtube.com/watch?v=77xPHfzciiY&t=4629s):
- **vertex blending** se čtyřmi nebo pěti vrstvami tilerů, takže podlaha s mechem a kámen s mechem do sebe přejdou [(1:17:56)](https://www.youtube.com/watch?v=77xPHfzciiY&t=4676s),
- **decaly** jako plovoucí geometrie, které spoj zakryjí,
- **sukně (skirt)**, tedy pruh geometrie na kusu, který dělá přechod mezi kusem a zemí. Autor se ho naučil na Call of Duty, kde se sukně dávaly spoustě modelů [(1:18:42)](https://www.youtube.com/watch?v=77xPHfzciiY&t=4722s),
- **světová projekce** sněhu nebo mechu přes všechno, hlavně u organických kusů.

Přechod mezi kusy přemostí i samostatné modely sukní a kupek, hlavně u organického kitu a sutin. Do kitu je autor přidává až ke konci, když stojí jeho základ [(1:19:29)](https://www.youtube.com/watch?v=77xPHfzciiY&t=4769s).

**Spoje geometrií:** kusy zabořené do sebe jako u skalního kitu, hromádky sutin nebo rozházené úlomky a vegetace, která skryje šev mezi skalním a architektonickým kitem [(1:19:29)](https://www.youtube.com/watch?v=77xPHfzciiY&t=4769s), [(1:20:16)](https://www.youtube.com/watch?v=77xPHfzciiY&t=4816s).

**Kitbashing.** Když se dva kity, třeba architektura a trubky, spojí do nových kusů, říká se tomu kitbashing [(1:20:16)](https://www.youtube.com/watch?v=77xPHfzciiY&t=4816s). Autorův kit propů pro Ásgard sdílí jeden shader, takže scénu zaplní bez spousty unikátních textur a draw callů [(1:21:03)](https://www.youtube.com/watch?v=77xPHfzciiY&t=4863s), [(1:21:50)](https://www.youtube.com/watch?v=77xPHfzciiY&t=4910s).

**Proč to celé.** Cílem jsou optimální a znovupoužitelné assety v nedestruktivním postupu. Kdykoli se jde vrátit třeba do ZBrushe, aniž by se rozbilo všechno ostatní [(1:21:50)](https://www.youtube.com/watch?v=77xPHfzciiY&t=4910s), [(1:22:36)](https://www.youtube.com/watch?v=77xPHfzciiY&t=4956s). Úspornost prostředí je dávání a braní s postavami, efekty a animacemi: optimální kit uvolní místo pro víc propů, lepší světlo a stíny nebo efekty. Autorovi pomohlo, že s kity pracoval i na vlastních projektech, a radí to ukázat i v portfoliu [(1:23:22)](https://www.youtube.com/watch?v=77xPHfzciiY&t=5002s).

> **Pozn.:** Šíření od zdroje by se dalo zapsat i jako pravidlo do PCG grafu. To je naše úvaha, zdroj na to knihovna zatím nemá; jak PCG rozmisťuje body, ukazují [Základy PCG](pcg-zaklady.md). Vrstvy prolnuté vertex colorem a podle výšky staví v UE [Nanite displacement](materialy.md#nanite-displacement-relief-malovany-vertex-colorem). Začátečník skálu obvykle prostě zvětší. Autor radši dělá víc velikostí kusu, protože škálování rozbije texel density.

**Souvislosti:** [Rejstřík: Kitbashing](../rejstrik.md#kitbashing) · [Rejstřík: Skirt](../rejstrik.md#skirt) · [Rejstřík: Vertex painting](../rejstrik.md#vertex-painting) · [Rejstřík: Triplanar projection](../rejstrik.md#triplanar-projection)

---

## Beauclair: 500 MB textur na celé město, orientační body, clony a jeden shader na čtvrť

**Zdroj:** [How The Witcher 3 Built Its Cities | Environment Breakdown](https://www.youtube.com/watch?v=cCovMWRSL6o) · [Next Level Game Art](https://www.youtube.com/channel/UCmPBLkozH1irLObN0Q3_aJw) · ~21 min, breakdown (DLC Blood and Wine)

**Shrnutí:** Beauclair z DLC Blood and Wine měl na celé město rozpočet 500 MB texturní paměti, a unikátní textura jednoho domu by při nové hustotě vyšla na 72 MB. Řešení CD Projekt Red nebyla jen technická. Layout dostal další orientační body a clony, které zkrátily průhledy a daly enginu čas na streamování. Budovy se staví z kitů a jeden vertex-blend shader obléká celou bohatou čtvrť tak, že stejné domy vypadají různě. Háček: zkušený environment artista podle autora nedodává jen assety, ale **umělecká řešení technických omezení**.

### Rozpad myšlenky

**Orientace.** Město leží na svahu a vede hráče dvěma orientačními body z knižní předlohy: horou, která pomáhá orientaci v celém regionu a je vidět z mnoha částí města, a palácem na severu [(0:49)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=49s). Čím výš, tím bohatší čtvrť, až k paláci, a každá čtvrť má vlastní architekturu [(1:35)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=95s). První layout měl ale tři rizika [(2:22)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=142s):
- místa, odkud není vidět ani hora, ani palác,
- extrémně dlouhé průhledy, drahé pro engine,
- tržiště plné NPC.

Tým proto zvýšil radnici, přidal chrám jako další orientační bod a přestavěl ulice tak, aby ústily na výhled na některý z nich [(2:22)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=142s), [(3:09)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=189s).

**Clony.** Dlouhé průhledy přeruší vizuální clona. U tržiště jen částečná, aby hráč věděl, že tam je [(3:09)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=189s). Částečné clony navíc skrývají doskakování LODů [(3:56)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=236s). Nejtěžší bylo hlavní náměstí: festival vína, spousta assetů a NPC a sedm domů s interiéry. Soukenická hala se tam stala clonou, která náměstí oddělí od zbytku města a dá enginu čas načíst další části [(4:12)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=252s). Výškové rozdíly a zakřivené ulice řídí, co hráč vidí, a tedy i co se musí načíst. Město přitom působí jako skutečné středověké [(5:03)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=303s), [(5:26)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=326s). Důležitá místa zůstala, kde byla, jen se město otevřelo a líp se jím chodí [(5:26)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=326s).

**Rozpočet a jak se do něj vejít.** Od tech artu přišlo 200 MB trvale nahraných textur pro proxy, tedy velmi vzdálené assety, dalších 300 MB pro obsah u hráče a půl milionu trojúhelníků celkem [(6:13)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=373s). Tým vybral šest nejnáročnějších míst. Když budou v rozpočtu ona, bude i zbytek města [(6:13)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=373s). Raná zpráva QA ukázala překročení ve všem, a tak se nevymýšlelo nic nového, jen se upravily nástroje ze základní hry [(6:59)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=419s).
- Streamování LODů: nad 50 m proxy, pod 50 m LOD1, pod 20 m LOD0 a interiér. LOD0 domu měl 30 000 trojúhelníků, proxy má zapečenou vlastní texturu a váží jen 0,5 MB [(7:47)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=467s).
- Okleštěné interiéry mají materiály na stěnách a podlaze, aby nebyla vidět prázdnota, když dovnitř vejde NPC. Parallax shader navozuje dojem, že je uvnitř něco, i když jde jen o pár ploch [(7:47)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=467s), [(8:34)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=514s).
- Occlusion culling přes middleware Umbra: když je vidět jen střecha domu, streamují se jen její dva meshe za 3 500 trojúhelníků, se středem domu přibude 6 000. Proto jsou modulární kity v otevřeném světě nutnost [(8:50)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=530s).

**Kit radnice.** Hustota vrcholů není úplně rovnoměrná a k vertex paintingu se rozbor vrací u shaderu [(9:37)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=577s). Hlavní fasáda soukenické haly je jeden kus, protože se jinde neopakuje [(9:37)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=577s). Stěny a sloupy pokračují několik metrů pod zem, takže na svahu jdou postavit kamkoli bez úprav v DCC, za cenu pár polygonů [(10:24)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=624s). Některé celé budovy jsou jediný asset použitý na mnoha místech mapy a shader je převlékne tak, že si opakování většina hráčů nevšimne [(11:12)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=672s).

**Jeden shader na čtvrť.** DLC zdvojnásobilo texel density ze 1024 px na 2 m na 1024 px na metr. Unikátní textura jednoho domu by tak měla kolem 5K × 6K na stranu, čtyřikrát, a to je těch 72 MB [(12:45)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=765s). Tech artista proto napsal vertex-blend shader [(12:45)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=765s), [(13:31)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=811s), [(14:01)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=841s), [(14:17)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=857s):
- masky prolínají vrstvy a každá vrstva má vlastní barevný nádech,
- navrch jdou decaly se zatékáním a prasklinami s nastavitelným opakováním,
- falešná okluze přidá hloubku,
- vertex paint se maloval v 3ds Max, protože u vlastního enginu se maluje v DCC.

Hodnota přiřazená vrcholu vybírá sadu textur [(15:05)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=905s). Začínali se třemi sadami a skončili u sedmi a dvou trim sheetů. **Každá budova bohaté čtvrti používá tenhle jediný shader** [(15:05)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=905s), [(15:51)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=951s). Sady textur leží v texture arrays (barva, normal, roughness, maska) a barva se nastavuje v material instanci [(15:51)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=951s). Výsledek: stejný materiál, různě vypadající domy, a město přitom drží pohromadě [(14:17)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=857s).

**Dekorace jako hotové balíčky.** Takzvaný deco tým připravil zaměnitelné balíčky pro interiéry a tržní stánky, entity, kterým jiné enginy říkají prefaby. Zařídit místo pak znamenalo přetáhnout balíček, minuty místo hodin [(16:32)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=992s), [(17:18)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=1038s). Podle jednoho z artistů by se týmy neměly bát iterovat: každá iterace je přiblížila cílové kvalitě. Bez komunikace s level designem, grafickými programátory a tech artisty by to nešlo [(18:36)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=1116s), [(19:22)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=1162s).

> **Pozn.:** Orientační body a clony jsou učebnicový level design. Pravidlo, že [landmark musí být jediný svého druhu](../teorie/level-design-solo.md#tema-ospravedlnuje-mechaniky-a-landmark-musi-byt-jediny-sveho-druhu), tu dostává i technický důvod: tatáž stavba vede hráče a zároveň šetří streamování. Resident Evil Requiem zase schovává nahrávání za dveře a cutscény, viz [Jak to dělá Resident Evil](levely-a-streaming.md#jak-to-dela-resident-evil-requiem). Proč u vertex blendingu záleží na hustotě geometrie, ukazuje [Naughty Dog](env-breakdowny.md#naughty-dog-shadery-misto-polygonu-a-nastroj-misto-modelovani): geometrie tam slouží blendování, ne siluetě. Video propaguje autorův kurz a partnerský web s balíčky tutoriálů [(11:12)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=672s), [(17:48)](https://www.youtube.com/watch?v=cCovMWRSL6o&t=1068s).

**Souvislosti:** [Rejstřík: Landmark](../rejstrik.md#landmark) · [Rejstřík: Visual blocker](../rejstrik.md#visual-blocker) · [Rejstřík: LOD](../rejstrik.md#lod) · [Rejstřík: Occlusion culling](../rejstrik.md#occlusion-culling) · [Rejstřík: Texture array](../rejstrik.md#texture-array) · [Rejstřík: Prefab](../rejstrik.md#prefab)

---

## Mortal Shell 2: špičkový vzhled od třiceti lidí, málo materiálů a hodně masek

**Zdroj:** [How 30 Devs Made One of 2026's Best Looking Games | Mortal Shell 2](https://www.youtube.com/watch?v=SleW5iuwyIA) · [Next Level Game Art](https://www.youtube.com/channel/UCmPBLkozH1irLObN0Q3_aJw) · ~21 min, breakdown (rozbor herních souborů, UE 5.2)

**Shrnutí:** Mortal Shell 2 udělal tým kolem 30 až 35 lidí v Unrealu 5.2. Podle autora videa patří mezi nejlépe vypadající hry roku, a přitom běží hladce. Rozbor jeho souborů ukazuje tři páky:
- svět skládaný z modulárních kitů s Nanitem,
- malá knihovna tilerů (autor v souborech našel asi osm sad kamenných zdí, dvě omítky a pět dřev), rozehraná RGB maskami, material functions a víc než 25 LUTy,
- design světa, který sám pomáhá výkonu: kompaktní mapa, dlouhé průhledy skoro vždy jen jako výhledy a úzké průchody, ve kterých se načítá další oblast.

Háček: část assetů a textur je z Megascans, stejných, jaké používají tisíce studentů, a přesto to není poznat. Rozdíl dělají materiály a shadery.

### Rozpad myšlenky

**Proti „UE5 vypadá všude stejně".** Autor připomíná, že Unreal je nástroj pro mnoho oborů, nejen hry [(1:38)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=98s), [(2:24)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=144s). Když tým stihne odstranit, co nepotřebuje, a sáhnout do kódu, výsledek vypadá jinak. Studio to ukázalo už na prvním dílu, kde boj narazil na strop Blueprintů, a tak přibral programátora C++ [(2:24)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=144s), [(3:11)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=191s).

**Nanite a kity.** Po vypnutí Nanitu konzolí jsou mnohé plochy úplně ploché a textury roztažené. S Nanitem se detail vrátí a pracuje se světlem i stíny [(3:57)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=237s). Celý svět stojí na kitech: stěny, střechy, dveře, prkna, trámy i sloupy [(4:44)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=284s). Podle portfolia jednoho z artistů dělal high poly spoluzakladatel studia a materiálový setup art director. Artista sám převedl high poly do low poly, rozbalil UV, připravil masky a kolize [(4:44)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=284s), [(5:31)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=331s).

**Málo materiálů, hodně variací.** Svět kombinuje textury z Megascans s vlastní knihovnou a vlastní vzhled mu dávají shadery a postprocess s víc než 25 LUTy [(7:06)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=426s). Herní soubory obsahují RGB masky a material functions pro opacity masky, triplanární projekci a masky kanálů [(7:06)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=426s), [(7:52)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=472s). Tilerů je podle všeho málo: autor v souborech našel jen asi osm sad kamenných zdí, dvě omítky, pět dřev a pro organické plochy dvě sady písku a oblázků a osm kamene pro zem. Při hraní si toho opakování nevšimneš [(7:52)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=472s). Počasí se mění po regionech, ne dynamicky, a materiály mají funkce pro kapky deště, mokrost a vzory deště [(8:40)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=520s). Megascans assety i textury jsou podle autora v oboru běžné a u malého týmu ještě pochopitelnější. Zároveň přiznává, že jsou jedním z důvodů, proč hry působí podobně: když artisti nestihnou vytvořit vlastní assety a sady textur, hry si opravdu začnou být podobné. Tady ale tým materiály a shadery přizpůsobil natolik, že se to poznat nedá [(10:59)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=659s), [(11:46)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=706s). Na mraky, volumetriku a mlhu autor v souborech poznal několik nástrojů z Fabu, což malému studiu pravděpodobně ušetřilo čas i peníze [(11:46)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=706s), [(12:33)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=753s).

**Výkon začíná u designu.** Svět je větší než v prvním dílu, ale kompaktnější. Arény spojují mosty, budovy nebo útesy a dlouhé průhledy jsou skoro vždy jen výhledy [(12:33)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=753s), [(13:20)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=800s). Úzké průchody, kterými se hráč protahuje, jsou okamžiky, kdy se načítá další oblast. Dungeony jde nahrávat plynule, nebo s obrazovkou načítání na několik sekund [(13:20)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=800s), [(14:07)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=847s).

**Co ukázala měření.** Autor cituje dva weby, které hru měřily:
- Lumen má osekaný rozpočet. Světové radiance probe jsou na středním a vysokém nastavení vypnuté a na ultra poloviční; tým zvolil výkon před obrazem, za cenu viditelných artefaktů Lumenu [(14:07)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=847s).
- Nastavení stínů mění jen polostín [(14:07)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=847s).
- Video paměť se mezi nejnižším a nejvyšším nastavením liší jen o asi 300 MB a na 1440p s ultra texturami stačí 8GB karta [(14:55)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=895s).
- Předkompilace PSO prakticky odstranila záškuby z kompilace shaderů [(14:55)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=895s).

Od sebe autor přidává, že u většiny sad textur z Megascans našel v souborech zabalené kanály: barvu s roughness v alfě, metalness s roughness a výškou a další varianty. Podle něj je to jeden z hlavních tahů pro texturní paměť [(14:55)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=895s), [(15:41)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=941s).

**Varování pro absolventy.** Podle autora se dnes většina absolventů učí na UE5 a mnozí učitelé jim radí, ať nepečou normály a sypou do enginu high poly s Nanitem a 4K mapami. Pak nedostanou ani pohovor, protože studia s vlastními enginy mají jiná omezení [(17:13)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=1033s), [(17:59)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=1079s). Radí rozebírat obsah her nástroji pro modding, studovat jejich modely a zkusit do hry vložit vlastní assety [(18:45)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=1125s), [(19:32)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=1172s).

> **Pozn.:** Rozbor stojí na herních souborech, moddingu, cizích měřeních a portfoliu jednoho artisty, ne na výpovědi studia o druhém dílu, a autor u některých kanálových zkratek sám přiznává, že si není jistý. Proti zjednodušování ve stylu „Nanite vyřeší polygony" stojí [Spor o Nanite](nanite-do-hloubky.md#spor-o-nanite-co-tvrdi-kritika-a-co-z-toho-plati). Zabalené kanály a malá knihovna tilerů jsou tentýž princip jako [dvě textury na kámen](#textury-pro-kit-tilery-trimy-a-masky-dve-textury-na-kamen). Proč na předkompilaci [PSO](../rejstrik.md#pso) tolik záleží, vysvětluje [Jak to vidí hráč](frame-pacing.md#jak-to-vidi-hrac-360p-upscaling-a-stutter). Video propaguje autorův kurz a partnerský web [(6:19)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=379s), [(12:33)](https://www.youtube.com/watch?v=SleW5iuwyIA&t=753s).

**Souvislosti:** [Rejstřík: Megascans](../rejstrik.md#megascans) · [Rejstřík: Channel packing](../rejstrik.md#channel-packing) · [Rejstřík: LUT](../rejstrik.md#lut) · [Rejstřík: Nanite](../rejstrik.md#nanite) · [Lumen: rozpočet a binární hledání](gpu-pruchod.md#lumen-rozpocet-a-binarni-hledani)
