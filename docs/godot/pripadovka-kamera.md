# Případovka: kamera pro pixel art

Kamera je u pixel-artové hry místo, kde se sejde nejvíc drobných technických rozhodnutí — a kde se každé z nich pozná okamžitě, protože pixel buď sedí, nebo nesedí. Autor projektu tomu věnoval celý devlog a udělal přitom dvě věci, které se cení: **pojmenoval jednotlivé artefakty**, takže se o nich dá vůbec mluvit, a **ukázal i řešení, které nefungovalo**.

Kapitola navazuje na [nastavení projektu](prvni-hra.md#nastaveni-projektu-je-soucast-hry-ne-administrativa) a na [rozlišení jako jednosměrné dveře](projekt-a-vykon.md#vizualni-pohodli-nesmi-diktovat-fyzikalni-pravdu); tady je totéž viděné zevnitř jednoho projektu.

---

## Čtyři vady pixelové kamery a rozlišení, které polovinu z nich řeší

**Zdroj:** [I made the PERFECT camera for my Indie Game! | Devlog](https://www.youtube.com/watch?v=80VlawJmDiE) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~23 min, devlog · + [Game Dev Secrets: Resolution!](https://www.youtube.com/watch?v=y_TwL5IfPxA) · týž kanál · ~1 min

**Shrnutí:** Když se hledá „proč mi v pixel-artové hře poskakuje obraz", vyleze **tucet různých příčin** a žádná odpověď. Autor to rozsekl tím, že si **artefakty pojmenoval**: *jitter* (obraz se chvěje), *frame stutter* (kamera se opozdí a doskočí), *boiling* (pixely se „vaří", než se usadí na velikosti) a *tearing* (dlaždice se od sebe trhají). Háček, který stojí za převzetí, i když pixel art neděláš: **pojmenování vad je diagnostický nástroj** — bez něj hledáš „nějakou divnost".

### Rozpad myšlenky

**Odkud se to bere** [(0:49)](https://www.youtube.com/watch?v=80VlawJmDiE&t=49s), vysvětlené způsobem, který si zapamatuješ: ten čtvereček na obrazovce **není pixel**. Na 4K monitoru je to hromada skutečných pixelů, které jeden pixel jen předstírají. A protože engine umí kameru posunout o **1,2 jednotky**, vzniká otázka, na kterou nemá kdo odpovědět: *„co to znamená posunout o dvě desetiny pixelu, když pixel je to nejmenší, co existuje?"*

**Čtyři vady, každá s vlastním projevem** [(2:21)](https://www.youtube.com/watch?v=80VlawJmDiE&t=141s):

| vada | jak vypadá |
|---|---|
| **jitter** | obraz se u zastavení kamery chvěje; sprity se „kroutí" místo aby se usadily |
| **frame stutter** | kamera se za postavou opozdí o kousek a pak **doskočí** |
| **boiling** | pixely se neusazují na *pozici*, ale na *velikosti* — dlaždice se „rozpouštějí" na místo |
| **tearing** | dlaždice se od sebe trhají; vznikají mezery, černé čáry, nebo se do sebe propadají |

Autorovo hodnocení stojí za zmínku, protože ukazuje, že to nejsou rovnocenné problémy: tearing označuje za *„jeden z nejhorších artefaktů, vypadá úplně příšerně"*, a boiling nesnáší z jiného důvodu — *„zbaví tě to všeho toho pěkného ostrého pixel artu"*, do kterého se dala spousta práce.

**A jeden důležitý detail metodiky** [(4:42)](https://www.youtube.com/watch?v=80VlawJmDiE&t=282s): aby ty vady vůbec ukázal, **vypnul svoje dosavadní opravy**. Postavil si tedy kontrolní vzorek. To je táž disciplína jako [postavit si měřicí stůl](kompozice.md#kolik-nodu-je-moc-zmereno) místo odhadování — jen pro vizuální problémy.

**První oprava je rozhodnutí, ne kód: rozlišení** [(6:14)](https://www.youtube.com/watch?v=80VlawJmDiE&t=374s). A minutový klip k tomu dodává celou úvahu [(0:01)](https://www.youtube.com/watch?v=y_TwL5IfPxA&t=1s). Pixel art se **hezky škáluje jen celými čísly** — dvakrát, třikrát, ne 2,4×. Nabízí se dělit 1080p čtyřmi, tedy **480 × 270**, a spousta her to používá. Jenže *„ne každý monitor má stejné rozlišení"*: na 2K displeji je z toho **násobek 5,33** a artefakty jsou zpátky.

Řešení je jedno konkrétní číslo — **640 × 360** (nebo jeho polovina 320 × 180) — protože se do běžných rozlišení vejde **beze zbytku**: ×2 dá 720p, ×3 dá 1080p, ×4 dá 1440p, ×6 dá 4K. Autor na to sám dodává, že *„k tomuhle rozhodnutí mi pomohly všechny ty game jamy"* — je to poznatek, který se nedá vyčíst, jen odsedět.

> **Pozn.:** Totéž rozlišení nezávisle doporučuje i [Fat Earth Studios](projekt-a-vykon.md#vizualni-pohodli-nesmi-diktovat-fyzikalni-pravdu) — shoda dvou nezávislých projektů je u takového čísla asi to nejlepší, co lze dostat. Za pozornost stojí, že **rozlišení řeší jen půlku problémů**: srovná škálování, ale nic neudělá s tím, že se kamera potřebuje posouvat o desetiny pixelu. Na to je potřeba druhá polovina řešení — [subpixelový posun](#lasagna-kamera-subpixelovy-posun-v-shaderu). A jedna vlastní poznámka k pojmenování: ta čtyři slova (jitter, stutter, boiling, tearing) **nejsou zavedená terminologie** — autor sám říká *„nevím, jestli se to takhle jmenuje"*. Přesto jsou užitečná, protože rozlišují čtyři různé příčiny; a to je celý smysl toho, proč si věci pojmenováváme.

**Souvislosti:** [Lasagna kamera](#lasagna-kamera-subpixelovy-posun-v-shaderu) *(druhá polovina řešení)* · [Vizuální pohodlí nesmí diktovat fyzikální pravdu](projekt-a-vykon.md#vizualni-pohodli-nesmi-diktovat-fyzikalni-pravdu) *(rozlišení jako one-way door)* · [Pixel art do Godotu](2d-svet.md#pixel-art-do-godotu-paleta-silueta-a-jedno-nastaveni) · [2D vizuál: pixel art](../teorie/2d-vizual.md#pixel-art-je-rozhodnuti-ne-nouzove-reseni) · [Rejstřík: Integer scaling](../rejstrik.md#integer-scaling) · [Rejstřík: Pixel-perfect](../rejstrik.md#pixel-perfect)

---

## Lasagna kamera: subpixelový posun v shaderu

**Zdroj:** [I made the PERFECT camera for my Indie Game! | Devlog](https://www.youtube.com/watch?v=80VlawJmDiE) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~23 min, devlog

**Shrnutí:** Trik, kterým autor vyřešil zbývající artefakty, je elegantní: **kamera ve světě se posune o celý pixel a zbývající zlomek dožene shader**, který posune celý vykreslený obraz. Pixely tak zůstanou dokonalé a pohyb plynulý. Cena je ale tvrdá — pixel-perfect viewport **zakáže rotaci a squash & stretch**, což autora dohnalo ke stavbě mnohovrstvého systému, kterému sám říká lasagna. A háček, kvůli kterému kapitola stojí za čtení celá: **jeho vlastní test celé měsíce lhal**, protože rychlost postavy náhodou vycházela na celá čísla.

### Rozpad myšlenky

**Jádro řešení** [(7:01)](https://www.youtube.com/watch?v=80VlawJmDiE&t=421s): pohne-li se kamera o 1,4 jednotky, **ve světě se posune o 1 pixel** a **shader posune vykreslený obraz o zbývajících 0,4**. Výsledek je posun o přesně správnou vzdálenost, ale mřížka pixelů zůstane nedotčená. Autor u toho vysvětluje, proč nešel jednodušší cestou — prostě renderovat v 640 × 360 a roztáhnout: *„přijdeš tím o možnost rotovat sprity, protože je k dispozici jenom tolik pixelů"*, a navíc *„ta věc s poměrem stran podle mě dělá víc problémů, než kolik jich vyřeší."*

**Cena, kterou to má** [(13:12)](https://www.youtube.com/watch?v=80VlawJmDiE&t=792s), se ukázala až potom: aby shader mohl fungovat, musí být vykreslený obraz **už předtím pixel-perfect** — a to znamená **žádné rotace a žádný squash & stretch**. U postavy mu to nevadí: *„ručně kreslený squash & stretch je stejně lepší, působí retro a autenticky."* Vadí to u **částic a efektů**, kde je *„fajn rychle přidat trochu roztažení, otočit to o kousek, dodat tomu šťávu"*.

**Řešení přes vrstvy** [(13:58)](https://www.youtube.com/watch?v=80VlawJmDiE&t=838s) je ta „lasagna": několik viewportů poskládaných na sebe — přední vrstva, hlavní svět s postavou, zadní vrstva, pozadí. **Hlavní a pozadí jsou pixel-perfect** a mají subpixelový shader; **přední a zadní vrstva pixel-perfect nejsou**, takže na nich sprite může rotovat a deformovat se, jak chce. Na konci se to složí do jednoho obrazu. Autor přiznává, že to nakonec přehnal: *„skončil jsem asi u třinácti viewportů… asi je všechny nepotřebuju, ale nikomu neublíží."*

**A teď ta část, kterou by většina lidí zamlčela** [(17:57)](https://www.youtube.com/watch?v=80VlawJmDiE&t=1077s). Autor byl přesvědčený, že subpixelový shader funguje — a pak zjistil, že **se vůbec nespouštěl**. Důvod je krásně banální: rychlost postavy byla nastavená na **180**, hra běží na **60 FPS**, což jsou **přesně 3 jednotky za snímek** — tedy **žádná desetinná část**. Shader neměl co dohánět, takže jeho chybná matematika nikdy nevyplavala. Odhalilo se to náhodou, když rychlost mírně změnil a postava se *„začala uprostřed obrazovky divoce třást"*.

Zobecnění, které z toho děláme a které je nejcennější věcí celé kapitoly: **test, ve kterém je zajímavá hodnota náhodou nulová, není test.** Postava s rychlostí dělitelnou snímkovou frekvencí byla degenerovaný případ, který systém obcházel. Vyplatí se proto ladit na **nepohodlných číslech** — nedělitelných rychlostech, nesudých rozměrech, nekulatých časech — protože přesně ty odhalí, jestli kód počítá, nebo má štěstí.

**Ladění snížením abstrakce** [(15:31)](https://www.youtube.com/watch?v=80VlawJmDiE&t=931s) je vedlejší, ale hezká historka: aby viděl, co dělají kamery jednotlivých viewportů, **připnul na každou kameru sprite** — a protože náhodou sáhl po prvním souboru ve složce, sledoval po scéně jezdit šneky. Metoda je ovšem správná: **udělej neviditelný stav viditelným, než začneš uvažovat.**

> **Pozn.:** Než tenhle přístup převezmeš, zvaž, že je to **hodně práce za hodně specifický zisk**. Godot má vestavěné pixel-perfect režimy a u většiny her stačí; autor se do vlastního řešení pustil proto, že chtěl **zároveň** ostré pixely, plynulou kameru a rotující částice — což jsou tři požadavky, které si navzájem odporují. To je legitimní volba pro projekt, jehož vizuál je hlavní argument, a předčasná optimalizace pro skoro každý jiný. Rozhodovací otázka zní: **vadí ti ty artefakty tak, že to hráč pozná?** Autor sám říká, že si jich všímá hlavně proto, že na hru kouká celý den.

**Souvislosti:** [Čtyři vady pixelové kamery](#ctyri-vady-pixelove-kamery-a-rozliseni-ktere-polovinu-z-nich-resi) · [Kolik nodů je moc](kompozice.md#kolik-nodu-je-moc-zmereno) *(táž disciplína: měř, neodhaduj)* · [Nástroje pro sebe](projekt-a-vykon.md#nastroje-pro-sebe-editor-script-ktery-ti-usetri-boilerplate) *(zviditelnit stav)* · [Rejstřík: Pixel-perfect](../rejstrik.md#pixel-perfect) · [Rejstřík: Render target](../rejstrik.md#render-target) · [Rejstřík: Squash & stretch](../rejstrik.md#squash-stretch)

---

## Kamera musí koukat dopředu

**Zdroj:** [Game Dev Secrets: Oops, we broke the camera](https://www.youtube.com/watch?v=KTOyrG2rfCU) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~1 min

**Shrnutí:** Kamera přilepená na postavu je tuhá, takže se přidá vyhlazování — a tím se **zruší důvod, proč kamera postavu vůbec sleduje**. Vyhlazená kamera se totiž opožďuje, takže větší část obrazovky ukazuje **to, co je za tebou**. V krajním případě *„je na to, co je před tebou, míň než čtvrtina obrazovky"*. Oprava je jednořádková a přitom se na ni zapomíná: **posuň kameru před postavu ve směru pohybu.**

### Rozpad myšlenky

**Řetěz tří rozhodnutí**, z nichž každé opravuje předchozí [(0:02)](https://www.youtube.com/watch?v=KTOyrG2rfCU&t=2s):

1. **Kamera na pozici postavy každý snímek.** Přesné, ale *„velmi statické a tuhé, protože kopíruje pohyb naprosto přesně"*.
2. **Vyhlazování** — kamera se k pozici postavy každý snímek jen přibližuje. Pohyb je příjemný, ale kamera **zaostává** a ukazuje minulost místo budoucnosti.
3. **Look ahead** — kamera se při pohybu **vysune před postavu**, aby na obrazovce byla ta část světa, kterou hráč potřebuje vidět.

Autorova argumentace je funkční, ne estetická, a proto sedí: *„jak máš bojovat s nepřáteli a trefovat těžké skoky, když je ani nevidíš?"* Kamera není rám kolem postavy — je to **nástroj pro rozhodování**, a rozhoduje se dopředu.

**Nastavení je věc míry** [(0:48)](https://www.youtube.com/watch?v=KTOyrG2rfCU&t=48s): v ukázce autor efekt zveličuje, aby byl vidět, a hned připojuje verzi s doladěnými hodnotami, kde je *„výrazně jemnější"*. Kombinace vyhlazování a look aheadu pak *„vytvoří kameru, která rámuje hratelnost správně a hezky se hýbe"*.

> **Pozn.:** Tenhle klip je hezká ukázka toho, že **oprava jednoho problému často vyrobí druhý** — a že se to nepozná, dokud se nepodíváš na to, k čemu ta věc vlastně je. Vyhlazování je samo o sobě správné; teprve otázka „co má být na obrazovce?" ukáže, že chybí třetí krok. V knihovně má look ahead [vlastní heslo](../rejstrik.md#look-ahead) a širší kontext v kapitole o [kameře](../teorie/kamera.md), kde se rozebírají i camera directors — tedy o patro výš: kdo v danou chvíli o rámování rozhoduje. Pro platformer se navíc vyplatí vědět, že [Celeste jde opačnou cestou](../teorie/game-feel.md#celeste-krivky-v-snimcich-a-hrst-tichych-ulev) — místnosti v jednom statickém záběru, protože **nehýbající se kamera usnadňuje přesnost**.

**Souvislosti:** [Kamera](../teorie/kamera.md) *(camera directors a rámování obecně)* · [Celeste: statická kamera](../teorie/game-feel.md#celeste-krivky-v-snimcich-a-hrst-tichych-ulev) *(opačné rozhodnutí a proč)* · [Čtyři vady pixelové kamery](#ctyri-vady-pixelove-kamery-a-rozliseni-ktere-polovinu-z-nich-resi) · [Rejstřík: Look ahead](../rejstrik.md#look-ahead) · [Rejstřík: Camera director](../rejstrik.md#camera-director)
