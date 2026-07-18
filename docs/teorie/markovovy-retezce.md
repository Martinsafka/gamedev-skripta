# Markovovy řetězce a Monte Carlo: matematika, která predikuje (skoro) vše

Jedna hádka dvou ruských matematiků z roku 1905 dala světu nástroj, který dnes sedí uvnitř Googlu, jaderné fyziky, prediktivní klávesnice i LLM: **Markovův řetěz** — pravděpodobnost pro události, které na sobě závisí. Veritasium vypráví celý příběh; pro tahle skripta je podstatné, že stavy s pravděpodobnostními přechody a simulace místo výpočtu jsou přesně to, z čeho se staví AI chování, procedurální generace i balanc herní ekonomiky.

---

## Řetěz místo nezávislosti: pravděpodobnost závislých událostí

**Zdroj:** [The Strange Math That Predicts (Almost) Anything](https://www.youtube.com/watch?v=KZeIEiBrT_w) · [Veritasium](https://www.youtube.com/channel/UCHnyfMqiRRG1u-2MsSQLbXA) · ~33 min, dokumentární esej

**Shrnutí:** Zákon velkých čísel (průměr se s počtem pokusů blíží očekávané hodnotě) byl 200 let dokázaný jen pro **nezávislé** události [(2:19)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=139s). Andrej Markov zkonstruoval protipříklad z Puškinova *Evžena Oněgina*: písmena textu na sobě prokazatelně závisí, a přesto jejich poměr konverguje [(7:46)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=466s). Vynález, kterým to dokázal — stavy a přechodové pravděpodobnosti — je Markovův řetěz.

### Rozpad myšlenky

Kontext hádky stojí za převyprávění: carista Pavel Nekrasov tvrdil, že když sociální statistiky (sňatky, kriminalita) konvergují, musí být rozhodnutí za nimi nezávislá — tedy „vědecký důkaz" svobodné vůle [(3:52)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=232s). Markov („Andrej Zuřivý", ateista a pedant na rigor [(0:46)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=46s)) obrátil implikaci v prach tím, že našel **závislý** systém, který konverguje taky.

Experiment [(5:27)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=327s): prvních 20 000 písmen *Oněgina* bez mezer; 43 % samohlásek. Kdyby písmena byla nezávislá, pár samohláska–samohláska by měl četnost 0,43² ≈ 18 % — reálně je to 6 % [(6:13)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=373s). Písmena tedy závisí na předchůdci. Markov pak postavil „predikční stroj" [(6:13)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=373s): dva kroužky-**stavy** (samohláska, souhláska), šipky-**přechody** s pravděpodobnostmi spočítanými z textu (P(V→V) = 0,06/0,43 ≈ 13 %; šipky z jednoho stavu se sčítají na 1 [(7:00)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=420s)). Když stroj necháš běžet s náhodnými čísly, poměr stavů konverguje přesně k napočítaným 43/57 [(7:46)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=466s) — zákon velkých čísel bez nezávislosti. Markov uzavřel paper posledním rýpnutím: „svobodná vůle není k pravděpodobnosti potřeba" [(8:34)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=514s).

Klíčová vlastnost, kterou z toho svět zdědil: řetěz je **memoryless** [(28:55)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=1735s). Systémy jako počasí, epidemie nebo text mají nekonečně dlouhou historii — ale pro predikci dalšího kroku stačí **současný stav**. To je brutální zjednodušení, které dělá nemodelovatelné modelovatelným; citát z videa: „řešení problému často znamená uvařit vhodný Markovův řetěz" [(28:55)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=1735s).

> **Pozn.:** Zní to povědomě? **State machine s pravděpodobnostními přechody je Markovův řetěz.** NPC, které z Idle přechází do Patrol s 70 % a do Alert s 30 %, generátor počasí ve hře, drop tabulky vázané na předchozí drop („pity systém" je řetěz se stavovou pamětí posledních tahů) — všechno jsou markovovské konstrukce, jen se jim tak v enginu neříká.

**Souvislosti:** [State Trees](../praxe/state-trees.md) — stavové stroje v UE · [Rejstřík: Markovův řetěz](../rejstrik.md#markovuv-retez) · [Rejstřík: State machine](../rejstrik.md#state-machine)

---

## Monte Carlo: zahraj to tisíckrát místo výpočtu

**Zdroj:** [The Strange Math That Predicts (Almost) Anything](https://www.youtube.com/watch?v=KZeIEiBrT_w) · [Veritasium](https://www.youtube.com/channel/UCHnyfMqiRRG1u-2MsSQLbXA) · stejné video, část o Manhattan Projectu

**Shrnutí:** Stanisław Ulam se při rekonvalescenci ptal, jaká je šance vyhrát rozdané Solitaire — analyticky beznadějné (52! ≈ 8·10⁶⁷ her), tak ho napadlo: **zahraj stovky her a počítej výhry** [(11:42)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=702s). S von Neumannem pak stejný princip — simulace mnoha náhodných běhů místo přesného výpočtu — použili na neutrony v jaderné bombě. Metoda dostala jméno Monte Carlo a je to dodnes nejpraktičtější odpověď na systémy, které neumíš spočítat.

### Rozpad myšlenky

Von Neumann viděl háček [(12:31)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=751s): karty jsou mezi hrami nezávislé, ale chování neutronu závisí na jeho poloze a historii — takže vzorkovat izolované náhodné výsledky nestačí, musíš simulovat **řetěz událostí**. Neutron jako Markovův řetěz [(13:17)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=797s): stavy scatter (šipka zpátky na sebe), únik/absorpce (konec řetězu), štěpení (2–3 nové neutrony = nové řetězy); přechodové pravděpodobnosti závisí na rychlosti a poloze [(14:05)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=845s). ENIAC to běžel stovkami opakování a histogram průměrného **multiplikačního faktoru k** dal odpověď, kterou nikdo neuměl spočítat rovnicemi: k < 1 reakce vyhasne, k = 1 se udrží, k > 1 roste exponenciálně — bomba [(14:52)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=892s). Jméno vymyslel Ulam podle kasina, kde hrával jeho strýc [(15:39)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=939s).

Princip k zapamatování: **Monte Carlo aproximuje řešení, které analyticky neexistuje nebo se nevyplatí** — za cenu výpočetního času a statistické (ne absolutní) jistoty [(15:39)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=939s).

> **Pozn.:** Pro herního designéra je tohle pracovní nástroj, ne historie. Ekonomiku, drop raty nebo souboj **nemusíš řešit vzorcem — nasimuluj 10 000 běhů** a podívej se na histogram: jak dlouho trvá průměrnému hráči farma na meč? V kolika procentech běhů hráč zbankrotuje? Skript na pár řádků odpoví líp než tabulka průměrů, protože ukáže i rozptyl a chvosty. Je to totéž, co [ekonomika na papíře](prototypovani.md#ekonomiku-si-zahraj-na-papire-nez-ji-naprogramujes) — jen s počítačem místo kostky.

**Souvislosti:** [Prototypování](prototypovani.md) · [Rejstřík: Monte Carlo metoda](../rejstrik.md#monte-carlo-metoda)

---

## Od PageRanku k LLM: řetězy, na kterých stojí internet

**Zdroj:** [The Strange Math That Predicts (Almost) Anything](https://www.youtube.com/watch?v=KZeIEiBrT_w) · [Veritasium](https://www.youtube.com/channel/UCHnyfMqiRRG1u-2MsSQLbXA) · stejné video, závěrečná část

**Shrnutí:** Google vyhrál válku vyhledávačů algoritmem, který je Markovův řetěz: **PageRank** modeluje web jako stavy (stránky) a přechody (odkazy) a měří, kde náhodný surfař tráví čas [(20:19)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=1219s). A prediktivní text od Shannonových experimentů po dnešní LLM je markovovská predikce dalšího tokenu — obohacená o attention. Stejná část videa poctivě ukazuje i hranice: systémy se zpětnou vazbou řetěz modelovat neumí.

### Rozpad myšlenky

**PageRank:** Yahoo řadilo podle výskytu klíčových slov — snadno ošálitelné bílým textem na bílém pozadí; chybělo měřítko *kvality* [(19:33)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=1173s). Brin a Page vzali starou knihovnickou heuristiku (hodně razítek = dobrá kniha [(20:19)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=1219s)) a přeložili ji do řetězu: odkaz = hlas, náhodný surfař skáče po odkazech a **podíl času na stránce = její skóre** [(21:05)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=1265s). Spam farma sta stránek nepomůže — na ty stránky nikdo neodkazuje, takže surfař se k nim skoro nedostane a jejich „hlasy" nic neváží [(21:53)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=1313s). Prakticky důležitý detail: **damping factor** — 85 % času následuj odkaz, 15 % skoč náhodně, jinak se surfař zasekne ve smyčkách odříznutých od zbytku webu [(22:42)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=1362s).

**Prediktivní text:** Shannon zjistil, že predikce se zlepšuje s délkou kontextu — dvě písmena dají slova, celá slova dají smysluplné čtyřslovné sekvence [(25:49)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=1549s). Dnešní LLM dělají totéž nad **tokeny**, ale s **attention**: model váží, která část kontextu je pro predikci relevantní („blood" a „mitochondria" říkají, že „cell" je buňka, ne cela [(27:22)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=1642s)). A varování, které stojí za zapamatování: když se výstupy modelů stanou trénovacími daty, systém konverguje k „nudnému stabilnímu stavu" — model collapse [(27:22)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=1642s).

**Kde řetěz nefunguje:** systémy se **zpětnou vazbou** — oteplování → víc vodní páry → víc oteplování [(28:09)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=1689s). Memoryless předpoklad se rozbije, když výstup systému mění jeho vlastní pravidla. A bonusová drobnost pro herní večery: balíček karet je taky řetěz (stav = uspořádání, krok = zamíchání) — riffle shuffle potřebuje **7 opakování** k plné náhodnosti [(30:28)](https://www.youtube.com/watch?v=KZeIEiBrT_w&t=1828s).

> **Pozn.:** Gamedev překlady: PageRank logika („důležité je, kam vedou cesty, ne co o sobě uzel tvrdí") funguje na analýzu level flow — kudy náhodný hráč skutečně chodí. Markovovské n-gramy jsou nejlevnější generátor jmen a textur světa: natrénuj přechody písmen na seznamu slovanských jmen a generuj nová. A pity-timery, žebříčky dropů či weather systémy jsou řetězy, u kterých chceš vědět, k jakému rozdělení konvergují — viz Monte Carlo výše. Závěr videa je sponzorský segment (Brilliant), fakta z něj nečerpám.

**Souvislosti:** [PCG: základy a nástroje](../praxe/pcg-zaklady.md) — procedurální generace v UE · [Algoritmy, které stojí za to znát](algoritmy-prehled.md) · [Rejstřík: Markovův řetěz](../rejstrik.md#markovuv-retez)
