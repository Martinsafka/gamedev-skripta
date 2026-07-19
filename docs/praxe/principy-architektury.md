# Principy architektury: dědičnost, vazby a data

Dvě videa, která se doplňují jako teorie a tělocvična: Ali Elzoheiry ukazuje na ability systému **tři principy škálovatelnosti** (separation of concerns, loose coupling, data-driven design) a Taken Grace v 80minutovém workshopu staví od nuly modulární systém dveří na **dědičnosti** — včetně všech praktických pastí, na které cestou narazíš. Společné poselství: systém, který funguje dnes, není totéž co systém, který funguje za půl roku s desetinásobkem obsahu.

---

## Dědičnost: test „is it a?" a rodič jako smlouva

**Zdroj:** [The ONLY Way to Build Scalable Systems in Unreal Engine 5](https://www.youtube.com/watch?v=zTsJM9T0NjM) · [Taken Grace](https://www.youtube.com/channel/UCLagdpQoUG-jtyH8bF0IGZg) · ~81 min, workshop (systém dveří ve 4 úrovních)

**Shrnutí:** Celý engine je postavený na dědičnosti — Actor → Pawn → Character je hierarchie, ne náhoda [(0:10)](https://www.youtube.com/watch?v=zTsJM9T0NjM&t=10s). Lakmusový test každého rozhodnutí o dědičnosti jsou tři slova: **is it a?** [(1:20)](https://www.youtube.com/watch?v=zTsJM9T0NjM&t=80s) Pes *je* mazlíček, mazlíček *je* actor; dům mazlíček *není* — a kdo vynucuje divné vztahy jen kvůli sdílené proměnné, vyrábí dům s funkcí „nakrm mě".

### Rozpad myšlenky

**Rodič je právní smlouva** [(2:00)](https://www.youtube.com/watch?v=zTsJM9T0NjM&t=120s): každá proměnná, funkce a komponenta definovaná v parent classe je garantovaně v každém dítěti — to není doporučení, to je slib, který engine drží za tebe. Na smlouvě stojí **polymorfismus** [(2:12)](https://www.youtube.com/watch?v=zTsJM9T0NjM&t=132s): hráč volá na cokoli jediné `Interact` a nezajímá ho, jestli stojí před obyčejnými dveřmi, zamčenými, nebo dveřmi s kódovým zámkem — každé dítě si odpověď definuje samo. Kód hráče se nemění, kód rodiče se nemění, děti řeší svoje.

Dvě disciplíny, které smlouvu drží čistou:

- **God class zákaz** [(2:41)](https://www.youtube.com/watch?v=zTsJM9T0NjM&t=161s): do rodiče patří jen to, co potřebují *všechny* děti. Když má kódový zámek jediný typ dveří, jeho logika žije v dítěti — ne v masteru „pro jistotu".
- **Abstract class** [(5:13)](https://www.youtube.com/watch?v=zTsJM9T0NjM&t=313s): u base classy zaškrtni `Class Settings → Generate Abstract Class` — master pak nejde umístit do světa ani vybrat v class referencích. Souvisí s pamětí: master má být čistá data a logika bez meshů a materiálů, protože **cokoli master referencuje, se nahrává do paměti u každé reference na něj** [(5:52)](https://www.youtube.com/watch?v=zTsJM9T0NjM&t=352s). Kontrola: pravý klik na asset → **Size Map** [(36:57)](https://www.youtube.com/watch?v=zTsJM9T0NjM&t=2217s) — workshop jím průběžně ověřuje, že switch class zůstává drobná a netahá s sebou textury dveří.

A dvě mechaniky dědičnosti, které v Blueprintech překvapí:

- **Component eventy nejdou overridnout** [(30:34)](https://www.youtube.com/watch?v=zTsJM9T0NjM&t=1834s): `OnComponentBeginOverlap` zapojený v rodiči poběží vždycky z rodiče. Řešení: v rodiči ho jen přepoj do vlastního custom eventu (`E CollisionOverlap`) s potřebnými vstupy — custom eventy děti overridovat umí.
- **Add Call to Parent Function** [(44:18)](https://www.youtube.com/watch?v=zTsJM9T0NjM&t=2658s): overridnutý event v dítěti *nespouští* rodičovskou verzi automaticky; oranžový uzel z pravého kliku ji zavolá explicitně — a záleží, *kde* v grafu stojí (napřed vlastní logika, pak rodič, nebo obráceně).

> **Pozn.:** Pointa celého workshopu je v závěru [(1:20:17)](https://www.youtube.com/watch?v=zTsJM9T0NjM&t=4817s): po čtyřech úrovních (obyčejné dveře → auto dveře → spínače a multi-dveře → zámky s klíči) zůstal master štíhlý a nové chování vznikalo skládáním existujících funkcí. „Skill není v dveřích — každý actor, item a nepřítel ve tvé hře má svou verzi téhle hierarchie." Srovnej s [enginy v enginu](../teorie/produktivita.md#investice-bez-validace-lesteni-systemy-a-optimalizace-predem): tohle je přesně ta architektura, kterou stavíš, *až když* je systém validovaný.

**Souvislosti:** [Interakce bez Event Ticku](interakce-bez-event-ticku.md) · [Komunikace Blueprintů](komunikace-blueprintu.md) · [Rejstřík: inheritance](../rejstrik.md#inheritance) · [Rejstřík: abstract class](../rejstrik.md#abstract-class) · [Rejstřík: god class](../rejstrik.md#god-class)

---

## Tři principy škálovatelnosti: separace, volné vazby, data

**Zdroj:** [3 Principles Every Game Programmer Needs to Know in Unreal Engine](https://www.youtube.com/watch?v=RhKqtQRy_j0) · [Ali Elzoheiry](https://www.youtube.com/channel/UCrrZx9bh7RMYhXvaN8BrbNg) · ~18 min, případovka na ability systému

**Shrnutí:** „Postavit systém, který funguje, je snadné. Postavit systém, který funguje za šest měsíců s desetinásobkem features — to je výzva" [(0:04)](https://www.youtube.com/watch?v=RhKqtQRy_j0&t=4s). Video vezme naivní ability systém (všechno v jedné komponentě) a třemi principy ho krok za krokem přestaví — a končí poznáním, že přesně takhle Epic postavil svůj Gameplay Ability System.

### Rozpad myšlenky

Výchozí stav: laser ability nadrátovaná v actor componentě — cooldown, sphere trace, damage, animace, VFX, zvuk, update UI, všechno v jednom grafu s hard-coded hodnotami. Funguje; a při třech abilitách je graf nečitelný [(2:13)](https://www.youtube.com/watch?v=RhKqtQRy_j0&t=133s), při dvaceti neladitelný. Léčba po krocích:

1. **Separation of concerns** [(3:27)](https://www.youtube.com/watch?v=RhKqtQRy_j0&t=207s) — motorová metafora: složitý systém z malých specializovaných dílů, které jdou měnit bez redesignu celku. Prakticky: ability se vytáhne z komponenty do vlastního objektu s base classou; návrhová otázka zní **„co mají všechny ability společné?"** [(4:13)](https://www.youtube.com/watch?v=RhKqtQRy_j0&t=253s) (activate/end/cooldown + pravidlo aktivace). Komponenta pak řeší jen aktivační logiku a centrální cooldowny; škálování na 20 abilit = 20 nezávislých blueprintů se stejnou strukturou.
2. **Loose coupling** [(7:49)](https://www.youtube.com/watch?v=RhKqtQRy_j0&t=469s) — diagnostika přes **Reference Viewer** [(6:06)](https://www.youtube.com/watch?v=RhKqtQRy_j0&t=366s): proč laser závisí na třídě nepřítele? Protože při damage castí na `BP_Enemy` [(6:22)](https://www.youtube.com/watch?v=RhKqtQRy_j0&t=382s). Lék: **damageable interface** — smlouva „poskytneš-li Take Damage, zavolám ji, a je mi jedno, kdo jsi" [(8:12)](https://www.youtube.com/watch?v=RhKqtQRy_j0&t=492s). Druhá klasická vazba: gameplay ↔ UI (komponenta referencuje HUD [(6:42)](https://www.youtube.com/watch?v=RhKqtQRy_j0&t=402s)); lék je **mediátor** — event manager subsystem [(9:21)](https://www.youtube.com/watch?v=RhKqtQRy_j0&t=561s) se dvěma delegáty (cooldown started/ended): gameplay broadcastuje a neřeší, kdo poslouchá; HUD se binduje a neřeší, kdo volá [(10:17)](https://www.youtube.com/watch?v=RhKqtQRy_j0&t=617s).
3. **Data-driven design** [(11:26)](https://www.youtube.com/watch?v=RhKqtQRy_j0&t=686s) — hodnoty (damage, montage, zvuky) nepatří do logiky, ale do **data assetu**; a protože ne každá ability má všechno, data asset nese pole **fragmentů** [(12:06)](https://www.youtube.com/watch?v=RhKqtQRy_j0&t=726s) (animace, damage, VFX, SFX) — ability si přidá jen ty svoje a base classa je centrálně zpracuje. Data asset navíc **vede designéra** [(13:07)](https://www.youtube.com/watch?v=RhKqtQRy_j0&t=787s): zaškrtneš „damage over time" a odkryjí se pole tick/duration (meta properties, jen C++). Vrchol demonstrace [(14:49)](https://www.youtube.com/watch?v=RhKqtQRy_j0&t=889s): výměnou data assetu se z laseru stane ground slam — jiná animace, jiné efekty, jiné časování — **bez jediné změny v logice** [(14:45)](https://www.youtube.com/watch?v=RhKqtQRy_j0&t=885s).

> **Pozn.:** Závěr videa [(16:20)](https://www.youtube.com/watch?v=RhKqtQRy_j0&t=980s) je dobrá mapa pro budoucí učení: pokračuj v aplikování těch tří principů a dojdeš k UE Gameplay Ability System — je postavený na tomtéž (data-driven, komponentový, separovaný). Tedy: GAS není magie, je to tahle kapitola dotažená do konce. Hodí se vědět, až přijde batch Motion Matching/GASP.

**Souvislosti:** [Dědičnost](#dedicnost-test-is-it-a-a-rodic-jako-smlouva) výše · [Komunikace Blueprintů](komunikace-blueprintu.md) · [Rejstřík: separation of concerns](../rejstrik.md#separation-of-concerns) · [Rejstřík: loose coupling](../rejstrik.md#loose-coupling) · [Rejstřík: data-driven design](../rejstrik.md#data-driven-design)

---

## Nářadí z workshopu: kde co bydlí a jak se to hýbe

**Zdroj:** [The ONLY Way to Build Scalable Systems in Unreal Engine 5](https://www.youtube.com/watch?v=zTsJM9T0NjM) · [Taken Grace](https://www.youtube.com/channel/UCLagdpQoUG-jtyH8bF0IGZg) · stejný workshop, praktické detaily

**Shrnutí:** Workshop mimochodem odpovídá na tři otázky, které si začátečník v UE klade pořád: *kam patří která data* (Player State vs. Game Instance), *jak plynule hýbat věcmi bez Ticku* (interp + timer) a *proč věci závisejí na pořadí inicializace* (race conditions a dispatchery).

### Rozpad myšlenky

**Kde co bydlí:** klíče, které hráč nasbíral, patří do **Player State** [(58:34)](https://www.youtube.com/watch?v=zTsJM9T0NjM&t=3514s) — tam, kde má žít inventář a další data vázaná na hráče (a v multiplayeru replikovaná). Generátor unikátních ID klíčů patří do **Game Instance** [(1:01:24)](https://www.youtube.com/watch?v=zTsJM9T0NjM&t=3684s) — jediného objektu, který žije od spuštění aplikace po její konec. Obě třídy existují v projektu vždy (C++ default); vlastní Blueprint verze se musí zaregistrovat v Game Mode, resp. `Project Settings → Maps & Modes`.

**Plynulý pohyb bez Ticku:** místo timeline volí workshop vzorec **RInterp/VInterp + Set Timer by Event** [(9:18)](https://www.youtube.com/watch?v=zTsJM9T0NjM&t=558s) — timer každých 0,05 s posune rotaci/pozici o krok k cíli. Proč ne timeline: rychlost jde měnit dynamicky za běhu (dveře, kterými prosprintuješ, se otevřou rychleji). Dva ošetřené detaily: delta čas z `Get World Delta Seconds` [(10:45)](https://www.youtube.com/watch?v=zTsJM9T0NjM&t=645s), aby rychlost neseděla na frame rate; a porovnání floatů s tolerancí [(12:34)](https://www.youtube.com/watch?v=zTsJM9T0NjM&t=754s) — rotace skončí na 89,999°, takže `==` bez variance nikdy nepadne a timer se nikdy nevypne (Clear & Invalidate Timer by Handle).

**Pořadí inicializace:** klíče se při BeginPlay ptají dveří na ID — jenže klíč se může inicializovat dřív než dveře. Klasická **race condition** [(1:03:52)](https://www.youtube.com/watch?v=zTsJM9T0NjM&t=3832s); řešení je event dispatcher `KeyAssigned`, na který se klíč binduje, místo aby ID četl hned. Obecné pravidlo: na data z BeginPlay jiného actora se nespoléhej — nech si je oznámit. A když se něco rozbije, **Blueprint Debugger** [(46:51)](https://www.youtube.com/watch?v=zTsJM9T0NjM&t=2811s) s watch hodnotami a breakpointy je rychlejší než print-string archeologie — workshop to dvakrát předvádí naživo včetně vlastních přehmatů.

**Souvislosti:** [Ukládání](ukladani.md) *(SaveGame jako další „kde co bydlí")* · [Interakce bez Event Ticku](interakce-bez-event-ticku.md) · [Rejstřík: Player State](../rejstrik.md#player-state) · [Rejstřík: Game Instance](../rejstrik.md#game-instance) · [Rejstřík: race condition](../rejstrik.md#race-condition)

---

## Komponenty místo dědičnosti: skládej místo větvení

**Zdroj:** [Understanding "Components" in Unreal Engine | UE5 Explained](https://www.youtube.com/watch?v=xo0sbSeWKe4) · [Ali Elzoheiry](https://www.youtube.com/channel/UCrrZx9bh7RMYhXvaN8BrbNg) · ~28 min, tutoriál (série o návrhových vzorech)

**Shrnutí:** Hráč i nepřítel potřebují zdraví, útoky a pohyb. Duplikace nepřipadá v úvahu, ale **ani společný rodič není správná odpověď** — a to je ta část, kterou většina tutoriálů přeskočí. Komponentní vzor staví složité aktéry **skládáním malých dílů s jedinou zodpovědností**, a video to dotáhne až k triku, kde si komponenta sama přidá health bar každému, kdo ji použije.

### Rozpad myšlenky

**Proč dědičnost selže dřív, než čekáš** [(0:48)](https://www.youtube.com/watch?v=xo0sbSeWKe4&t=48s): *„co když chceš zničitelný objekt, který má zdraví, ale ne útoky ani pohyb? Nebo NPC se zdravím a pohybem, které neumí útočit? Pořád ho musíš udělat potomkem a nacpat mu spoustu funkcí, které nepotřebuje, které mu budou překážet a časem se rozbijí."* Dědičnost odpovídá na otázku „**co to je**", ale schopnosti nejsou identita — a přesně tam se [test „is it a?"](#dedicnost-test-is-it-a-a-rodic-jako-smlouva) láme.

**Analogie, kterou video používá** [(1:35)](https://www.youtube.com/watch?v=xo0sbSeWKe4&t=95s), je lidské tělo: srdce pumpuje krev, plíce dýchají, žaludek tráví — a *„stejně jako u softwarových komponent se dá jeden orgán léčit nebo vyměnit izolovaně, aniž to zasáhne celý systém"*.

**Health komponenta** [(3:55)](https://www.youtube.com/watch?v=xo0sbSeWKe4&t=235s) je záměrně minimální: proměnná `Health`, funkce `TakeDamage(float)` a **dva dispatchery — `OnDamageTaken` a `OnDeath`**. A s ní přichází pravidlo, které je jádrem celé kapitoly [(6:16)](https://www.youtube.com/watch?v=xo0sbSeWKe4&t=376s): **„nikdy nesmíš předpokládat, kdo bude komponentu používat. Hráč zpracuje smrt úplně jinak než nepřítel — u hráče respawn a game over obrazovka, u nepřítele ragdoll a spawn nového."** Komponenta proto smrt **oznamuje**, neprovádí ji.

**Public vs. private** [(7:50)](https://www.youtube.com/watch?v=xo0sbSeWKe4&t=470s): zaškrtnutí `Private` u proměnné ji schová zvenku. *„Když jsou veřejné, říkáš uživateli komponenty ‚tyhle smíš měnit'; když soukromé, ‚nesahej na ně, něco bys rozbil'."* Je to nejlevnější forma dokumentace, jakou v Blueprintech máš.

**Trik, kvůli kterému stojí za to video vidět** [(12:34)](https://www.youtube.com/watch?v=xo0sbSeWKe4&t=754s): komponenta si v `BeginPlay` sáhne na `GetOwner` a zavolá **`AddComponentByClass(WidgetComponent)`** — tedy **přidá vlastníkovi další komponentu**. Nastaví jí lokaci +100 na Z, draw size, screen space a vypne kolize, vytvoří widget a nastrčí ho dovnitř. Widget se na `EventConstruct` naváže na `OnDamageTaken` vlastníkovy health komponenty a přepočítá progress bar. Výsledek [(15:40)](https://www.youtube.com/watch?v=xo0sbSeWKe4&t=940s): přidáš health komponentu nepříteli — a **má health bar, aniž bys udělal cokoli dalšího**; totéž kostka. *„Like magic — všichni tři teď máme zdraví a health bar, který se aktualizuje nezávisle."*

**Jak spolu komponenty mluví** [(17:37)](https://www.youtube.com/watch?v=xo0sbSeWKe4&t=1057s): attacks komponenta po zásahu zavolá `GetComponentByClass(HealthComponent)`, ověří platnost a teprve pak `TakeDamage`. Tím vzniká **implicitní pravidlo světa**: *„attacks komponenta ví, že aby šlo aktéra zranit, musí mít health komponentu — a když ji nemá, nejde ho zranit."* Alternativu autor zmíní hned [(18:23)](https://www.youtube.com/watch?v=xo0sbSeWKe4&t=1103s): dát `TakeDamage` do interface — *„zpočátku režie navíc, ale nakonec ušetří čas"*.

**Nejlepší důkaz skládání** [(23:51)](https://www.youtube.com/watch?v=xo0sbSeWKe4&t=1431s): behavior tree nepřítele čeká jen na to, že aktér má attacks komponentu. Takže **AI controller lze připnout na hráče** a nechat ho ovládat (mind control), nebo naopak **hráčským controllerem posednout nepřítele**. *„Nedělá to rozdíl, jestli je posednutý pawn hráč nebo nepřítel, protože sdílejí tutéž komponentu."* Nic z toho se neprogramuje zvlášť — plyne to z toho, že schopnost není přibitá k identitě.

**Když se přece jen liší** [(24:37)](https://www.youtube.com/watch?v=xo0sbSeWKe4&t=1477s): kostka má mít zdraví, ale ne health bar. Odpověď není větev v komponentě ani nová podtřída, nýbrž **konfigurace** — bool `HideHealthBar` vystavený v detailech. Vzorem je Character Movement komponenta se svou hromadou voleb, *„protože pohyb není jedna velikost pro všechny"*.

> **Pozn.:** Komponentní vzor je v UE tak samozřejmý, že si ho většina lidí neuvědomí jako rozhodnutí — panel Components **je** ten vzor. U hry s interakcemi a inventářem to znamená konkrétní věc: interakce, otevírání a stav dveří patří spíš do komponent než do společného rodiče `BP_InteractableActor`, protože **jinak si zaděláš na strom, ve kterém truhla dědí schopnost mluvit**. Praktický protějšek stejného uvažování je [health komponenta vs. interface](komunikace-blueprintu.md#interface-nebo-dispatcher-a-kolik-doopravdy-stoji-cast) z téže série.

**Souvislosti:** [Dědičnost: test „is it a?"](#dedicnost-test-is-it-a-a-rodic-jako-smlouva) *(kdy naopak rodič dává smysl)* · [Tři principy škálovatelnosti](#tri-principy-skalovatelnosti-separace-volne-vazby-data) · [Interface, nebo dispatcher](komunikace-blueprintu.md#interface-nebo-dispatcher-a-kolik-doopravdy-stoji-cast) · [Design patterns: tři rodiny vzorů](../teorie/design-patterns.md#tri-rodiny-vzoru-tvorba-struktura-chovani) · [Rejstřík: Actor Component](../rejstrik.md#actor-component) · [Rejstřík: separation of concerns](../rejstrik.md#separation-of-concerns)
