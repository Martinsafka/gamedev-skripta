# Tipy do editoru

Sbírka drobných triků, které nezaslouží vlastní kapitolu, ale šetří minuty každý den — výběry a navigace ve viewportu, oprava pivotu bez Blenderu, rozmisťování fyzikou, rychlejší mazání uzlů. A jedna větší myšlenka do začátku: **jak se engine vůbec učit**, sepsaná autorizovaným instruktorem Epicu.

---

## Vybrat všechny instance assetu v levelu naráz

**Zdroj:** [Select EVERY Copy of an Asset Instantly in UE5!](https://www.youtube.com/watch?v=De2fXs2JZxw) · [Matt Aspland](https://www.youtube.com/channel/UC8_RNwftEO4isrX2LJowcpg) · short (~30 s), editor tip

**Shrnutí:** Když je jeden prop rozesetý po celém levelu a potřebuješ všechny jeho kusy posunout, přenastavit nebo globálně vyměnit, nemusíš je lovit v outlineru: vyber jednu instanci ve viewportu a stiskni **Shift+E** — editor označí všechny instance téhož assetu v levelu [(0:01)](https://www.youtube.com/watch?v=De2fXs2JZxw&t=1s).

### Rozpad myšlenky

Užitečnost je přímočará: hromadná úprava vlastností (všechny lucerny → jiná intenzita), hromadný přesun, hromadná výměna assetu (přes pravý klik → Replace Selected Actors with). Za zkratkou stojí obecnější mechanismus výběru podle shody, který má editor i v kontextovém menu (`pravý klik → Select`), kde jsou k dispozici další varianty výběru podle třídy či assetu — zkratka je jen nejrychlejší cesta k té nejčastější.

> **Pozn.:** U tipů tohohle typu platí obecná výhrada: klávesové zkratky se mezi verzemi UE občas mění a dají se přemapovat v `Editor Preferences → Keyboard Shortcuts`. Když zkratka nefunguje, hledej akci podle jména právě tam.

**Souvislosti:** [Výběry a navigace](#vybery-navigace-a-drobna-zrychleni) · [Rejstřík: instance](../rejstrik.md#instance)

---

## Jak se učit engine: rady po pěti letech

**Zdroj:** [5 Years Of Unreal Engine Experience In 9 Minutes](https://www.youtube.com/watch?v=BHY46bPmsXY) · [Unreal University](https://www.youtube.com/channel/UCQv4mwerZLQVe3wPbsMc-qw) · ~9 min, rady

**Shrnutí:** Deset rad autorizovaného instruktora Epicu — a všechny míří na stejný cíl: přestat *sledovat* a začít *stavět*. Jádro: **tutorial hell je reálný** (video → funguje → prázdný projekt → nic) a útěk z něj je vždycky stejný — po každém tutoriálu zavřít video a postavit něco malého vlastního [(0:48)](https://www.youtube.com/watch?v=BHY46bPmsXY&t=48s).

### Rozpad myšlenky

**Učení:** základy napřed — nikdo nemaluje Monu Lisu první den se štětcem; začátečník stavící inventář a open world v prvním týdnu nepřeskakuje kroky, jen si připravuje pád bez diagnózy [(0:02)](https://www.youtube.com/watch?v=BHY46bPmsXY&t=2s). Nejnebezpečnější moment není bug — je to chvíle **po dokončení tutoriálu**, kdy si sedneš k vlastní hře a nevíš, co první; mezera mezi následováním kroků a myšlením vývojáře se zavírá malými vlastními projekty: dveře, mince, postava, co dostane damage [(2:20)](https://www.youtube.com/watch?v=BHY46bPmsXY&t=140s) [(3:06)](https://www.youtube.com/watch?v=BHY46bPmsXY&t=186s). A neuč se celý engine — uč se, **co tvůj projekt potřebuje**: third person hra = pohyb, kolize, kamery, základní AI; zbytek počká [(5:27)](https://www.youtube.com/watch?v=BHY46bPmsXY&t=327s).

**Práce:** v blueprintech zpomal — napřed záměr v přirozeném jazyce („když hráč overlapne box, otevři dveře"), pak přesně tohle postavit; pomalu a správně je vždycky rychlejší než rychle a špatně [(6:13)](https://www.youtube.com/watch?v=BHY46bPmsXY&t=373s). **Print String je nejlepší přítel**: pálí event, nebo nepálí? Jakou hodnotu má proměnná? Nezůstal odpojený pin? [(3:06)](https://www.youtube.com/watch?v=BHY46bPmsXY&t=186s) [(3:53)](https://www.youtube.com/watch?v=BHY46bPmsXY&t=233s) Když se zasekneš: Google „Unreal Engine 5 + problém", oficiální fóra (skutečné problémy se skutečnými řešeními), případně AI [(4:40)](https://www.youtube.com/watch?v=BHY46bPmsXY&t=280s) [(5:27)](https://www.youtube.com/watch?v=BHY46bPmsXY&t=327s).

**Projekt:** nepotřebuješ velký nápad, potřebuješ **dokončený** — první projekt maličký, druhý taky; dokončování je dovednost, kterou většina vývojářů nikdy nevytrénuje [(3:53)](https://www.youtube.com/watch?v=BHY46bPmsXY&t=233s) [(4:40)](https://www.youtube.com/watch?v=BHY46bPmsXY&t=280s). Nedělej všechno sám — jeho první horor stál na Fab assetech včetně hlavního monstra („jsem spíš kodér"); jen s cizími blueprint systémy počkej, až budeš umět je ohnout [(6:59)](https://www.youtube.com/watch?v=BHY46bPmsXY&t=419s) [(7:45)](https://www.youtube.com/watch?v=BHY46bPmsXY&t=465s). A pořádek: pojmenované proměnné, uklizené grafy, konvence typu `BP_`/`M_` — chvíle úklidu teď ušetří hodiny zmatku potom [(1:34)](https://www.youtube.com/watch?v=BHY46bPmsXY&t=94s) [(2:20)](https://www.youtube.com/watch?v=BHY46bPmsXY&t=140s).

> **Pozn.:** Praxe-strana toho, co Teorie říká z druhého břehu: [začátky bez zkušeností](../teorie/zacatky-bez-zkusenosti.md) (malé dokončené projekty), [kolik kódu potřebuješ na start](../teorie/co-se-ucit.md) (uč se, co projekt žádá) a [scope](../teorie/scope.md) (malý ≠ míň hodnotný). Bonusová teze videa sedí na celý tenhle projekt skript: problém učení není obtížnost, ale **struktura** — roztroušená videa ve špatném pořadí [(7:45)](https://www.youtube.com/watch?v=BHY46bPmsXY&t=465s). Konvence pojmenování do hloubky řeší [Organizace projektu](organizace-projektu.md).

**Souvislosti:** [Teorie: začátky bez zkušeností](../teorie/zacatky-bez-zkusenosti.md) · [Teorie: kolik kódu na start](../teorie/co-se-ucit.md) · [Organizace projektu](organizace-projektu.md) · [Zápisky: kvízový protokol](../zapisky/kvizovy-protokol.md) *(učení vlastní mezerou: otázky a počítadla chyb)* · [Rejstřík: tutorial hell](../rejstrik.md#tutorial-hell)

---

## Výběry, navigace a drobná zrychlení

**Zdroj:** [The Secret 3D Box-Select Tool in UE5!](https://www.youtube.com/watch?v=HprvvfEzrNI) a [5 Unreal Engine Tricks Every Beginner Misses](https://www.youtube.com/watch?v=kSHz_V79eCk) · [Matt Aspland](https://www.youtube.com/channel/UC8_RNwftEO4isrX2LJowcpg) · shorty · + [UE5 for Beginners: 5 Tips I Wish I Knew Sooner](https://www.youtube.com/watch?v=jxEfh8_zfdk) · [Sergey Maryshev](https://www.youtube.com/channel/UCVAdTnZgQ40jpKzC0-_RPAQ) · short

**Shrnutí:** Devět mikro-triků ze tří shortů — dohromady slušný upgrade denní rutiny: **Ctrl+Alt+tažení** vybere boxem přímo ve 3D viewportu (celý les jedním tahem) [(0:01)](https://www.youtube.com/watch?v=HprvvfEzrNI&t=1s), `F` zaostří kameru na objekt, `Alt+tažení` duplikuje, `End` upustí objekt na povrch pod ním [(0:01)](https://www.youtube.com/watch?v=kSHz_V79eCk&t=1s).

### Rozpad myšlenky

**Výběr a pohyb:** 3D box select (`Ctrl+Alt+tažení`) nahrazuje třicet shift-kliků [(0:01)](https://www.youtube.com/watch?v=HprvvfEzrNI&t=1s); k tomu výběr identických objektů (viz [Shift+E výše](#vybrat-vsechny-instance-assetu-v-levelu-naraz)) a **bookmarky**: `Ctrl+číslo` uloží pohled kamery, samotné číslo se k němu vrátí — pro velké levely zlato [(0:00)](https://www.youtube.com/watch?v=jxEfh8_zfdk&t=0s).

**Rychlovky z grafu i browseru:** `Ctrl+B` skočí z vybraného aktoru na jeho asset v content browseru; dvojklik na drát v blueprintu vloží **reroute node** — úklid špaget zadarmo [(0:01)](https://www.youtube.com/watch?v=kSHz_V79eCk&t=1s). A dvě pojistky ze Sergeyova shortu: **zámek transformu** na kameře (ikonka zámku v Details — konec omylem posunutých kamer) a vlastní **thumbnail** assetu v content browseru přes nastavení náhledu [(0:00)](https://www.youtube.com/watch?v=jxEfh8_zfdk&t=0s).

> **Pozn.:** Jak už řekla pilotní myšlenka: zkratky se mezi verzemi mění a přemapovávají v `Editor Preferences → Keyboard Shortcuts` — když něco nefunguje, hledej akci podle jména tam.

**Souvislosti:** [Shift+E: všechny instance](#vybrat-vsechny-instance-assetu-v-levelu-naraz) · [Rejstřík: instance](../rejstrik.md#instance)

---

## Pivot bez Blenderu a rozmístění fyzikou

**Zdroj:** [Change Your Mesh's Pivot Point in the Engine!](https://www.youtube.com/watch?v=f50yoTWThnw) · [Druid Mechanics](https://www.youtube.com/channel/UCzy_jDd65W3OFWYu4pplrQg) · short · + [The Secret to Realistic Level Design in UE5](https://www.youtube.com/watch?v=qo-LYeeKMr4) · [Matt Aspland](https://www.youtube.com/channel/UC8_RNwftEO4isrX2LJowcpg) · short

**Shrnutí:** Dva triky na umisťování. Nekonzistentní **pivoty** mezi asset packy (každá zbraň sedí v socketu jinak) se dají opravit přímo v enginu — modeling mode → Transform → **Edit Pivot** [(0:01)](https://www.youtube.com/watch?v=f50yoTWThnw&t=1s). A přirozený nepořádek světa neskládej ručně: **rozházej propy do vzduchu, pusť Simulate a nech gravitaci pracovat** [(0:02)](https://www.youtube.com/watch?v=qo-LYeeKMr4&t=2s).

### Rozpad myšlenky

**Edit Pivot:** mesh přetáhnout do levelu → modeling mode → sekce Transform → Edit Pivot → posunout/otočit → Accept; starou instanci smazat a přetáhnout novou — pivot je opravený v assetu, žádný export do Blenderu, žádné množení socketů per zbraň [(0:01)](https://www.youtube.com/watch?v=f50yoTWThnw&t=1s).

**Fyzikou na místo:** propy (sutiny, nádobí, klacky) nahoď volně nad povrch, zapni **Simulate** — gravitace je rozmístí věrohodně sama. Pointa, kterou většina nezná: po dopadu right-click → **Keep Simulation Changes** — pozice se zapíšou natrvalo a fyzika za hry už neběží [(0:02)](https://www.youtube.com/watch?v=qo-LYeeKMr4&t=2s).

> **Pozn.:** Keep Simulation Changes je set-dressing zkratka k „lived-in" neuspořádanosti, o které mluví [RE Requiem breakdown](env-breakdowny.md#re-requiem-realismus-je-vrstveni) — ručně naaranžovaný nepořádek vypadá naaranžovaně, spadlý nepořádek spadle. Pivot jako herní pojem (bod závěsu kyvadla) rozebírají [Pasti a mechaniky](pasti-a-mechaniky.md).

**Souvislosti:** [Breakdowny: RE Requiem](env-breakdowny.md#re-requiem-realismus-je-vrstveni) · [Pasti a mechaniky](pasti-a-mechaniky.md) · [Rejstřík: pivot](../rejstrik.md#pivot)

---

## Mazání se sešitím a lék na editor lag

**Zdroj:** [Stop Deleting Blueprint Nodes Like This!](https://www.youtube.com/watch?v=Pt1tFh4UqJk) a [How To Fix Editor Lag In 30 Seconds!](https://www.youtube.com/watch?v=U0nC8-882a0) · [Matt Aspland](https://www.youtube.com/channel/UC8_RNwftEO4isrX2LJowcpg) · shorty

**Shrnutí:** Dvě třicetivteřinové záchrany: **Shift+Delete** smaže blueprint uzel a **sešije dráty za něj** — konec ručního přepojování [(0:01)](https://www.youtube.com/watch?v=Pt1tFh4UqJk&t=1s); a když editor bez důvodu drhne, zkus vypnout **telemetry pluginy** [(0:01)](https://www.youtube.com/watch?v=U0nC8-882a0&t=1s).

### Rozpad myšlenky

**Shift+Delete:** obyčejné Delete nechá po uzlu díru a přetrhané exec i datové dráty; Shift+Delete uzel vyjme a spojení propojí napřímo — refaktoring grafu přestane bolet [(0:01)](https://www.youtube.com/watch?v=Pt1tFh4UqJk&t=1s).

**Editor lag:** Edit → Plugins → vyhledat „tele" → vypnout editor telemetry pluginy (podle verze „Editor Telemetry" či „Studio Telemetry") → restart editoru [(0:01)](https://www.youtube.com/watch?v=U0nC8-882a0&t=1s).

> **Pozn.:** K telemetrii poznámka: tip míří na *editor* telemetrii enginu (odesílání dat o používání editoru), ne na herní analytiku — vlastní [telemetrie ve hře](telemetrie.md) je jiná kapitola a vypínat ji nechceš. Jako u všech „vypni X a zrychlí to" tipů: změř si to (`stat unit`), placebo je levné.

**Souvislosti:** [Telemetrie](telemetrie.md) · [Výběry a navigace](#vybery-navigace-a-drobna-zrychleni) · [Rejstřík: draw call](../rejstrik.md#draw-call)
