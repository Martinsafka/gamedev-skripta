# Praxe v Godotu

Druhý enginový dokument vedle [Praxe v UE5](../praxe/index.md). Godot je jiná krabice na stejné řemeslo: open source, pár desítek megabajtů, vlastní skriptovací jazyk — a hlavně **jiný způsob, jak si rozdělit hru na kusy**. Kde Unreal staví na actorech a komponentách, Godot staví na **nodech a scénách**, a ten rozdíl prosakuje do každého rozhodnutí, které v něm uděláš.

Kapitoly píšeme tak, aby dávaly smysl i tomu, kdo přišel z Unrealu: kde se hodí, tam je most („tohle je zdejší event dispatcher"), a kde se paralela láme, říkáme to nahlas. Verzi enginu uvádíme tam, kde na ní záleží — Godot 4.x se hýbe rychle a část toho, co je tu popsané, se objevila až ve 4.6.

Témata a kapitoly:

**Godot: začínáme**

- **[Nody, scény a strom](zaklady.md)** — mentální model enginu: node jako stavební kostka s jednou prací, scéna jako znovupoužitelný balík, strom jako architektura. Plus mapa 2D nodů, co si přinést, než editor vůbec otevřeš, a proč se 4.6 prohledává, místo aby se procházel.
- **[První hra: od prázdné scény k .exe](prvni-hra.md)** — celý oblouk na nejmenší možné hře: znovupoužitelná kill zone, delta a physics process, AnimationPlayer jako časovač bez kódu — a nastavení projektu, které dělá rozdíl mezi školním cvičením a hrou, co si někdo koupí.

**GDScript a kód**

- **[GDScript](gdscript.md)** — jazyk jako sada rozhodnutí o bezpečnosti: gradual typing, signály a pravidlo „call down, signal up", `class_name` jako datový kontrakt, pořádek ve skriptu i v inspektoru — a jeden bug, který není v kódu, ale v klávesnici.

**Architektura projektu**

- **[Kompozice: skládej místo dědění](kompozice.md)** — has-a místo is-a a hrdinův batoh, test kamene pro sobeckou komponentu — a dvě videa, která si zdánlivě protiřečí: jedno změřilo, že nody nic nestojí, druhé má obrazovku, kterou nody stály 115 ms.
- **[Resource: data mimo kód](resources.md)** — skript řídí chování, resource popisuje, co ta věc je; past sdílených resourců, přestavěná hra jako důkaz, kdy scéna a kdy data — a kdy místo toho stačí dictionary.
- **[Signály do hloubky](signaly.md)** — událost, ne příkaz (jméno signálu tě prozradí), data v signálu, event bus pro dynamicky vznikající objekty — a jediný zdroj pravdy jako nejcennější koncept celé série.
- **[Stavové automaty a vzory](stavy-a-vzory.md)** — stav jako podmínka plus chování, strategy pattern jako vyměnitelný resource a celý přenositelný systém nepřítele, který se dá zkopírovat do jiného projektu složkou.
- **[Struktura projektu a výkon](projekt-a-vykon.md)** — vlastnictví napřed a složky potom, chyba se záporným měřítkem, která stála celý projekt, co skutečně stojí výkon (ne nody) — a nástroje, které si napíšeš sám pro sebe.

Sekce roste po dávkách; chystají se **systémy a nástroje** (animace, UI, 2D svět, multiplayer) a **případovka jednoho 2D akčního platformeru** od pohybu po změnu žánru.
