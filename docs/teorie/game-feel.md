# Game feel a imerze: pocit ze hry

Kapitola o tom, aby hra *působila* — aby souboj byl živý a svět skutečný. Dva devlogy řeší pohyb nepřátel (nuda vs. tanec) a reakci prostředí na hráče (kulisa vs. svět); katalog juice detailů ukazuje, jak tytéž mechaniky prodat desetkrát líp; a combat devlog SILKROAD přidává nejtěžší vrstvu — rytmus. Společný jmenovatel: pocit nevzniká z čísel v tabulkách, ale z pohybu, odezvy a načasování — a skoro vždycky je to chytrý fake, ne simulace.

---

## Souboj dělá zábavným pohyb nepřátel, ne jejich statistiky

**Zdroj:** [The Trick I Used to Make Combat Fun! | Devlog](https://www.youtube.com/watch?v=6BrZryMz-ac) · [Game Endeavor](https://www.youtube.com/channel/UCLweX1UtQjRjj7rs_0XQ2Eg) · ~8 min, devlog (open-world RPG)

**Shrnutí:** Nepřátelé, kteří na hráče běží po přímce, jsou placeholder, ne souboj. Autor předělal pohyb kostlivců na context steering — vážené rozhodování mezi směry — a přidal chování „přibliž se, krouž, drž odstup". Výsledek: tester u hrstky kostlivců dobrovolně strávil hodinu. Stejná mechanika, stejné dmg — jiný pohyb.

### Rozpad myšlenky

Cesta k řešení je poučná i s odbočkami. Klasické **steering behaviors** (boids) [(0:56)](https://www.youtube.com/watch?v=6BrZryMz-ac&t=56s) skládají jednoduché síly (jdi tam, drž se dál od…), jenže protichůdné vektory se umí vyrušit: nepřítel má utéct, za zády má zeď — a tak jen stojí a čeká na smrt [(1:34)](https://www.youtube.com/watch?v=6BrZryMz-ac&t=94s). **Context steering** [(1:58)](https://www.youtube.com/watch?v=6BrZryMz-ac&t=118s) problém řeší tím, že si drží *ohodnocení všech směrů* (přes dot product — jak moc směr souhlasí s tím kýženým [(3:10)](https://www.youtube.com/watch?v=6BrZryMz-ac&t=190s)) a vybírá nejlepší *proveditelný*: když je nejlepší směr zablokovaný, vezme druhý nejlepší, místo aby zamrzl.

Zábavnost pak vzniká tvarováním vah [(4:17)](https://www.youtube.com/watch?v=6BrZryMz-ac&t=257s): zblízka slábne váha „k cíli" a nastupuje preference pohybu do stran → kostlivci krouží kolem hráče, nabíhají a odskakují. (S komickou epizodou: dokonalé kroužení vyrobilo „Newtonovo kyvadlo z kostlivců" [(0:00)](https://www.youtube.com/watch?v=6BrZryMz-ac&t=0s) — spravil rozhozený odstup.) Poslední kaz byl jitter — nepřátelé se přetlačovali v tug-o-war a cukali sebou [(4:54)](https://www.youtube.com/watch?v=6BrZryMz-ac&t=294s); vyřešilo ho odpuzování pod úhlem místo přímo od souseda. Výsledek [(5:18)](https://www.youtube.com/watch?v=6BrZryMz-ac&t=318s): souboj, který baví i autora — a hodinový playtest z vlastní vůle.

Druhá půlka téže lekce je **wandering** [(5:32)](https://www.youtube.com/watch?v=6BrZryMz-ac&t=332s): „vyber náhodný bod a jdi k němu" působí trhaně a uměle. Přirozenost dodal smooth šum (OpenSimplex [(6:13)](https://www.youtube.com/watch?v=6BrZryMz-ac&t=373s)) řídící *pozvolné* zatáčení — a protože hodnoty šumu tíhnou k nule, entita většinu času jde rovně a jen občas plavně změní kurz. Návrat ke spawn pointu není tvrdá hranice, ale váha rostoucí se vzdáleností [(6:41)](https://www.youtube.com/watch?v=6BrZryMz-ac&t=401s) — hranici nejde vidět, a proto působí přirozeně.

> **Pozn.:** Bonusová lekce o emergenci: když autor zapnul faction systém, nepřátelé se začali mlátit mezi sebou v „battle royale" [(7:25)](https://www.youtube.com/watch?v=6BrZryMz-ac&t=445s) — a ten nečekaně skvělý pohled ho přesvědčil přitlačit na plánovaný pet-taming systém [(7:33)](https://www.youtube.com/watch?v=6BrZryMz-ac&t=453s). Systémy, které spolu mluví, občas vygenerují design zadarmo — stojí za to si takových nehod všímat, místo je „opravovat".

**Souvislosti:** [Jak udělat cokoli zábavným](zabava.md) · [Základy nepřátelské AI](../praxe/ai-zaklady.md) · [Rejstřík: context steering](../rejstrik.md#context-steering) · [Rejstřík: game feel](../rejstrik.md#game-feel) · [Bojové role v Lords of the Fallen](../praxe/ai-ve-velkem.md#kdo-utoci-a-kdo-ceka-aggro-skore-a-bojove-role) *(útočník, kryt a divák jako plán pohybu skupiny)*

---

## Imerze = svět, který na tebe odpovídá

**Zdroj:** [This Made My Game 10X More IMMERSIVE](https://www.youtube.com/watch?v=4t3B5brFui4) · [Its Rascal](https://www.youtube.com/channel/UCjwTasXewi5CRFi564vrf0g) · ~10 min, devlog (hra o balvanu)

**Shrnutí:** Autor dělá hru, kde hráč *je* velký těžký balvan — a chce, aby se tak i cítil [(0:08)](https://www.youtube.com/watch?v=4t3B5brFui4&t=8s). Devlog o trávě je ve skutečnosti devlog o imerzi: krásná tráva nestačí; imerze se láme přesně v momentě, kdy stébla projdou balvanem, jako by neexistoval. Svět je skutečný teprve tehdy, když na hráče reaguje.

### Rozpad myšlenky

Stavba trávy je katalog levných triků místo drahé simulace: hloubku místo stínů (tisíce stínů stébel by „zapálily grafiku") dodá **barevný gradient** [(2:04)](https://www.youtube.com/watch?v=4t3B5brFui4&t=124s); rozmístění řeší foliage brush a logika landscape materiálu — cesta se sama vyseká do trávy [(3:06)](https://www.youtube.com/watch?v=4t3B5brFui4&t=186s); vyšší trsy nejsou větší modely, ale **world position offset** — textura říká vrcholům stébel, o kolik se posunout nahoru [(3:41)](https://www.youtube.com/watch?v=4t3B5brFui4&t=221s), plus třetí barva do žluta pro vyšší partie [(4:22)](https://www.youtube.com/watch?v=4t3B5brFui4&t=262s); vítr je vlnění + ohyb + pásy poryvů z šumu panující krajinou [(5:07)](https://www.youtube.com/watch?v=4t3B5brFui4&t=307s). Všechno fake, všechno funguje.

Pointa přichází po „hotovo": při hraní stébla procházejí balvanem a imerze je pryč [(5:49)](https://www.youtube.com/watch?v=4t3B5brFui4&t=349s). Fyzika na 30 000 stéblech je mimo diskusi [(6:01)](https://www.youtube.com/watch?v=4t3B5brFui4&t=361s) — řešení je znovu trik, tentokrát krásný: barva jako směr. RGB kanály jsou tři čísla, stejně jako směrový vektor [(6:55)](https://www.youtube.com/watch?v=4t3B5brFui4&t=415s); particle pod balvanem + kamera shora, která ho každý frame renderuje do textury [(7:18)](https://www.youtube.com/watch?v=4t3B5brFui4&t=438s) → materiál trávy si z textury přečte, kudy balvan jede, a stébla se ohnou od něj. Druhý particle systém nechává stopu [(7:56)](https://www.youtube.com/watch?v=4t3B5brFui4&t=476s), takže zválcovaná tráva **zůstane ležet** [(7:50)](https://www.youtube.com/watch?v=4t3B5brFui4&t=470s) — a hráč za sebou kreslí cestičky [(8:46)](https://www.youtube.com/watch?v=4t3B5brFui4&t=526s).

Obecná lekce pod tím: imerze není počet polygonů, ale **smyčka akce → otisk**. Hráč něco udělá a svět si to pamatuje — byť jen ohnutou trávou. A skoro vždycky je levnější to předstírat (render target, offsety, barvy) než simulovat; hráč rozdíl nepozná, frame rate ano.

> **Pozn.:** Stejný vzorec „poslední 10 % dělá celý dojem" jako u [over-polishingu](produktivita.md#investice-bez-validace-lesteni-systemy-a-optimalizace-predem) — ale tady jde o jádro fantazie hry („jsi balvan"), takže to *je* to správné místo pro hyper-polish. Kritérium zůstává: leštit, co sytí hlavní fantazii, ne co je zrovna po ruce.

**Souvislosti:** [Nápad: core DNA a emoce](napad.md#core-dna-a-ctyri-emoce) · [Žrouti času: over-polishing](produktivita.md#investice-bez-validace-lesteni-systemy-a-optimalizace-predem) · [Materiály](../praxe/materialy.md) · [PCG: základy a nástroje](../praxe/pcg-zaklady.md) · [Rejstřík: game feel](../rejstrik.md#game-feel) · [Hudba a zvuk: sound design ve hře](../hudba/sound-design-ve-hre.md) *(zvuk jako vrstva imerze)*

---

## Katalog juice: deset detailů, které prodávají tutéž mechaniku

**Zdroj:** [10 Ways to Improve Game Feel](https://www.youtube.com/watch?v=qCj9CZoAvFY) · [Design Diary](https://www.youtube.com/channel/UCrIZMp3lvblamWCg21LcPvg) · ~11 min, praktický katalog

**Shrnutí:** Video staví na demu od Sébastiena Bénarda (Deepnight Games, designér Dead Cells), kde jde jednotlivé „juice" detaily vypínat a zapínat — **stejné mechaniky, stejná zbraň, stejný počet kulek**, a bez detailů je to „dull and lifeless" [(0:02)](https://www.youtube.com/watch?v=qCj9CZoAvFY&t=2s). Deset tipů tady skládáme do čtyř mechanismů: váha akcí, stopy ve světě, čitelnost zásahů a střídmost.

### Rozpad myšlenky

**Váha akcí:** postava se při výstřelu otřese a pomalu sune vzad — kulky najednou mají zpětný ráz [(0:48)](https://www.youtube.com/watch?v=qCj9CZoAvFY&t=48s); rozptyl střel dodá zbrani realističnost [(1:35)](https://www.youtube.com/watch?v=qCj9CZoAvFY&t=95s); **squash & stretch** dělá ze skoku pružinu a z nepřátel „želé", které na zásah reaguje [(6:54)](https://www.youtube.com/watch?v=qCj9CZoAvFY&t=414s); dash se stejnou rychlostí i vzdáleností *působí* rychlejší, když k němu přidáš deformaci a particles [(7:41)](https://www.youtube.com/watch?v=qCj9CZoAvFY&t=461s) — pocit se vyrábí kolem čísel, ne v nich. A **screen shake** při dopadu z výšky prodá tíhu zbroje [(8:28)](https://www.youtube.com/watch?v=qCj9CZoAvFY&t=508s).

**Stopy ve světě:** particles (trail střely, muzzle flash) nechávají po akci chvilkové stopy — hráč *vidí, že má na svět vliv* [(2:22)](https://www.youtube.com/watch?v=qCj9CZoAvFY&t=142s); dopad na povrch (záblesk + odletující kusy zdi) autor vypichuje jako nejpodceňovanější detail vůbec [(4:34)](https://www.youtube.com/watch?v=qCj9CZoAvFY&t=274s) — kulka nesmí prostě zmizet; světelné efekty (halo kolem výstřelu, flash) ukotvují akce do světa [(3:08)](https://www.youtube.com/watch?v=qCj9CZoAvFY&t=188s).

**Čitelnost zásahů** [(5:20)](https://www.youtube.com/watch?v=qCj9CZoAvFY&t=320s): nepřítel bez reakce = hráč v rychlé hře ani neví, že trefil. Flash při zásahu, knockback škálovaný zbraní (dýka málo, kopí hodně — juice zároveň *diferencuje mechaniky*), krev, která ulpívá — a hlavně **mrtvoly**: odlétnou, dopadnou, zůstanou (nebo explodují v částice); „něco se stát musí, nepřítel nesmí jen zmizet" [(6:06)](https://www.youtube.com/watch?v=qCj9CZoAvFY&t=366s).

**Střídmost:** světla i screen shake umí dezorientovat; u shake navíc hrozí motion sickness — patří do nastavení jako vypínatelná volba [(8:28)](https://www.youtube.com/watch?v=qCj9CZoAvFY&t=508s).

> **Pozn.:** Juice je feedback vrstva z [desatera](zaklady.md#desatero-principu-jako-checklist-kostra-puls-duse) dovedená k řemeslu — a teoreticky je to čistý [signal-to-noise](zabava.md#flow-kanal-je-pasmo-nejlepsiho-signalu): každý detail říká hráči, co právě udělal a že to svět zaznamenal. Půlka juice je mimochodem zvuk — viz [sound design ve hře](../hudba/sound-design-ve-hre.md). A pozor na pořadí: juice se leští na jádru, které už baví — jinak je to [over-polishing](produktivita.md#investice-bez-validace-lesteni-systemy-a-optimalizace-predem).

**Souvislosti:** [Základy: hračky](zaklady.md#engagement-hracky-spojene-zajimavymi-rozhodnutimi) · [Vizuální komunikace: mechaniky musí být vidět](vizualni-komunikace.md#mechaniky-funguji-jen-tehdy-kdyz-je-hrac-vidi) *(tytéž triky jako podmínka hratelnosti, ne jen příjemnosti)* · [Kroky a povrchy](../praxe/footsteps.md) · [Rejstřík: Juice](../rejstrik.md#juice) · [Rejstřík: Squash & stretch](../rejstrik.md#squash-stretch) · [Finisher bez střihu](../praxe/cutsceny.md#finisher-bez-strihu-sekvence-ktera-se-prehraje-kolem-hrace) *(kamera a otřes jako juice)* · [Souboj v UE: pět potvrzení rány](../praxe/souboj.md#rana-ktere-hrac-uveri-pet-potvrzeni-kazde-o-necem-jinem) *(tytéž vrstvy postavené v Blueprintech)*

---

## Combat je rytmus: každý útok má účel a placeholder je nástroj

**Zdroj:** [INDIE Game DevLog - Why GOOD Combat Is So HARD To Make](https://www.youtube.com/watch?v=NYqyAL7FKYg) · [SILKROAD Project](https://www.youtube.com/channel/UC2t1iUBVNHcK9v1h7E4Q8Ag) · ~15 min, devlog sólo vývojáře (Guedin)

**Shrnutí:** Po roce stavění základů combat systému (companion, větvení komb, reakce nepřátel, juggle) přišel měsíc, kdy se z prototypu měla stát zábava — a nejvíc času nesežraly animace, ale **rytmus**: aby útoky plynuly, každé kombo mělo účel a hráč dělal rozhodnutí místo mačkání [(0:01)](https://www.youtube.com/watch?v=NYqyAL7FKYg&t=1s). Devlog je vzácně upřímný záznam toho, jak se „objektivně lepší" změna umí pocitově nevyplatit.

### Rozpad myšlenky

**Každý útok má účel** [(2:27)](https://www.youtube.com/watch?v=NYqyAL7FKYg&t=147s): damage? launcher? pobídka vpletát companiona? odhoz při obklíčení? gap closer? bezpečný disengage? „Cool animace nedělá combat zajímavým — každý útok má vybízet k jinému rozhodnutí." Stejná logika platí pro celé combo větve [(7:10)](https://www.youtube.com/watch?v=NYqyAL7FKYg&t=430s): dlouhá s velkým damage, ale zranitelná; jiná zavírá vzdálenost; jiná končí úkrokem vzad. Čím víc *různých problémů* jednotlivé routy řeší, tím méně repetitivní boj je — je to [princip „ale"](zaklady.md#engagement-hracky-spojene-zajimavymi-rozhodnutimi) přeložený do útoků.

**Rytmus jako design space** [(3:14)](https://www.youtube.com/watch?v=NYqyAL7FKYg&t=194s): u juggle komba autor **záměrně nechává mezeru** mezi dvěma útoky hrdiny — kdo rytmus rozpozná, vloží do ní útok companiona a udrží nepřítele ve vzduchu. Mashující hráč projde; hráč, který se naučí tempo vlastních komb, je odměněn delšími sekvencemi. Nadstavba: charge útoky (commit ve správný moment místo rychlosti prstů [(7:59)](https://www.youtube.com/watch?v=NYqyAL7FKYg&t=479s)) a **anime finišery bez vlastního tlačítka** [(8:45)](https://www.youtube.com/watch?v=NYqyAL7FKYg&t=525s) — spustíš je jen tím, že jsi kombo řídil správně: nabitý útok na jugglovaného nepřítele. Mistrovství odměněné podívanou, ne QTE.

**Placeholder jako nástroj, dvakrát:** animace prvního roku „nikdy neměly zůstat" — byly to stavební bloky pro prototypování mechanik a svou práci odvedly [(0:50)](https://www.youtube.com/watch?v=NYqyAL7FKYg&t=50s). A nové animace dělá autor **záměrně horší** [(4:46)](https://www.youtube.com/watch?v=NYqyAL7FKYg&t=286s): minimum keyframes, základní pózy — protože ladění timingu znamená hýbat keyframy pořád dokola a vyleštěná animace by každou iteraci zdražila. „Nejtěžší je se udržet." Vyplatilo se hned: zpomalení útoků kvůli decision-space *mechanicky* fungovalo — a **zabilo intenzitu** [(5:35)](https://www.youtube.com/watch?v=NYqyAL7FKYg&t=335s); „změna může být objektivně lepší a celkový pocit horší." Protože je vše placeholder, drastický návrat nebolí. Bonusová lekce z leštění finišerů [(10:21)](https://www.youtube.com/watch?v=NYqyAL7FKYg&t=621s): u anime stylu rozhodují **silné pózy a timing víc než hladkost** — a cinematiky-kdekoli si vynutily kompromis „postavy se po finišeru vrátí přesně tam, kde začaly, kolize dočasně vypnuté, kamera triky skryje" [(13:37)](https://www.youtube.com/watch?v=NYqyAL7FKYg&t=817s): „dokonalost není cíl — nejlepší řešení vytváří nejméně problémů."

> **Pozn.:** Meta-věta devlogu stojí za vypíchnutí [(14:26)](https://www.youtube.com/watch?v=NYqyAL7FKYg&t=866s): „na začátku jsem stavěl systémy, aby fungovaly; teď se ptám, jestli jsou zábavné — a je to zajímavější fáze. Balanc feature trvá déle než její implementace." To je přesně přechod z [pre-produkce do produkce](obtiznost.md#challenge-je-co-difficulty-je-kolik) viděný zevnitř.

**Souvislosti:** [Obtížnost a výzva](obtiznost.md) · [MM systémy: combat přes choosery](../praxe/mm-systemy.md) · [Zábava: balanc rozhodnutí](zabava.md#balanc-bez-ctvercove-diry-co-dela-rozhodnuti-zabavnym) · [Rejstřík: Juice](../rejstrik.md#juice)

---

## Celeste: křivky v snímcích a hrst tichých úlev

**Zdroj:** [Why Does Celeste Feel So Good to Play?](https://www.youtube.com/watch?v=yorTG9at90g) · [Game Maker's Toolkit](https://www.youtube.com/channel/UCqJ-Xo29CKyLTjn6z2XwYAw) · ~18 min, rozbor s rozhovorem s autory

**Shrnutí:** Mark Brown rozebral kód Celeste, prošel animaci po snímcích a promluvil si s oběma autory — a výsledkem je nejlepší dostupný důkaz, že „pocit ze hry" je **měřitelná věc v konkrétních číslech**. Madeline zrychlí na plnou rychlost za **šest snímků** a zastaví za **tři**; skočí do výšky **tří svých těl**. K tomu **nespočet tichých úlev** v kódu, o kterých hráč neví. Věta, která to celé shrnuje a dá se použít jako pravidlo: **pracuj se záměrem hráče, ne s přesnou simulací stisků tlačítek.**

### Rozpad myšlenky

**Běh se rozpadá na tři čísla** [(1:43)](https://www.youtube.com/watch?v=yorTG9at90g&t=103s): zrychlení, maximální rychlost, zpomalení. A obě křivky mají svoje selhání na obou koncích — **krátké** dělají postavu strnulou a robotickou (Mega Man 11), **dlouhé** těžkopádnou při rozjezdu (Super Meat Boy) a klouzavou při brzdění (Super Mario Bros 3, kde Mario *„občas působí, jako by běhal po ledu"*).

Madeline sedí na krátkém konci, ale ne na kraji [(2:29)](https://www.youtube.com/watch?v=yorTG9at90g&t=149s): **šest snímků na plnou rychlost** (asi 4× rychleji než Meat Boy) a **tři snímky do zastavení** (asi 9× rychleji než Mario v New Super Mario Bros U). Brownovo zdůvodnění je to zajímavé: čísla jsou *„dost vysoká na to, aby působila lidsky a znemožnila obří skoky z místa — a dost nízká na to, aby postava dělala skoro okamžitě, co jí řekneš."* K tomu **nízká maximální rychlost a žádné tlačítko sprintu**: dost rychle na plynulost, dost pomalu na kontrolu.

**Skok se měří ve výškách těla** [(3:18)](https://www.youtube.com/watch?v=yorTG9at90g&t=198s) — Mario doskočí do čtyřnásobku vlastní výšky, Meat Boy do šestinásobku, **Madeline do trojnásobku**, což je jeden z nejnižších v žánru. Zajímavější než výška je ale rozdělení oblouku: **rychle nahoru, rychle dolů, ale se slušnou dobou setrvání nahoře**, aby si hráč stihl srovnat dopad. A dvě věci navíc, které vypadají jako detail a rozhodují [(4:08)](https://www.youtube.com/watch?v=yorTG9at90g&t=248s): **okamžitá změna směru bez smyku** a **obrovské tření ve vzduchu**, takže puštění páčky ve výskoku znamená skoro svislý pád — přesně to, co potřebuješ, když míříš na malou plošinku.

**Kamera je součást pocitu, ne obalu** [(4:55)](https://www.youtube.com/watch?v=yorTG9at90g&t=295s). Celeste je oddálená a místnosti jsou často **v jednom statickém záběru**. Důsledek: obraz sebou necuká, a *„když je Madeline jediná věc, která se hýbe, je snazší ji dostat tam, kam chceš."* Autoři za to zaplatili detailem v grafice a podle Browna to stálo za to.

**Tiché úlevy** jsou to, kvůli čemu se ta myšlenka vyplatí znát celá [(9:38)](https://www.youtube.com/watch?v=yorTG9at90g&t=578s). Celeste je tvrdá hra, která hráči **soustavně pomáhá**, aniž by to přiznala: **coyote time** (skok pár snímků po opuštění hrany — jméno vzniklo mimochodem, autoři přiznávají, že ho vymysleli hráči) · **dash do rohu neodrazí**, ale obeplachtí hranu · **bodce mají menší hitbox než grafiku** · **pozdní stisk u pohyblivých bloků** setrvačnost přesto započítá · **climb jump s odklonem od zdi** se změní na wall jump a **vrátí vydrženou stamina** · a **skok stisknutý těsně před dopadem** se provede při dopadu.

Zdůvodnění od programátora hry je nejlepší formulace toho problému, jakou známe [(10:26)](https://www.youtube.com/watch?v=yorTG9at90g&t=626s): *„je nepříjemné, když zmáčkneš skok snímek předtím, než se dotkneš země, a nestane se nic. Působí to, jako by hra chybovala — jako by ti vstup sežrala."* A poznámka, která ruší obvyklou námitku „to je berlička pro slabé hráče" [(11:12)](https://www.youtube.com/watch?v=yorTG9at90g&t=672s): **profesionálové ty snímky navíc naopak vyžívají** — tři snímky milosti umí speedrunner použít na skok, který „neměl" vyjít. Casual hráč z toho má lepší pocit, expert vyšší strop.

**Jak k těm číslům autoři došli** [(5:43)](https://www.youtube.com/watch?v=yorTG9at90g&t=343s), protože se to často romantizuje: *„hodně z toho byla intuice z toho, že jsme udělali spoustu plošinovek"* plus experimentování a **sledování testerů** — *„aha, tohle nefungovalo, jak jsme mysleli."* A výslovně: čísla se během vývoje měnila, i výrazně.

**A rada, kterou autoři dávají na konec, je zároveň nejlepší test** [(13:38)](https://www.youtube.com/watch?v=yorTG9at90g&t=818s): *„ať se moment po momentu cítí dobře — aby si člověk mohl sednout s ovladačem, místnost může být prázdná, a jen pohyb té postavy je zábavný."* Druhý autor to doplňuje větou, která platí i mimo plošinovky: **„ať je prostě zábava být tou postavou."**

> **Pozn.:** Nejcennější kus rozhovoru je ale metodologický a týká se celého vývoje [(14:27)](https://www.youtube.com/watch?v=yorTG9at90g&t=867s): dostaneš postavu do stavu „ujde to", pak **potřebuješ levely, abys ji mohl testovat** — a testování ti řekne, že postavu musíš změnit, což znamená přepsat dvacet levelů. Autorova formulace stojí za zapamatování: *„musíš nechat různé části hry měnit jiné části a nechat hru pomalu odhalit, čím chce být."* K tomu ochota zahodit práci: *„i když práci vyhazuješ, je to učení, které nakonec dělá hru lepší — je to práce směrem k dokončení, i když se neprojeví jako obsah."* To je totéž, co v knihovně stojí za [iterační spirálou](prototypovani.md#iteracni-spirala-ke-stredu-nevede-rychly-pruh). Kdo chce ty triky rovnou naprogramovat, má je rozebrané v [godotí kapitole o skoku](../godot/animace-a-pohyb.md#skok-ktery-rozumi-tomu-co-hrac-chtel).

**Souvislosti:** [Katalog juice](#katalog-juice-deset-detailu-ktere-prodavaji-tutez-mechaniku) *(vizuální vrstva téhož)* · [Combat je rytmus](#combat-je-rytmus-kazdy-utok-ma-ucel-a-placeholder-je-nastroj) · [Godot: skok, který rozumí hráči](../godot/animace-a-pohyb.md#skok-ktery-rozumi-tomu-co-hrac-chtel) *(implementace týchž úlev)* · [Prototypování: iterační spirála](prototypovani.md#iteracni-spirala-ke-stredu-nevede-rychly-pruh) · [Obtížnost a výzva](obtiznost.md) · [Rejstřík: Coyote time](../rejstrik.md#coyote-time) · [Rejstřík: Input buffering](../rejstrik.md#input-buffering) · [Rejstřík: Skill ceiling](../rejstrik.md#skill-ceiling)
