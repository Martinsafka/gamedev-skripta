# MegaLights: stovky světel za pevný rozpočet

MegaLights je systém přímého osvětlení v Unrealu, který je od verze 5.8 připravený pro produkci. Mění otázku, kterou si herní osvětlovač dlouho kladl. Dřív se ptal, kolik světel si může dovolit. Teď se ptá, kolik světel se potká v jednom pixelu. Kapitola stojí na jediném zdroji, téměř tříhodinovém streamu Inside Unreal se dvěma artisty z Epicu. Moderátor dřív pět let učil environment art na vysoké škole, host dělá technický marketing a ukazuje vlastní scénu. Nepřímé světlo a odrazy dál řeší Lumen. Fyzikální základ světla a expozice najdeš v kapitole [Osvětlení](osvetleni.md#pbl-svitit-podle-skutecnych-hodnot), opačný přístup s falešnými světly v [Malovat světlem](osvetleni.md#malovat-svetlem-scena-slozena-z-falesnych-svetel).

---

## Rozpočet vzorků na pixel: co MegaLights mění a co za to platíš

**Zdroj:** [Artist's Guide to Using MegaLights in Unreal Engine 5.8 | Inside Unreal](https://www.youtube.com/watch?v=Nrb17mtBJPM) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~2,8 h, livestream (dva artisti z Epicu)

**Shrnutí:** MegaLights počítá přímé světlo jedním průchodem s pevným počtem vzorků na pixel. Po počáteční ceně, kterou zaplatíš zapnutím, už další světla výkon skoro nezvedají. Každý pixel si jen rozdělí svoje vzorky mezi světla, která na něj dosáhnou. Háček: cena se přesunula z milisekund do kvality. Když se na jednom pixelu potká příliš mnoho světel, každé dostane méně vzorků. Obraz začne šumět a v čase blikat a denoiser to musí uklízet. Že můžeš dát světel kolik chceš, ještě neznamená, že bys měl.

### Rozpad myšlenky

**Odkud se to vzalo.** Moderátor to ukazuje na krátké historii [(14:49)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=889s):
- světlo zapečené do vrcholů bylo levné, ale ošklivé;
- lightmapy vypadají dobře, ale každá instance potřebuje vlastní texturu, platí se pamětí a světlo není dynamické [(17:12)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=1032s);
- Lumen počítá globální osvětlení za běhu, ale přímé světlo zvládá hůř. To je úkol MegaLights [(18:45)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=1125s).

Oba systémy tedy pracují spolu. Lumen dodává nepřímé světlo a odrazy, MegaLights přímé světlo [(1:07:25)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=4045s), [(1:21:27)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=4887s).

**Co nahrazuje.** Podle dokumentace, kterou moderátor čte na streamu, přebírá MegaLights stínové mapy, distance field i ray-traced stíny, deferred shading s vyhodnocením světla, světlo do volumetrické mlhy a projekci virtuálních stínových map [(13:15)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=795s). Virtuální stínové mapy jde použít i dál, ale pro dotčená světla pak běží obě pipeline najednou a výkon se rychle stane úzkým hrdlem [(21:51)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=1311s), [(22:37)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=1357s).

**Jak se platí.** Engine se pro každý pixel dívá, kolik světel na něj dosáhne a jak velký mají příspěvek. Podle toho rozdělí vzorky a nepodstatné zahodí [(8:54)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=534s). Na pixelu s desítkami světel tedy neplatíš za desítky světel, ale každé světlo dostane méně vzorků [(28:04)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=1684s), [(28:50)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=1730s). Cenu proto určuje hlavně renderovací rozlišení: dvakrát víc pixelů znamená dvakrát víc vzorků, kdežto počet světel tolik nerozhoduje [(1:15:57)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=4557s).

**Zkouška nejhoršího případu.** Moderátor postaví 200 stínících světel přímo na sebe, se stejným attenuation radiem [(30:25)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=1825s):
- s MegaLights scéna běží zhruba na 150 FPS, ať jsou světla zapnutá, nebo vypnutá [(31:11)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=1871s);
- světlo je ale nepoužitelné, stín postavy se rozpadne, protože každé světlo má na pixelu jen zlomek vzorků [(31:59)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=1919s);
- bez MegaLights spadne snímková frekvence na 33 až 34 FPS, tedy zhruba čtyř- až pětinásobný propad, a k tomu přijdou chyby vykreslování [(33:12)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=1992s).

Čísla jsou z přehrávání v editoru na silném stroji, takže platí jen jako poměr [(29:37)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=1777s).

**Co potřebuje a jak se zapíná.**
- **Shader Model 6** [(10:28)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=628s). Ray tracing výrazně pomáhá, protože MegaLights na něm stojí, ale hardwarový ray tracing nutný není. Podle hosta je softwarový ray tracing rychlý [(21:04)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=1264s), [(2:43:17)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=9797s).
- S forward shadingem MegaLights nefungují [(2:25:13)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=8713s).
- Zapínají se v Project Settings a zároveň je potřeba zapnout ray tracing. Nastavení projektu je jen výchozí hodnota pro nová světla, každé světlo má vlastní přepínač Allow MegaLights [(22:37)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=1357s), [(23:24)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=1404s). Přepnout je jde i v post-process volume [(1:02:46)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=3766s).
- Dřív se mohla překrývat jen hrstka stationary světel (moderátor říká tři, host čtyři). Tenhle strop s MegaLights padá, ale ikona varování zůstává, protože nové světlo má výchozí mobilitu stationary. Přepnutí na movable ji odstraní [(36:20)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=2180s), [(37:06)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=2226s).
- V projektu, který je celý dynamický, host radí vypnout Allow Static Lighting. Ubude tím shaderových permutací a stabilitu by to podle něj nemělo ovlivnit [(2:26:07)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=8767s), [(2:26:55)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=8815s), [(2:28:27)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=8907s).

**Kdy ne.** MegaLights možná nepotřebuješ na hardwaru bez Shader Modelu 6 a ray tracingu, ve scéně s pár světly bez dynamiky ani s pečeným světlem. Ve VR na samostatném headsetu by řečníci volili jinak, i když se hranice posouvají: jeden tým MegaLights rozjel na mobilu s hardwarem, který teprve přichází [(1:22:14)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=4934s), [(1:23:03)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=4983s). Moderátorův příklad: když hra má slunce a pochodeň v ruce hráče, MegaLights nepotřebuješ. Vyplatí se tam, kde se překrývá hodně dynamických stínů a cílová platforma ray tracing unese [(2:37:01)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=9421s), [(2:37:48)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=9468s). Na slabší počítače se projekt škáluje přes device profiles: autoruješ jednou a profil rozhodne, co dostane které zařízení [(2:29:14)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=8954s), [(2:30:00)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=9000s).

> **Pozn.:** Kapitola [Malovat světlem](osvetleni.md#malovat-svetlem-scena-slozena-z-falesnych-svetel) zapínala MegaLights v 5.5 jako trik na výkon. V 5.8 jsou podle obou řečníků výrazně stabilnější v čase, beta podle moderátora viditelně šuměla [(9:41)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=581s), [(11:14)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=674s). Paměť MegaLights skoro nežerou. V Render Resource Vieweru vycházejí na 44 MB a video paměť berou hlavně textury a geometrie [(2:31:33)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=9093s), [(2:37:48)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=9468s). Moderátor to přirovnává k Nanitu: rozvazuje ruce, ale zadarmo není [(1:14:25)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=4465s). Podobně u Nanitu rozhoduje, jak se geometrie překrývá, viz [Overdraw se autoruje, ne opravuje](nanite-do-hloubky.md#overdraw-se-autoruje-ne-opravuje). Demo scéna je z Fabu, kde Epic podle moderátora zhruba každé dva týdny rozdává assety zdarma [(19:32)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=1172s).

**Souvislosti:** [Rejstřík: MegaLights](../rejstrik.md#megalights) · [Rejstřík: Lumen](../rejstrik.md#lumen) · [Rejstřík: Denoiser](../rejstrik.md#denoiser) · [Rejstřík: Deferred rendering](../rejstrik.md#deferred-rendering) · [Rejstřík: Ray tracing](../rejstrik.md#ray-tracing) · [007 First Light: 1 500 světel a culling](env-technika.md#007-first-light-editor-ve-kterem-se-vsechno-sklada-z-entit-a-nikdo-neceka) *(stejný problém ve vlastním enginu)*

---

## Attenuation radius jako hlavní páka: počítej překryvy, ne světla

**Zdroj:** [Artist's Guide to Using MegaLights in Unreal Engine 5.8 | Inside Unreal](https://www.youtube.com/watch?v=Nrb17mtBJPM) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~2,8 h, livestream (část o dosahu světel a diagnostice)

**Shrnutí:** S MegaLights je nejdůležitější metrikou počet attenuation radiů, která se překrývají na jednom místě. Výchozích 1000 cm může být zbytečně moc, nebo naopak málo. Jen připomenutí: světlo počítá v celém svém objemu, i tam, kam už viditelně nedosvítí. Dosah se proto ladí od oka, podle toho, kde začne být vidět ořez. Háček: jako výchozí chování to engine dělat nemůže, protože jak daleko světlo „dosáhne", závisí na expozici, a ta je v každé scéně jiná. Pro konkrétní scénu se to ale nakalibrovat dá.

### Rozpad myšlenky

**Co radius dělá.** Attenuation radius je strop dosahu. I světlo s obrovskou intenzitou za ním končí [(25:43)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=1543s). Ladí se proto dvojice intenzita a dosah: tak daleko, jak je potřeba, a ne dál [(26:31)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=1591s).
- Nové světlo má radius 1000 jednotek, tedy centimetrů [(39:24)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=2364s).
- Výchozí jednotky jsou bez rozměru. Moderátor používá lumeny a výchozí jednotku jde nastavit v Project Settings [(40:10)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=2410s).
- U stolumenové žárovky větší radius viditelný dosah nezvětší, protože světlo dřív zeslábne. Engine ho ale počítá v celém objemu [(40:57)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=2457s).

**Proč to engine nedopočítá sám.** Studenti se moderátora ptali, proč radius neroste s intenzitou automaticky. Odpověď je expozice. Rozsah a kompenzace expozice v post-process volume mění, jak daleko světlo vypadá, že svítí. Radius, který sedí k jedné expozici, k jiné nesedí [(41:43)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=2503s), [(42:30)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=2550s), [(43:17)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=2597s).

**Kalibrace od oka.** Postup je jednoduchý [(48:40)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=2920s), [(49:26)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=2966s):
1. dej světlo na místo a nastav intenzitu, třeba jasná svíčka kolem 75 lumenů;
2. sleduj okraj osvětlené plochy a stahuj radius, dokud nezačne být vidět ořez;
3. kousek se vrať. Ve scéně z ukázky byl ořez vidět pod 600, takže dobrý radius vyšel kolem 650 až 700.

**Chytré světlo jako Blueprint.** Moderátor si postavil „smart point light", který radius dopočítá z intenzity [(44:03)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=2643s):
- radius = odmocnina z podílu intenzity a referenční intenzity, vynásobená referenčním radiem a násobičem [(47:08)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=2828s);
- referenci si nakalibroval ve své scéně se svou expozicí: 100 lumenů a radius kolem 700, s malou rezervou [(46:22)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=2782s);
- násobič stačí do čtyřnásobku;
- Blueprint nastavuje i specular scale, source radius a délku zdroje a přepíná mezi teplotou a barvou. Teplotu moderátor používá skoro vždy, barvu jen tam, kam teplota nedosáhne [(47:54)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=2874s);
- ve výchozím stavu svítí křiklavě růžově, aby bylo při kalibraci na šedé ploše dobře vidět [(44:03)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=2643s), [(45:36)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=2736s). Od obyčejného světla ho odliší ikona, kterou moderátor na Blueprintu nechal [(52:34)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=3154s).

**Kolik překryvů je moc.** Podle moderátora začne být pokles kvality vidět, když se na jednom místě překrývá zhruba deset a víc radiů. Říká ale, že je to číslo z hlavy a záleží na světlech i scéně [(50:13)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=3013s). Výchozí nastavení MegaLights míří na 60 FPS na současných konzolích. Pro film, virtuální produkci nebo silný stroj jde CVary posunout tak, aby snesly víc překryvů [(50:59)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=3059s), [(51:47)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=3107s).

**Světla neschovávej do geometrie.** Dokumentace varuje, že světlo zapíchnuté do meshe plýtvá vzorky na místech, která nikdo neuvidí [(54:07)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=3247s). Moderátor má světlo uvnitř lucerny, a tak lucerně vypne vrhání stínu. Stín nahoře a dole pak dělají dva válce, které jsou ve hře skryté, ale stín vrhají dál (hidden in game a zároveň hidden shadow) [(54:53)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=3293s), [(55:39)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=3339s).

**Když to šumí.**
- Pohled Lit → MegaLights → Light Complexity ukazuje čarami, která světla na pixel pod kurzorem dosáhnou. Text vlevo nahoře k nim vypíše poměr vlivu, typ a jméno [(27:17)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=1637s), [(1:04:18)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=3858s), [(1:05:04)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=3904s).
- Host hledá zdroj šumu CVary: vypíná postupně MegaLights, TSR a další, protože je to rychlejší než hledat, který post-process volume zrovna platí [(1:03:32)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=3812s). Pomáhají i režimy jen se světlem nebo jen se stíny. Často stačí přidat na problémové místo malé světlo [(1:16:43)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=4603s), [(1:17:29)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=4649s).
- Záře, která zůstane po zhasnutí světla, není adaptace oka, ale temporální akumulace [(1:17:29)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=4649s).
- Drobné letící částice a sklo nechávaly v TSR stopy. Pomůže zapnout v materiálu Output Depth and Velocity. U dvou vrstev skla na sobě musí být zapnuté v obou materiálech [(1:27:43)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=5263s), [(1:28:29)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=5309s), [(1:31:38)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=5498s).
- Vzdálená světla se ořezávala jako příliš malá na obrazovce. Host snížil CVar s minimálním poloměrem světla na obrazovce o řád [(1:31:38)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=5498s), [(1:32:24)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=5544s).

> **Pozn.:** Dva poslední body s MegaLights nesouvisejí, host to říká sám. Do kapitoly patří, protože se při ladění světla objeví jako první podezřelí. Odmocnina v chytrém světle odpovídá fyzice: osvětlení klesá s druhou mocninou vzdálenosti, takže dosah do zvolené hladiny jasu roste s odmocninou intenzity. Tohle je naše vysvětlení, moderátor konstantu jen nakalibroval od oka.

**Souvislosti:** [Rejstřík: Attenuation radius](../rejstrik.md#attenuation-radius) · [Rejstřík: TSR](../rejstrik.md#tsr) · [Rejstřík: Auto exposure](../rejstrik.md#auto-exposure) · [Profiling: měření místo odhadů](profiling.md) *(stejná disciplína pro výkon)*

---

## Svítidlo z víc světel: odraz, mlha a stín se ladí zvlášť

**Zdroj:** [Artist's Guide to Using MegaLights in Unreal Engine 5.8 | Inside Unreal](https://www.youtube.com/watch?v=Nrb17mtBJPM) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~2,8 h, livestream (ukázky obou řečníků)

**Shrnutí:** Když světla nestojí skoro nic navíc, může jedno svítidlo tvořit několik světel a každé má jiný úkol. Jedno dělá tvar odrazu, druhé žárovku, třetí jen světlo v mlze. Hostovo auto ve scéně má kolem třiceti světel. Nástroje jsou pořád stejné: velikost zdroje (source radius), obdélníková světla s klapkami (barn doors), kanály světel a IES profily, obojí nově s MegaLights v 5.8. Háček: tenhle přístup je bližší filmovému svícení než hernímu. Moderátor sám připomíná, že showcase scénu hodnotí jinak než hru, která má vyjít.

### Rozpad myšlenky

**Okno se dvěma stíny.** U okna má moderátor obdélníkové světlo vpředu a malé bodové světlo, které dosvětluje odražené světlo. Stín vrhají obě. Když druhému stín vypne, světlo začne prosakovat tam, kam nemá. Bez MegaLights by byly dva stínící zdroje přes sebe drahé a omezující [(52:34)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=3154s), [(53:21)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=3201s), [(54:07)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=3247s).

**Pouliční lampa ze tří světel.** Host plošná světla používá hodně. S MegaLights stojí obdélníkové světlo skoro stejně jako bodové nebo spot s nenulovým source radiem a nesvítí na všechny strany [(1:33:10)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=5590s). Lampa nad autem je složená ze tří světel [(1:33:57)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=5637s):
- široké tlumené obdélníkové světlo za difuzní sklo,
- malé jasné obdélníkové světlo uvnitř jako žárovka,
- bodové světlo bez stínu jen pro volumetrickou mlhu.

Jedno velké obdélníkové světlo by po laku auta táhlo čtvercový odlesk, který ke svítidlu nepatří. Tři světla dovolí vytvarovat odraz i kužel v mlze [(1:34:45)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=5685s).

**Světlomet jako malý projekt.** Uvnitř reflektoru světlometu sedí drobné žárovky s emisivním materiálem. Host do nich dá malá bodová světla bez stínu, jejichž dosah končí na vnitřní stěně reflektoru [(1:37:51)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=5871s), [(1:40:11)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=6011s). Se zmenšeným source radiem (kolem 0,5 až 1) se odlesk uvnitř reflektoru při pohybu kamery posouvá a přibude lens flare z bloomu. Samotný emisiv tohle nedá [(1:38:39)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=5919s), [(1:39:25)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=5965s). Nad tím je další bodové světlo, které trochu dosvítí karoserii, a hlavní spot s IES profilem [(1:40:58)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=6058s). Celé svítidlo tvoří devět malých bodových světel, jedno dosvětlení a dva spoty. Na celém autě je kolem třiceti světel a podle hosta to pořád běží rychle [(1:43:16)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=6196s), [(1:44:02)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=6242s).

**Nástroje, které se v ukázkách opakují.**
- **Source radius:** výchozí světlo vrhá ostré stíny, jako by svítilo z jediného bodu, a tak skoro žádný skutečný zdroj nesvítí. U svíčky nebo pochodně moderátor zvedá soft source radius na 0,5 až 4 a polostín změkne [(56:26)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=3386s), [(58:00)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=3480s), [(58:48)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=3528s).
- **Obdélníková světla a klapky:** na panelová světla v podzemním skladu doporučují oba řečníci obdélníková světla se staženými klapkami. Intenzita závisí na ploše, užší světlo je jasnější. Výchozí úhel klapek je 88° a zúžením vznikne přirozený přechod, jako když světlo padá zvenku dovnitř [(1:00:25)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=3625s), [(1:01:12)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=3672s), [(1:01:59)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=3719s).
- **Kanály světel:** od 5.8 fungují s MegaLights. Unreal má jen tři kanály, ale jako jednoduché light linking stačí. Host tak jedno bodové světlo nepustí na samotné svítidlo, aby ho nepřepálilo [(1:34:45)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=5685s), [(1:35:31)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=5731s).
- **IES profily:** taky novinka 5.8 s MegaLights. Host používá profil, který je přímo v enginu. Rada: vnitřní kužel světla má mít stejný úhel jako paprsek v profilu. Vytáhni ho, dokud se paprsek přestane plnit, a pak kousek vrať [(1:41:44)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=6104s), [(1:42:30)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=6150s).
- **Specular scale 0 u dosvětlení:** pomocné světlo je jinak vidět v odrazech, s větším source radiem jako čtverec nebo tečka. Hodnota je schovaná v sekci Advanced [(2:16:43)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=8203s), [(2:17:30)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=8250s).
- **Podíl světla v mlze:** každé světlo má vlastní intenzitu rozptylu ve volumetrické mlze. Ray-traced stíny se do mlhy dostanou přes CVar, který je potřeba zapnout. Dřív to šlo jen se stínovými mapami [(2:18:17)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=8297s).
- **Barva z teploty:** moderátor nastavuje teplotou skoro všechna světla [(47:54)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=2874s). Host u světla vedle emisivu bere barvu přímo z materiálu a emisiv světlometu nastaví uzlem BlackBody na 5200 K [(2:41:42)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=9702s), [(2:42:29)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=9749s).

**Emisiv nestačí.** Malé emisivní plochy jako hlavní zdroj světla jsou pro Lumen pořád těžké. Spolehlivější je doplnit emisivní svítidlo skutečným světlem. Ručně je to pracné, při procedurálním rozmisťování snadné [(1:07:25)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=4045s), [(1:08:13)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=4093s). Bodové světlo s délkou zdroje položené na emisivní materiál dá realistickou záři [(1:36:17)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=5777s), [(1:37:03)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=5823s).

**Pohyb a množství.** Pohyblivá světla jsou podle moderátora pravděpodobně to, kde MegaLights září nejvíc. Zdrojem světla mohou být i částice z Niagary, což zvýrazňovaly materiály k 5.7, a světla jde rozmisťovat přes PCG [(1:05:51)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=3951s), [(1:06:38)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=3998s). Host zkoušel tisíce světel, statisíce ne, a radí to zkusit v grayboxu. Moderátor tipuje, že by bylo potřeba hlídat dosahy, jinak to rychle zašumí [(2:28:27)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=8907s), [(2:29:14)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=8954s). V 5.8 jsou připravené pro produkci i vlasy a kvalitní průhledné plochy s víc odlesky od MegaLights, třeba sklo, ve kterém se odráží všechna okolní světla [(1:44:49)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=6289s), [(1:45:35)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=6335s).

> **Pozn.:** [Malovat světlem](osvetleni.md#malovat-svetlem-scena-slozena-z-falesnych-svetel) skládá scénu z pomocných světel pro jeden záběr kamery. MegaLights tenhle přístup zlevňují, protože pomocných světel může být mnohem víc a mohou vrhat stíny. Na tom, že světlo laděné pro jeden úhel se z jiného vymstí, ale nic nemění. To je naše čtení. Hostova scéna je zároveň ukázka Fabu, složená z cizích assetů a automotive material packu [(1:23:50)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=5030s), [(1:24:38)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=5078s). Moderátor upozorňuje, že hru, která má vyjít, by hodnotil jinak [(2:30:46)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=9046s). Třicet světel na auto je tedy strop pro showcase, ne doporučení pro hru.

**Souvislosti:** [Rejstřík: Source radius](../rejstrik.md#source-radius) · [Rejstřík: Rect light](../rejstrik.md#rect-light) · [Rejstřík: Lighting channels](../rejstrik.md#lighting-channels) · [Rejstřík: IES profile](../rejstrik.md#ies-profile) · [Rejstřík: Color temperature](../rejstrik.md#color-temperature) · [Objemy přes EVDB](osvetleni.md#objemy-pres-evdb-mraky-a-mlha-jako-asset) *(mlha, do které světla kreslí)*

---

## Slunce bez MegaLights: silné světlo spolkne rozpočet

**Zdroj:** [Artist's Guide to Using MegaLights in Unreal Engine 5.8 | Inside Unreal](https://www.youtube.com/watch?v=Nrb17mtBJPM) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~2,8 h, livestream (část o directional light a obloze)

**Shrnutí:** MegaLights rozděluje vzorky podle důležitosti. Jasné směrové světlo, které svítí na všechno, si vezme skoro celou váhu a malým měkkým světlům bere důležitost, takže dostanou méně vzorků. Slunce proto MegaLights nemá dostat a jeho stíny patří virtuálním stínovým mapám. Slabý měsíc MegaLights zvládnou. Háček je v tom, že pravidlo neplatí pro všechna směrová světla. Rozhoduje jas, ne typ světla.

### Rozpad myšlenky

**Proč ne slunce.** Silné směrové světlo podle hosta „rozhodí" vážení. MegaLights pak počítají s tím, že pixel osvětluje skoro jen ono, a výsledkem je šum. Slabé směrové světlo nevadí [(2:04:16)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=7456s), [(2:05:03)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=7503s). Moderátor dodává obecnější důvod: MegaLights pracují s důležitostí, takže velké jasné světlo bere důležitost menším a měkčím světlům [(2:06:35)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=7595s).

**Proč virtuální stínové mapy.** U směrového světla mají MegaLights radši ray tracing než virtuální stínové mapy. Jenže na scéně velikosti města by ray-traced slunce potřebovalo velmi dlouhý dosah paprsků, a to je drahé. Virtuální stínové mapy zvládají měřítko města dobře, a tak jsou pro slunce podle hosta skoro vždy správná volba [(2:05:49)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=7549s).

**Jak to má host nastavené.**
- **Měsíc:** MegaLights zapnuté a ray-traced stíny vypnuté, protože výchozí nastavení enginu je má zapnuté [(2:04:16)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=7456s).
- **Slunce:** MegaLights vypnuté, ray-traced stíny taky [(2:05:03)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=7503s).
- **Jas měsíce** je 0,1 luxu, o něco víc než skutečný měsíc, a má měkký zdroj [(1:58:00)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=7080s).
- **Pomocné směrové světlo** dodává scéně jen nepatrné zvýraznění. Host přiznává, že fyzikálně nesedí, ale líbí se mu. Host na něm vypnul volbu, která z něj dělá slunce atmosféry, protože jinak podle něj svítí do volumetrické mlhy podruhé. Sám ale přiznává, že si už nevybavuje, jestli to opravdu pomohlo [(2:11:17)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=7877s), [(2:12:04)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=7924s).
- **Budovy v pozadí** mají spoustu světel s MegaLights, ale bez stínů. Je tak daleko, že na stínech nesejde [(2:10:31)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=7831s).

**Obloha, která nezakryje záři.** Hvězdy a měsíc dává hostovi plugin Celestial Vault, který je součástí enginu. Stojí na Day Sequenceru z 5.3, nese databázi skutečných hvězd a umí nastavit slunce podle data a místa [(1:47:08)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=6428s), [(1:47:54)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=6474s). Sky dome s texturou mraků ale zakrývá světlo za sebou, a záře měsíce se ztratí. Host proto v materiálu dómu přičte k textuře jas světla ze sky atmosphere pro světlo 0 (slunce) a světlo 1 (měsíc) [(1:58:47)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=7127s), [(2:00:25)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=7225s), [(2:01:57)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=7317s).

**Světla ve dne.** Přes den lampy s MegaLights pořád svítí, jen jejich podíl proti slunci zmizí [(1:51:04)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=6664s). Aby okna budov svítila i ve dne, má host na světlech zapnutý Inverse Exposure Blend. S expozicí kamery, která se přizpůsobí slunci, roste i jejich intenzita [(2:08:13)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=7693s). Environment Light Mixer ukazuje jen slunce, měsíc a skylight, obyčejný Light Mixer všechna světla i jejich kanály [(2:40:54)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=9654s), [(2:41:42)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=9702s).

> **Pozn.:** Uzel, kterým host bere jas světla do materiálu dómu, ve streamu nezazní celým jménem. Nejspíš jde o SkyAtmosphereLightDiskLuminance, který bere index světla. To je náš odhad podle popisu. Pravidlo „slunce bez MegaLights" se potkává s [nastavením z Malovat světlem](osvetleni.md#malovat-svetlem-scena-slozena-z-falesnych-svetel), kde autor volí virtuální stínové mapy, protože se s Lumenem a Nanitem pracuje líp.

**Souvislosti:** [Rejstřík: Virtual Shadow Maps](../rejstrik.md#virtual-shadow-maps) · [Rejstřík: Importance sampling](../rejstrik.md#importance-sampling) · [Rejstřík: Volumetric fog](../rejstrik.md#volumetric-fog) · [Noční scéna z defaultního setupu](osvetleni.md#nocni-scena-z-defaultniho-setupu)

---

## Expozice, která drží: kalibrace, local exposure a dva modely světla

**Zdroj:** [Artist's Guide to Using MegaLights in Unreal Engine 5.8 | Inside Unreal](https://www.youtube.com/watch?v=Nrb17mtBJPM) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~2,8 h, livestream (otázky diváků a hostova scéna)

**Shrnutí:** Oba řečníci radši expozici zamykají. Host scénu kalibruje podle barevné tabulky a střední šedé a automatickou expozici pouští jen tam, kde ji hra opravdu potřebuje, a i pak v úzkém rozsahu. Pro střídání dne a noci má host dva samostatné modely světla, každý s vlastním post-process volume. Local exposure zvedne stíny, aniž by spálila světla. Háček: s dynamickým světlem expozice nikdy není jen otázka čísel. Lumen je simulace, která potřebuje čas, aby se po změně světla ustálila.

### Rozpad myšlenky

**Kalibrace místo dohadů.** Na otázku, jestli vypnout adaptaci oka, má host jasný postup [(1:18:16)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=4696s):
1. dát do scény kalibrátor barev s tabulkou Macbeth a šedou koulí;
2. s vypnutou automatickou expozicí najít základní nastavení;
3. automatickou expozici použít jen tam, kde je potřeba. Když se scéna moc nemění, vypnout ji, nebo jí hodně zúžit rozsah mezi minimem a maximem.

Kalibrátor je přímo v obsahu enginu jako static mesh. Podle hosta je nejspíš potřeba zapnout zobrazení engine a plugin contentu [(1:45:35)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=6335s), [(1:46:21)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=6381s). Výsledek host kontroluje v Pixel Inspectoru. Ten ukáže pre-exposure i barvu scény před tone mappingem a po něm. Střední šedá je kolem 0,18 v každém kanálu [(1:51:04)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=6664s), [(1:51:50)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=6710s).

**Kdy adaptace dává smysl.** Moderátor uvádí příklad z Falloutu: otevřou se dveře krytu a hráče oslepí den. Bez adaptace expozice to nejde. V domě s řízeným světlem stačí úzký rozsah [(1:19:49)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=4789s). Host k tomu dodává, že Lumen je simulace odrazů světla. Po změně se chvíli ustaluje a nikdy nedá úplně stejný obraz. Přechod z tmavé jeskyně do plného slunce bude dohánět [(1:19:49)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=4789s). Host by ve hře slunce asi nenastavoval na fyzikálních 100 000 luxů, ale spíš na zhruba deset. Skok od měsíce s 0,3 luxu by pak nebyl tak obří. Sám ale přiznává, že si není jistý, jak s tím Lumen po pre-exposure naloží [(1:20:39)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=4839s).

**Dva modely: noc a den.** Hostova scéna má dvě sady post-process volume, mlhy a dalších nastavení [(1:19:02)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=4742s), [(1:48:43)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=6523s):
- **noc** se zamčenou expozicí v úzkém rozsahu kolem −1 až −3 EV a s modřejším vyvážením bílé, protože tak noc vypadá líp;
- **den** s dynamickým rozsahem od −3 do 20 EV a vyvážením bílé uprostřed [(1:49:30)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=6570s).

Při posunu času dne je vidět, jak Lumen dohání. Při ladění si host hlídá, aby měnil ten správný post-process volume [(1:51:04)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=6664s). Všechno, co patří k obloze, má v názvu „sky", aby to šlo jedním filtrem najít [(1:48:43)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=6523s).

**Local exposure.** Uzavřený prostor, který nemá být černý, ale ani přepálený, host řeší local exposure v post-process volume [(2:19:03)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=8343s), [(2:19:51)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=8391s).
- **Výchozí hodnoty nesedí.** Šablony mají kontrast světel i stínů 0,8, nově přidaný post-process volume 1,0. Host se proto vrací k 0,8 a ladí od ní [(2:20:39)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=8439s), [(2:23:00)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=8580s).
- **Jak funguje.** Obraz se rozdělí na světla a stíny, podobně jako když se skládají dvě expozice do HDR. Snížený kontrast stínů je zvedne a světla zůstanou, kde byla [(2:22:12)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=8532s), [(2:23:00)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=8580s). V noci host hodnoty mírně stahuje.
- **Prahy vrátí černou.** Nejtmavší pixely se ze zvedání vyřadí, takže obraz nepřijde o čistou černou [(2:23:46)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=8626s).
- **Detail strength** dá obrazu „punch". Pak je dobré exposure compensation trochu snížit [(2:23:46)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=8626s).

**Emisiv a expozice.** Neonové nápisy se hostovi rozsvěcují podle času dne. Editor Utility Blueprint si jednou najde aktéra Celestial Vault a dvakrát za vteřinu se ptá na čas. Přes Material Parameter Collection pak posílá dvě hodnoty, den a noc, s přechodem kolem svítání a soumraku [(1:53:24)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=6804s), [(1:55:42)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=6942s). Emisiv v materiálu je navíc vydělený adaptací oka. Emisiv o síle deseti tisíc jednotek by podle hosta rozhodil Lumen i antialiasing, takže jeho rozsah musí zůstat rozumný [(1:55:42)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=6942s), [(1:56:29)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=6989s).

**Mlha, která rozmaže záři.** Velkou část nálady dělá volumetrická mlha a lokální fog volumes [(1:52:37)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=6757s). Exponential height fog má v 5.8 novou volbu screen space scattering. Ta rozmaže a rozzáří světla tím víc, čím je mlha hustší. Je to efekt v obrazovém prostoru, ne hloubka ostrosti [(2:02:44)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=7364s), [(2:03:30)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=7410s), [(2:07:23)](https://www.youtube.com/watch?v=Nrb17mtBJPM&t=7643s).

> **Pozn.:** Rada nesvítit sluncem fyzikálně jde proti [PBL workflow](osvetleni.md#pbl-svitit-podle-skutecnych-hodnot), který staví na skutečných hodnotách. Host ale mluví o hře, kde se střídá tma a plné slunce a Lumen musí přechod dohnat. Kdo svítí jednu scénu s pevnou expozicí, ten problém nemá. To je naše čtení rozporu a host sám přiznává nejistotu. Co se s obrazem děje po expozici, rozebírá [Tone mapper](osvetleni.md#tone-mapper-odkud-je-unreal-engine-look). Modřejší noc přes grading staví i [Temný les za odpoledne](env-tvorba.md#temny-les-za-odpoledne-hdri-mlha-a-grading).

**Souvislosti:** [Rejstřík: Auto exposure](../rejstrik.md#auto-exposure) · [Rejstřík: Local exposure](../rejstrik.md#local-exposure) · [Rejstřík: Pixel Inspector](../rejstrik.md#pixel-inspector) · [Rejstřík: Material Parameter Collection](../rejstrik.md#material-parameter-collection)
