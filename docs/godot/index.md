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

**Systémy a nástroje**

- **[Animace a pohyb](animace-a-pohyb.md)** — AnimationTree jako graf místo změti podmínek, skok, který rozumí tomu, co hráč chtěl (coyote time, buffer, korekce rohu), křivka místo vzorce a navigace, která se ve 2D obkresluje ručně.
- **[Control nody a UI](ui-control.md)** — kotvy a offsety pro layout, který přežije jiné rozlišení; čtyři kontejnery, ze kterých je 90 % UI; a témata, overridy a style boxy — včetně pasti se sdíleným resourcem.
- **[2D svět: dlaždice, světlo a pixel art](2d-svet.md)** — dual-grid a 16 dlaždic místo 256, tři nody na osvětlení (ztmavit, prosvítit, zaclonit) a pixel art od palety po import do enginu.
- **[Multiplayer: high-level API](multiplayer.md)** — spawner, synchronizer a otázka, kdo koho ovládá; co za tebe engine udělá a co tím ztratíš.

**Případovka: 2D akční platformer**

Poslední téma sekce jde jinou cestou: místo návodů sleduje **jeden projekt** — akční platformer *Isadora's Edge* — a to, jak se v něm rozhodovalo. Autor natáčí devlogy roky a mluví i o tom, co nevyšlo, včetně věcí, které nakonec vyhodil. Bere se z toho jinak než z tutoriálu: ne postup, ale **kritéria**.

- **[Pohyb a ovládání](pripadovka-pohyb.md)** — rozdělení vstupu od provedení (a dash jako důkaz, že to fungovalo), tři tiché opravy pohybu, proč vyhodil všechny šikmé plochy — a klasické dilema, jestli se při útoku zastavit.
- **[Kamera pro pixel art](pripadovka-kamera.md)** — čtyři pojmenované vady pixelové kamery, rozlišení, které polovinu z nich řeší, subpixelový posun v shaderu — a proč jeho vlastní test měsíce lhal.
- **[Nepřátelé a souboj](pripadovka-nepratele.md)** — tři patra AI a co se na nich rozbilo, létající nepřátelé ve třech verzích, frame data systém definovaný předem, boss stavěný z otázek — a combo s hit stopem ve dvou minutách.

Zbývají dvě dávky případovky: level a mapa, vizuál a zvuk, systémy a progrese, a proces.
