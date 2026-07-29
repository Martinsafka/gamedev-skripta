# První hra: od prázdné scény k .exe

Nejužitečnější věc na tutoriálu první hry není hra — je to **oblouk**: prázdný projekt, hráč, svět, nebezpečí, sbírání, skóre, zvuk, export. Tahle kapitola z toho oblouku vytahuje čtyři momenty, které se vyplatí umět dřív, než začneš stavět něco vlastního: znovupoužitelnou scénu jako jednotku návrhu, časovou nezávislost pohybu, AnimationPlayer coby deklarativní časovač — a nastavení projektu, které dělá rozdíl mezi školním cvičením a hrou.

Předpokládá mentální model z kapitoly [Nody, scény a strom](zaklady.md).

---

## Znovupoužitelná scéna: jedna kill zone pro propast i pro slimáka

**Zdroj:** [How to make a Video Game - Godot Beginner Tutorial](https://www.youtube.com/watch?v=LOhfqjmasi0) · [Brackeys](https://www.youtube.com/channel/UCYbK_tjZ2OrIZFBvU6CCMiA) · 77 min, tutoriál

**Shrnutí:** Ve chvíli, kdy hra potřebuje „něco, co hráče zabije", má člověk sto chutí napsat to do propasti a pak znova do nepřítele. Godot nabízí lepší tah: udělat **scénu bez tvaru**, která umí jen jedno — detekovat hráče a zabít ho — a tvar jí dodat až na místě použití. Ta jedna scéna pak obslouží propast, slimáka i budoucí bodáky. Háček je v tom, co se vynechalo: **kill zone záměrně nemá vlastní collision shape**, a právě to z ní dělá znovupoužitelnou věc.

### Rozpad myšlenky

**Problém, který to řeší,** je nejběžnější zdroj duplicit v malé hře. Nebezpečných věcí je ve hře deset druhů a chování mají identické: dotkni se → zemři. Kdo je píše jednu po druhé, má deset kopií téhož a jednu z nich zapomene opravit.

**Mechanismus** má tři kroky [(35:44)](https://www.youtube.com/watch?v=LOhfqjmasi0&t=2144s):

1. Nová scéna s kořenem `Area2D` — tedy detekce, ne kolize. Area2D hlásí vstup a výstup těles, ale nic nezastavuje.
2. **Collision mask se nastaví na vrstvu hráče** — kill zone se tak zajímá výhradně o hráče a ignoruje plošiny, mince i sama sebe.
3. **A teď to podstatné: žádný `CollisionShape2D` se nepřidá.** Autor to zdůvodňuje přesně [(35:44)](https://www.youtube.com/watch?v=LOhfqjmasi0&t=2144s) — chceme scénu použít pro věci různých tvarů, takže tvar patří až k použití. V propasti dostane kill zone `WorldBoundaryShape` (nekonečná rovina), v slimákovi obdélník kolem těla.

Skript scény je pak triviální [(37:18)](https://www.youtube.com/watch?v=LOhfqjmasi0&t=2238s): na signál `body_entered` spustit časovač, na `timeout` zavolat `get_tree().reload_current_scene()`.

**Důkaz, že to funguje**, přijde o pár minut později, když se staví nepřítel [(42:35)](https://www.youtube.com/watch?v=LOhfqjmasi0&t=2555s). Slimák je `Node2D` + `AnimatedSprite2D` + **instance kill zone s obdélníkovým tvarem** — a je hotovo. Nebezpečnost nepřítele se nemusela programovat vůbec; jen se do něj vložila existující scéna. Autor tenhle moment sám označuje za místo, kde to *„začne být opravdu zajímavé"*, a má pravdu: je to okamžik, kdy se vyplatí investice do abstrakce, která před pěti minutami vypadala zbytečně.

**Vrstvy jako filtr místo podmínek v kódu.** Souvisí s tím jedno rozhodnutí, které se dá udělat i špatně [(32:35)](https://www.youtube.com/watch?v=LOhfqjmasi0&t=1955s). Mince původně reagovala na cokoli, co do ní vstoupilo — včetně pohyblivé plošiny, která přes ni projížděla. Dvě cesty ven: (a) v kódu ověřit, co za těleso to bylo, nebo (b) **dát hráče na vlastní fyzikální vrstvu a nastavit minci masku jen na tu vrstvu**. Autor volí druhou a to je ta správná volba: **filtr patří do konfigurace, ne do každé podmínky ve skriptu.** Vrstva říká „co jsem", maska říká „co mě zajímá".

**Hranice.** Znovupoužitelnost má cenu — kill zone bez tvaru je scéna, která sama o sobě „nefunguje" a v editoru vypadá rozbitě. To je přijatelná daň za to, že se logika smrti píše jednou. Horší je jiná mez: jakmile budeš chtít, aby různá nebezpečí dělala různé věci (bodáky ubírají život, propast restartuje, kyselina zpomaluje), tahle scéna se začne větvit a v tu chvíli je čas na parametr, ne na další `if`.

> **Pozn.:** Tenhle vzorec je zdejší varianta téhož principu, který v Unrealu vede k [interakci přes overlap místo trasování v Ticku](../praxe/interakce-bez-event-ticku.md#overlap-trigger-misto-trasovani-v-ticku) — reagovat na událost, ne se ptát každý snímek. A rozhodnutí „tvar až na místě použití" je malý bratříček [komponentního uvažování](../praxe/principy-architektury.md#komponenty-misto-dedicnosti-skladej-misto-vetveni): scéna nese *chování*, hostitel dodá *specifika*.

**Souvislosti:** [Nody a scény](zaklady.md#nody-a-sceny-strom-ktery-je-zaroven-architekturou) *(scéna jako znovupoužitelný balík)* · [Mapa 2D nodů](zaklady.md#mapa-2d-nodu-vyber-tela-je-prvni-designove-rozhodnuti) *(Area2D vs. fyzikální tělo)* · [Interakce bez Event Ticku](../praxe/interakce-bez-event-ticku.md#overlap-trigger-misto-trasovani-v-ticku) *(týž princip v UE)* · [Rejstřík: Collision mask](../rejstrik.md#collision-mask)

---

## Delta a physics process: proč se rychlost násobí časem

**Zdroj:** [How to make a Video Game - Godot Beginner Tutorial](https://www.youtube.com/watch?v=LOhfqjmasi0) · [Brackeys](https://www.youtube.com/channel/UCYbK_tjZ2OrIZFBvU6CCMiA) · 77 min, tutoriál

**Shrnutí:** Přičíst k pozici jeden pixel za snímek vypadá jako pohyb a je to bug — na rychlejším počítači bude nepřítel rychlejší. Oprava je znásobit posun hodnotou **delta**, tedy časem uplynulým od minulého snímku. K tomu patří druhé rozhodnutí: `_process` běží tak často, jak to jde, kdežto `_physics_process` běží **v pevném rytmu 60× za sekundu**, a fyzika potřebuje to druhé. Obojí dohromady je minimum, bez kterého se v enginu nedá hnout.

### Rozpad myšlenky

**Kontext problému** vzniká z toho, jak hra funguje [(44:56)](https://www.youtube.com/watch?v=LOhfqjmasi0&t=2696s): před vykreslením každého snímku engine aktualizuje stav všech nodů, pak nakreslí obraz, a takhle pořád dokola — *game loop*. Kolikrát za sekundu se to stihne, závisí na stroji a na tom, co se zrovna děje. Film má pevných 24 snímků, hra jich chce co nejvíc.

A tady je ta chyba, kterou udělá každý [(45:44)](https://www.youtube.com/watch?v=LOhfqjmasi0&t=2744s): `position.x += 1` v `_process` znamená *jeden pixel za snímek*, tedy rychlost svázanou s výkonem počítače. Autor to říká přesně: *nepřítel se bude někdy hýbat rychleji než jindy, což není moc dobré.*

**Mechanismus opravy** [(46:30)](https://www.youtube.com/watch?v=LOhfqjmasi0&t=2790s): **delta je čas, který uplynul od minulého snímku.** Vysoký framerate → malá delta → malý posun. Nízký framerate → velká delta → velký posun. Vynásobením se obojí vyrovná a pohyb se stane nezávislým na výkonu. Autor nabízí použitelné pravidlo palce: *máš-li rychlost, kterou si můžeš nastavit, nejspíš ji máš násobit deltou.*

Jednotky se tím posunou do smysluplné roviny — `position.x += 1 * delta` znamená **jeden pixel za sekundu**, což je skoro nic, takže konstanta poskočí na 60. A rovnou do pojmenované konstanty na začátku skriptu [(47:16)](https://www.youtube.com/watch?v=LOhfqjmasi0&t=2836s), protože číslo zapsané uprostřed výrazu se špatně ladí — táž disciplína, kterou popisuje [Literály se mstí](../teorie/co-se-ucit.md#literaly-se-msti-cisla-do-promennych-klavesy-do-pojmenovanych-akci).

**Kanonický tvar pohybu** je pak `position.x += direction * speed * delta` [(48:03)](https://www.youtube.com/watch?v=LOhfqjmasi0&t=2883s), kde `direction` je 1 nebo −1. Tři složky, každá má svou roli: kam, jak rychle, za jak dlouho.

**A proč `_physics_process`, když už máme deltu?** [(53:29)](https://www.youtube.com/watch?v=LOhfqjmasi0&t=3209s) Protože fyzikální engine je jediná část, které proměnlivá frekvence opravdu vadí — *fyzika potřebuje pevné intervaly, jinak se chová trhaně.* `_physics_process` běží defaultně **60× za sekundu bez ohledu na framerate hry**. Pravidlo je tedy jednoduché: **cokoli sahá na fyziku (pohyb tělesa, které má s něčím kolidovat), patří do `_physics_process`; zbytek do `_process`.**

**Ping-pong nepřítele jako celý příklad.** Dva `RayCast2D` (vlevo, vpravo) a v každém snímku dvě podmínky [(49:35)](https://www.youtube.com/watch?v=LOhfqjmasi0&t=2975s): koliduje-li pravý paprsek, `direction = -1` a sprite se otočí; koliduje-li levý, `direction = 1`. Slimák se sám odráží mezi libovolnými dvěma zdmi — a co je na tom cenné, je **absence dat o levelu**: nepřítel neví, kde je, ptá se prostoru kolem sebe. To je čtení světa dotazem, ne konfigurací, a škáluje to na libovolný počet umístění.

**Hranice.** Delta neřeší všechno. Při skokových výpadcích framerate může být delta tak velká, že objekt „proskočí" stěnou, protože se mezi dvěma snímky posune o víc, než je tloušťka kolizního tvaru. Godot to částečně řeší pevnou frekvencí fyziky a nastavením continuous collision detection — ale pravidlo palce zůstává: **kritické kolize nestav na rychlostech, které za snímek urazí víc než vlastní tělo.**

> **Pozn.:** Vstupy si zaslouží stejnou pozornost jako pohyb. Godot má **input action systém** [(54:17)](https://www.youtube.com/watch?v=LOhfqjmasi0&t=3257s): akce `jump`, `move_left`, `move_right` se definují v nastavení projektu a klávesy se k nim váží — klidně **víc kláves k jedné akci** (šipky i WASD naráz, bez jediného řádku kódu navíc). Skript se pak ptá na akci, ne na klávesu. Proč to není kosmetika, ukazuje jinde v této sekci [keyboard ghosting](gdscript.md#kdyz-bug-neni-v-kodu-keyboard-ghosting): některé kombinace kláves na levných klávesnicích prostě nedorazí, a jediná obrana je **nechat hráče přemapovat ovládání** — což bez akcí nejde.

**Souvislosti:** [Mapa 2D nodů](zaklady.md#mapa-2d-nodu-vyber-tela-je-prvni-designove-rozhodnuti) *(RayCast2D vs. ShapeCast2D)* · [Když bug není v kódu](gdscript.md#kdyz-bug-neni-v-kodu-keyboard-ghosting) *(proč jsou pojmenované akce nutnost)* · [Literály se mstí](../teorie/co-se-ucit.md#literaly-se-msti-cisla-do-promennych-klavesy-do-pojmenovanych-akci) *(čísla do konstant, klávesy do akcí)* · [Rejstřík: Delta time](../rejstrik.md#delta-time)

---

## AnimationPlayer jako časovač: sekvence bez jediného řádku kódu

**Zdroj:** [How to make a Video Game - Godot Beginner Tutorial](https://www.youtube.com/watch?v=LOhfqjmasi0) · [Brackeys](https://www.youtube.com/channel/UCYbK_tjZ2OrIZFBvU6CCMiA) · 77 min, tutoriál

**Shrnutí:** Sebrání mince má nepříjemné časování: chceš zahrát zvuk, ale objekt hned mizí, takže zvuk nemá kde doznít. Napsat to v kódu jde a je to nepříjemné — čekání, ochrana proti dvojímu sebrání, viditelnost. Godot má elegantnější řešení: **AnimationPlayer neanimuje jen vlastnosti, umí i volat funkce**, takže celá sekvence „skryj, vypni kolizi, přehraj zvuk, po vteřině se smaž" je jedna animace a jeden řádek kódu.

### Rozpad myšlenky

**Problém je klasická past na začátečníka** [(1:10:31)](https://www.youtube.com/watch?v=LOhfqjmasi0&t=4231s). Mince při sebrání volá `queue_free()`, tedy okamžité smazání — a zvuk, který se měl přehrát, umře s ní. Kód, který na zvuk počká, přinese další problémy: mince je pořád vidět a pořád se dá sebrat znovu.

**Mechanismus** má čtyři stopy v jedné animaci `pickup` [(1:11:17)](https://www.youtube.com/watch?v=LOhfqjmasi0&t=4277s):

- **viditelnost** sprite → false v čase 0,
- **`disabled` na collision shapu** → true v čase 0 (zabrání dvojímu sebrání),
- **`playing` na audio přehrávači** → true v čase 0,
- a v čase 1 s **call method track** — stopa, která volá funkci [(1:13:36)](https://www.youtube.com/watch?v=LOhfqjmasi0&t=4416s). Vloží se klíč a vybere metoda `queue_free`.

Skript se scvrkne na `animation_player.play("pickup")`. Autor to komentuje přesně: *všechno, co bychom udělali kódem, je uvnitř téhle animace.*

**Reset track je to, co z toho dělá udržovatelnou věc** [(1:11:17)](https://www.youtube.com/watch?v=LOhfqjmasi0&t=4277s). Když zakládáš klíč na vlastnost, Godot nabídne vytvořit **stopu `RESET`**, která hodnotu vrátí do výchozího stavu. Bez ní se ti stane klasika: v editoru zůstane objekt v posledním naanimovaném stavu (neviditelný, s vypnutou kolizí) a ty půl hodiny hledáš, proč scéna vypadá rozbitě. S ní si kdykoli přehráním resetu srovnáš scénu zpátky.

**Proč to není jen trik.** Sekvence napsaná jako animace je **deklarativní**: vidíš celý průběh na časové ose naráz, změna časování je tažení klíče a nikdo nemusí číst kód, aby pochopil pořadí. Sekvence napsaná jako kód je imperativní — spolehlivější pro složité větvení, ale u „udělej tyhle čtyři věci v tomhle pořadí" je to zbytečná režie. **Volba mezi nimi je volba mezi čitelností a flexibilitou**, a u efektů, které nemají větve, vyhrává čitelnost.

**Hranice** stojí za vyslovení, protože video je nezmiňuje. Animace jako sekvencer se rozbije ve chvíli, kdy potřebuješ **podmínky** („zvuk jen když má hráč zapnutý zvuk", „bonus jen při comba nad 3") — pak buď zapneš animaci z kódu podle podmínky, nebo se vrátíš k imperativnímu zápisu. A call method tracky se **hůř refaktorují**: přejmenuješ-li funkci, editor tě na rozbitou stopu neupozorní tak hlasitě jako na chybu ve skriptu.

> **Pozn.:** Táž kapitola tutoriálu obsahuje ještě jednu drobnost, která se hodí i mimo Godot [(1:09:44)](https://www.youtube.com/watch?v=LOhfqjmasi0&t=4184s): hudba se restartovala pokaždé, když se scéna po smrti načetla znovu. Řešení je **autoload** — scéna zaregistrovaná jako globální, která přežívá výměnu scén. Je to zdejší singleton a platí na něj přesně tytéž výhrady jako všude jinde: skvělé na hudbu, save data a audio mixer, špatné jako odkladiště pro všechno, co se zrovna nehodí jinam.

**Souvislosti:** [Znovupoužitelná scéna](#znovupouzitelna-scena-jedna-kill-zone-pro-propast-i-pro-slimaka) *(týž tutoriál, jiná abstrakce)* · [Nastavení projektu](#nastaveni-projektu-je-soucast-hry-ne-administrativa) · [Rejstřík: Autoload](../rejstrik.md#autoload) · [Rejstřík: Singleton](../rejstrik.md#singleton)

---

## Nastavení projektu je součást hry, ne administrativa

**Zdroj:** [Do THIS Before You Publish Your Godot Game](https://www.youtube.com/watch?v=3iGHpha-DmE) · [StayAtHomeDev](https://www.youtube.com/channel/UCDshKIMtFjYreCzApleuV8w) · ~4 min, tipy · + [How to make a Video Game - Godot Beginner Tutorial](https://www.youtube.com/watch?v=LOhfqjmasi0) · [Brackeys](https://www.youtube.com/channel/UCYbK_tjZ2OrIZFBvU6CCMiA) · 77 min, tutoriál

**Shrnutí:** Osm položek v nastavení projektu rozhoduje o tom, jestli tvoje hra působí jako školní cvičení, nebo jako produkt — a **žádná z nich není složitá**. Ikona, splash, hlavní scéna, jméno, režim okna, kurzor, antialiasing a filtrování textur. Autorova formulace to trefuje: nedělat je *„může způsobit, že hra působí lajdácky"*, a to je škoda za deset minut práce.

### Rozpad myšlenky

**Problém je nenápadný, protože se týká věcí, které při vývoji nevidíš.** Ve svém editoru ikonu neřešíš, splash přeskakuješ a okno si roztáhneš. Hráč potká přesně tyhle věci první — *ještě než uvidí, do čeho jsi nalil krev, pot a slzy* [(0:02)](https://www.youtube.com/watch?v=3iGHpha-DmE&t=2s).

**První dojem** (`Application → Config` a `Application → Boot Splash`) [(0:02)](https://www.youtube.com/watch?v=3iGHpha-DmE&t=2s): **vlastní ikona** místo loga Godotu · **splash** s vlastním obrázkem a barvou pozadí — a autor je smířlivý, aspoň změň barvu · **jméno hry**, protože jinak to bude „My Untitled Game 123", a rovnou i **lokalizovaná jména** přes *Add Translation* pro jiné jazyky.

**Hlavní scéna** (`Application → Run`) [(0:49)](https://www.youtube.com/watch?v=3iGHpha-DmE&t=49s) je položka, na kterou se snadno zapomene, a bez ní hra po spuštění neví, co načíst. Brackeys ji nastavuje hned na začátku tutoriálu, protože ho na to Godot vyzve při prvním spuštění [(7:36)](https://www.youtube.com/watch?v=LOhfqjmasi0&t=456s).

**Okno a kurzor** [(1:35)](https://www.youtube.com/watch?v=3iGHpha-DmE&t=95s): `Display → Window → Mode` na fullscreen, pokud je hra myšlená na celou obrazovku — *hráči fullscreen čekají a okno působí amatérsky*. A `Display → Mouse Cursor` pro vlastní kurzor včetně hotspotu, což je levný způsob, jak stylovou konzistenci protáhnout i mimo herní plochu.

**Vyhlazení** [(2:22)](https://www.youtube.com/watch?v=3iGHpha-DmE&t=142s): zubaté hrany na šikmých čarách a křivkách — *„jaggies"* — patří pryč, **pokud nejsou součástí retro stylu**. Antialiasing něco stojí, ale na PC je dneska standard; Godot nabízí volby zvlášť pro 2D a 3D plus screen space a temporal varianty. Ta podmínka není formalita: u pixel artu je vyhlazení přesně to, co styl ničí (viz níž).

**A dvě věci navíc, které v nastavení bydlí taky.** Import Blender souborů přímo do projektu [(2:22)](https://www.youtube.com/watch?v=3iGHpha-DmE&t=142s) se zapíná ve dvou krocích — `Project Settings → File System → Import` zapnout Blender a `Editor Settings → File System → Import` nasměrovat na instalaci Blenderu 3+. A **filtrování textur**, které Brackeys řeší hned, jakmile se objeví rozmazaný pixel art [(11:32)](https://www.youtube.com/watch?v=LOhfqjmasi0&t=692s): `Rendering → Textures → Default Texture Filter` z `Linear` na `Nearest`. Godot se ve výchozím stavu snaží textury vyhlazovat, což je u fotorealistických textur žádoucí a u pixel artu katastrofa.

**Export sám je pak krátký** [(1:14:23)](https://www.youtube.com/watch?v=LOhfqjmasi0&t=4463s): poprvé se musí stáhnout **export templates** (`Editor → Manage Export Templates`), protože nejsou součástí instalace — proto je Godot tak malý. Pak `Project → Export`, přidat platformu, zapnout **Embed PCK** (vše do jednoho souboru), vyplnit jméno produktu a vypnout *export with debug*.

> **Pozn.:** Stejná logika platí na písmo [(1:01:14)](https://www.youtube.com/watch?v=LOhfqjmasi0&t=3674s): v pixel-artové hře je pohled hodně přiblížený, takže běžný font vypadá rozmazaně a **velikost písma musí být násobek základní velikosti** — 8, 16, 24, 32; devítka už rozmazává. To je táž disciplína jako [integer scaling u pixel artu](../teorie/2d-vizual.md#pixel-art-je-rozhodnuti-ne-nouzove-reseni) a stojí za ní totéž: v pixel artu je celočíselnost součástí stylu, ne detail. Typografická stránka věci má vlastní kapitolu — [Typografie](../teorie/typografie.md).

**Souvislosti:** [AnimationPlayer jako časovač](#animationplayer-jako-casovac-sekvence-bez-jedineho-radku-kodu) · [2D vizuál: pixel art je rozhodnutí](../teorie/2d-vizual.md#pixel-art-je-rozhodnuti-ne-nouzove-reseni) *(proč nearest a celá čísla)* · [Vydání hry](../teorie/vydani-hry.md) *(co dělat s hotovým buildem)* · [První dojem](../teorie/prvni-dojem.md) *(tentýž princip o patro výš)* · [Rejstřík: Export template](../rejstrik.md#export-template) · [Rejstřík: Nearest-neighbor filtering](../rejstrik.md#nearest-neighbor-filtering)
