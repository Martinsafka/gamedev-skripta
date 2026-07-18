# Algoritmy, které stojí za to znát

Fireship v deseti minutách proletí deset „divných" algoritmů — od procedurální generace map po kvantové lámání šifer. Pro tahle skripta nejde o katalog k memorování, ale o **nápadník**: tři z těch algoritmů (wave function collapse, marching cubes, boids) jsou přímo herní klasika a zbytek kalibruje intuici, co všechno „algoritmus" umí být. Kapitola je přeskládaná po mechanismech, ne po pořadí videa.

---

## Algoritmy, které staví herní světy

**Zdroj:** [10 weird algorithms every developer should know](https://www.youtube.com/watch?v=SmyPTnlqhlk) · [Fireship](https://www.youtube.com/channel/UCsBjURrPoezykLs9EqgamOA) · ~9 min, rychlý přehled

**Shrnutí:** Tři algoritmy z videa řeší tutéž herní otázku — „jak vyrobit obsah, který nikdo ručně nepostavil": **wave function collapse** skládá mapy z dlaždic podle pravidel sousedství [(0:47)](https://www.youtube.com/watch?v=SmyPTnlqhlk&t=47s), **marching cubes** převádí objemová data na mesh [(6:14)](https://www.youtube.com/watch?v=SmyPTnlqhlk&t=374s) a **diffusion** generuje obrázky postupným odšumováním [(1:34)](https://www.youtube.com/watch?v=SmyPTnlqhlk&t=94s).

### Rozpad myšlenky

**Wave function collapse** si půjčuje metaforu z kvantové mechaniky [(0:47)](https://www.youtube.com/watch?v=SmyPTnlqhlk&t=47s): každé políčko mapy začíná jako „superpozice" všech možných dlaždic a pozorování (= generátor na něj přijde řada) ho zkolabuje na konkrétní dlaždici — ale jen takovou, která neporuší pravidla sousedství (silnice musí navazovat). Výsledek je „náhodný, a přitom soudržný" [(1:34)](https://www.youtube.com/watch?v=SmyPTnlqhlk&t=94s): nekonečný sidescroller, dungeon nebo město bez ručního kladení dlaždic — a bez jakékoli generativní AI. To je přesně rodina nástrojů, kterou v UE zastupuje PCG framework: pravidla místo assetů.

**Marching cubes** (1987, General Electric — původně pro vizualizaci CT/MRI snímků [(0:01)](https://www.youtube.com/watch?v=SmyPTnlqhlk&t=1s)) řeší opačný směr: máš 3D pole čísel (skalární pole — hustota, vzdálenost, „kolik je tu kamene") a chceš z něj povrch. Algoritmus jde bod po bodu, z osmi sousedů složí krychli, hodnoty nad/pod prahem přečte jako bity 8bitového čísla → 256 případů s předpočítanou tabulkou polygonů — a „pochoduje" polem, dokud nevyskládá celý mesh [(6:14)](https://www.youtube.com/watch?v=SmyPTnlqhlk&t=374s). Každý voxelový terén, deformovatelná jeskyně nebo metaball efekt stojí na něm či jeho potomcích.

**Diffusion** [(1:34)](https://www.youtube.com/watch?v=SmyPTnlqhlk&t=94s) je dnešní generativní standard (DALL-E, Stable Diffusion): trénink obrázky postupně zašumuje, model se učí šum vracet zpět — a generace pak začne čistým šumem a „vyodšumuje" z něj nový obrázek. Výpočetně drahé, funguje i na audio, další meta je video. Pro pipeline AI assetů viz [AI assety](../praxe/ai-assety.md).

**Souvislosti:** [PCG: základy a nástroje](../praxe/pcg-zaklady.md) · [Mesh Terrain (UE 5.8)](../praxe/mesh-terrain.md) · [AI assety](../praxe/ai-assety.md) · [Rejstřík: Wave Function Collapse](../rejstrik.md#wave-function-collapse) · [Rejstřík: Marching cubes](../rejstrik.md#marching-cubes)

---

## Emergence, žíhání a kabinet kuriozit

**Zdroj:** [10 weird algorithms every developer should know](https://www.youtube.com/watch?v=SmyPTnlqhlk) · [Fireship](https://www.youtube.com/channel/UCsBjURrPoezykLs9EqgamOA) · stejné video, zbytek katalogu

**Shrnutí:** Druhá půlka výběru učí dvě přenositelné lekce: **boids** ukazují, jak tři primitivní pravidla vyrobí chování, které nikdo nenaprogramoval [(7:47)](https://www.youtube.com/watch?v=SmyPTnlqhlk&t=467s), a **simulated annealing** ukazuje, jak se hledá „dost dobré" řešení v krajině plné lokálních vrcholů [(2:21)](https://www.youtube.com/watch?v=SmyPTnlqhlk&t=141s). Zbytek je kulturní kapitál programátora — od sleep sortu po kvantové hrozby šifrování.

### Rozpad myšlenky

**Boids** (Craig Reynolds, 1986 [(7:47)](https://www.youtube.com/watch?v=SmyPTnlqhlk&t=467s)): každý „pták" se řídí třemi pravidly — vyhýbej se tlačenici (separation), leť průměrným směrem hejna (alignment), drž se těžiště sousedů (cohesion) — a z jejich součtu **emergují** vzory hejna, které v kódu nikde nejsou. Pro gamedev dvojí lekce: davy, hejna ryb a ptáků máš za tři pravidla; a obecněji — komplexní chování se levněji *pěstuje* z jednoduchých pravidel, než skriptuje. Stejný princip nese steering chování nepřátel v [game feel kapitole](game-feel.md#souboj-dela-zabavnym-pohyb-nepratel-ne-jejich-statistiky) a smyčky–řetězce uvažování o systémech.

**Simulated annealing** [(2:21)](https://www.youtube.com/watch?v=SmyPTnlqhlk&t=141s), vypůjčené z metalurgie (žíhání = ohřát a nechat chladnout): hledáš nejvyšší vrchol v pohoří samých kopečků; prostý hill-climb uvízne na prvním lokálním vrcholu. Řešení: začni s vysokou „teplotou" — ochotou přijímat i horší kroky (explorace) — a postupně chladni k čistému vylepšování (exploatace) [(3:08)](https://www.youtube.com/watch?v=SmyPTnlqhlk&t=188s). Je to tentýž trade-off explore/exploit, na kterém stojí [teorie zábavy](zabava.md#zabava-je-odmena-za-dobre-vyuzity-mozek); tady jako optimalizační nástroj (rozmístění skladu, rozvrh, tuning parametrů).

**Kabinet kuriozit** — každá věc jedna věta a jedna lekce:

- **Sleep sort** [(3:54)](https://www.youtube.com/watch?v=SmyPTnlqhlk&t=234s): pro každé číslo otevři vlákno, které spí číslo sekund a pak ho vypíše — „geniální i k ničemu, protože řazení deleguje na plánovač CPU". Vtip, který mimochodem učí, co je scheduler.
- **Bogo sort** [(4:41)](https://www.youtube.com/watch?v=SmyPTnlqhlk&t=281s): míchej náhodně, dokud není seřazeno — loterie jako algoritmus; kvantová verze je fyzikální anekdota.
- **RSA a Shorův algoritmus** [(4:41)](https://www.youtube.com/watch?v=SmyPTnlqhlk&t=281s): internetová bezpečnost stojí na tom, že rozklad velkého čísla na prvočísla trvá bilionky let; kvantový Shor to umí exponenciálně rychleji — jen zatím největší fakticky rozložené číslo je 21 [(5:27)](https://www.youtube.com/watch?v=SmyPTnlqhlk&t=327s).
- **Byzantští generálové a pBFT** [(7:01)](https://www.youtube.com/watch?v=SmyPTnlqhlk&t=421s): jak se distribuovaný systém dohodne, když třetina uzlů lže nebo spí — základ blockchainů a distribuovaných databází.
- **Boyer–Moore** [(8:33)](https://www.youtube.com/watch?v=SmyPTnlqhlk&t=513s): hledání v textu, které je *rychlejší na delším textu*, protože se naučí přeskakovat — důvod, proč je grep tak rychlý.

> **Pozn.:** Video je rychlopalba a u některých položek zjednodušuje na hranu memu; ber ho jako mapu, ne učebnici. Hloubku k marching cubes a WFC hledej v dokumentaci enginu a v PCG kapitolách — a k Markovovým řetězcům, které by do tohohle výběru patřily taky, máme [vlastní kapitolu](markovovy-retezce.md).

**Souvislosti:** [Zábava a flow: explore vs. exploit](zabava.md) · [Základy nepřátelské AI](../praxe/ai-zaklady.md) · [Rejstřík: Boids](../rejstrik.md#boids) · [Rejstřík: Simulated annealing](../rejstrik.md#simulated-annealing)
