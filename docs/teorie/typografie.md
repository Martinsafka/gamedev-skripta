# Typografie pro herní vývojáře

Písmo je jediný výtvarný prvek, který se ve hře nedá obejít: i hra bez jediného assetu má menu, čísla a texty. Přesto se řeší jako poslední — vybere se font, který „vypadá dobře", a řeší se až ve chvíli, kdy si někdo stěžuje, že to nejde přečíst. Indie Game Clinic tomu věnoval čtyřicetiminutový kurz a rozdělil ho do tří vrstev: **čitelnost** (jestli text vůbec funguje), **semiotika** (co písmo znamená, aniž bys to napsal) a **forma** (mezery a tvary písmen, které v herním enginu stejně neovlivníš).

---

## Pravidlo dvou fontů a vizuální jazyk textu

**Zdroj:** [Typography Basics Every Game Dev Should Know](https://www.youtube.com/watch?v=QuNNdPrVMm0) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · ~40 min, kurz

**Shrnutí:** Začni **dvěma fonty a jasným zadáním, k čemu který je** — jeden na nadpisy, druhý na běžný text. Není to estetické pravidlo, ale trénink pokročilejšího návyku: **každý nový řez, tučné písmo nebo kurzíva musí mít logický důvod a v celé hře znamenat vždycky totéž.** Nejlepší školou jsou sběratelské karetní hry, které tenhle systém dotáhly do detailu.

### Rozpad myšlenky

Proč zrovna dva [(2:25)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=145s): pravidlo samo o sobě není posvátné — dají se najít krásné výjimky — ale nutí tě přemýšlet správným směrem. **Když přidáváš nový textový styl, musí pro to existovat důvod** [(3:11)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=191s), a ten důvod má být čitelný i pro hráče. Herní příklady, kdy se odchylka vyplatí: **čísla poškození** vyskakující během souboje, **klíčová slova** v popisu předmětu (status „otrávený" tučně, protože označuje mechanický efekt) a **flavor text kurzívou**, aby hráč **jediným pohledem poznal, že tohle je příběh, ne informace nutná ke hraní** [(3:57)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=237s).

Tady je jádro celé myšlenky: pravidla nejsou o písmu, ale o **vizuálním jazyce**. Když kurzíva jednou znamená lore, musí to znamenat **v celé hře** — jinak hráč každý nový text luští znovu.

Nejlepší doklad jsou karetní hry, které stojí mezi tiskem a herním designem [(4:44)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=284s). V Hearthstone má název karty, velká čísla i typ bytosti tentýž tučný dekorativní **patkový** řez s obrysem, zatímco **text pravidel dole je čistě bezpatkový** — protože nese celou větu a musí se číst rychle [(5:31)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=331s). Magic: The Gathering dělá totéž a navíc vyhrazuje **kurzívu pro příběhový útržek nebo vtip** [(6:18)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=378s). Pointa, kterou video vytáhne nahlas: **dvě nejúspěšnější karetní hry historie nepoužívají spoustu písem — používají několik, ale s pravidly**, kdy je co tučně a kdy kurzívou.

Mimochodem, i tvar písma nese svou historii [(4:44)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=284s): **serify** — ty „nožičky" na koncích tahů — vznikly v době fyzického tisku, protože **bránily rozpíjení inkoustu a opotřebení stroje**. Proto s patkovým písmem podvědomě spojujeme starší dobu; a proto taky serify **čtenáře mírně zpomalují**, což je u dlouhých herních textů argument proti nim.

> **Pozn.:** Hranice pravidla je poctivě přiznaná [(29:33)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=1773s): **spousta různých řezů umí záměrně vytvořit dojem retro nebo bohémské změti** — jen to nedělej u textu, který má být snadno čitelný (dialogy, tutoriály), ale u materiálů, které existují **uvnitř světa hry**: cedule obchodů, plakáty, etikety. Tam je typografická změť realistická, protože v reálném světě taky vzniká.

**Souvislosti:** [Art specializace: UI jako ekosystém pravidel](art-specializace.md#ui-a-ux-ekosystem-pravidel-a-pet-cilu-pohybu) · [GDD: dokument, který chce někdo číst](gdd.md#will-should-could-jazyk-zavazku-a-dokument-ktery-chce-nekdo-cist) *(tatáž disciplína aplikovaná na dokumentaci)* · [Rejstřík: serif](../rejstrik.md#serif) · [Rejstřík: typografie](../rejstrik.md#typografie)

---

## Čtyři zločiny proti čitelnosti — a proč zhoršují i hraní

**Zdroj:** [Typography Basics Every Game Dev Should Know](https://www.youtube.com/watch?v=QuNNdPrVMm0) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · sekce o legibilitě

**Shrnutí:** Čtyři chyby dělají text ve hře těžko čitelným: **celé věty verzálkami**, zbytečně dekorativní řezy, **příliš velké skoky ve velikosti** a špatný kontrast. A nejde jen o pohodlí — psychologický výzkum ukazuje, že **špatně čitelná instrukce zhoršuje výkon v úkolu, který popisuje**. Nečitelný text tedy nezhoršuje jen dojem z hry, ale i to, jak dobře ji lidé hrají.

### Rozpad myšlenky

**Verzálky** jsou nejčastější prohřešek [(7:04)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=424s) a mají dva různé problémy. Ten měkčí: velká písmena čteme jako křik, protože jsme si tu konvenci vypěstovali na internetu. Ten tvrdší je mechanický [(7:50)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=470s): **verzálky mají všechny stejnou výšku, takže text tvoří rovný blok bez charakteristických tvarů slov** — a právě podle těch tvarů oko čte. Nejvíc to dopadá na **dyslektiky a lidi se zrakovým postižením**. Použitelné jsou proto jen na krátké věci: název předmětu, nadpis, zvýraznění jednoho slova — řádově do pěti slov. Na obvyklou obranu má video jednu z nejlepších vět celého kurzu [(7:50)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=470s): **„Nejhorší odpověď na tuhle výtku je ‚ale ten font má jen velká písmena.' Tak si vezmi jiný font."** Výjimku uznává u komiksového stylu, který je verzálkami psaný desítky let a jinak nepůsobí autenticky [(8:38)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=518s).

**Dekorativní řezy** [(8:38)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=518s) — s upřesněním, že řeč není o názvu hry na úvodní obrazovce, ale o textu, který čteš během hraní.

**Skoky ve velikosti** [(9:26)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=566s) jsou nejpodceňovanější položka. Drobný copyright na kartě je v pořádku, protože ho nikdy nepotřebuješ přečíst — ale stejný skok u **herně důležité informace** nutí oko přeostřovat. Autor to vídá i mimo hry [(10:13)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=613s): v prezentacích, kde po slidu se třemi velkými větami přijde slide plný drobného textu, vznikne **„moment ‚hm' v hlavě publika, po kterém je pravděpodobnější, že vypne"**.

**Špatný kontrast** [(10:13)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=613s) je ve hrách vyhrocený tím, že text často leží **přes pohyblivé pozadí**. Proto se používá obrys, vržený stín nebo **průhledná viněta pod textem** [(11:00)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=660s) — aby exploze za písmem nerozhodovala o tom, jestli si hráč přečte, co má dělat.

A pak přijde argument, který posouvá celou kapitolu z estetiky do funkčnosti [(11:47)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=707s). V knize Susan Weinschenk *100 Things Every Designer Needs to Know About People* popisuje experiment, ve kterém lidé dostali **instrukce k basketbalovým hodům vysázené různě čitelně** — a ti, kdo dostali hůř čitelnou verzi, **v samotném házení dopadli hůř** [(12:33)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=753s). Nečitelnost tedy nezhoršuje jen čtení, ale i **provedení toho, co je napsáno**. Autor z toho vyvozuje širší důsledek [(13:20)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=800s): špatně čitelný text nastavuje čtenáře do podrážděného rozpoložení, které se přenáší do všeho ostatního — „publikum krčí obličej, je nabručené, a to ovlivní, jak s tvým designem zachází".

> **Pozn.:** Tohle je zároveň nejlevnější přístupnostní opatření, jaké hra může mít: **volba fontu a velikosti nestojí nic a rozhoduje o tom, jestli hru zvládne hrát člověk s dyslexií.** Srovnej s [bariérami hraní](obtiznost.md#challenge-je-co-difficulty-je-kolik) — nečitelné písmo je učebnicová bariéra, kterou designér testovat nechtěl, a přesto se podle ní měří celá jeho obtížnost.

**Souvislosti:** [Obtížnost: bariéry hraní](obtiznost.md#challenge-je-co-difficulty-je-kolik) · [Vizuální komunikace: mechaniky musí být vidět](vizualni-komunikace.md#mechaniky-funguji-jen-tehdy-kdyz-je-hrac-vidi) · [První dojem](prvni-dojem.md#splash-prazdna-scena-a-menu-ktere-zije) · [Rejstřík: legibilita](../rejstrik.md#legibilita) · [Rejstřík: cognitive load](../rejstrik.md#cognitive-load)

---

## Semiotika písma: font řekne žánr dřív než první věta

**Zdroj:** [Typography Basics Every Game Dev Should Know](https://www.youtube.com/watch?v=QuNNdPrVMm0) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · sekce o semiotice

**Shrnutí:** Když se podíváš na písmo a řekneš „to je sci-fi" nebo „to je fantasy", čteš **sadu kulturních symbolů** — a ta se do písma dostala třemi cestami: z **materiálu a nástroje**, kterým vzniklo (dláto, brk, tiskový lis), z **historické epochy** a z **jiných médií**, hlavně filmu. Pro herního vývojáře to je levný nástroj: font sdělí dobu a tón scény dřív, než hráč přečte první slovo.

### Rozpad myšlenky

Semiotika je studium toho, **co symboly znamenají a proč** [(13:20)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=800s). Nejjednodušší vrstva je emoční [(14:06)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=846s): kulaté a zdobné tvary působí přátelsky, hranaté a strohé formálně — a z pouhé typografie proto uhodneš žánr i tón hry. Video to zkouší naslepo na dvou hrách a dodá: „kdybych ti je ukázal bez kontextu, poznal bys, ve které z nich se víc bojuje" [(14:52)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=892s).

Hlubší vrstva je **historická, a nese ji materiál** [(14:52)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=892s). Římské kapitálky mají rovné tahy, protože vznikaly **dlátem do kamene**; středověké lomené písmo je zdobné, protože ho psali **brkem** mniši v iluminovaných rukopisech [(15:38)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=938s); viktoriánské etikety jsou přehlídkou dekorativních řezů, protože si to tehdejší tisk mohl dovolit. Praktický důsledek pro vývojáře je varovný [(16:24)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=984s): **hra zasazená do takové éry znamená spoustu práce navíc** — každý plakát a cedule ve světě musí ten jazyk mluvit.

Třetí vrstva přichází **z jiných médií** [(16:24)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=984s): obal hry *It Came from the Desert* je vysázený jako **plakát béčkového filmu 50. let**; Ape Out staví grafiku i typografii na **filmových předtitulcích Saula Basse** ze 60. let a rýmuje ji s jazzem, který ve hře hraje [(17:12)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=1032s); BioShock používá **art deco 20. let**, které rovnou určuje dobu i architekturu [(17:12)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=1032s). Ve všech případech hra půjčuje hráčovu znalost uměleckých hnutí — a nemusí nic vysvětlovat.

Nejpraktičtější část je **procházka po skutečných cedulích ve městě** [(23:25)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=1405s), protože ukazuje, jak číst typografii jako důkaz. Baculatá písmena kavárny působí přátelsky a spolu s teplými barvami odkazují na 70. léta; asijský supermarket používá **viktoriánské cirkusové plakátové písmo** — „nejsem si jistý, jestli majitel tu asociaci zná" [(24:11)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=1451s); pizzerie sází na bezpatkový font **bez velkých písmen**, aby působila „classy" [(24:57)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=1497s). U řecké restaurace se sejdou tři vrstvy najednou [(28:47)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=1727s): **tvary napodobující řecká písmena, mozaika jako materiál a barevná sada** — všechno dohromady prodává autenticitu. A u starožitnictví v lomeném písmu se ukáže, že asociace bývají vrstvené [(33:26)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=2006s): gotika znamená staré věci, ale zároveň **medievalismus motorkářské kultury** (nášivky, rytířské symboly). Stejně tak vojenský stencil font nese armádu i džungli — **a zároveň razítka na přepravních bednách** [(34:13)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=2053s), což z něj dělá logickou volbu pro obchod s tropickým zbožím.

Dvě konkrétní herní pozorování stojí za převzetí. **Mini Metro** [(19:32)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=1172s) postavilo grafiku na **značení a brožurách newyorského metra** — z čehož plyne přenositelný postup: **je-li hra zasazená do konkrétního času a místa, najdi dobové vizuální manuály** a čti je jako referenci. Naopak hra z autorova review působí nepořádně jen proto, že v ní běží několik nesouvisejících řezů najednou [(18:45)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=1125s) — včetně **nul s přeškrtnutím**, které se špatně čtou zvlášť u měnících se čísel; „nedokážu vždycky říct, proč je zrovna tenhle font použitý na zrovna tuhle věc".

> **Pozn.:** Ručně malované cedule mají podle autora ještě jeden efekt [(31:53)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=1913s): **„skoro to působí, že bys takový text nemohl udělat bez ručního návrhu — a to samo o sobě vytváří dojem kvality"**. Pro herní vývojáře je to použitelné doslova: nepravidelnost čitelně vyrobená rukou nese informaci „tohle někdo dělal", zatímco dokonalý font nese „tohle vygeneroval počítač". Táž logika stojí za [ručně malovaným vzhledem izometrie](2d-vizual.md#izometrie-perspektiva-bez-perspektivy-a-jeji-kompromisy).

**Souvislosti:** [Ludotematický soulad: téma je jazyk hry](ludonarativni-soulad.md#zanr-je-gameplay-tema-je-jazyk-a-tema-uci-hru-za-tebe) · [Scope: design by constraint](scope.md#design-by-constraint-krabice-napred-napad-dovnitr) *(Mini Metro jako škola omezení)* · [Nápad: ideace jako řemeslo](napad.md#ideace-jako-remeslo-skills-audit-veta-s-cilem-a-scamper) *(Ape Out a jeho retheming)* · [Rejstřík: semiotika](../rejstrik.md#semiotika)

---

## Balancování: flair pro atmosféru, čistý font pro funkci

**Zdroj:** [Typography Basics Every Game Dev Should Know](https://www.youtube.com/watch?v=QuNNdPrVMm0) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · závěr kurzu

**Shrnutí:** Čitelnost a atmosféra táhnou proti sobě: dekorativní písmo dodá hře identitu a zpomalí čtení, čistý bezpatkový font se čte rychle a nic neříká. Řešení není kompromis uprostřed, ale **rozdělení rolí** — a klasickou ukázkou je Diablo. K tomu platí jedno tvrdé omezení: **každé přepnutí mezi velmi odlišnými řezy je pro čtenáře kognitivní práh**, takže rolí nesmí být moc.

### Rozpad myšlenky

Diablo I dělá obojí najednou [(20:19)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=1219s): **název nese ikonickou gotickou typografii s kříži**, která hře dodává celou její identitu — „takové písmo bys viděl na desce v katedrále nebo na náhrobku" [(35:47)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=2147s) — zatímco **všechen text, který musíš přečíst, abys pochopil, co zbraň dělá, je v prostém bezpatkovém fontu** [(21:06)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=1266s). Autor k tomu dodává poznámku, kterou by leckterý vývojář nerad slyšel: **„nemusí ti to připadat hezké, ale dělá to, co má"** — informace jde do hlavy rychle, protože ji nezdržují serify. A ještě jedna vrstva na tomtéž obrázku: **bílý text vystupuje víc než šedý** a barvy zároveň kódují vzácnost předmětu, takže písmo pracuje současně jako text i jako signál.

Proč je počet rolí omezený, vysvětluje závěrečná metafora [(36:33)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=2193s): **přepnutí mezi dvěma velmi odlišnými řezy v krátkém sledu funguje jako mentální zpomalovací práh** — autor to přirovnává k situaci, kdy v jednom hovoru mluví dva lidé různými jazyky a ty musíš v hlavě přehodit výhybku. Každý takový práh je malý, ale hráč jich během hraní překoná stovky.

Praktický postup, který z toho plyne, je jednoduchý: projdi všechna místa, kde hra ukazuje text, a **rozděl je na dvě hromádky — „tady jde o atmosféru" a „tady jde o informaci"**. První hromádka smí být dekorativní (titulky, jména předmětů, nápisy ve světě), druhá musí být nudná a rychlá (popisy schopností, tutoriály, dialogy, čísla). Nejasné případy vyhrává čitelnost — protože zdobný popis schopnosti nezachrání atmosféru, ale rozbije souboj.

> **Pozn.:** Video je v půlce i na konci proložené propagací autorových služeb — Discord přes Patreon [(21:52)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=1312s) a placené review dokumentů, freelance konzultace a mentoring [(38:06)](https://www.youtube.com/watch?v=QuNNdPrVMm0&t=2286s). Na obsahu kurzu to nic nemění, ale patří to k poctivému čtení zdroje.

**Souvislosti:** [GDD: Diablo a grafický jazyk dokumentu](gdd.md#will-should-could-jazyk-zavazku-a-dokument-ktery-chce-nekdo-cist) *(tentýž font o dvacet let dřív — v pitch dokumentu z roku 1994)* · [Art specializace: UI a pět cílů pohybu](art-specializace.md#ui-a-ux-ekosystem-pravidel-a-pet-cilu-pohybu) · [Rejstřík: legibilita](../rejstrik.md#legibilita)
