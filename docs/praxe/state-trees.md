# State Trees: kompletní nepřítel se smysly

State Tree je Epicem preferovaný nástupce behavior tree — a tahle kapitola na něm staví celého nepřítele: patroluje po spline, na dohled tě honí, za zvukem nebo zásahem se jde podívat, po dostižení mlátí a když zmizíš, vrátí se k patrole. Zdrojem je jeden důkladný 40minutový tutoriál; koncepty State Tree v kontextu Epicova použití (smart objects, NPC) ukazuje [GASP kapitola](gasp.md#npc-pres-state-tree-a-smart-objects-mozek-na-serveru-motor-v-komponente).

---

## Kostra: State Tree AI komponenta, tasky a kontext

**Zdroj:** [Build Smart AI with State Trees in UE5 (Full Tutorial)](https://www.youtube.com/watch?v=UuqKC0AgeXU) · [HardcastleGames](https://www.youtube.com/channel/UCOCEq2hstYaRxT9wsUK1nig) · ~40 min, tutoriál — část setup + patrola

**Shrnutí:** Setup má tři nečekané zádrhely: k defaultnímu StateTree pluginu je nutné doinstalovat **Gameplay StateTree** [(0:48)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=48s), asset se zakládá jako varianta **State Tree AI Component** (ne obecný State Tree) [(2:22)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=142s), a strom neběží na postavě, ale na **AI controlleru** přes StateTreeAI komponentu [(3:08)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=188s). Pak už platí jednoduchá anatomie: stav → task → přechod.

### Rozpad myšlenky

**Mozek a tělo:** controller = rozhodnutí, postava = pohyb a fyzická přítomnost; oddělení umožňuje znovupoužít logiku napříč postavami [(1:35)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=95s). Postava dostane `AI Controller Class` + `Auto Possess AI: Placed in World or Spawned` [(3:08)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=188s).

**Anatomie tasku** [(8:33)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=513s): blueprint task má `Event Enter State` (co se stane při vstupu do stavu) a `Finish Task` (úspěch/neúspěch). Zásadní rozdíl proti behavior tree: **Finish Task neukončí jen task, ale celý stav** — z toho žijí přechody `On State Succeeded/Failed`. K okolí se task dostane přes **context**: Unreal automaticky injektuje AI controller každému tasku [(9:19)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=559s) — proměnná typu AI Controller označená jako context se naplní sama, žádné manuální gettery [(10:06)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=606s).

**Patrola po spline:** trasa je **BP actor se Spline komponentou** — body se tahají po zemi, `Alt` + tažení duplikuje bod, trasa má tvořit smyčku [(3:54)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=234s). Postava dostane cestu proměnnou (instance editable + expose on spawn → přiřazení v details každé instance) [(6:07)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=367s) — a controller si ji vytáhne přes **Blueprint Interface** `Get Patrol Path`, žádný cast na konkrétní třídu [(5:27)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=327s). Na `On Possess`: get spline → `Get Number of Spline Points` → čítač current/total [(6:54)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=414s). Pohyb: `AI MoveTo` ← **Get Location at Spline Point** (coordinate space **World**, ne Local!) [(11:36)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=696s); on success inkrement, přetečení → 0, další bod [(12:23)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=743s). Stav patrol má transition `On State Completed → Patrol` — smyčka [(10:49)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=649s).

> **Pozn.:** Interface na patrol path je stejný vzor jako v [komunikaci Blueprintů](komunikace-blueprintu.md) — task potřebuje data, ale nemá znát třídu; kontrakt místo castu. Drobný hack z videa: default ABP_Manny po nav mesh „klouzal", autor to vyřešil odstraněním idle stavu z locomotion [(12:51)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=771s) — čistší řešení je `Use Acceleration for Paths` ze [základů AI](ai-zaklady.md#vyssi-liga-ai-controller-behavior-tree-a-blackboard).

**Souvislosti:** [GASP: NPC a smart objects](gasp.md#npc-pres-state-tree-a-smart-objects-mozek-na-serveru-motor-v-komponente) · [Komunikace Blueprintů](komunikace-blueprintu.md) · [Rejstřík: State Tree](../rejstrik.md#state-tree) · [Rejstřík: spline](../rejstrik.md#spline) · [Rejstřík: AI Controller](../rejstrik.md#ai-controller)

---

## Jedna percepce, tři smysly a Report eventy

**Zdroj:** [Build Smart AI with State Trees in UE5 (Full Tutorial)](https://www.youtube.com/watch?v=UuqKC0AgeXU) · [HardcastleGames](https://www.youtube.com/channel/UCOCEq2hstYaRxT9wsUK1nig) · část o AI Perception

**Shrnutí:** Jedna AI Perception komponenta na controlleru obslouží **zrak, sluch i damage** — tři sense configy a jedna funkce, která z updatu pozná, *který* smysl se ozval. K tomu klíčové rozlišení: sluch a damage se do percepce hlásí přes **Report Noise/Damage Event**, což jsou signály pro AI — s přehráním zvuku ani skutečným poškozením nemají nic společného.

### Rozpad myšlenky

**Config** [(14:24)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=864s): tři configy (Sight, Hearing, Damage), `Dominant Sense = Sight`; zrak `Sight Radius` 750 / `Lose Sight Radius` 1250. Dvakrát pozor na **Detect Enemies/Neutrals/Friendlies**: u zraku na to autor myslel, u sluchu ne — a půl videa později debugoval, proč nepřítel neslyší [(20:33)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=1233s). Checkbox chybí v každém novém configu.

**Který smysl to byl?** `On Perception Updated` vrací seznam aktualizovaných actorů; funkce **Can Sense Actor** (vstup: actor + vlastní enum sight/hearing/damage) pak přes `Get Actors Perception` projde poslední stimuly a porovná `Get Class for Sense Stimulus` se **Select** uzlem mapujícím enum na třídy `AISense_Sight/Hearing/Damage` [(15:27)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=927s), [(17:06)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=1026s). Vrací stimulus, actora a `Successfully Sensed` — **true = vjem začal** (poprvé vidím/slyším), **false = vjem skončil** (ztratil jsem ho) [(17:25)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=1045s). Jedna funkce, tři volání — smysly se nepletou do sebe.

**Report eventy** [(18:12)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=1092s): `Report Noise Event` (pozice, loudness, range) a `Report Damage Event` (instigator, pozice, množství, zasažený) jsou **vstupy pro percepci** — testovací klávesy N/M je ve videu volají přímo. Zásadní: `Play Sound` percepci **neprobudí** a `Report Damage` **neubere život** [(18:58)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=1138s). Herní zvuk a herní damage jsou jiné systémy; kdo chce obojí, volá obojí.

> **Pozn.:** Tohle oddělení je designová příležitost, ne otrava: můžeš mít kroky, které AI slyší, ale hráč ne (a naopak), nebo „hlasité" gameplay akce definované čistě designem (rozbité okno = Report Noise s velkým range). Pro stealth přesně ta páka, kterou chceš držet v ruce.

**Souvislosti:** [AI vnímání: tři nástroje](ai-vnimani.md#tri-nastroje-detekce-pawn-sensing-ai-perception-trigger) · [Rejstřík: AI Perception](../rejstrik.md#ai-perception) · [Rejstřík: State Tree](../rejstrik.md#state-tree)

---

## Přechody přes gameplay tagy a event dispatchery

**Zdroj:** [Build Smart AI with State Trees in UE5 (Full Tutorial)](https://www.youtube.com/watch?v=UuqKC0AgeXU) · [HardcastleGames](https://www.youtube.com/channel/UCOCEq2hstYaRxT9wsUK1nig) · část chase + investigate + attack

**Shrnutí:** Stavy se přepínají dvěma mechanismy: **eventy s gameplay tagy** (percepce pošle `Send State Tree Event` s tagem „chase" a strom má přechod „on event chase") a **dokončením stavu** (`On State Succeeded/Failed`). Dlouhotrvající akce (dojdi, zaútoč) tasky řeší bindem na **event dispatcher** — task čeká, dispatcher ho probudí, `Finish Task` rozhodne o přechodu.

### Rozpad myšlenky

**Eventové přechody** [(24:34)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=1474s): na stavu `Transition on Event`, priorita High, required event = **gameplay tag** (nový tag „chase"; pozor vybrat *source* — bez toho přechod mlčí [(25:22)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=1522s)). Percepce pak při spatření volá `Send State Tree Event` s `Make State Tree Event` (jen tag, payload netřeba) [(25:52)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=1552s); ztráta cíle posílá tag „patrol". Kdokoli odkudkoli může poslat tag — stavy nemusí o odesílateli nic vědět.

**Investigate — jdi za stimulem** [(29:05)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=1745s): sluch/damage větev percepce pošle tag „investigate" (patrol má na něj přechod [(29:51)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=1791s)) a controller vyrazí `AI MoveTo` na **stimulus location** — pozici zvuku, ne actora. Task investigate se binduje (`Assign`) na dispatcher `On Investigate Finished`, který controller vystřelí po doběhnutí; task pak `Finish Task` → `On State Succeeded → Patrol` [(28:35)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=1715s). Investigate má navíc on-event přechod na chase — když cestou uvidí hráče, plynule přepne [(31:40)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=1900s).

**Chase a attack — řetěz dispatcherů:** spatřený hráč se drží v proměnné `attack target` (nastaví true větev, vynuluje false) [(21:54)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=1314s); chase event dělá `AI MoveTo` přes **validated get** [(22:40)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=1360s) a hlásí `On Chase Completed` (dostižen) nebo `On Chase Failed` (ztracen). Task chase binduje obojí: completed → `Finish Task` úspěch, failed → neúspěch [(36:50)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=2210s). Přechody pak čtou výsledek: `Succeeded → Attack`, `Failed → Patrol` — a attack po dokončení úderu (montáž + dispatcher `Attack Finished` [(32:38)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=1958s)) přechází `Succeeded → Chase`, takže dokud tě drží v dosahu, střídá běh a rány [(37:35)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=2255s).

**Výsledné chování** [(38:21)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=2301s): patroluje → slyší zvuk → jde ho prověřit → cestou tě uvidí → honí → mlátí → ztratí tě → patrola. Kompletní smyčka stealth nepřítele z pěti stavů a hrstky tagů. (Drobnost na závěr: kamera se při úderu cukala o kapsli nepřítele — camera boom → `Do Collision Test` off [(38:21)](https://www.youtube.com/watch?v=UuqKC0AgeXU&t=2301s).)

> **Pozn.:** Vzor „task binduje dispatcher a čeká" je přesně to, co GASP dělá u [smart objects](gasp.md#npc-pres-state-tree-a-smart-objects-mozek-na-serveru-motor-v-komponente) — mozek (strom) rozhoduje, motor (controller/komponenta) vykonává a hlásí zpět. Srovnání s [behavior tree přístupem](ai-zaklady.md#vyssi-liga-ai-controller-behavior-tree-a-blackboard) je poučné: co tam řeší Blackboard + decoratory (sdílený stav, observer aborts), tady řeší tagy + eventy — State Tree je „push" model, strom nemusí nic pollovat.

**Souvislosti:** [GASP: NPC a smart objects](gasp.md#npc-pres-state-tree-a-smart-objects-mozek-na-serveru-motor-v-komponente) · [Základy AI: Behavior Tree](ai-zaklady.md#vyssi-liga-ai-controller-behavior-tree-a-blackboard) · [Gameplay Tags](gameplay-tags.md) · [Rejstřík: State Tree](../rejstrik.md#state-tree) · [Rejstřík: event dispatcher](../rejstrik.md#event-dispatcher) · [Rejstřík: gameplay tag](../rejstrik.md#gameplay-tag)
