# Kompozice: skládej místo dědění

Godot je na kompozici postavený — node je komponenta a scéna je jejich složenina. Tahle kapitola vysvětluje, proč se `player.gd` po třetí schopnosti hroutí, jak vypadá komponenta, která se dá přenést do dalšího projektu, a kde má skládání hranici. Ta poslední část je tu proto, že o ní ostatní tutoriály mlčí: máme dvě videa, která si zdánlivě protiřečí — jedno změřilo, že node navíc nic nestojí, druhé ukazuje obrazovku, kterou nody stály **115 milisekund**. Obě mají pravdu a v tom rozdílu je celé poučení.

---

## Has-a místo is-a: hrdinův batoh

**Zdroj:** [Mastering Composition for Beginners in Godot](https://www.youtube.com/watch?v=e3H_nw4w5U8) · [Code With Ro](https://www.youtube.com/channel/UCN1RBQN6LXaOFKRSznC0mnw) · 58 min, tutoriál · + [How You Can Easily Make Your Code Simpler in Godot 4](https://www.youtube.com/watch?v=74y6zWZfQKk) · [Bitlytic](https://www.youtube.com/channel/UCOlPBtGeh1YGL_rWpOLgLyg) · ~7 min, tutoriál

**Shrnutí:** Dědičnost odpovídá na otázku „co ta věc **je**", kompozice na otázku „co ta věc **má**". Rozdíl vypadá akademicky, dokud nenarazíš na strom, který má život jako nepřítel, ale nemá se hýbat — a ty zjistíš, že mu musíš dát schopnost útočit, protože je ve společném předkovi. Háček, který spor rozhoduje: **v Godotu nejde dědit ze dvou tříd naráz**, takže první `StaticBody2D` v hierarchii postavené na `CharacterBody2D` ti rozbije celý strom dědičnosti.

### Rozpad myšlenky

**Kontext problému** popisuje Code With Ro jako trajektorii, kterou pozná každý [(0:49)](https://www.youtube.com/watch?v=e3H_nw4w5U8&t=49s): začneš pohybem — funguje. Přidáš dvojskok, dash, útok mečem, úhyb, blok štítem. `player.gd` má tři sta řádků *a nepřátele jsi ještě nezačal*. V tu chvíli přichází myšlenka „radši to začnu znovu". Diagnóza je jedna věta: skript porušil **single responsibility** — jeden skript, jedna práce.

**Proč dědičnost narazí,** ukazuje Bitlytic na příkladu, který je cennější než jakákoli teorie [(0:48)](https://www.youtube.com/watch?v=74y6zWZfQKk&t=48s). Hráč a nepřítel sdílejí útok, život a hitbox — dobře, vytáhneme je do třídy `Entity` a oba z ní zdědí. Elegantní. Pak přijde **strom**, který má taky život a taky se dá zasáhnout. Zdědí z `Entity` a rovnou dostane i schopnost útočit, kterou nechceme. To je otravné, ale ne fatální. Fatální je tohle [(1:35)](https://www.youtube.com/watch?v=74y6zWZfQKk&t=95s): hráč a nepřítel jsou `CharacterBody2D`, strom je `StaticBody2D` — a **z více tříd dědit nejde**. Buď je `Entity` potomkem `CharacterBody2D` (a strom se musí umět hýbat, což nechceme), nebo `Entity` rozštěpíš na `StaticEntity` a `CharacterEntity` a začneš stavět taxonomii. Autorův komentář sedí: *„a to jsme jenom přidali strom."*

**Mechanismus kompozice** je pak triviální [(2:21)](https://www.youtube.com/watch?v=74y6zWZfQKk&t=141s): místo jedné nadtřídy uděláš `AttackComponent`, `HealthComponent`, `HitboxComponent` — a každá entita si vezme ty, které potřebuje. Strom dostane život a hitbox, střela útok a hitbox (*„je jedno, kolik má střela životů; když do něčeho narazí, zanikne"*), a **na tom, z čeho ta entita dědí, přestane záležet**. Code With Ro pro to má dobrý obraz [(2:23)](https://www.youtube.com/watch?v=e3H_nw4w5U8&t=143s): komponenty jsou **hrdinův batoh**. Chceš, aby uměl plavat? Nepředěláváš hrdinu, přidáš mu do batohu ploutve.

**Tři zisky**, které autor jmenuje [(2:23)](https://www.youtube.com/watch?v=e3H_nw4w5U8&t=143s) — a stojí za to je číst jako tři různé věci, ne jako tři slova pro totéž:

- **Znovupoužitelnost** přesahuje projekt. Komponentu, kterou jsi doladil, přeneseš do dalšího projektu; *„je to, jako bys psal plugin do enginu."*
- **Zapouzdření** je hlavně o ladění [(3:10)](https://www.youtube.com/watch?v=e3H_nw4w5U8&t=190s): postava nebere damage → **víš, kde bug je**, a komponentu si můžeš otestovat v prázdné scéně zvlášť. Bonus, na který se zapomíná: **i UI se tím zjednoduší** — health bar se nedívá do skriptu hráče, dívá se do health komponenty.
- **Iterativní design**: „při bloku se má chodit o 20 % pomaleji" je v monolitu noční můra `if`ů, s komponentami je to jeden signál ze štítu do pohybové komponenty [(3:57)](https://www.youtube.com/watch?v=e3H_nw4w5U8&t=237s).

> **Pozn.:** Rozhodovací test „is it a?" má knihovna popsaný [z unrealí strany](../praxe/principy-architektury.md#dedicnost-test-is-it-a-a-rodic-jako-smlouva) — a stojí za to všimnout si, že **oba enginy došly ke stejnému doporučení jinou cestou**. UE ke komponentám tlačí přes `ActorComponent`, protože actor je těžký objekt; Godot k nim tlačí proto, že **node je komponenta už z definice** a skládání je tu výchozí operace, ne vzor, který se musí zavádět. Rozdíl je v ceně vstupu: v Unrealu je „udělám z toho komponentu" rozhodnutí, v Godotu je to to, co děláš tak jako tak.

**Souvislosti:** [Komponenta má být sobecká](#komponenta-ma-byt-sobecka-test-kamene) *(jak taková komponenta vypadá)* · [Principy architektury: komponenty místo dědičnosti](../praxe/principy-architektury.md#komponenty-misto-dedicnosti-skladej-misto-vetveni) *(týž spor v UE)* · [Nody a scény](zaklady.md#nody-a-sceny-strom-ktery-je-zaroven-architekturou) · [Od tří parametrů k jednomu objektu](gdscript.md#od-tri-parametru-k-jednomu-objektu-vlastni-trida-jako-datovy-kontrakt) *(týž autor, předchozí díl série)* · [Rejstřík: Inheritance](../rejstrik.md#inheritance) · [Rejstřík: Separation of concerns](../rejstrik.md#separation-of-concerns)

---

## Komponenta má být sobecká: test kamene

**Zdroj:** [Mastering Composition for Beginners in Godot](https://www.youtube.com/watch?v=e3H_nw4w5U8) · [Code With Ro](https://www.youtube.com/channel/UCN1RBQN6LXaOFKRSznC0mnw) · 58 min, tutoriál · + [Using Composition to Make More Scalable Games in Godot](https://www.youtube.com/watch?v=rCu8vQrdDDI) · [Firebelley Games](https://www.youtube.com/channel/UC89NzFUOsBrjRSJt4Y8s6WQ) · ~10 min, tutoriál

**Shrnutí:** Dobrá komponenta neví, komu slouží. Code With Ro na to má test, který se dá použít okamžitě: **„kdyby ten skript seděl na obyčejném kameni, fungoval by pořád?"** Když ano, je komponenta hotová. Firebelley přidává druhou půlku otázky — *„jaká je minimální množina znovupoužitelné funkčnosti, o které vím jistě, že se bude hodit ve víc scénách?"* A háček, o kterém se v tutoriálech nemluví: obě videa nezávisle varují, že **jde přehnat granularitu** a skončit se sto komponentami ve stromu.

### Rozpad myšlenky

**Sobeckost komponenty** je konkrétní požadavek, ne postoj [(8:37)](https://www.youtube.com/watch?v=e3H_nw4w5U8&t=517s): *„moje pohybová komponenta neví, že pomáhá hráči zachránit království. Ví jen, že má proměnnou rychlost a vektor směru."* Právě proto funguje na kostlivci stejně jako na hrdinovi. Odborně je to *stateless* / *context agnostic*; prakticky je to test kamene.

**Jak se komponenta zapojí,** je tu důležitější než jak se napíše. Historicky se to dělalo cestou `@onready var health = get_node("Components/HealthComponent")` — a to je **křehké**, protože přejmenování nebo přesun nodu shodí hru [(6:17)](https://www.youtube.com/watch?v=e3H_nw4w5U8&t=377s). Dnešní způsob je **typovaný export**:

- `@export var health: HealthComponent` vyrobí v inspektoru **zásuvku**, do které se komponenta přetáhne myší. Přesuneš-li node později, spojení drží.
- Typ není kosmetika: **do zásuvky nejde vložit nic jiného než health komponenta** a editor to vynutí [(7:04)](https://www.youtube.com/watch?v=e3H_nw4w5U8&t=424s). Autor to shrnuje užitečně — *„zabrání to těm tichým bugům, kdy se kód pokusí zavolat jump na health skriptu a spadne."*
- Alternativa pro věci hluboko ve stromu je **unikátní jméno** (`%HealthComponent`), které je najde bez ohledu na cestu.

**Skládání komponent na sebe.** Firebelleyho příklad ukazuje věc, kterou samotná definice neprozradí [(4:45)](https://www.youtube.com/watch?v=rCu8vQrdDDI&t=285s): jeho `HurtboxComponent` **nedělá nic užitečného sám** — umí přijmout zásah, ale ten nemá následek, dokud mu nepřipojíš health komponentu. A to je záměr, ne nedodělek: *„je to táž kompozice, jakou dělá `CharacterBody2D`, který taky funguje až ve chvíli, kdy mu dáš collision shape."* Stejně tak `PathfindComponent` si vyžádá `VelocityComponent`, protože sám umí jen počítat cestu, ne se hýbat.

**Kořenový skript se tím nestane zbytečným — dostane vyšší roli.** Code With Ro ji pojmenoval **orchestrátor** [(9:24)](https://www.youtube.com/watch?v=e3H_nw4w5U8&t=564s): skript hráče nedělá těžkou práci, řídí stav. *„Hele, pohybová komponento, input komponenta hlásí stisk útoku, tak se na chvíli zastav, dokud útočná komponenta neskončí."* Firebelley to říká z druhé strany [(7:03)](https://www.youtube.com/watch?v=rCu8vQrdDDI&t=423s): kořenový skript má být **lepidlo** — lehký kód, který drží komponenty pohromadě a řeší jen interakce mezi nimi.

**A teď ta hranice.** Firebelley je na ni konkrétní [(8:37)](https://www.youtube.com/watch?v=rCu8vQrdDDI&t=517s): *„kde se to dá pokazit, je granularita — nechceš skončit u sta komponent ve stromu."* Jeho vlastní příklad, co komponenta **není**: stavové automaty nepřátel. Nedělá je genericky, píše je pro každou entitu zvlášť, *„protože jsou natolik specifické pro chování té entity, že se to nevyplatí modularizovat"* — a otevřeně přiznává, že mu tím vzniká duplicitní kód (akvizice cíle bývá podobná, útok bývá podobný), který **vědomě nechává být**, protože obecné řešení by bylo složitější než ta duplicita.

> **Pozn.:** Ta poslední věta je nejcennější kus obou videí a mimochodem přesně to, co odlišuje zkušenost od nadšení. **Duplicita je cena, ne hřích** — a rozhodovací otázka nezní „opakuje se to?", ale **„mění se ty kopie spolu, nebo nezávisle?"** Když spolu, je to komponenta. Když nezávisle, je abstrakce past. Firebelleyho state machiny se mění nezávisle, takže zůstávají zvlášť; jeho health komponenta se mění naráz, takže je jedna. Táž logika stojí za [pravidlem tří principů](../praxe/principy-architektury.md#tri-principy-skalovatelnosti-separace-volne-vazby-data) a je to jediná obrana proti tomu, aby se z „prefer composition" stal kult.

**Souvislosti:** [Has-a místo is-a](#has-a-misto-is-a-hrdinuv-batoh) *(proč se vůbec skládá)* · [Kolik nodů je moc](#kolik-nodu-je-moc-zmereno) *(kolik ta granularita stojí)* · [Systém místo nepřítele](stavy-a-vzory.md#system-misto-nepritele-prenositelny-balik) *(komponenty jako schopnosti nepřítele)* · [Editor se prohledává](zaklady.md#editor-se-prohledava-ne-prochazi) *(unikátní jména `%`)* · [Rejstřík: Loose coupling](../rejstrik.md#loose-coupling) · [Rejstřík: Single responsibility principle](../rejstrik.md#single-responsibility-principle)

---

## Kolik nodů je moc: změřeno

**Zdroj:** [Godot Performance Myths Debunked: Does Modular Component Design Actually Slow Down Your Game (Part 1)](https://www.youtube.com/watch?v=PWHxoAYmyLM) · [DeeRaghooGames](https://www.youtube.com/channel/UC-KLgU0nzoCCEU6W16CS3vQ) · ~14 min, benchmark

**Shrnutí:** Obava „každá komponenta navíc je node navíc, a nody stojí výkon" je oprávněná otázka se špatně odhadovanou odpovědí. Autor postavil měřicí stůl: tentýž slime jednou jako **jeden monolitický skript**, podruhé jako **kořen + šest komponent**, a pustil na scénu 500 až 2 000 kusů. Výsledek: modulární verze je pomalejší **zhruba o desetinu** — a při realistickém počtu nepřátel je rozdíl **neměřitelný**. Háček je v tom, co ta čísla neříkají: obě verze se rozpadly ve stejném okamžiku, takže **nody nejsou to, co tvou hru zabije**.

### Rozpad myšlenky

**Metodika stojí za převzetí**, protože se dá zopakovat na vlastním projektu [(2:58)](https://www.youtube.com/watch?v=PWHxoAYmyLM&t=178s). Autor **vypnul VSync** a nenastavil strop FPS — jinak by `delta` vždy hlásila 16,6 ms, protože engine čeká na monitor, a měřilo by se čekání místo práce [(3:45)](https://www.youtube.com/watch?v=PWHxoAYmyLM&t=225s). Pak `delta × 1000` dá **frame time v milisekundách**, což je jediné číslo, které je při optimalizaci k něčemu (FPS je jeho převrácená hodnota a hůř se z něj počítá rozpočet). Prahy nastavil proti **rozpočtu 16,6 ms na 60 FPS**: zelená pod 8 ms, žlutá nad 8, červená nad 15. A nenechal nepřátele stát — časovač jim postupně vyprazdňuje život, takže se naráz spustí health bary, poškozovací čísla, probliknutí, zvuk i částice.

**Naměřené hodnoty** (monolit → modulární):

| nepřátel | monolit | modulární | poznámka |
|---|---|---|---|
| 500 | 125–130 FPS | 112–122 FPS | obojí zelené |
| 1 000 | 54–58 FPS | 47–52 FPS | žlutá, špičky do červené |
| 1 500 | 19–35 FPS | 17–28 FPS | červená |
| 2 000 | 9–17 FPS | 8–12 FPS | nehratelné |
| **~20 (realisticky)** | **1402–1428 FPS** | **1394–1402 FPS** | rozdíl v šumu |

**Proč modulární verze prohrává** [(9:21)](https://www.youtube.com/watch?v=PWHxoAYmyLM&t=561s), a proč je ten důvod méně zajímavý, než se zdá: každý node má malou režii v CPU i paměti, takže 1 000 nepřátel se šesti komponentami je **6 000 nodů místo tisíce**. Druhá polovina ceny není v počtu, ale v komunikaci: monolit odečte život z lokální proměnné v témž skriptu, modulární verze **projde strom, zavolá funkci v cizím skriptu a vyšle signál**. Jednotlivě mikroskopické, tisíckrát za snímek měřitelné.

**Závěr, který si autor dovolí a my ho podepisujeme** [(11:42)](https://www.youtube.com/watch?v=PWHxoAYmyLM&t=702s): *„jestli tvoje hra seká, není to nikdy proto, že jsi použil health komponentu místo natvrdo napsaného skriptu."* Musel by ses dostat k tisícům současně žijících entit, než tě režie nodů začne zajímat — a do té doby narazíš na **draw cally, rendering a fyzikální kolize**, tedy věci, které se dějí v `_process` a `_physics_process`.

> **Pozn.:** Tohle je [předčasná optimalizace](../rejstrik.md#premature-optimization) učebnicově: reálný náklad architektonického rozhodnutí byl **odhadován bez měření** a odhad byl špatný o řád. Zajímavá je i sociologie kolem — video vzniklo z komentáře pod jiným videem („cítí se to dobře, ale co výkon?"), tedy z otázky, kterou si klade každý a nikdo ji neověří. **Chování, které si z toho bereme: než změníš architekturu kvůli výkonu, postav si měřicí stůl.** Půl hodiny práce a máš číslo místo pocitu. Ta rada má ovšem jednu tvrdou výhradu — viz [následující myšlenka](#kdyz-nody-opravdu-boli-115-ms-na-jednu-obrazovku), kde totéž měření dopadne přesně opačně.

**Souvislosti:** [Když nody opravdu bolí](#kdyz-nody-opravdu-boli-115-ms-na-jednu-obrazovku) *(protipříklad, který mez upřesňuje)* · [Co skutečně stojí výkon](projekt-a-vykon.md#co-skutecne-stoji-vykon-ne-nody-ale-co-v-nich-bezi-kazdy-snimek) *(pokračování téhož benchmarku)* · [Optimalizace scény](../praxe/optimalizace.md#proc-jsou-levely-pomale-od-instanci-po-data-layers) *(draw cally z unrealí strany)* · [Rejstřík: Premature optimization](../rejstrik.md#premature-optimization) · [Rejstřík: Frame time](../rejstrik.md#frame-time)

---

## Když nody opravdu bolí: 115 ms na jednu obrazovku

**Zdroj:** [Stop Using Nodes for Everything in Godot](https://www.youtube.com/watch?v=1PnG3r1rKcs) · [Firebelley Games](https://www.youtube.com/channel/UC89NzFUOsBrjRSJt4Y8s6WQ) · ~6 min, případovka

**Shrnutí:** Obrazovka se sto kartami se v autorově hře vykreslovala **115 ms** — skoro sedm zahozených snímků. Po přepsání trvá **pod 10 ms**. Nešlo o špatný kód: každá karta byla scéna s desítkami nodů a **instanciovat sto takových scén v jednom snímku prostě nejde**. Řešení, které zní hůř, než je: obejít nody a mluvit s **RenderingServerem** přímo. Háček, kvůli kterému tahle myšlenka stojí hned za tou předchozí: to, co je při stálém běhu zadarmo, může být při hromadném vzniku drtivé.

### Rozpad myšlenky

**Co autor zkusil, než sáhl po tomhle** [(0:47)](https://www.youtube.com/watch?v=1PnG3r1rKcs&t=47s), je na tom to poučné: **object pooling** a **rozložení instanciace do několika snímků**. Obojí fungovalo částečně a obojí *„působilo spíš jako hack, který se dřív nebo později rozbije"*. Diagnóza, ke které došel, je přesná a nesvádí vinu na engine: **jediná skutečná oprava je zmenšit počet nodů přidávaných do stromu.**

**Mechanismus obejití** stojí na jednoduchém modelu [(2:19)](https://www.youtube.com/watch?v=1PnG3r1rKcs&t=139s): `Sprite2D` sám nic nekreslí — je to **konfigurační objekt**, který svoje data předá RenderingServeru. Z čehož plyne, že **kterýkoli node, jenž pod kapotou používá RenderingServer, se dá obejít tím, že RenderingServer oslovíš sám.** Prakticky: `create_canvas_item()` vrátí **RID** (resource ID), na canvas item se pověsí textura (`canvas_item_add_texture_rect`), materiál a transformace (`canvas_item_set_transform`) — a co je nejdůležitější pro použitelnost, **canvas items se dají zanořovat do sebe** a dědí transformaci rodiče přesně jako `Node2D` v editoru.

**Cena té zkratky** je jedna věta, kterou nelze přeslechnout [(3:05)](https://www.youtube.com/watch?v=1PnG3r1rKcs&t=185s): **RID si musíš uklidit sám.** Skončil-li canvas item, musíš ho explicitně uvolnit; engine to za tebe neudělá. Tím se z bezpečné práce se stromem stává ruční správa životního cyklu — a to je přesně ta daň, kterou nody normálně platí za tebe.

**Výsledek** [(4:37)](https://www.youtube.com/watch?v=1PnG3r1rKcs&t=277s): karta zůstala `Control` (kvůli myši a možnosti přeřadit ji jinam ve stromu), ale při instanciaci **nevzniká žádný další node** — jen strom canvas itemů, kde každý nahrazuje jeden bývalý node. Sto karet za **~8 ms, a to v debug buildu**.

> **Pozn.:** Postavené vedle [změřeného benchmarku](#kolik-nodu-je-moc-zmereno) to vypadá jako spor a není. DeeRaghoo měřil **ustálený stav** — nody, které už ve stromu jsou, běží a nic zvláštního se s nimi neděje. Firebelley narazil na **hromadný vznik**: sto scén, které musejí vzniknout, zapojit se do stromu a nastavit se **v jediném snímku**. To je jiná operace s jinou cenou. Praktické pravidlo, které z té dvojice plyne a které ani jedno video nevysloví: **počet nodů řeš podle toho, kolik jich vzniká naráz, ne kolik jich existuje.** A protipól k tomu je taky jasný — sáhnout po RenderingServeru bez naměřeného čísla znamená vyměnit bezpečnost za výkon, který možná nepotřebuješ.

**Souvislosti:** [Kolik nodů je moc](#kolik-nodu-je-moc-zmereno) *(druhá strana téhož měření)* · [Mapa 2D nodů](zaklady.md#mapa-2d-nodu-vyber-tela-je-prvni-designove-rozhodnuti) *(`CanvasGroup` jako levnější mezikrok)* · [Optimalizace scény](../praxe/optimalizace.md#proc-jsou-levely-pomale-od-instanci-po-data-layers) · [Rejstřík: Object pooling](../rejstrik.md#object-pooling) · [Rejstřík: Draw call](../rejstrik.md#draw-call)
