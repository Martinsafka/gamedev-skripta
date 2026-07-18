# 2D vizuál: pixel art a izometrie

Dvě rozhodnutí, která u 2D hry padnou nejdřív a nejdéle drží: **jaké má hra rozlišení** a **z jakého úhlu se na svět díváš**. Obě vypadají jako technikálie a obě jsou ve skutečnosti designové volby s dlouhým stínem — určují, kolik práce dá jeden asset, jak čitelná bude scéna a co všechno hráč uvidí. Tahle kapitola spojuje dva zdroje z opačných konců zkušenosti: vývojáře, který přesvědčuje netvůrce, že na pixel art stačí hrstka nastavení, a autorku, která na vlastní hře popisuje, co izometrie stojí.

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

**Souvislosti:** [Vizuální komunikace: krása je volitelná](vizualni-komunikace.md#dve-strany-artu-krasa-je-volitelna-srozumitelnost-ne) · [Scope: design by constraint](scope.md#design-by-constraint-krabice-napred-napad-dovnitr) *(omezení jako zdroj konzistence)* · [Sólo vývoj: pipeline jednoho člověka](solo-vyvoj.md#pipeline-jednoho-cloveka-gdd-engine-verzovani-cizi-assety) · [Kamera: zoom v pixel artu](kamera.md#look-ahead-focus-objekty-a-zoom-ktery-nesel) · [Rejstřík: integer scaling](../rejstrik.md#integer-scaling) · [Rejstřík: pixel-perfect](../rejstrik.md#pixel-perfect)

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

**Zdroj:** [How we made our Isometric Game Art! ★ || GOLEMBERT Devlog #12](https://www.youtube.com/watch?v=UYBzqCldDDI) · [Studio Firlefanz](https://www.youtube.com/channel/UCAfPaxLy2g5uy7IrQToCcCg) · druhá půlka devlogu

**Shrnutí:** Se statickou kamerou vznikají dva problémy, které 3D hry řeší samy: **co je před čím** a **co komu zakrývá výhled**. První se řeší řazením vrstev podle pozice na ose Y, druhý designem samotného světa — mřížkou pro umísťování, „zdí" na horním okraji mapy nebo stupňovitým rozvržením. Autorka to popisuje jako práci scénografa, a to je přesná metafora.

### Rozpad myšlenky

**Layering** [(4:46)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=286s) mají vyřešený jednoduše: celé prostředí je nakreslené jako jeden celek (podlaha i schody jsou na jednom obrázku, žádná zvláštní textura podlahy), zatímco **objekty, které se hýbou nebo se dají umístit, mají skript měnící jejich vrstvu podle pozice na ose Y** [(5:32)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=332s). Postava stojící „níž" než květináč se vykreslí před ním, o kus výš za ním. Detaily, které mají být vždy vepředu, jsou vyčleněné na vlastní vrstvy — což je levné řešení výjimek, se kterými by se automatické řazení pralo.

**Mřížka jako designová volba** [(5:32)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=332s) je zajímavější, než se zdá. Stardew Valley má neviditelnou mřížku a získává tím dvě věci: jednotný vzhled **a hlavně pojistku, že nevznikne objekt dost vysoký a dost blízko, aby zakryl něco za sebou**. Oni šli opačnou cestou kvůli svobodě umísťování — a kompromis vyřešili tím, že **mřížku nabízejí jako volitelnou, kterou si hráč sám zapne**, chce-li čistě uspořádanou zahradu [(6:19)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=379s). Cena: objekty se můžou vizuálně křížit, což zatím podle autorky nezpůsobilo problém při hraní.

**Verticalita** [(6:19)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=379s) je pak odpověď na otázku, jak navrhnout svět, aby si sám nezakrýval výhled. Video rozlišuje dva případy podle toho, kdo staví:

- **Když staví hráč** (budovatelské a manažerské hry), vysoké budovy zakryjí cokoli — proto tyhle hry nabízejí **otáčení mapy a pohled ze čtyř směrů** [(7:06)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=426s).
- **Když jsou velké struktury dané** a hráč umísťuje jen drobnosti, používá se **„zeď" na horním okraji mapy**. Nejlepší důkaz je Stardew Valley: **za domem vlastně nic není, a všechno, co na farmě umístíš, je před ním** [(7:06)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=426s).

Jejich vlastní řešení stojí na pojmu **frame** [(7:06)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=426s) — tak si pojmenovaly oblast, kterou je vidět celou na jednu obrazovku (zahrada je jeden frame, přístav druhý). Schody vedou jen mezi framy a **celý layout ostrova je kolem toho postavený**: každá další oblast leží o kus výš, aby loď, strom ani dům nezakrývaly to za sebou [(7:54)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=474s). Autorka dodává, že totéž jde udělat do šířky s pomyslnou zdí v pozadí, a že hry jako Stardew si problém zjednodušují **rozdělením na víc scén**, takže nemusí všechno navazovat bezešvě [(8:41)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=521s).

Závěrečná formulace je nejlepší část devlogu [(8:41)](https://www.youtube.com/watch?v=UYBzqCldDDI&t=521s): **„přemýšlet o věcech jako verticalita je sám o sobě fakt cool designový trik — připomíná to scénografii. Obzvlášť se statickou kamerou pro to musíš najít chytré řešení."** Statická kamera totiž nedovolí uhnout: co je špatně komponované, zůstane špatně komponované po celou hru.

> **Pozn.:** Tohle je 2D obdoba práce, kterou ve 3D dělá [kamera](kamera.md#kamera-metroidvanie-hranice-ktere-umi-lhat) — jen s obráceným zadáním. Ve 3D se kamera přizpůsobuje světu; tady se **svět staví tak, aby vyhověl nehybné kameře**. Proto je „stupňovitý ostrov" plnohodnotné designové rozhodnutí, ne dekorace.

**Souvislosti:** [Kamera: neviditelný designér](kamera.md#kamera-metroidvanie-hranice-ktere-umi-lhat) · [Prostor a hranice](prostor-a-hranice.md#jeskyne-ktera-se-hraje-landmark-napred-detail-nakonec) · [Vizuální komunikace: mechaniky musí být vidět](vizualni-komunikace.md#mechaniky-funguji-jen-tehdy-kdyz-je-hrac-vidi) · [Rejstřík: izometrie](../rejstrik.md#izometrie)
