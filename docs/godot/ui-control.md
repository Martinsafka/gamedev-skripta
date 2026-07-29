# Control nody a UI

UI je v Godotu oblast, na které se lidé zasekávají nejčastěji — a skoro vždycky proto, že si zvyknou uvažovat v pixelech a pozicích, zatímco engine chce uvažovat v **procentech a kontejnerech**. Kapitola vychází z jediného, ale hodně důkladného zdroje a je záměrně postavená jako výklad pojmů, ne jako návod krok za krokem: kotvy, kontejnery a témata jsou tři koncepty, ze kterých se skládá skoro každý layout.

Autor si o svém přístupu nedělá iluze a rovnou upozorňuje, že po prvním zhlédnutí to nedá smysl [(8:05)](https://www.youtube.com/watch?v=5Hog6a0EYa0&t=485s): *„nedělej si starosti, to se čeká — až si to sám vyzkoušíš, začne to intuitivně sedět."* Kapitola se čte stejně: jednou jako přehled, podruhé jako referenční tahák.

---

## Kotvy a offsety: layout, který přežije jiné rozlišení

**Zdroj:** [Godot Control Node (UI) Masterclass](https://www.youtube.com/watch?v=5Hog6a0EYa0) · [Karto](https://www.youtube.com/channel/UChQhbB_RSVtZ9aChSTJb62A) · ~27 min, výklad

**Shrnutí:** Health bar umístěný na střed obrazovky v pixelech přestane být na středu, jakmile ho někdo spustí v jiném rozlišení. **Kotva** je odpověď: čtyři čísla mezi 0 a 1, která říkají „kde v procentech rodiče tenhle prvek začíná a končí". K nim patří **offsety** v pixelech, měřené od kotvy. Háček, který mate úplně všechny: kotvy **nejsou relativní k oknu**, ale **k rodičovskému nodu** — s jedinou výjimkou kořene.

### Rozpad myšlenky

**Základ transformace** je nutné vzít nejdřív, protože Control node se chová jinak než sprite [(1:02)](https://www.youtube.com/watch?v=5Hog6a0EYa0&t=62s): **pozice je vždycky levý horní roh**, ne střed. **Size** říká, jak daleko je pravý dolní roh v pixelech — takže **zvětšení velikosti roste jen doprava a dolů**. A `scale` je násobič velikosti, který na rozdíl od size **respektuje pivot offset** [(1:49)](https://www.youtube.com/watch?v=5Hog6a0EYa0&t=109s): posuneš-li pivot do poloviny šířky, začne prvek při škálování růst na obě strany. Rotace se řídí týmž pivotem.

**Kotvy jako procenta** [(2:36)](https://www.youtube.com/watch?v=5Hog6a0EYa0&t=156s): představ si okno jako rozsah 0 až 1 od levého horního rohu. Kotva 0,5 je střed — a **zůstane středem i po změně rozlišení**, protože počet pixelů přestal hrát roli. Autorův příklad je učebnicový: health bar vycentrovaný pixely vypadá dobře u tebe a rozbije se u kamaráda s jiným poměrem stran. Kotva to řeší napevno.

**Offsety** jsou pixelové odchylky **od kotvy** [(4:58)](https://www.youtube.com/watch?v=5Hog6a0EYa0&t=298s), a tady je jedna nepříjemnost: **pravý a dolní offset musí být záporné**, chceš-li být uvnitř. Zajímavější je důsledek jejich kombinace s roztaženými kotvami: nastav kotvy přes celou šířku okna a offsety na 100 a −100, a prvek bude **vždycky 100 pixelů od obou okrajů**, jakkoli široké okno bude. To je způsob, jak udělat pruh, který se skutečně roztahuje — což pouhá kotva neumí.

**Presety** (ta „tlačítka jako ze Smash Bros") dělají dvě věci naráz [(6:32)](https://www.youtube.com/watch?v=5Hog6a0EYa0&t=392s): nastaví kotvy a **vynulují offsety**. Proto po kliknutí na *top left* prvek zmizí — kotvy jsou v jednom bodě a nulové offsety znamenají nulovou velikost. Autor přiznává i nekonzistenci, kterou nerozluštil: *„občas to vypadá, že se offsety na nulu nenastaví, a nepřišel jsem na to, co to způsobuje."* Jeho rada je dobrá — rozumíš-li kotvám a offsetům, je to jen drobná nepříjemnost, protože víš, co dodělat ručně.

**A teď to, co plete nejvíc** [(8:05)](https://www.youtube.com/watch?v=5Hog6a0EYa0&t=485s): **presety a kotvy jsou relativní k obdélníku rodiče**, ne k oknu. Kořenový node je výjimka jen proto, že rodiče nemá. Jakmile tedy vnoříš Control do Controlu, začnou kotvy pracovat uvnitř toho vnitřního prostoru — což je logické a přesto to překvapí každého, kdo si zvykl uvažovat v souřadnicích obrazovky.

> **Pozn.:** Za zmínku stojí drobnost, která šetří čas: **přepínač u kotvových tlačítek**, po kterém se při změně velikosti prvku **hýbou i kotvy** [(6:32)](https://www.youtube.com/watch?v=5Hog6a0EYa0&t=392s) — offsety pak zůstanou konstantní. Bez něj se při každém tažení myší přepisují offsety, což vypadá jako by editor „bojoval" proti tobě. A pořadí ve stromu tu funguje stejně jako všude jinde v Godotu: **níž ve stromu = výš vizuálně**, takže překryv se řeší přesunem v hierarchii nebo [Z indexem](../rejstrik.md#z-index).

**Souvislosti:** [Kontejnery: 90 % UI jsou čtyři nody](#kontejnery-90-ui-jsou-ctyri-nody) *(pozor — dítě kontejneru kotvy mít nemůže)* · [Nody a scény](zaklady.md#nody-a-sceny-strom-ktery-je-zaroven-architekturou) *(pořadí ve stromu a vykreslení)* · [Rejstřík: Anchor (UI)](../rejstrik.md#anchor-ui) · [Rejstřík: HUD](../rejstrik.md#hud)

---

## Kontejnery: 90 % UI jsou čtyři nody

**Zdroj:** [Godot Control Node (UI) Masterclass](https://www.youtube.com/watch?v=5Hog6a0EYa0) · [Karto](https://www.youtube.com/channel/UChQhbB_RSVtZ9aChSTJb62A) · ~27 min, výklad

**Shrnutí:** Kontejner je node, který **rozmisťuje své děti sám** — a proto s nimi nesmíš hýbat ty. To zní jako omezení a je to hlavní nástroj: **HBox, VBox, Margin a Panel container dělají devadesát procent všeho UI**, když se vnořují ve správném pořadí. Háček, bez kterého ti kontejnery nebudou fungovat: **custom minimum size** — protože dítě kontejneru, které nemá minimum, se smrskne na nulu.

### Rozpad myšlenky

**Co kontejner dělá a co ti bere** [(9:39)](https://www.youtube.com/watch?v=5Hog6a0EYa0&t=579s): rozmisťuje děti a **sám si nastavuje velikost podle nich**. Důsledek — přímé dítě kontejneru **nejde volně transformovat**, ty vlastnosti spravuje rodič. Autor to komentuje férově: *„zní to dost omezujícím dojmem, což upřímně tak trochu je"* — jenže naučit se v tom pohybovat je celá pointa.

**Čtyři kontejnery, které stačí** [(10:25)](https://www.youtube.com/watch?v=5Hog6a0EYa0&t=625s): **HBoxContainer** skládá děti vedle sebe v pořadí, v jakém jsou ve stromu · **VBoxContainer** totéž svisle · **MarginContainer** přidá odstup mezi svůj obrys a obsah · **PanelContainer** obalí děti a nakreslí za ně panel.

**Nejčastější past** je použít PanelContainer a divit se, proč nejdou děti uspořádat [(10:25)](https://www.youtube.com/watch?v=5Hog6a0EYa0&t=625s): panel jen **omezuje** děti do svých hranic, neuspořádává je. Správné vnoření je `PanelContainer → MarginContainer → VBoxContainer → obsah`, a **pořadí není libovolné**: VBox si nastaví velikost podle obsahu, margin přidá okraje kolem toho výsledku a panel se přizpůsobí velikosti marginu. Autorovo shrnutí je zároveň návod na jakýkoli layout [(11:11)](https://www.youtube.com/watch?v=5Hog6a0EYa0&t=671s): *„rozlož si layout na vodorovné a svislé sekce a přemýšlej o nich jako o těchhle kontejnerech."*

**Zarovnání místo kotev** [(11:58)](https://www.youtube.com/watch?v=5Hog6a0EYa0&t=718s): dítě kontejneru kotvy nemá, místo nich má **container sizing options**. Levá polovina voleb jsou **shrink** (smrskni na minimum a zarovnej k dané straně), pravá **fill** (zaber celý dostupný prostor v dané ose). A protože dítě nemá vlastní velikost, **shrink bez custom minimum znamená nulu** — proto je ta vlastnost tak důležitá.

**Expand versus fill** je rozdíl, na kterém se láme nejvíc lidí [(14:17)](https://www.youtube.com/watch?v=5Hog6a0EYa0&t=857s). `fill` roztáhne dítě na prostor, který **kontejner dítěti přidělil**; `expand` říká, že si dítě má vzít **zbývající volné místo kontejneru**. Máš-li dva panely ve VBoxu a chceš, aby jeden vyplnil zbytek, zapneš mu expand. Zapneš-li ho oběma, **perou se o zbytek rovným dílem** — a poměr se řídí **stretch ratio** (ratio 2 versus 1 znamená dvojnásobek). Autor přidává i to, co lidi mate: samotné přepnutí toho tlačítka nedělá nic, expand se nastavuje **spolu se zarovnáním**, a stretch ratio je bez zapnutého expandu **k ničemu**.

**A jedna vysloveně praktická pomoc** [(13:30)](https://www.youtube.com/watch?v=5Hog6a0EYa0&t=810s): `TextureRect` uvnitř kontejneru nejde normálně zvětšit. Trik je nastavit **expand mode na *ignore size*** (obrázek se smrskne) a pak mu dát **custom minimum**. Podobně u HBoxu platí, že **vodorovné zarovnání dítěte nastavit nejde** — to řídí kontejner; svislé ano.

> **Pozn.:** Kontejnerové myšlení je totéž, co dělá CSS flexbox, a kdo ho zná z webu, má náskok — včetně pastí. Rozdíl, který se vyplatí mít v hlavě: **v Godotu je „minimální velikost" hlavní páka, ne okrajová vlastnost.** Většina problémů typu „proč se mi to smrsklo na nic" má stejnou odpověď: prvek nemá vnitřní velikost, kterou by kontejner respektoval, a ty jsi mu žádnou nedal. Praktický postup, který z videa plyne: **napřed vnoř kontejnery, pak nastav minimální velikosti, teprve nakonec řeš vzhled.**

**Souvislosti:** [Kotvy a offsety](#kotvy-a-offsety-layout-ktery-prezije-jine-rozliseni) *(co platí mimo kontejnery)* · [Téma, override a style box](#tema-override-a-style-box-vzhled-oddeleny-od-rozlozeni) · [Vizuální hierarchie](../teorie/vizualni-komunikace.md) *(co má layout vlastně sdělit)* · [Rejstřík: UX](../rejstrik.md#ux) · [Rejstřík: Vizuální hierarchie](../rejstrik.md#vizualni-hierarchie)

---

## Téma, override a style box: vzhled oddělený od rozložení

**Zdroj:** [Godot Control Node (UI) Masterclass](https://www.youtube.com/watch?v=5Hog6a0EYa0) · [Karto](https://www.youtube.com/channel/UChQhbB_RSVtZ9aChSTJb62A) · ~27 min, výklad

**Shrnutí:** Rozložení řeší kontejnery, **vzhled řeší témata**. `Theme` je resource, který určuje, jak má vypadat celý *typ* nodu; **theme override** přepíše jednu vlastnost na jednom konkrétním nodu; a **style box** je resource popisující vzhled jedné oblasti (barva, okraj, zaoblení). Háček, který kousne každého: **style boxy jsou resources, takže se při duplikaci nodu sdílejí** — a změna barvy u jednoho změní barvu u obou.

### Rozpad myšlenky

**Tři úrovně, každá jinak široká** [(15:51)](https://www.youtube.com/watch?v=5Hog6a0EYa0&t=951s): **téma** platí na typ nodu v celém projektu (všechny labely, všechna tlačítka), **override** jen na ten jeden node. Z toho plyne rozumné rozdělení práce: co je pravidlo, patří do tématu; co je výjimka, do overridu.

**Zaškrtávátko u overridu není kosmetika** [(17:24)](https://www.youtube.com/watch?v=5Hog6a0EYa0&t=1044s), a je to jedna z těch věcí, které vyrábějí půlhodinové zmatky: **hodnota, kterou v overridu vidíš, není hodnota, která se používá**, dokud override nezapneš. Autorův příklad: VBoxContainer ukazuje separaci 0, a přesto mezi dětmi mezera je — protože se používá hodnota z tématu a override je vypnutý.

**Kde se schovávají věci, které bys čekal jinde** [(18:10)](https://www.youtube.com/watch?v=5Hog6a0EYa0&t=1090s): **okraje MarginContaineru se nastavují právě přes theme override**, ne přes běžnou vlastnost. Autorovo pravidlo je použitelné jako reflex: *„chceš-li změnit vzhled jakéhokoli Control nodu, podívej se nejdřív do jeho vlastností a hned potom do sekce theme overrides."*

**Style box** je resource pro vzhled jedné oblasti [(18:10)](https://www.youtube.com/watch?v=5Hog6a0EYa0&t=1090s). Nejběžnější je `StyleBoxFlat` — barva, okraj, zaoblené rohy — a poznáš, jestli ho node umí, podle sekce *Styles* v theme override. Užitečná dvojice, kterou autor ukazuje na progress baru [(22:07)](https://www.youtube.com/watch?v=5Hog6a0EYa0&t=1327s): pozadí dostane `StyleBoxEmpty` (zmizí) a výplň `StyleBoxFlat` s barvou a zaoblením — tím se z obecného prvku stane prvek tvojí hry.

**A ta past** [(18:56)](https://www.youtube.com/watch?v=5Hog6a0EYa0&t=1136s): duplikuješ panel se style boxem, změníš barvu — a změní se **oběma**. Protože *„style boxy jsou resources a duplikování nodu jen kopíruje odkaz na tentýž resource."* Řešení je pravý klik → **make unique**. Je to přesně tatáž past, jakou má [sdílený Resource obecně](resources.md#sdileny-ve-vychozim-stavu-past-jednoho-dina), jen se projeví v UI, kde je vidět dřív.

**Několik drobností z živé ukázky**, které mají lepší poměr užitku k délce než většina tutoriálů: **MSDF pro ostré písmo** [(20:33)](https://www.youtube.com/watch?v=5Hog6a0EYa0&t=1233s) — v nastavení projektu se zapne *multi-channel signed distance field* a rozmazané písmo se změní na ostré; autorův komentář *„nechápu, proč to není zapnuté defaultně"* sdílíme · **Tab** přeskočí na další vstupní pole, takže se čtyři poloměry rohů vyplní bez myši · **šipky nahoru/dolů** u číselného pole přičítají po jedné, se Shiftem po deseti, s Ctrl po stu, s Alt po desetinách · **Alt + pravý klik** vypíše všechny nody pod kurzorem, takže si vybereš ten správný místo věčného trefování · **zámek** u nodu zabrání, aby se do něj klikalo · **Ctrl + šipky** v stromu scény posouvají vybraný node mezi sourozenci.

> **Pozn.:** Za nejcennější kus téhle myšlenky považujeme něco, co ve videu zaznělo mimochodem [(21:20)](https://www.youtube.com/watch?v=5Hog6a0EYa0&t=1280s): dva labely sdílející **`LabelSettings` resource** se změní naráz, protože sdílejí týž soubor. To je tentýž mechanismus jako past se style boxem — jen tentokrát **využitý schválně**. Praktické pravidlo, které z toho plyne pro celé UI: **sdílení resourcu je nástroj, když je záměrné, a bug, když je náhodné** — a rozdíl je jen v tom, jestli sis to rozmyslel. Když tedy duplikuješ node se style boxem, polož si otázku „mají se ty dva měnit spolu?" dřív, než sáhneš po *make unique*.

**Souvislosti:** [Kontejnery](#kontejnery-90-ui-jsou-ctyri-nody) · [Sdílený ve výchozím stavu](resources.md#sdileny-ve-vychozim-stavu-past-jednoho-dina) *(táž past mimo UI)* · [Typografie](../teorie/typografie.md) *(co s tím ostrým písmem dělat dál)* · [Nastavení projektu](prvni-hra.md#nastaveni-projektu-je-soucast-hry-ne-administrativa) · [Rejstřík: Typografie](../rejstrik.md#typografie)
