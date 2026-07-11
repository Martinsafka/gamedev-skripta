# Karta selhání: packaging visel na posledních dvou shaderech

**Kontext:** První packaging test buildu IZBY pro kolegy, UE 5.7, Windows stroj s VS 2022 (C++ game dev workload), i7-12700KF + RTX 4070. Odpoledne, které mělo skončit odeslaným buildem — a místo toho zrodilo formát, kterým teď zapisuju technická selhání.

## Co se stalo

Packaging doběhl na **19 100 z 19 102 shader jobů** — a tam stál přes tři hodiny. Log každých patnáct minut opakoval `No shader compile worker state change in 900.00 seconds`; engine sám nakonec ohlásil `Hung shadermap detected: 7200 s`. Zaseknuté byly poslední dva globální shadery (`VirtualShadowMapProjection`, `StochasticLightingTileClassification`).

**Slepá ulička:** „Je to normální, první cook prostě trvá." Nejzákeřnější možná, protože **je to pravda** — symptom nemá tvar chyby, má tvar čekání. Bez přečtení logu by následovaly klasické zastávky (smazat Intermediate a DDC, podezřívat těžké assety, přeinstalovat engine) — všechny mimo.

**Skutečná příčina:** IncrediBuild. Instalátor VS 2022 ho u C++ game dev workloadu přibalí **defaultně zaškrtnutý**; běžel bez licence ve standalone módu, Unreal ho detekoval a routoval přes něj kompilaci shaderů (XGE Controller). Workery opakovaně padaly na access violation (`0xC0000005`) a zaseknuté joby se už nikdy nepřeplánovaly. Log to říkal celou dobu: `License not activated` … `Using XGE Controller for shader compilation`.

**Fix:** zrušit packaging → v Task Manageru dorazit sirotky (`UnrealEditor-Cmd.exe` — pozor, *ne* `UnrealEditor.exe`; všechny `ShaderCompileWorker.exe`; `dotnet.exe` s AutomationTool), protože drží zámky na souborech a rozbily by další pokus → odinstalovat IncrediBuild (alternativy: vypnout XGE Controller plugin, nebo `r.XGEController.Enabled=0` v `ConsoleVariables.ini`) → spustit znovu. Hotové shadery seděly v DDC — doběhlo to za minuty.

**Baseline pro příště:** první cook je dominovaný shadery — na téhle sestavě typicky 15–60 minut, těžká scéna i přes hodinu; každý další packaging bere shadery z DDC a trvá jednotky minut. Diagnostika visení: stejné pending joby + opakované „no state change" = **není na co čekat**. Řetěz procesů pro úklid: editor → AutomationTool (`dotnet`) → `UnrealEditor-Cmd` (cook) → `ShaderCompileWorker` děti.

## Co si z toho beru

Ze záseku vznikla šablona **karty selhání**, kterou od té doby plním:

> *Název (ve tvaru symptomu) → Kontext → Čekal jsem / Stalo se → Zevnitř (jedna věta, jak to bylo cítit) → Slepá ulička → Skutečná příčina → Fix → Baseline pro příště.*

Definice formátu jednou větou: **citelné je ta věta zevnitř a účet v hodinách; čitelné je všechno ostatní.** Dvě doplňkové pointy: „nemám k tomu zápis, jen jsme to řešili v konverzaci" neplatí — konverzace, ve které se problém řešil, je surovina *lepší* než dodatečný zápis, protože zachovává pořadí myšlenek včetně slepých uliček. A karty se dají obrátit v pedagogiku: dej někomu symptom a kontext, nech ho hádat příčinu, pak reveal — kvíz vyrobený z vlastních jizev.

> **Pozn.:** U nástrojů (na rozdíl od her) patří vedle karet selhání ještě ADR — architecture decision records („zvolil jsem X místo Y, protože Z"), protože u nástrojů jsou selhání hlavně designová rozhodnutí, ne runtime záseky.

**Souvislosti:** [Selhávat citelně a čitelně](selhavat-citelne-a-citelne.md) *(karta je ta filozofie přeložená do formuláře)* · [Praxe: optimalizace scény](../praxe/optimalizace.md) *(kde žijí shader/výkonová témata z playlistu)* · [Rejstřík: draw call](../rejstrik.md#draw-call) · [Rejstřík: tutorial hell](../rejstrik.md#tutorial-hell) *(protipól: učit se z vlastních zásek, ne jen z cizích návodů)*
