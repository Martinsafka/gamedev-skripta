# AI vnímání: jak si tě nepřítel všimne

Detekce hráče je pro stealth hru gameplay sám o sobě — kdy si mě stráž všimne, jak dlouho mě pronásleduje a kdy to vzdá, to jsou čísla, která rozhodují o napětí. Kapitola srovnává tři detekční nástroje enginu a pak jde do hloubky u dvou hlavních: Pawn Sensing (jednoduchý, vizuální) a AI Perception (mocnější, s háčky). Základní kostru nepřítele předpokládá ze [základů AI](ai-zaklady.md).

---

## Tři nástroje detekce: Pawn Sensing, AI Perception, trigger

**Zdroj:** [Create Smarter AI With These 3 Easy Detection Methods in Unreal Engine 5](https://www.youtube.com/watch?v=XgOEkcnJT0M) · [Gorka Games](https://www.youtube.com/channel/UCv_n9oioNF6OpzR2dt6E4xg) · ~9 min, srovnání

**Shrnutí:** Tři cesty, jak dát AI smysly, seřazené podle složitosti: **Pawn Sensing** (komponenta s gizmy ve viewportu, event a hotovo), **AI Perception** (víc smyslů a parametrů, ale bez vizualizace a s povinným protikusem na cíli) a **kolizní trigger** (overlap sféra — primitivní, ale pro „všimni si hráče v okruhu" stačí).

### Rozpad myšlenky

**Pawn Sensing** [(1:35)](https://www.youtube.com/watch?v=XgOEkcnJT0M&t=95s): přidáš komponentu, ve viewportu hned vidíš kužel zraku i rádius sluchu, nastavíš `Sight Radius` a `Peripheral Vision Angle` a napojíš `On See Pawn` [(2:22)](https://www.youtube.com/watch?v=XgOEkcnJT0M&t=142s). Autorova volba pro většinu případů: přímočará, vidíš co ladíš [(3:08)](https://www.youtube.com/watch?v=XgOEkcnJT0M&t=188s).

**AI Perception** [(3:56)](https://www.youtube.com/watch?v=XgOEkcnJT0M&t=236s): pole smyslů (sight, hearing, damage…), každý s vlastní konfigurací, k tomu stárnutí vjemů a síla stimulu. Dvě věci, na kterých se každý zasekne: cíl **musí mít komponentu `AI Perception Stimuli Source`** (auto register + zvolený smysl), jinak pro percepci neexistuje [(5:30)](https://www.youtube.com/watch?v=XgOEkcnJT0M&t=330s); a v configu smyslu je nutné zaškrtnout **Detect Enemies/Neutrals/Friendlies** — bez toho detekce mlčí (afiliace se bez C++ nedají nastavit jinak) [(6:16)](https://www.youtube.com/watch?v=XgOEkcnJT0M&t=376s). Nevýhoda proti Pawn Sensingu: ve viewportu není vidět nic [(4:42)](https://www.youtube.com/watch?v=XgOEkcnJT0M&t=282s).

**Trigger** [(7:02)](https://www.youtube.com/watch?v=XgOEkcnJT0M&t=422s): sphere collision s overlap presetem + `On Component Begin/End Overlap`. Žádný výhled, žádné překážky — čistě „jsi blízko". Pro pasti, zóny agrese nebo levné ambientní reakce ideální [(7:48)](https://www.youtube.com/watch?v=XgOEkcnJT0M&t=468s).

> **Pozn.:** Praktické pravidlo z videa: začni s Pawn Sensingem a přejdi na AI Perception, až budeš potřebovat víc smyslů nebo jemnější kontrolu [(8:34)](https://www.youtube.com/watch?v=XgOEkcnJT0M&t=514s) — přesně to dělá [State Trees kapitola](state-trees.md#jedna-percepce-tri-smysly-a-report-eventy), kde jedna perception obsluhuje zrak, sluch i damage. Trigger nezavrhuj: kombinace „trigger zóna + teprve pak drahá percepce" je legitimní optimalizace.

**Souvislosti:** [Základy AI](ai-zaklady.md) · [State Trees: smysly](state-trees.md#jedna-percepce-tri-smysly-a-report-eventy) · [Matematika pro gamedev: dot product](../teorie/matematika-pro-gamedev.md#vektory-a-dot-product-poloha-pohyb-a-zorne-pole) *(zorné pole je cos-práh nad dot productem)* · [Rejstřík: Pawn Sensing](../rejstrik.md#pawn-sensing) · [Rejstřík: AI Perception](../rejstrik.md#ai-perception) · [Rejstřík: trigger volume](../rejstrik.md#trigger-volume)

---

## Pawn Sensing v praxi: kužel, zdi a přesný timing ztráty

**Zdroj:** [AI Sight Detection And Chase - Unreal Engine 5 Tutorial](https://www.youtube.com/watch?v=tKrBdxm4uxI) · [Matt Aspland](https://www.youtube.com/channel/UC8_RNwftEO4isrX2LJowcpg) · ~8 min, tutoriál

**Shrnutí:** Doplněk předchozí myšlenky o tři praktické detaily: kužel zraku si **zobraz přímo v levelu** (vybraná AI ukazuje úhel i dosah ve světě), Pawn Sensing **nevidí přes zdi** (stačí, aby překážka měla kolizi), a ztráta zájmu má přesnou matematiku: **Retriggerable Delay musí být delší než sensing interval**.

### Rozpad myšlenky

**Ladění v kontextu:** místo odhadování čísel v blueprintu polož AI do levelu, nech ji vybranou a uprav `Peripheral Vision Angle` a `Sight Radius` s kuželem před očima [(2:21)](https://www.youtube.com/watch?v=tKrBdxm4uxI&t=141s). Object permanence je zadarmo: zeď s kolizí = AI tě nevidí [(2:21)](https://www.youtube.com/watch?v=tKrBdxm4uxI&t=141s).

**Mechanika ztráty zájmu** [(3:55)](https://www.youtube.com/watch?v=tKrBdxm4uxI&t=235s): `On See Pawn` pálí každý sensing interval (default 0,5 s), dokud tě AI vidí. Druhá větev sequence vede do **Retriggerable Delay**, který se každým výstřelem restartuje — doběhne teprve, když spatření ustane. Proto **duration ≥ 0,6 s**: kratší než interval by doběhla i mezi dvěma spatřeními a AI by „zapomínala", zatímco se dívá. Po doběhnutí: stop movement / návrat k patrole [(4:42)](https://www.youtube.com/watch?v=tKrBdxm4uxI&t=282s). Herní hodnoty bývají 5–10 s, ať zahnutí za roh neznamená okamžitý konec honičky [(4:42)](https://www.youtube.com/watch?v=tKrBdxm4uxI&t=282s).

**Chase samotný** je jeden uzel: `AI MoveTo` s target actorem = spatřený pawn — destinace se sleduje průběžně [(3:09)](https://www.youtube.com/watch?v=tKrBdxm4uxI&t=189s).

> **Pozn.:** Délka retriggerable delay je designová páka, ne technický detail: krátká = „goldfish" stráže vhodné pro komedii, dlouhá = neodbytní pronásledovatelé pro horor. Pro stealth se vyplatí k tomu přidat i vizuální komunikaci stavu (viz [vedení hráče](../teorie/vedeni-hrace.md)) — hráč musí poznat, že už je čistý vzduch.

**Souvislosti:** [Základy AI: chase a ztráta zájmu](ai-zaklady.md#chase-a-ztrata-zajmu-do-once-a-retriggerable-delay) · [Rejstřík: Retriggerable Delay](../rejstrik.md#retriggerable-delay) · [Rejstřík: Pawn Sensing](../rejstrik.md#pawn-sensing)

---

## AI Perception na controlleru: lose sight radius a Blackboard bool

**Zdroj:** [Terrifying AI Chase System in Unreal Engine 5](https://www.youtube.com/watch?v=GMYfVNftR-U) · [Ugur Batur GameDev](https://www.youtube.com/channel/UC4Sx-iR0_fK37T5nPAVy3uw) · ~7 min, tutoriál (navazuje na autorovu patrol část)

**Shrnutí:** AI Perception patří koncepčně na **AI Controller** (mozek vnímá, tělo se hýbe) — a sight config tam nabízí detail, který Pawn Sensing nemá: **Lose Sight Radius**, tedy větší rádius pro *ztrácení* cíle než pro jeho *získání*. Vnímání se do Behavior Tree propisuje přes Blackboard bool a dvě sekvence s decoratory.

### Rozpad myšlenky

**Config** [(0:21)](https://www.youtube.com/watch?v=GMYfVNftR-U&t=21s): AI Perception na controlleru, sight sense + `Dominant Sense = Sight`. `Sight Radius` určuje, kdy tě AI **uvidí**; `Lose Sight Radius` (větší), kdy tě **přestane vidět** [(1:09)](https://www.youtube.com/watch?v=GMYfVNftR-U&t=69s) — hystereze proti blikání stavu na hraně dosahu: jednou spatřený hráč se drží dál, než byl spatřen.

**Propojení s BT:** `On Target Perception Updated` → `Set Blackboard Value as Bool` na klíč „can see us" (pozor: key name přes `Make Literal Name` musí sedět **do písmene**) [(2:22)](https://www.youtube.com/watch?v=GMYfVNftR-U&t=142s). Strom: selector se dvěma sekvencemi — patrol s decoratorem *Is Not Set*, chase s *Is Set*, obě s **Observer aborts: Both**, ať změna boolu okamžitě přepne větev [(3:10)](https://www.youtube.com/watch?v=GMYfVNftR-U&t=190s). Chase task: `Receive Execute AI` → pozice hráče → Set Blackboard vector → **Simple Move to Location** → finish [(3:50)](https://www.youtube.com/watch?v=GMYfVNftR-U&t=230s). Ztráta: `Break AIStimulus` → `Successfully Sensed` false → bool false → patrola sama naskočí [(5:33)](https://www.youtube.com/watch?v=GMYfVNftR-U&t=333s).

> **Pozn.:** Umístění percepce (controller vs. postava — [LeafBranchGames](ai-zaklady.md#vyssi-liga-ai-controller-behavior-tree-a-blackboard) ji dává na postavu) je věc konvence; controller je čistší pro znovupoužití mozku napříč těly a odpovídá tomu, jak to dělá [GASP s NPC](gasp.md#npc-pres-state-tree-a-smart-objects-mozek-na-serveru-motor-v-komponente). Simple Move to Location je jednodušší příbuzný AI MoveTo — bez acceptance radius a callbacků; pro „doběhni na místo" stačí.

**Souvislosti:** [Základy AI: vyšší liga](ai-zaklady.md#vyssi-liga-ai-controller-behavior-tree-a-blackboard) · [GASP: NPC](gasp.md#npc-pres-state-tree-a-smart-objects-mozek-na-serveru-motor-v-komponente) · [Objektový klíč a odklad ztráty cíle](#objektovy-klic-a-odklad-ztraty-cile-percepce-navazana-na-strom) · [Rejstřík: AI Perception](../rejstrik.md#ai-perception) · [Rejstřík: Blackboard](../rejstrik.md#blackboard)

---

## Objektový klíč a odklad ztráty cíle: percepce navázaná na strom

**Zdroj:** [UE5 AI Sight Detection & Chasing With Behaviour Trees!](https://www.youtube.com/watch?v=JF5hIBcycPc) · [Matt Aspland](https://www.youtube.com/channel/UC8_RNwftEO4isrX2LJowcpg) · ~15 min, tutoriál

**Shrnutí:** Tatáž úloha jako výše — nepřítel bloumá, uvidí hráče, pronásleduje — ale se dvěma rozhodnutími, která stojí za převzetí. Blackboard nedrží **bool** „vidím", nýbrž **objektový klíč `Target`**, takže „koho honit" a „jestli honit" je jedna informace. A ztráta cíle je **odložená timerem**, takže nepřítel nepřestane pronásledovat v milisekundě, kdy mu hráč zmizí za rohem.

### Rozpad myšlenky

**Jeden klíč místo dvou** [(0:48)](https://www.youtube.com/watch?v=JF5hIBcycPc&t=48s): v blackboardu vznikne jediný klíč `Target` typu **Object** s base class nastavenou na Character. Tím zmizí klasická dvojice „bool vidím + objekt koho" a s ní i možnost, aby se rozešly. K tomu drobnost o pojmenování, která se vyplácí u pátého nepřítele: **kategorizuj podle chování, ne podle nepřítele** — `BB_Chase`, případně `BB_ChaseRandomRoam`, *„abys pak mohl mít jiný pro chase patrol"*.

**Dekorátor, který strom přeruší sám** [(2:20)](https://www.youtube.com/watch?v=JF5hIBcycPc&t=140s) je jádro celého návrhu. Struktura je root → **Selector** → větev „can see player" a větev „random roam". Na první visí **Blackboard dekorátor** hlídající klíč `Target`, a klíčové nastavení je **`Observer Aborts = Both`**: dekorátor pak **přeruší běžící větev v obou směrech** — objeví-li se cíl, ukončí bloumání; zmizí-li, ukončí pronásledování. Chování se tak nepřepíná v kódu, ale **vyplývá z toho, že se změnil jeden údaj v blackboardu**.

**Bloumání jako vlastní task** [(3:53)](https://www.youtube.com/watch?v=JF5hIBcycPc&t=233s): nový BT task přepíše `ReceiveExecuteAI` a udělá `AIMoveTo(ControlledPawn, GetRandomReachablePointInRadius(pozice pawna, 1000))` → na success `FinishExecute(success)`. Za ním v sekvenci `Wait` — *„jakmile AI dojde do náhodného bodu, počká sekundu (nebo kolik nastavíš), než to udělá znovu"*. Jednoduchý rytmus, který od bloumání odliší nervózní pobíhání.

**Percepce na pawnovi** [(6:59)](https://www.youtube.com/watch?v=JF5hIBcycPc&t=419s): komponenta AI Perception s `AI Sight Config` přímo na postavě. Dvě nastavení, na kterých to lidem nejčastěji tiše nefunguje: **v `Detection by Affiliation` zaškrtnout všechny tři** (enemies, neutrals, friendlies) a nastavit **`Dominant Sense = AI Sense Sight`**. Pak `OnTargetPerceptionUpdated` → split struktury `Stimulus` → bool `Successfully Sensed` rozhodne, jestli se klíč nastaví na `Actor`, nebo vyprázdní.

**Odklad ztráty cíle** [(10:06)](https://www.youtube.com/watch?v=JF5hIBcycPc&t=606s) je ta část, která z funkčního systému dělá slušný. Přímé vyprázdnění klíče při ztrátě zraku znamená, že nepřítel **okamžitě** ztratí zájem. Místo toho: na ztrátě se spustí `SetTimerByEvent(2 s)` a teprve jeho event klíč vyprázdní; při opětovném spatření se přes `IsValidTimerHandle` → `ClearAndInvalidateTimerByHandle` timer zruší a pronásledování plynule pokračuje. **Dvě sekundy tolerance jsou rozdíl mezi nepřítelem, který působí pozorně, a nepřítelem, který působí jako spínač.**

> **Pozn.:** Dva provozní detaily, které video zmíní mimochodem a stojí za zapamatování: **Pawn je optimalizovanější než Character** [(6:12)](https://www.youtube.com/watch?v=JF5hIBcycPc&t=372s), *„když jich budeš mít v levelu hodně"* — Character s sebou nese celý Character Movement; a bez **Nav Mesh Bounds Volume** v levelu nepůjde nic, přičemž klávesa **P** zobrazí zeleně, kudy AI smí [(13:14)](https://www.youtube.com/watch?v=JF5hIBcycPc&t=794s). Umístění percepce (tady na pawnovi, výše na controlleru) zůstává věcí konvence — viz Pozn. u předchozí myšlenky.

**Souvislosti:** [AI Perception na controlleru](#ai-perception-na-controlleru-lose-sight-radius-a-blackboard-bool) *(tatáž úloha s boolem místo objektu)* · [Základy AI: chase a ztráta zájmu](ai-zaklady.md#chase-a-ztrata-zajmu-do-once-a-retriggerable-delay) *(týž odklad postavený přes Retriggerable Delay)* · [Utility AI](ai-zaklady.md#utility-ai-rozhodovani-podle-skore-misto-vetveni) · [State Trees](state-trees.md#kostra-state-tree-ai-komponenta-tasky-a-kontext) · [Rejstřík: Behavior Tree](../rejstrik.md#behavior-tree) · [Rejstřík: Blackboard](../rejstrik.md#blackboard)
