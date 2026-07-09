# Telemetrie: co hráč dělá — lokálně i vzdáleně

Dvě patra téže otázky „co se ve hře děje": **lokální activity tracker** (Ryan Laley) — gameplay tagy hlášené centrálnímu systému, palivo pro achievementy, statistiky a tutorialy — a **vzdálená analytika** (DevEdge Studio) — TrackEdge + PostHog, tedy reálná data od reálných hráčů v dashboardu.

---

## Activity tracker: gameplay tagy jako záznam činnosti

**Zdroj:** [Unreal Engine 5 Tutorial - Stats and Achievements Part 1: Activity Tracker](https://www.youtube.com/watch?v=9iWSVZoADpo) · [Ryan Laley](https://www.youtube.com/channel/UCsS5i15vvUbwfr_1JdRKCAA) · ~13 min, díl 1 série o achievementech

**Shrnutí:** Než postavíš achievementy, potřebuješ vědět, *co hráč dělá*. Autorův vzor [(0:23)](https://www.youtube.com/watch?v=9iWSVZoADpo&t=23s): strom tagů `Activity.*`, centrální funkce `RecordActivity` v Game Mode a event dispatcher, na který se věší cokoli — čítače statistik, achievement manager i tutorial.

### Rozpad myšlenky

**Tagy jako slovník činností** [(1:26)](https://www.youtube.com/watch?v=9iWSVZoADpo&t=86s): v Gameplay Tag Manageru vznikne kategorie `Activity` a pod ní libovolně jemné větve — `Activity.PlayerActions.Jump`, `.FellFromHeight`, `Activity.Tutorial.Move`, `.LearnControls` [(2:00)](https://www.youtube.com/watch?v=9iWSVZoADpo&t=120s). Přidávej bez zábran; hierarchie z [kapitoly o tazích](gameplay-tags.md) se hodí i tady (dotaz na `Activity.Tutorial` chytí celý tutorial).

**Centrální příjem** [(3:50)](https://www.youtube.com/watch?v=9iWSVZoADpo&t=230s): Game Mode (u multiplayeru spíš Game State [(3:56)](https://www.youtube.com/watch?v=9iWSVZoADpo&t=236s)) dostane funkci `RecordActivity(ActivityTag)` [(4:27)](https://www.youtube.com/watch?v=9iWSVZoADpo&t=267s), která okamžitě zavolá dispatcher `OnActivity` [(4:49)](https://www.youtube.com/watch?v=9iWSVZoADpo&t=289s) — „stalo se tohle, koho to zajímá" ([vzor z komunikace](komunikace-blueprintu.md#tri-kanaly-a-kdy-ktery-cast-interface-event-dispatcher)). Aby hlásit mohl kdokoli dvěma uzly, obal volání do **common function library** [(5:47)](https://www.youtube.com/watch?v=9iWSVZoADpo&t=347s). Hlásit pak jde odkudkoli: trigger volume v level blueprintu ohlásí `Tutorial.LearnControls` [(6:57)](https://www.youtube.com/watch?v=9iWSVZoADpo&t=417s), jump v characteru ohlásí skok [(9:34)](https://www.youtube.com/watch?v=9iWSVZoADpo&t=574s).

**Počítání**: mapa `GameplayTag → Integer` v Game Mode [(9:56)](https://www.youtube.com/watch?v=9iWSVZoADpo&t=596s) — na každý record najdi a inkrementuj [(10:37)](https://www.youtube.com/watch?v=9iWSVZoADpo&t=637s). Tím má systém tři odběratele zadarmo: statistiky (kolikrát skočil), achievementy (další díl série staví achievement manager poslouchající tagy [(11:50)](https://www.youtube.com/watch?v=9iWSVZoADpo&t=710s)) a tutorial (tag `LearnControls` může zavřít nápovědu). Čítač napojený na [SaveGame](ukladani.md) přežije i restart.

> **Pozn.:** Všimni si, jak se tu skládá celý batch: tagy (slovník) + dispatcher (doručení) + game mode (kde bydlí) + function library (přístup) + save (persistence). Activity tracker je vlastně cvičebnice architektury z [principů](principy-architektury.md) — a zároveň přesně ten druh systému, který se staví, *až když* hra existuje ([žrouti času](../teorie/produktivita.md) posílají pozdravy).

**Souvislosti:** [Gameplay Tags](gameplay-tags.md) · [Komunikace Blueprintů](komunikace-blueprintu.md) · [Ukládání](ukladani.md) · [Rejstřík: telemetrie](../rejstrik.md#telemetrie)

---

## Vzdálená analytika: TrackEdge + PostHog

**Zdroj:** [How to Track Player Behavior in Unreal Engine 5 (TrackEdge + Post Hog)](https://www.youtube.com/watch?v=o0HlCeQXxAQ) · [DevEdge Studio](https://www.youtube.com/channel/UCGa0hsNw3BK6xTDnVvfFltw) · ~13 min, setup průvodce

**Shrnutí:** Jakmile hru hrají cizí lidé, print stringy nestačí — chceš vidět, co dělají, ve svém dashboardu. TrackEdge je UE plugin [(0:25)](https://www.youtube.com/watch?v=o0HlCeQXxAQ&t=25s), PostHog analytický backend; propojení je API klíč + URL [(1:08)](https://www.youtube.com/watch?v=o0HlCeQXxAQ&t=68s) a první event odejde za deset minut. (Autor videa je zároveň autor pluginu — ber jako představení nástroje.)

### Rozpad myšlenky

**Tři druhy dat:** *Person properties* [(2:21)](https://www.youtube.com/watch?v=o0HlCeQXxAQ&t=141s) — metadata hráče: verze enginu, OS, jazyk, platforma, projekt [(2:28)](https://www.youtube.com/watch?v=o0HlCeQXxAQ&t=148s); posílá se jednou (Create TrackEdge Manager → Set Person Properties). *Eventy s vlastnostmi* [(4:48)](https://www.youtube.com/watch?v=o0HlCeQXxAQ&t=288s) — `Track Event with Properties` s mapou hodnot: obtížnost (enum [(5:10)](https://www.youtube.com/watch?v=o0HlCeQXxAQ&t=310s)), level, typ postavy — cokoli, co chceš později filtrovat. *Sessions* [(7:20)](https://www.youtube.com/watch?v=o0HlCeQXxAQ&t=440s) — `Start/End Custom Session` (jména se musí shodovat [(7:57)](https://www.youtube.com/watch?v=o0HlCeQXxAQ&t=477s)) měří trvání: v demu 28,8 s hraní [(9:26)](https://www.youtube.com/watch?v=o0HlCeQXxAQ&t=566s).

**Co dostaneš v PostHogu:** persistentní ID hráče na zařízení [(10:05)](https://www.youtube.com/watch?v=o0HlCeQXxAQ&t=605s) (opakovaná spuštění se nespojí do nových identit), *People & Groups* s historií každého hráče [(10:12)](https://www.youtube.com/watch?v=o0HlCeQXxAQ&t=612s) a **dashboardy** [(10:56)](https://www.youtube.com/watch?v=o0HlCeQXxAQ&t=656s) — grafy, čísla, tabulky nad vlastními eventy. Free tier: milion eventů měsíčně [(12:01)](https://www.youtube.com/watch?v=o0HlCeQXxAQ&t=721s) — pro indie hru prakticky zadarmo.

> **Pozn.:** Dvě věci k rozmyšlení předem. **Soukromí:** person properties zahrnují i polohu na úrovni města — pro reálné vydání to znamená privacy policy a souhlas (GDPR); posílej jen, co skutečně potřebuješ. **Co měřit:** ideálně napoj vzdálenou telemetrii na *už existující* activity tagy z první myšlenky — jeden slovník událostí, dva odběratelé (lokální čítač + PostHog). A vzpomeň na [the Gap](../teorie/rady-z-praxe.md#the-gap-rozdil-mezi-to-je-hezky-a-tohle-musim-hrat): telemetrie je čisté *chování* hráčů — přesně ta měna, které se dá věřit víc než slovům.

**Souvislosti:** [Activity tracker výše](#activity-tracker-gameplay-tagy-jako-zaznam-cinnosti) · [Idea iceberg: the Gap](../teorie/rady-z-praxe.md#the-gap-rozdil-mezi-to-je-hezky-a-tohle-musim-hrat) · [Postmortem ShantyTown](../teorie/postmortem-shantytown.md) *(QA a balanc map z dat)* · [Rejstřík: telemetrie](../rejstrik.md#telemetrie)
