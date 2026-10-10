# Principy architektury: dědičnost, vazby a data

Kapitola o tom, jak stavět třídy a blueprinty, aby systém, který funguje dnes, fungoval i za půl roku s desetinásobkem obsahu. Začíná **dědičností** — kdy dává smysl, kdy z ní stačí jedna konfigurovatelná třída a na jaké pasti v Blueprintech narazíš (workshop dveří Taken Grace a vysvětlení Aliho Elzoheiryho). Pokračuje **třemi principy škálovatelnosti**, **komponentami** a Tyrollerovým poměrem kostek a lepidla a končí u **dat**: třída jako data a fragmenty z inventářové série, jejíž pokračování má vlastní kapitolu [Inventář](inventar.md).

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

**Souvislosti:** [Interakce bez Event Ticku](interakce-bez-event-ticku.md) · [Komunikace Blueprintů](komunikace-blueprintu.md) · [Kdy dědit a kdy jen konfigurovat](#kdy-dedit-a-kdy-jen-konfigurovat) · [Rejstřík: inheritance](../rejstrik.md#inheritance) · [Rejstřík: abstract class](../rejstrik.md#abstract-class) · [Rejstřík: god class](../rejstrik.md#god-class) · [Master actor interakcí a BP_BaseItem](interakcni-animace.md#objekt-vi-jak-se-s-nim-zachazi-data-interakce-patri-k-veci-ne-k-postave) *(rodič jako smlouva u interaktivních objektů)*

---

## Kdy dědit a kdy jen konfigurovat

**Zdroj:** [Why Your Unreal Project Becomes a Mess (And How to Fix It) | UE5 Inheritance Explained](https://www.youtube.com/watch?v=xS7wckoboAo) · [Ali Elzoheiry](https://www.youtube.com/channel/UCrrZx9bh7RMYhXvaN8BrbNg) · ~27 min, vysvětlující video (nepřátelé, zbraně, pickupy)

**Shrnutí:** Na jedné straně spektra stojí kopírování nepřítele a úprava kopie, na druhé jedna obří třída, která umí všechno; obojí neškáluje a dědičnost je rozumné mezi [(0:50)](https://www.youtube.com/watch?v=xS7wckoboAo&t=50s). Video ale nejvíc stojí za hranici, kde dědičnost přestává být odpovědí: **liší-li se dvě varianty jen daty, nepatří do dvou tříd, ale do jedné třídy se dvěma hodnotami.** Dítě si zaslouží jen jiné *chování* — a i to jde často vyřešit konfigurací.

### Rozpad myšlenky

**Pravidlo na jednom příkladu** [(7:47)](https://www.youtube.com/watch?v=xS7wckoboAo&t=467s): každý nepřítel má jinou animaci smrti. Přepsat funkci *die* v každém dítěti? Ne — chování je stejné (přehraj animaci), liší se jen animace, takže je to **proměnná** s hodnotou v každém dítěti. Přepsat se vyplatí, až když se liší samo chování: jeden nepřítel padá jako ragdoll, druhý hraje animaci. A co je skutečně unikátní (teleport mága), žije jen v dítěti a nikoho dalšího nezatěžuje.

**Prázdná událost jako háček** [(9:58)](https://www.youtube.com/watch?v=xS7wckoboAo&t=598s): jeden behavior tree pro všechny tři typy nepřátel. Task castne na rodiče a zavolá *attack*, kterou má rodič **prázdnou**; každé dítě ji naplní po svém a strom o konkrétních typech nic neví. Pravidlo z toho: víš-li, že funkci budou děti přepisovat, dej ji do rodiče aspoň prázdnou, aby šla zavolat přes rodičovskou referenci [(10:45)](https://www.youtube.com/watch?v=xS7wckoboAo&t=645s). Strom tím ovšem funguje jen s nepřáteli — má-li fungovat s čímkoli, je to práce pro interface.

**Přepsat, nebo rozšířit** [(6:15)](https://www.youtube.com/watch?v=xS7wckoboAo&t=375s): přepsání říká „ignoruj rodiče", rozšíření „udělej, co rodič, a pak tohle" (`Add Call to Parent Function`). Past, která z toho vychází nejčastěji, je tichá [(23:13)](https://www.youtube.com/watch?v=xS7wckoboAo&t=1393s): `BeginPlay` přidaný do dítěte kvůli jednomu tisku **přepíše** rodičův — a v ukázce tím všem nepřátelům zmizí zbraně, protože je rodič vybavoval právě v `BeginPlay`. Stejně zrádný je dvojklik na interface funkci v dítěti: tím ji přepíšeš a funkce se z panelu *Interfaces* přesune do *Functions* [(24:45)](https://www.youtube.com/watch?v=xS7wckoboAo&t=1485s).

**Zbraně: kde dědičnost pomáhá** [(11:33)](https://www.youtube.com/watch?v=xS7wckoboAo&t=693s): naivně si každá postava v `BeginPlay` spawne a připne svou zbraň — opakování, které nejde znovu použít. Rodičovská zbraň s meshem, jménem socketu a funkcí *attach* ho odstraní; meč se štítem jsou dva meshe, takže dostanou vlastní dítě s druhým socketem a přepsaným *attach* [(13:07)](https://www.youtube.com/watch?v=xS7wckoboAo&t=787s). A protože pak všichni nepřátelé dělají v `BeginPlay` totéž, přesune se i to do rodiče a třída zbraně je jen proměnná [(14:40)](https://www.youtube.com/watch?v=xS7wckoboAo&t=880s).

**Pickupy: kde dědičnost škodí** [(15:26)](https://www.youtube.com/watch?v=xS7wckoboAo&t=926s): mrkev, brambora, lektvar, šípy, zbraň — dítě pro každou položku je přesně ten omyl „dítě na každou drobnou změnu". Lepší je jedna konfigurovatelná třída: nejprve struct editovatelný na instanci (pohodlné, ale ruční a náchylné k chybám) [(17:00)](https://www.youtube.com/watch?v=xS7wckoboAo&t=1020s), pak **[data table](../rejstrik.md#data-table)**, ve které pickup drží jen jméno řádku a zbytek si dohledá v construction scriptu [(17:47)](https://www.youtube.com/watch?v=xS7wckoboAo&t=1067s). Jedna třída, žádná dědičnost, blueprint sám žádnou informaci nenese. Neznamená to nikdy nedědit: vybavitelná položka se *chová* jinak, a proto si dítě zaslouží [(19:20)](https://www.youtube.com/watch?v=xS7wckoboAo&t=1160s).

**Drobné rady na závěr** [(20:06)](https://www.youtube.com/watch?v=xS7wckoboAo&t=1206s): rodiče, které se nemají používat samy, označ jako abstraktní (zmizí z rozbalovacích nabídek a nejdou spawnout) · rané rozhodnutí jde opravit **reparentem** — například společný základ pro hráče i nepřítele, kteří stejně berou zásah, umírají i vybavují zbraně [(22:26)](https://www.youtube.com/watch?v=xS7wckoboAo&t=1346s) · v C++ projektu založ základní třídy nejdřív v C++, i prázdné, a blueprintové základy postav stav až na nich; je snazší to naplánovat než později reparentovat [(25:31)](https://www.youtube.com/watch?v=xS7wckoboAo&t=1531s).

> **Pozn.:** Pravidlo „liší se data → proměnná, liší se chování → dítě" je to, co v knihovně chybělo mezi [testem „is it a?"](#dedicnost-test-is-it-a-a-rodic-jako-smlouva) a [komponentami](#komponenty-misto-dedicnosti-skladej-misto-vetveni): první říká, kdy dědičnost dává smysl, druhé, kdy ji nahradit skládáním, a tohle říká, **kdy vystačíš s jedinou třídou**. Data table z ukázky je jedna ze tří cest, které autor rozebírá v inventářové sérii ([data table, data asset, třída jako data](#trida-jako-data-cdo-misto-instanci)) — pro pickup ve světě stačí, pro položku s funkčností už ne. A past s `BeginPlay` je důvod, proč se vyplatí mít v rodiči co nejméně logiky v obecných událostech: co rodič dělá v `BeginPlay`, je smlouva, kterou dítě umí potichu porušit.

**Souvislosti:** [Dědičnost: test „is it a?"](#dedicnost-test-is-it-a-a-rodic-jako-smlouva) · [Komponenty místo dědičnosti](#komponenty-misto-dedicnosti-skladej-misto-vetveni) · [Třída jako data](#trida-jako-data-cdo-misto-instanci) · [Inventář: vybavení](inventar.md#vybaveni-je-samostatny-system-definice-instance-manazer-a-akter) *(rodičovská definice položky)* · [Rejstřík: Inheritance](../rejstrik.md#inheritance) · [Rejstřík: Data table](../rejstrik.md#data-table) · [Rejstřík: Abstract class](../rejstrik.md#abstract-class)

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

**Souvislosti:** [Ukládání](ukladani.md) *(SaveGame jako další „kde co bydlí")* · [Interakce bez Event Ticku](interakce-bez-event-ticku.md) · [Ladění: čtyři otázky, čtyři nástroje](debugging.md#ctyri-otazky-ctyri-nastroje-od-print-stringu-po-visual-logger) *(debugger a jeho sourozenci)* · [Rejstřík: Player State](../rejstrik.md#player-state) · [Rejstřík: Game Instance](../rejstrik.md#game-instance) · [Rejstřík: race condition](../rejstrik.md#race-condition)

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

**Souvislosti:** [Dědičnost: test „is it a?"](#dedicnost-test-is-it-a-a-rodic-jako-smlouva) *(kdy naopak rodič dává smysl)* · [Tři principy škálovatelnosti](#tri-principy-skalovatelnosti-separace-volne-vazby-data) · [Interface, nebo dispatcher](komunikace-blueprintu.md#interface-nebo-dispatcher-a-kolik-doopravdy-stoji-cast) · [Design patterns: tři rodiny vzorů](../teorie/design-patterns.md#tri-rodiny-vzoru-tvorba-struktura-chovani) · [Rejstřík: Actor Component](../rejstrik.md#actor-component) · [Rejstřík: separation of concerns](../rejstrik.md#separation-of-concerns) · [Souboj jako dvě komponenty](souboj.md#dve-komponenty-misto-bojove-postavy-utocnik-a-terc) *(komponenty, které jednají samy — a kdy radši dispatcher)*

---

## Znovupoužitelné kostky a lepidlo: 70 ku 30

**Zdroj:** [Best Code Architectures For Indie Games](https://www.youtube.com/watch?v=8WqYQ1OwxJ4) · [Jonas Tyroller](https://www.youtube.com/channel/UC_p_9arduPuxM8DHTGIuSOg) · ~16 min, esej

**Shrnutí:** Autor otevírá poznámkou, která celé video zachraňuje před dogmatismem: *„většina her je pod kapotou čisté špagety. A je to v pořádku. Funguje-li to, funguje to."* Pak nabídne architekturu, kterou by sám příště použil, a je pozoruhodná tím, jak je konkrétní — včetně poměru. Háček, který je celé myšlence jádrem: **složitost uvnitř modulu je v pořádku, složitost mezi moduly ne.**

### Rozpad myšlenky

**Základní rozdělení** [(0:48)](https://www.youtube.com/watch?v=8WqYQ1OwxJ4&t=48s): **znovupoužitelné moduly** (systém pohybu, systém zdraví, spawner vln) — každý úplně nezávislý na ostatních, takže se dá vyměnit, znovu použít a má nízkou složitost. A k nim **lepidlo**: skripty, o kterých **předem víš, že je znovu nepoužiješ**, a jejichž jediná práce je ty moduly propojit.

A hned k tomu ukázka toho, co lepidlo **není**: dát systému zdraví referenci na systém pohybu a naopak. *„Ne, ne, ne. Tohle je špatná cesta. Teď už nejsou nezávislé. Teď jsi je svázal dohromady."*

**Poměr**, který je nejlépe zapamatovatelnou částí videa: **70 % znovupoužitelných kostek, 30 % lepidla.** *„Uděláš-li dobrou práci, zhruba takhle to skončí."*

**Obraz, který se drží** [(3:55)](https://www.youtube.com/watch?v=8WqYQ1OwxJ4&t=235s): **špagety musí zůstat na talíři.** Ne že by ve tvém kódu neměly být — mají zůstat **uvnitř modulu**. Ven z talíře nesmí. *„Odkazují-li se všechny moduly navzájem, mění se to v nepřehlednou změť."*

**A výjimka, kterou dodává sám**: jsou dva systémy, které se od sebe fakticky nedají oddělit (jeho příklad: zdraví a útok)? *„No a co. Prostě z toho udělej jeden systém."* Některé systémy prostě mají být jeden.

**Pravidlo palce, které funguje i bez znovupoužití** [(5:27)](https://www.youtube.com/watch?v=8WqYQ1OwxJ4&t=327s): **piš systémy se záměrem použít je v příštích projektech, i když je nepoužiješ.** *„I když je nikdy znovu nepoužiješ, pořád to má velkou výhodu — udržíš je uklizenější, modulárnější a nezávislejší."*

**A totéž o lepidle**: nechceš **jeden obří game manager**, který lepí všechno. V jejich hře jich mají **kolem třiceti** — každý s velmi malým a specializovaným úkolem, některé úplně drobné. *„Nikdy nechceš mít moc špaget na jednom místě."*

**Druhá zeď: kód proti datům** [(6:59)](https://www.youtube.com/watch?v=8WqYQ1OwxJ4&t=419s). Neměnná data (balanc, překlady) mají žít v databázi, ze které kód jen čte. Nejsrozumitelnější příklad jsou **překlady**: nikdo je nezadrátuje do kódu, protože ví, že by se to nedalo lokalizovat — *„a není důvod to dělat jen s překlady."*

K tomu poctivé přiznání vlastní chyby: v jejich hře je **balanc rozházený po celém projektu** — rychlost pohybu tady, cooldown tamhle — *„a je to docela otravné, protože všechna data jsou schovaná na náhodných místech."* Pravidlo, které z toho plyne: **co je navrhované spolu, ukládej spolu.** A rozvedení, které je vlastně o použitelnosti: **spokojený designér** má všechna čísla na jednom místě a může rychle zkoušet; **naštvaný designér** hledá hodiny. Vedlejší výhoda uspořádaných dat: **modderům stačí přidat data.** Autor jde místy tak daleko, že **navrhne databázi dřív, než má hru**.

**Špageta, které se nevyhneš** [(10:55)](https://www.youtube.com/watch?v=8WqYQ1OwxJ4&t=655s): **čas.** Každý systém se musí připojit k tomu, kdy se co spustí. Jeho současný přístup: **těsně řídit pořadí spouštění** — jeden skript, který volá všechny update události přesně v pořadí, které chce. *„Nemám proto moc rád události. Pro vizuál jsou v pohodě, ale u herní logiky nemám rád, když se mi kód spouští v náhodném pořadí, které nemůžu snadno ovládat."*

**A poslední vrstva: oddělit simulaci od zobrazení** [(12:32)](https://www.youtube.com/watch?v=8WqYQ1OwxJ4&t=752s), kterou sám označuje za pokročilejší. Simulace je **jen holý herní stav**; zobrazení ho **čte jako databázi v reálném čase** a vykresluje. Z pohledu simulace zobrazení **neexistuje**. Výsledek: dva skoro samostatné projekty uvnitř jednoho, žádný systém nedělá obojí — a čas je kritický jen pro simulaci.

> **Pozn.:** Nejužitečnější je to **rozdělení na kostky a lepidlo**, protože pojmenovává něco, s čím se lidé perou: rada „všechno má být znovupoužitelné" je nesplnitelná, protože propojení znovupoužitelné z definice není. Tenhle rámec říká **kolik toho smí být neznovupoužitelné a kde to má být** — a tím se z ideálu stane návrh. Souvisí to přímo s [třemi principy škálovatelnosti](#tri-principy-skalovatelnosti-separace-volne-vazby-data) a s [pravidlem 70/30](../zapisky/pravidlo-70-30.md), byť to druhé mluví o něčem jiném. Za pozornost stojí i to, že autor **nedoporučuje události pro herní logiku** — což jde proti většině rad v knihovně (i proti [event busu](../godot/signaly.md#event-bus-kdyz-se-systemy-nemaji-cim-potkat)). Není to spor: on řeší **determinismus pořadí**, ne provázanost. U hry, kde na pořadí vyhodnocení záleží (simulace, fyzika, souboj po snímcích), je ta výhrada namístě; u UI a vizuálu ne. Stojí za to obě rady držet vedle sebe a ptát se, **jestli u téhle konkrétní věci na pořadí záleží.**

**Souvislosti:** [Tři principy škálovatelnosti](#tri-principy-skalovatelnosti-separace-volne-vazby-data) · [Komponenty místo dědičnosti](#komponenty-misto-dedicnosti-skladej-misto-vetveni) · [Fragmenty: skládání položky z kusů](#fragmenty-skladani-polozky-z-kusu-misto-jedne-obri-tridy) · [Rejstřík: Data-driven design](../rejstrik.md#data-driven-design) · [Rejstřík: Loose coupling](../rejstrik.md#loose-coupling) · [Rejstřík: Separation of concerns](../rejstrik.md#separation-of-concerns) · [Tvorové, kteří poslouchají, ale nehlasují](niagara-vykon.md#zivy-svet-z-castic-tvorove-kteri-poslouchaji-ale-nehlasuji) *(oddělení simulace od zobrazení v praxi)*

---

## Třída jako data: CDO místo instancí

**Zdroj:** [Build a Scalable Inventory System — Part 1: The Foundation](https://www.youtube.com/watch?v=eocJvH15L4Q) a [Part 2: Item Definition](https://www.youtube.com/watch?v=8ylTGxeMR7w) · [Ali Elzoheiry](https://www.youtube.com/channel/UCrrZx9bh7RMYhXvaN8BrbNg) · ~23 + 45 min, kurz gameplay programování

**Shrnutí:** Série staví inventář podle vzoru z Lyry a začíná záměrně naivně: **položka je řetězec**. Do dvaceti minut je vidět, proč to nejde — ikona i mesh se přiřazují `switch`em na jméno, takže každá nová položka znamená úpravu na třech místech. Řešení není data table ani data asset, ale **třída použitá jako data**. Háček, který ten vzor umožňuje: **Unreal pro každou třídu vytvoří jednu výchozí instanci sám** — a z té se dá číst.

### Rozpad myšlenky

**Proč naivní verze selže** [(19:58)](https://www.youtube.com/watch?v=eocJvH15L4Q&t=1198s): kus dřeva není slovo „dřevo". Má kategorii, mesh, ikonu, použití při craftu — a hlavně **funkčnost**: lektvar léčí o 20 HP. *„Kde ta informace žije a kde žije ta funkčnost?"* V naivní verzi je zadrátovaná v `switch`ích rozesetých po projektu.

**Tři možnosti a proč zvolil třetí** [(20:45)](https://www.youtube.com/watch?v=eocJvH15L4Q&t=1245s): **data tables** jsou statické (nedá se k nim přidat funkčnost ani z nich dědit, všechno žije na jednom místě) · **data assety** jsou mnohem lepší (proměnné, funkce, potomci) · **třídy jako data** jsou tomu velmi blízko a je to cesta, kterou jde **Lyra**.

**Jak se to postaví** [(2:22)](https://www.youtube.com/watch?v=8ylTGxeMR7w&t=142s). `UItemDefinition` je obyčejný `UObject` v C++, ve kterém jsou **jen společné vlastnosti** (název, popis, ikona). Čtyři specifikátory na třídě dělají celý vzor: **`Blueprintable`** (dá se z ní dědit v blueprintu), **`BlueprintType`** (dá se použít jako typ proměnné), **`Abstract`** (sama se neobjeví v rozbalovacích nabídkách — jen její potomci) a **`Const`**. Na vlastnostech pak `EditDefaultsOnly` + `BlueprintReadOnly`, protože se **upravují jen výchozí hodnoty**.

Konkrétní položka (chléb, dřevo, lektvar) je pak **blueprintový potomek**, který nemá event graph — jen výchozí hodnoty. *„Otevřeš ho podruhé a otevře se ti to v režimu jen pro čtení. Je to velmi podobné data assetu."*

**A ta část, kvůli které to celé funguje** [(10:09)](https://www.youtube.com/watch?v=8ylTGxeMR7w&t=609s): z třídy se normálně data číst nedají, jen z vytvořeného objektu. Jenže *„Unreal Engine má tuhle opravdu skvělou věc: každá třída, každý `UObject`, má už vytvořenou výchozí instanci, které se říká **class default object**."* V blueprintech se k ní dostaneš uzlem **`Get Class Defaults`**, v C++ přes **`GetDefaultObject()`**. Takže se **nikdy nic nekonstruuje** — jen se předává třída a čtou se její výchozí hodnoty.

Praktický důsledek, který zazní mimochodem a je zásadní: *„nemusíš předávat objektové reference data assetů. Předáváš jedinou třídu."*

> **Pozn.:** Tenhle vzor je zajímavý hlavně tím, **jak se liší od data assetu, přestože vypadá stejně** — a rozdíl je v tom, co se předává dál. Reference na data asset je odkaz na **objekt**, a objekt se musí načíst; reference na třídu je odkaz na **třídu**, jejíž CDO v paměti stejně už je. To je táž úvaha, kterou má knihovna u [tvrdých referencí a Size Mapu](pamet-a-instance.md#size-map-v-rezimu-pameti-co-drzi-tvuj-blueprint), jen s příjemnějším koncem. Za pozornost stojí i **pedagogický postup celé série**: autor nejdřív postaví naivní verzi a **nechá ji selhat na obrazovce**, teprve pak nabídne vzor. To je násobně účinnější než začít správným řešením — a je to stejná technika jako [strhnout kontext a podívat se, co zbylo](../teorie/ludonarativni-soulad.md#kontext-tataz-mechanika-jiny-zazitek). Vlastní výhrada: **CDO je globální a sdílené.** Cokoli, co se má lišit mezi kusy téže položky (opotřebení, počet nábojů, vlastník), do něj nepatří a musí žít v instanci inventáře — a v tom se dá při přebírání toho vzoru snadno uklouznout.

**Souvislosti:** [Fragmenty: skládání položky z kusů](#fragmenty-skladani-polozky-z-kusu-misto-jedne-obri-tridy) · [Inventář: definice popisuje druh, instance nese kus](inventar.md#definice-popisuje-druh-instance-nese-kus) *(kam s tím, co se liší mezi kusy)* · [Znovupoužitelné kostky a lepidlo](#znovupouzitelne-kostky-a-lepidlo-70-ku-30) · [Paměť a instancování: Size Map](pamet-a-instance.md#size-map-v-rezimu-pameti-co-drzi-tvuj-blueprint) · [Ukládání](ukladani.md) · [Rejstřík: CDO](../rejstrik.md#cdo) · [Rejstřík: Data asset](../rejstrik.md#data-asset) · [Rejstřík: Hard reference](../rejstrik.md#hard-reference)

---

## Fragmenty: skládání položky z kusů místo jedné obří třídy

**Zdroj:** [Build a Scalable Inventory System — Part 2: Item Definition](https://www.youtube.com/watch?v=8ylTGxeMR7w) · [Ali Elzoheiry](https://www.youtube.com/channel/UCrrZx9bh7RMYhXvaN8BrbNg) · ~45 min, kurz gameplay programování

**Shrnutí:** Druhá polovina vzoru řeší otázku, kterou třída jako data sama nevyřeší: **ne všechny položky mají totéž.** Ne všechno má mesh ve světě, ne všechno se dá vybavit, ne všechno se stohuje. Odpověď je kompozice — **fragment** je objekt, který k položce připojí kus dat a kus funkčnosti. Háček, kvůli kterému to musí být v C++: **celý vzor stojí na třech specifikátorech, které v blueprintu nejsou.**

### Rozpad myšlenky

**Proč ne jedna velká třída** [(17:52)](https://www.youtube.com/watch?v=8ylTGxeMR7w&t=1072s): *„některé položky se dají stohovat, na některé se dá kliknout a použít je, některé se dají zahodit, jiné ne. Kdybychom se pokusili dát všechny informace do jedné třídy, byla by gigantická a plná informací, které jsou užitečné třeba pro jednu jedinou položku."*

Řešení: `UItemDefinition` drží **pole fragmentů**. Je-li položka vybavitelná, připojíš fragment vybavení. Má-li reprezentaci ve světě, připojíš fragment světové reprezentace. *„Každý fragment přichází s vlastními daty a vlastní funkčností."*

**Tři specifikátory, které to dělají použitelné** [(20:16)](https://www.youtube.com/watch?v=8ylTGxeMR7w&t=1216s), a stojí za to je znát, protože bez nich je z toho jen teoreticky hezký vzor:

| specifikátor | co dělá | proč to potřebuješ |
|---|---|---|
| **`DefaultToInstanced`** | instance třídy se při vytvoření duplikují | fragment patří té položce, která ho vytvořila |
| **`EditInlineNew`** | objekt se dá vytvořit **přímo v okně vlastností** editoru | přidáš fragment tlačítkem `+` v assetu místo zakládání samostatného souboru |
| **`Instanced`** (na tom poli) | každá instance dostane **vlastní kopii** objektu | chléb a dřevo nesmí sdílet tentýž mesh |

Autor to shrnuje názorně: bez toho *„bys musel vytvořit blueprint typu world representation, nastavit mu mesh, a teprve ten použít jako ukazatel. Tohle tomu všemu předchází."*

**Jak se fragment najde** [(29:49)](https://www.youtube.com/watch?v=8ylTGxeMR7w&t=1789s) — a tady se ukáže drobná nepříjemnost: `Get Class Defaults` v blueprintu **instancované vlastnosti nezobrazí**, takže pole fragmentů takhle nepřečteš. Musí se dopsat **statická funkce** `FindFragmentByClass(itemDefinition, fragmentClass)`, která si vytáhne CDO, projde pole a vrátí první fragment odpovídající třídy. Statická je proto, že *„nikdy nevytváříme instanci item definition — vždycky ji používáme jako třídu."*

**A specifikátor, který z toho udělá pohodlí** [(37:33)](https://www.youtube.com/watch?v=8ylTGxeMR7w&t=2253s): **`meta = (DeterminesOutputType = "FragmentClass")`**. Bez něj funkce vrací rodičovský typ a v blueprintu bys musel castovat. S ním se **návratový typ uzlu změní podle třídy, kterou do něj zapojíš** — vybereš world representation a uzel začne vracet world representation. *„Krásný specifikátor. Žádné castování."*

> **Pozn.:** Tohle je **kompozice místo dědičnosti** dotažená do konce a v knihovně to má sourozence na obou stranách: [komponenty místo dědičnosti](#komponenty-misto-dedicnosti-skladej-misto-vetveni) v UE a [has-a místo is-a](../godot/kompozice.md#has-a-misto-is-a-hrdinuv-batoh) v Godotu. Nové je tady to, že se skládá **datový popis**, ne chování aktéra — a že tím zmizí celá kategorie problému: nikdy nevznikne třída `ZbranKteraSeDaSnistAJeZaroveňKlic`. Praktické měřítko, které z toho plyne a autor ho neříká přímo: **vlastnost patří do fragmentu, jakmile ji nemá aspoň polovina položek.** Za pozornost stojí i to, že celý vzor je vlastně **licencovaný z Lyry** — což je dobrá připomínka, že [ukázkové projekty Epicu](gasp.md) nejsou jen hračky, ale zdroj hotových architektonických rozhodnutí. Vlastní výhrada: fragmenty **posunou složitost, nezruší ji**. Deset fragmentů znamená deset míst, kde se dá udělat chyba, a nováček v projektu musí nejdřív zjistit, které existují — takže k tomu patří dokumentace nebo aspoň editor script, který je vypíše.

**Souvislosti:** [Třída jako data](#trida-jako-data-cdo-misto-instanci) · [Komponenty místo dědičnosti](#komponenty-misto-dedicnosti-skladej-misto-vetveni) · [Inventář: použití jako seznam akcí](inventar.md#pouziti-jako-seznam-akci-chovani-slozene-z-malych-kroku) *(fragment, který nese chování)* · [Godot: has-a místo is-a](../godot/kompozice.md#has-a-misto-is-a-hrdinuv-batoh) · [Interakce s předměty](interakce-predmety.md) · [Rejstřík: Fragment](../rejstrik.md#fragment) · [Rejstřík: CDO](../rejstrik.md#cdo) · [Rejstřík: Data-driven design](../rejstrik.md#data-driven-design) · [Fragment v Mass](mass-ecs.md#entita-neni-actor-rozkladej-podle-pristupu-do-pameti-ne-podle-postavy) *(jiný význam téhož slova)*
