# Selhávat citelně, selhávat čitelně

**Kontext:** Maxima, která vykrystalizovala v létě 2026 z dlouhé debaty nad vlastní cestou samouka — a nad tím, jak se testují systémy, které si nemůžou dovolit selhat před publikem. Je to filozofické jádro celých Zápisků: všechno ostatní tady jsou její aplikace.

## Co se stalo

Debata začala nevinně (jak vlastně funguje testování velkých AI modelů před nasazením) a skončila u otázky, co dělá ze selhání lekci. Odpověď má dvě slova, která dělí jediné písmeno:

- **Citelně** — selhání musí být cítit. Vzniká jen z poctivé snahy o výhru: sázka byla reálná, prohra zabolela, signál existuje. Selhání „naoko" nenese žádnou informaci — gradient vzniká z rozdílu mezi poctivou snahou a výsledkem. Když se snažíš selhat a selžeš, chyba je nula a lekce taky. Citelně ale neznamená zničujícně: cílem jsou selhání **častá, levná a výživná**. Bolest je informace, ne trest.
- **Čitelně** — selhání musí jít přečíst. Pád sám o sobě je šum; lekcí se stává až záznamem: co se stalo, kdy, proč, s jakým zdrojem. Devlog, failure log, postmortem, datovaný seznam. Spousta nadšených lidí selhává nečitelně — a nenaučí se nic.

Jedno bez druhého nefunguje. Citelné a nečitelné selhání je trauma: bolí, ale nevíš proč, takže se naučíš strach místo dovednosti. Čitelné a necitelné je sterilní: dá se přečíst, ale nic tě nenutí to udělat. Učí až průnik — **bolelo to a je to zapsané.**

K tomu tři pomocné věty, které z debaty zůstaly:

**Crash v QA je informace; crash v den vydání je průšvih.** Stejná chyba, diametrálně jiná cena — rozdíl nedělá chyba, ale prostředí. Umění není se selhání vyhnout (to nejde), ale vědomě si stavět prostory, kde je levné: playtest je QA pro design, game jam je QA pro scope. A když už drahé selhání nastalo, zpětná destilace (postmortem, tenhle zápisek) je mechanismus, kterým se dodatečně zlevňuje — cena už padla, ale výtěžnost se dá zvednout.

**Nadšení je palivo, ne motor.** Motivačně-plakátová verze zní „s dostatečným zápalem neexistují mantinely". Neexistuje: motor je smyčka *vlézt do domény → selhávat citelně → zapisovat čitelně → iterovat*; palivo rozhoduje jen o tom, jak dlouho poběží. Bez smyčky zápal jen rychleji spálí nadšence, který selhává nečitelně.

**Mantinely existují — zjišťují se testem, ne cizím výrokem.** Cizí věty o tom, kdo jsi a na co máš, nejsou data — jsou to hypotézy pronesené z nedostatečné znalosti, často s velkou sebejistotou. Test je benchmark, prototyp, jam, publikovaná komponenta. S dvěma korektivy, bez kterých se z téhle teze stane hluchota: když test řekne, že pravdu měla druhá strana, **datům se ustupuje** — i uprostřed konfliktu, i od člověka, jehož verdikt o tobě byl nespravedlivý (umění je třídit *verdikty o osobě* od *dat o práci*). A vyvrácené verdikty nevysvětluj skrytým talentem — to jen otáčí znaménko cizí teorie a nechává ji žít. Verdikty nevyvrací talent, vyvrací je metoda.

A jedna past na závěr: **kronika cizích omylů není failure log.** Datovaný seznam toho, kdo se ve mně kdy spletl, je čitelný artefakt — ale sám o sobě jen vindikační oblouk. Filozofie se pozná podle toho, že člověk čitelně zapisuje *svoje* pády: zaseklé shadery, audit vlastní komunikace i s nelichotivými nálezy, přestřelený scope.

## Co si z toho beru

Tahle filozofie se nevyznává — staví se. A při zpětném pohledu už v mých projektech stojí: stealth hra je stroj na citelná a čitelná selhání (smrt bolí ztrátou postupu a zároveň je čitelná — vidíš patrolu, která tě dostala; nečitelná smrt je frustrace, čitelná je lekce). IZBA dělá čitelným to nejhůř čitelné selhání ze všech — vlastní nekompetenci, kterou Dunning-Kruger drží mimo dohled jejího nositele. Kvízový protokol jsou mikroselhání na předpis s okamžitým zápisem. A tahle skripta i devlogy jsou „zapisovat čitelně" povýšené na infrastrukturu.

Druhá vrstva je generační: odkazem není pád, ale destilát. Selhání s vytěženou lekcí přestává být selháním — a prvním dědicem dnešních pádů je zítřejší já.

> **Pozn.:** Forma maximy zrcadlí obsah: *citelně* a *čitelně* dělí jediné písmeno — stejně malý je rozdíl mezi selháním, které tě něco naučí, a tím, které ne. Rozhoduje o něm, jestli se pád dostal na papír.

**Souvislosti:** [Karta selhání: packaging](karta-selhani-packaging.md) *(filozofie přeložená do formuláře)* · [Dokumentace jako audit](dokumentace-jako-audit.md) · [Teorie: začátky bez zkušeností](../teorie/zacatky-bez-zkusenosti.md) *(motivace vs. vůle je tatáž distinkce o patro výš)* · [Teorie: prototypování a vertical slice](../teorie/prototypovani.md) · [Rejstřík: postmortem](../rejstrik.md#postmortem) · [Rejstřík: playtest](../rejstrik.md#playtest)
