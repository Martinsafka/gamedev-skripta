# Souboj: od montáže po hit stop

Kompletní melee souboj v Blueprintech, rozložený na otázky, na které musí odpovědět každý soubojový systém: kde logika bydlí, kdy smí útok navázat, co přesně zasáhne a kolikrát, jak terč zareaguje a čím se rána prodá. Páteří je 3,8hodinový tutoriál, který systém staví jako dvě přenositelné komponenty. K němu pět vrstev game feelu a zdraví po končetinách. Proč juice funguje a co dělá souboj rytmickým, vysvětluje [Game feel](../teorie/game-feel.md); variantu nad Motion Matchingem najdeš v [Systémech nad MM](mm-systemy.md#combat-nad-mm-horni-telo-v-montazi-spodni-v-matchingu) a frame data v [godotové případovce](../godot/pripadovka-nepratele.md#frame-data-definuj-system-driv-nez-ho-postavis). Kde souboj přechází v kameru nebo párovou animaci, pokračuje [finisher bez střihu](cutsceny.md#finisher-bez-strihu-sekvence-ktera-se-prehraje-kolem-hrace) a [zápas se sekcemi montáže](interakcni-animace.md#zapas-se-smyckou-sekce-montaze-a-rozhodnuti-hrace).

---

## Dvě komponenty místo bojové postavy: útočník a terč

**Zdroj:** [How to Make a Combat System in UE5](https://www.youtube.com/watch?v=4omEu9N9WIE) · [Evans Bohl](https://www.youtube.com/channel/UC36uolRnnwoMMH27vzecLBg) · ~3 h 49 min, tutoriál (UE 5.7)

**Shrnutí:** Celý systém je postavený tak, aby postava sama neobsahovala ani uzel bojové logiky. Útočník dostane komponentu `AC_CombatSystem`, terč komponentu `AC_HealthSystem` a animační část žije v šabloně AnimBP bez skeletu. Nová dvojice postav se pak nastaví za pár minut. Háček: přenositelnost nevzniká z komponent samotných, ale z toho, že **data útoků jsou v montážích** a komponenty si samy dohledají vlastníka i všechno, co potřebují.

### Rozpad myšlenky

**Proč.** Bojová logika napsaná přímo do postavy se s každou další postavou kopíruje a každá oprava se dělá N-krát. Evans Bohl si od začátku klade cíl, že bojová komponenta půjde přidat jakékoli postavě a zdravotní čemukoli, co má jít zranit, a to bez psaní kódu [(0:48)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=48s). Několik vzorů se pak opakuje celým tutoriálem:

- **Komponenta si najde vlastníka sama.** Na BeginPlay `Get Owner` → cast na Character → uloží si postavu a její mesh [(7:05)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=425s). Postava o komponentě skoro nic neví, jen jí z input akce zavolá `Trigger Attack` [(3:11)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=191s).
- **Události si bere od vlastníka.** Komponenta nemá vlastní Event Point Damage, a tak se přihlásí k delegátu `OnTakePointDamage` postavy [(1:56:45)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=7005s), [(1:57:33)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=7053s). Stejně se bojová komponenta přihlásí k `Landed` [(53:12)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=3192s).
- **Všechno k ladění je v jedné kategorii.** Montáže, mapa reakcí, maximum zdraví i offset ukazatele jdou do kategorie System Parameters [(11:01)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=661s). Kdo komponentu přidá, vidí v Details jen to, co má vyplnit.
- **Data útoku bydlí v montáži.** Damage a rozměry hitboxu jsou instance editable proměnné na notify (viz [hitboxy](#hitbox-podle-toho-jak-poctiva-je-animace-impact-frame-nebo-active-frames)), takže se každý útok ladí na časové ose své animace.
- **Závislosti si komponenty přidají samy.** Hit stop komponentu si bojová i zdravotní komponenta nejdřív zkusí najít (`Get Component by Class`) a přidají ji jen tehdy, když chybí. Postava s oběma systémy tak nemá dvě [(2:39:00)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=9540s), [(2:39:48)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=9588s). Stejně se z kódu nastaví i kolize pro ragdoll, aby se kvůli smrti nemuselo sahat do blueprintu postavy [(2:10:05)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=7805s).

**Důkaz.** Na konci tutoriálu Evans vymění obě postavy za jiné dvě z Paragonu, Crunche a Steela, a nastaví je znovu. Útočník potřebuje montáže s notify, komponentu s vyplněnými poli, input a linked anim graph [(3:43:49)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=13429s). Terč potřebuje mapu reakcí, offset ukazatele a slot v AnimBP [(3:46:57)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=13617s), [(3:47:44)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=13664s).

**Hranice.** AnimBP modul neumí vystavit branch filtry, takže postava s jinou hierarchií kostí potřebuje kopii modulu [(48:30)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=2910s). Autor sám vyjmenovává, co systému chybí: posun vpřed při útoku, root motion a další věci [(3:48:30)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=13710s). Komponenty navíc počítají s tím, že vlastník je Character, takže na jiném pawnu jejich cast neprojde.

> **Pozn.:** Tyhle komponenty nejsou tak zdrženlivé jako zdravotní komponenta v [Principech architektury](principy-architektury.md#komponenty-misto-dedicnosti-skladej-misto-vetveni), která smrt jen ohlásí dispatcherem a co dál, rozhodne vlastník. Evansova komponenta při nule sama zastaví montáž, zapne ragdoll a za čtyři sekundy aktéra zničí [(2:05:24)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=7524s), [(2:12:25)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=7945s). V tutoriálu je to pohodlné. Ve hře, kde smrt nepřítele spouští loot, quest nebo počítadlo vlny, se vyplatí přidat `OnDeath` dispatcher a ragdoll nechat jako jednoho z posluchačů.

**Souvislosti:** [Komunikace Blueprintů: tři kanály](komunikace-blueprintu.md#tri-kanaly-a-kdy-ktery-cast-interface-event-dispatcher) · [Rejstřík: Actor Component](../rejstrik.md#actor-component) · [Rejstřík: Delegate](../rejstrik.md#delegate) · [Rejstřík: Linked anim graph](../rejstrik.md#linked-anim-graph)

---

## Útok je časová osa: montáž, okna z notify a stav, který se musí vrátit

**Zdroj:** [How to Make a Combat System in UE5](https://www.youtube.com/watch?v=4omEu9N9WIE) · [Evans Bohl](https://www.youtube.com/channel/UC36uolRnnwoMMH27vzecLBg) · ~3 h 49 min, tutoriál (UE 5.7)

**Shrnutí:** Útok se nepřehrává jako sekvence, ale jako **montáž přes slot** v AnimBP. O tom, kdy smí přijít další úder, nerozhoduje časovač v kódu, ale **notify state přímo v animaci**: okno pro navázání začíná po zásahu a končí před zotavením, kód jen poslouchá jeho začátek a konec. Háček je ve stavu kolem: montáž, kterou přeruší jiná montáž, nikdy nedoběhne do konce. Pokud se `Can Attack` vrací jen tam, postava přestane útočit.

### Rozpad myšlenky

**Montáž a slot.** Animační sekvence se do AnimBP přes slot dostat nedá, potřebuje montáž [(5:32)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=332s). V anim grafu musí před výstupní pózou stát uzel `Slot`, trubka, ve které montáž přebije všechno, co právě hraje [(3:58)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=238s), [(4:44)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=284s). Jedna montáž může skládat víc sekvencí; Evans do ní dává útok i jeho zotavení [(6:18)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=378s). Ze stejného místa jsou dvě drobnosti z praxe. Přejmenování slotu v montáži umí postavu zaseknout v T-póze, dokud montáž nezavřeš a znovu neotevřeš. A výchozí blend dělá útok „ostýchavý", takže se nedohraje naplno. Svižný útok chce **blend in 0 s a blend out 0,2 s**, nastavené pro všechny montáže najednou přes Property Matrix [(8:41)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=521s), [(9:27)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=567s).

**Combo jako pole a index.** Montáže leží v poli a index ukazuje na aktuální útok. Po každém spuštění se zvýší o jedna a za posledním útokem se vrátí na nulu [(12:35)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=755s); místo větvení stačí `Select Int` [(14:08)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=848s). Samo o sobě to ale dovolí útočit rychlým klikáním bez jakékoli prodlevy [(14:56)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=896s).

**Okno z notify state.** Notify je značka na jednom snímku, notify state má začátek a konec [(16:29)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=989s), [(18:50)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=1130s). Evans si vyrobí vlastní třídu z `AnimNotify_PlayMontageNotifyWindow`, pojmenuje ji ComboInputWindow a dá jí žlutou barvu, aby byla v timeline vidět [(23:29)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=1409s), [(24:15)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=1455s). V jeho útoku úder zasáhne na 5. snímku, okno začne na 10. a trvá 20 snímků [(25:02)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=1502s). Kdo stiskne útok v okně, naváže. Kdo okno mine, musí počkat, až montáž doběhne celá, a combo se vrátí na první útok [(15:42)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=942s).

**Kód jen poslouchá.** `Play Montage` má výstupy On Notify Begin, On Notify End a On Completed [(18:04)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=1084s), [(21:56)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=1316s). Jména notify se rozdělují přes `Switch on Name` bez default pinu a musí přesně odpovídat jménům v animaci [(21:08)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=1268s). Stav drží jediný bool `Can Attack`:
- při útoku se shodí,
- na začátku okna nahodí a na jeho konci zase shodí [(28:06)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=1686s), [(28:55)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=1735s),
- po dokončení montáže se nahodí a index comba se vynuluje [(27:20)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=1640s), [(29:42)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=1782s).

**Konec comba je vlastnost dat.** Bez dalšího zásahu se combo točí dokola. Aby skončilo a hráč musel počkat, stačí, že **poslední montáž okno nemá** [(29:42)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=1782s), [(30:30)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=1830s). Při nasazení na novou postavu to Evans opakuje jako pravidlo [(3:42:14)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=13334s).

**Stav, který se musí vrátit.** Útok ve vzduchu má vlastní montáž a podle `Is Falling` se spustí buď vzdušný, nebo pozemní [(50:52)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=3052s). Vzdušný útok spuštěný těsně před dopadem by dohrával na zemi. Komponenta se proto přihlásí k delegátu `Landed` a při dopadu ho zastaví [(53:12)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=3192s), [(55:32)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=3332s). Spam ve vzduchu hlídá druhý bool a to, kam se zapojí, je designová volba. Nahozený při dopadu dovolí jeden útok na skok, nahozený na Blend Out montáže řetěz útoků ve vzduchu [(57:04)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=3424s), [(57:50)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=3470s).

Pak přijde past [(58:38)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=3518s). `Play Montage` zastaví všechny ostatní montáže, takže pozemní útok přerušený vzdušným nikdy nedoběhne do On Completed a `Can Attack` zůstane navždy false. Evans to opraví tak, že při dopadu vrátí `Can Attack` i index comba [(59:24)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=3564s).

> **Pozn.:** [Godotová případovka](../godot/pripadovka-nepratele.md#combo-a-hit-stop-dva-casovace-a-ctvrt-sekundy) staví totéž combo ze dvou časovačů v kódu, tady okna leží v animaci. Rozdíl není kosmetický. Heslo [Frame data](../rejstrik.md#frame-data) chce, aby časování mělo jediný zdroj pravdy, a notify state v montáži ho má: kdo animaci zrychlí, posune okno s ní. Na past s přerušenou montáží máš ještě jednu cestu: `Play Montage` má i výstup On Interrupted, který při přerušení přijde místo On Completed. Vzor s notifies `AddCombo`/`ResetCombo` nad Motion Matchingem je v [Systémech nad MM](mm-systemy.md#combat-nad-mm-horni-telo-v-montazi-spodni-v-matchingu).

**Souvislosti:** [Rejstřík: Anim montage](../rejstrik.md#anim-montage) · [Rejstřík: Anim Notify](../rejstrik.md#anim-notify) · [Rejstřík: Delegate](../rejstrik.md#delegate) · [Combat je rytmus](../teorie/game-feel.md#combat-je-rytmus-kazdy-utok-ma-ucel-a-placeholder-je-nastroj) *(proč na délce a umístění okna záleží)*

---

## Útok za běhu: horní půlka bojuje, dolní běží — a křivka řekne, kdy ne

**Zdroj:** [How to Make a Combat System in UE5](https://www.youtube.com/watch?v=4omEu9N9WIE) · [Evans Bohl](https://www.youtube.com/channel/UC36uolRnnwoMMH27vzecLBg) · ~3 h 49 min, tutoriál (UE 5.7)

**Shrnutí:** Montáž ve slotu přebije celé tělo, takže útok v běhu vypadá jako jízda na skateboardu. Řešením je Layered Blend per Bone: horní tělo bere pózu z montáže, nohy z locomotion. Platí to ale jen tehdy, když se postava hýbe, a ne v momentech, kdy útok potřebuje celé tělo. Háček: na takový moment, třeba skok s otočkou uprostřed útoku, stačí **křivka v montáži**, kterou AnimBP čte. V animacích, které ji nemají, vrací nulu, a nula znamená „vrstvi" — takže výjimku nesou jen animace, které ji potřebují.

### Rozpad myšlenky

**Vrstvení.** Bez něj se při útoku v běhu zamknou nohy a postava klouže [(30:30)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=1830s). Layered Blend per Bone vezme locomotion jako základ a přes něj položí pózu se slotem [(31:16)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=1876s). Výstup uzlu v anim grafu jde zapojit jen na jedno místo. Locomotion i bojová póza se proto rozvádějí přes **cached pose**, pózu uloženou pod jménem, kterou jde použít víckrát [(32:04)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=1924s), [(32:51)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=1971s).

**Kde se vrství.** Branch filter na pánvi s blend depth 4 rozloží přechod do čtyř kostí: pánev 25 %, spine 1 50 %, spine 2 75 % a od spine 3 výš plných 100 % [(34:23)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=2063s), [(35:11)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=2111s). Stehna jsou ale dětmi pánve, takže se útok propsal i do nohou. Dva další filtry, `thigh_l` a `thigh_r`, s blend depth −1 tyhle větve z vrstvy vyřadí [(35:57)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=2157s). Trup je pak ještě trochu skloněný k zemi. Spraví ho **Mesh Space Rotation Blend**, se kterým se rotace vrstvy bere v prostoru meshe, a ne podle natočení rodičovských kostí [(36:44)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=2204s).

**Kdy se vrství.** Kdyby se vrstvilo pořád, hrály by nohy i ve stoje idle a ztratily by se pohyby celého těla, které animace útoku nese [(36:44)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=2204s). Rozhodne `Blend Poses by Bool` podle `Accelerating`. V pohybu se vrství, ve stoje hraje montáž celé tělo [(37:31)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=2251s), [(38:18)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=2298s). Kvůli vzdušným útokům přibude podmínka „není ve vzduchu", jinak se vzdušný útok smíchá se skokem [(51:38)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=3098s), [(52:25)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=3145s).

**Kdy ne, i když postava běží.** Jeden z útoků je skok s otočkou o 360°. V běhu by se otočil jen trup, zatímco nohy by běžely dál, což je s tělem těžko proveditelné [(39:04)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=2344s). Evans do montáže přidá křivku `BlendOff`. Na prvním snímku má hodnotu 1, od dopadu kolem 12. snímku 0, a s konstantní interpolací, aby mezi nimi nevznikly mezihodnoty [(39:52)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=2392s), [(41:28)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=2488s), [(42:14)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=2534s). AnimBP ji čte přes `Get Curve Value` a vrstvení pustí jen při `BlendOff ≤ 0` a zároveň pohybu [(43:48)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=2628s). Animace bez té křivky vrací nulu [(43:00)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=2580s), takže se nemusí nijak upravovat.

**Modul pro další postavy.** Celá vrstva se přestěhuje do AnimBP vytvořeného jako *template*, tedy bez cílového skeletu [(44:35)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=2675s). Základní pózu dostane přes `Input Pose` a do postavy se zapojí jako Linked Anim Graph s booleany vystavenými jako piny [(46:12)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=2772s), [(46:58)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=2818s). Sloty uvnitř linked grafu se ve výchozím stavu nevyhodnocují. V Class Defaults modulu se proto musí zapnout `Use Main Instance Montage Evaluation Data`, jinak útok nehraje vůbec [(47:44)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=2864s). Při nasazení na další postavu jde místo pinů navázat proměnné modulu rovnou na proměnné jejího AnimBP [(3:45:24)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=13524s).

> **Pozn.:** Tentýž vzor nad Motion Matchingem, tedy slot Upper Body, Layered Blend per Bone a Blend Poses by Bool podle `IsAttacking`, je v [Systémech nad MM](mm-systemy.md#combat-nad-mm-horni-telo-v-montazi-spodni-v-matchingu). Liší se tím, co rozhoduje: tam útok, tady pohyb, takže ve stoje dostane montáž celé tělo. Křivka `BlendOff` stojí na stejném principu jako [křivky, které z montáže řídí svět](interakcni-animace.md#animace-ridi-svet-normalizovane-krivky-v-montazi). Animace nese informaci o tom, co se v ní děje, a kód ji jen čte.

**Souvislosti:** [Rejstřík: Layered Blend Per Bone](../rejstrik.md#layered-blend-per-bone) · [Rejstřík: Cached pose](../rejstrik.md#cached-pose) · [Rejstřík: Blend Poses by Bool](../rejstrik.md#blend-poses-by-bool) · [Rejstřík: Animation curve](../rejstrik.md#animation-curve) · [Rejstřík: Linked anim graph](../rejstrik.md#linked-anim-graph)

---

## Hitbox podle toho, jak poctivá je animace: impact frame, nebo active frames

**Zdroj:** [How to Make a Combat System in UE5](https://www.youtube.com/watch?v=4omEu9N9WIE) · [Evans Bohl](https://www.youtube.com/channel/UC36uolRnnwoMMH27vzecLBg) · ~3 h 49 min, tutoriál (UE 5.7)

**Shrnutí:** Tutoriál nabízí dvě metody detekce, každou pro jiný druh animace. **Jednoduchá:** notify na impact frame spustí jeden box trace před postavou s parametry útoku ve structu. **Pokročilá:** notify state pokryje celé *active frames* a každý snímek protáhne kouli mezi dvěma sockety zbraně. Háček: ani jedna není lepší. Přesná metoda se vyplatí jen tam, kde animace poctivě ukazuje, co zasahuje; kde to neukazuje, poslouží líp box [(1:28:24)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=5304s), [(1:29:12)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=5352s).

### Rozpad myšlenky

**Jednoduchá metoda.** Útok nezasahuje celou dobu, jen malou částí. U prvního útoku je *impact frame* pátý snímek [(1:00:58)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=3658s). Vlastní notify ImpactFrame spustí `Multi Box Trace for Objects`, tedy box, který se sune od startu k cíli a vrátí všechny zasažené objekty zvolených typů, tady Pawn [(1:03:19)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=3799s), [(1:04:08)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=3848s). Box se natočí podle postavy, začne v ní a skončí 120 jednotek před ní. Debug kresba při zásahu zezelená [(1:05:40)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=3940s), [(1:06:26)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=3986s).

**Parametry na útok, ne v kódu.** Jeden box pro všechny útoky nestačí, jeden útok má mít delší dosah a jiný víc poškození [(1:06:26)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=3986s). Struct `F_AttackProfile` (damage, dosah, šířka a výška boxu, typy objektů) se stane instance editable proměnnou přímo na notify třídě [(1:07:12)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=4032s), [(1:14:18)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=4458s). Volání se přestěhuje z komponenty do `Received Notify` v notify blueprintu. Ten si přes `MeshComp` → `Get Owner` → `Get Component by Class` najde bojovou komponentu [(1:11:55)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=4315s), [(1:13:31)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=4411s). Damage a dosah konkrétního útoku se pak nastavují kliknutím na notify v jeho montáži [(1:15:04)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=4504s).

**Trik s plochou.** Délka boxu (half size X) zůstává nulová, takže trace táhne plochu, ne kvádr [(1:11:09)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=4269s). S půldélkou 50 a dosahem 100 by box zasáhl i postavu 150 jednotek daleko. S nulovou délkou je dosah přesně to číslo, které nastavíš.

**Pokročilá metoda.** Jednoduchá má dvě slabiny: box nesleduje zbraň a zásah padne na jediný snímek, přestože útok obvykle zraňuje několik snímků [(1:15:51)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=4551s). Proto vznikne notify state ActiveFrames. Je pojmenovaný podle termínu z bojovek pro snímky, ve kterých útok zraňuje, a v prvním útoku pokrývá snímky 4–8 [(1:16:39)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=4599s), [(1:17:25)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=4645s). Jeho `Received Notify Tick` běží v každém snímku okna [(1:18:14)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=4694s). V něm `Multi Sphere Trace for Objects` táhne kouli od startovního ke koncovému socketu [(1:24:30)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=5070s), [(1:25:17)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=5117s). U Wukongovy hole vede od kosti uprostřed k socketu `weapon_tip`. Ten Evans přidá sám, protože žádná kost na špičce hole nesedí [(1:19:03)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=4743s), [(1:20:36)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=4836s). Struct pokročilého profilu nese damage, oba sockety, poloměr koule a typy objektů [(1:21:23)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=4883s).

**Varianty bez dalšího kódu** [(1:27:38)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=5258s), [(1:28:24)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=5304s):
- víc ActiveFrames na jeden útok, třeba pro úder oběma rukama, nebo aby špička meče zraňovala víc než kořen čepele jako ve Smash Bros.;
- boxer, kterému stačí start i konec na stejné kosti, takže se koule drží na pěsti. U Crunche Evans nastaví úder levou rukou (`hand_l` → `hand_l2`) a připomene, že u úderů a kopů stačí jedna kost [(3:42:14)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=13334s), [(3:43:01)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=13381s).

> **Pozn.:** Tohle je druhá strana [hitboxů z pastí](pasti-a-mechaniky.md#hitboxy-velkorysost-ne-presnost), které mají být velkorysé, ne přesné, zatímco tady se metoda vybírá podle animace. Neodporuje si to: přesnost je k ničemu, když animace „lže", a velkorysost jde i v pokročilé metodě nastavit poloměrem koule. Koule na pěsti se startem i koncem v jednom bodě je mimochodem postup ze [směrových hit reakcí](mm-systemy.md#smerove-hit-reakce-dot-product-rozhodne-odkud-chooser-vybere-co), kde má poloměr 100 a autor ho sám nazývá velkorysým. A ActiveFrames s parametry na každém okně jsou [frame data](../godot/pripadovka-nepratele.md#frame-data-definuj-system-driv-nez-ho-postavis) postavená v UE.

**Souvislosti:** [Rejstřík: Hitbox](../rejstrik.md#hitbox) · [Rejstřík: Active frames](../rejstrik.md#active-frames) · [Rejstřík: Socket](../rejstrik.md#socket) · [Rejstřík: Struct](../rejstrik.md#struct) · [Rejstřík: Anim Notify](../rejstrik.md#anim-notify)

---

## Damage jednou za útok: seznam zasažených patří útoku, ne terči

**Zdroj:** [How to Make a Combat System in UE5](https://www.youtube.com/watch?v=4omEu9N9WIE) · [Evans Bohl](https://www.youtube.com/channel/UC36uolRnnwoMMH27vzecLBg) · ~3 h 49 min, tutoriál (UE 5.7)

**Shrnutí:** Koule tažená v každém snímku trefí tentýž cíl několikrát, takže útok za 20 udělí 100. První nápad je krátká nezranitelnost terče. Funguje jen do chvíle, než se změní délka jeho reakce: pomalá reakce pak spolkne půlku comba. Paměť proto patří **útoku**. Pole zasažených se vyprázdní s každým novým útokem a damage dostane jen ten, kdo v něm ještě není.

### Rozpad myšlenky

**Odkud damage přichází.** Oba trace vracejí, jestli něco trefily, a pole všech zásahů. Funkce `ApplyDamageToHitActors` ho projde a na každého zasaženého zavolá vestavěný `Apply Damage`, s útočníkem jako causerem [(1:29:58)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=5398s), [(1:32:22)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=5542s), [(1:33:08)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=5588s). Terč musí mít zapnuté `Can Be Damaged` a zachytit `Event Any Damage` [(1:34:42)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=5682s).

**Problém.** Výpis v Event Any Damage se objeví víckrát za jediný úder, protože zásah zachytí několik po sobě jdoucích koulí. Útok za 20 bodů zachycený pětkrát udělí 100 [(1:35:28)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=5728s).

**První oprava a proč nestačí.** Terč si po zásahu na chvíli vypne `Can Be Damaged`, nejdřív na 0,2 s a později až do konce reakční animace [(1:36:16)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=5776s), [(1:38:36)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=5916s). Vypadá to dobře, dokud Evans reakci nezpomalí na poloviční rychlost. Z pětiranného comba pak dopadne jen pár ran, protože terč je pořád „v reakci" [(1:39:24)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=5964s). Hráč, který combo vystřihl, přitom čeká, že platí každá rána.

**Správná oprava.** Bojová komponenta drží pole `HitActors` a na začátku každého útoku, pozemního i vzdušného, ho vyprázdní [(1:40:11)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=6011s), [(1:40:59)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=6059s). Před každým damage se zeptá `Contains`: damage dostane jen ten, kdo v poli ještě není, a hned se do něj zapíše [(1:41:46)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=6106s), [(1:42:34)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=6154s). Nezranitelnost terče pak není potřeba vůbec. Každý útok zraní každý cíl právě jednou, i když terč ještě dohrává předchozí reakci [(1:43:21)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=6201s).

> **Pozn.:** Nejde to proti radě z [kostry pasti](pasti-a-mechaniky.md#kostra-pasti-a-tri-variace-bodaky-rameno-rotor), že nezranitelnost patří na postavu. Past zraňuje opakovaně v čase, takže imunitu po zásahu musí řešit ten, kdo zásahy schytává. Útok je naopak jedna událost s jasným začátkem a kolikrát smí zasáhnout, je vlastnost útoku. Obojí jde kombinovat a každé řeší jiný problém: seznam na útoku vícenásobné zásahy jedné rány, nezranitelnost na postavě opakované zásahy z různých zdrojů.

**Souvislosti:** [Rejstřík: Apply Damage](../rejstrik.md#apply-damage) · [Hitbox podle poctivosti animace](#hitbox-podle-toho-jak-poctiva-je-animace-impact-frame-nebo-active-frames) · [Rejstřík: Hitbox](../rejstrik.md#hitbox)

---

## Terč: směr rány, zdraví a smrt bez řádku v postavě

**Zdroj:** [How to Make a Combat System in UE5](https://www.youtube.com/watch?v=4omEu9N9WIE) · [Evans Bohl](https://www.youtube.com/channel/UC36uolRnnwoMMH27vzecLBg) · ~3 h 49 min, tutoriál (UE 5.7)

**Shrnutí:** Druhá komponenta udělá terč z čehokoli. Přihlásí se k bodovému poškození vlastníka a spočítá, odkud rána přišla. Pak přehraje reakci z mapy směr → montáž, odečte zdraví a při nule postavu shodí jako ragdoll. Háček je ve dvou nenápadných kolizních nastaveních: bez prvního propadne ragdoll podlahou, bez druhého mrtvola dál blokuje cestu. Komponenta si obě nastaví sama.

### Rozpad myšlenky

**Odkud.** `Apply Damage` neříká, kam rána dopadla, `Apply Point Damage` přidá i hit result [(1:44:54)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=6294s), [(1:45:41)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=6341s). Terč z místa dopadu spočítá směr funkcí `HitLocationToDirection` označenou jako Pure function [(1:47:14)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=6434s). Postup je tento:
1. Jednotkový vektor od sebe k místu zásahu.
2. `Acos` jeho dot productu s forward vektorem. Do 45° je zásah zepředu [(1:48:58)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=6538s), [(1:49:45)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=6585s).
3. Totéž s negovaným forward vektorem. Do 45° je zásah zezadu [(1:50:33)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=6633s).
4. Zbytek rozsoudí znaménko dot productu s right vektorem: kladné je zprava, jinak zleva [(1:51:19)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=6679s), [(1:52:27)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=6747s).

Výsledek je Enum `E_Direction` a podle něj se vybere montáž [(1:53:15)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=6795s).

**Mapa místo výběru.** V komponentě nahradí `Select` proměnná typu map (směr → montáž) v kategorii System Parameters a uzel `Find` [(1:58:20)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=7100s), [(1:59:07)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=7147s). Kdo komponentu přidává, jen vyplní čtyři řádky. Postava sama nemá v grafu nic, a přesto reaguje [(2:01:26)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=7286s).

**Zdraví.** Maximum je 100 a při BeginPlay se aktuální zdraví nastaví na maximum [(2:02:13)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=7333s). `ProcessDamage` odečte poškození a přes `Max` s nulou nikdy nespadne pod nulu [(2:03:47)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=7427s). Při nule zastaví montáž reakce a vypne `Can Be Damaged` [(2:05:24)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=7524s), [(2:06:13)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=7573s).

**Smrt jako ragdoll a dvě kolizní pasti.** Mesh potřebuje physics asset. Automaticky vygenerovaný na ukázku stačí, dobrý dá hodně práce [(2:06:59)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=7619s), [(2:07:47)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=7667s). `Set Simulate Physics` na meshi postavu shodí rovnou skrz podlahu, protože mesh má kolizi jen Query; musí mít **Query and Physics** [(2:08:33)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=7713s), [(2:09:19)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=7759s). Komponenta si to nastaví sama přes `Set Collision Enabled`, aby se kvůli tomu nemuselo sahat do postavy [(2:10:05)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=7805s). Druhá past: kapsle zůstane stát a hráč se o mrtvolu zasekne. Opraví to `Set Collision Response to Channel` s Pawn → Ignore [(2:10:51)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=7851s). Nakonec časovač, který tělo za čtyři sekundy odstraní [(2:11:38)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=7898s).

> **Pozn.:** Směrové reakce s chooserem místo mapy jsou v [Systémech nad MM](mm-systemy.md#smerove-hit-reakce-dot-product-rozhodne-odkud-chooser-vybere-co). Tam se porovnávají absolutní hodnoty obou dot productů a 45° kužel dává v rovině tytéž čtyři kvadranty. Jednu věc ale video neřeší: Evans počítá směr k **místu zásahu ve 3D**. Rána zepředu vysoko nad středem kapsle, třeba do hlavy, má velkou svislou složku. Úhel k forward vektoru pak přeleze 45° a funkce zásah pošle do levé nebo pravé větve. Kdo zasahuje i vysoko a nízko, vynuluje před normalizací Z. Ragdoll do hloubky, včetně physics assetu a vstávání, je v kapitole [Ragdoll](ragdoll.md#ragdoll-za-minutu-preset-simulace-kamera).

**Souvislosti:** [Rejstřík: Apply Damage](../rejstrik.md#apply-damage) · [Rejstřík: Dot product](../rejstrik.md#dot-product) · [Rejstřík: Map (dictionary)](../rejstrik.md#map-dictionary) · [Rejstřík: Enum](../rejstrik.md#enum) · [Health bar nad hlavou](ui-ve-svete.md#health-bar-nad-hlavou-screen-space-ukazatel-z-materialu-a-dojezd-poskozeni) *(tatáž komponenta spawnuje i ukazatel)* · [Ragdoll, který se chrání](ragdoll.md#ragdoll-ktery-se-chrani-pozy-z-animace-sila-z-krivek-a-cas-do-dopadu) *(kam až jde smrt přes fyziku)*

---

## Hit stop: zastav oba, ale každého jinak

**Zdroj:** [How to Make a Combat System in UE5](https://www.youtube.com/watch?v=4omEu9N9WIE) · [Evans Bohl](https://www.youtube.com/channel/UC36uolRnnwoMMH27vzecLBg) · ~3 h 49 min, tutoriál (UE 5.7)

**Shrnutí:** Hit stop zmrazí oba bojovníky v okamžiku zásahu. Evans ho staví podle rad, které ve svých videích dává Masahiro Sakurai, tvůrce Smash Bros. Je to komponenta, která mění **čas jednoho aktéra** (Custom Time Dilation), ne celé hry, a proto může zasažený úplně stát, zatímco útočník jen zpomalí na 5 %. K tomu přijde otřes meshe: zasažený se třese víc než útočník, otřes slábne podle křivky a míří vždy doleva a doprava z pohledu kamery.

### Rozpad myšlenky

**Proč čas jednoho aktéra.** `Set Custom Time Dilation` zpomalí nebo zrychlí čas konkrétního aktéra. Hodnota 0 ho zmrazí a časovač po zadané době vrátí 1 [(2:35:52)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=9352s), [(2:37:28)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=9448s), [(2:38:14)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=9494s). Komponentu `AC_HitStop` si bojová i zdravotní komponenta přidají, pokud chybí [(2:39:00)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=9540s). Spouští se v `ApplyDamageToHitActors`, kde jsou zasažení po ruce. Délky jsou v tutoriálu čtvrt a půl sekundy [(2:41:24)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=9684s), [(2:42:12)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=9732s).

**Útočník zpomalí, nezamrzne.** Sakurai radí zasaženého zmrazit a útočníka jen silně zpomalit. Evans útočníkovi nastaví dilation 0,05, takže jeho animace běží na 5 % rychlosti [(2:42:36)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=9756s), [(2:43:23)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=9803s).

**Otřes meshe, ne aktéra.** Třese se jen skeletal mesh. Kdyby se třásl celý aktér, třásla by se i kapsle a další úder by mohl minout [(2:44:11)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=9851s). Mesh se střídavě posouvá o amplitudu na obě strany od své výchozí relativní polohy, s `teleport`, aby ignoroval kolize [(2:45:44)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=9944s), [(2:46:30)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=9990s). Kroky spouští opakovaný časovač s intervalem 1 / rychlost [(2:52:00)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=10320s).

**Z pohledu kamery.** Třes podél lokální osy X skoro zmizí, když se na postavu díváš ve směru té osy [(2:48:02)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=10082s). Vezme se proto right vektor kamery z Player Camera Manageru a převede se přes `Inverse Transform Direction` do lokálního prostoru postavy [(2:48:48)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=10128s). Když se mu vynuluje Z, postava se třese vždy doleva a doprava na obrazovce, ať se díváš odkudkoli [(2:49:35)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=10175s), [(2:50:24)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=10224s).

**Kdo se třese víc.** Zasažený má rychlost 30 a amplitudu 20, útočník rychlost 30 a amplitudu 1. Podle Sakuraie má víc kmitat ten, kdo ránu dostal, aby bylo vidět, koho zasáhla [(2:52:46)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=10366s), [(2:53:32)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=10412s). Otřes má navíc začít silně a ke konci slábnout. Postará se o to křivka z 1 na 0,2 s plynulým náběhem i doběhem [(2:54:19)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=10459s), [(2:55:05)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=10505s). Čte se podle uplynulého času hit stopu děleného jeho délkou, tedy normalizovaně od 0 do 1 [(2:56:40)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=10600s), [(2:57:28)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=10648s).

> **Pozn.:** Délky jsou tu výrazně delší, než doporučuje [godotová případovka](../godot/pripadovka-nepratele.md#combo-a-hit-stop-dva-casovace-a-ctvrt-sekundy): ta pro běžný sek dává pásmo 1/20–1/10 s a delší hit stop nechává silným úderům. Evans nastavuje čtvrt a půl sekundy. Sám ale navrhuje dát parametry hit stopu do structu útoku a škálovat je podle síly úderu [(2:57:28)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=10648s), [(2:58:14)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=10694s), a tím se obě rady potkají. Kdo hit stop prodlouží, měl by myslet i na [input buffering](../rejstrik.md#input-buffering), jinak zmražená postava polyká vstupy. Převod směru kamery do prostoru postavy je tatáž operace jako [převod cíle ruky do prostoru meshe](interakcni-animace.md#ruka-na-klice-ik-v-control-rigu-prevod-prostoru-a-alfa-z-krivky).

**Souvislosti:** [Rejstřík: Hit stop](../rejstrik.md#hit-stop) · [Rejstřík: Custom Time Dilation](../rejstrik.md#custom-time-dilation) · [Rejstřík: Player Camera Manager](../rejstrik.md#player-camera-manager) · [Celeste: křivky v snímcích](../teorie/game-feel.md#celeste-krivky-v-snimcich-a-hrst-tichych-ulev) *(čtyřsnímková pauza u dashe jako tatáž technika)*

---

## Rána, které hráč uvěří: pět potvrzení, každé o něčem jiném

**Zdroj:** [5 Ways to Improve Game Feel In Unreal Engine](https://www.youtube.com/watch?v=78MBe46IBrQ) · [Unreal University](https://www.youtube.com/channel/UCQv4mwerZLQVe3wPbsMc-qw) · ~9 min, přehled technik ·
[How to Make a Combat System in UE5](https://www.youtube.com/watch?v=4omEu9N9WIE) · [Evans Bohl](https://www.youtube.com/channel/UC36uolRnnwoMMH27vzecLBg) · ~3 h 49 min, tutoriál (úsek o camera shake)

**Shrnutí:** Podle Unreal University dělí amatérsky a hotově působící hru obvykle pět drobností: stopa zbraně, reakce nepřítele, zvuk, otřes kamery a ukazatel zdraví [(0:02)](https://www.youtube.com/watch?v=78MBe46IBrQ&t=2s). Žádná z nich nemění damage. Každá hráči **potvrzuje něco jiného**: kudy rána šla, že měla sílu, že dopadla, že je hráč u toho a jak boj stojí. Háček: vrstvy se nezastupují. Video je přidává jednu po druhé a s každou ukazuje, že i když ostatní fungují, pořád „něco chybí".

### Rozpad myšlenky

**Stopa: kudy rána šla.** Švih bez stopy je pro oko skoro neviditelný. Animace hraje a zásah se započte, ale nic neříká, že se stalo něco rychlého a nebezpečného [(0:02)](https://www.youtube.com/watch?v=78MBe46IBrQ&t=2s). Řešením je Niagara ribbon na zbrani, viditelný jen během švihu [(0:48)](https://www.youtube.com/watch?v=78MBe46IBrQ&t=48s). Autor to vysvětluje tak, že oko potřebuje vidět dráhu pohybu, ne jen jeho začátek a konec, a z dráhy pozná, kde je nebezpečí.

**Reakce nepřítele: že rána měla sílu.** Nepřítel, který zásah spolkne jako pytel písku, bere hráči pocit síly [(1:35)](https://www.youtube.com/watch?v=78MBe46IBrQ&t=95s). Záblesk říká „něco se stalo", [knockback](../rejstrik.md#knockback) „mělo to sílu" a částice v místě zásahu to podtrhnou [(2:21)](https://www.youtube.com/watch?v=78MBe46IBrQ&t=141s). Autor dělá záblesk tak, že materiál vymění za červený a po pár sekundách vrátí [(3:07)](https://www.youtube.com/watch?v=78MBe46IBrQ&t=187s). Evans totéž řeší overlay materiálem, který svítí jen po dobu hit stopu (viz [další myšlenka](#zablesk-a-kapow-efekt-musi-sedet-na-tele-i-mezi-tely)).

**Zvuk: že rána dopadla.** Bez zvuku je to jako akční film se staženou hlasitostí [(3:07)](https://www.youtube.com/watch?v=78MBe46IBrQ&t=187s). Stačí dva zvuky: švih vzduchem ohlásí, že něco přichází, dopad potvrdí, že to trefilo. Sound Cue s uzlem Modulator zajistí, že každé přehrání zní trochu jinak [(3:53)](https://www.youtube.com/watch?v=78MBe46IBrQ&t=233s).

**Kamera: že je hráč u toho.** Nehybná kamera dělá z hráče diváka za oknem; drobný otřes při dopadu ho vtáhne dovnitř [(4:39)](https://www.youtube.com/watch?v=78MBe46IBrQ&t=279s), [(5:25)](https://www.youtube.com/watch?v=78MBe46IBrQ&t=325s). Evans k tomu dává konkrétní nastavení [(2:58:54)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=10734s), [(2:59:42)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=10782s):
- Camera Shake Base s patternem Perlin noise,
- amplituda 20 a frekvence 20 za sekundu,
- trvání 0,2 s, blend in 0 a blend out 0,1 s,
- spouští se z Player Camera Manageru spolu s hit stopem.

Sám přiznává, že efekt je jemný [(3:00:30)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=10830s).

**Ukazatel: jak boj stojí.** Bez ukazatele hráč neví, jestli ubírá 10, nebo 100, ani jestli je nepřítel skoro mrtvý, a souboj pak působí náhodně [(6:12)](https://www.youtube.com/watch?v=78MBe46IBrQ&t=372s). Health bar nad nepřítelem je skóre každé rány. Druhý, bílý pruh klesá pomaleji, takže je vidět, kolik ubrala poslední rána [(6:59)](https://www.youtube.com/watch?v=78MBe46IBrQ&t=419s), [(7:46)](https://www.youtube.com/watch?v=78MBe46IBrQ&t=466s). Jak takový ukazatel postavit, popisuje [UI ve světě](ui-ve-svete.md#health-bar-nad-hlavou-screen-space-ukazatel-z-materialu-a-dojezd-poskozeni).

> **Pozn.:** Video je zčásti reklama na autorův placený program a cvičný projekt [(0:02)](https://www.youtube.com/watch?v=78MBe46IBrQ&t=2s), [(7:46)](https://www.youtube.com/watch?v=78MBe46IBrQ&t=466s). V popisu navíc přiznává, že vychází z cizího tweetu s ukázkou v Unity. Techniky jsou ale obecné a s [katalogem juice](../teorie/game-feel.md#katalog-juice-deset-detailu-ktere-prodavaji-tutez-mechaniku) se překrývají. Z katalogu stojí za převzetí výhrada, kterou tu nikdo neříká: otřes kamery umí způsobit nevolnost, a proto patří do nastavení jako vypínatelná volba. Zvukové půlce se věnuje [sound design ve hře](../hudba/sound-design-ve-hre.md#tri-ukoly-herniho-zvuku).

**Souvislosti:** [Rejstřík: Juice](../rejstrik.md#juice) · [Rejstřík: Camera shake](../rejstrik.md#camera-shake) · [Rejstřík: Random pitch variation](../rejstrik.md#random-pitch-variation) · [Mechaniky fungují jen tehdy, když je hráč vidí](../teorie/vizualni-komunikace.md#mechaniky-funguji-jen-tehdy-kdyz-je-hrac-vidi) *(tytéž signály jako podmínka čitelnosti)*

---

## Záblesk a kapow: efekt musí sedět na těle i mezi těly

**Zdroj:** [How to Make a Combat System in UE5](https://www.youtube.com/watch?v=4omEu9N9WIE) · [Evans Bohl](https://www.youtube.com/channel/UC36uolRnnwoMMH27vzecLBg) · ~3 h 49 min, tutoriál (UE 5.7)

**Shrnutí:** Poslední dvě vrstvy Evansova juice jsou materiálové. **Záblesk** je overlay materiál, který jde položit přes jakýkoli materiál postavy. **Komiksové „kapow"** je Niagara sprite v místě zásahu. Obě narazí na totéž: efekt se kreslí jinde, než je tělo. Overlay nevidí deformaci, kterou materiál pod ním dělá přes WPO, a sprite se schová do těla. Řešením je nafouknutí podél normál a custom stencil s porovnáním hloubek.

### Rozpad myšlenky

**Záblesk přes overlay materiál.** Materiál v režimu Additive a Unlit, bez stínů, s emisivní bílou [(3:01:16)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=10876s), [(3:02:03)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=10923s). Do slotu Overlay Material na meshi se položí přes jakýkoli základní materiál. Dřív se kvůli tomu musel měnit materiál postavy [(3:02:51)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=10971s).

**Past s WPO.** Na Rampageovi overlay některá místa nepokryje. Jeho materiál totiž tvar meshe posouvá přes World Position Offset a overlay o tom neví, takže se kreslí na nedeformovaný tvar [(3:02:51)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=10971s), [(3:03:38)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=11018s). Evans overlay nafoukne: `VertexNormalWS` × parametr (2) zapojí do jeho vlastního WPO. Velká hodnota pokryje všechno, ale postava pak vypadá jako maskot Michelinu, a autor přiznává, že to není dokonalé [(3:04:25)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=11065s).

**Obrys a blikání.** Fresnel zapojený do emise rozsvítí jen obrys. Power a násobič ladí kontrast a intenzitu, barevný parametr barvu [(3:05:13)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=11113s), [(3:06:01)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=11161s). Blikání vznikne řetězem: čas × rychlost → sinus → ×0,5 + 0,5 → `Round`. Výsledek je čisté zapnuto, nebo vypnuto, a jde do opacity [(3:07:39)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=11259s), [(3:08:41)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=11321s). Za běhu se vytvoří dynamic material instance s rychlostí 20 [(3:11:01)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=11461s). Overlay se nastaví na začátku hit stopu a smaže na jeho konci, a bliká jen zasažený [(3:11:47)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=11507s), [(3:12:34)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=11554s), [(3:13:23)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=11603s).

**Kapow ze spritu.** Inspirací je komiksová bojovka Comix Zone ze Sega Genesis, obrázek je zdarma stažené PNG [(3:14:11)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=11651s). Materiál je Translucent a Unlit a textura se násobí uzlem Particle Color, takže ji půjde tónovat z Niagary [(3:15:00)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=11700s). Barvu a alfu rozdělí nový uzel Convert z 5.7 [(3:15:47)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=11747s). Niagara systém vznikne ze šablony Simple Sprite Burst [(3:17:20)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=11840s):
- sprite natočený ke kameře [(3:18:52)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=11932s),
- náhodná velikost 200–250 a rotace ±45° [(3:19:38)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=11978s), [(3:20:25)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=12025s),
- Scale Sprite Size s ease-in křivkou ho prudce nafoukne [(3:21:12)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=12072s),
- život 0,3 s a průhlednost, která klesá až ke konci [(3:21:59)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=12119s), [(3:22:48)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=12168s),
- GPU simulace, která chce pevné bounds [(3:23:34)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=12214s).

Systém se spawnuje v impact pointu zásahu [(3:24:20)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=12260s).

**Kapow mezi těly.** Sprite v místě zásahu se občas zařízne do těl postav [(3:25:07)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=12307s). `Disable Depth Test` ho vytáhne nad všechno, i nad hráče [(3:25:54)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=12354s). Evans chce efekt nad zasaženým, ale pod útočníkem, a staví to na custom depth stencilu [(3:26:40)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=12400s):
1. V Project Settings se Custom Depth-Stencil Pass přepne na Enabled with Stencil.
2. Útočník kreslí do custom depth se stencilovou hodnotou 1. Nastaví se to z kódu v BeginPlay bojové komponenty [(3:28:12)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=12492s), [(3:29:49)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=12589s).
3. V materiálu spritu jde `SceneTexture: CustomStencil` přes saturate a 1 − x do násobení s alfou. Kde je útočník, sprite zmizí [(3:31:22)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=12682s), [(3:32:56)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=12776s), [(3:33:43)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=12823s).

Jenže když zasažený stojí mezi útočníkem a kamerou, sprite se vykrojí do útočníkova tvaru, i když je útočník schovaný [(3:33:43)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=12823s). Druhá podmínka proto porovná custom depth se scene depth. Útočník musí být ve stencilu **a zároveň opravdu vidět**, teprve pak se sprite vykrojí [(3:35:57)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=12957s), [(3:36:44)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=13004s), [(3:38:19)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=13099s).

> **Pozn.:** Custom depth není zadarmo. Při [profilování cizí hry](gpu-pruchod.md#profilovat-cizi-hru-priprava-ktera-rozhoduje) se v jeho průchodu našla Nanite programmable rasterization, která tam zbyla po obrysovém shaderu. Kdo ho zapne kvůli jednomu efektu, ať ho po čase zkontroluje v profileru. Kapow se navíc spawnuje jako nový systém při každém zásahu; jak spawnování systémů omezit, popisují [dvě cesty v Niagaře](niagara-vykon.md#dve-cesty-jak-prestat-spawnovat-systemy). A k blikání: Evans v náhledu nechává pomalou rychlost, prý aby na YouTube nikomu nezpůsobil záchvat [(3:10:15)](https://www.youtube.com/watch?v=4omEu9N9WIE&t=11415s). Rychlé blikání je opravdu otázka přístupnosti, i když tady trvá jen po dobu hit stopu.

**Souvislosti:** [Rejstřík: Overlay material](../rejstrik.md#overlay-material) · [Rejstřík: Hit flash](../rejstrik.md#hit-flash) · [Rejstřík: WPO](../rejstrik.md#wpo) · [Rejstřík: Fresnel](../rejstrik.md#fresnel) · [Rejstřík: Custom Depth](../rejstrik.md#custom-depth) · [Rejstřík: Dynamic Material Instance](../rejstrik.md#dynamic-material-instance)

---

## Zdraví po končetinách: physical material jako adresa, struct jako stav

**Zdroj:** [Limb Health + Breakable Limbs in Unreal Engine 5](https://www.youtube.com/watch?v=Mv1LGtQRVls) · [Tank Control Games](https://www.youtube.com/channel/UCoHLpKMSi5LlOMFlxuoR1rA) · ~22 min, tutoriál (UE 5.7)

**Shrnutí:** Každá končetina nepřítele má vlastní zdraví a vlastní ukazatel. Když klesne na nulu, buď se „zlomí", takže od kotevní kosti dolů začne simulovat fyziku, nebo se zničí: zmizí celý řetěz kostí a přehraje se efekt a zvuk. Adresou končetiny je **physical material** na tělech physics assetu, který už v projektu je, a jejím stavem jeden struct. Háček: funkce, která struct upravuje, ho musí brát **referencí**, jinak upraví kopii a změnu zahodí.

### Rozpad myšlenky

**Adresa zdarma.** Physics asset z autorova předchozího dílu už má physical materials po skupinách: rameno, předloktí a ruka sdílejí `PM_L_Arm`, páteř `PM_Torso` [(1:33)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=93s). Jméno physical materialu z hit resultu (`Get Display Name`) se přes `Switch on String` v Pure function převede na Enum `E_HitLimb` s hlavou, rukama, nohama a trupem [(2:19)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=139s), [(7:46)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=466s), [(8:33)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=513s). Zbraň pak na nepříteli zavolá `HandleHitLimb` s výsledkem [(9:21)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=561s).

**Stav v structu.** `S_Limb` nese max a aktuální zdraví, příznak zlomení, kost pro ukazatel, **kotevní kost fyziky** a volbu „zničit místo zlomit" [(2:19)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=139s), [(3:08)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=188s). Nepřítel má jeden struct na každou končetinu a `Select` podle enumu vybere ten správný [(10:07)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=607s). Kotvy a ukazatele jsou rozdělené takto [(10:54)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=654s), [(11:40)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=700s), [(12:26)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=746s):
- hlava: kotva `neck_01`, takže simuluje všechno pod krkem; ukazatel na hlavě,
- ruka: kotva klíční kost, ukazatel na předloktí,
- noha: kotva stehno, ukazatel na lýtku,
- trup: kotva `spine_01`, ukazatel na `spine_05`.

**Reference, ne kopie.** Vstup `DamageLimb` typu `S_Limb` musí mít zaškrtnuté Pass-by-Reference [(12:26)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=746s), [(13:12)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=792s). Bez toho funkce dostane kopii, kterou na konci zahodí, a změny by se do končetiny nepropsaly. Hodnoty se pak mění přes `Set Members in S_Limb` [(15:32)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=932s), [(16:20)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=980s).

**Zlomit, nebo zničit.** Zlomená končetina se už dál nezraňuje [(13:12)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=792s). Při nule jsou dvě cesty:
- zlomení: `Set All Bodies Below Simulate Physics` od kotevní kosti a zvuk zlomení. Autor zahrne i kotvu samotnou, aby končetina víc plandala [(17:07)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=1027s), [(17:53)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=1073s);
- zničení: efekt připojený ke kosti, `Hide Bone by Name`, který skryje celý řetěz pod kostí, a zvuk [(19:27)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=1167s), [(20:15)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=1215s).

Volí se zvlášť pro každou končetinu, takže hlava může explodovat a ruce se jen zlomit [(21:01)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=1261s). Autor sám dodává, co by hra chtěla navíc: s prostřelenýma nohama by nepřítel měl upadnout [(18:39)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=1119s).

**Drobnost s fyzikou.** Impulz při zásahu jde až o snímek později (`Delay Until Next Tick`) a jen na kost, která už simuluje. Ve stejném snímku, ve kterém se fyzika zapíná, by se nemusel projevit. Jiskry a zvuk zásahu hrají vždy [(0:47)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=47s).

> **Pozn.:** Physical materials se v knihovně objevují hlavně jako [povrchy pod nohama](footsteps.md#physical-materials-a-trace-misto-notify). Tady jde o tentýž mechanismus v jiné roli: materiál neříká „po čem šlapeš", ale „kam jsi trefil". Video navazuje na autorův díl o impulzu a ragdollu, který v knihovně není, a krvavý efekt pochází z placeného balíku [(20:15)](https://www.youtube.com/watch?v=Mv1LGtQRVls&t=1215s). Plnou ragdoll smyčku najdeš v [Ragdollu](ragdoll.md#active-ragdoll-motory-rizene-rychlosti), ukazatel, který skáče na zasaženou končetinu, v [UI ve světě](ui-ve-svete.md#health-bar-nad-hlavou-screen-space-ukazatel-z-materialu-a-dojezd-poskozeni).

**Souvislosti:** [Rejstřík: Physical Material](../rejstrik.md#physical-material) · [Rejstřík: Pass by reference](../rejstrik.md#pass-by-reference) · [Rejstřík: Physics Asset](../rejstrik.md#physics-asset) · [Rejstřík: Enum](../rejstrik.md#enum) · [Rejstřík: Struct](../rejstrik.md#struct)
