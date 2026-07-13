# Derivační řetěz: od zadání sobě samému k žánru

**Kontext:** IZBA je můj slovanský stealth horor — a tenhle zápisek je rekonstrukce procesu, kterým vznikl. Sepsaná mimo jiné proto, že v jedné týmové debatě zazněla poučka „nejdřív mechaniky, z nich odvodit hru — jinak vznikne generický produkt". Poučka je správně. Ironie: přesně tímhle postupem hra vznikla, měsíce předtím — jenže proces nebyl sepsaný, takže ostatní četli jen hotové GDD. **Hotový dokument maže vlastní historii:** bez derivace se čte jako objednávka („chci slovanský horor"), s derivací jako uvažování kolegy.

## Co se stalo

Řetěz, jak skutečně proběhl:

**1. Zadání sobě samému.** Impuls byla rada od kamaráda u kávy během práce na mnohem větším projektu: „vydej nejdřív něco menšího." Z ní dvě tvrdá omezení: *doručitelné jedním člověkem* a *maximum učení*. Hra je učební artefakt na prvním místě, produkt na druhém — a tohle zadání pak rozhoduje každý spor níž.

**2. Žánr z jádrové mechaniky.** Survival horor: jednoduchá premisa, hráč utíká před AI. Chase je hlavní mechanika — a hlavní mechanika potřebuje podpůrné. Teprve teď vzniká seznam.

**3. Podpůrné mechaniky — každá s alternativou a zamítnutím.** Nejcennější vrstva procesu, protože rozhodnutí mají tvar *proč tohle a proč ne tamto*: **pohyb** (jediná zbraň i obrana; věc, se kterou spousta indie vývojářů bojuje → učení s vysokou přenositelností). **Stamina, ne zdraví** — zdraví zamítnuto ne proto, že je špatné, ale kvůli **stromu závislostí, který táhne s sebou**: zdraví → doplňování → předměty → nejspíš inventář; stamina je čistá a sedí do smyčky. **Chase AI** ohraničená na *jedno* AI v celé hře. **Skrývání, ne souboj** — combat je těžké udělat dobře a hlavně **je to hlavní mechanika převlečená za podpůrnou**. **Environmentální puzzly** navíc: přemýšlení ve stresu.

**4. Narativ až nakonec — odvozený, ne vybraný.** Ze seznamu mechanik vypadla premisa známá všem: Baba Jaga, chaloupka, dítě. A hlavně dětské hry: **na babu ↔ chase, na schovávanou ↔ skrývání** — ludonarativní harmonie doslova. Prohloubení přišlo z pozorování, že původní pohádky bývaly děsivé a poučné → alegorická vrstva: level design jako doslovná Dunning-Krugerova křivka (propad podlahy = pád z Mount Stupid, podzemí = údolí zoufalství, útěk = nabytá kompetence), říkanka jako jediný diegetický quest log.

**5. Technický ocas.** Ověření pohybu: hotový vzorový projekt zamítnut (známé bolesti, není to produkční základ) → state machines postavené a zavržené (příšerně se rozšiřují) → motion matching (řádově lepší, ale systémové tření: každý projekt = nastavovat vše znovu) → **z tření se zrodila komponenta** CLS_MM. A milník „vydej něco svého" se splnil *uprostřed derivace* — komerčním nástrojem, ne hrou.

K tomu metodologický rám, který z pozdější debaty stojí za zafixování: **žánr je one-way door** — rozhodnutí drahé na reverz; dělá ho vlastník, vědomě, se vstupy od ostatních. **Mechaniky uvnitř žánru jsou two-way doors** — levné experimenty, volné hřiště. Vyslovené premisy fixní rozhodnutí *posilují*: samy definují, jak by se dalo vyvrátit. A právo designéra u one-way door není relitigovat, ale **testovat premisy v sankcionovaném okně** — gamedev má to okno institucionalizované: preprodukce, s vertical slicem jako gate artefaktem. Po gate platí disagree & commit.

## Co si z toho beru

- **Neviditelný proces je pro okolí neexistující proces.** Oprava není hádka, ale artefakt: Design Rationale dokument — zadání, derivační řetěz ve formátu *rozhodnutí → alternativy → proč zamítnuty → co mě to učí*, pilíře jako akceptační kritéria („Pohyb je jediná zbraň." „Jsi kořist, ne bojovník.").
- **Alternativy se zapisují i se zamítnutím.** „Stamina místo zdraví kvůli stromu závislostí" je znalost; „máme staminu" je jen stav.
- Sólo důsledek one-way door: vlastník, designér i prototypér v jednom těle → **gate si musíš vnutit sám**. Premisy se znovu otevírají *jen* u gate — ne ve dvě ráno po mizerném dni, kdy každý sólo vývojář „ví", že měl dělat jinou hru. Datované rozhodnutí chrání před věčným přehodnocováním i sunk-cost slepotou naráz.

> **Pozn.:** Koncept je autobiografický dvakrát: hra o cestě ke kompetenci, stavěná jako autorova cesta ke kompetenci. Co v jedné debatě zaznělo jako výtka („jen se učí engine"), je v konceptu záměr a metoda — a proces, kterému se tak říkalo, cestou mimochodem vyprodukoval komerční produkt.

**Souvislosti:** [Lom, ne hřbitov](lom-ne-hrbitov.md) *(odkud se vzalo „vydej něco menšího" a mechanická DNA)* · [Dokumentace jako audit](dokumentace-jako-audit.md) *(kam dorostl technický ocas)* · [GDD review](gdd-review.md) *(co v hotovém dokumentu našlo review)* · [Cut line](cut-line.md) *(gate artefakt premis v praxi)* · [Nářadí, ne archiv](naradi-ne-archiv.md) *(co s těmi dokumenty dál, když začne vývoj)* · [Teorie: nápad](../teorie/napad.md) *(derivace je „pracuj zpátky od omezení" v plné délce)* · [Teorie: scope a malé hry](../teorie/scope.md) · [Teorie: prototypování a vertical slice](../teorie/prototypovani.md) *(slice jako gate premis)* · [Rejstřík: scope](../rejstrik.md#scope) · [Rejstřík: vertical slice](../rejstrik.md#vertical-slice) · [Rejstřík: one-way door](../rejstrik.md#one-way-door)
