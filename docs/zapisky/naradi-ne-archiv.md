# Nářadí, ne archiv: co s dokumenty po konceptu

**Kontext:** Koncepční audit ti nechá čtyři dokumenty — intake, design rationale, pilíře, audit konceptu. Otázka, kterou nikdo neřeší, přijde hned po nich: co se s nimi děje, až začne vývoj? Jen je linknout do GDD a zapomenout? Většina designových dokumentů skončí v šuplíku den po dopsání. Správně mají tři ze čtyř žít dál — jako nářadí, ne archiv.

## Co se stalo

Derivace konceptu vyprodukuje sadu dokumentů: intake dostane na papír *co / cíl / omezení*, design rationale zaznamená řetěz rozhodnutí, pilíře z něj vydestilují akceptační kritéria. Projde audit. A pak stojíš před GDD s hromádkou papírů vedle a přirozenou otázkou nováčka: **a teď?**

Naivní odpověď je „nalinkuju je do GDD jako přílohy". Je špatně, protože předpokládá, že ty dokumenty sdílejí životnost. Nesdílejí. GDD je cíl — *co hra JE teď*. Ostatní čtyři kolem něj obíhají, každý s jinou prací a jinak dlouhým životem.

**Intake je lešení.** Jednorázový základ. Jakmile se identita hry vleje do přehledu v GDD, intake dosloužil — necháš si ho jako datovaný snímek startu a víc na něj nesáhneš. Je to jediný ze čtyř, který opravdu *je* archiv: vylezeš po něm a opustíš ho. Kdo se k intake vrací během vývoje, dělá nejspíš chybu — buď řeší něco, co už patří do GDD, nebo mu chybí pilíře.

**Design rationale je živý decision log.** Drží *proč* za každým rozhodnutím v GDD, ve formátu *rozhodnutí → alternativy → proč zamítnuty*. Přírůstkový, datovaný, nemaže se. Jeho výplata nepřijde teď, ale za půl roku — až narazíš na rozhodnutí, které vypadá blbě, a budeš ho chtít předělat. Rationale řekne „tohle jsi zkusil a padlo to kvůli X" a ušetří ti druhé projití téže slepé uličky ve dvě ráno po mizerném dni. Druhá funkce: je to způsob, jak člověk, který přijde do projektu později, pochopí záměr, aniž tě musí vyrušit. V softwaru se tomu říká decision log nebo ADR — hry si ho půjčují málo a platí za to opakovaným přehodnocováním.

**Pilíře jsou denní filtr.** Nejprovoznější dokument z celé sady. Každý nový nápad na feature, každé „a co kdyby tam ještě bylo", každé pokušení ke scope creepu se proti nim testuje: *podporuje / neutrál / porušuje*. To je jejich celá práce — a je vývojová, ne konceptová. Proto patří na první stránku GDD, pořád na očích, ne do přílohy. Jsou živé: přepisuješ je vědomě, a pilíř, který za celý projekt nic nezamítl, je moc měkký — přepiš ho, nebo zahoď. Tohle není indie exotika; design pillars jsou standardní AAA praxe, doslova vytištěné na zdi studia, přesně proto, aby je každý spor o feature měl na očích.

**Audit je opakovaná událost, ne udržovaný dokument.** Neudržuješ ho — opakuješ. Na milnících: po prototypu, až padnou věci vědomě odložené „hradluje prototyp"; před přechodem do produkce; kdykoli scope začne ujíždět a ty to cítíš. Každý audit je datovaný artefakt a jejich série je čitelný záznam zdraví projektu v čase — vidíš, kdy se co zlomilo a kdy se to spravilo.

Celé to drží jedna věta: **GDD říká co, rationale proč (a proč ne), pilíře co se nikdy nesmí rozbít, audit jestli to celé ještě drží pohromadě.** Čtyři otázky, čtyři dokumenty.

A protože vývoj je kontakt s realitou, dokumenty cyklí. Prototyp zabije premisu nebo si vynutí změnu rozhodnutí → dopíšeš kartu do rationale → překontroluješ, jestli změna neporušila pilíř → na milníku spustíš nový audit. Nepíšou se jednou. Jen se — na rozdíl od nápadů ve dvě ráno — otevírají u gate, vědomě a datovaně.

## Co si z toho beru

- **Dokument má cenu jen tehdy, když se používá — jinak je archiv.** Tři ze čtyř se používají: rationale se dopisuje, pilíře filtrují, audit se opakuje. Intake je jediná výjimka, a to je v pořádku — lešení se po dostavbě odklízí.
- **Rozděl dokumenty podle otázky, kterou zodpovídají**, ne podle toho, že „jsou to všechno design docs": co (GDD) / proč (rationale) / co se nesmí rozbít (pilíře) / drží to ještě? (audit). Jeden dokument = jedna otázka. Míchání dvou otázek do jednoho papíru je začátek nepořádku, který zjistíš až za běhu.
- **Domov dokumentu se řídí frekvencí použití, ne jeho typem.** Po pilířích saháš denně → první stránka GDD. Do rationale koukneš dvakrát za projekt → příloha. Intake je hotový → archiv. „Kam to dát" není otázka o druhu dokumentu, ale o tom, jak často do něj půjdeš.
- **Audit není dokument, je to návyk.** Datovaná série auditů je čitelný záznam — přesně to, co dobrá praxe chce po každém selhání: aby šlo zpětně přečíst. Playtest je totéž o patro níž: QA pro design.

> **Pozn.:** Skrytý paradox téhle sady: dokument, který nejpracněji derivuješ (rationale), je ten, do kterého během vývoje koukneš nejmíň často — ale nejvíc ho oceníš, když ano. Je to pojistka, ne denní nářadí. Pilíře jsou naopak levné na napsání a saháš po nich pořád. Hodnota dokumentu se neměří časem, který jsi strávil jeho psaním.

**Souvislosti:** [Derivační řetěz IZBY](derivace-izby.md) *(odkud ty dokumenty jsou: rationale a pilíře jako akceptační kritéria)* · [Cut line](cut-line.md) *(pilíře vynucují cut line; onboarding juniorů přes zapsaný záměr)* · [GDD review](gdd-review.md) *(audit dokumentu: kde slib nesedí s technikou)* · [Dokumentace jako audit](dokumentace-jako-audit.md) *(piš z artefaktu — dokument má cenu, jen když se používá)* · [Selhávat citelně a čitelně](selhavat-citelne-a-citelne.md) *(audit jako „čitelný" záznam; playtest = QA pro design)* · [Devlog jako mapa](devlog-jako-mapa.md) *(živý přírůstkový záznam během stavby)* · [Teorie: scope a malé hry](../teorie/scope.md) *(pilíře jako design by constraint)* · [Teorie: žrouti času](../teorie/produktivita.md) *(scope creep, proti kterému pilíře stojí)* · [Teorie: prototypování a vertical slice](../teorie/prototypovani.md) *(slice jako gate, kde audit ožívá)* · [Rejstřík: Game Design Document](../rejstrik.md#game-design-document) · [Rejstřík: scope creep](../rejstrik.md#scope-creep) · [Rejstřík: design by constraint](../rejstrik.md#design-by-constraint) · [Rejstřík: one-way door](../rejstrik.md#one-way-door)
