# AI agenti: Claude Code a MCP v enginu

Rok 2026 přinesl do Unrealu **agentní AI**: 5.8 má nativní **MCP** (Model Context Protocol) a AI agent s přístupem do editoru staví blueprinty, materiály i celé levely. Kapitola jde od setupu přes poctivé stress testy až po největší lekci celého tématu: **agent je násobič pro toho, kdo věcem rozumí** — obecný prompt dá obecný výsledek. Generování assetů (obrázky → 3D) řeší [sesterská kapitola](ai-assety.md).

---

## Nativní MCP v 5.8: setup a první testy

**Zdroj:** [How to Setup Claude Code in Unreal Engine 5.8 (Easy)](https://www.youtube.com/watch?v=0tzXVwDxzt8) · [Unreal University](https://www.youtube.com/channel/UCQv4mwerZLQVe3wPbsMc-qw) · ~6 min · + [NEW Unreal Engine 5.8 MCP Tutorial (QuickStart Guide)](https://www.youtube.com/watch?v=PqrKqhkj3gQ) · [Smart Poly](https://www.youtube.com/channel/UCp1e34nrTQqVXkNU5ekH9CQ) · ~12 min, tutoriály

**Shrnutí:** UE 5.8 umí připojit AI agenta (Claude Code, ale i Codex, Gemini či Cursor) přímo do editoru — agent pak vidí kontext projektu a sahá na blueprinty, PCG, materiály i level design [(0:01)](https://www.youtube.com/watch?v=PqrKqhkj3gQ&t=1s). Epic to na Unreal Festu předvedl agentem, který postavil celé město přes PCG graf a assety z content browseru [(0:01)](https://www.youtube.com/watch?v=PqrKqhkj3gQ&t=1s).

### Rozpad myšlenky

**Tři pluginy:** Edit → Plugins → zapnout **Unreal MCP**, **Terminal** a **Editor Toolset** — poslední je ten důležitý most: dává agentovi kontrolu nad aktory, blueprinty a systémy editoru [(0:49)](https://www.youtube.com/watch?v=0tzXVwDxzt8&t=49s) [(2:19)](https://www.youtube.com/watch?v=PqrKqhkj3gQ&t=139s). Pak Editor Preferences → **Model Context Protocol → Auto Start Server** [(3:05)](https://www.youtube.com/watch?v=PqrKqhkj3gQ&t=185s) a v nastavení Terminalu tři startup příkazy: barvy, `cd "cesta k projektu"` (najdeš přes right-click na Content folder → Show in Explorer) a `claude` [(3:52)](https://www.youtube.com/watch?v=PqrKqhkj3gQ&t=232s).

**Agent a config:** Claude Code se instaluje příkazem z oficiální dokumentace (Windows chce Git for Windows) a přidává do PATH [(5:25)](https://www.youtube.com/watch?v=PqrKqhkj3gQ&t=325s) [(6:11)](https://www.youtube.com/watch?v=PqrKqhkj3gQ&t=371s); konzolový příkaz v editoru pak vygeneruje **`.mcp.json`** — pro jiné agenty (Cursor, VS Code, Gemini, Codex) má dokumentace vlastní varianty [(8:32)](https://www.youtube.com/watch?v=PqrKqhkj3gQ&t=512s). Po restartu Tools → Terminal ohlásí „new MCP server found" [(9:18)](https://www.youtube.com/watch?v=PqrKqhkj3gQ&t=558s). Prakticky: free účet je omezený, reálná práce chce placený tarif; modely se přepínají (default bývá nižší tier) [(7:46)](https://www.youtube.com/watch?v=PqrKqhkj3gQ&t=466s) [(10:51)](https://www.youtube.com/watch?v=PqrKqhkj3gQ&t=651s).

**První testy — a první lekce:** „pět barevných kostek na sobě" dopadlo vzorně — agent vytvořil static mesh aktory a **material instances z basic master materiálu**, ne pět unikátních materiálů [(10:51)](https://www.youtube.com/watch?v=PqrKqhkj3gQ&t=651s). „Rotující červená kostka" už ne: rotace nefungovala, dokud autor ručně nepřepnul mobility na movable, a červená se cestou ztratila [(4:49)](https://www.youtube.com/watch?v=0tzXVwDxzt8&t=289s). Obojí ilustruje totéž: výsledky jsou působivé, ale **kontrola člověkem zůstává součást pipeline** [(5:36)](https://www.youtube.com/watch?v=0tzXVwDxzt8&t=336s).

> **Pozn.:** Oba autoři opakují stejnou podmínku: znej základy enginu, než si pustíš agenta — AI dělá chyby a bez vlastní diagnózy se v nich utopíš [(0:02)](https://www.youtube.com/watch?v=0tzXVwDxzt8&t=2s). To je tatáž rada jako v [Jak se učit engine](editor-tipy.md#jak-se-ucit-engine-rady-po-peti-letech) — agent nezkracuje učení, zkracuje práci naučených.

**Souvislosti:** [Editor tipy: jak se učit engine](editor-tipy.md#jak-se-ucit-engine-rady-po-peti-letech) · [Rejstřík: MCP](../rejstrik.md#mcp)

---

## Komunitní cesta v 5.7: endless runner jako stress test

**Zdroj:** [Claude Code Took Over Unreal Engine 5 and Built a Game](https://www.youtube.com/watch?v=iRcrZjOt5H8) · [Stefan 3D AI](https://www.youtube.com/channel/UCRW08KcTVjXEmBzBsVl7XjA) · ~17 min, test s postupem

**Shrnutí:** Před nativním MCP vede cesta přes komunitní pluginy — po měsíci zkoušení („spousta odpadu, některé drahé") autor doporučuje dvojici zdarma: **Unreal Claude** (screenshoty a hýbání objekty) + **Vibe UE** (editace blueprintů, Python skripty) [(0:00)](https://www.youtube.com/watch?v=iRcrZjOt5H8&t=0s) [(1:33)](https://www.youtube.com/watch?v=iRcrZjOt5H8&t=93s). Stress test: postavit endless runner — a z něj plyne nejcennější lekce celé kapitoly o promptování.

### Rozpad myšlenky

**Setup deleguj agentovi:** Claude Code otevřený ve složce projektu si oba pluginy i závislosti (node, C++ knihovny) nainstaluje sám — stačí mu hodit odkazy [(0:47)](https://www.youtube.com/watch?v=iRcrZjOt5H8&t=47s) [(2:19)](https://www.youtube.com/watch?v=iRcrZjOt5H8&t=139s); instrukce se ukládají do **CLAUDE.md**, který šetří tokeny při dalších sezeních [(3:05)](https://www.youtube.com/watch?v=iRcrZjOt5H8&t=185s). A **Git od první minuty**: commit na každém milníku, snadné reverty — „AI agenti s verzováním pracují výborně" (a Claude Git klidně i nainstaluje) [(4:38)](https://www.youtube.com/watch?v=iRcrZjOt5H8&t=278s) [(5:24)](https://www.youtube.com/watch?v=iRcrZjOt5H8&t=324s).

**Stavba hry:** úklid scény (agent se ptá rozumné otázky — nechat světla?) [(6:11)](https://www.youtube.com/watch?v=iRcrZjOt5H8&t=371s), nekonečná dráha z dlaždic (BP_RunnerTile se smysluplnými proměnnými), autoběh, tři lajny na A/D, překážky, mince, UI se skóre [(6:57)](https://www.youtube.com/watch?v=iRcrZjOt5H8&t=417s) [(9:15)](https://www.youtube.com/watch?v=iRcrZjOt5H8&t=555s) [(11:34)](https://www.youtube.com/watch?v=iRcrZjOt5H8&t=694s). Nejzajímavější moment: agent **sám spouští hru, dělá si screenshoty a kontroluje se** [(6:57)](https://www.youtube.com/watch?v=iRcrZjOt5H8&t=417s). Cena reálná: mince + randomizace = 15 minut a 14 000 tokenů Opus 4.8 [(11:34)](https://www.youtube.com/watch?v=iRcrZjOt5H8&t=694s). Grafy fungují, ale layout je špagetový a ani na žádost ho agent neuklidí [(7:43)](https://www.youtube.com/watch?v=iRcrZjOt5H8&t=463s).

**Lekce o promptech:** obecné zadání → agent zvolí *nejrychlejší* cestu, ne škálovatelnou; **rozepiš logiku a koncepty a výsledky skočí o třídu výš** [(10:02)](https://www.youtube.com/watch?v=iRcrZjOt5H8&t=602s). „Je to boost pro ty, kdo věcem rozumějí" — a začátečníkům neradí agenta odložit, ale učit se s ním: ptej se proč, nech si vysvětlit architekturu [(10:48)](https://www.youtube.com/watch?v=iRcrZjOt5H8&t=648s). Assety agentovi nepatří: obrázky generuj jinde, připrav je — **agent je na logiku a organizaci, ne na placement** [(15:24)](https://www.youtube.com/watch?v=iRcrZjOt5H8&t=924s).

> **Pozn.:** Debugging přes screenshoty funguje (bug s game over při úkroku, mezery mezi dlaždicemi) [(14:38)](https://www.youtube.com/watch?v=iRcrZjOt5H8&t=878s) — ale vizuální kontrola stojí tokeny; viz [72hodinová hra](#72-hodin-delba-prace-clovekai) pro dotažení téhle ekonomie.

**Souvislosti:** [72 hodin: dělba práce](#72-hodin-delba-prace-clovekai) · [Rejstřík: MCP](../rejstrik.md#mcp) · [Rejstřík: version control](../rejstrik.md#version-control)

---

## Agent v Blenderu a ComfyUI: lokální pipeline

**Zdroj:** [Claude Took Over ComfyUI + Blender: Here's What Happened](https://www.youtube.com/watch?v=KdYv_TT-ZnQ) · [PixelArtistry](https://www.youtube.com/channel/UCRGb8yCnI5-upL3hT4oiOZw) · ~23 min, tutoriál

**Shrnutí:** Agent nepatří jen do Unrealu: **Blender MCP** (oficiální add-on) + **ComfyUI MCP** propojí Clauda s lokálním generováním — „postav mi středověký kit deseti propů, obrázky přes z-image, 3D přes Trellis 2, importuj do Blenderu a rozmísti do levelu" pak běží samo, včetně hlášení průběhu a oprav vlastních chyb [(7:03)](https://www.youtube.com/watch?v=KdYv_TT-ZnQ&t=423s) [(8:36)](https://www.youtube.com/watch?v=KdYv_TT-ZnQ&t=516s).

### Rozpad myšlenky

**Setup:** Blender 5.1+ má MCP add-on (drag & drop, ověřit v Preferences → Add-ons, server musí běžet) [(0:50)](https://www.youtube.com/watch?v=KdYv_TT-ZnQ&t=50s) [(1:37)](https://www.youtube.com/watch?v=KdYv_TT-ZnQ&t=97s); ComfyUI MCP z GitHubu se přidá do configu Claude desktopu (Settings → Developer → Edit Config) a Blender se doinstaluje přes Extensions [(2:25)](https://www.youtube.com/watch?v=KdYv_TT-ZnQ&t=145s) [(3:57)](https://www.youtube.com/watch?v=KdYv_TT-ZnQ&t=237s). Sanity check klasika: „smaž kostku a vytvoř novou jménem test succeeded" [(4:44)](https://www.youtube.com/watch?v=KdYv_TT-ZnQ&t=284s).

**Workflow jako slovník agenta:** ComfyUI workflow exportuj jako **API formát** (File → Export API; zapnout API nodes v settings) a hoď Claudovi se zprávou „načti tenhle JSON a připrav ho pro ComfyUI MCP" — od té chvíle umí workflow volat s vlastními prompty [(5:30)](https://www.youtube.com/watch?v=KdYv_TT-ZnQ&t=330s) [(6:17)](https://www.youtube.com/watch?v=KdYv_TT-ZnQ&t=377s). Stylovou jednotu kitů udrží LoRA [(7:49)](https://www.youtube.com/watch?v=KdYv_TT-ZnQ&t=469s); rozmazaná země se spravila třetím workflow (Trellis Splat na gaussian splat) stejným postupem [(9:22)](https://www.youtube.com/watch?v=KdYv_TT-ZnQ&t=562s).

**Cleanup vzor (nejpřenositelnější kus):** prompt „vyčisti importovaný mesh: merge vertices, oprav scale, retopo přes Quad Remesher, udělej low poly a **zapeč texturu z high na low (normal + base color)**" — „Claude je v bakingu opravdu dobrý" a hlavně si kroky **pamatuje**: další model projde stejnou linkou jedním příkazem [(10:08)](https://www.youtube.com/watch?v=KdYv_TT-ZnQ&t=608s) [(11:41)](https://www.youtube.com/watch?v=KdYv_TT-ZnQ&t=701s). Poctivá hranice: pokažené oko po remeshi zkusil nechat opravit agenta, ten se zacyklil — ručně to bylo rychlejší [(12:28)](https://www.youtube.com/watch?v=KdYv_TT-ZnQ&t=748s).

**Animace:** **Kimodo Blender Bridge** add-on (i na 6 GB VRAM přes cestu k venv Pythonu) a prompt „vygeneruj 5 různých animací, 5× duplikuj postavu a retargetuj přes Rokoko add-on" — agent pohyby sám vymyslí, spustí i retargetuje; clipující ruce = nedokonalá T-póza, ne chyba nástroje [(14:02)](https://www.youtube.com/watch?v=KdYv_TT-ZnQ&t=842s) [(20:17)](https://www.youtube.com/watch?v=KdYv_TT-ZnQ&t=1217s) [(21:50)](https://www.youtube.com/watch?v=KdYv_TT-ZnQ&t=1310s).

> **Pozn.:** Část videa o Rodin Gen 2.5 je **sponzorovaný segment** (hero postavy, smart low poly, 12K textury) — nástroj je reálný, ale čti to jako inzerci [(15:35)](https://www.youtube.com/watch?v=KdYv_TT-ZnQ&t=935s). Autorův verdikt k agentům sedí s ostatními: generování trvá, síla je v **pipeline, kterou agenta naučíš** — a v debuggingu instalací, kde je Claude výborný [(22:36)](https://www.youtube.com/watch?v=KdYv_TT-ZnQ&t=1356s). Kimodo samotné rozebírá [AI assety](ai-assety.md#animace-a-2d-kimodo-a-pixellab). *(V indexu přeřazeno ze slugu ai-assets — obsahově patří k agentům.)*

**Souvislosti:** [AI assety: Kimodo](ai-assety.md#animace-a-2d-kimodo-a-pixellab) · [Rejstřík: MCP](../rejstrik.md#mcp) · [Rejstřík: retopologie](../rejstrik.md#retopologie)

---

## 72 hodin: dělba práce člověk–AI

**Zdroj:** [I Built My Dream Game in 72 Hours — Assets by AI, Gameplay by Claude Code](https://www.youtube.com/watch?v=k9cbm5jSOxk) · [Stefan 3D AI](https://www.youtube.com/channel/UCRW08KcTVjXEmBzBsVl7XjA) · ~35 min, case study

**Shrnutí:** Vysněná 3D plošinovka à la Mario 64 / Banjo-Kazooie — liščí onsen inspirovaný Cestou do fantazie — za tři dny. Teze videa: „tohle **není** video, kde AI všechno vyřeší jedním promptem; AI je nástroj" [(0:46)](https://www.youtube.com/watch?v=k9cbm5jSOxk&t=46s). Dělba, která z toho plyne, je nejlepší mapa celého tématu: **assety AI nástroji, kompozice a placement ručně, logika agentem**.

### Rozpad myšlenky

**Den 1–2 — svět:** z konceptu se extrahují party (Asset Hub), generují 3D modely (Tripo/Hunyuan) a **skládají ručně v Blenderu** — „Lego pro dospělé vývojáře"; celý level zabral den [(2:19)](https://www.youtube.com/watch?v=k9cbm5jSOxk&t=139s) [(13:38)](https://www.youtube.com/watch?v=k9cbm5jSOxk&t=818s) (detaily pipeline v [AI assetech](ai-assety.md)). V UE pak third-person šablona, koupené stavební kameny z vlastní knihovny (Stylized Water, Ultra Dynamic Sky), hory zdarma z Fabu a mlha přes volume scattering [(16:22)](https://www.youtube.com/watch?v=k9cbm5jSOxk&t=982s) [(17:54)](https://www.youtube.com/watch?v=k9cbm5jSOxk&t=1074s). **Proč placement ručně:** vizuální rozpoznávání agentů je zatím slabé — autor suše konstatuje, že nejlíp mu viděl „Fable 5, ale nevím, jestli ho ještě uvidíme", a rozdíly mezi agenty jsou u rozmisťování světel minimální [(18:40)](https://www.youtube.com/watch?v=k9cbm5jSOxk&t=1120s).

**Den 3 — příprava na logiku:** scéna se musí **zlogičtit dřív, než přijde agent**: tok pohybu (vstup bez návratu, cesta nahoru), mosty ovládané pákami, kolizní bariéry po obvodu (jednoduché plane v Blenderu), kolize na lucernách, dočasný collider u tajné hvězdy, který logika mostu později odstraní — a rozmístění sběratelných předmětů ručně, „jako schovávání velikonočních vajec" [(21:48)](https://www.youtube.com/watch?v=k9cbm5jSOxk&t=1308s) [(24:07)](https://www.youtube.com/watch?v=k9cbm5jSOxk&t=1447s) [(25:41)](https://www.youtube.com/watch?v=k9cbm5jSOxk&t=1541s). Páka se v Blenderu rozdělí a dostane správný pivot za minutu — „kdybys to zadal AI, trvalo by to věčnost" [(23:20)](https://www.youtube.com/watch?v=k9cbm5jSOxk&t=1400s).

**Logika agentem (nativní MCP + Vibe UE, obojí zdarma, „no affiliation"):** sběr mincí přes kolize — snadné; páka na klávesu E (agent se sám zeptá, jak ji ovládat); **dveře: „posuň po ose X jako sliding door"** — detailní prompt ušetří tokeny, protože obecné „otevři dveře" končí drahým screenshot-ověřováním, jak se vlastně otevřely [(26:27)](https://www.youtube.com/watch?v=k9cbm5jSOxk&t=1587s) [(27:14)](https://www.youtube.com/watch?v=k9cbm5jSOxk&t=1634s) [(28:01)](https://www.youtube.com/watch?v=k9cbm5jSOxk&t=1681s). Health bar + počítadlo mincí = 22 minut; horká voda ubírá zdraví přes válcový volume [(28:47)](https://www.youtube.com/watch?v=k9cbm5jSOxk&t=1727s) [(29:33)](https://www.youtube.com/watch?v=k9cbm5jSOxk&t=1773s).

> **Pozn.:** Titulky videa jsou strojově přeložená en-ko stopa (a končí před koncem videa) — názvosloví je v textu narovnané podle kontextu (Claude Code, Fab, Spirited Away). Level design vrstva případovky — tajemství za skálou, památné cesty vzhůru — je čistá praxe [vedení hráče](../teorie/vedeni-hrace.md); mizanscéna „světla svítí, nikdo doma" zase [environmental storytelling](../rejstrik.md#environmental-storytelling).

**Souvislosti:** [AI assety](ai-assety.md) · [Komunitní cesta + prompt lekce](#komunitni-cesta-v-57-endless-runner-jako-stress-test) · [Teorie: vedení hráče](../teorie/vedeni-hrace.md) · [Rejstřík: MCP](../rejstrik.md#mcp)

---

## Produkty okolo: Blueprint AI

**Zdroj:** [This AI builds blueprints for you in Unreal Engine](https://www.youtube.com/watch?v=Kzy7isA2xO0) · [TUF](https://www.youtube.com/channel/UCvgYjqG2Es0VIhIgqyAEEDw) · ~8 min, produktové video

**Shrnutí:** Vedle open-source cest rostou placené obálky: **Blueprint AI** je plugin (jednorázová koupě), který do editoru přidá dockovatelné chat okno a napojí agenta dle výběru — Codex CLI, Claude CLI nebo Gemini, s tlačítkem „install" přímo v okně [(1:36)](https://www.youtube.com/watch?v=Kzy7isA2xO0&t=96s). Funguje i v 5.7, tedy bez nativního MCP.

### Rozpad myšlenky

**Co předvádí:** změna oblohy na noční (agent sám upraví directional light, skylight a přidá hvězdy) [(2:58)](https://www.youtube.com/watch?v=Kzy7isA2xO0&t=178s); hlavní menu se čtyřmi tlačítky včetně založení UI složky [(3:45)](https://www.youtube.com/watch?v=Kzy7isA2xO0&t=225s); a nejužitečnější ukázka — **úprava existujícího editor utility widgetu**: „když přidáš sekvenci, přidej do ní i cine cameru" [(5:18)](https://www.youtube.com/watch?v=Kzy7isA2xO0&t=318s). Chybové stavy řešíš tím, že je agentovi popíšeš [(6:40)](https://www.youtube.com/watch?v=Kzy7isA2xO0&t=400s).

> **Pozn.:** Produktové video se slevovým kódem — hodnotu ber jako průzkum trhu: totéž (a víc) dnes umí nativní MCP v 5.8 zdarma, plus vlastní předplatné agenta. Placené obálky dávají smysl hlavně pro starší verze enginu nebo pohodlnější UI; před koupí si srovnej [nativní setup](#nativni-mcp-v-58-setup-a-prvni-testy).

**Souvislosti:** [Nativní MCP](#nativni-mcp-v-58-setup-a-prvni-testy) · [Rejstřík: MCP](../rejstrik.md#mcp)

---

## Agent ve hře: Convai NPC

**Zdroj:** [From Dialogue to Action: Create Scene-Aware AI Characters That Act AND React](https://www.youtube.com/watch?v=lB5_KRWdg_w) · [Convai](https://www.youtube.com/channel/UCcYtXgiavJYMKSirsk6VNsw) · ~5 min, produktové demo

**Shrnutí:** Agent nemusí sedět jen ve vývojářském terminálu — Convai ho dává do hry jako **NPC, které rozumí přirozené řeči a jedná**: „můžeš dojít ke kostce za tebou a vrátit se?" a MetaHuman jde [(0:02)](https://www.youtube.com/watch?v=lB5_KRWdg_w&t=2s). Produktové demo, ale s přenositelným vzorem: jazykový model potřebuje **ukotvení ve scéně**.

### Rozpad myšlenky

**Akce a pohyb:** na Convai chatbot komponentě se zapnou **Actions** (out-of-box: move to, ukazování, gesta) [(0:50)](https://www.youtube.com/watch?v=lB5_KRWdg_w&t=50s); pohyb chce klasiku — **Nav Mesh Bounds Volume** (náhled klávesou P) a na MetaHuman blueprintu right-click → Convai → setup pawn movement [(1:38)](https://www.youtube.com/watch?v=lB5_KRWdg_w&t=98s) [(2:26)](https://www.youtube.com/watch?v=lB5_KRWdg_w&t=146s). Follow/stop pak funguje hlasem [(2:59)](https://www.youtube.com/watch?v=lB5_KRWdg_w&t=179s).

**Ukotvení objektů:** aby NPC umělo „ukaž na zbraň", potřebuje **reference objektů** — buď seznam na chatbot komponentě (picker + jméno + volitelný popis), nebo **Convai Object komponenta přímo na objektu**, která přežije přidání dalších avatarů; jedno, nebo druhé, ne obojí [(2:59)](https://www.youtube.com/watch?v=lB5_KRWdg_w&t=179s) [(4:14)](https://www.youtube.com/watch?v=lB5_KRWdg_w&t=254s). Pak fungují i řetězce: „ke kostce, pak ke zbrani, pak ke mně" [(3:45)](https://www.youtube.com/watch?v=lB5_KRWdg_w&t=225s).

> **Pozn.:** Demo z kanálu výrobce — počítej s předplatným a závislostí na službě. Přenositelná lekce ale platí obecně: LLM NPC bez nav meshe a referencí objektů jen *mluví* o akcích. Zajímavý kontrast s [klasickou AI](state-trees.md): State Tree dává spolehlivost a laditelnost, jazykový agent improvizaci — hybridní budoucnost nejspíš spojí obojí. *(V indexu přeřazeno ze slugu ai-npc-dialogy.)*

**Souvislosti:** [State Trees](state-trees.md) · [Základy nepřátelské AI](ai-zaklady.md) · [MetaHuman v praxi](metahuman.md) · [Rejstřík: Nav Mesh](../rejstrik.md#nav-mesh)
