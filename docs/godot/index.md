# Praxe v Godotu

Druhý enginový dokument vedle [Praxe v UE5](../praxe/index.md). Godot je jiná krabice na stejné řemeslo: open source, pár desítek megabajtů, vlastní skriptovací jazyk — a hlavně **jiný způsob, jak si rozdělit hru na kusy**. Kde Unreal staví na actorech a komponentách, Godot staví na **nodech a scénách**, a ten rozdíl prosakuje do každého rozhodnutí, které v něm uděláš.

Kapitoly píšeme tak, aby dávaly smysl i tomu, kdo přišel z Unrealu: kde se hodí, tam je most („tohle je zdejší event dispatcher"), a kde se paralela láme, říkáme to nahlas. Verzi enginu uvádíme tam, kde na ní záleží — Godot 4.x se hýbe rychle a část toho, co je tu popsané, se objevila až ve 4.6.

Témata a kapitoly:

**Godot: začínáme**

- **[Nody, scény a strom](zaklady.md)** — mentální model enginu: node jako stavební kostka s jednou prací, scéna jako znovupoužitelný balík, strom jako architektura. Plus mapa 2D nodů, co si přinést, než editor vůbec otevřeš, a proč se 4.6 prohledává, místo aby se procházel.
- **[První hra: od prázdné scény k .exe](prvni-hra.md)** — celý oblouk na nejmenší možné hře: znovupoužitelná kill zone, delta a physics process, AnimationPlayer jako časovač bez kódu — a nastavení projektu, které dělá rozdíl mezi školním cvičením a hrou, co si někdo koupí.

**GDScript a kód**

- **[GDScript](gdscript.md)** — jazyk jako sada rozhodnutí o bezpečnosti: gradual typing, signály a pravidlo „call down, signal up", `class_name` jako datový kontrakt, pořádek ve skriptu i v inspektoru — a jeden bug, který není v kódu, ale v klávesnici.

Sekce roste po dávkách; chystá se **architektura projektu** (kompozice, Resource jako data, signály do hloubky, stavové automaty, struktura a výkon), **systémy a nástroje** (animace, UI, 2D svět, multiplayer) a **případovka jednoho 2D akčního platformeru** od pohybu po změnu žánru.
