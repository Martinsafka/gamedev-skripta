# 2D vizuál: pixel art a izometrie

Dvě rozhodnutí, která u 2D hry padnou nejdřív a nejdéle drží: **jaké má hra rozlišení** a **z jakého úhlu se na svět díváš**. Obě vypadají jako technikálie a obě jsou ve skutečnosti designové volby s dlouhým stínem — určují, kolik práce dá jeden asset, jak čitelná bude scéna a co všechno hráč uvidí. Tahle kapitola spojuje dva zdroje z opačných konců zkušenosti: vývojáře, který přesvědčuje netvůrce, že na pixel art stačí hrstka nastavení, a autorku, která na vlastní hře popisuje, co izometrie stojí. Na okraji přibyl krátký návod, jak z AI obrázků poskládat [parallax vrstvy](#layering-a-verticalita-staticka-kamera-jako-scenografie), které k sobě sedí.

---

## Pixel art je rozhodnutí, ne nouzové řešení

**Zdroj:** [You Don't Need to Be an Artist to Make Great Game Art](https://www.youtube.com/watch?v=3eg5Lp3pGNk) · [TechDad Impact](https://www.youtube.com/channel/UCRGAMb_zSjT4hBVdB3JNyPw) · ~14 min, tutoriál a úvaha

**Shrnutí:** Pixel art je pro sólo vývojáře atraktivní ze dvou důvodů: **nostalgie** má reálnou kupní sílu a **omezení** (nízké rozlišení, omezená paleta) vyrábějí konzistentní vizuál skoro sama od sebe. Cenou je, že se řemeslo učí dlouho a **každý pixel váží víc**. Technicky přitom stojí celá věc na třech nastaveních, která rozhodují o tom, jestli hra vypadá ostře, nebo rozmazaně.

### Rozpad myšlenky

Nejdřív ta tři nastavení, protože bez nich vypadá i dobrý art špatně. Video je ukazuje v Godotu [(1:33)](https://www.youtube.com/watch?v=3eg5Lp3pGNk&t=93s), ale principy jsou univerzální:

1. **Filtrování textur na `nearest`** [(1:33)](https://www.youtube.com/watch?v=3eg5Lp3pGNk&t=93s). Jakákoli hladká filtrace pixel art rozmaže — místo ostrých čtverců dostaneš kaši. Tohle je globální přepínač, ne per-asset volba.
2. **Nízké interní rozlišení** [(2:21)](https://www.youtube.com/watch?v=3eg5Lp3pGNk&t=141s): autor používá **640×360**, protože drží poměr **16:9** jako většina monitorů; pro „NES vzhled" se hodí **320×180**. Zisk není estetický, ale ekonomický: **tvoříš assety v nízkém rozlišení, a přesto naplníš 4K displej** — nemusíš kreslit detail, který velké rozlišení jinak vyžaduje.
3. **Integer scaling** [(3:07)](https://www.youtube.com/watch?v=3eg5Lp3pGNk&t=187s): škálování **celými čísly** (2×, 3×) místo 2,5× nebo 2,75×. Neceločíselné zvětšení totiž rozdělí jeden zdrojový pixel mezi dva cílové a hrana se rozmaže — proto se k tomu přidává zachování poměru stran, aby se obraz nedeformoval.

Proč vůbec pixel art volit [(3:53)](https://www.youtube.com/watch?v=3eg5Lp3pGNk&t=233s) — a tady video mluví za velkou část indie scény. Jednak **nostalgie je silná droga**: „spousta nás starých šedivých lišek chce znovu prožít dětství skrz moderní indie hry", a dobře provedený retro styl **zasahuje publikum s kupní silou**. Jednak je to **efektivní volba pro jednoho člověka, protože stojí na omezeních** — nižší rozlišení a menší paleta mají tendenci **vyrábět konzistentní a jednotný vizuál**, což je přesně to, co sólo tvůrci nejčastěji chybí.

Video ale hned dodává protiváhu, kterou většina nadšených doporučení vynechá [(4:40)](https://www.youtube.com/watch?v=3eg5Lp3pGNk&t=280s): **pixel art se učí dlouho, a protože máš míň plochy, každý jednotlivý pixel má větší dopad na kvalitu a čitelnost** — „nepoužívej je nedbale". Nízké rozlišení tedy neznamená míň práce na assetu, ale **jinou práci**: místo detailu se řeší silueta a čitelnost.

Zbytek videa je sada praktických postojů, které stojí za převzetí i mimo pixel art:

- **Nástroj nemusí stát nic** [(4:53)](https://www.youtube.com/watch?v=3eg5Lp3pGNk&t=293s): autor doporučuje Kritu (open source, bez účtů a aktivací, umí i frame-by-frame animace a export snímků), zatímco specializovaný Aseprite je za dvacet dolarů — což označuje za naprosto přijatelnou cenu, jen ho sám nepotřebuje.
- **Začni jednoduše a používej reference** [(5:41)](https://www.youtube.com/watch?v=3eg5Lp3pGNk&t=341s): „tvoř rozpoznatelné tvary a vyhýbej se vysokému detailu"; a rovnou k tomu nejlepší věta videa — **„nesrovnávej se s ostatními; tvým úkolem je být lepší než včerejší verze tebe samého."**
- **Míř výš než na první nápad** [(7:17)](https://www.youtube.com/watch?v=3eg5Lp3pGNk&t=437s): autor přiznává, že nemá rád simplistický pixel art, který jen napodobuje éru NES, a ptá se, **proč nemířit na úroveň Sega Genesis nebo Super Nintenda** (jmenuje Streets of Rage 2 nebo Seiken Densetsu 3). K tomu dodává realistickou naději: „talent těch artistů mi nejspíš chybí, **ale mám víc pixelů a moderní nástroje — snad to hřiště trochu vyrovná**."
- **Nemaluje pixel po pixelu** [(8:03)](https://www.youtube.com/watch?v=3eg5Lp3pGNk&t=483s) kromě postav a nepřátel — zbytek maluje štětci s plynulými přechody. Zdůvodnění je historicky přesné: **hry devadesátek se hrály na CRT monitorech, kde pixely nebyly ostré kostky**, takže měkčí přechody jsou věrnější poctou, než jak si tu dobu pamatujeme.
- **Nepoužívá tilesety** [(8:50)](https://www.youtube.com/watch?v=3eg5Lp3pGNk&t=530s) a přiznává to jako kompromis. Dlaždice vznikly proto, že je konzole osmdesátých let uměly renderovat extrémně rychle; dnes je enginy podporují, ale on radši maluje celý level jako jeden dlouhý obraz a **exportuje ho po vrstvách zezadu dopředu**. Cena: **pořád vyrábí nové assety místo skládání ze stavebnice** — obhájitelné jen tím, že dělá střílečku, kde nejsou potřeba složité layouty, ale výpravné kulisy.

> **Pozn.:** Video je celé natočené v Godotu, což je v knihovně jinak postavené na Unrealu výjimka — konkrétní cesty v menu tedy neplatí, principy ano. A závěrečná věta míří přesně na čtenáře, který art odkládá [(11:58)](https://www.youtube.com/watch?v=3eg5Lp3pGNk&t=718s): **„technické věci působí jako zeď, ale jsou to dveře, které jsi ještě neotevřel. Začni jednoduše, udělej nejdřív něco ošklivého a pak iteruj."**

**Souvislosti:** [Vizuální komunikace: krása je volitelná](vizualni-komunikace.md#dve-strany-artu-krasa-je-volitelna-srozumitelnost-ne) · [Scope: design by constraint](scope.md#design-by-constraint-krabice-napred-napad-dovnitr) *(omezení jako zdroj konzistence)* · [Sólo vývoj: pipeline jednoho člověka](solo-vyvoj.md#pipeline-jednoho-cloveka-gdd-engine-verzovani-cizi-assety) · [Kamera: zoom v pixel artu](kamera.md#look-ahead-focus-objekty-a-zoom-ktery-nesel) · [Praxe: PS1 estetika](../praxe/ps1-estetika.md#textura-dela-styl-rozliseni-kontrast-a-nearest) *(tatáž disciplína ve 3D)* · [Rejstřík: integer scaling](../rejstrik.md#integer-scaling) · [Rejstřík: pixel-perfect](../rejstrik.md#pixel-perfect)

---

## Izometrie: perspektiva bez perspektivy a její kompromisy

**Zdroj:** [How we made our Isometric Game Art! ★ || GOLEMBERT Devlog #12](https://www.youtube.com/watch?v=UYBzqCldDDI) · [Studio Firlefanz](https://www.youtube.com/channel/UCAfPaxLy2g5uy7IrQToCcCg) · ~9 min, devlog

**Shrnutí:** Izometrie má jednu definiční vlastnost, ze které plyne všechno ostatní: **neobsahuje realistickou perspektivu, takže se objekty dozadu nezmenšují.** Díky tomu dává skvělý přehled o prostoru a snese hodně detailu, aniž by si věci překážely — a proto po ní sahají budovatelské a simulační hry. Cenou je, že perspektivu musíš držet **všude**, jinak se objekty odmítnou slučovat s prostředím.

### Rozpad myšlenky

Východisko je technické omezení, ne estetika [(0:50)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=50s): hra není ve 3D, takže **kamera musí zůstat statická**. Inspirací byly Harvest Moon a Stardew Valley, které nemají čistý pohled shora — vidíš u nich i boky objektů, čemuž se říká **oblique** perspektiva. Autorka chtěla tentýž pocit s větší hloubkou, a k tomu se izometrie hodí.

Její klíčová vlastnost [(0:50)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=50s): **v izometrii neexistuje úběžník, takže se vzdálené objekty nezmenšují**. Proto ji volí hry, které potřebují dobrý přehled o prostředí (jmenuje Roller Coaster Tycoon a The Sims), a proto je oblíbená na mobilech [(1:38)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=98s) — **umožňuje víc detailu, aniž by si prvky navzájem překážely**.

Nejcennější je ale přiznaný kompromis [(1:38)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=98s). Jejich hra je izometrická jen zčásti: objekty jako vyvýšené záhony ano, **ale většina prostředí je pořád viděná zepředu**. Důsledek je konkrétní a nepříjemný — **hůř se slučují objekty s prostředím, což je jinak právě ta věc, ve které izometrie vyniká**. Rada pro ostatní je proto jednoznačná [(2:26)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=146s): **„používáš-li izometrii, dělej v perspektivě všechno — ušetří to spoustu potíží."**

Workflow má dva návyky, které jdou převzít nezávisle na stylu:

- **Návrhy nejdřív na papír** [(2:26)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=146s), kde se perspektiva odhaduje volně: „analogové myšlení je pro mě mnohem snazší a přináší kreativnější nápady." Cena je přiznaná — návrhy se pak musí hodně upravovat.
- **Podkládání prostředí s poloviční průhledností** [(3:13)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=193s) při kreslení objektů, aby se srovnaly rohy a hrany. Není to čistá metoda (na to jsou vodicí linky), ale **záměrná nepřesnost dává ručně malovaný vzhled** — „dokonalý izometrický pohled má v sobě někdy něco velmi sterilního, i když jsou kresby samy o sobě hezké". Nevýhoda je poctivě dodaná: **linky nejsou přesně rovné a někdy to působí nečistě**.

Zajímavý je poznatek o tom, kde na přesnosti záleží víc a kde míň [(4:00)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=240s): **u postav a rostlin je dokonalá perspektiva méně důležitá než u objektů**, protože **u organických tvarů jsou malé chyby méně nápadné než u statických věcí** — křivá strana vyvýšeného záhonu bije do očí víc než nedostatečně natočená rostlina. Obecné doporučení je přitom velkorysé [(4:46)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=286s): **vodicí linky používej, „skoro každý to dělá, není to podvádění, ale normální součást izometrického kreslení"** — a chceš-li přesto freehand vzhled, nakresli s vodítky prostředí a zbytek zarovnávej podle něj.

> **Pozn.:** Napětí mezi „dokonalé je sterilní" a „nepřesné je nečisté" je tatáž volba jako u [ručně malovaných cedulí](typografie.md#semiotika-pisma-font-rekne-zanr-driv-nez-prvni-veta): nepravidelnost čte hráč jako **stopu po člověku**, dokonalost jako **výstup nástroje**. Rozdíl je, že v typografii je to čistý zisk, zatímco v izometrii za to platíš tím, že se ti objekty hůř skládají.

**Souvislosti:** [Art pipeline: vizuální hierarchie](art-pipeline.md#vizualni-hierarchie-fokus-vznika-ubranim-ne-pridanim) · [Typografie: semiotika](typografie.md#semiotika-pisma-font-rekne-zanr-driv-nez-prvni-veta) · [Rejstřík: izometrie](../rejstrik.md#izometrie) · [Rejstřík: oblique](../rejstrik.md#oblique)

---

## Layering a verticalita: statická kamera jako scénografie

**Zdroj:** [How we made our Isometric Game Art! ★ || GOLEMBERT Devlog #12](https://www.youtube.com/watch?v=UYBzqCldDDI) · [Studio Firlefanz](https://www.youtube.com/channel/UCAfPaxLy2g5uy7IrQToCcCg) · druhá půlka devlogu ·
[Create a FREE 2D Parallax System Using AI ( Game Ready )](https://www.youtube.com/watch?v=4_u5Ues1zPY) · [Iris Ogli - Modeling, AI Animation & Game Assets](https://www.youtube.com/channel/UC9NUEIVt0LPz0KA4SUWO9Hg) · ~4 min, tutoriál (doplněk o parallaxu)

**Shrnutí:** Se statickou kamerou vznikají dva problémy, které 3D hry řeší samy: **co je před čím** a **co komu zakrývá výhled**. První se řeší řazením vrstev podle pozice na ose Y, druhý designem samotného světa — mřížkou pro umísťování, „zdí" na horním okraji mapy nebo stupňovitým rozvržením. Autorka to popisuje jako práci scénografa, a to je přesná metafora.

### Rozpad myšlenky

**Layering** [(4:46)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=286s) mají vyřešený jednoduše: celé prostředí je nakreslené jako jeden celek (podlaha i schody jsou na jednom obrázku, žádná zvláštní textura podlahy), zatímco **objekty, které se hýbou nebo se dají umístit, mají skript měnící jejich vrstvu podle pozice na ose Y** [(5:32)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=332s). Postava stojící „níž" než květináč se vykreslí před ním, o kus výš za ním. Detaily, které mají být vždy vepředu, jsou vyčleněné na vlastní vrstvy — což je levné řešení výjimek, se kterými by se automatické řazení pralo.

**Mřížka jako designová volba** [(5:32)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=332s) je zajímavější, než se zdá. Stardew Valley má neviditelnou mřížku a získává tím dvě věci: jednotný vzhled **a hlavně pojistku, že nevznikne objekt dost vysoký a dost blízko, aby zakryl něco za sebou**. Oni šli opačnou cestou kvůli svobodě umísťování — a kompromis vyřešili tím, že **mřížku nabízejí jako volitelnou, kterou si hráč sám zapne**, chce-li čistě uspořádanou zahradu [(6:19)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=379s). Cena: objekty se můžou vizuálně křížit, což zatím podle autorky nezpůsobilo problém při hraní.

**Verticalita** [(6:19)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=379s) je pak odpověď na otázku, jak navrhnout svět, aby si sám nezakrýval výhled. Video rozlišuje dva případy podle toho, kdo staví:

- **Když staví hráč** (budovatelské a manažerské hry), vysoké budovy zakryjí cokoli — proto tyhle hry nabízejí **otáčení mapy a pohled ze čtyř směrů** [(7:06)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=426s).
- **Když jsou velké struktury dané** a hráč umísťuje jen drobnosti, používá se **„zeď" na horním okraji mapy**. Nejlepší důkaz je Stardew Valley: **za domem vlastně nic není, a všechno, co na farmě umístíš, je před ním** [(7:06)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=426s).

Jejich vlastní řešení stojí na pojmu **frame** [(7:06)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=426s) — tak si pojmenovaly oblast, kterou je vidět celou na jednu obrazovku (zahrada je jeden frame, přístav druhý). Schody vedou jen mezi framy a **celý layout ostrova je kolem toho postavený**: každá další oblast leží o kus výš, aby loď, strom ani dům nezakrývaly to za sebou [(7:54)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=474s). Autorka dodává, že totéž jde udělat do šířky s pomyslnou zdí v pozadí, a že hry jako Stardew si problém zjednodušují **rozdělením na víc scén**, takže nemusí všechno navazovat bezešvě [(8:41)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=521s).

Závěrečná formulace je nejlepší část devlogu [(8:41)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=521s): **„přemýšlet o věcech jako verticalita je sám o sobě fakt cool designový trik — připomíná to scénografii. Obzvlášť se statickou kamerou pro to musíš najít chytré řešení."** Statická kamera totiž nedovolí uhnout: co je špatně komponované, zůstane špatně komponované po celou hru.

**Doplněk: parallax vrstvy z AI.** Boční 2D hra řeší s vrstvami jiný problém než izometrie, totiž rychlost posunu podle hloubky. Krátký návod z kanálu Iris Ogli ukazuje, jak takové vrstvy vyrobit z AI obrázků, aby k sobě seděly [(0:00)](https://www.youtube.com/watch?v=4_u5Ues1zPY&t=0s). Nejdřív vznikne jediná scéna ve striktním 16:9, která má vypadat jako screenshot z hotové hry. Prompt v ní drží pevný úhel kamery a horizont, aby výsledek působil jako hratelná scéna, a ne jako obrázek [(0:48)](https://www.youtube.com/watch?v=4_u5Ues1zPY&t=48s). Ze stejné scény se pak generují samostatné vrstvy (vzdálené pozadí, střední plán a popředí), které po složení sedí, protože sdílejí styl, světlo i záběr kamery [(1:39)](https://www.youtube.com/watch?v=4_u5Ues1zPY&t=99s). Další vrstvy, třeba mlhu, vzdálené hory nebo listí v popředí, přidá další běh téhož promptu se stejnou referencí [(2:27)](https://www.youtube.com/watch?v=4_u5Ues1zPY&t=147s). Nakonec se z vrstev odstraní pozadí a uloží se jako průhledná PNG. Každá vrstva pak může mít v enginu vlastní rychlost a mezi vrstvy jdou vložit herní prvky [(3:13)](https://www.youtube.com/watch?v=4_u5Ues1zPY&t=193s). Celé prompty odkazuje popis videa na web kanálu. Zamčený horizont je tu stejná disciplína jako statická kamera výš: když nesedí perspektiva, rozpadne se celá kompozice. Toto čtení je naše.

> **Pozn.:** Tohle je 2D obdoba práce, kterou ve 3D dělá [kamera](kamera.md#kamera-metroidvanie-hranice-ktere-umi-lhat) — jen s obráceným zadáním. Ve 3D se kamera přizpůsobuje světu; tady se **svět staví tak, aby vyhověl nehybné kameře**. Proto je „stupňovitý ostrov" plnohodnotné designové rozhodnutí, ne dekorace.

**Souvislosti:** [Kamera: neviditelný designér](kamera.md#kamera-metroidvanie-hranice-ktere-umi-lhat) · [Prostor a hranice](prostor-a-hranice.md#jeskyne-ktera-se-hraje-landmark-napred-detail-nakonec) · [Vizuální komunikace: mechaniky musí být vidět](vizualni-komunikace.md#mechaniky-funguji-jen-tehdy-kdyz-je-hrac-vidi) · [Rejstřík: izometrie](../rejstrik.md#izometrie)

---

## Zpomalit, abys byl rychlejší: volba nástrojů jako investice

**Zdroj:** [Why I don't use Aseprite — The Tools I Use for Indie Game Dev (2D and 3D)](https://www.youtube.com/watch?v=wuO_iy0zhPA) · [Zizaco](https://www.youtube.com/channel/UCvFDxvCvvibNScfJD5h4oBQ) · ~8 min, přehled nástrojů

**Shrnutí:** Přehled nástrojů, který je zajímavý jednou tezí a jednou provokací. Teze zní **„zpomal, abys byl rychlejší"** — investice do těžšího nástroje se vrátí. Provokace je v titulku: autor nepoužívá Aseprite a vysvětluje proč, způsobem, který stojí za zvážení i pro toho, kdo u něj zůstane. Háček: **je to názor jednoho člověka na jeho vlastní pipeline**, ne měření.

### Rozpad myšlenky

**Argument proti Aseprite** [(0:00)](https://www.youtube.com/watch?v=wuO_iy0zhPA&t=0s) není o funkcích, ale o technice: *„nutí tě kreslit každý jednotlivý pixel — a to není postup, který používají špičkoví pixel artisté."* Jeho doklad je nepřímý, ale poctivě uvedený: podívej se na nejlepší práce na Pixel Jointu a zjistíš, čím vznikaly. Předvádí to na kouli, kterou udělá **jedním kliknutím** s nastavenou paletou a filtry, a pak do ní jen domaluje praskliny.

**Co používá místo toho**: **Photopea** (bezplatná webová alternativa Photoshopu — *„nabízí skoro všechny funkce, které bys našel ve Photoshopu"*, včetně omezení na paletu pro pixel art) a **Krita** na kreslení tabletem, kvůli ovládání štětců a onion skinningu pro animaci. Dělba práce u něj: **Krita pro kreslení tabletem, Photopea pro úpravy myší.**

**Ta hlavní teze** se opakuje třikrát a je to jediné, co z videa má obecnou platnost: *„učit se nový software může působit zastrašujícím dojmem, ale nakonec ti to může pomoct pracovat rychleji a dělat kvalitnější výsledky."* Aplikuje ji i na Git: *„může působit složitě, jsi-li v tom nový, ale věřím, že se investice do jeho pořádného naučení mnohonásobně vrátí."*

**Ke 3D** [(5:19)](https://www.youtube.com/watch?v=wuO_iy0zhPA&t=319s) přidává radu, která patří k nejopakovanějším v celé knihovně, a je dobré ji slyšet i tady: *„neradil bych indie ani sólo vývojářům honit vysokou vizuální věrnost. Místo toho zvolit výrazný stylizovaný 3D styl je nejspíš tvoje nejlepší sázka."* Konkrétně používá **Blockbench** na modelování (styl, který podle něj sedí tomu, co indie vývojáři zvládnou) a **Blender** na všechno ostatní — *„nedá se to obejít, Blender je v podstatě nezbytná součást výbavy každého 3D artisty."*

**A dokumentace bez estetiky**: Google Docs, Sheets a Slides. *„Přiznávám, že tyhle nástroje nemají žádné estetické kouzlo. Vlastně jsou ošklivé. Ale bohatě to vynahrazují funkčností."* Argument: napadne tě nápad v tramvaji, zapíšeš ho z telefonu, sdílíš, komentuješ, a máš historii toho, co se kdy změnilo.

> **Pozn.:** To „zpomal, abys byl rychlejší" je jediná část, kterou stojí za to brát jako obecné pravidlo — a je užitečné právě proto, že **jde proti tomu, jak se nástroje vybírají v praxi**: podle toho, co se dá dnes odpoledne rozjet. Rozumný test, který z toho plyne: **kolikrát ten nástroj použiju?** U věci, kterou uděláš jednou, vyhrává snadnost; u věci, kterou budeš dělat tisíckrát, vyhrává strop. To je táž úvaha jako u [nástrojů, které si napíšeš pro sebe](../godot/projekt-a-vykon.md#nastroje-pro-sebe-editor-script-ktery-ti-usetri-boilerplate). Argument proti Aseprite je slabší, než jak zní: **není to spor o nástroj, ale o techniku** — filtry a paletizace proti kreslení pixel po pixelu — a tu první se dá dělat i v Aseprite. Ber to tedy jako pozvánku vyzkoušet **jiný postup**, ne jako důvod měnit software. A jedno přiznání, které video samo obsahuje: autor je zároveň propagátorem konkrétního enginu a odkazuje na svůj mailing list, takže část doporučení je i osobní pipeline, ne nezávislé srovnání.

**Souvislosti:** [Pixel art je rozhodnutí, ne nouzové řešení](#pixel-art-je-rozhodnuti-ne-nouzove-reseni) · [Herní art — pipeline](art-pipeline.md) · [Plánovací nástroje](planovani-nastroje.md#nastroje-full-time-indie-vyvojare-a-jedna-vec-navic-ktera-neni-software) · [Godot: nástroje pro sebe](../godot/projekt-a-vykon.md#nastroje-pro-sebe-editor-script-ktery-ti-usetri-boilerplate) · [Rejstřík: Blockout](../rejstrik.md#blockout) · [Rejstřík: Version control](../rejstrik.md#version-control)
