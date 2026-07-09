# Organizace projektu: Content Browser a čisté grafy

Dvě vrstvy pořádku: struktura složek v Content Browseru (kde bydlí assety a proč se špatný úklid mstí až při balení buildu) a hygiena uvnitř Blueprint grafů (aby ses ve vlastní logice vyznal i za tři měsíce). První řeší Taken Grace podle standardu Epicu, druhou devět tipů Unreal University.

---

## Content Browser podle Epicu: feature foldery, Developers a redirectory

**Zdroj:** [Why Your UE5 Projects Are Messy (And How to Fix It)](https://www.youtube.com/watch?v=0-xB4P2yYN8) · [Taken Grace](https://www.youtube.com/channel/UCLagdpQoUG-jtyH8bF0IGZg) · ~11 min, úklid reálného projektu naživo

**Shrnutí:** Složky podle *typu assetu* (Materials, Sounds, Blueprints…) jsou past [(0:57)](https://www.youtube.com/watch?v=0-xB4P2yYN8&t=57s) — správně se organizuje podle *funkce* (feature). Test je migrace: klikni na systém pravým → Migrate, a když se s ním táhne půlka projektu napříč deseti složkami, struktura selhala. Epic má dokumentovaný standard [(0:07)](https://www.youtube.com/watch?v=0-xB4P2yYN8&t=7s) — a video ukazuje i chybu, která spolehlivě shodí packaging [(0:17)](https://www.youtube.com/watch?v=0-xB4P2yYN8&t=17s).

### Rozpad myšlenky

**Struktura:** v rootu Contentu jediná složka se jménem hry/studia [(1:57)](https://www.youtube.com/watch?v=0-xB4P2yYN8&t=117s) a v ní feature foldery: `Core` (player controller, HUD, game state…), `Systems` (každý systém se vším, co k němu patří), `Characters` (+ `Common` pro sdílené skeletony), `Art`, `Sounds` jen pro skutečně globální věci — specifické zvuky bydlí u svého characteru. Efekt: assety z Fabu si žijí ve vlastních složkách mimo tvoji hru [(5:49)](https://www.youtube.com/watch?v=0-xB4P2yYN8&t=349s) a migrace systému do jiného projektu táhne jen jeho vlastní strom. K tomu **Developers folder** [(1:33)](https://www.youtube.com/watch?v=0-xB4P2yYN8&t=93s) (zapíná se v nastavení Content Browseru): každý člen týmu si rozdělanou práci staví u sebe a do hlavní struktury ji stěhuje, až když je hotová.

**Stěhování bez rozbití projektu:** přesun assetu zanechá na starém místě **redirector** — ghost soubor, který říká „hledej mě jinde" [(3:36)](https://www.youtube.com/watch?v=0-xB4P2yYN8&t=216s). Proto „prázdné" složky nejdou smazat; force delete = rozbitý projekt [(4:17)](https://www.youtube.com/watch?v=0-xB4P2yYN8&t=257s). Správný postup: pravý klik → **Update Redirector References** [(4:30)](https://www.youtube.com/watch?v=0-xB4P2yYN8&t=270s) (všechny odkazy se přepíšou na novou cestu), pak teprve mazat. A stěhuj **po jedné složce** [(5:24)](https://www.youtube.com/watch?v=0-xB4P2yYN8&t=324s) — přesun načítá assety do paměti a hladový výběr editor spolehlivě sestřelí [(5:06)](https://www.youtube.com/watch?v=0-xB4P2yYN8&t=306s) (ve videu 2× naživo).

**Jména:** prefixové konvence (BP_, IMC_…) podle style guide Michaela Allara, na kterou odkazuje sám Epic [(6:15)](https://www.youtube.com/watch?v=0-xB4P2yYN8&t=375s); jeho úvodní věta je laťka — „každý asset má vypadat, jako by celý projekt dělal jediný člověk" [(6:39)](https://www.youtube.com/watch?v=0-xB4P2yYN8&t=399s). A slíbená bomba: **Windows má 260znakový limit cesty** [(7:09)](https://www.youtube.com/watch?v=0-xB4P2yYN8&t=429s) — hluboko vnořené složky s dlouhými jmény projdou celým vývojem a shodí až packaging v den vydání. Jména krátká, vnoření mělké.

**Souvislosti:** [Tipy do editoru](editor-tipy.md) · [Principy architektury](principy-architektury.md) *(size map, reference)* · [Rejstřík: redirector](../rejstrik.md#redirector) · [Rejstřík: hard reference](../rejstrik.md#hard-reference)

---

## Devět tipů proti špagetám v grafech

**Zdroj:** [9 Tips To Better Organize Your Unreal Engine Projects](https://www.youtube.com/watch?v=S7TwnS2wAZQ) · [Unreal University](https://www.youtube.com/channel/UCQv4mwerZLQVe3wPbsMc-qw) · ~6 min, listicle

**Shrnutí:** Hygiena Blueprint grafů v devíti tipech — od tvrdého pravidla (stejná logika nikdy dvakrát [(0:40)](https://www.youtube.com/watch?v=S7TwnS2wAZQ&t=40s)) po kosmetiku. Seskupeno podle toho, co tip skutečně řeší: duplicitu, čitelnost, nebo strukturu.

### Rozpad myšlenky

**Proti duplicitě:** opakovaná logika patří do **funkce** [(0:29)](https://www.youtube.com/watch?v=S7TwnS2wAZQ&t=29s); funkce sdílené napříč blueprinty do **Blueprint Function Library** (globálně volatelné odkudkoli — viz [tag helpers](gameplay-tags.md#kde-tagy-bydli-a-jak-se-na-ne-ptat-bez-skrytych-bugu)). A celé subsystémy do **komponent** [(3:05)](https://www.youtube.com/watch?v=S7TwnS2wAZQ&t=185s): inventář nekóduj v player characteru, ale v actor componentě, kterou na character přidáš — systém je přenositelný a character čitelný.

**Pro čitelnost:** **komentáře** [(1:04)](https://www.youtube.com/watch?v=S7TwnS2wAZQ&t=64s) — na uzel pravým klikem, na blok výběr + `C` („budeš si to pamatovat" je lež, kterou si říkáme všichni); **reroute uzly** [(1:33)](https://www.youtube.com/watch?v=S7TwnS2wAZQ&t=93s) dvojklikem na drát, ať vodiče nekříží uzly; **méně uzlů pro totéž** [(1:56)](https://www.youtube.com/watch?v=S7TwnS2wAZQ&t=116s): `Select` místo branch/switch, **Validated Get** (pravý klik na proměnnou → Convert) místo `IsValid` + branch, a od 5.7 i převod boolean proměnné rovnou na branch; **zarovnávací nástroje** [(4:52)](https://www.youtube.com/watch?v=S7TwnS2wAZQ&t=292s) z kontextového menu.

**Pro strukturu:** **kategorie proměnných** [(4:28)](https://www.youtube.com/watch?v=S7TwnS2wAZQ&t=268s) — jakmile jich je víc než hrst, kategorie v details panelu jsou jediná obrana (workshop dveří je používá taky); **collapse do sub-grafů** [(3:50)](https://www.youtube.com/watch?v=S7TwnS2wAZQ&t=230s) s upřímnou výhradou autora, že schovaná logika se hůř hledá — používat s mírou. A **tip 9**: placený plugin Blueprint Assist [(5:34)](https://www.youtube.com/watch?v=S7TwnS2wAZQ&t=334s) formátuje graf algorytmicky jedním tlačítkem.

> **Pozn.:** Tip 1 má architektonický háček, který video neřeší: „nikdy neopakuj uzly" platí pro *produkční* kód — v [prototypu na vyhození](../teorie/napad.md#prototyp-do-tydne-a-momentum-bar) je copy-paste ctnost. A pozor, čistý graf ≠ dobrá architektura: špagety jsou symptom, vazby jsou nemoc ([loose coupling](principy-architektury.md#tri-principy-skalovatelnosti-separace-volne-vazby-data)).

**Souvislosti:** [Principy architektury](principy-architektury.md) · [Gameplay Tags: function library](gameplay-tags.md) · [Rejstřík: Blueprint Function Library](../rejstrik.md#blueprint-function-library)
