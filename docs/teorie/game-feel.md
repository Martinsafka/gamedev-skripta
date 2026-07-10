# Game feel a imerze: dva devlogy o pocitu ze hry

Dva praktické devlogy o tomtéž cíli z opačných stran: aby hra *působila* — aby souboj byl živý a svět skutečný. První řeší pohyb nepřátel (nuda vs. tanec), druhý reakci prostředí na hráče (kulisa vs. svět). Společný jmenovatel: pocit nevzniká z čísel v tabulkách, ale z pohybu a odezvy — a skoro vždycky je to chytrý fake, ne simulace.

---

## Souboj dělá zábavným pohyb nepřátel, ne jejich statistiky

**Zdroj:** [The Trick I Used to Make Combat Fun! | Devlog](https://www.youtube.com/watch?v=6BrZryMz-ac) · [Game Endeavor](https://www.youtube.com/channel/UCLweX1UtQjRjj7rs_0XQ2Eg) · ~8 min, devlog (open-world RPG)

**Shrnutí:** Nepřátelé, kteří na hráče běží po přímce, jsou placeholder, ne souboj. Autor předělal pohyb kostlivců na context steering — vážené rozhodování mezi směry — a přidal chování „přibliž se, krouž, drž odstup". Výsledek: tester u hrstky kostlivců dobrovolně strávil hodinu. Stejná mechanika, stejné dmg — jiný pohyb.

### Rozpad myšlenky

Cesta k řešení je poučná i s odbočkami. Klasické **steering behaviors** (boids) [(0:56)](https://www.youtube.com/watch?v=6BrZryMz-ac&t=56s) skládají jednoduché síly (jdi tam, drž se dál od…), jenže protichůdné vektory se umí vyrušit: nepřítel má utéct, za zády má zeď — a tak jen stojí a čeká na smrt [(1:34)](https://www.youtube.com/watch?v=6BrZryMz-ac&t=94s). **Context steering** [(1:58)](https://www.youtube.com/watch?v=6BrZryMz-ac&t=118s) problém řeší tím, že si drží *ohodnocení všech směrů* (přes dot product — jak moc směr souhlasí s tím kýženým [(3:10)](https://www.youtube.com/watch?v=6BrZryMz-ac&t=190s)) a vybírá nejlepší *proveditelný*: když je nejlepší směr zablokovaný, vezme druhý nejlepší, místo aby zamrzl.

Zábavnost pak vzniká tvarováním vah [(4:17)](https://www.youtube.com/watch?v=6BrZryMz-ac&t=257s): zblízka slábne váha „k cíli" a nastupuje preference pohybu do stran → kostlivci krouží kolem hráče, nabíhají a odskakují. (S komickou epizodou: dokonalé kroužení vyrobilo „Newtonovo kyvadlo z kostlivců" [(0:00)](https://www.youtube.com/watch?v=6BrZryMz-ac&t=0s) — spravil rozhozený odstup.) Poslední kaz byl jitter — nepřátelé se přetlačovali v tug-o-war a cukali sebou [(4:54)](https://www.youtube.com/watch?v=6BrZryMz-ac&t=294s); vyřešilo ho odpuzování pod úhlem místo přímo od souseda. Výsledek [(5:18)](https://www.youtube.com/watch?v=6BrZryMz-ac&t=318s): souboj, který baví i autora — a hodinový playtest z vlastní vůle.

Druhá půlka téže lekce je **wandering** [(5:32)](https://www.youtube.com/watch?v=6BrZryMz-ac&t=332s): „vyber náhodný bod a jdi k němu" působí trhaně a uměle. Přirozenost dodal smooth šum (OpenSimplex [(6:13)](https://www.youtube.com/watch?v=6BrZryMz-ac&t=373s)) řídící *pozvolné* zatáčení — a protože hodnoty šumu tíhnou k nule, entita většinu času jde rovně a jen občas plavně změní kurz. Návrat ke spawn pointu není tvrdá hranice, ale váha rostoucí se vzdáleností [(6:41)](https://www.youtube.com/watch?v=6BrZryMz-ac&t=401s) — hranici nejde vidět, a proto působí přirozeně.

> **Pozn.:** Bonusová lekce o emergenci: když autor zapnul faction systém, nepřátelé se začali mlátit mezi sebou v „battle royale" [(7:25)](https://www.youtube.com/watch?v=6BrZryMz-ac&t=445s) — a ten nečekaně skvělý pohled ho přesvědčil přitlačit na plánovaný pet-taming systém [(7:33)](https://www.youtube.com/watch?v=6BrZryMz-ac&t=453s). Systémy, které spolu mluví, občas vygenerují design zadarmo — stojí za to si takových nehod všímat, místo je „opravovat".

**Souvislosti:** [Jak udělat cokoli zábavným](zabava.md) · [Základy nepřátelské AI](../praxe/ai-zaklady.md) · [Rejstřík: context steering](../rejstrik.md#context-steering) · [Rejstřík: game feel](../rejstrik.md#game-feel)

---

## Imerze = svět, který na tebe odpovídá

**Zdroj:** [This Made My Game 10X More IMMERSIVE](https://www.youtube.com/watch?v=4t3B5brFui4) · [Its Rascal](https://www.youtube.com/channel/UCjwTasXewi5CRFi564vrf0g) · ~10 min, devlog (hra o balvanu)

**Shrnutí:** Autor dělá hru, kde hráč *je* velký těžký balvan — a chce, aby se tak i cítil [(0:08)](https://www.youtube.com/watch?v=4t3B5brFui4&t=8s). Devlog o trávě je ve skutečnosti devlog o imerzi: krásná tráva nestačí; imerze se láme přesně v momentě, kdy stébla projdou balvanem, jako by neexistoval. Svět je skutečný teprve tehdy, když na hráče reaguje.

### Rozpad myšlenky

Stavba trávy je katalog levných triků místo drahé simulace: hloubku místo stínů (tisíce stínů stébel by „zapálily grafiku") dodá **barevný gradient** [(2:04)](https://www.youtube.com/watch?v=4t3B5brFui4&t=124s); rozmístění řeší foliage brush a logika landscape materiálu — cesta se sama vyseká do trávy [(3:06)](https://www.youtube.com/watch?v=4t3B5brFui4&t=186s); vyšší trsy nejsou větší modely, ale **world position offset** — textura říká vrcholům stébel, o kolik se posunout nahoru [(3:41)](https://www.youtube.com/watch?v=4t3B5brFui4&t=221s), plus třetí barva do žluta pro vyšší partie [(4:22)](https://www.youtube.com/watch?v=4t3B5brFui4&t=262s); vítr je vlnění + ohyb + pásy poryvů z šumu panující krajinou [(5:07)](https://www.youtube.com/watch?v=4t3B5brFui4&t=307s). Všechno fake, všechno funguje.

Pointa přichází po „hotovo": při hraní stébla procházejí balvanem a imerze je pryč [(5:49)](https://www.youtube.com/watch?v=4t3B5brFui4&t=349s). Fyzika na 30 000 stéblech je mimo diskusi [(6:01)](https://www.youtube.com/watch?v=4t3B5brFui4&t=361s) — řešení je znovu trik, tentokrát krásný: barva jako směr. RGB kanály jsou tři čísla, stejně jako směrový vektor [(6:55)](https://www.youtube.com/watch?v=4t3B5brFui4&t=415s); particle pod balvanem + kamera shora, která ho každý frame renderuje do textury [(7:18)](https://www.youtube.com/watch?v=4t3B5brFui4&t=438s) → materiál trávy si z textury přečte, kudy balvan jede, a stébla se ohnou od něj. Druhý particle systém nechává stopu [(7:56)](https://www.youtube.com/watch?v=4t3B5brFui4&t=476s), takže zválcovaná tráva **zůstane ležet** [(7:50)](https://www.youtube.com/watch?v=4t3B5brFui4&t=470s) — a hráč za sebou kreslí cestičky [(8:46)](https://www.youtube.com/watch?v=4t3B5brFui4&t=526s).

Obecná lekce pod tím: imerze není počet polygonů, ale **smyčka akce → otisk**. Hráč něco udělá a svět si to pamatuje — byť jen ohnutou trávou. A skoro vždycky je levnější to předstírat (render target, offsety, barvy) než simulovat; hráč rozdíl nepozná, frame rate ano.

> **Pozn.:** Stejný vzorec „poslední 10 % dělá celý dojem" jako u [over-polishingu](produktivita.md#investice-bez-validace-lesteni-systemy-a-optimalizace-predem) — ale tady jde o jádro fantazie hry („jsi balvan"), takže to *je* to správné místo pro hyper-polish. Kritérium zůstává: leštit, co sytí hlavní fantazii, ne co je zrovna po ruce.

**Souvislosti:** [Nápad: core DNA a emoce](napad.md#core-dna-a-ctyri-emoce) · [Žrouti času: over-polishing](produktivita.md#investice-bez-validace-lesteni-systemy-a-optimalizace-predem) · budoucí praxe témata „Materiály a VFX", „PCG a procedurální svět" · [Rejstřík: game feel](../rejstrik.md#game-feel)
