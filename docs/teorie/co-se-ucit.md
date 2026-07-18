# Kolik kódu potřebuješ na start

Kapitola pro den, kdy tě od první hry dělí strach z programování. Dobrá zpráva: základní stavebnice je překvapivě malá — pár konstruktů, které pochopíš za odpoledne a pak roky prohlubuješ. Zdrojové video staví hru v Godotu, ale stavebnice je ve všech enginech stejná; v UE5 se jen místo řádků textu skládají Blueprint uzly.

---

## Stavebnice o pěti kostkách: proměnné, podmínky, funkce, smyčky, třídy

**Zdroj:** [All of the Coding You Need to Start Gamedev!](https://www.youtube.com/watch?v=yjiFwz6mS6k) · [Brainless.](https://www.youtube.com/channel/UCJmAuKzz_VHa3Yb7v19KIvQ) · ~16 min, crash course na miniaturní hře

**Shrnutí:** Autor staví malou 2D hru (jsi pod vodou, sbíráš bubliny, než dojde vzduch) a cestou ukazuje, že celý pohybový skript stojí na pěti konstruktech. Teze videa: programování je snadné se naučit, jen má vysoký strop — a začátečníka od první hry nedělí roky studia, ale těchhle pět pojmů.

### Rozpad myšlenky

**Proměnná (variable)** je pojmenovaná přihrádka na data, jejíž obsah se za běhu mění [(2:05)](https://www.youtube.com/watch?v=yjiFwz6mS6k&t=125s). Tři typy pokryjí většinu začátků: **integer** (číslo), **string** (text), **boolean** (pravda/nepravda). Ve hře je proměnnou skoro všechno, co se hýbe: zbývající vzduch, skóre, jestli hráč stojí na zemi.

**Podmínka (if statement)** větví běh programu: *když platí tohle, udělej tamto* [(3:17)](https://www.youtube.com/watch?v=yjiFwz6mS6k&t=197s). `else` zachytí opačný případ [(4:11)](https://www.youtube.com/watch?v=yjiFwz6mS6k&t=251s) a `else if` skládá větve do řetězu, kde první splněná podmínka ukončí zbytek. Spojkami `and`/`or` se podmínky kombinují — na tom stojí příklad se skokem níže.

**Funkce (function)** autor přirovnává ke stroji s tlačítkem start: zabalený kus kódu, který se spustí zavoláním; **parametry** jsou vstupy, které do stroje vhodíš [(12:25)](https://www.youtube.com/watch?v=yjiFwz6mS6k&t=745s). Engine navíc některé funkce volá sám — physics process v Godotu běží ~60× za vteřinu a patří do ní fyzika a pohyb [(2:58)](https://www.youtube.com/watch?v=yjiFwz6mS6k&t=178s).

**Smyčky (loops)**: `for` zopakuje kód daný počet iterací, `while` běží, *dokud* něco platí — a je na tobě zajistit, aby přestalo platit, jinak hra zamrzne [(11:54)](https://www.youtube.com/watch?v=yjiFwz6mS6k&t=714s).

**Třída (class)** je v autorově obrazu továrna: balík souvisejících funkcí a vlastností, ke kterým se přistupuje tečkou — `Input.is_action_just_pressed(...)` [(8:40)](https://www.youtube.com/watch?v=yjiFwz6mS6k&t=520s).

K tomu jeden nástroj zdarma: `print` vypíše hodnotu do konzole — nejlevnější způsob, jak zjistit, co se v kódu skutečně děje a jestli vůbec běží.

> **Pozn.:** Převod do UE5 Blueprintů je 1:1 — proměnné jsou proměnné, if je uzel `Branch`, funkce jsou funkce/eventy, smyčky `ForLoop`/`WhileLoop`, třída je Blueprint sám. Jen pozor: obdobou physics processu je v UE `Event Tick`, volaný každý snímek — a ten se u nás v praxi učíme spíš *nepoužívat* (viz [Interakce bez Event Ticku](../praxe/interakce-bez-event-ticku.md)).

**Souvislosti:** [Začátky bez zkušeností](zacatky-bez-zkusenosti.md) · [Programátorské myšlení](programatorske-mysleni.md) *(hlubší mentální modely týchž kostek)* · [Rejstřík: Event Tick](../rejstrik.md#event-tick)

---

## Skutečná dovednost je rozklad problému, ne syntax

**Zdroj:** [All of the Coding You Need to Start Gamedev!](https://www.youtube.com/watch?v=yjiFwz6mS6k) · [Brainless.](https://www.youtube.com/channel/UCJmAuKzz_VHa3Yb7v19KIvQ) · stejné video, meta-lekce

**Shrnutí:** Nejcennější moment videa není žádný konstrukt, ale scéna, kdy postava skáče donekonečna ve vzduchu. Syntax si vygooglíš; to, co se trénuje léta, je převod „tohle se chová blbě" na pravidlo, které jde zapsat podmínkou.

### Rozpad myšlenky

Postup u chyby se skokem [(9:13)](https://www.youtube.com/watch?v=yjiFwz6mS6k&t=553s) je miniatura celého programátorského řemesla: **chtěné chování** (postava skáče) → **pozorování** (skáče i ve vzduchu, protože tlačítko funguje kdykoli) → **pravidlo** (skákat se smí jen ze země) → **zápis** (`and is_on_floor` v podmínce skoku). Tenhle řetěz — od pocitu „to je špatně" k formulaci, kterou stroj pochopí — je ta skutečná dovednost; pět kostek z předchozí myšlenky je jen abeceda, kterou se pravidlo zapíše.

Druhá půlka lekce: nauč se číst dokumentaci dřív, než se naučíš zpaměti API. Funkcí jsou v každém enginu tisíce a nikdo je nezná všechny — v Godotu stačí najet myší a editor funkci popíše, a totéž umí UE5 u uzlů [(10:03)](https://www.youtube.com/watch?v=yjiFwz6mS6k&t=603s). Znát všechno není cíl; cíl je umět si rychle najít, co zrovna potřebuješ.

> **Pozn.:** Autor přiznává, že na hře strávil ~15 hodin a video z toho ukazuje zlomek [(14:15)](https://www.youtube.com/watch?v=yjiFwz6mS6k&t=855s) — a plná verze ho stála dalších ~50. Dobrá kalibrace: i „muší" hra je násobně víc práce, než kolik jí je vidět. Souvisí s pravidlem ×40 z kapitoly [Start projektu](jak-zacit.md).

**Souvislosti:** [Start projektu](jak-zacit.md) · [Produktivita](produktivita.md)

---

## Literály se mstí: čísla do proměnných, klávesy do pojmenovaných akcí

**Zdroj:** [All of the Coding You Need to Start Gamedev!](https://www.youtube.com/watch?v=yjiFwz6mS6k) · [Brainless.](https://www.youtube.com/channel/UCJmAuKzz_VHa3Yb7v19KIvQ) · stejné video, dvě praktiky

**Shrnutí:** Hard coding — hodnoty napsané natvrdo přímo v kódu — funguje přesně do chvíle, kdy je potřeba je změnit. Stejná past číhá u vstupů: kód se nemá ptát na mezerník, ale na akci „jump". V obou případech pomáhá jedna vrstva nepřímosti.

### Rozpad myšlenky

Autorův příklad s gravitací [(7:30)](https://www.youtube.com/watch?v=yjiFwz6mS6k&t=450s): napíšeš `9.8` na tři místa v kódu, za měsíc usoudíš, že gravitace má být silnější, a teď je lovíš po celém projektu — a jednu zapomeneš. Řešení je triviální: hodnota žije v proměnné, kód se odkazuje na ni, ladí se na jednom místě. Pravidlo z videa stojí za zapamatování: **každé surové číslo v kódu je kandidát na proměnnou** — obzvlášť všechno, co budeš někdy tunit (rychlosti, cooldowny, dosahy).

Vstupy jsou tentýž princip o patro výš [(8:09)](https://www.youtube.com/watch?v=yjiFwz6mS6k&t=489s): v nastavení projektu pojmenuješ akce („jump", „move_left") a přiřadíš jim klávesy; kód pak zná jen jména akcí. Přemapování ovládání, podpora gamepadu nebo nastavení kláves hráčem pak nesahá do logiky hry vůbec.

> **Pozn.:** V UE5 téhle myšlence odpovídá **Enhanced Input** (Input Actions + Mapping Contexts) a „čísla do proměnných" v Blueprintech krok dál znamená konfiguraci v Data Assetech — hodnoty pak ladí i ne-programátor, bez otevírání grafu. K tomu se vrátíme v praxi u architektury Blueprintů.

**Souvislosti:** [Interakce bez Event Ticku](../praxe/interakce-bez-event-ticku.md) · [Rejstřík: Hard coding](../rejstrik.md#hard-coding) · [Rejstřík: Data asset](../rejstrik.md#data-asset)
