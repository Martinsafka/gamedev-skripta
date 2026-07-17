# Smyčky a řetězce

Dva základní tvary, kterými design popisuje strukturu hry. Smyčka (loop) je nejcitovanější pojem herního designu — a právě proto stojí za to vědět, kde končí její vysvětlovací síla a co nabízí řetězec (chain) jako doplňkový model.

---

## Design teorie je sada metafor, ne fyzikální zákony

**Zdroj:** [Gameplay Loops Are Out, Chains Are In](https://www.youtube.com/watch?v=6SYX17NzNqE) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · ~11 min, video esej o designovém myšlení

**Shrnutí:** Než video vůbec začne řešit řetězce, srovná půdu pod celou design teorií: smyčky, řetězce a podobné koncepty nejsou vlastnosti her, ale **popisný jazyk** — kulturně podmíněné metafory, které designérům umožňují vidět vzory, pojmenovat je a vědomě je reprodukovat. To není relativismus („na teorii nezáleží"), ale přesné určení, k čemu teorie je: je to notace, ne hudba.

### Rozpad myšlenky

Autor používá hudební přirovnání [(0:49)](https://www.youtube.com/watch?v=6SYX17NzNqE&t=49s): notový zápis umožňuje hudbu číst, zapsat a předat, ale hudba existuje nezávisle na něm a samotný zápis je arbitrární konvence. Stejně tak hráčovo chování a prožitek existují ve hře; „smyčka" je způsob, jak na ně ukázat prstem. Praktický důsledek pro designéra: teorie je **čtecí a komunikační nástroj**. Když analyzuješ cizí hru, pojmy ti pomáhají vidět strukturu; když navrhuješ vlastní, pomáhají ti sdělit záměr týmu. Ale hra se nestane dobrou tím, že „má smyčku" — stejně jako se skladba nestane dobrou tím, že jde zapsat do not.

Odtud plyne autorova výtka smyčkám [(1:40)](https://www.youtube.com/watch?v=6SYX17NzNqE&t=100s): základní reward-investment smyčka (zabij → seber → nakup → zabij silnějšího) popisuje skoro každou hru, a právě proto vysvětluje tak málo. Model, který sedí na všechno, nediskriminuje — neřekne ti, proč jedna hra s toutéž smyčkou baví a druhá nudí. Smyčky mají smysl při analýze konkrétních rytmů (video zmiňuje Dark Souls a jeho „negativní oslavu" smrti, která proměňuje další běh pro ztracené duše), ale jako univerzální odpověď na „co mé hře chybí" jsou plytké.

> **Pozn.:** Tohle je dobrý test na jakýkoli design pojem: *co by musela hra dělat, aby pod něj nespadala?* Pokud nic, je to slovník, ne teorie. Slovník je užitečný — jen od něj nečekej predikce.

**Souvislosti:** [Řetězce a emoce](#retezec-nese-emocni-oblouk) níže · [Zábava a flow](zabava.md) · [Základy: engagement a appeal](zaklady.md) · [Rejstřík: gameplay loop](../rejstrik.md#gameplay-loop) · [Rejstřík: core loop](../rejstrik.md#core-loop) · [Hudba a zvuk: aranžmá z loopu](../hudba/aranz.md) *(opakování a proměna v aranži)*

---

## Řetězec nese emoční oblouk

**Zdroj:** [Gameplay Loops Are Out, Chains Are In](https://www.youtube.com/watch?v=6SYX17NzNqE) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · stejné video, hlavní teze

**Shrnutí:** Řetězec je posloupnost akcí s **pořadím a cílem** — a právě směřování k cíli dává řetězci to, co smyčce chybí: rostoucí emoční investici. Video rozlišuje tři podoby: exekuční řetězec (combo), hodnotový řetězec (sbírám → stavím) a tajný řetězec (objevování skrytého). Každá mapuje na jinou emoci.

### Rozpad myšlenky

**Exekuční řetězec** je nejnázornější na combu z bojovky [(2:56)](https://www.youtube.com/watch?v=6SYX17NzNqE&t=176s): pět úderů ve správném pořadí. Klíčové pozorování — selhání na prvním kroku zamrzí, selhání na čtvrtém bolí. Každý zvládnutý článek zvyšuje sázku toho dalšího, takže napětí roste *uvnitř* řetězce. Smyčka tohle neumí: její iterace jsou si rovné, kdežto řetězec má dramaturgii. (Proto se combo nedá „button-mashovat" — bez závazku ke konkrétní sekvenci není co ztratit, a bez možné ztráty není napětí.)

**Hodnotový řetězec** staví na eseji designéra Dana Cooka o value chains, na kterou video odkazuje [(3:44)](https://www.youtube.com/watch?v=6SYX17NzNqE&t=224s): sbírání klacíků není zábavné samo o sobě a žádné vizuální pozlátko to nespasí — zábavným ho dělá až to, **co s klacíky hráč plánuje udělat** a jak to sytí fantazii, na které hra stojí. Autor to ilustruje na base buildingu ve Fallout 4 [(5:19)](https://www.youtube.com/watch?v=6SYX17NzNqE&t=319s): jakmile se z harampádí stal stavební materiál, změnil se význam *už existující* mechaniky lootování. Rozhodování „co sebrat" přestalo být optimalizací poměru cena/váha a stalo se nákupním seznamem pro vlastní projekt — hráč se učí, které ventilátory a telefony obsahují měděné dráty, protože staví osvětlení baru [(5:51)](https://www.youtube.com/watch?v=6SYX17NzNqE&t=351s). Obecný princip: **cíl řetězce zpětně obarvuje všechny jeho články.** Chceš-li oživit nudnou sběrací mechaniku, nepřidávej jí lesk, přidej jí destinaci.

**Tajný řetězec** [(6:38)](https://www.youtube.com/watch?v=6SYX17NzNqE&t=398s): hráč netuší, že v řetězci je. Spelunky nebo Castlevania: Symphony of the Night mají za „koncem" skrytý pravý konec, k němuž vede sekvence kroků, o kterých se hráč dozví náhodou, pozorováním — nebo od komunity, což je legitimní součást designu. Emoce je tu jiná než u comba: ne napětí, ale **prozření** („chodil jsem kolem toho celou dobu!"). Video trefně dodává, proč tenhle vzor sedí systémovým hrám a roguelikům [(7:39)](https://www.youtube.com/watch?v=6SYX17NzNqE&t=459s): opakované běhy násobí šanci na náhodné objevení spouštěče, takže tajemství se odemyká přirozeně, bez návodu. A pro sólo vývojáře je tu ekonomická pointa: autor vlastní hru s triviálním ovládáním (skoč, prašti, hoď) staví do hloubky právě tajnými řetězci [(8:25)](https://www.youtube.com/watch?v=6SYX17NzNqE&t=505s) — hloubka z obsahu a vztahů je levnější než hloubka z mechanik.

> **Pozn.:** Pro stealth adventuru je tajný řetězec obzvlášť zajímavý: žánr stojí na pozorování prostředí, takže hráč už má „skenovací" návyk, na který jde zavěsit objevitelské řetězce. A hodnotový řetězec je zase přesný popis toho, proč inventářové puzzly fungují — předmět bez známého použití je šum, předmět s tušeným použitím je motivace.

**Souvislosti:** [Design teorie jako metafory](#design-teorie-je-sada-metafor-ne-fyzikalni-zakony) výše · [Postmortem ShantyTown: účel jako soudce](postmortem-shantytown.md#hra-ti-rika-cim-chce-byt-ucel-jako-designovy-soudce) · [Vedení hráče](vedeni-hrace.md) · [Zápisky: oblouk se potvrzuje formou](../zapisky/oblouk-formou.md) *(tajný řetězec z rekvizity v praxi)* · [Rejstřík: value chain](../rejstrik.md#value-chain) · [Rejstřík: roguelike](../rejstrik.md#roguelike)
