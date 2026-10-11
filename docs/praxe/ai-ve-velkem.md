# AI ve velkém: navigace, rozhodování a role v boji

Jak postavit nepřátelskou AI, která vydrží celý AAA projekt: desítky druhů nepřátel všech velikostí, stovky behavior trees a souboje, ve kterých na hráče jde víc nepřátel naráz. Kapitola stojí na jedné přednášce o Lords of the Fallen (Unreal Fest Stockholm 2025) a jejích třech systémech: navigaci pro mnoho velikostí, rozhodování z dat a reakcí a bojových rolích. Hodně z toho je C++ v AAA měřítku. Přenositelné jsou hlavně důvody a tvary řešení. Základy, na kterých to stojí (AI Controller, Behavior Tree, State Tree, utility), najdeš v [Základech nepřátelské AI](ai-zaklady.md) a v [State Trees](state-trees.md).

---

## Jeden nav mesh pro všechny velikosti: šířka chodby jako flag v nav datech

**Zdroj:** [Crafting Scalable AI for a AAA Souls-Like Game in Unreal Engine | Unreal Fest Stockholm 2025](https://www.youtube.com/watch?v=XKQfMZOXFv0) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~41 min, přednáška (senior AI programátor CI Games)

**Shrnutí:** Unreal generuje nav data pro „nav agenta" s jedním poloměrem. Hra s mnoha velikostmi nepřátel by tak potřebovala sadu nav meshů a jejich údržbu při každém přesunu nepřítele. Lords of the Fallen místo toho mají jeden nav mesh pro nejmenší velikost a do jeho polygonů při cookování zapíšou, **jak široká je chodba**, ve které leží. Háček: Unreal flag polygonu používá jen jako 0 a 1 (díra a navigace), takže čísla od 1 výš jsou volná. Navigační filtr pak velkému nepříteli úzké chodby z hledání cesty vyřadí.

### Rozpad myšlenky

**Kontext.** Hra má rychlý reaktivní souboj, velké světy a nepřátele mnoha chování i velikostí. Cílila i na slabší hardware podle měřítek roku 2020 [(0:50)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=50s), [(1:36)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=96s). Proto žádné generování navigace za běhu, jen statická nav data s modifikátory. Nav data se streamují po sublevelech World Composition, protože World Partition v době startu projektu ještě nebyl [(1:36)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=96s), [(2:23)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=143s).

**Problém nav agentů.** Poloměr agenta je odstup okraje navigace od překážek. Zaručuje dvě věci: AI se stejným poloměrem kapsle se o nic neodře a navigace nevznikne tam, kam by se nikdo nevešel [(2:23)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=143s). Jednoduché hře stačí jeden agent, případně druhý pro vozidlo nebo velké zvíře [(3:09)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=189s). Když ale designéři a artisti dostanou volnou ruku, vznikne spousta archetypů s různými kapslemi. Každý nový by chtěl vlastního agenta, nav data by se generovala všude a každý přesun nepřítele při iteraci by znamenal kontrolu nav volume, aby dat bylo dost, ale ne víc kvůli paměti [(3:09)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=189s), [(3:56)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=236s).

**Šířka chodby z nav hran.** Při statickém generování se nav data dělí na dlaždice, které jsou pevné od cookování. V dlaždicích jsou polygony a po jejich okrajích vedou nav hrany [(3:56)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=236s), [(4:44)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=284s). Hrana má směr, takže vektorový součin se svislou osou dá normálu a po normále se dojde k protější hraně. Každé úzké místo je prostor mezi dvěma hranami.

**Velikosti jako trička.** Nepřátelé mají pět velikostí: velmi malou, malou, střední, velkou a velmi velkou. Poloměr agenta odpovídá té velmi malé, takže nejmenší nepřítel projde všude [(4:44)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=284s), [(5:31)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=331s). Šířka, kterou potřebuje největší nepřítel, je dvojnásobek jeho poloměru minus okraje, které už nav data mají [(5:31)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=331s). Při cookování se z každé hrany v dlaždici každých 25 cm vyšle nav trace. Bez zásahu se vejde každý, se zásahem se změřená vzdálenost přiřadí jedné z velikostí [(6:17)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=377s). V nálevkách a v chodbách z víc polygonů se pro každý polygon bere **nejkratší** zásah. Jinak by se polygon označil špatně a nepřítel by se v něm zasekl [(7:05)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=425s).

**Zápis a čtení.** Unreal u polygonu rozlišuje jen 0 pro díru a 1 pro navigaci. Každé číslo od 1 výš je pořád navigace a jeho význam je na tobě, takže každá velikost dostane vlastní flag [(7:05)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=425s). Flag se zapíše na polygon nejbližší ke startu trace; trasuje se z obou stran chodby, takže to pokryje všechny její polygony. Polygon se najde podle jeho identifikátoru (NavNodeRef) [(7:51)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=471s). Dlaždice se analyzují paralelně na pozadí a flagy se zapíšou, až skončí všechny [(8:38)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=518s). Čtou se **navigačním filtrem**, který běží při výpočtu cesty. Podle poloměru kapsle toho, kdo se ptá, vyřadí všechny menší velikosti [(8:38)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=518s), [(9:25)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=565s). Je to výchozí filtr všech nepřátel a vlastní filtry z něj dědí. Nepřítel, který neprojde ohněm, třeba vyřadí i flag ohně [(21:52)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1312s).

**Výsledek.** Střední nepřítel honí hráče jedinou chodbou, kterou projde, malý jde nejkratší cestou [(16:25)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=985s). A hlavně: designéři mohou udělat nepřítele libovolné velikosti v rámci škály, postavit ho kamkoli a na navigaci nesahat [(17:12)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1032s).

> **Pozn.:** Pro malou hru platí přednáška obráceně. S jednou nebo dvěma velikostmi nepřátel stačí jeden nebo dva nav agenti, jak řečník sám říká [(3:09)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=189s), a vlastní krok cookování v C++ se nevyplatí. Přenositelná je myšlenka, že **nav data mohou nést víc než „dá se tu chodit"**, a že filtr rozhoduje podle toho, kdo se ptá. Agent radius jako lék na zasekávání o rohy zná [Nav Mesh v rejstříku](../rejstrik.md#nav-mesh). Co se stane, když je poloměr agenta menší než nepřítel, řeší [další myšlenka](#velky-nepritel-na-malem-agentovi-offset-cesty-ktery-nevyjede-z-navigace).

**Souvislosti:** [Minimální nepřítel a nav mesh](ai-zaklady.md#minimalni-nepritel-pawn-sensing-ai-moveto-a-nav-mesh) · [Levely a streaming](levely-a-streaming.md#open-level-zamrzne-hru-streaming-ji-drzi-zivou) · [Rejstřík: Nav Agent](../rejstrik.md#nav-agent) · [Rejstřík: Navigation Query Filter](../rejstrik.md#navigation-query-filter) · [Rejstřík: World Composition](../rejstrik.md#world-composition)

---

## Velký nepřítel na malém agentovi: offset cesty, který nevyjede z navigace

**Zdroj:** [Crafting Scalable AI for a AAA Souls-Like Game in Unreal Engine | Unreal Fest Stockholm 2025](https://www.youtube.com/watch?v=XKQfMZOXFv0) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~41 min, přednáška (senior AI programátor CI Games)

**Shrnutí:** Když je poloměr agenta menší než nepřítel, vede cesta těsně kolem rohů a velký nepřítel se o ně otírá. Vestavěný Offset From Corners posouvá jen konce úseků cesty, takže umí roh rozdvojit, udělat cik-cak, nebo s cestou vyjet z navigace. Lords of the Fallen mají vlastní „good enough path offset", který roh odsune ve směru osy úhlu a ověří, že bod pořád leží v navigaci. Háček je v ceně, až dva trace na každý bod cesty. Zvládá se přesunem mimo herní vlákno a hlavně tím, co se vůbec nepočítá.

### Rozpad myšlenky

**Proč cesta olizuje rohy.** String pulling, tedy algoritmus simple stupid funnel, zkrátí cestu na nejkratší možnou: přitáhne body k rohům a smaže přebytečné [(10:12)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=612s), [(10:59)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=659s). S agentem velikosti nepřítele je to v pořádku. S agentem nejmenší velikosti vede velkého nepřítele po samé hraně překážky.

**Proč ne Offset From Corners.** Funkci se předá vzdálenost a cesta se od rohů odsune. Posouvá ale začátky a konce úseků a nedívá se, co je mezi nimi. Roh se pak rozdvojí do dvou úhlů, vznikne cik-cak a v nejhorším případě cesta vyjede mimo navigaci [(10:59)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=659s), [(11:45)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=705s).

**Good enough path offset.** Vedle cesty se dá získat **nav koridor**: polygony, kterými cesta vede, a portálové hrany mezi nimi. Každý vnitřní bod cesty leží na levém nebo pravém konci některé z nich [(11:45)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=705s), [(12:32)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=752s). Algoritmus má tyto kroky:
1. Nejdražší krok jde první: nav raycast z bodu na další bod cesty. Když narazí, je tam roh, který se musí odsunout [(13:18)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=798s).
2. Na dvou úsecích kolem rohu se ve stejné vzdálenosti od bodu postaví kolmice. To je levná operace: prohodit x a y a otočit jedno znaménko. Konce kolmic tvoří základnu trojúhelníku a směr odsunu vede ze středu základny k bodu [(13:18)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=798s).
3. U rovnostranného trojúhelníku střed základny splyne s bodem, takže se použije výška [(14:05)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=845s).
4. Kontrola: dot product kandidáta se směrem portálové hrany. Když vyjde záporný, směr se otočí, jinak by bod vyjel z navigace [(14:05)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=845s).
5. Nakonec se směr natáhne podle poloměru agenta, rezervy od překážky a poloměru kapsle [(14:51)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=891s).

**Jak to uživit.** Výpočet běží na pozadí v asynchronní úloze. Výsledek se vrátí za 0,2–0,5 s a to stačí, protože nepřátelé se nemusí rozejít okamžitě [(14:51)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=891s). Úloha má rozpočet snímků, a když ho přetáhne, zaloguje se. Právě logy odhalily chyby: příliš složitou navigaci a selhané výpočty, které posílaly AI do počátku světa (0, 0, 0) po absurdně dlouhé cestě [(15:38)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=938s). Přímé cesty se přeskakují a těch je většina. V boji je přiblížení k hráči, couvnutí i úkrok rovná čára [(15:38)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=938s), [(16:25)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=985s). Aktivních nepřátel je díky Significance Manageru nanejvýš 20, s LOD a agregací ticku. V Insights se offset objeví zřídka, a když ano, bývá to bug [(16:25)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=985s).

> **Pozn.:** Nejpřenositelnější je poslední odstavec, ne geometrie. Těžký výpočet patří mimo herní vlákno a hlavně se **nemusí dělat vůbec** tam, kde výsledek předem znáš, jako u přímé cesty. Rozpočet s logováním přitom není jen ochrana výkonu, ale i detektor chyb. Strop aktivních nepřátel je tentýž tah jako [strop instancí u Niagary](niagara-vykon.md#effect-type-jeden-asset-ktery-rozhoduje-o-vsem): nejdřív omezit počet, pak ladit, kdo dostane výpočet.

**Souvislosti:** [Co je v herním vlákně a co v renderovacím](profiling.md#co-je-v-hernim-vlakne-a-co-v-renderovacim) · [Rejstřík: String pulling](../rejstrik.md#string-pulling) · [Rejstřík: Significance Manager](../rejstrik.md#significance-manager) · [Rejstřík: Multithreading](../rejstrik.md#multithreading)

---

## Strom jen rozhoduje: akce v gameplay abilitách, nepřítel v datech

**Zdroj:** [Crafting Scalable AI for a AAA Souls-Like Game in Unreal Engine | Unreal Fest Stockholm 2025](https://www.youtube.com/watch?v=XKQfMZOXFv0) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~41 min, přednáška (senior AI programátor CI Games)

**Shrnutí:** V Lords of the Fallen behavior tree jen rozhoduje a akci provede gameplay ability, které úloha stromu předá data. Každá úloha má navíc časový limit, který nastaví designér, takže rytmus boje může řídit animace i designér. Nepřítel je popsaný daty. Character data asset nese 145 hodnot a mapy tag → animace, AI data asset smysly, navigaci a stromy. Háček: i tak projekt skončil u obřího hlavního stromu, ve kterém se priority žonglovaly tak, že ho nikdo nechtěl ladit. Odtud vede cesta k [reakcím](#reakce-vedle-stromu-co-se-muze-stat-v-kazdem-stavu-nepatri-do-zadne-vetve).

### Rozpad myšlenky

**Strom rozhoduje, ability jedná.** [GAS](../rejstrik.md#gas) se ve hře používá na všechno, včetně AI [(17:12)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1032s). Úloha `Approach Target` nese data od designéra a předá je abilitě jako payload [(17:58)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1078s):
- chůze, nebo běh,
- jestli smí nepřítel sejít z římsy přirozeným pohybem místo nav linku,
- kterou animaci přehrát, určenou gameplay tagem.

Buď skončí úloha a ukončí abilitu, nebo skončí abilita a dá úloze vědět, že strom může pokračovat [(17:58)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1078s), [(18:44)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1124s).

**Časový limit úlohy.** Combo skončí, když dohraje animace, a couvnutí, když je nepřítel dost daleko. Smyčka idle by ale hrála navěky. Každá úloha proto má timeout: designér řekne „dvě sekundy" a úloha po nich abilitu zastaví [(18:44)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1124s), [(19:30)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1170s). Souboj jde tím řídit dvojím způsobem: **rytmus určí animace**, nebo ho poskládá designér, třeba dvě sekundy doleva, tři dozadu a pak tahle animace [(19:30)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1170s).

**Nepřítel v datech.** Character data asset skládá další data assety, tabulky a hodnoty [(19:30)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1170s), [(20:18)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1218s):
- výbavu a staty, až 145 hodnot na nepřítele,
- loot i s kvalitou a pravděpodobností,
- udělené ability,
- chování kamery při zamčení cíle podle velikosti a rychlosti nepřítele,
- animace jako mapy *gameplay tag → asset*. Zvlášť jsou montáže, tedy jednorázové animace s root motion jako smrt, krok stranou nebo parry útok, a zvlášť sekvence, tedy smyčky a blendy jako chůze a idle [(21:06)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1266s).

Jednoduchý nepřítel má 54 montáží a 17 sekvencí, boss mnohem víc, a proto na organizaci dat záleží [(21:06)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1266s), [(21:52)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1312s). AI data asset nese vnímání, navigační data (kdo projde ohněm) a stromy, které se mají spustit [(21:52)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1312s).

**Kombinace stromů a jak dopadla.** Každý nepřítel spouští hlavní strom (master enemy tree), do kterého se vkládají jeho vlastní stromy pro idle, boj a patrolu. Vedle běží state tree, který z vnímání určí základní stav: idle, caution, found nebo combat [(22:38)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1358s). Koncept byl jednoduchý a snadno se ladil. Na konci projektu byl ale hlavní strom obří [(23:26)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1406s):
- idle zahrnoval deset různých věcí,
- found a caution spouštěly až pět stromů,
- boj zahrnoval i chování, když na hráče útočí další nepřátelé,
- k tomu reakce, které můžou přijít v jakémkoli stavu.

Pro hlubší chování v pokračování by se do stromu muselo přidávat dál. Přidávání ale bylo křehké a ladit ten strom nikdo nechtěl [(24:13)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1453s).

> **Pozn.:** Rozdělení „strom rozhoduje, něco jiného jedná" zná knihovna z [godotové případovky](../godot/pripadovka-nepratele.md#tri-patra-ai-stav-exekutor-controller) jako tři patra: stav, exekutor a controller. Timeout úlohy je drobnost, kterou stojí za to převzít i bez GAS. Úloha, která může běžet donekonečna, je tichý zdroj zaseknutých nepřátel.

**Souvislosti:** [AI Controller, Behavior Tree a Blackboard](ai-zaklady.md#vyssi-liga-ai-controller-behavior-tree-a-blackboard) · [Rejstřík: GAS](../rejstrik.md#gas) · [Rejstřík: Data asset](../rejstrik.md#data-asset) · [Rejstřík: Gameplay tag](../rejstrik.md#gameplay-tag)

---

## Reakce vedle stromu: co se může stát v každém stavu, nepatří do žádné větve

**Zdroj:** [Crafting Scalable AI for a AAA Souls-Like Game in Unreal Engine | Unreal Fest Stockholm 2025](https://www.youtube.com/watch?v=XKQfMZOXFv0) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~41 min, přednáška (senior AI programátor CI Games)

**Shrnutí:** Pro Lords of the Fallen 2 hlavní strom rozebrali. State tree vnímání spouští behavior trees přímo a vedle něj běží **reakce**, malé state trees od designérů. Hlídají, jestli se nemá stát něco, co nepatří do žádného stavu: parry, úhyb, návrat na území, rozbití bedny, za kterou se hráč schoval. Háček je v disciplíně kolem nich. Reakce se netiká, dokud nesplní levnou podmínku, priority jsou jen dvě a fronta má jediné místo. A dlouhé combo nepřeruší, protože hráč soulslike her se učí z konzistence.

### Rozpad myšlenky

**Co je reakce.** Něco, co není základní stav, ale může přijít v kterémkoli [(24:59)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1499s), [(25:45)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1545s):
- parry, blok nebo úhyb před útokem na blízko, magií nebo projektilem,
- omráčení zvláštní schopností hráče,
- cíl mimo dosah nebo mimo navigaci,
- bedna, za kterou se hráč v boji schová. Nepřítel ji rozbije a hráč si výměny chování nevšimne,
- rubber banding: nepřítel se nenechá odlákat daleko od svého území a pomalu se vrací, ať hráč přijde za ním,
- připravená první setkání. Dva vojáci třeba začnou sestupovat po schodech, až když hráč stojí na přesném místě a dívá se tím směrem [(26:32)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1592s).

Cílem bylo znovu použít stovku stromů z první hry a být víc řízený daty [(24:13)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1453s).

**Jak běží.** Vlastní State Tree komponenta spouští perception state tree a paralelně vyhodnocuje reakce [(26:32)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1592s). Perception state tree je bývalý combat state tree, který teď spouští behavior trees sám, takže hlavní strom zmizel [(27:18)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1638s). Příklad: reakce na parry zjistí, že nepřítel může vykrýt další útok, a pošle perception stromu event s behavior tree pro parry. Strom přeruší bojový BT a skočí do stavu Run Reaction, kam se dá dostat jen přes tyhle eventy. Odehraje parry a znovu se vyhodnotí [(28:05)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1685s).

**Disciplína.**
- **Tick podmínky.** Vyhodnocovat parry v idle, když nikdo neútočí, nedává smysl. Každá reakce má levnou podmínku, třeba přítomný gameplay tag nebo poslaný gameplay event. Bez ní se její strom vůbec netiká [(28:51)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1731s).
- **Dvě priority.** Vysoká znamená, že se reakce musí stát hned a nesmí se přerušit; nízká, že přerušit smí. Návrat na území přeruší parry, a když parry skončí, návrat se spustí znovu [(29:38)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1778s), [(30:24)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1824s).
- **Fronta o jednom místě.** Desetisekundové combo návrat na území nepřeruší a reakce počká [(31:11)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1871s). Nová reakce ve frontě nahradí starou a okamžitá reakce frontu smaže. Nic se nehromadí, jinak by nepřítel po návratu vykrýval útok, který už dávno nepřišel [(31:58)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1918s).
- Cooldown ve stylu GAS (tag a čas), tagy přidané po dobu reakce a vypínač pro ladění a izolaci chyb [(31:11)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1871s), [(31:58)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1918s).

**Past s pamětí stromu.** Behavior tree komponenta drží trvalou paměť (known instances) a dočasnou (instance stack) a paměť podstromů si kopíruje tam a zpátky [(32:45)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=1965s), [(33:32)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=2012s). Lords of the Fallen v boji vybírají přes utility a poslední volbu si ukládají do paměti stromu, aby se neopakovala. Když se strom zastaví, paměť se ale smaže. Se samostatnými stromy, které se podle reakcí spouštějí a zastavují, pak utility vybíral pořád totéž [(34:19)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=2059s). Oprava: při zastavení se paměť zálohuje do vlastní kopie a při dalším spuštění obnoví [(35:05)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=2105s). Jen pro vlastní uzly, tedy utility a cooldowny, ne pro uzly enginu, aby je nerozbila změna v tom, jak Unreal paměť spravuje [(35:52)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=2152s).

> **Pozn.:** Rubber banding tu neznamená pomoc hráči, který zaostává, jak ho zná [rejstřík](../rejstrik.md#rubber-banding), ale vodítko, které drží nepřítele u jeho území. Fronta, která počká na konec comba, je AI strana téhož principu jako [tells](../rejstrik.md#tell): hráč se v soulslike učí číst vzorce, takže vzorec se nesmí rozpadnout uprostřed. Tick podmínky dělají totéž co [overlap místo trasování v Ticku](interakce-bez-event-ticku.md#overlap-trigger-misto-trasovani-v-ticku): drahé se vyhodnocuje až po levném filtru. Řečník doporučuje článek o reaktivních behavior trees, odkaz je na konci přednášky.

**Souvislosti:** [State Trees: kostra](state-trees.md#kostra-state-tree-ai-komponenta-tasky-a-kontext) · [Utility AI](ai-zaklady.md#utility-ai-rozhodovani-podle-skore-misto-vetveni) · [Rejstřík: State Tree](../rejstrik.md#state-tree) · [Rejstřík: Behavior Tree](../rejstrik.md#behavior-tree) · [Rejstřík: Gameplay tag](../rejstrik.md#gameplay-tag)

---

## Kdo útočí a kdo čeká: aggro skóre a bojové role

**Zdroj:** [Crafting Scalable AI for a AAA Souls-Like Game in Unreal Engine | Unreal Fest Stockholm 2025](https://www.youtube.com/watch?v=XKQfMZOXFv0) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~41 min, přednáška (senior AI programátor CI Games)

**Shrnutí:** Každá akční hra s víc postavami řeší dvě situace. Nepřítel si vybírá mezi dvěma hráči (online co-op) a víc nepřátel míří na jednoho hráče. Na první je **aggro skóre** z blízkosti, vydrženého poškození, umělého aggra a skóre přepnutí, které brání přeskakování mezi cíli. Na druhou jsou **role** útočník, kryt a divák, přidělované podle toho, jak je nepřítel nebezpečný. Háček: nikdo nestojí. I divák se hýbe a občas zaútočí a role se za boje střídají, takže souboj působí jako tanec, ne jako fronta.

### Rozpad myšlenky

**Aggro.** Skóre každého cíle se skládá ze čtyř složek [(36:38)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=2198s):
- blízkost: čím blíž, tím víc,
- poškození, které cíl nepříteli dává, a to nejen jak velké, ale i jak dlouho vydržené,
- umělé aggro, které jde přidat, když má nepřítel zůstat u jednoho hráče,
- skóre přepnutí, které funguje jako cooldown proti přeskakování mezi cíli.

Některé složky s časem klesají k nule podle křivek, které ladí designéři [(36:38)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=2198s). V ukázce druhý hráč nepřítele občas trefí a nic se nestane. Teprve vytrvalý útok ho udělá nebezpečnějším a nepřítel se k němu otočí [(37:25)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=2245s). Kdo chce nepřítele odlákat, musí útočit soustavně [(38:11)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=2291s).

**Role.** Aby na jednoho hráče nešli všichni najednou, což by bylo nefér, počítá se kromě aggra i nebezpečnost nepřítele z jeho útočné síly [(38:11)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=2291s).
- **Útočník** jde na hráče naplno. Nebezpečný nepřítel smí být útočníkem jen jeden, slabších až tři, takže tři obyčejní, nebo boss a jeden obyčejný [(38:11)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=2291s).
- **Kryt** krouží kolem boje, snaží se dostat do pozice, ze které se stane útočníkem, a útočí jen občas [(38:58)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=2338s).
- **Divák** se drží vzadu, hýbe se a útočí velmi zřídka [(38:58)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=2338s).

Role se podle skóre střídají a každá má vlastní behavior tree v data assetu. Nepřátelé s holí jako kryt a divák útočí na dálku, jako útočníci jdou na hráče zblízka [(38:58)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=2338s).

**Za hranice žánru.** Řečník to vztahuje i na střílečky: kryt je za krytem a divák přebíhá nebo přebíjí. V pokračování role dál rozšiřují [(39:45)](https://www.youtube.com/watch?v=XKQfMZOXFv0&t=2385s).

> **Pozn.:** Tady se AAA systém potkává s [teorií souboje](../teorie/game-feel.md#souboj-dela-zabavnym-pohyb-nepratel-ne-jejich-statistiky): zábavu dělá pohyb nepřátel, ne jejich staty, a role jsou způsob, jak naplánovat pohyb celé skupiny. Útočník, kryt a divák jsou zároveň regulátor [obtížnosti](../teorie/obtiznost.md#challenge-je-co-difficulty-je-kolik), protože počet útočníků podle nebezpečnosti je nastavitelné číslo. Menší hře může stačit samotné pravidlo „nanejvýš N útočníků naráz" a krouživé chování ostatních. Skóre a křivky přijdou na řadu, až bude co ladit.

**Souvislosti:** [Rejstřík: Aggro](../rejstrik.md#aggro) · [Utility AI](ai-zaklady.md#utility-ai-rozhodovani-podle-skore-misto-vetveni) *(aggro je skóre stejného druhu)* · [Rejstřík: Context steering](../rejstrik.md#context-steering) *(krouživý pohyb kolem cíle)* · [Rejstřík: Data asset](../rejstrik.md#data-asset) · [Spawn closet](../teorie/prostor-a-hranice.md#spawn-closet-posily-ktere-odnekud-prijdou) *(odkud posily přijdou, když rozpočet dovolí)*
