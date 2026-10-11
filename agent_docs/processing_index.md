# Processing Index

Per-video status tracker for the whole playlist — created in the Phase 2 taxonomy. **Update the status column whenever a video is processed.** Chapter slugs are working titles for grouping; final chapter names/files are decided at synthesis time. Téma tree **approved by user 2026-07-09** (incl. „Rešerše: slovanská mytologie" and the skip/low-priority flags); re-assigning individual videos later is cheap (nav-only change).

Legend: status `todo / drafted / published / skip` · track `manual / auto / —` (— = no English subtitle track, "bez přepisu") · slova = word count of the cleaned transcript.

**Stats (hlavní playlist):** 210 videos (31 Teorie, 179 Praxe) · 202 published (pilot + batch 1–19) · 7 bez přepisu · 5 skip (news/promo) + 2 low-priority (beginner courses). **Phase 3 komplet — zbývá: 2 low-priority kurzy + 1 CS video (čeká na cs-subtitle pipeline).**

**Phase 7 (samostatný playlist „Gamedev-music"):** 17 videí, **všech 17 published** v dokumentu „Hudba a zvuk" (tabulka na konci souboru).

**Třetí vlna (staženo 2026-07-29):** +174 videí ve třech playlistech — **Godot playlist 93 (nový, samostatná sekce)**, hlavní +61, Gamedev-music +20. Tabulky v sekci „Třetí vlna" na konci souboru; Godot má vlastní sekci s navrženou taxonomií. Pořadí práce: **nejdřív Godot** (Phase 9, hotovo), **pak hlavní playlist se startem u výkonu a profilingu** (Phase 10, hotovo — dávky 36–43), **hudba nakonec** (Phase 11, hotovo — dávky 44–45). **Celá třetí vlna je zpracovaná.**

**Čtvrtá vlna (staženo 2026-10-10):** +93 videí jen z hlavního playlistu („ue5 - izba"), ~458k slov. Taxonomie navržena: **81 todo v dávkách 47–56** (~403k slov; 73 Praxe, 8 Teorie), 9 skip, 3 todo-lp; 15 nových kapitol v Praxi + nové nav téma „UI a rozhraní". **Strom schválen uživatelem 2026-10-10** (vč. 9 skipů a Evanse Bohla jako páteře `souboj.md`). **Stav: 81 published (dávky 47–56 ✅, čtvrtá vlna hotová), 0 todo, 9 skip, 3 lp.** Tabulky v sekci „Čtvrtá vlna" na konci souboru.

**Druhá vlna hlavního playlistu (+116 videí, staženo 2026-07-17):** taxonomie **schválena 2026-07-18** — kompletní tabulky v sekci „Druhá vlna" na konci souboru; tam běží i statusy dávek (20–30). Rozložení: 86 Teorie (z toho 6 nových témat) · 27 Praxe · 3 Hudba; ~512k slov přepisů; 2 bez přepisu; 2 nové low-priority beginner kurzy. **Strom schválen uživatelem 2026-07-18.** Stav: **114/116 published (dávky 20–30) — druhá vlna hotová**, 0 todo + 2 todo-lp (beginner kurzy). Nav témata „Design do hloubky" a „Byznys, data a kariéra" kompletní; Design do hloubky (8 kapitol: obtiznost, systemy-a-mechaniky, ludonarativni-soulad, zanry, engineering-experiences, pripadovky-designu, horor-design, kamera).

## Proposed téma tree

- **Teorie her**
    - Tvůrčí proces a mindset (7)
    - Nápad, scope a plánování (5)
    - Základy designu (6)
    - Level design (5)
    - Vydání a marketing (4)
    - Rešerše: slovanská mytologie (4)
- **Praxe v UE5**
    - Blueprint architektura a organizace projektu (14)
    - Herní systémy a interakce (12)
    - AI a chování NPC (9)
    - Motion Matching a GASP (21)
    - Animace: nástroje a mocap (5)
    - Pohyb postavy (locomotion) (13)
    - Fyzika: ragdoll, lana, simulace (8)
    - Voda (10)
    - Terén a krajina (7)
    - PCG a procedurální svět (19)
    - Prostředí a environment art (11)
    - Materiály a VFX (6)
    - Osvětlení a atmosféra (6)
    - Rendering a optimalizace (7)
    - MetaHuman (5)
    - AI nástroje ve vývoji (14)
    - Editor a workflow (12)


## Teorie her

### Tvůrčí proces a mindset · `T-MIND` (7)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [All of the Coding You Need to Start Gamedev!](https://www.youtube.com/watch?v=yjiFwz6mS6k) `yjiFwz6mS6k` | Brainless. | 15:41 | auto | 4172 | `teorie/co-se-ucit.md` |  |
| published | [How To PROPERLY Start Making A Game](https://www.youtube.com/watch?v=ekOp35B1Bdg) `ekOp35B1Bdg` | Brainless. | 15:19 | auto | 4373 | `teorie/jak-zacit.md` |  |
| published | [ShantyTown Final Devlog - From Idea to Launch](https://www.youtube.com/watch?v=84biRLlHJMk) `84biRLlHJMk` | Silk Softworks | 29:18 | auto | 4101 | `teorie/postmortem-shantytown.md` | devlog: nápad → vydání |
| published | [Make Something](https://www.youtube.com/watch?v=GELGIhL9mZo) `GELGIhL9mZo` | Sinikick | 30:26 | auto | 5040 | `teorie/proc-tvorit.md` |  |
| published | [7 Gamedev Time Wastes](https://www.youtube.com/watch?v=nckLk3qJ-yo) `nckLk3qJ-yo` | BiteMe Games | 20:42 | auto | 4802 | `teorie/produktivita.md` |  |
| published | [The Game Dev Advice That Took 10 Years to Discover](https://www.youtube.com/watch?v=12tZyCMIYbg) `12tZyCMIYbg` | Isto Inc. | 16:25 | auto | 3366 | `teorie/rady-z-praxe.md` |  |
| published | [How to Make Games When You're Bad at Everything](https://www.youtube.com/watch?v=ySZynbrqMRM) `ySZynbrqMRM` | Brainless. | 8:19 | auto | 1805 | `teorie/zacatky-bez-zkusenosti.md` |  |

### Nápad, scope a plánování · `T-SCOPE` (5)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [The Only Game Idea Guide You’ll Ever Need](https://www.youtube.com/watch?v=d_e9Apys9Dg) `d_e9Apys9Dg` | BiteMe Games | 67:09 | auto | 14746 | `teorie/napad.md` |  |
| published | [Your game idea (probably) sucks](https://www.youtube.com/watch?v=RqmHvVabdL0) `RqmHvVabdL0` | BiteMe Games | 18:13 | auto | 4138 | `teorie/napad.md` |  |
| published | [Prototyping, Vertical Slices, and Planning a Complex Game](https://www.youtube.com/watch?v=atUsa3BE7t0) `atUsa3BE7t0` | Indie Game Clinic | 22:26 | auto | 4489 | `teorie/prototypovani.md` | vertical slice |
| published | [Develop Better Games, Faster, with "Design by Constraint"](https://www.youtube.com/watch?v=sk4mpNuFGeE) `sk4mpNuFGeE` | Indie Game Clinic | 49:31 | auto | 9830 | `teorie/scope.md` | design by constraint |
| published | [What does "Make Small Games" really mean?](https://www.youtube.com/watch?v=xenwRup_sC4) `xenwRup_sC4` | BiteMe Games | 15:50 | auto | 3670 | `teorie/scope.md` | v playlistu 2× |

### Základy designu · `T-DESIGN` (6)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [The Trick I Used to Make Combat Fun! \| Devlog](https://www.youtube.com/watch?v=6BrZryMz-ac) `6BrZryMz-ac` | Game Endeavor | 8:12 | manual | 1942 | `teorie/game-feel.md` |  |
| published | [This Made My Game 10X More IMMERSIVE](https://www.youtube.com/watch?v=4t3B5brFui4) `4t3B5brFui4` | Its Rascal | 9:35 | auto | 2161 | `teorie/game-feel.md` | devlog o imerzi |
| published | [Story in Games: Characters & Dialogue 🗣️](https://www.youtube.com/watch?v=orvZIxC54NU) `orvZIxC54NU` | Indie Game Clinic | 39:41 | auto | 7898 | `teorie/pribeh-a-postavy.md` |  |
| published | [Gameplay Loops Are Out, Chains Are In](https://www.youtube.com/watch?v=6SYX17NzNqE) `6SYX17NzNqE` | Indie Game Clinic | 11:01 | manual | 1987 | `teorie/smycky-a-retezce.md` |  |
| published | [How to Make Anything Fun](https://www.youtube.com/watch?v=bMwfH8hJtRc) `bMwfH8hJtRc` | Jonas Tyroller | 73:31 | auto | 13817 | `teorie/zabava.md` |  |
| published | [Your Game Must Do These 2 Things](https://www.youtube.com/watch?v=rTxKsBclbxk) `rTxKsBclbxk` | Indie Game Clinic | 23:38 | auto | 4824 | `teorie/zaklady.md` |  |

### Level design · `T-LEVEL` (5)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [How AAA Level Designers Create Gameplay Moments](https://www.youtube.com/watch?v=tRBGGuh1ajY) `tRBGGuh1ajY` | Gabriel Fuentes | 4:44 | auto | 766 | `teorie/vedeni-hrace.md` |  |
| published | [Map Boundary in Level Design \| Tips for Solo Game Devs \| Unity \| Unreal](https://www.youtube.com/watch?v=tcXGVyy4Mm8) `tcXGVyy4Mm8` | Seta - Level Design | 6:55 | manual | 1083 | `teorie/prostor-a-hranice.md` |  |
| published | [How Level Designers Build Caves in UE5](https://www.youtube.com/watch?v=lSrDXaTwvNU) `lSrDXaTwvNU` | Gabriel Fuentes | 5:11 | auto | 810 | `teorie/prostor-a-hranice.md` |  |
| published | [Recall Priming as a Level Design Technique](https://www.youtube.com/watch?v=Y2QBzdaMAAI) `Y2QBzdaMAAI` | timdoesleveldesign (TimDoesLevelDesign) | 4:40 | manual | 801 | `teorie/vedeni-hrace.md` |  |
| skip | [Epic Just Dropped a FREE Level Design Project (Unreal Engine 5)](https://www.youtube.com/watch?v=A7CNW9y0-UI) `A7CNW9y0-UI` | Unreal University  | 3:34 | auto | 686 | `zdroje` | novinka o free projektu — přeskočit? |

### Vydání a marketing · `T-MARKET` (4)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [What Sells on Steam: You Don't Need a Hook](https://www.youtube.com/watch?v=uiBDyZ-Pf2M) `uiBDyZ-Pf2M` | Jonas Tyroller | 15:20 | auto | 3192 | `teorie/co-prodava.md` |  |
| published | [The Problem with Indie Game Devlogs on Youtube](https://www.youtube.com/watch?v=48C9hYoLMis) `48C9hYoLMis` | Inbound Shovel | 15:10 | auto | 3620 | `teorie/devlogy.md` |  |
| published | [Your Game's First Impression Is Ruined By These Three Things](https://www.youtube.com/watch?v=s9VOnhQU1hE) `s9VOnhQU1hE` | Game Dev Guide | 7:24 | auto | 1711 | `teorie/prvni-dojem.md` |  |
| published | [Everything you need to make a great Steam page](https://www.youtube.com/watch?v=cYvV_RLwKJ8) `cYvV_RLwKJ8` | BiteMe Games | 35:54 | auto | 7956 | `teorie/steam-stranka.md` |  |

### Rešerše: slovanská mytologie · `T-MYTH` (4)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [Terrible creatures of Slavic mythology](https://www.youtube.com/watch?v=D23Tl7a2q0k) `D23Tl7a2q0k` | Slavique | 19:38 | auto | 2935 | `teorie/slovanska-monstra.md` |  |
| todo | [Slovanské pohanství – Mytologie, bohové, rituály a nadpřirozené bytosti](https://www.youtube.com/watch?v=uPwV7dgokOQ) `uPwV7dgokOQ` | Nerdopolis | 27:02 | — | — | `slovanske-pohanstvi` | bez přepisu — české video, zkusit cs titulky |
| published | [Every Winter Slavs Perform These Strange Rituals...](https://www.youtube.com/watch?v=csgkkrNf4PE) `csgkkrNf4PE` | Slavique | 18:28 | auto | 2718 | `teorie/slovanske-ritualy.md` |  |
| published | [Slavic folklore: Baba Yaga and Vasilisa the Beautiful \| Folktales and legends for a scary world](https://www.youtube.com/watch?v=O6L71XNYqys) `O6L71XNYqys` | Tales by Alma | 19:05 | auto | 3523 | `teorie/slovansky-folklor.md` | Baba Yaga |


## Praxe v UE5

### Blueprint architektura a organizace projektu · `P-BP` (14)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| todo | [Learn Blueprints for Unreal Engine 5 in ONE VIDEO - Beginner Tutorial](https://www.youtube.com/watch?v=dB-pS8PHALY) `dB-pS8PHALY` | Cobra Code | 75:39 | auto | 16852 | `blueprint-zaklady` | kurz pro začátečníky (76 min) — nízká priorita |
| published | [Everything You Need to Know About Gameplay Tags \| UE5 Tutorial](https://www.youtube.com/watch?v=UNDbcAMMJwk) `UNDbcAMMJwk` | Ali Elzoheiry | 49:53 | auto | 8411 | `praxe/gameplay-tags.md` |  |
| published | [How to Line Trace Without Event Tick - UE5 Tutorial](https://www.youtube.com/watch?v=rCd36pNqCeo) `rCd36pNqCeo` | Doppelganger Studios | 16:43 | auto | 1883 | `praxe/interakce-bez-event-ticku.md` |  |
| published | [All 3 Blueprint Communication Methods in Unreal Engine Explained in Under 18 Minutes](https://www.youtube.com/watch?v=ZSRSktpezII) `ZSRSktpezII` | Unreal University  | 17:41 | auto | 3163 | `praxe/komunikace-blueprintu.md` | 3 metody |
| published | [Unreal Engine: Boost Game Perf with Smart Broadcasts! #shorts](https://www.youtube.com/watch?v=dIXGXiB9Okc) `dIXGXiB9Okc` | Taken Grace | 1:23 | auto | 329 | `praxe/komunikace-blueprintu.md` | short |
| published | [How to CORRECTLY Load Levels in Unreal Engine!](https://www.youtube.com/watch?v=mwyJ7rKUqKE) `mwyJ7rKUqKE` | DevEdge Studio | 22:37 | auto | 5250 | `praxe/levely-a-streaming.md` |  |
| published | [How Resident Evil Requiem Hides Loading and Level Instancing \| Game Dev Breakdown](https://www.youtube.com/watch?v=l_U0enrB9IY) `l_U0enrB9IY` | HALbot Studios | 19:07 | auto | 3237 | `praxe/levely-a-streaming.md` | breakdown (RE Requiem) |
| published | [Why Your UE5 Projects Are Messy (And How to Fix It)](https://www.youtube.com/watch?v=0-xB4P2yYN8) `0-xB4P2yYN8` | Taken Grace | 11:17 | auto | 2598 | `praxe/organizace-projektu.md` |  |
| published | [9 Tips To Better Organize Your Unreal Engine  Projects](https://www.youtube.com/watch?v=S7TwnS2wAZQ) `S7TwnS2wAZQ` | Unreal University  | 6:21 | auto | 1230 | `praxe/organizace-projektu.md` | 9 tipů |
| published | [The ONLY Way to Build Scalable Systems in Unreal Engine 5](https://www.youtube.com/watch?v=zTsJM9T0NjM) `zTsJM9T0NjM` | Taken Grace | 80:47 | auto | 16859 | `praxe/principy-architektury.md` | 81 min |
| published | [3 Principles Every Game Programmer Needs to Know in Unreal Engine](https://www.youtube.com/watch?v=RhKqtQRy_j0) `RhKqtQRy_j0` | Ali Elzoheiry | 18:09 | auto | 2934 | `praxe/principy-architektury.md` |  |
| published | [Unreal Engine 5 Tutorial -  Stats and Achievements Part 1: Activity Tracker](https://www.youtube.com/watch?v=9iWSVZoADpo) `9iWSVZoADpo` | Ryan Laley | 12:53 | auto | 1915 | `praxe/telemetrie.md` | stats+achievementy |
| published | [How to Track Player Behavior in Unreal Engine 5 (TrackEdge + Post Hog)](https://www.youtube.com/watch?v=o0HlCeQXxAQ) `o0HlCeQXxAQ` | DevEdge Studio | 12:33 | auto | 2913 | `praxe/telemetrie.md` | PostHog |
| published | [How to Easily Save Games with SaveGame Objects in Unreal Engine (Demo and Guide)](https://www.youtube.com/watch?v=-0111fuUPz8) `-0111fuUPz8` | Unreal University  | 14:02 | auto | 2694 | `praxe/ukladani.md` | SaveGame objekty |

### Herní systémy a interakce · `P-SYS` (12)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [Surface-Based Footprint Decals in Unreal Engine 5 (Dynamic & Fading)](https://www.youtube.com/watch?v=buQ6JvwvHuw) `buQ6JvwvHuw` | Tank Control Games | 32:38 | auto | 6114 | `praxe/footsteps.md` | stopy (decals) |
| published | [Footstep Sounds by Surface Type in Unreal Engine 5 (MetaSounds)](https://www.youtube.com/watch?v=e2N0dRLHsGY) `e2N0dRLHsGY` | Tank Control Games | 28:02 | auto | 5025 | `praxe/footsteps.md` | MetaSounds |
| published | [Unreal Engine 5.7 - Smart Footstep System (Physical Materials) - Tutorial](https://www.youtube.com/watch?v=6E-l9tWSCt4) `6E-l9tWSCt4` | Unreal - X - Tutorials | 11:31 | auto | 1587 | `praxe/footsteps.md` | physical materials |
| published | [Complete Unreal Footsteps System Using Niagara Data Channel!](https://www.youtube.com/watch?v=sGJ8cqe94ps) `sGJ8cqe94ps` | Grid & Node | 9:38 | auto | 962 | `praxe/footsteps.md` | Niagara Data Channel |
| published | [Fall Guys Hex-A-Gon Tutorial Unreal Engine 4](https://www.youtube.com/watch?v=ANWzAitL0Jg) `ANWzAitL0Jg` | Unreal University  | 6:20 | auto | 1177 | `praxe/pasti-a-mechaniky.md` | Hex-A-Gon (UE4); merge herni-mechaniky+pasti |
| published | [Game Dev Secrets: A Simple Hitbox Trick! #indiegamedev #gamedev](https://www.youtube.com/watch?v=X0jy94VP_Ko) `X0jy94VP_Ko` | Inbound Shovel | 1:01 | auto | 233 | `praxe/pasti-a-mechaniky.md` | hitbox trik, short |
| published | [How To Create Pickup And Drop System In Unreal Engine 5 Full Tutorial #subscribe #subscribeme](https://www.youtube.com/watch?v=Hd0od7sQdds) `Hd0od7sQdds` | Overlook Games | 16:58 | — | — | `praxe/interakce-predmety.md` | bez přepisu — jen krátká zmínka (popis nic nedává) |
| published | [Throwing Objects System And Projectile Path Trajectory \| Unreal Engine 5](https://www.youtube.com/watch?v=B4W9lKbGeIc) `B4W9lKbGeIc` | Vercion Games | 12:25 | auto | 2885 | `praxe/interakce-predmety.md` | házení + trajektorie |
| published | [UE5 - TUTORİAL İnteractive World [FREE PLUGIN]](https://www.youtube.com/watch?v=xYGz-oGAGkk) `xYGz-oGAGkk` | REFORCH | 4:38 | — | — | `praxe/footsteps.md` | bez přepisu — kryto z popisu; přeřazeno k footsteps (snow trails/mud) |
| published | [3D Platformer Tutorial UE5  - Episode 5 - TRAPS!!!](https://www.youtube.com/watch?v=47d_s2e-RlM) `47d_s2e-RlM` | Shane_Gamedev | 23:28 | auto | 4139 | `praxe/pasti-a-mechaniky.md` |  |
| published | [Moving Obstacles (Swinging Axes) Unreal engine 5 Traps Tutorial](https://www.youtube.com/watch?v=RdItM2xmF5M) `RdItM2xmF5M` | Zero2GameDev | 21:46 | auto | 2547 | `praxe/pasti-a-mechaniky.md` | kyvadlové sekery |
| published | [Hide Inside Locker Almirah \| Unreal Engine 5](https://www.youtube.com/watch?v=nLjUs8_5QBI) `nLjUs8_5QBI` | Vercion Games | 17:19 | auto | 3774 | `praxe/interakce-predmety.md` | skříň/lokr; merge stealth-ukryty→interakce |

### AI a chování NPC · `P-AI-NPC` (9)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [How to Make an AI Follow a Waypoint Path Patrol in Unreal Engine 5](https://www.youtube.com/watch?v=WqcDNlWEgsI) `WqcDNlWEgsI` | Gorka Games | 11:17 | auto | 2066 | `praxe/ai-zaklady.md` | waypointy — editorial merge do ai-zaklady |
| published | [Create Smarter AI With These 3 Easy Detection Methods in Unreal Engine 5](https://www.youtube.com/watch?v=XgOEkcnJT0M) `XgOEkcnJT0M` | Gorka Games | 9:15 | auto | 1740 | `praxe/ai-vnimani.md` | 3 metody detekce |
| published | [AI Sight Detection And Chase - Unreal Engine 5 Tutorial](https://www.youtube.com/watch?v=tKrBdxm4uxI) `tKrBdxm4uxI` | Matt Aspland | 7:33 | auto | 1728 | `praxe/ai-vnimani.md` | sight+chase |
| published | [Terrifying AI Chase System in Unreal Engine 5 – Learn in Minutes!](https://www.youtube.com/watch?v=GMYfVNftR-U) `GMYfVNftR-U` | Ugur Batur GameDev | 6:39 | auto | 664 | `praxe/ai-vnimani.md` | chase |
| published | [AI: Easy chasing player setup - Tutorial Unreal Engine 5](https://www.youtube.com/watch?v=EeN65RxmCak) `EeN65RxmCak` | LeafBranchGames | 27:12 | auto | 4523 | `praxe/ai-zaklady.md` | chase, BT/BB architektura |
| published | [The Easiest Way to Make a Simple Enemy AI in Unreal Engine 5](https://www.youtube.com/watch?v=xm-7m5Fw1HU) `xm-7m5Fw1HU` | Gorka Games | 15:40 | auto | 2249 | `praxe/ai-zaklady.md` |  |
| published | [How To Create A Basic AI Enemy That Follows You - Unreal Engine 5 Tutorial](https://www.youtube.com/watch?v=sVV32qivy1A) `sVV32qivy1A` | Pitchfork Academy | 14:32 | auto | 2022 | `praxe/ai-zaklady.md` | + ragdoll bonus |
| published | [Unreal Engine 5 AI Patrol and Chase Tutorial](https://www.youtube.com/watch?v=lbqZS-cgcQs) `lbqZS-cgcQs` | Pixel Helmet | 12:36 | auto | 2383 | `praxe/ai-zaklady.md` | patrol+chase |
| published | [Build Smart AI with State Trees in UE5 (Full Tutorial)](https://www.youtube.com/watch?v=UuqKC0AgeXU) `UuqKC0AgeXU` | HardcastleGames | 39:30 | auto | 6598 | `praxe/state-trees.md` |  |

### Motion Matching a GASP · `P-ANIM` (21)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [GASP - It's Mover! Game Animation Sample Updates + Q&A \| Inside Unreal](https://www.youtube.com/watch?v=i27eY7LbRzc) `i27eY7LbRzc` | Unreal Engine | 181:00 | auto | 30277 | `praxe/gasp.md` | 181 min, + Mover |
| published | [Game Animation Sample Walkthrough \| Inside Unreal](https://www.youtube.com/watch?v=mhVp_cC9MLc) `mhVp_cC9MLc` | Unreal Engine | 154:00 | auto | 26831 | `praxe/gasp.md` | 154 min, Inside Unreal |
| published | [Unreal Engine 5 GASP Cover Shooter Series Tutorial 1 (Setup Layer System)](https://www.youtube.com/watch?v=kfu4jKyazzU) `kfu4jKyazzU` | Make A Real One | 34:24 | — | — | `praxe/gasp.md` | bez přepisu; cover shooter 1 — kryto z kontextu série |
| published | [GASP Adding New Weapon Animations and Pose Search Database's](https://www.youtube.com/watch?v=fXNahVSGssg) `fXNahVSGssg` | Zero2GameDev | 28:04 | auto | 3780 | `praxe/gasp.md` | zbraně |
| published | [Unreal Engine 5 GASP Cover Shooter Series Tutorial 2 (Add Layer Curves)](https://www.youtube.com/watch?v=1xj3nPEmHPw) `1xj3nPEmHPw` | Make A Real One | 17:23 | — | — | `praxe/gasp.md` | bez přepisu; cover shooter 2 — kryto z kontextu série |
| published | [Different Overlay States for GASP/ Motion Matching in Unreal Engine!](https://www.youtube.com/watch?v=tqVbYSEJLBE) `tqVbYSEJLBE` | DevEdge Studio | 8:01 | auto | 1817 | `praxe/gasp.md` | overlay states |
| published | [Unreal Engine 5.4: Combining Attack Animations with Motion Matching in Custom Characters \| Tutorial](https://www.youtube.com/watch?v=BDjGNdMlEAg) `BDjGNdMlEAg` | The Epic Singh | 33:30 | auto | 3782 | `praxe/mm-systemy.md` | combat, vlastní postavy |
| published | [Unreal Engine 5  Motionmatching ParkourSystem and Motionmatching Cover System Component Setup](https://www.youtube.com/watch?v=bxKzYbA50l0) `bxKzYbA50l0` | Make A Real One | 26:07 | auto | 1698 | `praxe/mm-systemy.md` | parkour+cover |
| published | [Unreal Engine 5 MotionMatching Cover System Component Setup](https://www.youtube.com/watch?v=vm5aPoXgtWM) `vm5aPoXgtWM` | Make A Real One | 23:27 | auto | 1954 | `praxe/mm-systemy.md` | cover |
| published | [🎮 Master Motion Matching: Climb Everywhere & Export Like a Pro](https://www.youtube.com/watch?v=N60w1Nk0sKU) `N60w1Nk0sKU` | Mask Devlog | 11:52 | manual | 1478 | `praxe/mm-systemy.md` | climb |
| published | [Motion Matching \| Flexible Combat System \| Unreal Engine 5](https://www.youtube.com/watch?v=V1I9gdJD45g) `V1I9gdJD45g` | Beardgames | 11:12 | auto | 1577 | `praxe/mm-systemy.md` | combat |
| published | [How To Set Up Combat Using Choosers - Unreal Engine 5](https://www.youtube.com/watch?v=G41RGiXLhnE) `G41RGiXLhnE` | Clydiie | 9:08 | auto | 1819 | `praxe/mm-systemy.md` | choosers |
| published | [Unscripted Motion Matching Interactions In The Witcher 4](https://www.youtube.com/watch?v=dd35tkF-5io) `dd35tkF-5io` | Clydiie | 6:49 | auto | 1115 | `praxe/mm-systemy.md` | interakce (Witcher 4) |
| published | [Motion Matching Explained (State Machines to GASP ) in Unreal Engine 5!](https://www.youtube.com/watch?v=9BWLj98pekM) `9BWLj98pekM` | DevEdge Studio | 58:40 | auto | 12652 | `praxe/mm-zaklady.md` | state machines → GASP |
| published | [UE5 \| Motion Matching Breakdown \| Part-1](https://www.youtube.com/watch?v=-r4nafTJI5c) `-r4nafTJI5c` | TechAnim Studios | 53:57 | auto | 5896 | `praxe/mm-zaklady.md` | breakdown |
| published | [Embracing Motion Matching: Using a Little to Get a Lot \| Unreal Fest Bali 2025](https://www.youtube.com/watch?v=FLDXtAV7qsw) `FLDXtAV7qsw` | Unreal Engine | 47:44 | auto | 8792 | `praxe/mm-zaklady.md` | Unreal Fest |
| published | [Motion Matching and the Game Animation Sample in UE 5.4 \| Unreal Fest 2024](https://www.youtube.com/watch?v=tNw9lD2PW3U) `tNw9lD2PW3U` | Unreal Engine | 41:28 | auto | 6725 | `praxe/mm-zaklady.md` | Unreal Fest |
| published | [Understand Motion Matching in Unreal Engine 5 - Part 2](https://www.youtube.com/watch?v=q-Ag6iYalAo) `q-Ag6iYalAo` | Ryan Laley | 17:39 | auto | 2648 | `praxe/mm-zaklady.md` | part 2 |
| published | [Understand Motion Matching in Unreal Engine 5 - Part 1](https://www.youtube.com/watch?v=YtIxWtMPYQE) `YtIxWtMPYQE` | Ryan Laley | 15:29 | auto | 2486 | `praxe/mm-zaklady.md` | part 1 |
| published | [Unreal Engine 5.4 Motion Matching in 13 Minutes \| 2024](https://www.youtube.com/watch?v=LJi_vPAuTv4) `LJi_vPAuTv4` | Reality Forge | 13:40 | auto | 2775 | `praxe/mm-zaklady.md` |  |
| published | [Unreal Engine 5.4 Tutorial - Motion Matching](https://www.youtube.com/watch?v=HxY0WWQe_XA) `HxY0WWQe_XA` | Unreal University  | 8:14 | auto | 1464 | `praxe/mm-zaklady.md` |  |

### Animace: nástroje a mocap · `P-ANIMTOOLS` (5)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [How To Animate Your Character In Unreal Engine 5 With Animation Blueprint And Blendspace (Tutorial)](https://www.youtube.com/watch?v=BuoeWNQOe0Y) `BuoeWNQOe0Y` | Matt Aspland | 17:02 | auto | 3706 | `praxe/animace-nastroje.md` | blendspace; merge 3 slugů do 1 kapitoly |
| published | [The Fastest "Video to Animation" Tutorial in UE5.8](https://www.youtube.com/watch?v=SHP5fBaTPJQ) `SHP5fBaTPJQ` | Kartoon Develop Tips | 6:30 | auto | 1058 | `praxe/animace-nastroje.md` | video→animace |
| published | [MetaHuman Markerless Mocap Tutorial FREE in Unreal 5.8](https://www.youtube.com/watch?v=iJXJO-J7z3g) `iJXJO-J7z3g` | Thomas Halpin | 5:12 | auto | 484 | `praxe/animace-nastroje.md` | MetaHuman, zdarma |
| published | [Unreal Engine 5.8 NEW Markerless Motion Capture Tutorial](https://www.youtube.com/watch?v=kxsncXh8hhM) `kxsncXh8hhM` | World Of VFX | 4:51 | auto | 942 | `praxe/animace-nastroje.md` | markerless 5.8 |
| published | [EASY Procedural Spider Animation in UE5 \| Locomotor + Control Rig Tutorial](https://www.youtube.com/watch?v=uhjN4jf3q6k) `uhjN4jf3q6k` | Tank Control Games | 11:18 | auto | 2287 | `praxe/animace-nastroje.md` | pavouk, Control Rig |

### Pohyb postavy (locomotion) · `P-MOVE` (13)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [An Introduction to the Mover Plugin \| Unreal Fest 2024](https://www.youtube.com/watch?v=P4IKS5k47Wg) `P4IKS5k47Wg` | Unreal Engine | 42:13 | auto | 7191 | `praxe/mover.md` | Unreal Fest |
| published | [Unreal Engine 5 Mover Component Setup For Character (5.7) Part 1](https://www.youtube.com/watch?v=7Uu3ocESVIE) `7Uu3ocESVIE` | Make A Real One | 23:15 | auto | 1608 | `praxe/mover.md` | setup |
| published | [Unreal Engine 5 Mover Component Add Sprinting and Crouch For Character (5.7) Part 2](https://www.youtube.com/watch?v=-aYbOp65EvQ) `-aYbOp65EvQ` | Make A Real One | 17:42 | auto | 1130 | `praxe/mover.md` | sprint+crouch |
| published | [How To Make Better Looking Locomotion in Mover 2.0](https://www.youtube.com/watch?v=gFDxFskLtck) `gFDxFskLtck` | Zero2GameDev | 10:19 | auto | 1838 | `praxe/mover.md` | Mover 2.0 |
| published | [How To Make Perfect Ledge Grabs Every Time - Unreal Engine](https://www.youtube.com/watch?v=gzb356i0Fqk) `gzb356i0Fqk` | DEVenestration | 34:01 | auto | 4061 | `praxe/parkour-vault.md` | ledge grab |
| published | [Vaulting & Climbing (Parkour) Part 1 - Unreal Engine 5 Tutorial](https://www.youtube.com/watch?v=6hPArmWkKJQ) `6hPArmWkKJQ` | Matt Aspland | 24:27 | auto | 5464 | `praxe/parkour-vault.md` |  |
| published | [Make Advance Vaulting System in Unreal Engine!](https://www.youtube.com/watch?v=TZ-lhSHQjPU) `TZ-lhSHQjPU` | DevEdge Studio | 12:55 | — | — | `praxe/parkour-vault.md` | bez přepisu — kryto z kontextu (popis) |
| published | [How To Add A Crouch And Prone Mechanic With Animations In Unreal Engine 5 - Beginners Tutorial](https://www.youtube.com/watch?v=7yRKF-_hMok) `7yRKF-_hMok` | H2 Unreal | 14:02 | auto | 1761 | `praxe/pohyb-zaklady.md` | crouch+prone |
| published | [Epic Games Didn’t Fix This😒, So I Had To Fix Myself \| Resident Evil 9 Style \| UE5 \| Easy Tutorial](https://www.youtube.com/watch?v=83eC8TtVZTw) `83eC8TtVZTw` | Hydra | 13:45 | auto | 1714 | `praxe/pohyb-zaklady.md` | wall-stop à la RE9 |
| published | [Unreal Engine 5 Tutorial -  Charged Jump Part 1: The Jump](https://www.youtube.com/watch?v=CKvTgBf-9Ss) `CKvTgBf-9Ss` | Ryan Laley | 12:08 | auto | 2015 | `praxe/pohyb-zaklady.md` | charged jump; part 2 mimo playlist |
| published | [Unreal Engine 5 Tutorial - Walk, Run, and Sprint Toggle](https://www.youtube.com/watch?v=f-NEj00qprs) `f-NEj00qprs` | The Real Unreal | 7:46 | auto | 937 | `praxe/pohyb-zaklady.md` | walk/run/sprint |
| published | [Unreal Engine 5 Tutorial - How to Crouch](https://www.youtube.com/watch?v=0DQJkzLqCLk) `0DQJkzLqCLk` | The Real Unreal | 6:40 | auto | 809 | `praxe/pohyb-zaklady.md` | crouch |
| published | [Using Floor Angle to Determine Walk Speed \| #ue5](https://www.youtube.com/watch?v=K87dmHB1M54) `K87dmHB1M54` | DEVenestration | 5:25 | auto | 753 | `praxe/pohyb-zaklady.md` | rychlost dle sklonu |

### Fyzika: ragdoll, lana, simulace · `P-PHYS` (8)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [Create Dynamic Cable Systems in UE5.7, Attach Any Mesh Procedurally #unrealengine #cable #blueprint](https://www.youtube.com/watch?v=hGz_TWoez0M) `hGz_TWoez0M` | PolyBoost | 10:42 | auto | 841 | `praxe/lana-kabely.md` |  |
| published | [How to Simulate Ropes And Cables In Unreal Engine 5](https://www.youtube.com/watch?v=uVYaJNUjL2Y) `uVYaJNUjL2Y` | Unreal ART With Alireza  | 5:18 | auto | 843 | `praxe/lana-kabely.md` |  |
| published | [UE5.2 - Physics Control Component - Let's build a character interactive raft in the water (Subtitle)](https://www.youtube.com/watch?v=A_NMmn-Do38) `A_NMmn-Do38` | Yepkoo | 8:09 | manual | 794 | `praxe/lana-kabely.md` | raft; merge physics-control→lana-kabely |
| published | [UE5 Ragdoll Physics Tutorial: Active Ragdoll, Stand Up & Moving Platforms (Complete Guide)](https://www.youtube.com/watch?v=R5o2CjPb3Tk) `R5o2CjPb3Tk` | LocoDev | 61:56 | auto | 7799 | `praxe/ragdoll.md` | komplet průvodce (nad GASP 5.5) |
| published | [Advanced Seamless Ragdoll mode enter/exit, UE 5 tutorial](https://www.youtube.com/watch?v=-mHfpyBn_UQ) `-mHfpyBn_UQ` | DK 3D | 53:07 | auto | 5334 | `praxe/ragdoll.md` |  |
| published | [UE5 Ragdoll Deep Dive Guide: Active Ragdoll, Tricks, and Getting Up](https://www.youtube.com/watch?v=ZpcOYg1Qfm4) `ZpcOYg1Qfm4` | frinky | 39:48 | auto | 7031 | `praxe/ragdoll.md` | deep dive |
| published | [How to Make an Active Ragdoll (like Gang Beasts) in Unreal Engine 5](https://www.youtube.com/watch?v=l4nfL9RHcA4) `l4nfL9RHcA4` | Gorka Games | 6:30 | auto | 1235 | `praxe/ragdoll.md` | active ragdoll |
| published | [Unreal Engine 5 Tutorial - Ragdoll](https://www.youtube.com/watch?v=ZHgnfFj7pco) `ZHgnfFj7pco` | The Real Unreal | 3:32 | auto | 433 | `praxe/ragdoll.md` |  |

### Voda · `P-WATER` (10)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [How to Make a Boat Float in Unreal Engine 5 - Buoyancy Tutorial](https://www.youtube.com/watch?v=KwPnb8CglDY) `KwPnb8CglDY` | Gorka Games | 6:41 | auto | 1302 | `praxe/voda-a-buoyancy.md` |  |
| published | [Unreal Engine 5 (works in UE4) Floating objects a.k.a. Buoyancy](https://www.youtube.com/watch?v=Wg3lP8zW3HI) `Wg3lP8zW3HI` | ArtFX 3D | 2:50 | auto | 332 | `praxe/voda-a-buoyancy.md` |  |
| published | [Objects NOT Floating in UE5? 😱 FIX Water Buoyancy in Unreal Engine 5 (EASY METHOD)](https://www.youtube.com/watch?v=JgWaK3OYqg4) `JgWaK3OYqg4` | World Of VFX | 2:11 | auto | 459 | `praxe/voda-a-buoyancy.md` | fix (5.7 physical material) |
| published | [Unreal Engine 5.7 - Buoyancy in Shallow Water - Quick Tip](https://www.youtube.com/watch?v=qeG0OxBFwzk) `qeG0OxBFwzk` | Unreal - X - Tutorials | 1:41 | auto | 190 | `praxe/voda-a-buoyancy.md` | mělká voda |
| published | [How To Enable Water Interaction - Unreal Engine 5 Tutorial](https://www.youtube.com/watch?v=EUbSj2hEMCE) `EUbSj2hEMCE` | Pitchfork Academy | 11:21 | auto | 2192 | `praxe/interaktivni-voda.md` | + water bodies část ve voda-a-buoyancy.md |
| published | [How To Make Interactive Water Simulation (Just Like The Witcher 4) - Unreal Engine 5.6 Tutorial](https://www.youtube.com/watch?v=kkwXxeys8JE) `kkwXxeys8JE` | MakeCodeSimple_Unreal | 6:54 | auto | 566 | `praxe/interaktivni-voda.md` | à la Witcher 4 |
| published | [Unreal 5 - Realistic Interactive Water in 5 Minutes](https://www.youtube.com/watch?v=i9Bfg5H_fKM) `i9Bfg5H_fKM` | renderBucket | 6:31 | auto | 1089 | `praxe/interaktivni-voda.md` |  |
| published | [Making Interactive Water in Unreal Engine](https://www.youtube.com/watch?v=QdwKSsVjYo8) `QdwKSsVjYo8` | sappydev | 5:46 | auto | 885 | `praxe/interaktivni-voda.md` |  |
| published | [Create INSANE Realistic & Interactive Water in 5 minutes in Unreal 5.5](https://www.youtube.com/watch?v=FqkS6Ke0ouE) `FqkS6Ke0ouE` | LearningTheWires | 4:52 | auto | 668 | `praxe/interaktivni-voda.md` |  |
| published | [Introducing EasyWaterscape for Unreal Engine 5](https://www.youtube.com/watch?v=dXuwb4PpodQ) `dXuwb4PpodQ` | William Faucher | 25:07 | auto | 4678 | `praxe/nastroje-voda.md` | produktové video — psáno s tímto vědomím |

### Terén a krajina · `P-TERRAIN` (7)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [Unreal Engine Landscape creation for beginners \| Full Tutorial](https://www.youtube.com/watch?v=gNLL1jFmWjQ) `gNLL1jFmWjQ` | World Of VFX | 13:08 | auto | 2413 | `praxe/landscape-tipy.md` | pro začátečníky |
| published | [Secret Copy/Paste Tool for Landscapes in Unreal Engine 5](https://www.youtube.com/watch?v=1ySwXsKR4VM) `1ySwXsKR4VM` | Aziel Arts | 12:05 | auto | 2666 | `praxe/landscape-tipy.md` |  |
| published | [Unreal Engine 5.7 - Procedural Landscape Painting - Tutorial](https://www.youtube.com/watch?v=REpMPdptKWQ) `REpMPdptKWQ` | Unreal - X - Tutorials | 7:33 | auto | 1026 | `praxe/landscape-tipy.md` | procedurální malování |
| published | [Unreal Engine 5.7 - Fix Repeating Landscape Textures - Tutorial](https://www.youtube.com/watch?v=A1P8LK7POuM) `A1P8LK7POuM` | Unreal - X - Tutorials | 5:49 | auto | 802 | `praxe/landscape-tipy.md` | opakující se textury |
| published | [How to Use Unreal Engine’s New Landscape System - Mesh Terrain Tutorial](https://www.youtube.com/watch?v=Lhj2LutYNjA) `Lhj2LutYNjA` | Unreal Sensei | 66:18 | auto | 12472 | `praxe/mesh-terrain.md` | doplněno do pilotní kapitoly (nová myšlenka) |
| published | [Unreal Engine 5.8 Mesh Terrain — Full Deep Dive](https://www.youtube.com/watch?v=JzQrUAVPmr4) `JzQrUAVPmr4` | Aziel Arts | 47:55 | auto | 9304 | `praxe/mesh-terrain.md` |  |
| published | [How to use Mesh terrain layers? Material + PCG](https://www.youtube.com/watch?v=LWhQwVILHMk) `LWhQwVILHMk` | DK 3D | 28:05 | auto | 3552 | `praxe/mesh-terrain.md` | merge mesh-terrain-materialy → mesh-terrain (nová myšlenka) |

### PCG a procedurální svět · `P-PCG` (19)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [The NEW Instanced Actors Interop in 5.6 is Game Changing!](https://www.youtube.com/watch?v=B9s_1qkTRfI) `B9s_1qkTRfI` | Procedural Minds | 21:46 | auto | 4858 | `instanced-actors` |  |
| published | [I Recreated Fall Guy's Hex-A-Gone Game Using PCG. Here's How I Did It!](https://www.youtube.com/watch?v=G5eXYvFbMko) `G5eXYvFbMko` | Procedural Minds | 25:23 | auto | 5807 | `pcg-hexagone` | Hex-A-Gone; slug pcg-pripadovky → pcg-hexagone |
| published | [Spawn Vines On Any Mesh With A Single Click Using PCG Mode in UE5.7](https://www.youtube.com/watch?v=rYLF1up8sc8) `rYLF1up8sc8` | Procedural Minds | 26:27 | auto | 6701 | `pcg-liany` | liány na mesh; slug → pcg-liany |
| published | [Spawn Hanging PCG Vines And More Using This Simple Setup](https://www.youtube.com/watch?v=5bbKHksth9Q) `5bbKHksth9Q` | Procedural Minds | 25:18 | auto | 6205 | `pcg-liany` | visící liány; slug → pcg-liany |
| published | [SpeedTree to Nanite foliage with Wind! Unreal Engine 5.7](https://www.youtube.com/watch?v=67-W5lCSD_0) `67-W5lCSD_0` | lumpy668 | 16:30 | — | — | `pcg-vegetace` | bez přepisu — kryto z popisu (Pozn. u stromů) |
| published | [Everything You Need to Know About Procedural Vegetation in UE5.8 #tutorial #unrealengine #procedural](https://www.youtube.com/watch?v=DvBECqijNDg) `DvBECqijNDg` | PolyBoost | 14:09 | auto | 1042 | `pcg-vegetace` |  |
| published | [How to integrate PCG with landscape layers in Unreal engine 5 - Part 2](https://www.youtube.com/watch?v=hEHF0x22LpY) `hEHF0x22LpY` | Rbnks | 9:50 | auto | 1610 | `pcg-vegetace` | landscape layers |
| published | [Unreal Engine 5.7 - Procedural Vegetation - Build Your Own Forest - Tutorial (Part 1/2)](https://www.youtube.com/watch?v=o-kMXZX_oK8) `o-kMXZX_oK8` | Unreal - X - Tutorials | 9:04 | auto | 1235 | `pcg-vegetace` | les 1/2 |
| published | [Create a PCG forest with the new Megaplants and Collision in Unreal Engine 5](https://www.youtube.com/watch?v=ryb0sb2SQ-U) `ryb0sb2SQ-U` | Rbnks | 8:25 | auto | 1249 | `pcg-vegetace` | Megaplants |
| published | [Unreal Engine 5.7 - Create Forest Clearings & Paths With PCG - Tutorial](https://www.youtube.com/watch?v=8UxAmQfIj5s) `8UxAmQfIj5s` | Unreal - X - Tutorials | 8:20 | auto | 1102 | `pcg-vegetace` | mýtiny a cesty |
| published | [Unreal Engine 5.7 - PCG Vegatation - Build Your Own Forest - Tutorial (Part 2/2)](https://www.youtube.com/watch?v=4TZG9fBEiR0) `4TZG9fBEiR0` | Unreal - X - Tutorials | 6:20 | auto | 829 | `pcg-vegetace` | les 2/2 |
| published | [Unreal Engine 5.7 - How To Add Collision To PCG Wind Trees - Tutorial](https://www.youtube.com/watch?v=Ag6r2YNtSe0) `Ag6r2YNtSe0` | Unreal - X - Tutorials | 4:42 | auto | 619 | `pcg-vegetace` | kolize větrných stromů |
| published | [Unreal Engine 5.7 - Procedural Vegetation Pine Trees - Quick Tip](https://www.youtube.com/watch?v=Wqmr0bSR99U) `Wqmr0bSR99U` | Unreal - X - Tutorials | 1:26 | auto | 173 | `pcg-vegetace` | quick tip |
| skip | [SpeedTree 10 to Unreal Engine 5 with Wind Animation (Udemy Course)](https://www.youtube.com/watch?v=Kke6IaV7dc0) `Kke6IaV7dc0` | BlenderToUnreal | 1:23 | auto | 151 | `pcg-vegetace` | promo kurzu (1:23) — přeskočit? |
| published | [Unreal Engine 5.7 - Procedural Vegetation - Distance Wind Fix - QuickTip](https://www.youtube.com/watch?v=X_83dlYoZ7w) `X_83dlYoZ7w` | Unreal - X - Tutorials | 0:57 | auto | 120 | `pcg-vegetace` | quick tip |
| published | [Add Scattering To The PCG Mode Brush To Simulate Actual Painting](https://www.youtube.com/watch?v=AYulmKtqhLM) `AYulmKtqhLM` | Procedural Minds | 24:29 | auto | 5953 | `pcg-zaklady` | brush scattering |
| published | [How To Use the NEW UE5.7 PCG Mode, and Tips To Make It MORE Powerful!](https://www.youtube.com/watch?v=IPwVOhvQ2bo) `IPwVOhvQ2bo` | Procedural Minds | 23:29 | auto | 5451 | `pcg-zaklady` | PCG mode 5.7 (2 myšlenky) |
| published | [Precise Cutouts Using Collisions in UE5 PCG, And More Tips and Tricks](https://www.youtube.com/watch?v=-G14-4m4-LA) `-G14-4m4-LA` | Procedural Minds | 16:02 | auto | 3812 | `pcg-zaklady` | cutouts |
| published | [UE5.7 Just Upgraded PCG! Here’s How to Use the New Editor Tools](https://www.youtube.com/watch?v=fjuCUJ1r-Wk) `fjuCUJ1r-Wk` | All things GAME! | 15:03 | auto | 1585 | `pcg-zaklady` |  |

### Prostředí a environment art · `P-ENV` (11)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [This Developer Recreated San Francisco 1:1 in Unreal Engine 5](https://www.youtube.com/watch?v=TBGPbs9yjMM) `TBGPbs9yjMM` | Gorka Games | 36:19 | auto | 6875 | `env-breakdowny` | San Francisco 1:1 |
| published | [How 4 Artists Built a AAA World](https://www.youtube.com/watch?v=a78WoZeZGqI) `a78WoZeZGqI` | Next Level Game Art | 21:53 | auto | 3678 | `env-breakdowny` |  |
| published | [Why Resident Evil Requiem Looks So Real \| Graphics Breakdown](https://www.youtube.com/watch?v=utYMtJwGxiM) `utYMtJwGxiM` | Next Level Game Art | 17:33 | auto | 2201 | `env-breakdowny` | RE Requiem |
| published | [The ''Fake'' Geometry of Crimson Desert: How it Really Works](https://www.youtube.com/watch?v=44PT8XRZRGA) `44PT8XRZRGA` | Next Level Game Art | 13:30 | auto | 2025 | `env-breakdowny` | Crimson Desert |
| published | [The Environment Art Tricks Behind TLOU Part 1](https://www.youtube.com/watch?v=EJcqhvylH50) `EJcqhvylH50` | Next Level Game Art | 10:15 | auto | 1709 | `env-breakdowny` | TLOU |
| published | [How Crimson Desert Fakes Realism (It’s Genius)](https://www.youtube.com/watch?v=TUAyiCswYt4) `TUAyiCswYt4` | Next Level Game Art | 9:48 | auto | 1587 | `env-breakdowny` | Crimson Desert |
| published | [Forest Path Environment in UE5 \| Step-by-Step Tutorial](https://www.youtube.com/watch?v=WrjgH4sRja8) `WrjgH4sRja8` | Hoj Dee Studio | 131:44 | auto | 11297 | `env-tvorba` | 132 min |
| published | [How to create Cinematic dark Forest scene in Unreal Engine 5.5.4 \| Full Tutorial](https://www.youtube.com/watch?v=Eh8QgGhjxyg) `Eh8QgGhjxyg` | World Of VFX | 16:47 | auto | 3302 | `env-tvorba` | temný les |
| published | [Use this Technique to take your Environments to the next Level](https://www.youtube.com/watch?v=R9yr1ksLlmY) `R9yr1ksLlmY` | UNF Games | 14:54 | auto | 2282 | `env-tvorba` |  |
| published | [Unreal Engine 5.7 - Forest Atmosphere: Dynamic Audio & Falling Leaves - Tutorial](https://www.youtube.com/watch?v=ItHOm_BJpCM) `ItHOm_BJpCM` | Unreal - X - Tutorials | 14:20 | auto | 1839 | `env-tvorba` | audio + padající listí |
| skip | [DASH 1.12 - IMPROVED UE5 WORLD BUILDING TOOLS](https://www.youtube.com/watch?v=ZvTJBAkx_lY) `ZvTJBAkx_lY` | Polygonflow Dash | 6:40 | auto | 671 | `nastroje-treti-strany` | changelog nástroje — přeskočit? |

### Materiály a VFX · `P-MAT` (6)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [Smart Master Material Workflow in Unreal Engine 5 #tutorial  #unrealengine #substance_painter](https://www.youtube.com/watch?v=xLlFljzdLF4) `xLlFljzdLF4` | PolyBoost | 15:34 | auto | 918 | `materialy` | slug → materialy |
| published | [Easy Nanite Displacement in UE5 - Create Stunning Detail](https://www.youtube.com/watch?v=pLl25FaqCiI) `pLl25FaqCiI` | duongunreal | 30:09 | manual | 585 | `materialy` | slug → materialy |
| published | [Unreal Engine 5.4 Preview Nanite Cliff Tessellation RTX 4090](https://www.youtube.com/watch?v=CdyLdkRmFA0) `CdyLdkRmFA0` | Gorka Games | 2:19 | auto | 432 | `materialy` | preview (2:19); slug → materialy |
| published | [How To Create A Procedural Decay System - Unreal Engine 5 Material Tutorial](https://www.youtube.com/watch?v=OCgrHAHKmuM) `OCgrHAHKmuM` | Pitchfork Academy | 85:23 | auto | 13694 | `materialy` | 85 min (2 myšlenky); slug → materialy |
| published | [Stop Stretching Textures in UE5 #unrealengine #gamedev #indiedev](https://www.youtube.com/watch?v=kJgRLfyqjL0) `kJgRLfyqjL0` | Matt Aspland | 0:32 | auto | 107 | `materialy` | short; slug → materialy |
| published | [How To Use Toon Shading New In UE5.8 - Unreal Engine 5.8 Materials Tutorial](https://www.youtube.com/watch?v=iMJJYXHMw4o) `iMJJYXHMw4o` | Pitchfork Academy | 31:15 | auto | 5671 | `materialy` | slug → materialy |

### Osvětlení a atmosféra · `P-LIGHT` (6)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [Recreating Silent Hill 2 Fog in Unreal Engine 5](https://www.youtube.com/watch?v=96sheL5UqJQ) `96sheL5UqJQ` | Dallas Drapeau | 36:10 | auto | 4985 | `osvetleni` | Silent Hill 2; slug → osvetleni |
| published | [Realistic and Physical Lighting in UE5: The PBL Workflow](https://www.youtube.com/watch?v=GsE0mDtxtiQ) `GsE0mDtxtiQ` | arthur tasquin | 28:39 | manual | 5022 | `osvetleni` | slug → osvetleni |
| published | [Create a horror lighting in Unreal Engine.](https://www.youtube.com/watch?v=0w3SBb5ktlg) `0w3SBb5ktlg` | Karim aboushousha | 16:12 | auto | 1793 | `osvetleni` | slug → osvetleni |
| published | [How to make a simple night scene in Unreal Engine 5](https://www.youtube.com/watch?v=YHhRTjD_P2A) `YHhRTjD_P2A` | UE5 Poseidon | 8:28 | auto | 958 | `osvetleni` | slug → osvetleni |
| published | [Game Dev Secrets: How does light work? #indiegamedev #indiedev](https://www.youtube.com/watch?v=rzm8v5gx7l0) `rzm8v5gx7l0` | Inbound Shovel | 1:00 | auto | 254 | `osvetleni` | short (2D normal mapy); slug → osvetleni |
| published | [UE5 Lighting Tricks You Need to Know](https://www.youtube.com/watch?v=9PFrFDjVXHM) `9PFrFDjVXHM` | Sergey Maryshev | 0:51 | manual | 142 | `osvetleni` | short (3 triky); slug → osvetleni |

### Rendering a optimalizace · `P-PERF` (7)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [DLSS 4.5 Setup Guide for UE 5.7 Projects](https://www.youtube.com/watch?v=y80hX4IlzmI) `y80hX4IlzmI` | DK 3D | 25:10 | auto | 3078 | `textury-a-dlss` | slug → textury-a-dlss |
| published | [How to use Nanite Voxelization (like in the Witcher Demo)](https://www.youtube.com/watch?v=q2T4ni7UPfI) `q2T4ni7UPfI` | DK 3D | 11:25 | auto | 1467 | `optimalizace` | voxelizace; slug → optimalizace |
| published | [LOD or Nanite in UE5? \| Unreal Engine 5 Optimization Tutorial for Beginners](https://www.youtube.com/watch?v=-FmFOiqTO-8) `-FmFOiqTO-8` | Sergey Maryshev | 8:58 | manual | 1569 | `optimalizace` | LOD vs Nanite; slug → optimalizace |
| published | [Foliage Optimization Done Right (UE 5.7)](https://www.youtube.com/watch?v=QvE_EUuGFm4) `QvE_EUuGFm4` | Dallas Drapeau | 54:47 | auto | 8236 | `optimalizace` | 55 min (2 myšlenky); slug → optimalizace |
| published | [Why your levels are Slow in Unreal Engine 5](https://www.youtube.com/watch?v=4fjTSbDaeYQ) `4fjTSbDaeYQ` | Taken Grace | 34:16 | auto | 7923 | `optimalizace` | slug → optimalizace |
| published | [Stop Shipping 4K Textures — Right-Size Everything in UE5 (Surface Forge)](https://www.youtube.com/watch?v=WnHgLJcmhTM) `WnHgLJcmhTM` | Arghanion's Puzzlebox | 20:14 | auto | 4092 | `textury-a-dlss` | slug → textury-a-dlss |
| published | [Virtual Textures vs Atlases: The Truth about UE5 Optimization](https://www.youtube.com/watch?v=_fUzAKlxiQg) `_fUzAKlxiQg` | Sergey Maryshev | 7:42 | manual | 1386 | `textury-a-dlss` | virtual textures; slug → textury-a-dlss |

### MetaHuman · `P-MH` (5)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [New Unreal Engine 5.8 Metahuman Crowd Plugin](https://www.youtube.com/watch?v=bJIPlvmoTVw) `bJIPlvmoTVw` | Smart Poly | 9:04 | auto | 1756 | `praxe/metahuman.md` | merge 4 slugů do 1 kapitoly |
| published | [Unreal Engine 5.7 - Turn Your Metahuman Into A Player Character - Tutorial](https://www.youtube.com/watch?v=cARn14Ec14w) `cARn14Ec14w` | Unreal - X - Tutorials | 6:07 | auto | 778 | `praxe/metahuman.md` |  |
| published | [Optimize Metahuman Facial Performance \| Metapipe 3.3 Nitrous](https://www.youtube.com/watch?v=TE9NJHHVHsM) `TE9NJHHVHsM` | Arts and Spells | 12:05 | auto | 1994 | `praxe/metahuman.md` | placený Maya nástroj — psáno s tímto vědomím |
| published | [Unreal Engine 5.7 - Metahuman Cinematic Look At System - Tutorial](https://www.youtube.com/watch?v=UBSNmxXurkk) `UBSNmxXurkk` | Unreal - X - Tutorials | 9:08 | auto | 1247 | `praxe/metahuman.md` | look-at |
| published | [Unreal Engine 5.6 - Chaos Cloth for Metahuman - Tutorial](https://www.youtube.com/watch?v=RXq1X8q04Dk) `RXq1X8q04Dk` | Unreal - X - Tutorials | 6:48 | auto | 790 | `praxe/metahuman.md` | Chaos Cloth |

### AI nástroje ve vývoji · `P-AITOOLS` (14)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [AI Animation Just Got a Revolution — NVIDIA Kimodo](https://www.youtube.com/watch?v=CVA4jGHAbnA) `CVA4jGHAbnA` | Stefan 3D AI | 6:47 | manual | 1211 | `ai-assety` | NVIDIA Kimodo; slug → ai-assety |
| published | [From AI to Metahuman - Best New UE 5.8 Workflow for Custom Character](https://www.youtube.com/watch?v=4w7oA4oJMqs) `4w7oA4oJMqs` | Stefan 3D AI | 28:22 | manual | 5461 | `ai-assety` | → MetaHuman 5.8 · přečištěno 2026-10-11 z ruční `en` (dřív zpětný překlad `en-it`) |
| published | [I Built a Modular Character with AI (Full Workflow)](https://www.youtube.com/watch?v=gZIxrX1n2D4) `gZIxrX1n2D4` | Stefan 3D AI | 26:54 | manual | 5047 | `ai-assety` | modulární postava |
| published | [Claude Took Over ComfyUI + Blender: Here's What Happened](https://www.youtube.com/watch?v=KdYv_TT-ZnQ) `KdYv_TT-ZnQ` | PixelArtistry | 23:07 | auto | 4860 | `claude-code-ue` | ComfyUI+Blender; slug → claude-code-ue |
| published | [From AI to Playable 3D Character in Unreal Engine](https://www.youtube.com/watch?v=k1xBERhXtHA) `k1xBERhXtHA` | Stefan 3D AI | 22:04 | manual | 4195 | `ai-assety` | hratelná postava tandem |
| published | [Next-Gen 3D AI Is Here (5-Second Game-Ready Models)](https://www.youtube.com/watch?v=mXjUz3viYmQ) `mXjUz3viYmQ` | Stefan 3D AI | 19:48 | manual | 3282 | `ai-assety` | Tripo vs Hunyuan vs Rodin |
| published | [Complete Free AI Workflow for Game-Ready 3D Characters](https://www.youtube.com/watch?v=TkP-_LyacMI) `TkP-_LyacMI` | Stefan 3D AI | 12:09 | manual | 2316 | `ai-assety` | free pipeline |
| published | [Make infinite characters in the SAME style!](https://www.youtube.com/watch?v=LcJQQwltQ2Q) `LcJQQwltQ2Q` | PixelLab | 11:06 | auto | 1744 | `ai-assety` | 2D styl konzistence (PixelLab) |
| published | [From Dialogue to Action: Create Scene-Aware AI Characters That Act AND React \| Convai Unreal Engine](https://www.youtube.com/watch?v=lB5_KRWdg_w) `lB5_KRWdg_w` | Convai | 5:20 | auto | 889 | `claude-code-ue` | produkt Convai; slug → claude-code-ue |
| published | [I Built My Dream Game in 72 Hours — Assets by AI, Gameplay by Claude Code](https://www.youtube.com/watch?v=k9cbm5jSOxk) `k9cbm5jSOxk` | Stefan 3D AI | 35:14 | manual | 5812 | `claude-code-ue` | hra za 72 h (capstone) · přečištěno 2026-10-11 z ruční `en` (dřív zpětný překlad `en-ko`) |
| published | [Claude Code Took Over Unreal Engine 5 and Built a Game](https://www.youtube.com/watch?v=iRcrZjOt5H8) `iRcrZjOt5H8` | Stefan 3D AI | 16:45 | manual | 3136 | `claude-code-ue` | endless runner stress test |
| published | [NEW Unreal Engine 5.8 MCP Tutorial (QuickStart Guide)](https://www.youtube.com/watch?v=PqrKqhkj3gQ) `PqrKqhkj3gQ` | Smart Poly | 12:21 | auto | 2579 | `claude-code-ue` | MCP 5.8 setup |
| published | [This AI builds blueprints for you in Unreal Engine](https://www.youtube.com/watch?v=Kzy7isA2xO0) `Kzy7isA2xO0` | TUF | 7:42 | auto | 1048 | `claude-code-ue` | produkt Blueprint AI |
| published | [How to Setup Claude Code in Unreal Engine 5.8 (Easy)](https://www.youtube.com/watch?v=0tzXVwDxzt8) `0tzXVwDxzt8` | Unreal University  | 5:51 | auto | 1066 | `claude-code-ue` | Claude Code setup |

### Editor a workflow · `P-EDITOR` (12)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [5 Years Of Unreal Engine Experience In 9 Minutes](https://www.youtube.com/watch?v=BHY46bPmsXY) `BHY46bPmsXY` | Unreal University  | 9:14 | auto | 1805 | `praxe/editor-tipy.md` | 5 let zkušeností |
| published | [UE5 for Beginners: 5 Tips I Wish I Knew Sooner](https://www.youtube.com/watch?v=jxEfh8_zfdk) `jxEfh8_zfdk` | Sergey Maryshev | 0:48 | manual | 148 | `praxe/editor-tipy.md` | short (5 tipů) |
| published | [Change Your Mesh's Pivot Point in the Engine! #unrealengine5 #modelingmode #pivot #ue5 #blender](https://www.youtube.com/watch?v=f50yoTWThnw) `f50yoTWThnw` | Druid Mechanics | 0:41 | auto | 192 | `praxe/editor-tipy.md` | short — pivot |
| published | [The Secret 3D Box-Select Tool in UE5! 🤯 #unrealengine #indiedev #gamedev](https://www.youtube.com/watch?v=HprvvfEzrNI) `HprvvfEzrNI` | Matt Aspland | 0:30 | auto | 100 | `praxe/editor-tipy.md` | short — box select |
| published | [Stop Deleting Blueprint Nodes Like This! #unrealengine #gamedev #indiedev](https://www.youtube.com/watch?v=Pt1tFh4UqJk) `Pt1tFh4UqJk` | Matt Aspland | 0:28 | auto | 98 | `praxe/editor-tipy.md` | short — Shift+Delete |
| published | [Select EVERY Copy of an Asset Instantly in UE5! 🤯 #unrealengine #gamedev #indiedev](https://www.youtube.com/watch?v=De2fXs2JZxw) `De2fXs2JZxw` | Matt Aspland | 0:27 | auto | 102 | `praxe/editor-tipy.md` |  |
| published | [5 Unreal Engine Tricks Every Beginner Misses #unrealengine #indiedev #gamedev](https://www.youtube.com/watch?v=kSHz_V79eCk) `kSHz_V79eCk` | Matt Aspland | 0:26 | auto | 81 | `praxe/editor-tipy.md` | short (5 triků) |
| published | [The Secret to Realistic Level Design in UE5 #unrealengine #gamedev #indiedev](https://www.youtube.com/watch?v=qo-LYeeKMr4) `qo-LYeeKMr4` | Matt Aspland | 0:26 | auto | 88 | `praxe/editor-tipy.md` | short — physics placement |
| published | [How To Fix Editor Lag In 30 Seconds! #unrealengine5 #indiedev](https://www.youtube.com/watch?v=U0nC8-882a0) `U0nC8-882a0` | Matt Aspland | 0:22 | auto | 73 | `praxe/editor-tipy.md` | short — editor lag |
| todo | [Unreal Engine 5.7.1 Beginner Tutorial - UE5 Starter Course 2026#unrealengine5  #megascans #cgi](https://www.youtube.com/watch?v=0yBSEiMldo0) `0yBSEiMldo0` | Magnet VFX | 97:40 | auto | 13268 | `kurzy` | kurz pro začátečníky (98 min) — nízká priorita |
| skip | [Unreal Engine 5.8 JUST DROPPED (Mesh Terrain, Control Rig, Physics, AI)](https://www.youtube.com/watch?v=sDLYd2keSwA) `sDLYd2keSwA` | Proj Prod | 12:44 | manual | 2188 | `novinky` | novinkové video — přeskočit? |
| skip | [Unreal Engine 5.8 Feature Highlights](https://www.youtube.com/watch?v=ExFF5gXVhDU) `ExFF5gXVhDU` | Unreal Engine | 3:26 | manual | 412 | `novinky` | novinkové video — přeskočit? · přečištěno 2026-10-11 z ruční `en` (dřív zpětný překlad `en-ko`) |

---

## Hudba a zvuk · Phase 7 _(samostatný playlist „Gamedev-music")_

Nový top-level dokument z 17videového playlistu o tvorbě hudby a zvuku (ne hlavní studijní playlist). Taxonomie schválena uživatelem 2026-07-17; 5 témat / 12 kapitol; **všech 17 videí published** v dávkách A–C (2026-07-17). Video `P_GLkYNBhBY` živí dvě kapitoly (melodická a akordová půlka).

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [The Physics Of Dissonance](https://www.youtube.com/watch?v=tCsl6ZcY9ag) `tCsl6ZcY9ag` | minutephysics | 27:58 | auto | 5874 | `hudba/fyzika-souzvuku.md` | dávka A |
| published | [Music Theory Basics Explained \|\| Music for Games is Easy](https://www.youtube.com/watch?v=K74fbAxO0wg) `K74fbAxO0wg` | Seraphin | 9:20 | auto | 1316 | `hudba/hudebni-teorie-zaklady.md` | dávka A |
| published | [how to actually write good melodies](https://www.youtube.com/watch?v=0BYBNSHMA0o) `0BYBNSHMA0o` | flowerhead | 13:05 | auto | 1942 | `hudba/melodie.md` | dávka A |
| published | [Rhythm Rule for Better Melodies](https://www.youtube.com/watch?v=WTj-b6oD-Ks) `WTj-b6oD-Ks` | Hack Music Theory | 5:58 | auto | 852 | `hudba/melodie.md` | dávka A |
| published | [Give me 12 minutes… chords & melodies](https://www.youtube.com/watch?v=P_GLkYNBhBY) `P_GLkYNBhBY` | Arcade | 12:13 | auto | 1759 | `hudba/melodie.md` + `hudba/akordy-a-harmonie.md` | dávka A — 2 kapitoly |
| published | [Why Avicii's Melodies Are So Good](https://www.youtube.com/watch?v=qSjmVBXHuJo) `qSjmVBXHuJo` | Alex Rome | 15:37 | auto | 1698 | `hudba/melodie.md` | dávka A — případovka |
| published | [How to Make Emotional Chord Patterns (10 Ways)](https://www.youtube.com/watch?v=U5QucXeCiwU) `U5QucXeCiwU` | Alex Rome | 17:14 | auto | 2197 | `hudba/akordy-a-harmonie.md` | dávka A |
| published | [An Insanely Simple Arrangement System](https://www.youtube.com/watch?v=ZkRds6iTfhQ) `ZkRds6iTfhQ` | Alex Rome | 12:54 | auto | 1689 | `hudba/aranz.md` | dávka B |
| published | [Analyzing 20 Genres And Their Unique Melodies](https://www.youtube.com/watch?v=0vLNybDXh2g) `0vLNybDXh2g` | Servida Music | 19:40 | auto | 3824 | `hudba/zanry-a-styl.md` | dávka B |
| published | [How To Make Any Sound From Scratch](https://www.youtube.com/watch?v=p1-WmITJqBk) `p1-WmITJqBk` | Alex Rome | 24:04 | auto | 3039 | `hudba/synteza-zvuku.md` | dávka B |
| published | [So You Wanna Make Games?? Ep. 8: Sound Design](https://www.youtube.com/watch?v=KcorIwJscFA) `KcorIwJscFA` | Riot Games | 14:31 | manual | 1844 | `hudba/sound-design-ve-hre.md` | dávka B |
| published | [Why Indie Games Have The Best Sound Design](https://www.youtube.com/watch?v=VJ6ENLakB2g) `VJ6ENLakB2g` | Marshall McGee | 10:14 | auto | 1936 | `hudba/sound-design-ve-hre.md` | dávka B |
| published | [How to Make a Video Game Soundtrack (from scratch)](https://www.youtube.com/watch?v=1qPfH95ry84) `1qPfH95ry84` | Jaies | 43:23 | auto | 5822 | `hudba/tvorba-soundtracku.md` | dávka C |
| published | [A Guide to Making Video Game Music](https://www.youtube.com/watch?v=dMkTdYmOgiQ) `dMkTdYmOgiQ` | Zectro | 10:35 | auto | 1577 | `hudba/tvorba-soundtracku.md` | dávka C |
| published | [How To Make Music FAST and FREE for your Indie Games!](https://www.youtube.com/watch?v=2jLeuviQ7Ho) `2jLeuviQ7Ho` | Madbook | 15:59 | auto | 2924 | `hudba/nastroje-zdarma-a-game-jam.md` | dávka C |
| published | [The Composer Roadmap I Wish I Had at 18](https://www.youtube.com/watch?v=1E1EjqIrZD4) `1E1EjqIrZD4` | Inside the Score | 28:01 | auto | 5734 | `hudba/cesta-skladatele.md` | dávka C |
| published | [My ROUGH Gamedev Music Experience](https://www.youtube.com/watch?v=3uvJQWxFX4Y) `3uvJQWxFX4Y` | Brainless. | 19:28 | auto | 3434 | `hudba/zacit-a-vydrzet.md` | dávka C — kapitola, ne zápisek |

---

## Druhá vlna hlavního playlistu (+116) · Phase 8 _(strom schválen 2026-07-18; dávky 20–23 published)_

Hlavní playlist narostl 210 → 327 (uživatel přidával průběžně; staženo + vyčištěno 2026-07-17 při music fetchi). Klasifikace z titulů + kanálů s nahlédnutím do ~30 přepisů (hraniční případy). **Celkem 116 videí, ~512k slov.** Po schválení se počty promítnou do stromu v hlavičce a tabulky níže se stanou ostrými řádky indexu (statusy se aktualizují na místě).

**Co je ve vlně jiného než v první:** těžiště se přesunulo k Teorii (86/116). Dominují: **Indie Game Clinic (36 videí!)** — systematický design-theory korpus (zábava, obtížnost, žánry, GDD, playtesting, marketing); **Riot „So You Wanna Make Games??"** (9 dílů — E8 Sound Design už je published v `hudba/sound-design-ve-hre.md`, série se novou vlnou kompletuje); matematicko-programátorský blok (Visual Kernel, SimonDev, Veritasium, Fireship); byznys podcasty (3× 95–103 min). Praxe UE tvoří jen 27 videí — většina jde jako **rozšíření existujících kapitol** (Elzoheiry → Blueprint kapitoly, 5.8 novinky → MM/MetaHuman/AI nástroje).

**Navrhovaná nová témata (6):**

- **Teorie** — Učení a růst v éře AI `T-LEARN` (8) · Programátorské myšlení `T-PROG` (4) · Matematika a algoritmy `T-MATH` (7) · Byznys, data a kariéra `T-BIZ` (6) · Herní umění a vizuál `T-ART` (13)
- **Praxe** — Tvorba assetů mimo engine (Blender) `P-ASSET` (4)

Zbytek jde do existujících témat; 3 videa do dokumentu Hudba a zvuk. **Rozhodnuto uživatelem 2026-07-18:** T-DESIGN se v nav rozdělí na „Základy designu" (zaklady, zabava, game-feel, pribeh-a-postavy + rozšíření z vlny) a nové téma **„Design do hloubky" `T-DEEP`** (obtiznost, systemy-a-mechaniky, ludonarativni-soulad, zanry, engineering-experiences, pripadovky-designu, horor-design, kamera — vše nové kapitoly z vlny 2); nav-only změna, provede se s první kapitolou T-DEEP. Oba nové beginner kurzy potvrzeny jako **low-priority** (konzistentně s Phase 2).

**Navrhované dávky (pokračování číslování; 10–25 videí / dávka):**

| dávka | téma | videí | ~slov |
|---|---|---|---|
| 20 | Matematika a programátorské myšlení (T-MATH + T-PROG) | 11 | 46k |
| 21 | Mindset a učení (T-MIND + T-LEARN) | 17 | 47k |
| 22 | Design I: základy, zábava, obtížnost, systémy | 10 | 45k |
| 23 | Design II: žánry, případovky, horor, kamera (vč. Tynan 95 min) | 8 | 57k |
| 24 | Scope, GDD a playtesting (T-SCOPE) | 11 | 51k |
| 25 | Herní umění a vizuál (T-ART) | 13 | 34k |
| 26 | Level design + Vydání a marketing (T-LEVEL + T-MARKET) | 10 | 56k |
| 27 | Byznys, data a kariéra (T-BIZ; 3 dlouhé podcasty) | 6 | 59k |
| 28 | Praxe: architektura, AI, animace, pohyb (P-BP, P-AI-NPC, P-ANIM…) | 12 | 44k |
| 29 | Praxe: vizuál, optimalizace, AI nástroje, editor | 9 | 21k |
| 30 | Blender assety + rozšíření Hudby (P-ASSET + H-EXT) | 7 | 11k |

_(114 videí v dávkách + 2 low-priority kurzy mimo dávky = 116.)_

### Tvůrčí proces a mindset · `T-MIND` (+9)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [You Can Make Other Things](https://www.youtube.com/watch?v=rv4okZp-mk0) `rv4okZp-mk0` | Indie Game Clinic | 7:49 | auto | 1688 | `teorie/proc-tvorit.md` | rozšíření kapitoly · dávka 21 |
| published | [Why “Motivation” is Overrated](https://www.youtube.com/watch?v=kUTFNgESEUg) `kUTFNgESEUg` | Indie Game Clinic | 21:07 | auto | 4322 | `teorie/produktivita.md` | rozšíření: motivace vs. systém · dávka 21 |
| published | [Why 99% of Devs Never Ship Their First Game (I Have the Data)](https://www.youtube.com/watch?v=2PKTvinv-oo) `2PKTvinv-oo` | Gorka Games | 6:59 | auto | 1168 | `teorie/produktivita.md` | data o dokončování; pozor: promo challenge · dávka 21 |
| published | [Stop Looking For Game Dev "Advice"](https://www.youtube.com/watch?v=d5VdFScmXcM) `d5VdFScmXcM` | Indie Game Clinic | 18:53 | auto | 3399 | `teorie/rady-z-praxe.md` | meta: rozšíření — kdy rady nefungují · dávka 21 |
| published | [The Game Dev Advice You Actually Need (Ft. AIA, Goodgis, and more...)](https://www.youtube.com/watch?v=n3fjdwJ5eQk) `n3fjdwJ5eQk` | Juniper Dev | 14:27 | auto | 3068 | `teorie/rady-z-praxe.md` | kompilace rad více tvůrců · dávka 21 |
| published | [I Wasted 6 Years Making Games...](https://www.youtube.com/watch?v=jDPxHf_6KuI) `jDPxHf_6KuI` | Sunny Gamedev | 6:29 | — | — | `teorie/rady-z-praxe.md` | bez přepisu — krýt z popisu · dávka 21 |
| published | [How To Make A Game Alone](https://www.youtube.com/watch?v=my8euq9bzFQ) `my8euq9bzFQ` | Dog's Dream | 26:13 | auto | 3859 | `teorie/solo-vyvoj.md` | dávka 21 |
| published | [Creativity isn't a gift, it's a system](https://www.youtube.com/watch?v=_QVYfPnNOg4) `_QVYfPnNOg4` | Perry Daniels | 13:07 | manual | 2470 | `teorie/tvurci-zasek.md` | kreativita jako systém · dávka 21 |
| published | [Hayao Miyazaki's wisdom for stuck artists](https://www.youtube.com/watch?v=RT-SJvjw8xQ) `RT-SJvjw8xQ` | Adam Westbrook | The Long Game | 9:21 | auto | 1738 | `teorie/tvurci-zasek.md` | dávka 21 |

### Učení a růst v éře AI · `T-LEARN` (+8) ⭐ NOVÉ TÉMA

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [Coding is Hard Until You Learn This](https://www.youtube.com/watch?v=gaCY4QxfSzA) `gaCY4QxfSzA` | Phillip Choi | 19:28 | auto | 3240 | `teorie/jak-se-ucit-kodovat.md` | dávka 21 |
| published | [Why You Struggle to Learn Game Coding](https://www.youtube.com/watch?v=SU8d0c9aAQo) `SU8d0c9aAQo` | Indie Game Clinic | 14:32 | auto | 2785 | `teorie/jak-se-ucit-kodovat.md` | IGC: proč se herní kód učí špatně · dávka 21 |
| published | [How to Actually LEARN from YouTube Tutorials!](https://www.youtube.com/watch?v=APwQFdaH0eY) `APwQFdaH0eY` | Brainless. | 8:56 | auto | 2314 | `teorie/jak-se-ucit-kodovat.md` | cross-link: tutorial hell v editor-tipy · dávka 21 |
| published | [3 Projects for Beginners: Game Design and Art Fundamentals](https://www.youtube.com/watch?v=cf9xDdPXOA0) `cf9xDdPXOA0` | Indie Game Clinic | 37:19 | manual | 7753 | `teorie/prvni-projekty.md` | 3 projekty pro začátečníky (IGC, univerzitní kurz) · dávka 21 |
| published | [The New Way of Being a Software Engineer In the Age of AI](https://www.youtube.com/watch?v=mYzbbjA3smY) `mYzbbjA3smY` | Phillip Choi | 16:02 | auto | 2777 | `teorie/uceni-v-ere-ai.md` | role inženýra v éře AI · dávka 21 |
| published | [How To Become Dangerously Self-Educated (with AI)](https://www.youtube.com/watch?v=VeU6gScy92s) `VeU6gScy92s` | Sandeep Swadia | 17:41 | auto | 2757 | `teorie/uceni-v-ere-ai.md` | sebevzdělávání s AI · dávka 21 |
| published | [A CS Professor on Why Slow Learning Wins in the AI Era \| CU Boulder, Tom Yeh](https://www.youtube.com/watch?v=BAgxGp2WEu4) `BAgxGp2WEu4` | EO | 12:38 | auto | 2342 | `teorie/uceni-v-ere-ai.md` | pomalé učení, CU Boulder · dávka 21 |
| published | [The Art Of Winning In Tech](https://www.youtube.com/watch?v=4MAupwjl3pc) `4MAupwjl3pc` | Lattice | 6:24 | auto | 1496 | `teorie/uceni-v-ere-ai.md` | kariérní pohled, spíš SW obecně · dávka 21 |

### Programátorské myšlení · `T-PROG` (+4) ⭐ NOVÉ TÉMA

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [7 Design Patterns EVERY Developer Should Know](https://www.youtube.com/watch?v=BJatgOiiht4) `BJatgOiiht4` | ForrestKnight | 22:01 | auto | 4139 | `teorie/design-patterns.md` | cross-link: komunikace-blueprintu (observer…) · dávka 20 |
| published | [Programming Thinking](https://www.youtube.com/watch?v=KtBefDeECVU) `KtBefDeECVU` | Visual Kernel | 129:56 | auto | 19488 | `teorie/programatorske-mysleni.md` | 130 min — kotva tématu · dávka 20 |
| published | [Programming Concepts Only the TOP 0.1% Know](https://www.youtube.com/watch?v=5xSQR5shQYk) `5xSQR5shQYk` | Shade of Code | 3:49 | auto | 834 | `teorie/programatorske-mysleni.md` | krátké — koncepty · dávka 20 |
| published | [15 Tiny Coding Hacks That Got Me In Amazon](https://www.youtube.com/watch?v=Z36-xqUv3W8) `Z36-xqUv3W8` | Manware | 9:44 | auto | 1833 | `teorie/programatorske-navyky.md` | drobné návyky; mimo gamedev kontext · dávka 20 |

### Matematika a algoritmy · `T-MATH` (+7) ⭐ NOVÉ TÉMA

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [10 weird algorithms every developer should know](https://www.youtube.com/watch?v=SmyPTnlqhlk) `SmyPTnlqhlk` | Fireship | 9:05 | auto | 1981 | `teorie/algoritmy-prehled.md` | Fireship — 10 algoritmů · dávka 20 |
| published | [SVD Visualized, Singular Value Decomposition explained \| SEE Matrix , Chapter 3 #SoME2](https://www.youtube.com/watch?v=vSczTbgc8Rc) `vSczTbgc8Rc` | Visual Kernel | 16:27 | auto | 2312 | `teorie/linearni-algebra-vizualne.md` | SEE Matrix ch.3 — SVD · dávka 20 |
| published | [Visualize Spectral Decomposition \| SEE Matrix, Chapter 2](https://www.youtube.com/watch?v=mhy-ZKSARxI) `mhy-ZKSARxI` | Visual Kernel | 15:55 | auto | 2083 | `teorie/linearni-algebra-vizualne.md` | SEE Matrix ch.2 — spektrální rozklad · dávka 20 |
| published | [Visualize Different Matrices part1 \| SEE Matrix, Chapter 1](https://www.youtube.com/watch?v=7Gtxd-ew4lk) `7Gtxd-ew4lk` | Visual Kernel | 14:51 | auto | 1871 | `teorie/linearni-algebra-vizualne.md` | SEE Matrix ch.1 · dávka 20 |
| published | [The Strange Math That Predicts (Almost) Anything](https://www.youtube.com/watch?v=KZeIEiBrT_w) `KZeIEiBrT_w` | Veritasium | 32:32 | manual | 5631 | `teorie/markovovy-retezce.md` | Veritasium; most k AI/PCG · dávka 20 |
| published | [What Kind of Math Should Game Developers Know?](https://www.youtube.com/watch?v=eRVRioN4GwA) `eRVRioN4GwA` | SimonDev | 19:39 | auto | 3657 | `teorie/matematika-pro-gamedev.md` | SimonDev — jaká matika je potřeba · dávka 20 |
| published | [The Math Hack That Made Quake 3 Possible](https://www.youtube.com/watch?v=coU_o6L5XZI) `coU_o6L5XZI` | Dr. Pavel Vlašánek | 17:10 | manual | 2621 | `teorie/matematika-pro-gamedev.md` | případovka: fast inverse sqrt (Quake 3) · dávka 20 |

### Nápad, scope a plánování · `T-SCOPE` (+11)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [What Do "Professional" Game Design Documents Look Like? 📜](https://www.youtube.com/watch?v=fk-rQlrNYZ8) `fk-rQlrNYZ8` | Indie Game Clinic | 41:21 | auto | 7826 | `teorie/gdd.md` | jak vypadají profesionální GDD · dávka 24 |
| published | [Game Design Documents - a Minimalist Approach 🧘🏽](https://www.youtube.com/watch?v=uBxYGFRi-S4) `uBxYGFRi-S4` | Indie Game Clinic | 37:44 | manual | 7296 | `teorie/gdd.md` | minimalistický přístup; cross-link zápisek gdd-review · dávka 24 |
| published | [How to find amazing game ideas](https://www.youtube.com/watch?v=0m60QbT85Tc) `0m60QbT85Tc` | Game Maker's Toolkit | 27:09 | manual | 4856 | `teorie/napad.md` | rozšíření (GMTK) · dávka 24 |
| published | [The Secret to GOOD Game Ideas 💡 [Practical Ideation Methods Explained]](https://www.youtube.com/watch?v=LMOCQNcMleg) `LMOCQNcMleg` | Indie Game Clinic | 24:29 | auto | 4622 | `teorie/napad.md` | rozšíření (IGC ideation) · dávka 24 |
| published | [Manage Your GameDev Projects with Trello/Kanban](https://www.youtube.com/watch?v=-SqcrlAarGo) `-SqcrlAarGo` | Indie Game Clinic | 22:33 | auto | 4741 | `teorie/planovani-nastroje.md` | Trello/Kanban · dávka 24 |
| published | [The ULTIMATE Playtest Guide](https://www.youtube.com/watch?v=zXNRJuc48Ek) `zXNRJuc48Ek` | Indie Game Clinic | 39:27 | auto | 7549 | `teorie/playtesting.md` | pozn. sponzor GameMaker segment · dávka 24 |
| published | [GameDev as an Iterative Spiral](https://www.youtube.com/watch?v=9L6XX9kDQyA) `9L6XX9kDQyA` | Indie Game Clinic | 12:30 | auto | 2656 | `teorie/prototypovani.md` | rozšíření: iterační spirála · dávka 24 |
| published | [9 Months of Dev… Pivot or Perish?](https://www.youtube.com/watch?v=CbWpsNs7nrg) `CbWpsNs7nrg` | Indie Game Clinic | 28:57 | auto | 6003 | `teorie/scope.md` | pivot po 9 měsících · dávka 24 |
| published | [Stopping Scope Creep without Crushing Creativity (Stream Highlights)](https://www.youtube.com/watch?v=Xyl3tsZx4wQ) `Xyl3tsZx4wQ` | Indie Game Clinic | 10:02 | auto | 2113 | `teorie/scope.md` | rozšíření: scope creep · dávka 24 |
| published | [How I Made A Steam Game In Only 1 Month](https://www.youtube.com/watch?v=7naIKclU1A4) `7naIKclU1A4` | Zoteling | 6:53 | auto | 1470 | `teorie/scope.md` | devlog: hra za měsíc · dávka 24 |
| published | [How To Make Small Games \| Indie Game Dev Tutorial](https://www.youtube.com/watch?v=U-j91fw648Q) `U-j91fw648Q` | RETRODEAD | 5:27 | auto | 1399 | `teorie/scope.md` | malé hry · dávka 24 |

### Základy designu · `T-DESIGN` (+18)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [Tynan Sylvester - Designing Games, A Guide to Engineering Experiences (GDL ep07)](https://www.youtube.com/watch?v=RFSxLRBht14) `RFSxLRBht14` | Indie Game Clinic | 95:02 | auto | 20346 | `teorie/engineering-experiences.md` | Tynan Sylvester — kniha Designing Games (95 min) · dávka 23 |
| published | [INDIE Game DevLog - Why GOOD Combat Is So HARD To Make (June 2026)](https://www.youtube.com/watch?v=NYqyAL7FKYg) `NYqyAL7FKYg` | SILKROAD Project | 15:20 | manual | 2843 | `teorie/game-feel.md` | devlog: proč je dobrý combat těžký · dávka 22 |
| published | [10 Ways to Improve Game Feel](https://www.youtube.com/watch?v=qCj9CZoAvFY) `qCj9CZoAvFY` | Design Diary | 10:37 | auto | 2078 | `teorie/game-feel.md` | rozšíření: 10 způsobů · dávka 22 |
| published | [How To Create A Horror Game That SCARES](https://www.youtube.com/watch?v=JVTWbRMHYeY) `JVTWbRMHYeY` | Devilish Inks | 37:17 | auto | 8040 | `teorie/horor-design.md` | jak vyvolat strach · dávka 23 |
| published | [How Metroidvania Cameras are Shockingly Different than Platformer Cameras](https://www.youtube.com/watch?v=drbatB2KWlo) `drbatB2KWlo` | Inbound Shovel | 20:33 | auto | 4929 | `teorie/kamera.md` | metroidvania vs. platformer kamery · dávka 23 |
| published | [LUDOTHEMATICS: Harmony and Dissonance in Game Design](https://www.youtube.com/watch?v=uG-RPNilP-8) `uG-RPNilP-8` | Indie Game Clinic | 39:24 | auto | 7769 | `teorie/ludonarativni-soulad.md` | ludothematics: harmonie a disonance · dávka 22 |
| published | [Challenge & Difficulty in Game Design](https://www.youtube.com/watch?v=FLCet4Z7zew) `FLCet4Z7zew` | Indie Game Clinic | 49:58 | auto | 9741 | `teorie/obtiznost.md` | challenge & difficulty (IGC, 50 min) · dávka 22 |
| published | [This Puzzle Platformer Has a Unique Approach to Difficulty [Octojump]](https://www.youtube.com/watch?v=IcSD7w-fdJ8) `IcSD7w-fdJ8` | Indie Game Clinic | 6:28 | auto | 1172 | `teorie/obtiznost.md` | případovka Octojump · dávka 22 |
| published | [Indie Soulsborne "Fade: The First Chapter" - Game Design Deep-Dive](https://www.youtube.com/watch?v=cIi-mgZUELE) `cIi-mgZUELE` | Indie Game Clinic | 28:09 | auto | 4574 | `teorie/pripadovky-designu.md` | soulsborne Fade deep-dive · dávka 23 |
| published | [I Played 150 of Your Games; Common Problems (and Solutions!)](https://www.youtube.com/watch?v=8bYnlOE_pl0) `8bYnlOE_pl0` | Indie Game Clinic | 21:26 | manual | 4078 | `teorie/pripadovky-designu.md` | 150 her — časté problémy · dávka 23 |
| published | [Game Mechanics & Systems Thinking](https://www.youtube.com/watch?v=nkLmjJK3vOw) `nkLmjJK3vOw` | Indie Game Clinic | 40:49 | auto | 7443 | `teorie/systemy-a-mechaniky.md` | cross-link smycky-a-retezce · dávka 22 |
| published | [What is Fun? A Game Design Introduction](https://www.youtube.com/watch?v=56ENqlUST9U) `56ENqlUST9U` | Indie Game Clinic | 31:10 | manual | 4766 | `teorie/zabava.md` | rozšíření: What is Fun (IGC) · dávka 22 |
| published | [Game Design Theory: A Guided Tour](https://www.youtube.com/watch?v=TATKLd1Q6ho) `TATKLd1Q6ho` | Indie Game Clinic | 31:14 | auto | 5423 | `teorie/zaklady.md` | přehled teorií designu (IGC) · dávka 22 |
| published | [How To Think Like A Game Designer](https://www.youtube.com/watch?v=iIOIT3dCy5w) `iIOIT3dCy5w` | Game Maker's Toolkit | 13:06 | manual | 2245 | `teorie/zaklady.md` | rozšíření (GMTK) · dávka 22 |
| published | [The 10 Basic Principles of Game Design Every Indie Dev Should Know](https://www.youtube.com/watch?v=5Fk7p-f2ymY) `5Fk7p-f2ymY` | NOBL Games | 12:18 | auto | 1822 | `teorie/zaklady.md` | 10 principů · dávka 22 |
| published | [Game Genres - a Design Perspective](https://www.youtube.com/watch?v=3KJbYdNP5js) `3KJbYdNP5js` | Indie Game Clinic | 38:00 | auto | 7937 | `teorie/zanry.md` | žánry očima designu · dávka 23 |
| published | [Indie Game Genres & Subtractive Design](https://www.youtube.com/watch?v=RkcmljWlvrs) `RkcmljWlvrs` | Indie Game Clinic | 21:41 | manual | 3713 | `teorie/zanry.md` | subtraktivní design · dávka 23 |
| published | [Become a Game Dev NECROMANCER!!!](https://www.youtube.com/watch?v=nN5VEvl9fik) `nN5VEvl9fik` | Indie Game Clinic | 16:03 | auto | 3179 | `teorie/zanry.md` | mrtvé žánry (nekromancie) · dávka 23 |

### Level design · `T-LEVEL` (+4)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [Level Design Approaches for Solo Devs](https://www.youtube.com/watch?v=OLXn6YYAk7M) `OLXn6YYAk7M` | Indie Game Clinic | 20:45 | auto | 4162 | `teorie/level-design-solo.md` | přístupy pro sólo vývojáře · dávka 26 |
| published | [Game vs Level Design [explained with Golf and Robots]](https://www.youtube.com/watch?v=R7N1XUKL5JE) `R7N1XUKL5JE` | Indie Game Clinic | 19:40 | auto | 3301 | `teorie/level-design-solo.md` | game design vs. level design · dávka 26 |
| published | [Creating an In-Game Level Editor \| Indie Devlog #9](https://www.youtube.com/watch?v=nAXMHOWliAA) `nAXMHOWliAA` | Game Endeavor | 8:12 | manual | 2063 | `teorie/level-design-solo.md` | devlog in-game editor; tenké — merge kandidát · dávka 26 |
| published | [Environmental Storytelling Explained [Stray, Gone Home, Amnesia, Unpacking, Minit]](https://www.youtube.com/watch?v=sSFs61IF2Rs) `sSFs61IF2Rs` | Indie Game Clinic | 23:06 | auto | 4568 | `teorie/prostor-vypravi.md` | environmental storytelling; cross-link env-breakdowny · dávka 26 |

### Vydání a marketing · `T-MARKET` (+6)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [Game Marketing Advice with Chris Z](https://www.youtube.com/watch?v=O7GoWKwEwIk) `O7GoWKwEwIk` | Indie Game Clinic | 49:07 | auto | 10853 | `teorie/co-prodava.md` | rozšíření: rozhovor Chris Z (49 min) · dávka 26 |
| published | [What Makes a Successful Game?](https://www.youtube.com/watch?v=nO9HMnuZO78) `nO9HMnuZO78` | Indie Game Clinic | 11:23 | auto | 2507 | `teorie/co-prodava.md` | rozšíření: co dělá hru úspěšnou · dávka 26 |
| published | [Roasting Steam Pages with a Marketing Expert](https://www.youtube.com/watch?v=8gY9SU9ShOw) `8gY9SU9ShOw` | Indie Game Clinic | 68:45 | auto | 14515 | `teorie/steam-stranka.md` | rozšíření: roasting s marketérem (69 min) · dávka 26 |
| published | [How To Write Marketing Copy For Your Game](https://www.youtube.com/watch?v=m5X_ZYXVpQE) `m5X_ZYXVpQE` | Indie Game Clinic | 24:59 | auto | 5246 | `teorie/steam-stranka.md` | rozšíření: marketingová copy · dávka 26 |
| published | [What nobody tells you about releasing a game on Steam...](https://www.youtube.com/watch?v=uQnIkK6BOLQ) `uQnIkK6BOLQ` | BiteMe Games | 21:34 | auto | 4874 | `teorie/vydani-hry.md` | co nikdo neřekne o vydání na Steamu · dávka 26 |
| published | [Most Steam Demos Suck; Here's Why](https://www.youtube.com/watch?v=1vtqBTX2Lzc) `1vtqBTX2Lzc` | Indie Game Clinic | 18:35 | auto | 3540 | `teorie/vydani-hry.md` | proč většina dem nefunguje · dávka 26 |

### Byznys, data a kariéra · `T-BIZ` (+6) ⭐ NOVÉ TÉMA _(hotovo — dávka 27)_

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [I Analysed 62,000 Indie Developers. Here's What Actually Predicts Success](https://www.youtube.com/watch?v=WueQ75GP1wc) `WueQ75GP1wc` | Game Oracle | 16:07 | auto | 2660 | `teorie/data-o-uspechu.md` | vývojářů — Extremistan a křivka přežití · dávka 27 |
| published | [I Scraped the Entire Steam Catalog, Here’s the Data](https://www.youtube.com/watch?v=qiNv3qv-YbU) `qiNv3qv-YbU` | Newbie Indie Game Dev | 11:28 | manual | 2101 | `teorie/data-o-uspechu.md` | scrape celého Steam katalogu — metodologie · dávka 27 |
| published | [Ultimate gamedev funding tierlist](https://www.youtube.com/watch?v=qjyPRnzlx8A) `qjyPRnzlx8A` | BiteMe Games | 40:06 | auto | 9139 | `teorie/financovani.md` | tierlist zdrojů financování (40 min) · dávka 27 |
| published | [How To Make Indie Games In 2026 w/ Jonathan Blow — Full Time Game Dev Podcast Ep. 061](https://www.youtube.com/watch?v=yNdRv5LFuQk) `yNdRv5LFuQk` | Thomas Brush | 96:41 | auto | 20137 | `teorie/indie-kariera.md` | podcast Jonathan Blow (97 min) — 3 myšlenky · dávka 27 |
| published | [When is an Indie Game Not an Indie Game?](https://www.youtube.com/watch?v=CyX41iR08Pc) `CyX41iR08Pc` | Indie Game Clinic | 9:58 | auto | 2040 | `teorie/indie-kariera.md` | kdy indie není indie · dávka 27 |
| published | [How BiteMe Games Survived 4 Years Without a Viral Game](https://www.youtube.com/watch?v=KehpqxUfz60) `KehpqxUfz60` | Dev Dream Pod with Blake Gocey | 103:20 | auto | 22461 | `teorie/prezit-jako-studio.md` | podcast BiteMe 4 roky (103 min) — 5 myšlenek · dávka 27 |

### Herní umění a vizuál · `T-ART` (+13) ⭐ NOVÉ TÉMA

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [How we made our Isometric Game Art! ★ \|\| GOLEMBERT Devlog #12](https://www.youtube.com/watch?v=UYBzqCldDDI) `UYBzqCldDDI` | Studio Firlefanz | 9:25 | auto | 1646 | `teorie/2d-vizual.md` | isometrická grafika (devlog); tenké — merge kandidát · dávka 25 |
| published | [So You Wanna Make Games?? \| Episode 10: Game Design](https://www.youtube.com/watch?v=yYYtBFSxoCg) `yYYtBFSxoCg` | Riot Games | 14:50 | manual | 2739 | `teorie/art-pipeline.md` | Riot E10: game design (pro artisty) · dávka 25 · přečištěno 2026-10-11 z ruční `en` (dřív zpětný překlad `en-cs`) |
| published | [So You Wanna Make Games?? \| Episode 2: Concept Art](https://www.youtube.com/watch?v=FqX-UMVTLHI) `FqX-UMVTLHI` | Riot Games | 12:39 | manual | 2069 | `teorie/art-pipeline.md` | Riot E2: concept art · dávka 25 |
| published | [So You Wanna Make Games?? \| Episode 3: Character Art](https://www.youtube.com/watch?v=PfpE5dNTWeI) `PfpE5dNTWeI` | Riot Games | 12:10 | manual | 1969 | `teorie/art-pipeline.md` | Riot E3: character art · dávka 25 |
| published | [So You Wanna Make Games?? \| Episode 5: Technical Art](https://www.youtube.com/watch?v=kr7XYXMM7-U) `kr7XYXMM7-U` | Riot Games | 12:44 | manual | 2089 | `teorie/art-specializace.md` | Riot E5: technical art · dávka 25 · přečištěno 2026-10-11 z ruční `en` (dřív zpětný překlad `en-ro`) |
| published | [So You Wanna Make Games?? \| Episode 4: Environment Art](https://www.youtube.com/watch?v=37LVhP15zGw) `37LVhP15zGw` | Riot Games | 12:54 | manual | 2154 | `teorie/art-pipeline.md` | Riot E4: environment art · dávka 25 · přečištěno 2026-10-11 z ruční `en` (dřív zpětný překlad `en-pl`) |
| published | [So You Wanna Make Games?? \| Episode 6: Character Animation](https://www.youtube.com/watch?v=VmNUAX2V8JQ) `VmNUAX2V8JQ` | Riot Games | 13:11 | manual | 2146 | `teorie/art-specializace.md` | Riot E6: character animation · dávka 25 · přečištěno 2026-10-11 z ruční `en` (dřív zpětný překlad `en-pl`) |
| published | [So You Wanna Make Games?? \| Episode 1: Intro to Game Art](https://www.youtube.com/watch?v=RqRoXLLwJ8g) `RqRoXLLwJ8g` | Riot Games | 11:28 | manual | 1817 | `teorie/art-pipeline.md` | Riot E1: intro to game art · dávka 25 |
| published | [So You Wanna Make Games?? \| Episode 9: User Interface Design](https://www.youtube.com/watch?v=sc3h5JXtIzw) `sc3h5JXtIzw` | Riot Games | 12:29 | manual | 1776 | `teorie/art-specializace.md` | Riot E9: UI design · dávka 25 |
| published | [So You Wanna Make Games?? \| Episode 7: Game VFX](https://www.youtube.com/watch?v=3QKK2o5rWSQ) `3QKK2o5rWSQ` | Riot Games | 11:50 | manual | 1861 | `teorie/art-specializace.md` | Riot E7: game VFX · dávka 25 · přečištěno 2026-10-11 z ruční `en` (dřív zpětný překlad `en-es`) |
| published | [Typography Basics Every Game Dev Should Know](https://www.youtube.com/watch?v=QuNNdPrVMm0) `QuNNdPrVMm0` | Indie Game Clinic | 40:08 | auto | 8060 | `teorie/typografie.md` | typografie pro vývojáře (40 min) · dávka 25 |
| published | [Visual Communication: Why Game Art Matters](https://www.youtube.com/watch?v=SV1BBtD3hY4) `SV1BBtD3hY4` | Indie Game Clinic | 20:49 | manual | 3673 | `teorie/vizualni-komunikace.md` | proč na artu záleží · dávka 25 |
| published | [You Don't Need to Be an Artist to Make Great Game Art](https://www.youtube.com/watch?v=3eg5Lp3pGNk) `3eg5Lp3pGNk` | TechDad Impact | 13:36 | manual | 2665 | `teorie/2d-vizual.md` | nemusíš být umělec · dávka 25 |

### Blueprint architektura a organizace projektu · `P-BP` (+6) _(hotovo — dávka 28)_

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [Why Dependencies are Bad and How To Avoid Them In Unreal Engine \| UE5 Mediator Pattern Explained](https://www.youtube.com/watch?v=y4fE2JdFdvY) `y4fE2JdFdvY` | Ali Elzoheiry | 26:39 | auto | 4490 | `praxe/komunikace-blueprintu.md` | rozšíření: mediator pattern + event manager · dávka 28 |
| published | [Why Use "Interfaces" & "Event Dispatchers" in Unreal Engine \| UE5 Explained](https://www.youtube.com/watch?v=EQfml2D9hwE) `EQfml2D9hwE` | Ali Elzoheiry | 21:54 | auto | 4020 | `praxe/komunikace-blueprintu.md` | rozšíření: interface vs. dispatcher + cena castu · dávka 28 |
| published | [The Most Common Mistake Beginners Make in Unreal Engine \| UE5 Observer Pattern Explained](https://www.youtube.com/watch?v=YFtLd-bKl-U) `YFtLd-bKl-U` | Ali Elzoheiry | 12:17 | auto | 2190 | `praxe/komunikace-blueprintu.md` | rozšíření: observer pattern · dávka 28 |
| published | [The Power of Git in Unreal Engine: a Step-by-Step Guide \| UE5](https://www.youtube.com/watch?v=zf_44hN4Lkg) `zf_44hN4Lkg` | Ali Elzoheiry | 18:48 | auto | 3494 | `praxe/organizace-projektu.md` | rozšíření: Git v UE · dávka 28 |
| published | [Understanding "Components" in Unreal Engine \| UE5 Explained](https://www.youtube.com/watch?v=xo0sbSeWKe4) `xo0sbSeWKe4` | Ali Elzoheiry | 28:11 | auto | 5326 | `praxe/principy-architektury.md` | rozšíření: komponentní vzor · dávka 28 |
| published | [The ultimate guide \| How to Save & Load your unreal engine 5 game \| ue5](https://www.youtube.com/watch?v=H6rqJbwjRIk) `H6rqJbwjRIk` | Ali Elzoheiry | 49:59 | auto | 8148 | `praxe/ukladani.md` | rozšíření: save/load guide (50 min) — 2 myšlenky · dávka 28 |

### AI a chování NPC · `P-AI-NPC` (+2) _(hotovo — dávka 28)_

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [UE5 AI Sight Detection & Chasing With Behaviour Trees!](https://www.youtube.com/watch?v=JF5hIBcycPc) `JF5hIBcycPc` | Matt Aspland | 14:51 | auto | 3191 | `praxe/ai-vnimani.md` | rozšíření: objektový klíč + odklad ztráty cíle · dávka 28 |
| published | [What is Utility AI? \| Smarter AI Design in Unreal Engine 5](https://www.youtube.com/watch?v=LF81fxuQeF8) `LF81fxuQeF8` | D3kryption | 18:40 | auto | 4042 | `praxe/ai-zaklady.md` | rozšíření: Utility AI · dávka 28 |

### Motion Matching a GASP · `P-ANIM` (+1) _(hotovo — dávka 28)_

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [EASY Directional Hit Reactions in Unreal Engine 5 (Using Choosers)](https://www.youtube.com/watch?v=d6icw1-KPwI) `d6icw1-KPwI` | Tank Control Games | 20:48 | auto | 4375 | `praxe/mm-systemy.md` | rozšíření: směrové hit reakce přes choosery · dávka 28 |

### Animace: nástroje a mocap · `P-ANIMTOOLS` (+1) _(hotovo — dávka 28)_

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [New FREE Animation Tool in Unreal Engine 5.8 \| (S.A.M) Solo Animation Mode](https://www.youtube.com/watch?v=-mcMxpVmnAM) `-mcMxpVmnAM` | Proj Prod | 12:42 | auto | 2343 | `praxe/animace-nastroje.md` | rozšíření: SAM (Solo Animation Mode) 5.8 · dávka 28 |

### Pohyb postavy (locomotion) · `P-MOVE` (+1) _(hotovo — dávka 28)_

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [I Created THE LAST OF US PART - 2 Style Wall Detection System \| And It's AMAZING 😎\| UE 5.8](https://www.youtube.com/watch?v=EL4s7sHAFV8) `EL4s7sHAFV8` | Hydra | 12:08 | auto | 1126 | `praxe/pohyb-zaklady.md` | rozšíření: TLOU2 detekce zdi (přesun z parkour-vault) · dávka 28 |

### MetaHuman · `P-MH` (+1) _(hotovo — dávka 28)_

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [UE 5.8 - Any Mesh To MetaHuman - Tutorial](https://www.youtube.com/watch?v=ZmiTuYglaRI) `ZmiTuYglaRI` | Unreal - X - Tutorials | 13:58 | auto | 1714 | `praxe/metahuman.md` | rozšíření: any mesh -> MetaHuman 5.8 · dávka 28 |

### Osvětlení a atmosféra · `P-LIGHT` (+3)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [Understanding Expanse for Unreal Engine \| Complete Beginner Tutorial](https://www.youtube.com/watch?v=rky_GNM0EZs) `rky_GNM0EZs` | SARKAMARI | 23:44 | auto | 3435 | `praxe/osvetleni.md` | rozšíření: Expanse a EVDB objemy · dávka 29 |
| published | [Lighting Hacks Got My Project Featured on Unreal Engine 5 Page 😯 \| Tips & Tricks You Should Know](https://www.youtube.com/watch?v=H2Jfs7nDKh0) `H2Jfs7nDKh0` | Karim Yasser | 15:22 | manual | 2484 | `praxe/osvetleni.md` | rozšíření: malování světlem (protipól PBL) · dávka 29 |
| published | [How I Made My Horror Game Look 10x Better \| DEVLOG](https://www.youtube.com/watch?v=D4n7BeKNOtg) `D4n7BeKNOtg` | AkulDev | 8:30 | auto | 1954 | `praxe/env-tvorba.md` | rozšíření: přestavba kvůli Steam stránce (přesun z osvetleni) · dávka 29 |

### Materiály a VFX · `P-MAT` (+1)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [VFX Texture Creation: The ULTIMATE guide](https://www.youtube.com/watch?v=dMthnzpR-eU) `dMthnzpR-eU` | Le Lu | 28:46 | auto | 4089 | `praxe/materialy.md` | rozšíření: VFX textury (29 min) · dávka 29 |

### Prostředí a environment art · `P-ENV` (+1)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [How Naughty Dog Automates AAA Art (TLOU Part 1)](https://www.youtube.com/watch?v=dqfvgA7oKC4) `dqfvgA7oKC4` | Next Level Game Art | 11:42 | auto | 1922 | `praxe/env-breakdowny.md` | rozšíření: Naughty Dog shadery a Houdini nástroj · dávka 29 |

### Rendering a optimalizace · `P-PERF` (+1)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [Game Dev Secrets: Multithreaded Optimization! #indiegamedev #gamedev](https://www.youtube.com/watch?v=44hfu7ELgVc) `44hfu7ELgVc` | Inbound Shovel | 1:46 | auto | 480 | `praxe/optimalizace.md` | rozšíření: hlavní vlákno a multithreading (short) · dávka 29 |

### AI nástroje ve vývoji · `P-AITOOLS` (+2)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [NVIDIA ARDY: The Real-Time Leap in AI Animation (Open-Source)](https://www.youtube.com/watch?v=xLf27GC0-hE) `xLf27GC0-hE` | Stefan 3D AI | 6:18 | manual | 1158 | `praxe/ai-assety.md` | rozšíření: NVIDIA ARDY — real-time AI animace · dávka 29 |
| published | [Claude And New UE 5.8 MCP is Crazy Good (But I made it better)](https://www.youtube.com/watch?v=I5WLl4MdK28) `I5WLl4MdK28` | Stefan 3D AI | 16:46 | manual | 3263 | `praxe/claude-code-ue.md` | rozšíření: proč nativní MCP samo nestačí + PCG metoda · dávka 29 |

### Editor a workflow · `P-EDITOR` (+3)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [The Best Way To Learn Unreal Engine in 2026!](https://www.youtube.com/watch?v=Nn9F341Vwy0) `Nn9F341Vwy0` | Unreal University | 11:02 | auto | 2295 | `praxe/editor-tipy.md` | rozšíření: pětikroková metoda učení (chunking, rutina) · dávka 29 |
| todo-lp | [Unreal Engine 5 \| Blueprint For Beginners (2026)](https://www.youtube.com/watch?v=c6qW2NP8TP4) `c6qW2NP8TP4` | Smart Poly | 159:31 | manual | 29574 | — | LOW-PRIORITY: beginner kurz 160 min (jako dB-pS8PHALY) |
| todo-lp | [Unreal Engine 5.8 Beginner Tutorial - UE5 Starter Course 2026#unrealengine5  #megascans #cgi](https://www.youtube.com/watch?v=FAo9nfWYPSE) `FAo9nfWYPSE` | Magnet VFX | 88:12 | auto | 11655 | — | LOW-PRIORITY: starter kurz 88 min |

### Tvorba assetů mimo engine (Blender) · `P-ASSET` (+4) ⭐ NOVÉ TÉMA _(hotovo — dávka 30)_

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [Turn Any Photo into a Game Asset (Fast & Easy Blender Tutorial)](https://www.youtube.com/watch?v=ZR_X2OhsteQ) `ZR_X2OhsteQ` | Grant Abbitt (Gabbitt) | 22:21 | auto | 5301 | `praxe/foto-do-assetu.md` | Blender: fotka -> herní asset (2 myšlenky) · dávka 30 |
| published | [How to make PS1 style models in Blender \| Part 1: Textures and UV Mapping \| Tutorial](https://www.youtube.com/watch?v=8--xYWCY_bc) `8--xYWCY_bc` | hacktic | 4:33 | auto | 1005 | `praxe/ps1-estetika.md` | Blender: PS1 modely, textury a UV · dávka 30 |
| published | [How to make PS1 Graphics in 4 minutes](https://www.youtube.com/watch?v=A25NTdPGNaw) `A25NTdPGNaw` | binbun3D | 3:49 | auto | 631 | `praxe/ps1-estetika.md` | PS1 grafika ve 4 minutách (Blender) · dávka 30 |
| published | [Environment in PS1 style. (Blender Timelapse)](https://www.youtube.com/watch?v=d9GUXlnwRGk) `d9GUXlnwRGk` | Summer 85 | 7:03 | — | — | `praxe/ps1-estetika.md` | bez přepisu — timelapse; uveden jako vizuální reference v Pozn. · dávka 30 |

### Hudba a zvuk (rozšíření dokumentu) · `H-EXT` (+3) _(hotovo — dávka 30)_

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [Making an Indie Pop Banger from Scratch w/ Lyncs (Cook Up)](https://www.youtube.com/watch?v=X6RMUest2sw) `X6RMUest2sw` | Splice | 18:58 | auto | 1418 | `hudba/aranz.md` | rozšíření: cook-up Splice — skladba od nuly · dávka 30 |
| published | [The most insane sound design tool nobody's heard of (is free)](https://www.youtube.com/watch?v=TGczsxuAm1I) `TGczsxuAm1I` | mylarmelodies | 14:50 | manual | 2028 | `hudba/nastroje-zdarma-a-game-jam.md` | rozšíření: CDP + SoundThread · dávka 30 |
| published | [How to Make a 3D Sound in Unreal Engine 5](https://www.youtube.com/watch?v=dttUv6--1nA) `dttUv6--1nA` | Gorka Games | 3:43 | auto | 572 | `hudba/sound-design-ve-hre.md` | rozšíření: attenuation v UE · dávka 30 |

---

## Třetí vlna — nové přepisy staženy 2026-07-29

Fetch 2026-07-29 přinesl **174 nových videí** ve třech playlistech: **Godot playlist (93, nový)**, **hlavní playlist (+61)**, **Gamedev-music (+20)**. Archiv `scripts/fetched.txt` má 517 id, `transcripts_clean/` 506 souborů (11 videí bez anglického tracku).

Pořadí práce **dohodnuté s uživatelem**: **nejdřív celý Godot** (nová sekce, taxonomie schválena 2026-07-29), teprve pak zbytek. Tabulky hlavního a hudebního playlistu jsou proto zatím **jen evidence** — bez taxonomie, bez přiřazených kapitol.

---

## Godot playlist — nová sekce „Praxe v Godotu" (93 videí)

Samostatný playlist zaměřený na Godot; zrcadlí roli, kterou má hlavní playlist pro UE5. Nový top-level dokument `docs/godot/` v nav mezi „Praxe v UE5" a „Hudba a zvuk".

**Taxonomie schválena uživatelem 2026-07-29.** Rozložení: **86 videí do Godot sekce** (5 témat / 15 kapitol) · **5 mimo sekci** (routing do Teorie a Hudby) · **1 skip** (duplikát) · **2 low-priority** (mega-kurzy Clear Code, 137k slov dohromady). Celkem ~351k slov přepisů, bez mega-kurzů ~215k.

Dvě rozhodnutí uživatele z tohoto dne: (a) **Inbound Shovel dostává vlastní téma uvnitř Godot sekce**, ne rozpuštění do Teorie — 42 videí jednoho autora se čte jako jeden příběh stavby hry; cena je, že část tématu učí 2D řemeslo, ne Godot API. (b) **Oba Clear Code mega-kurzy zůstávají low-priority**, stejně jako UE beginner kurzy.

Plán dávek: **31 ✅ · 32 ✅ · 33 ✅ · 34 ✅ · 35 ✅ — všechny hotové, Phase 9 uzavřená.**

**Stav: 90/93 published (dávky 31–35).** Sekce „Praxe v Godotu" má **devatenáct kapitol v pěti tématech** a 75 myšlenek. Zbývají už jen **2 low-priority mega-kurzy** (Clear Code, rozhodnutí uživatele 2026-07-29) a **1 skip** (duplikátní re-upload) — tedy nic, co by bylo v hlavním proudu.

Přeřazení proti původnímu návrhu taxonomie (všechna dole v tabulkách poznamenaná): `74y6zWZfQKk` (Bitlytic, „make your code simpler") je o **kompozici vs. dědičnosti**, ne o jazyce → z G-CODE do G-ARCH · `N7UgrLFzW08` (7 coding tips) je **engine-agnostická rada o učení** → mimo sekci, do `teorie/jak-se-ucit-kodovat.md` · `YnfsyZJRsL8` (multiplayer) dostal **vlastní kapitolu s jedinou myšlenkou** místo merge — nikam jinam nepatřil a samostatně je dohledatelný.

### Godot: začínáme · `G-START` (8)

Co Godot je, jak se v něm orientuje a jak z prázdného projektu vznikne hratelná hra.

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [How to make a Video Game - Godot Beginner Tutorial](https://www.youtube.com/watch?v=LOhfqjmasi0) `LOhfqjmasi0` | Brackeys | 77:12 | auto | 14939 | `godot/prvni-hra.md` | páteř kapitoly — 3 myšlenky (kill zone, delta, AnimationPlayer) + export; sponzor přiznán · dávka 31 |
| published | [Godot 4.6 Tips: 7 Features I Wish I Used Sooner](https://www.youtube.com/watch?v=z-9AI9ZPiLM) `z-9AI9ZPiLM` | DeeRaghooGames | 12:38 | auto | 2122 | `godot/zaklady.md` | dědičnost scén + remote inspector + filtry; **Resource, sub-viewport a terén v tilemapách odloženy do dávek 32/33** · dávka 31 |
| published | [Do THIS Before You Publish Your Godot Game](https://www.youtube.com/watch?v=3iGHpha-DmE) `3iGHpha-DmE` | StayAtHomeDev | 3:33 | auto | 658 | `godot/prvni-hra.md` | nastavení projektu před vydáním · dávka 31 |
| published | [Every 2D Node Explained in 9 Minutes !](https://www.youtube.com/watch?v=22VYNOtrcgM) `22VYNOtrcgM` | Lukky | 9:19 | auto | 2150 | `godot/zaklady.md` | mapa 2D nodů — přeskládaná podle řešeného problému · dávka 31 |
| published | [Before You Use Godot 4.6… Watch This (Beginner Guide 2026)](https://www.youtube.com/watch?v=e5imI_IX6ds) `e5imI_IX6ds` | DeeRaghooGames | 9:38 | auto | 1723 | `godot/zaklady.md` | editor 4.6 jako pracovní plocha · dávka 31 |
| published | [Godot Beginner Guide 2026: What I Wish I Knew Before Starting](https://www.youtube.com/watch?v=VwbD5_c7Bq0) `VwbD5_c7Bq0` | DeeRaghooGames | 8:40 | auto | 1465 | `godot/zaklady.md` | sloučeno s DevWorm do myšlenky „co si přinést" · dávka 31 |
| published | [I Wish I Had Known This Before Starting Godot Game Development](https://www.youtube.com/watch?v=TkvRsGstk-w) `TkvRsGstk-w` | DevWorm | 5:54 | auto | 1413 | `godot/zaklady.md` | sloučeno s DeeRaghoo do myšlenky „co si přinést" · dávka 31 |
| published | [Godot in 100 Seconds](https://www.youtube.com/watch?v=QKgTZWbwD1U) `QKgTZWbwD1U` | Fireship | 2:40 | auto | 613 | `godot/zaklady.md` | Godot ve 100 sekundách — rám pro myšlenku „nody a scény" · dávka 31 |

### GDScript a kód · `G-CODE` (7)

Jazyk, typy, návyky — a jeden problém, který vypadá jako bug v kódu, ale je v klávesnici.

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [How to program in Godot - GDScript Tutorial](https://www.youtube.com/watch?v=e1zJS31tr88) `e1zJS31tr88` | Brackeys | 58:09 | manual | 10836 | `godot/gdscript.md` | páteř kapitoly — typování, signály, třídy; sponzor přiznán · dávka 31 |
| published | [Nobody Tells Beginners These 7 Coding Tips \| learn to code in Godot](https://www.youtube.com/watch?v=N7UgrLFzW08) `N7UgrLFzW08` | DeeRaghooGames | 15:50 | auto | 2661 | `teorie/jak-se-ucit-kodovat.md` | **PŘESUN mimo Godot sekci** — engine-agnostická rada o učení; rozšířilo existující kapitolu Teorie · dávka 31 |
| published | [Why Your Godot Code Isn't Actually Broken (Keyboard Ghosting)](https://www.youtube.com/watch?v=qA3dnGGC3ow) `qA3dnGGC3ow` | DeeRaghooGames | 11:21 | auto | 1877 | `godot/gdscript.md` | keyboard ghosting — bug mimo kód · dávka 31 |
| published | [How You Can Easily Make Your Code Simpler in Godot 4](https://www.youtube.com/watch?v=74y6zWZfQKk) `74y6zWZfQKk` | Bitlytic | 6:59 | manual | 1606 | `godot/kompozice.md` | zeď dědičnosti: strom je StaticBody, hráč CharacterBody · dávka 32 |
| published | [Maximize Your Game Development Potential with Classes in Godot (class_name is OP)](https://www.youtube.com/watch?v=y3faMdIb2II) `y3faMdIb2II` | Bitlytic | 4:34 | manual | 1099 | `godot/gdscript.md` | parameter object přes class_name · dávka 31 |
| published | [5 Tricks For Better GDScript in Godot](https://www.youtube.com/watch?v=p_IvmDm-Ywk) `p_IvmDm-Ywk` | StayAtHomeDev | 2:50 | auto | 511 | `godot/gdscript.md` | sloučeno s „1 Easy Habit" do myšlenky o pořádku · dávka 31 |
| published | [1 Easy Habit To Level Up Your Godot Game](https://www.youtube.com/watch?v=Ez6BEiGOMCc) `Ez6BEiGOMCc` | StayAtHomeDev | 2:58 | auto | 549 | `godot/gdscript.md` | sloučeno s „5 Tricks" do myšlenky o pořádku · dávka 31 |

### Architektura projektu · `G-ARCH` (19)

Kompozice, Resource jako data, signály, stavové automaty, struktura projektu a výkon. Největší téma sekce.

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [Mastering Composition for Beginners in Godot](https://www.youtube.com/watch?v=e3H_nw4w5U8) `e3H_nw4w5U8` | Code With Ro | 58:02 | auto | 11914 | `godot/kompozice.md` | páteř kapitoly (58 min) — has-a, test kamene, orchestrátor · dávka 32 |
| published | [Godot Performance Myths Debunked: Does Modular Component Design Actually Slow Down Your Game Part 1](https://www.youtube.com/watch?v=PWHxoAYmyLM) `PWHxoAYmyLM` | DeeRaghooGames | 13:33 | auto | 1939 | `godot/kompozice.md` | benchmark monolit vs. moduly — naměřená tabulka · dávka 32 |
| published | [Using Composition to Make More Scalable Games in Godot](https://www.youtube.com/watch?v=rCu8vQrdDDI) `rCu8vQrdDDI` | Firebelley Games | 10:13 | auto | 2239 | `godot/kompozice.md` | komponenty, které se skládají na sebe + hranice granularity · dávka 32 |
| published | [Stop Using Nodes for Everything in Godot](https://www.youtube.com/watch?v=1PnG3r1rKcs) `1PnG3r1rKcs` | Firebelley Games | 6:10 | manual | 1253 | `godot/kompozice.md` | protipříklad: 115 ms → 8 ms přes RenderingServer · dávka 32 |
| published | [Stop Copying Code! Learn Custom Resources in Godot 4](https://www.youtube.com/watch?v=7dzrc7pEAwE) `7dzrc7pEAwE` | DeeRaghooGames | 13:22 | auto | 2153 | `godot/resources.md` | custom resource od nuly + tři typické chyby · dávka 32 |
| published | [I Rebuilt My Godot Game Using Custom Resources (Here's Why)](https://www.youtube.com/watch?v=uMyxxsMtiOQ) `uMyxxsMtiOQ` | DeeRaghooGames | 12:58 | auto | 2098 | `godot/resources.md` | tatáž hra dvakrát — kdy scéna a kdy data · dávka 32 |
| published | [How to use Resources in Godot 4](https://www.youtube.com/watch?v=h5vpjCDNa-w) `h5vpjCDNa-w` | Bitlytic | 8:07 | manual | 1845 | `godot/resources.md` | past sdílených resourců (duplicate) + dědičnost resourců · dávka 32 |
| published | [Using Resources and Dictionaries for Godot Game Development](https://www.youtube.com/watch?v=D0uGtnMhB-E) `D0uGtnMhB-E` | DevWorm | 6:15 | auto | 1325 | `godot/resources.md` | resource vs. dictionary — rozhodovací pravidlo · dávka 32 |
| published | [Stop Making Messy Games: Godot Rules For Scalable Projects \| Signals PT2](https://www.youtube.com/watch?v=btCeflqFw4o) `btCeflqFw4o` | DeeRaghooGames | 15:10 | auto | 2548 | `godot/signaly.md` | skupiny, event bus, single source of truth · dávka 32 |
| published | [Stop Making Messy Games: Godot Rules For Scalable Projects \| Signals PT1](https://www.youtube.com/watch?v=1rvlexb1fCU) `1rvlexb1fCU` | DeeRaghooGames | 14:20 | auto | 2512 | `godot/signaly.md` | událost vs. příkaz, jména, data v signálu · dávka 32 |
| skip | [Stop Making Messy Games: Godot Rules For Scalable Projects \| Signals PT2 better audio](https://www.youtube.com/watch?v=t6wZiKPJ-g0) `t6wZiKPJ-g0` | DeeRaghooGames | 15:10 | auto | 2553 | — | DUPLIKÁT btCeflqFw4o (re-upload „better audio", týž scénář) |
| published | [Beginner Game Dev? Stop Making Basic Enemies \|\| Build Enemy Systems Instead](https://www.youtube.com/watch?v=QXbgOX5Wl9E) `QXbgOX5Wl9E` | DeeRaghooGames | 16:11 | auto | 2744 | `godot/stavy-a-vzory.md` | přenositelný systém nepřítele (komponenty + FSM + dědičnost scén) · dávka 32 |
| published | [Finite State Machines in Godot 4 in Under 10 Minutes](https://www.youtube.com/watch?v=ow_Lum-Agbs) `ow_Lum-Agbs` | Bitlytic | 7:16 | manual | 1774 | `godot/stavy-a-vzory.md` | FSM od nuly; automat agnostický ke svým stavům · dávka 32 |
| published | [Modular Upgrades Made Easy Using the Strategy Pattern](https://www.youtube.com/watch?v=sZDJJeDNe_M) `sZDJJeDNe_M` | Bitlytic | 6:41 | manual | 1561 | `godot/stavy-a-vzory.md` | strategy pattern jako Resource; autor sám přiznává overkill · dávka 32 |
| published | [10 Things I Wish I Knew Before Starting a Large Godot Project (Cost Me Months)](https://www.youtube.com/watch?v=zLdTvkLsmgA) `zLdTvkLsmgA` | Fat Earth Studios | 15:40 | manual | 2993 | `godot/projekt-a-vykon.md` | záporné měřítko = zabitý projekt; position vs. offset; preload · dávka 32 |
| published | [How to Build Godot Editor Tools Like a Pro](https://www.youtube.com/watch?v=VyTys5oCdN8) `VyTys5oCdN8` | Firebelley Games | 15:13 | auto | 3225 | `godot/projekt-a-vykon.md` | editor scripty; card creation + statistics tool · dávka 32 |
| published | [The Godot Project Setup I Wish I'd Used From the Start](https://www.youtube.com/watch?v=V4SO7foDoW4) `V4SO7foDoW4` | Fat Earth Studios | 13:36 | manual | 2758 | `godot/projekt-a-vykon.md` | vlastnictví napřed, složky potom; process mode past · dávka 32 |
| published | [8 Godot Tips You've Probably Never Heard Of](https://www.youtube.com/watch?v=P8ssMWWQ1R8) `P8ssMWWQ1R8` | Firebelley Games | 13:59 | manual | 2578 | `godot/projekt-a-vykon.md` | profily editoru, self-contained mode, quick open, _has_point · dávka 32 |
| published | [Godot Performance Myths Debunked: Stop Putting Heavy Logic in _process() Godot Performance Part 2](https://www.youtube.com/watch?v=ozEtFPIMWeg) `ozEtFPIMWeg` | DeeRaghooGames | 11:18 | auto | 1653 | `godot/projekt-a-vykon.md` | co skutečně stojí výkon: logika v _process · dávka 32 |
| published | [My game is running at 2 FPS](https://www.youtube.com/watch?v=EA4hDMlhN3o) `EA4hDMlhN3o` | Sealubbers | 1:05 | auto | 283 | `godot/projekt-a-vykon.md` | 2 FPS: frekvence, dávkování, dosah (short) · dávka 32 |

### Systémy a nástroje · `G-SYS` (9)

Konkrétní subsystémy: animace a pohyb, UI, 2D svět, multiplayer.

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [Godot Control Node (UI) Masterclass](https://www.youtube.com/watch?v=5Hog6a0EYa0) `5Hog6a0EYa0` | Karto | 26:25 | auto | 5590 | `godot/ui-control.md` | páteř kapitoly (27 min) — 3 myšlenky: kotvy, kontejnery, témata · dávka 33 |
| published | [How Much Can 2D Lighting Transform a Godot Game?](https://www.youtube.com/watch?v=BXoaRBsmY7o) `BXoaRBsmY7o` | TechDad Impact | 16:26 | manual | 3182 | `godot/2d-svet.md` | tři nody na 2D světlo + kdy stíny nepoužít · dávka 33 |
| published | [How To Pixel Art For Godot](https://www.youtube.com/watch?v=q2bPO4K6r_c) `q2bPO4K6r_c` | Sebbyspoons - Game Dev and Pixel Art | 13:25 | auto | 2458 | `godot/2d-svet.md` | pixel art: paleta, silueta, nearest; autor prodává vlastní balíčky (přiznáno) · dávka 33 |
| published | [Draw fewer tiles - by using a Dual-Grid system!](https://www.youtube.com/watch?v=jEWFSv3ivTg) `jEWFSv3ivTg` | jess::codes | 6:21 | manual | 1185 | `godot/2d-svet.md` | dual-grid: 16 kombinací místo 256; 155 dlaždic místo 507 · dávka 33 |
| published | [Why Animation Trees in Godot 4 are Unbelievably Useful](https://www.youtube.com/watch?v=iElHZhOxGYA) `iElHZhOxGYA` | Bitlytic | 7:28 | manual | 1844 | `godot/animace-a-pohyb.md` | AnimationTree: blend space -> automat -> blend tree; past continuous vs. discrete · dávka 33 |
| published | [I Rebuilt the Default Godot Jump to Feel Amazing](https://www.youtube.com/watch?v=s5XoTDwdjVo) `s5XoTDwdjVo` | Coding Quests | 4:55 | auto | 1033 | `godot/animace-a-pohyb.md` | sedm doplňků výchozího skoku (coyote, buffer, korekce rohu) · dávka 33 |
| published | [Enemy Pathfinding AI in Godot 4](https://www.youtube.com/watch?v=OZCApGqUHGU) `OZCApGqUHGU` | TheYellowDude | 3:06 | auto | 503 | `godot/animace-a-pohyb.md` | navigace ve 2D: region, agent size, bezpečná rychlost · dávka 33 |
| published | [save hours of programming using curves \| Godot Tutorial](https://www.youtube.com/watch?v=cTSrjN_2qDI) `cTSrjN_2qDI` | AceSpectre | 2:49 | auto | 626 | `godot/animace-a-pohyb.md` | Curve resource místo nelineárního vzorce · dávka 33 |
| published | [Godot Multiplayer Tutorial: The Quick and Easy High-Level API](https://www.youtube.com/watch?v=YnfsyZJRsL8) `YnfsyZJRsL8` | IcyEngine | 8:16 | manual | 1587 | `godot/multiplayer.md` | vlastní kapitola s 1 myšlenkou — high-level API a autorita; low-level díl v playlistu není · dávka 33 |

### Případovka: 2D akční platformer · `G-CASE` (42)

Isadora's Edge — jeden projekt od pohybu po vydání, 15 dlouhých devlogů a 26 shortů jednoho autora (+ 1 cizí short o one-way platformách). Rozhodnutí uživatele 2026-07-29: vlastní téma uvnitř Godot sekce, ne rozpuštění do Teorie.

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [Perfecting MOVEMENT for my Indie Game \| Devlog](https://www.youtube.com/watch?v=EQxcdftp_eQ) `EQxcdftp_eQ` | Inbound Shovel | 18:53 | auto | 4348 | `godot/pripadovka-pohyb.md` | rozdělení vstup/provedení; dash jako důkaz; animace jako ladicí nástroj; dilema útoku v pohybu · dávka 34 |
| published | [Why Slopes are Shockingly Difficult for Indie Game Devs](https://www.youtube.com/watch?v=rHMJccb5IOM) `rHMJccb5IOM` | Inbound Shovel | 17:20 | auto | 4233 | `godot/pripadovka-pohyb.md` | proč vyhodil šikmé plochy: fyzika, výtvarno, level design · dávka 34 |
| published | [Game Dev Secrets: Why am I so heavy? #indiegamedev #gamedev](https://www.youtube.com/watch?v=ZSD2EOBEWlU) `ZSD2EOBEWlU` | Inbound Shovel | 0:52 | auto | 271 | `godot/pripadovka-pohyb.md` | hromadící se gravitace — bug bez symptomu v místě příčiny (short) · dávka 34 |
| published | [Game Dev Secret: REAL control over your character? #indiegamedev #gamedev](https://www.youtube.com/watch?v=jd91r5kwdnc) `jd91r5kwdnc` | Inbound Shovel | 0:45 | auto | 212 | `godot/pripadovka-pohyb.md` | jump cutting (short) · dávka 34 |
| published | [Game Dev Secrets: How to make your Aerial Attacks feel SUPER smooth! #indiegamedev #gamedev](https://www.youtube.com/watch?v=kYPMIfROc_A) `kYPMIfROc_A` | Inbound Shovel | 0:59 | auto | 269 | `godot/pripadovka-pohyb.md` | oddělený smear → animation canceling (short) · dávka 34 |
| published | [How passable (one-way) platforms work in game development!](https://www.youtube.com/watch?v=CZgJgrndt5Q) `CZgJgrndt5Q` | Challacade | 0:59 | auto | 252 | `godot/pripadovka-pohyb.md` | jednosměrné plošiny (Challacade — jediné cizí video v případovce) · dávka 34 |
| published | [I made the PERFECT camera for my Indie Game! \| Devlog](https://www.youtube.com/watch?v=80VlawJmDiE) `80VlawJmDiE` | Inbound Shovel | 23:08 | auto | 5550 | `godot/pripadovka-kamera.md` | páteř kapitoly — 4 pojmenované vady, lasagna kamera, test, který lhal · dávka 34 |
| published | [Game Dev Secrets: Oops, we broke the camera #indiegamedev #gamedev](https://www.youtube.com/watch?v=KTOyrG2rfCU) `KTOyrG2rfCU` | Inbound Shovel | 1:15 | auto | 371 | `godot/pripadovka-kamera.md` | look ahead: vyhlazení kamery ruší důvod, proč sleduje (short) · dávka 34 |
| published | [Game Dev Secrets: Resolution! #indiegamedev #gamedev](https://www.youtube.com/watch?v=y_TwL5IfPxA) `y_TwL5IfPxA` | Inbound Shovel | 1:00 | auto | 264 | `godot/pripadovka-kamera.md` | rozlišení 640x360 a proč ne 480x270 (short) · dávka 34 |
| published | [I made a Fighting Game Frame Data System for my Indie Game!](https://www.youtube.com/watch?v=Dptztdm1rtg) `Dptztdm1rtg` | Inbound Shovel | 31:42 | auto | 8468 | `godot/pripadovka-nepratele.md` | frame data — požadavky definované předem, SSOT, tool script s tlačítky · dávka 34 |
| published | [Making a BIG BOSS FROG for my indie game! \| Devlog](https://www.youtube.com/watch?v=atqSho7wmGE) `atqSho7wmGE` | Inbound Shovel | 25:57 | auto | 6456 | `godot/pripadovka-nepratele.md` | boss: kontrast, tell přes barevný obdélník, vážený výběr se sestupnou pravděpodobností · dávka 34 |
| published | [Making Flying Enemies for my Indie Game! (Isadora's Edge Devlog)](https://www.youtube.com/watch?v=bGET0eZIo9w) `bGET0eZIo9w` | Inbound Shovel | 18:49 | auto | 4751 | `godot/pripadovka-nepratele.md` | létající nepřátelé ve 3 verzích, donut místo bodu; eskalace abstrakce; sponzor přiznán · dávka 34 |
| published | [Creating SMART Enemies for my Indie Game! \| Devlog](https://www.youtube.com/watch?v=4yqg1UEkiZo) `4yqg1UEkiZo` | Inbound Shovel | 18:29 | auto | 4404 | `godot/pripadovka-nepratele.md` | tři patra AI + interruptible stavy; autor přiznává, že se s tím špatně pracuje · dávka 34 |
| published | [Game Dev Secrets: About Combo Attacks #indiegamedev #gamedev](https://www.youtube.com/watch?v=GbSTBAI6dJc) `GbSTBAI6dJc` | Inbound Shovel | 0:56 | auto | 291 | `godot/pripadovka-nepratele.md` | combo přes dva překrývající se časovače (short) · dávka 34 |
| published | [Game Dev Secrets: Stealing from Fighting Games! #indiegamedev #gamedev](https://www.youtube.com/watch?v=JAW6Zn3rMBk) `JAW6Zn3rMBk` | Inbound Shovel | 0:58 | auto | 256 | `godot/pripadovka-nepratele.md` | hit stop s konkrétními hodnotami 1/20-1/4 s (short) · dávka 34 |
| published | [I made a Custom Level Editor for my Indie Game!](https://www.youtube.com/watch?v=wQwHKKzKQL4) `wQwHKKzKQL4` | Inbound Shovel | 19:08 | auto | 4954 | `godot/pripadovka-level-a-mapa.md` | místnost jako parametrizovaný celek + level editor, který nebyl level editor; sponzor přiznán · dávka 35 |
| published | [Making a Massive Metroidvania Map (The Right Way)](https://www.youtube.com/watch?v=FI0-yz5Xcz0) `FI0-yz5Xcz0` | Inbound Shovel | 17:38 | auto | 4340 | `godot/pripadovka-level-a-mapa.md` | mapa metroidvanie: data vs. pohled, brute-force test 300 místností; sponzor přiznán · dávka 35 |
| published | [Game Dev Secrets: Tiles and Maps! #indiegamedev #gamedev](https://www.youtube.com/watch?v=1j_B8Ra3TY4) `1j_B8Ra3TY4` | Inbound Shovel | 0:59 | auto | 308 | `godot/2d-svet.md` | auto-tiling jako pravidla sousedství — doplněno k dual-gridu jako křížový odkaz · dávka 35 |
| published | [Game Dev Secrets: Maps and Transitions! #indiegamedev #gamedev](https://www.youtube.com/watch?v=zG4ShItsV_Q) `zG4ShItsV_Q` | Inbound Shovel | 1:36 | auto | 414 | `godot/pripadovka-level-a-mapa.md` | dveře definované dvakrát = SSOT (short) · dávka 35 |
| published | [Game Dev Secrets: Loading Zone Trick! #indiegamedev #gamedev](https://www.youtube.com/watch?v=EP-fIhAe2Jo) `EP-fIhAe2Jo` | Inbound Shovel | 1:27 | auto | 404 | `godot/pripadovka-level-a-mapa.md` | persistence key (short) · dávka 35 |
| published | [Game Dev Secrets: A trick for environmental immersion! #indiegamedev #gamedev](https://www.youtube.com/watch?v=ok4Zst3R7aQ) `ok4Zst3R7aQ` | Inbound Shovel | 0:57 | auto | 260 | `godot/pripadovka-level-a-mapa.md` | parallax a vnímaná velikost (short) · dávka 35 |
| published | [Lighting VFX Completely Changed my Game!](https://www.youtube.com/watch?v=TS0hP7wX-zI) `TS0hP7wX-zI` | Inbound Shovel | 16:02 | auto | 3926 | `godot/pripadovka-vizual-a-zvuk.md` | 4 nepovedené pokusy o glow + normal mapy; chyba byla v měřítku vzorkování · dávka 35 |
| published | [Redesigning the Main Character of my Indie Game! \| Devlog](https://www.youtube.com/watch?v=HsWnv6rCiJ4) `HsWnv6rCiJ4` | Inbound Shovel | 24:29 | auto | 5814 | `godot/pripadovka-vizual-a-zvuk.md` | redesign postavy (silueta) — video dělené do 3 kapitol: vizuál, systémy (upgrady), proces (Git, profiling) · dávka 35 |
| published | [Game Dev Secrets: The Key to Colors! #indiegamedev #gamedev](https://www.youtube.com/watch?v=x8EGyYUELUw) `x8EGyYUELUw` | Inbound Shovel | 1:33 | auto | 439 | `godot/pripadovka-vizual-a-zvuk.md` | hue shifting (short) · dávka 35 |
| published | [Game Dev Secrets: Palette Swaps! #indiegamedev #gamedev](https://www.youtube.com/watch?v=7joIPGLcWHY) `7joIPGLcWHY` | Inbound Shovel | 0:59 | auto | 303 | `godot/pripadovka-vizual-a-zvuk.md` | palette swap přes shader (short) · dávka 35 |
| published | [Game Dev Secrets: Sound Effect Magic! #indiegamedev #gamedev](https://www.youtube.com/watch?v=ZYZRr05AMNE) `ZYZRr05AMNE` | Inbound Shovel | 1:00 | auto | 279 | `godot/pripadovka-vizual-a-zvuk.md` | náhodný posun výšky tónu 90-110 % (short) · dávka 35 |
| published | [Creating a Game-Changing Badge System for my Indie Game! \| Devlog](https://www.youtube.com/watch?v=KtbNdDWi30k) `KtbNdDWi30k` | Inbound Shovel | 37:10 | auto | 9437 | `godot/pripadovka-systemy.md` | odznaky: odměna, která nezlehčí hru + rychlé ladění jako designový nástroj (37 min) · dávka 35 |
| published | [Game Dev Secrets: How to handle Rewards? #indiegamedev #gamedev](https://www.youtube.com/watch?v=tgczIVACFXI) `tgczIVACFXI` | Inbound Shovel | 1:04 | auto | 275 | `godot/pripadovka-systemy.md` | odměny bez posílení: lore, kosmetika, další výzvy (short) · dávka 35 |
| published | [Game Dev Secrets: Risks and Rewards! #indiegamedev #gamedev](https://www.youtube.com/watch?v=pwUKx1WDsm0) `pwUKx1WDsm0` | Inbound Shovel | 1:01 | auto | 269 | `godot/pripadovka-systemy.md` | regenerace života vyrobila pasivitu — pobídky (short) · dávka 35 |
| published | [Game Dev Secrets: NUMBER GO UP #indiegamedev #gamedev](https://www.youtube.com/watch?v=kaRyRRHF-5o) `kaRyRRHF-5o` | Inbound Shovel | 2:04 | auto | 506 | `godot/pripadovka-systemy.md` | nepřesnost floatů daleko od počátku (short) · dávka 35 |
| published | [Game Dev Secrets: Becoming a Billionaire? #indiegamedev #gamedev](https://www.youtube.com/watch?v=NZSJ7n2Ix0A) `NZSJ7n2Ix0A` | Inbound Shovel | 1:55 | auto | 508 | `godot/pripadovka-systemy.md` | integer overflow (short) · dávka 35 |
| published | [Game Dev Secrets: An Easy Dialogue Fix! #indiegamedev #gamedev](https://www.youtube.com/watch?v=b_4pEe4chfs) `b_4pEe4chfs` | Inbound Shovel | 1:16 | auto | 347 | `godot/pripadovka-systemy.md` | psací stroj přes neviditelné znaky, ne přidávání (short) · dávka 35 |
| published | [Game Dev Secrets: Keybindings? #indiegamedev #gamedev](https://www.youtube.com/watch?v=b9pl67ZbhX8) `b9pl67ZbhX8` | Inbound Shovel | 1:15 | auto | 335 | `godot/pripadovka-systemy.md` | soubor preferencí vs. save; argument speedrunnerů (short) · dávka 35 |
| published | [The Dangers of Taking Shortcuts (as a Game Dev)](https://www.youtube.com/watch?v=qkefNtAPjUE) `qkefNtAPjUE` | Inbound Shovel | 20:19 | auto | 5387 | `godot/pripadovka-proces.md` | sto projektilů bez systému — tři náklady technického dluhu · dávka 35 |
| published | [Man, making a video game is hard \| Devlog](https://www.youtube.com/watch?v=6v_gu8vbeQQ) `6v_gu8vbeQQ` | Inbound Shovel | 14:31 | auto | 3354 | `godot/pripadovka-proces.md` | neviditelná práce, demoralizace, Git po roce · dávka 35 |
| published | [After 3 Years, I'm Changing My Indie Game's Genre!](https://www.youtube.com/watch?v=R_bX6FeEUFw) `R_bX6FeEUFw` | Inbound Shovel | 15:15 | auto | 3825 | `godot/pripadovka-proces.md` | změna žánru po 3 letech; spirála nechuti; sponzor přiznán · dávka 35 |
| published | [Game Dev Secrets: Increase your FPS by ten thousand percent! #indiegamedev #gamedev](https://www.youtube.com/watch?v=8_5Zrgek1p8) `8_5Zrgek1p8` | Inbound Shovel | 1:00 | auto | 287 | `godot/pripadovka-proces.md` | time slicing (short) · dávka 35 |
| published | [Game Dev Secrets: Async/Await/Ahelpme #indiegamedev #gamedev](https://www.youtube.com/watch?v=cuvW_dg9Y7c) `cuvW_dg9Y7c` | Inbound Shovel | 1:14 | auto | 301 | `godot/pripadovka-proces.md` | async není multithreading (short) · dávka 35 |
| published | [Game Dev Secrets: How to Playtest! #indiegamedev #gamedev](https://www.youtube.com/watch?v=TPEn3Ur__sQ) `TPEn3Ur__sQ` | Inbound Shovel | 1:35 | auto | 413 | `godot/pripadovka-proces.md` | playtester popsal řešení, ne problém (short) · dávka 35 |
| published | [Game Dev Secrets: It's definitely not built to scale... #indiegamedev #gamedev](https://www.youtube.com/watch?v=4_v6vw7DFus) `4_v6vw7DFus` | Inbound Shovel | 1:21 | auto | 399 | `godot/pripadovka-vizual-a-zvuk.md` | velikost plátna relativně k postavě (short) · dávka 35 |
| published | [Game Dev Secrets: The Most Common Beginner Mistake! #indiegamedev #gamedev](https://www.youtube.com/watch?v=OQzApE2FXmI) `OQzApE2FXmI` | Inbound Shovel | 0:58 | auto | 289 | `godot/pripadovka-vizual-a-zvuk.md` | mixely (short) · dávka 35 |
| published | [Game Dev Secrets: Stress? #indiegamedev #gamedev](https://www.youtube.com/watch?v=1E5b-fOhfzc) `1E5b-fOhfzc` | Inbound Shovel | 1:01 | auto | 275 | `godot/pripadovka-proces.md` | squeeze and release (short) · dávka 35 |

### Mimo Godot sekci — routing do stávajících dokumentů (5)

Videa z playlistu, která s Godotem nemají nic společného; míří do existujících kapitol Teorie a Hudby.

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [Why Does Celeste Feel So Good to Play?](https://www.youtube.com/watch?v=yorTG9at90g) `yorTG9at90g` | Game Maker's Toolkit | 17:33 | manual | 3145 | `teorie/game-feel.md` | MIMO SEKCI — Celeste: křivky v snímcích a tiché úlevy · dávka 33 |
| published | [Small games win big, here's how to make them](https://www.youtube.com/watch?v=8Kr5TruT-YU) `8Kr5TruT-YU` | BiteMe Games | 14:59 | auto | 3608 | `teorie/scope.md` | MIMO SEKCI — jak se malá hra doopravdy dělá (staged disagreement s rd1HzPy3fP4) · dávka 33 |
| published | [Beginner Game Dev? Don’t Make Small Games \|\| Do This Instead](https://www.youtube.com/watch?v=rd1HzPy3fP4) `rd1HzPy3fP4` | DeeRaghooGames | 7:47 | auto | 1342 | `teorie/scope.md` | MIMO SEKCI — nedělej malé hry, dělej systémy (protiteze k 8Kr5TruT-YU) · dávka 33 |
| published | [The Tools I Use For Full Time Indie Game Development](https://www.youtube.com/watch?v=mrVM2zehqiw) `mrVM2zehqiw` | Firebelley Games | 12:09 | manual | 2471 | `teorie/planovani-nastroje.md` | MIMO SEKCI — nástroje full-time indie vývojáře; placený segment přiznán · dávka 33 |
| published | [10 Chord Patterns for 10 Different Emotions](https://www.youtube.com/watch?v=_yw85rAb6cw) `_yw85rAb6cw` | Alex Rome | 13:19 | auto | 1756 | hudba/akordy-a-harmonie.md | odložený z Godot playlistu — 10 progresí, sloučeno s cU4mqDPZuXg do jednoho katalogu |

### Low-priority · mega-kurzy (2)

Rozhodnutí uživatele 2026-07-29: oba zůstávají `todo-lp` mimo hlavní proud — follow-along formát se špatně destiluje a obsahově se překrývá se zbytkem playlistu.

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| todo-lp | [The new ultimate introduction to Godot](https://www.youtube.com/watch?v=TLG2yVpLDT8) `TLG2yVpLDT8` | Clear Code | 536:40 | auto | 87112 | — | LOW-PRIORITY: kompletní úvod do Godotu, 8,9 h / 87k slov (rozhodnutí 2026-07-29) |
| todo-lp | [Recreate Stardew Valley in Godot & and master advanced Godot concepts](https://www.youtube.com/watch?v=jIKuiUdCsuo) `jIKuiUdCsuo` | Clear Code | 311:30 | auto | 49611 | — | LOW-PRIORITY: Stardew Valley v Godotu, 5,2 h / 50k slov (rozhodnutí 2026-07-29) |


---

### Hlavní playlist · třetí vlna (+61) · `todo`

Celkem ~297k slov. Dominantní shluk na první pohled: **výkon, profiling a optimalizace v UE5** (~35 videí — 13× Unreal Fest / Inside Unreal, Tom Looman, Dallas Drapeau ×3, Threat Interactive, SimonDev, Smart Poly ×2, Matt Aspland ×2 a další). To je materiál na samostatné téma, ne na rozšíření stávající kapitoly `praxe/optimalizace.md`. Druhý shluk je **design a teorie** (5 Principles, GDD, worldbuilding, engagement bez temných vzorů, architektury kódu podle Tyrollera), třetí je **UE praxe** (Ali Elzoheiry inventory 2 díly, animace, 5.8 preview).

**Plán bloku „Výkon a profiling"** (nové téma v Praxi v UE5, ~36 videí / ~200k unikátních slov po odečtu překryvů), rozdělený do pěti dávek:

| dávka | kapitola | stav |
|---|---|---|
| 36 | `praxe/profiling.md` — měření místo odhadů | ✅ hotovo |
| 37 | `praxe/rozpocet-snimku.md` + `praxe/frame-pacing.md` — rozpočet, potrubí a latence | ✅ hotovo |
| 38 | `praxe/nanite-do-hloubky.md` + `praxe/gpu-pamet.md` + `praxe/gpu-pruchod.md` (+1 myšlenka do `osvetleni.md`) | ✅ hotovo |
| 39 | `praxe/niagara-vykon.md` + `praxe/pamet-a-instance.md` + `praxe/lehky-render.md` | ✅ hotovo |
| 40 | `praxe/velke-svety.md` + `praxe/persistence-a-hydratace.md` + `praxe/mereni-automaticky.md` | ✅ hotovo — **blok uzavřen** |

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [Build a Scalable Inventory System \| Part 2: Item Definition \| Unreal Engine 5 Tutorial](https://www.youtube.com/watch?v=8ylTGxeMR7w) `8ylTGxeMR7w` | Ali Elzoheiry | 44:28 | auto | 7722 | `praxe/principy-architektury.md` | +2: třída jako data (CDO) · fragmenty jako kompozice; vzor z Lyry |
| published | [Build a Scalable Inventory System \| Part 1: The Foundation \| Unreal Engine 5 Tutorial](https://www.youtube.com/watch?v=eocJvH15L4Q) `eocJvH15L4Q` | Ali Elzoheiry | 22:31 | auto | 3972 | `praxe/principy-architektury.md` | část 1 (naivní verze a proč selže) — vstup do myšlenky „třída jako data" |
| published | [5 Tips for Great Level Design](https://www.youtube.com/watch?v=LBtucVc8l0M) `LBtucVc8l0M` | Apox Fox | 12:33 | auto | 2727 | `teorie/level-design-solo.md` | +1 myšlenka: pět principů; nejcennější je „tvoje hra je jazyk" |
| published | [Animation Process (EMP Spike) - Dev Diary](https://www.youtube.com/watch?v=Lo0569JZTSU) `Lo0569JZTSU` | chaotic works | 7:00 | auto | 1195 | `praxe/animace-nastroje.md` | +1: řemeslo první osoby — křivky, protipohyb kamery, past 30 → 60 snímků |
| published | [UE5 Optimization Made Easy: Fundamentals](https://www.youtube.com/watch?v=zVNViTNHHdA) `zVNViTNHHdA` | Dallas Drapeau | 36:27 | auto | 6425 | `praxe/rozpocet-snimku.md` | cílový framerate jako designové rozhodnutí + legenda k optimalizačním view modes |
| published | [UE5: Profilers Explained](https://www.youtube.com/watch?v=tuAtGaVqcSM) `tuAtGaVqcSM` | Dallas Drapeau | 35:52 | auto | 6354 | `praxe/profiling.md` | slovníček položek GPU profileru + kalibrace očekávání (Epic/High = 30/60 FPS) |
| published | [The “Unreal Engine Look” Explained — And How to Fix It](https://www.youtube.com/watch?v=ciCRiQmwTrs) `ciCRiQmwTrs` | Dallas Drapeau | 23:31 | auto | 4045 | `praxe/osvetleni.md` | REASSIGN: není výkon, ale vzhled — ACES vs. AGX jako 8. myšlenka Osvětlení |
| published | [How to Learn Coding FAST And Make Cool Stuff](https://www.youtube.com/watch?v=nCZbZyyuHRg) `nCZbZyyuHRg` | Eray Sona | 4:18 | auto | 864 | `teorie/jak-se-ucit-kodovat.md` | součást téže myšlenky: projekt hned po konceptu, AI jako doučující ne berla |
| published | [5 Principles of Game Design](https://www.youtube.com/watch?v=pF2LGYVRCwI) `pF2LGYVRCwI` | Field of View: The Art of Game Design | 39:47 | manual | 7030 | `teorie/zaklady.md` | +1 myšlenka: „pěst je silnější než pět prstů" — soudržnost, struktura vs. svoboda, sladění s rozpoložením hráče |
| published | [Nanite Forest Optimisation in Unreal Engine 5](https://www.youtube.com/watch?v=uE4cGZjMfuY) `uE4cGZjMfuY` | Filgeck | 21:06 | auto | 3210 | `praxe/gpu-pruchod.md` | les 30 → 60 FPS na 8GB kartě, včetně negativního nálezu |
| published | [7 Programming myths that waste your time](https://www.youtube.com/watch?v=niWpfRyvs2U) `niWpfRyvs2U` | Fireship | 6:17 | auto | 1412 | `teorie/programatorske-navyky.md` | +1: devět mýtů, které žerou čas; RUG místo DRY |
| published | [The Design Principle That Separates Good Games From Great Ones](https://www.youtube.com/watch?v=uuc6DRe4U4Q) `uuc6DRe4U4Q` | Game Design Library | 11:37 | auto | 2322 | `teorie/ludonarativni-soulad.md` | +1 myšlenka: kontext — metoda „strhni rámec a podívej se, co zbylo" |
| published | [How to write a Game Design Document](https://www.youtube.com/watch?v=bro4rwYVo0I) `bro4rwYVo0I` | Game Dev Beginner | 12:23 | manual | 2296 | `teorie/gdd.md` | +1 myšlenka: jedna stránka, formát rozhoduje (domovní plánek) |
| published | [How to Keep Players Engaged (Without Being Evil)](https://www.youtube.com/watch?v=hbzGO_Qonu0) `hbzGO_Qonu0` | Game Maker's Toolkit | 10:46 | manual | 2038 | `teorie/zaklady.md` | +1 myšlenka: poutavost proti návykovosti — pacing, naznačené novinky, dlouhodobý cíl · přečištěno 2026-10-11 z ruční `en` (dřív zpětný překlad `en-de`) |
| published | [How to Analyze your Level Performance in Unreal Engine 5 - Profiler Tutorial](https://www.youtube.com/watch?v=HOcXWZY044E) `HOcXWZY044E` | Gorka Games | 3:30 | auto | 727 | `praxe/profiling.md` | doplněk k GPU profileru (barevný pruh, limit vůči blueprintům) |
| published | [Game Dev Secrets: About Steam #indiegamedev #gamedev](https://www.youtube.com/watch?v=48_qqfGk6wY) `48_qqfGk6wY` | Inbound Shovel | 1:00 | auto | 330 | `teorie/steam-stranka.md` | doplněk stávající myšlenky: key art ve vrstvách pro všechny formáty; 7–12k wishlistů |
| published | [Best Code Architectures For Indie Games](https://www.youtube.com/watch?v=8WqYQ1OwxJ4) `8WqYQ1OwxJ4` | Jonas Tyroller | 16:10 | auto | 3141 | `praxe/principy-architektury.md` | +1: znovupoužitelné kostky a lepidlo 70/30, špagety na talíři, čas jako nevyhnutelná špageta |
| published | [I Made Game Animation in minutes inside unreal engine 5.8](https://www.youtube.com/watch?v=stc0_aMvkPQ) `stc0_aMvkPQ` | Just An Animator | 8:27 | manual | 945 | `praxe/animace-nastroje.md` | DUPLIKÁT: markerless mocap v 5.8 už pokryt ze tří zdrojů a podrobněji |
| published | [The Seven Levels of Worldbuilding](https://www.youtube.com/watch?v=vFMnz75y5y4) `vFMnz75y5y4` | Large Lads Studios | 29:29 | auto | 5196 | `teorie/pribeh-a-postavy.md` | +1 myšlenka: sedm pater worldbuildingu — šířka není hloubka |
| published | [900+ hours of Learning System Design in 9 Minutes](https://www.youtube.com/watch?v=3Pusamd6BO4) `3Pusamd6BO4` | Maddy Zhang | 9:42 | auto | 1914 | `teorie/programatorske-mysleni.md` | +1: šest pojmů z návrhu systémů; tři z nich mají přímý gamedev protějšek |
| published | [How To Optimise Memory Usage In Your Unreal Engine 5 Game](https://www.youtube.com/watch?v=JWDnTDi_aLY) `JWDnTDi_aLY` | Matt Aspland | 10:02 | auto | 2176 | `praxe/pamet-a-instance.md` | Size Map v režimu paměti: cast na hráče = 111 MB, interface + Get Player Character = 1,7 MB |
| published | [How To Create AI Random Roam in Unreal Engine 5 Using Behaviour Trees (Tutorial)](https://www.youtube.com/watch?v=aUaBtau2M3c) `aUaBtau2M3c` | Matt Aspland | 6:43 | auto | 1439 | `praxe/ai-zaklady.md` | DUPLIKÁT: náhodné bloumání už pokrývá „Patrola dvěma způsoby" (blueprint verze) + „Vyšší liga" (behavior trees) |
| published | [I Reduced My UE5 Game Size By 70% #unrealengine #indiedev #gamedev](https://www.youtube.com/watch?v=qlPqwTAmQ5E) `qlPqwTAmQ5E` | Matt Aspland | 0:25 | auto | 127 | `praxe/pamet-a-instance.md` | do „drobků": čtyři nastavení packagingu, balíček o 70 % menší |
| published | [Triple Your FPS With These 5 Lighting Optimization Tips for Unreal Engine 5](https://www.youtube.com/watch?v=MLS96wgSMk4) `MLS96wgSMk4` | MelvinTang Games | 7:17 | auto | 1200 | `praxe/pamet-a-instance.md` | do „drobků": mobilita světel, draw distance + fade, MegaLights 19 → 60 FPS |
| published | [3 Years Working on AAA Games ... Here's What Nobody Tells You](https://www.youtube.com/watch?v=HECL-9qPlxM) `HECL-9qPlxM` | Next Level Game Art | 18:07 | auto | 3534 | `teorie/indie-kariera.md` | +1: tři roky v AAA — měkké dovednosti nad prahem tvrdých, 130–140 přihlášek na 1 nabídku |
| published | [Why Every Developer Needs to Understand CI/CD](https://www.youtube.com/watch?v=omB2JkC4QfA) `omB2JkC4QfA` | Nova Designs | 13:42 | auto | 2574 | `teorie/programatorske-navyky.md` | +1: CI/CD jako automatizovaný kontrolní seznam; myčka aut |
| published | [What's Causing my Frame Rate to Drop? - Unreal Engine 5 Stat Profiling Tutorial](https://www.youtube.com/watch?v=nQdsY2a-Fn8) `nQdsY2a-Fn8` | NumenBrothers | 6:09 | auto | 1373 | `praxe/profiling.md` | případovka k rozhodovacímu stromu: `stat` → Session Frontend → viník ve foliage |
| published | [How To Improve Performance - Unreal Engine 5 Tutorial](https://www.youtube.com/watch?v=S-vO9YNI7zs) `S-vO9YNI7zs` | Pitchfork Academy | 27:26 | auto | 5173 | `praxe/lehky-render.md` | rozpad ceny výchozí scény + náhrady; screen percentage; nepotvrzená hypotéza o VSM |
| published | [Optimization UE5 - The Power of Instanced Static Meshes with Efficient Materials](https://www.youtube.com/watch?v=S7lJnSeL41M) `S7lJnSeL41M` | PolySphere 3D | 5:35 | manual | 838 | `praxe/pamet-a-instance.md` | ISM + materiálová variace (per-instance custom data, náhoda z pozice instance) |
| published | [How I Beat 99% of Computer Science Students (Georgia Tech Lessons)](https://www.youtube.com/watch?v=oJ6LN7t0Vr8) `oJ6LN7t0Vr8` | Sajjaad Khader | 12:04 | auto | 2606 | `teorie/jak-se-ucit-kodovat.md` | +1 (spolu s `nCZbZyyuHRg`): rychlostní daň, pit crew, „přestaň být student" |
| published | [Unreal Engine 5.8 Preview: What Epic Games Changed Under The Hood \| New Features & Updates](https://www.youtube.com/watch?v=NfDzhmXiUNA) `NfDzhmXiUNA` | Sergey Maryshev | 4:56 | manual | 856 | `praxe/editor-tipy.md` | +1: co se změnilo v editoru 5.8 (Parent Space, CAD výběr, Lumen na Medium) |
| published | [How to Quickly Optimize Your Scene in Unreal Engine 5 Using ISM/HISM](https://www.youtube.com/watch?v=lZegK5ussdU) `lZegK5ussdU` | Sergey Maryshev | 3:16 | auto | 623 | `praxe/pamet-a-instance.md` | ISM vs. HISM vs. merge actors; past se sloučenými stromy za budovami; Nanite ISM nepotřebuje |
| published | [Unreal Engine 5 Level Design Workflow Trick](https://www.youtube.com/watch?v=4itMlAQC3LE) `4itMlAQC3LE` | Sergey Maryshev | 0:29 | manual | 99 | `praxe/editor-tipy.md` | z velké části duplikát už zpracovaného triku — převzaty jen klávesové zkratky do stávající myšlenky · přečištěno 2026-10-11 z ruční `en-US` (dřív zpětný překlad `en-pl`) |
| published | [When Optimisations Work, But for the Wrong Reasons](https://www.youtube.com/watch?v=hf27qsQPRLQ) `hf27qsQPRLQ` | SimonDev | 22:18 | manual | 4049 | `praxe/rozpocet-snimku.md` | 2×2 quad, quad utilization, primitive assembly — proč LODy a Nanite fungují |
| published | [How To Create An Optimized UE5 Base Project](https://www.youtube.com/watch?v=2ZcagAT3EXQ) `2ZcagAT3EXQ` | Smart Poly | 16:50 | auto | 3331 | `praxe/lehky-render.md` | vlastní šablona enginu, start ve 4.27 jako obchvat; nastavení se přesto částečně resetují |
| published | [The Most Optimized Version of UE5??? (The ViteFork)](https://www.youtube.com/watch?v=dRR5AC8PV2U) `dRR5AC8PV2U` | Smart Poly | 13:30 | auto | 2631 | `praxe/lehky-render.md` | komunitní fork (NvRTX 5.0.3, DDGI) jako krajní varianta — orientace, ne doporučení |
| published | [Introduction and setup of Unreal Engine 5 memory insights](https://www.youtube.com/watch?v=qGma-I9PD1c) `qGma-I9PD1c` | Spacemarine658 | 12:35 | auto | 2508 | `praxe/mereni-automaticky.md` | doplněk k tracingu: jak Memory Insights vůbec spustit (bat soubor, metadata kanály, bookmarky) |
| published | [Unreal Engine 5.6 The 10 Biggest Mistakes You're Making](https://www.youtube.com/watch?v=QcGFO0DzFMg) `QcGFO0DzFMg` | Taken Grace | 9:45 | auto | 2182 | `teorie/zaklady.md` | DUPLIKÁT: všech 10 „chyb" už knihovna pokrývá do hloubky (GDD, organizace, blueprinty, tick, LODy, světla, testování, verzování) — nic nového nepřidáno |
| published | [What to teach when AI writes the code \| Rainer Stropek \| TEDxLinz](https://www.youtube.com/watch?v=yhGzXULZkEw) `yhGzXULZkEw` | TEDx Talks | 18:19 | manual | 2400 | `teorie/uceni-v-ere-ai.md` | +1: „nový programovací jazyk je srozumitelnost"; smutek místo strachu |
| published | [How This Game Dev Sold 1,000,000 Copies of His Game (In A WEEK) — Full Time Game Dev Podcast Ep. 007](https://www.youtube.com/watch?v=kodquYtxXd8) `kodquYtxXd8` | Thomas Brush | 76:49 | auto | 15454 | `teorie/napad.md` + `teorie/prototypovani.md` | 2 myšlenky: hook „X, ale Y" (Cult of the Lamb) · iterace bez GDD, booleovské A/B a tři pilíře |
| published | [Epic's Unreal Optimization Disaster \| Why Nanite Tanks Performance!](https://www.youtube.com/watch?v=M00DGjAP-mU) `M00DGjAP-mU` | Threat Interactive | 13:07 | auto | 2529 | `praxe/nanite-do-hloubky.md` | staged disagreement: kritika Nanitu — mechanismus platí, závěr z něj neplyne |
| published | [1-hour of Unreal GPU Optimization Tips & Tricks](https://www.youtube.com/watch?v=c2MH20OPSw0) `c2MH20OPSw0` | Tom Looman | 62:04 | manual | 11791 | `praxe/gpu-pruchod.md` | hodinový průchod ukázkovou scénou — 8 nálezů; contact shadows i do stínové cache |
| published | [Geometry Optimization In a Few Clicks \| Unreal Engine 5](https://www.youtube.com/watch?v=h6uLdQmwc7c) `h6uLdQmwc7c` | Unreal ArchWizard | 1:36 | auto | 308 | `praxe/pamet-a-instance.md` | do „drobků": AutoLOD v modeling mode, 1M → 5k trojúhelníků, 100× menší na disku |
| published | [Unreal Fest Stockholm 2025 Collection - Profiling, Telemetry, and Performance](https://www.youtube.com/watch?v=CijCVXa0wBQ) `CijCVXa0wBQ` | Unreal Engine | 145:05 | auto | 25310 | `praxe/mereni-automaticky.md` | **PŘEKRYV (ověřeno 2026-07-29):** sestřih tří přednášek — 0:00–1:01 = `C-AjCqjKRSs`, 1:01–1:39 = **unikátní** talk o tracingu (Johan Berg, Insights tým, ~4,9k slov), 1:39–2:24 = `vnbARZHccpQ`. Číst **jen prostřední úsek**; zbytek brát ze samostatných videí. Úspora ~21k slov. **Dávka 38 (2026-07-30):** unikátní úsek je o tracingu, ne o GPU — odloženo k plánované myšlence „automatizace měření" spolu s `bfkbwXVMtn8` a `HQLYkwoDoT4`. **ZPRACOVÁNO (dávka 40):** **jen prostřední úsek 1:04–1:34** (tracing, Johan Berg); zbytek sestřihu je duplikát — viz poznámka |
| published | [Automated Performance Profiling for Local Workflows \| Inside Unreal](https://www.youtube.com/watch?v=bfkbwXVMtn8) `bfkbwXVMtn8` | Unreal Engine | 115:40 | auto | 18793 | `praxe/mereni-automaticky.md` | automatizovaný benchmark z level sequence; Take Recorder jako past |
| published | [Profiling with Purpose: Performance Lessons from a Real Unreal Project \| Unreal Fest Stockholm 2025](https://www.youtube.com/watch?v=C-AjCqjKRSs) `C-AjCqjKRSs` | Unreal Engine | 57:30 | auto | 11598 | `praxe/gpu-pruchod.md` | **doplněk bloku (2026-07-30):** příprava profilování cizí hry + Chaos Visual Debugger; dřív omylem vynecháno jako část sestřihu |
| published | [A Frame’s Life: Frame Timing, Synchronization, and Latency in UE \| Unreal Fest Chicago 2026](https://www.youtube.com/watch?v=dKSHw_8vz3I) `dKSHw_8vz3I` | Unreal Engine | 52:47 | auto | 10389 | `praxe/frame-pacing.md` | páteř druhé kapitoly: potrubí snímku, latence vs. odolnost, jitter |
| published | [Optimizing UE5: Advanced Rendering, Graphics Performance, and Memory Management \| Unreal Fest 2024](https://www.youtube.com/watch?v=dj4kNnj4FAQ) `dj4kNnj4FAQ` | Unreal Engine | 51:14 | auto | 10400 | `praxe/nanite-do-hloubky.md` | páteř dávky: rozhodovací strom Nanitu, cluster culling, VSM cache, VT a pooly, Lumen |
| published | [How to Start Your Project at 60 FPS and Keep It There \| Unreal Fest Chicago 2026](https://www.youtube.com/watch?v=DxBKmQ-0kfw) `DxBKmQ-0kfw` | Unreal Engine | 50:06 | auto | 10327 | `praxe/rozpocet-snimku.md` | první changelist: defaulty, scalability, device profily a rozlišovací žebřík |
| published | [The Player Was Here: Persisting World State and Actor LOD Systems \| Unreal Fest Chicago 2026](https://www.youtube.com/watch?v=KBn62trwkLw) `KBn62trwkLw` | Unreal Engine | 48:56 | auto | 8602 | `praxe/persistence-a-hydratace.md` | celá kapitola: kvíz o dveřích a GC, identita/stav/verze, instance actory a mass |
| published | [Optimizing Niagara: a Practical Approach to Performant Worlds \| Unreal Fest Orlando 2025](https://www.youtube.com/watch?v=71c5yv-XeY8) `71c5yv-XeY8` | Unreal Engine | 46:56 | auto | 9776 | `praxe/niagara-vykon.md` | páteř kapitoly o Niagaře: diagnostika, effect type, škálování a pooling, lightweight vs. data channels |
| published | [New GPU Profiler and RHI Submission Pipeline \| Unreal Fest Stockholm 2025](https://www.youtube.com/watch?v=vnbARZHccpQ) `vnbARZHccpQ` | Unreal Engine | 45:59 | auto | 9950 | `praxe/gpu-pamet.md` | nový GPU profiler 5.6: busy/wait/idle, RHI submission a paralelní překlad |
| published | [Profiling with Pirates: Performance Plundered from a Real Game \| Unreal Fest Chicago 2026](https://www.youtube.com/watch?v=CYvLn-tYRag) `CYvLn-tYRag` | Unreal Engine | 45:11 | auto | 8509 | `praxe/profiling.md` | prahy: `UObject`y, GC, shading biny, `obj list`/`obj refs`, `-corelimit` |
| published | [Maximizing Your Game's Performance in Unreal Engine \| Unreal Fest 2022](https://www.youtube.com/watch?v=GuIav71867E) `GuIav71867E` | Unreal Engine | 41:53 | manual | 7933 | `praxe/rozpocet-snimku.md` | rozpočet jako peněženka, kdy optimalizovat, pořadí co → proč → jak |
| published | [Mastering Performance Analysis with Unreal Insights \| Unreal Fest Bali 2025](https://www.youtube.com/watch?v=HQLYkwoDoT4) `HQLYkwoDoT4` | Unreal Engine | 40:05 | auto | 4522 | `praxe/mereni-automaticky.md` | systematické čtení Insights; přepis silně zkomolený, zpracováno konzervativně |
| published | [From Scan to Stream: Open Pipelines for Large-Scale 3D in Unreal Engine  \| Unreal Fest Chicago 2026](https://www.youtube.com/watch?v=5ehoHM-uzRQ) `5ehoHM-uzRQ` | Unreal Engine | 38:12 | auto | 7299 | `praxe/velke-svety.md` | REASSIGN: arch-viz, ne hry — bereme techniku (adaptivní octree, skořápka první, 98 % odložených trojúhelníků) |
| published | [Lessons Learned from Building a Very Large Open World Game in UE5 \| Unreal Fest Chicago 2026](https://www.youtube.com/watch?v=AalP65lrtpo) `AalP65lrtpo` | Unreal Engine | 37:30 | auto | 7309 | `praxe/velke-svety.md` | páteř kapitoly: vlastní nástroj do koše, World Partition + OFPA, asset user data, animace na události |
| published | [Technical Artist's Guide to Profiling in Unreal Engine \| Unreal Fest Orlando 2025](https://www.youtube.com/watch?v=mCZRHljYnZA) `mCZRHljYnZA` | Unreal Engine | 33:26 | auto | 5305 | `praxe/profiling.md` | páteř kapitoly: rozhodovací strom, reprodukovatelný test, předávka nálezu |
| published | [Unreal Engine Performance Optimization Tips](https://www.youtube.com/watch?v=V8NnLnBQFIg) `V8NnLnBQFIg` | Unreal University  | 8:10 | auto | 1749 | `praxe/pamet-a-instance.md` | do „drobků": mipy potřebují mocninu dvou (tichá podmínka), LODy, draw distance, options menu |
| published | ["Optimized for 360p" ... huh?](https://www.youtube.com/watch?v=zT8DZsdJ72Y) `zT8DZsdJ72Y` | Vex | 17:40 | auto | 3610 | `praxe/frame-pacing.md` | pohled hráče: dynamické rozlišení, shader stutter, mlha jako optimalizace |
| published | [Why I don't use Aseprite - The Tools I Use for Indie Game Dev (2D and 3D)](https://www.youtube.com/watch?v=wuO_iy0zhPA) `wuO_iy0zhPA` | Zizaco | 8:21 | manual | 1760 | `teorie/2d-vizual.md` | +1: „zpomal, abys byl rychlejší" — volba nástrojů jako investice |

### Gamedev-music · třetí vlna (+20) · `hotovo` (dávky 44–45)

Celkem ~41k slov. Dominantní shluk: **Strudel a live coding hudby** (Glossing ×6, Switch Angel ×4, workshop Creative Code Art 82 min, SAGA3K) — nové téma, ve stávající sekci Hudba nemá kam. Dál **Alex Rome ×3** (progrese a emoce, systém psaní písní, remake Zimmera — přímé rozšíření `hudba/akordy-a-harmonie.md` a `hudba/melodie.md`), rytmus (Red Means Recording), AI na vokály. Pozor: několik položek jsou **performance/mixy, ne tutoriály** (137–405 slov přepisu) — kandidáti na `skip` nebo pouhou vizuální/poslechovou referenci; 2 videa jsou bez přepisu.

**Stav po dávce 45 — HOTOVO:** 13 published (dávka 44: strudelový shluk → nová kapitola `hudba/live-coding.md` + FM do `hudba/synteza-zvuku.md`; dávka 45: Alex Rome ×3 + odložený `_yw85rAb6cw` → `akordy-a-harmonie.md`, `aranz.md` a `tvorba-soundtracku.md`, rytmus → nová kapitola `hudba/rytmus.md`, AI vokály → `nastroje-zdarma-a-game-jam.md`, kvintový kruh → `fyzika-souzvuku.md`), 7 skip (performance a mixy — potvrzeno poměrem délky přepisu ke stopáži). **0 todo — třetí vlna je celá zpracovaná.**

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [15 Chord Progressions for 15 Different Emotions](https://www.youtube.com/watch?v=cU4mqDPZuXg) `cU4mqDPZuXg` | Alex Rome | 22:22 | auto | 2579 | hudba/akordy-a-harmonie.md | katalog 15 progresí + hlavní zdroj myšlenky o překlopitelných („neutrálních") progresích |
| published | [A Simple System For Making Songs in 2026](https://www.youtube.com/watch?v=XlltkalLaU4) `XlltkalLaU4` | Alex Rome | 16:58 | auto | 2183 | hudba/aranz.md | metoda zákopu — vlastní myšlenka; kontrola celku mezi každými dvěma nástroji |
| published | [I Remade The Most Emotional Song Ever Written (Hans Zimmer)](https://www.youtube.com/watch?v=uOUPEqTU9ag) `uOUPEqTU9ag` | Alex Rome | 13:54 | auto | 1191 | hudba/tvorba-soundtracku.md | rozbor přestavbou (Cornfield Chase) — prodleva jako nosník, přírůstek po 16 taktech |
| published | [This AI Will Fix Your BAD Vocals — And Keep Your Real Voice](https://www.youtube.com/watch?v=8w97N0rEIS8) `8w97N0rEIS8` | Arcade | 8:38 | auto | 1535 | hudba/nastroje-zdarma-a-game-jam.md | AI řetěz na vokál; placená spolupráce — zpracováno s výhradami (cloud, licence, sponzor) |
| published | [WORKSHOP // Coding Music With Strudel // Dan Gorelick and Viola He](https://www.youtube.com/watch?v=oqyAJ4WeKoU) `oqyAJ4WeKoU` | Creative Code Art | 82:20 | auto | 13321 | hudba/live-coding.md | Workshop pro úplné začátečníky — hlavní zdroj myšlenky „Co je Strudel", plus mini notace a euklidovské rytmy |
| published | [STRUDEL FOR BEGINNERS](https://www.youtube.com/watch?v=m7Rp46AU8dw) `m7Rp46AU8dw` | Glossing | 45:56 | auto | 5786 | hudba/live-coding.md | Skladba od nuly — hlavní zdroj mini notace, signálového řetězce a myšlenky „Od smyčky k vystoupení" |
| published | [You Can Modulate ANYTHING in Strudel](https://www.youtube.com/watch?v=11frBA9L638) `11frBA9L638` | Glossing | 31:30 | auto | 3537 | hudba/live-coding.md | Modulátory (LFO/envelope/bus) na warm.strudel.cc — do myšlenky „Zvuk, efekty a modulace" |
| published | [this tutorial is 10 minutes long.](https://www.youtube.com/watch?v=7GcSgrJRcIw) `7GcSgrJRcIw` | Glossing | 31:10 | auto | 2172 | hudba/live-coding.md | Časovaný běh — vlastní myšlenka „Deset minut na track"; wchoose, perlin, ribbon |
| skip | [EUPHORIC TRANCE START TO FINISH IN STRUDEL](https://www.youtube.com/watch?v=7NyoZkJgykQ) `7NyoZkJgykQ` | Glossing | 23:51 | auto | 405 | — | performance (405 slov na 24 min) — hudba bez výkladu, žádná přenositelná technika |
| published | [STRUDEL DLC](https://www.youtube.com/watch?v=jKkmzWmIyfs) `jKkmzWmIyfs` | Glossing | 13:30 | auto | 1656 | hudba/live-coding.md | MIDI klávesy, scribe, move, vlastní knihovna skriptů — do myšlenky „Od smyčky k vystoupení" |
| published | [How many FMs can we bake into a strudel?](https://www.youtube.com/watch?v=8ruLuZv1ju8) `8ruLuZv1ju8` | Glossing | 4:53 | auto | 568 | hudba/synteza-zvuku.md | FM syntéza — vlastní myšlenka „FM: když jeden zvuk ohýbá druhý" (obecná, ne strudelová) |
| published | [music theory is witchcraft](https://www.youtube.com/watch?v=7mLqpA-PMwM) `7mLqpA-PMwM` | GST Channel | 4:00 | manual | 515 | hudba/fyzika-souzvuku.md | kvintový kruh je spirála (pythagorejské koma) + tvary na kruhu tónů |
| skip | [Best of Deep Trance 2026 \| Emotional Melodic Trance Mix](https://www.youtube.com/watch?v=2zKnDoUjk1I) `2zKnDoUjk1I` | Interstellar Station | 54:58 | auto | 137 | — | 55min mix (137 slov) — poslechový set, ne tutoriál |
| published | [Fundamentals of Rhythm for Electronic Music](https://www.youtube.com/watch?v=JE3QM_9sljI) `JE3QM_9sljI` | Red Means Recording | 21:02 | auto | 3210 | hudba/rytmus.md | páteř celé nové kapitoly — mřížka a swing, silné/slabé doby, frázování a fill vs. prázdno |
| skip | [A Ronin Mode Tribute to Rob Dougan Furious Angels Full Album HQ Remastered](https://www.youtube.com/watch?v=7xo56yUbVv0) `7xo56yUbVv0` | Ronin Mode | 7:27 | — | — | — | bez přepisu, hudební set — ne tutoriál |
| skip | [BIRDS OF A FEATHER (Remake in Strudel)](https://www.youtube.com/watch?v=_PjSOSoZeSA) `_PjSOSoZeSA` | SAGA3K Records | 1:36 | — | — | — | 96s klip bez přepisu — ukázka, ne výklad |
| published | [Creating Beats & Rhythms in STRUDEL](https://www.youtube.com/watch?v=sefJz9biLCY) `sefJz9biLCY` | Switch Angel | 15:16 | auto | 1789 | hudba/live-coding.md | Euklidovské rytmy, struct/beat, degrade a ribbon — hlavní zdroj myšlenky „Euklidovské rytmy a řízená náhoda" |
| skip | [Coding Trance IV](https://www.youtube.com/watch?v=3fpx7Scysw4) `3fpx7Scysw4` | Switch Angel | 6:05 | auto | 172 | — | performance (172 slov) — bez výkladu |
| skip | [Coding Trance Music from Scratch (Again )](https://www.youtube.com/watch?v=iu5rnQkfO6M) `iu5rnQkfO6M` | Switch Angel | 5:02 | auto | 249 | — | performance (249 slov) — bez výkladu |
| skip | [Livecoding melodic DNB music in Strudel](https://www.youtube.com/watch?v=aPsq5nqvhxg) `aPsq5nqvhxg` | Switch Angel | 4:28 | auto | 290 | — | performance (290 slov) — bez výkladu |


---

## Čtvrtá vlna — hlavní playlist „ue5 - izba" (+93) · staženo 2026-10-10 · **taxonomie schválena 2026-10-10**

Fetch 2026-10-10 **jen z hlavního playlistu** (na YouTube se jmenuje „ue5 - izba"; hudba a Godot se tentokrát nestahovaly). Playlist má 480 unikátních videí, proti `scripts/fetched.txt` je nových **93** → archiv 610 id, `transcripts_clean/` 600 souborů. Všech 93 má `info.json` i anglickou stopu: 11 ručních, 82 automatických, `VxTQhSr1sbw` je španělský originál přepsaný z anglického dabingu. Celkem ~458k slov.

**Tři opravy pipeline při té příležitosti** (detail v dev_logu 2026-10-10): `clean_transcripts.py` vybírá stopu podle `info.json` (dřív si u vícejazyčných videí bral strojový zpětný překlad typu `en-de` místo ručních titulků), bere `en-orig` před `en` (automatická `en` je u 10 nových videí zpětný překlad z auto-dabingu; ve starém korpusu takový případ není) a odmítne ruční stopu, která je delší než video (`wknRD5g-vvk` má ruční titulky z jiného videa svého autora).

**Rozložení:** **81 `todo`** v deseti dávkách (47–56, ~403k slov) — 73 do Praxe v UE5, 8 do Teorie · **9 `skip`** (5 mimo záběr knihovny nebo bez mluveného slova, 4 duplikáty obsahu) · **3 `todo-lp`** (dlouhé začátečnické průchody, stejně jako `FAo9nfWYPSE`). Skip potvrzen uživatelem 2026-10-10 (všech 9).

**Stav po dávce 47:** 11 published — nové kapitoly `praxe/inventar.md` (5 myšlenek) a `praxe/debugging.md` (2), +1 myšlenka do `principy-architektury.md` a `pamet-a-instance.md`, doplňky do `komunikace-blueprintu.md` a `organizace-projektu.md`; `R_gX46NtqU8` přesunut do skip (obsah už v knihovně je). Zbývá 70 todo v dávkách 48–56.

**Dotčené díry z `content_gaps.md`:** UI a UMG (P1) dostává první zdroje, ale jen pro **UI ve světě** (diegetické menu, health bary nad hlavou, cena in-world widgetů) — jádro UMG a Common UI dál chybí; multiplayer (P3) jeden zdroj (`_jRLlTDqoGI`); doba buildu a testy (P2) částečně (`BJ8gQQmJJ-U`); slabý hardware (P2) jedna případovka (`Pkd7-ouyb-M`).

### Změny ve stromu (schváleno 2026-10-10)

**15 nových kapitol v Praxi v UE5 a 1 nové nav téma.** Slugy jsou pracovní, dokud kapitola nevyjde — pak jsou veřejné API.

| nová kapitola | nav téma | dávka | páteř |
|---|---|---|---|
| `praxe/inventar.md` — inventář: definice, instance, akce, vybavení | Blueprint architektura a organizace projektu | 47 | Ali Elzoheiry, díly 6 · 8 · 10 · 11 (díly 1–2 už jsou v `principy-architektury.md`) |
| `praxe/debugging.md` — ladění: vidět, co hra dělá | Editor a workflow | 47 | DK 3D + gameplay debugger |
| `praxe/mass-ecs.md` — Mass a ECS: data místo objektů | Výkon a profiling | 48 | Unreal Fest Chicago 2026 |
| `praxe/interakcni-animace.md` — postava sahá na svět (motion warping, IK, contextual animation) | Animace: nástroje a mocap | 49 | Houman Creates ×3, Tank Control Games ×2 |
| `praxe/cutsceny.md` — cutscény a přechod do cinematiky bez střihu | Animace: nástroje a mocap | 49 | 2 tutoriály (Sequencer má v knihovně jen zmínky) |
| `praxe/souboj.md` — souboj: od montáže po hit stop | Herní systémy a interakce | 50 | Evans Bohl (3,8 h) + game feel + zdraví končetin |
| `praxe/ui-ve-svete.md` — UI ve světě: diegetické menu a world-space widgety | **nové téma „UI a rozhraní"** | 50 | Houman Creates + úseky ze tří dalších videí |
| `praxe/ai-ve-velkem.md` — AI ve velkém: navigace, rozhodování, reakce | AI a chování NPC | 50 | Lords of the Fallen (Unreal Fest Stockholm 2025) |
| `praxe/destrukce-a-latky.md` — Chaos: destrukce a látky | Fyzika: ragdoll, lana, simulace | 51 | Unreal Fest 2024 + Chaos Cloth Dataflow 5.8 |
| `praxe/blockout.md` — blockout jako polovina projektu | Prostředí a environment art | 52 | JaviSkau + hybridní blockout Naughty Dog |
| `praxe/modularni-kity.md` — modulární kity a trim sheety | Prostředí a environment art | 52 | Beyond Extent (87 min) + 2× trim sheety + Witcher 3 a Mortal Shell 2 |
| `praxe/env-technika.md` — breakdowny II: technika za vzhledem | Prostředí a environment art | 52 | 007 First Light, Alan Wake 2, AC Black Flag Resynced |
| `praxe/megalights.md` — MegaLights | Osvětlení a atmosféra | 53 | Inside Unreal (2,8 h) |
| `praxe/pcg-mesta.md` — procedurální města | PCG a procedurální svět | 54 | Lucid Games (Unreal Fest Chicago 2026) |
| `praxe/mcp-v-editoru.md` — MCP v editoru: jak ho Epic navrhl a jak ho rozšířit | AI nástroje ve vývoji | 55 | Epic ×2 + JetBrains Rider |

Schválené přejmenování v nav (jen titulek, URL beze změny): „Animace: nástroje a mocap" → **„Animace: nástroje, interakce a cutscény"**, protože do tématu přibudou dvě kapitoly, které nejsou o nástrojích. _Provedeno až v dávce 50 (v dávce 49 opomenuto)._

### Plán dávek

| dávka | téma | todo | ~slov | nové kapitoly | rozšiřuje |
|---|---|---|---|---|---|
| 47 ✅ | Blueprint architektura, inventář a ladění | 11 + 1 skip | 51k | `inventar`, `debugging` | `principy-architektury`, `pamet-a-instance`, `komunikace-blueprintu`, `organizace-projektu`, `editor-tipy` |
| 48 ✅ | Výkon, škálování a zdraví projektu | 7 | 37k | `mass-ecs` | `gpu-pruchod`, `mereni-automaticky`, `nanite-do-hloubky`, `lehky-render`, `niagara-vykon`, `organizace-projektu` (místo `optimalizace`) |
| 49 ✅ | Animace: interakce, cutscény, rigging a mocap | 12 | 46k | `interakcni-animace`, `cutsceny` | `animace-nastroje`, `metahuman` |
| 50 ✅ | Souboj, herní systémy, UI ve světě a AI nepřátel | 7 | 55k | `souboj`, `ui-ve-svete`, `ai-ve-velkem` | `pasti-a-mechaniky` |
| 51 ✅ | Fyzika a GASP 5.8 | 5 | 49k | `destrukce-a-latky` | `mover`, `gasp`, `ragdoll` |
| 52 ✅ | Prostředí: blockout, modulární kity a breakdowny | 10 | 47k | `blockout`, `modularni-kity`, `env-technika` | — |
| 53 ✅ | Světlo a materiály | 6 | 40k | `megalights` | `materialy`, `ps1-estetika`, `landscape-tipy` |
| 54 ✅ | PCG, terén, povrchy a velké světy | 7 | 39k | `pcg-mesta` | `pcg-liany`, `pcg-vegetace`, `mesh-terrain`, `velke-svety`, `footsteps` |
| 55 ✅ | AI nástroje: MCP, agenti a AI animace | 8 | 26k | `mcp-v-editoru` | `claude-code-ue`, `ai-assety`, `teorie/2d-vizual` |
| 56 ✅ | Teorie: příběh, plánování, design a level design | 7 | 14k | — | `pribeh-a-postavy`, `planovani-nastroje`, `jak-se-ucit-kodovat`, `systemy-a-mechaniky`, `algoritmy-prehled`, `prostor-a-hranice`, `vydani-hry` |

**Vazby mezi dávkami** (ať se nic neztratí, když se pořadí změní): `ui-ve-svete` (50) čerpá i z úseků `xr-2TrMUd9w` (48), `4omEu9N9WIE` a `Mv1LGtQRVls` (50) a dostane backlink z Cyberpunku `G_te2IkVVi4` (56) · GASP 5.8 `6NYC4ryO9ik` (51) má úsek pro `interakcni-animace` (49, backlink) a úsek o AnimGen pro dávku 55 · `blockout` (52) dostane Pozn. z Cyberpunku (56) · prostřelené barely ze 007 (52) jsou AAA protějšek k `8aDH2KUGdbE` (50).

### Dávka 47 — Blueprint architektura, inventář a ladění · `hotovo`

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [Data Driven Inventory System (Part 6: Using Items) \| Unreal Engine 5 Tutorial](https://www.youtube.com/watch?v=LKdBlgQ8_rY) `LKdBlgQ8_rY` | Ali Elzoheiry | 43:08 | auto | 7216 | `praxe/inventar.md` | myšlenka „Použití jako seznam akcí" (+ problém stavu, na který navazuje díl 8) · dávka 47 |
| published | [Data Driven Inventory System (Part 8: Item Instances Integrated) \| Unreal Engine 5](https://www.youtube.com/watch?v=jRTjBB8vIfM) `jRTjBB8vIfM` | Ali Elzoheiry | 48:44 | auto | 7794 | `praxe/inventar.md` | dvě myšlenky: „Definice popisuje druh, instance nese kus" a „Když stav opouští inventář, cestuje jako data" · dávka 47 |
| published | [Data Driven Inventory System (Part 10: EQUIPMENT) \| Unreal Engine 5](https://www.youtube.com/watch?v=vW2zUajnaGY) `vW2zUajnaGY` | Ali Elzoheiry | 58:09 | auto | 9663 | `praxe/inventar.md` | myšlenka „Vybavení je samostatný systém"; v Pozn. paralela s třídami vybavení v Lyře · dávka 47 |
| published | [Data Driven Inventory System (Part 11: ITEM STATS) \| Unreal Engine 5](https://www.youtube.com/watch?v=a7sVIyCwbbY) `a7sVIyCwbbY` | Ali Elzoheiry | 23:34 | auto | 3908 | `praxe/inventar.md` | myšlenka „Staty: náhoda při vzniku, modifikátory při vybavení" (500 → 400); přepis z `en-orig`, auto `en` byl zpětný překlad · dávka 47 |
| published | [Why Your Unreal Project Becomes a Mess (And How to Fix It) \| UE5 Inheritance Explained](https://www.youtube.com/watch?v=xS7wckoboAo) `xS7wckoboAo` | Ali Elzoheiry | 27:24 | auto | 4528 | `praxe/principy-architektury.md` | +1 „Kdy dědit a kdy jen konfigurovat" (hned za Dědičností); úvod kapitoly obnoven · dávka 47 |
| published | [Stop Overusing Hard References ( Do This Instead )](https://www.youtube.com/watch?v=OpotdQGOAYE) `OpotdQGOAYE` | Unreal University | 8:21 | auto | 1587 | `praxe/pamet-a-instance.md` | +1 „Soft reference: načti, až když to hra potřebuje" (24,5 MB → 99 KB) · dávka 47 |
| published | [Every Unreal Engine Tutorial Teaches Casting Wrong](https://www.youtube.com/watch?v=PkCIoPIIOzc) `PkCIoPIIOzc` | Unreal University | 10:30 | auto | 1991 | `praxe/komunikace-blueprintu.md` | doplněk „Třetí cesta: castuj na lehkého společného rodiče" v myšlence o ceně castu · dávka 47 |
| published | [5 Ways To Optimise Your Game In Unreal Engine](https://www.youtube.com/watch?v=UAVz7WTARIk) `UAVz7WTARIk` | Unreal University | 16:32 | auto | 3054 | `praxe/pamet-a-instance.md` | do soft reference (past: v editoru funguje, po restartu ne) + doplněk Drobků (normál mapa, menu nastavení) · dávka 47 |
| published | [Level up your UE DEBUGGING skills](https://www.youtube.com/watch?v=xPihqWA6tkE) `xPihqWA6tkE` | DK 3D | 25:30 | auto | 3219 | `praxe/debugging.md` | myšlenka „Čtyři otázky, čtyři nástroje" · dávka 47 |
| published | [Learn Character AI in Unreal Engine 5: Basics](https://www.youtube.com/watch?v=vcGtpTn5X8s) `vcGtpTn5X8s` | Taken Grace | 24:58 | auto | 5450 | `praxe/debugging.md` | myšlenka „AI, která nereaguje" — gameplay debugger a tři chyby naživo; základy BT zůstaly v `ai-zaklady.md` · dávka 47 |
| published | [This Tool Makes Git Much More Accessible For Game Dev Teams](https://www.youtube.com/watch?v=sB8jryDaaXE) `sB8jryDaaXE` | Game Dev Guide | 10:59 | auto | 2478 | `praxe/organizace-projektu.md` | doplněk Git myšlenky „Kde Git na hry přestane stačit" (zámky souborů); sponzor flag v Pozn. · dávka 47 |
| skip | [Work 4X Faster in UE5.7: 5 Pro Hotkeys Nobody Uses (UE5)](https://www.youtube.com/watch?v=R_gX46NtqU8) `R_gX46NtqU8` | 3D Dreamer | 0:30 | manual | 79 | — | obsah už je v `organizace-projektu.md` (devět tipů: komentáře, reroute, zarovnání, collapse) — dávka 47 |

### Dávka 48 — Výkon, škálování a zdraví projektu · `hotovo`

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [Fighting the Frame Budget: Stage Optimization Lessons from 2XKO \| Unreal Fest Chicago 2026](https://www.youtube.com/watch?v=Pkd7-ouyb-M) `Pkd7-ouyb-M` | Unreal Engine | 34:07 | auto | 6533 | `praxe/gpu-pruchod.md` + `praxe/mereni-automaticky.md` | rozděleno: první dvě třetiny jako „Bojovka pro desetiletý hardware" (rozpočet po částech, CPU i GPU nálezy) v `gpu-pruchod`, nástrojová třetina jako „Výkon jako věc celého týmu" (dashboard, validace textur, memory checker) v `mereni-automaticky` · dávka 48 |
| published | [UE5 Nanite Optimization Deep Dive — Cutting 3GB](https://www.youtube.com/watch?v=RvEcTRAqA6Y) `RvEcTRAqA6Y` | DK 3D | 45:11 | auto | 5661 | `praxe/nanite-do-hloubky.md` | +1 „Nanite a velikost balíčku" (Keep Triangle Percent, Trim Relative Error na listí, Property Matrix; 3 GB) · dávka 48 |
| published | [How I Optimized My Game to Over 200 FPS in UE5](https://www.youtube.com/watch?v=xr-2TrMUd9w) `xr-2TrMUd9w` | Procedural Minds | 22:46 | auto | 4555 | `praxe/lehky-render.md` + `praxe/niagara-vykon.md` | rozděleno: „Ze 100 na 200 FPS" (TSR jako AA, celé vypnutí Nanitu, SSGI) v `lehky-render` + doplněk „Niagara Debugger" v Diagnostice Niagary; úsek o in-world widgetech (11:00–15:40) zpracován v `ui-ve-svete.md` jako „Sto health barů" (dávka 50) · dávka 48 |
| published | [How to Boost FPS Fast in UE5 with this ONE Setting](https://www.youtube.com/watch?v=aK9K7CffqCk) `aK9K7CffqCk` | 3D Dreamer | 0:21 | manual | 54 | `praxe/gpu-pruchod.md` | místo `optimalizace.md` jako závorka v 2XKO myšlence (Bounds Scale, s výhradou, že bounds musí obalit viditelný mesh) · dávka 48 |
| published | [Unlearning OOP: Data-Oriented Gameplay Design with ECS and Mass Entity \| Unreal Fest Chicago 2026](https://www.youtube.com/watch?v=UXA8axmAb-U) `UXA8axmAb-U` | Unreal Engine | 43:37 | auto | 8573 | NOVÁ `praxe/mass-ecs.md` | tři myšlenky: „Proč objekty zpomalují", „Entita není actor", „Jak s Mass pracovat"; spor s hydratací rozehraný v Pozn.; „fragment" rozlišen v rejstříku · dávka 48 |
| published | [Building Living World Creatures with Niagara \| Unreal Fest Chicago 2026](https://www.youtube.com/watch?v=pwpwy6m38bk) `pwpwy6m38bk` | Unreal Engine | 16:51 | auto | 2943 | `praxe/niagara-vykon.md` | +1 „Živý svět z částic: tvorové, kteří poslouchají, ale nehlasují" (CPU 0,15 ms vs GPU 2 ms, PCG → Data Channel) · dávka 48 |
| published | [Project Health in Unreal Engine: The Technical Indicators That Matter \| Unreal Fest Chicago 2026](https://www.youtube.com/watch?v=BJ8gQQmJJ-U) `BJ8gQQmJJ-U` | Unreal Engine | 44:21 | auto | 8211 | `praxe/organizace-projektu.md` | +1 „Technické zdraví projektu" — deset ukazatelů přeskládaných podle fáze projektu; nová hesla ABTest, Hitch, Gauntlet · dávka 48 |
| skip | [How Subnautica 2 Handles 100,000+ Actors in UE5](https://www.youtube.com/watch?v=x6UqZq-XpXE) `x6UqZq-XpXE` | Smart Poly | 9:05 | auto | 1660 | — | DUPLIKÁT obsahu: shrnutí přednášky `AalP65lrtpo` (Subnautica 2), která je ve `velke-svety.md` zpracovaná z originálu |
| skip | [Scaling AI the Smart Way: Memory Footprint and Runtime Efficiency \| Unreal Fest Chicago 2026](https://www.youtube.com/watch?v=BFfebAtBLfU) `BFfebAtBLfU` | Unreal Engine | 33:07 | auto | 4865 | — | runtime ML inference pro moderaci hlasového chatu (NNE, AMD) — mimo záběr sólo vývoje; jediný přenositelný fakt: trvalá inference na CPU sní půl CPU rozpočtu (27:42) |

### Dávka 49 — Animace: interakce, cutscény, rigging a mocap · `hotovo`

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [Build Better Doors in Unreal Engine 5](https://www.youtube.com/watch?v=CR8Qy6dmCAU) `CR8Qy6dmCAU` | Houman Creates | 29:27 | auto | 4485 | `praxe/interakcni-animace.md` | páteř 4 myšlenek: data interakce v objektu, motion warping s krokem v animaci, IK ruky (osy, pole vector, mesh space), normalizované křivky v montáži (Max/Min drží stav) · dávka 49 |
| published | [Realistic Pickup System in Unreal Engine 5 (Control Rig + Grip Poses)](https://www.youtube.com/watch?v=W856GJgqM2U) `W856GJgqM2U` | Houman Creates | 35:12 | auto | 5711 | `praxe/interakcni-animace.md` | +1 „Jedna animace zvednutí pro všechno" (grip point jako vlastní Scene Component, dot product, pose asset) + podklad pro IK, interface a křivky · dávka 49 |
| published | [The Secret to Realistic Item Interactions in Unreal Engine 5](https://www.youtube.com/watch?v=6zGQFsnKCeY) `6zGQFsnKCeY` | Houman Creates | 11:50 | auto | 1885 | `praxe/interakcni-animace.md` | +1 „Předmět do ruky bez teleportu" (attach ≠ snap, výšky ±40 cm, dohled 500 vs. dosah 120 cm) + ruční pole vector · dávka 49 |
| published | [EASY Object Interactions in Unreal Engine 5 \| Contextual Animation](https://www.youtube.com/watch?v=OpSqCcPVJUY) `OpSqCcPVJUY` | Tank Control Games | 17:07 | auto | 3687 | `praxe/interakcni-animace.md` | +1 „Contextual Animation: scéna s rolemi" (rules a scene asset, stejná délka, pauza po konci scény) + master actor, warp k objektu · dávka 49 |
| published | [Finally, PERFECT Zombie Synced Animations in UE5 (Contextual Animation Tutorial)](https://www.youtube.com/watch?v=NoI3GyDvyKI) `NoI3GyDvyKI` | Tank Control Games | 21:32 | auto | 4567 | `praxe/interakcni-animace.md` | +1 „Zápas se smyčkou" (sekce Enter → Loop → Exit/Bite, Set Next Section na obou montážích) + warp napůl, Flying, inertialization · dávka 49 |
| published | [SEAMLESS Gameplay to Cinematic Finishers in Unreal Engine 5 (No Cuts)](https://www.youtube.com/watch?v=buVZ7-0NX94) `buVZ7-0NX94` | Tank Control Games | 14:58 | auto | 3154 | `praxe/cutsceny.md` | „Finisher bez střihu" — Transform Origin Actor, autoring v nule, posun kvůli warpingu, pop přes Override Aspect Ratio Axis Constraint · dávka 49 |
| published | [UE 5.8 - How To Add Cutscenes To Your Game - Tutorial](https://www.youtube.com/watch?v=pV727-cB69Y) `pV727-cB69Y` | Unreal - X - Tutorials | 11:34 | auto | 1565 | `praxe/cutsceny.md` | „Cutscéna, která vrátí hru tam, kde skončila" — Keep State, Can Blend, control rotation, Do Once a tři triggery, zatmívačka v makru · dávka 49 |
| published | [Creating a Pistol w/ Flashlight Aim Set - Unreal Engine 5 Tutorial](https://www.youtube.com/watch?v=1N4yZ6g6LB0) `1N4yZ6g6LB0` | Surreptitious Vignettes | 4:52 | auto | 816 | `praxe/animace-nastroje.md` | doplněk do „Křivky, kamera a past 30 snímků" (úprava hotových animací klíči přímo v UE; video z 2023) · dávka 49 |
| published | [State of Rigging and Animation Tools in Unreal Engine 5.8 \| Unreal Fest Chicago 2026](https://www.youtube.com/watch?v=yi-oDmC1nqU) `yi-oDmC1nqU` | Unreal Engine | 38:57 | auto | 7231 | `praxe/animace-nastroje.md` | +2 (místo +1): „Sekundární pohyb v Control Rigu" (dynamics, fyzika jako vrstva, AutoBake) a „Rig, který se přenese" (DMC, moduly, Dataflow, shot correctives) · dávka 49 |
| published | [Aprons on, it's time for some baking🧑‍🍳](https://www.youtube.com/watch?v=ueozYU2YNlI) `ueozYU2YNlI` | Unreal Engine | 0:48 | auto | 196 | `praxe/animace-nastroje.md` | doplněk AutoBake v „Sekundární pohyb v Control Rigu" · dávka 49 |
| published | [MetaHuman Animator Markerless Motion Capture Demo](https://www.youtube.com/watch?v=r_-fEi7fXLA) `r_-fEi7fXLA` | Unreal Engine | 51:05 | auto | 7187 | `praxe/animace-nastroje.md` | prohloubení „Markerless mocap v 5.8": checklist záznamu, pády při Process, Existing Skeleton, aditivní dočištění, hranice · dávka 49 |
| published | [MetaHuman in 2026: Five Years In, What's Next? \| Unreal Fest Chicago 2026](https://www.youtube.com/watch?v=IsbgHRa5N3A) `IsbgHRa5N3A` | Unreal Engine | 33:29 | auto | 5297 | `praxe/metahuman.md` + `praxe/animace-nastroje.md` | +1 „MetaHuman jako standard" (Mesh to MetaHuman pro celé tělo, Collections, DevKit pod MIT; výzkum zvlášť) + úsek o markerless (Meshcapade, lokální zpracování, rozpor s webinářem) do markerless mocapu · dávka 49 |
| skip | [Unreal Engine 5 Tutorial: First-Person Horror Pickup System](https://www.youtube.com/watch?v=Z2cvh0vKa0k) `Z2cvh0vKa0k` | Houman Creates | 31:12 | auto | 2909 | — | starší verze W856GJgqM2U (autor sám odkazuje na novou) |
| skip | [Unreal Engine 5.8 Video To Metahuman Animation! Markerless MoCap Plugin Beginner Tutorial](https://www.youtube.com/watch?v=8lokT6WXnU0) `8lokT6WXnU0` | pinkpocketTV | 8:27 | auto | 1438 | — | čtvrtý krátký návod na markerless workflow, který kapitola už má |
| published | [Don't Buy Mocap Gear! Do This Instead in Unreal Engine 5.8](https://www.youtube.com/watch?v=ol5nY6P4jlg) `ol5nY6P4jlg` | Monsoon Studios 3D | 6:26 | manual | 525 | `praxe/animace-nastroje.md` | jen jedna věta: aspoň 1080p a viditelný obličej (4:38) v checklistu markerless mocapu · dávka 49 (dřív skip) |

### Dávka 50 — Souboj, herní systémy, UI ve světě a AI nepřátel · `hotovo`

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [How to Make a Combat System in UE5](https://www.youtube.com/watch?v=4omEu9N9WIE) `4omEu9N9WIE` | Evans Bohl | 229:17 | auto | 34750 | NOVÁ `praxe/souboj.md` + `praxe/ui-ve-svete.md` | páteř kapitoly, čteno celé: 8 myšlenek v `souboj` (dvě komponenty · combo okna z notify state · útok za běhu s křivkou BlendOff · hitbox impact frame vs. active frames · damage jednou za útok · terč, směr a ragdoll · hit stop per aktér · záblesk a kapow přes custom stencil) + camera shake do „pět potvrzení"; health bar 2:12–2:35 a dispatcher trik 2:31–2:35 → `ui-ve-svete` (2 myšlenky) · dávka 50 |
| published | [5 Ways to Improve Game Feel In Unreal Engine](https://www.youtube.com/watch?v=78MBe46IBrQ) `78MBe46IBrQ` | Unreal University | 8:47 | auto | 1605 | `praxe/souboj.md` + `praxe/ui-ve-svete.md` | „Rána, které hráč uvěří: pět potvrzení" (trail, reakce, zvuk s Modulatorem, kamera, ukazatel) + bílý dojezdový pruh do health baru; promo vlastního programu a cizí Unity tweet přiznány v Pozn. · dávka 50 |
| published | [Limb Health + Breakable Limbs in Unreal Engine 5](https://www.youtube.com/watch?v=Mv1LGtQRVls) `Mv1LGtQRVls` | Tank Control Games | 22:00 | auto | 4372 | `praxe/souboj.md` + `praxe/ui-ve-svete.md` | „Zdraví po končetinách" (physical material jako adresa, struct, pass-by-reference, zlomit vs. zničit) + ukazatel skrytý do zásahu a přesouvaný na socket končetiny do health baru · dávka 50 |
| published | [Interactive Horror Menu in Unreal Engine 5](https://www.youtube.com/watch?v=CDf-5lp4yxQ) `CDf-5lp4yxQ` | Houman Creates | 13:26 | auto | 1382 | NOVÁ `praxe/ui-ve-svete.md` | „Menu jako předmět ve scéně" (Widget Component, Widget Interaction Component jako virtuální myš, kolize blokující paprsek, Press/Release Pointer Key); pojem diegetic UI doplněn námi · dávka 50 |
| published | [Crafting Scalable AI for a AAA Souls-Like Game in Unreal Engine \| Unreal Fest Stockholm 2025](https://www.youtube.com/watch?v=XKQfMZOXFv0) `XKQfMZOXFv0` | Unreal Engine | 40:41 | auto | 8323 | NOVÁ `praxe/ai-ve-velkem.md` | 5 myšlenek: jeden nav mesh pro všechny velikosti (flag šířky chodby) · offset cesty a jak ho uživit · strom jen rozhoduje, nepřítel v datech · reakce vedle stromu (+ paměť BT a utility) · aggro a bojové role · dávka 50 |
| published | [Create a Water Leak System in Unreal Engine 5 \| Blueprint Tutorial (Part 1)](https://www.youtube.com/watch?v=8aDH2KUGdbE) `8aDH2KUGdbE` | Zima Env | 10:46 | auto | 976 | `praxe/pasti-a-mechaniky.md` | +1 „Barel, který teče" (díry jako data, hladina k nejnižší díře, časovač místo ticku); díl 1, druhý podmíněný odezvou · dávka 50 |
| published | [How We Designed a Puzzle Adventure Game in Unreal Engine](https://www.youtube.com/watch?v=tpq66PFyzf0) `tpq66PFyzf0` | Unreal Engine | 18:22 | manual | 3533 | `praxe/pasti-a-mechaniky.md` | +1 „Hádanka ze stavebnice" (spínač přes BPI, kostka jako závaží, pasti z jednoho rodiče, výhra podle klíčů, spawner kostek s limitem) · dávka 50 |

### Dávka 51 — Fyzika a GASP 5.8 · `hotovo`

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [Using Chaos Physics for Large-Scale and High-Fidelity Scenes \| Unreal Fest 2024](https://www.youtube.com/watch?v=uCYGFdEWyZw) `uCYGFdEWyZw` | Unreal Engine | 50:41 | auto | 9460 | NOVÁ `praxe/destrukce-a-latky.md` + `praxe/debugging.md` | 4 myšlenky: graf spojení a cluster union (+ buoyancy) · výkon destrukce (konvexy, debris, ISM pooling, paměť, strop zlomů, Event Relay) · predictive interpolation v multiplayeru · cloth jako samostatný asset přes Dataflow; úsek o CVD → nová myšlenka v `debugging`; talk z 5.4, verze hlídány v Pozn. · dávka 51 |
| published | [Unreal Engine 5.8's NEW Cloth Physics System \| Chaos Cloth Dataflow Tutorial](https://www.youtube.com/watch?v=6XDPQX-i0AQ) `6XDPQX-i0AQ` | Pixelart Animation | 8:04 | auto | 981 | `praxe/destrukce-a-latky.md` | postup v 5.8 v myšlence „Látka jako samostatný asset" (skin v Mayi, cloth asset ze skeletal meshe, Max Distance, simulace v sequenceru); díl 1, další vrstvy slibuje díl 2 · dávka 51 |
| published | [A Dive Into Networked Physics-Based Character Movement \| Unreal Fest Stockholm 2025](https://www.youtube.com/watch?v=_jRLlTDqoGI) `_jRLlTDqoGI` | Unreal Engine | 41:21 | auto | 6834 | `praxe/mover.md` + `praxe/debugging.md` + `praxe/destrukce-a-latky.md` | +2 místo +1: „Chaos Mover: postava jako fyzikální těleso" a „Síťová fyzika zevnitř" (snímky, resimulace, input decay, logika na fyzikálním vlákně); úsek o CVD do `debugging`, replikační LOD do multiplayer destrukce · dávka 51 |
| published | [The Last GASP!? Game Animation Sample Updates for 5.8 + Q&A \| Inside Unreal](https://www.youtube.com/watch?v=6NYC4ryO9ik) `6NYC4ryO9ik` | Unreal Engine | 166:35 | auto | 29960 | `praxe/gasp.md` + `praxe/ragdoll.md` | 7 myšlenek: `gasp` +4 (MM uvnitř chooseru a blend spacy · aditivní look-at · párové akce přes multi-character MM · poslední update, sample ne framework), `ragdoll` +3 (Physics Control profily · ragdoll, který se chrání · vstávání přes MM); backlink z `interakcni-animace`. AnimGen (10:09–13:14, Q&A 2:35:57–2:38:16) zpracován v dávce 55 (`ai-assety`) · dávka 51 |
| published | [Unreal Engine Just Got AAA Animation Physics (Game Animation Sample 5.8)](https://www.youtube.com/watch?v=UP3zWCMPn3E) `UP3zWCMPn3E` | Gorka Games | 8:26 | auto | 1532 | `praxe/gasp.md` + `praxe/ragdoll.md` | doplněk do 5 myšlenek (motory a profily, migrace a experimentální stav, multi-char MM, look-at, chooser); promo konzultací v Pozn. · dávka 51 |
| skip | [Beyond Native: Real-Time Scientific & Cable Simulation in UE5 \| Unreal Fest Chicago 2026](https://www.youtube.com/watch?v=ngx2Cy5tkXo) `ngx2Cy5tkXo` | Unreal Engine | 41:20 | auto | 6121 | — | průmyslový plugin (Skyreal XDE) pro vědeckou simulaci kabelů, živé demo — mimo dosah indie; nanejvýš Pozn. v `lana-kabely.md` |

### Dávka 52 — Prostředí: blockout, modulární kity a breakdowny · `hotovo`

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [BLOCKOUT de Escenarios para Videojuegos](https://www.youtube.com/watch?v=VxTQhSr1sbw) `VxTQhSr1sbw` | JaviSkau \| Senior Environment Artist | 21:07 | auto | 4076 | NOVÁ `praxe/blockout.md` | „Zastav, omez, porovnej" (rozklad na tvary, hierarchie velikostí, poměr detailu a klidu, test přimhouřených očí, šedá jako hodnota, měřítko s postavou, hrát každou půlhodinu); španělský originál, přepis z anglického dabingu, citovaní lidé jen jako role; mentoring v Pozn. |
| published | [Why Naughty Dog's 3D Blockouts Are World Class (Hybrid Workflow)](https://www.youtube.com/watch?v=2OBTIFS0PdE) `2OBTIFS0PdE` | EMC3D - Game Art | 16:09 | auto | 3049 | NOVÁ `praxe/blockout.md` | „Hybridní blockout" (pipeline Naughty Dog z GDC 2014: šedá → hodnoty → barva v mezích PBR → postprocess; úrovně 0–2; čtyři pohledy ve výuce); Patreon v Pozn. |
| published | [The easiest Way to Create Modular 3D Kits Without Stress](https://www.youtube.com/watch?v=77xPHfzciiY) `77xPHfzciiY` | Beyond Extent | 86:47 | auto | 21844 | NOVÁ `praxe/modularni-kity.md` | páteř kapitoly, 3 myšlenky: kit jako lego (co nejméně kusů, mřížka 512 px/m, pivoty, zoo) · textury pro kit (tilery → trimy → masky, dvě textury na kámen) · organický kit a spoje (čtyři texturové spoje, spoje geometrií, kitbashing); placené členství v Pozn. |
| published | [How AAA Studios Texture Huge Worlds \| The Last of Us & Valorant Trim Sheet Workflows](https://www.youtube.com/watch?v=Jn9Zl5SO4EU) `Jn9Zl5SO4EU` | Class Creatives | 19:08 | auto | 3143 | NOVÁ `praxe/modularni-kity.md` | „Trim sheet jako systém" spolu s `Jw9X4HjlFpI` (AC Mirage, TLOU, Valorant, zkosení a navazující hrany na fontáně); ukázka z kurzu (masterclass) v Pozn. |
| published | [Why AAA Games Use Trim Sheets (And How They Actually Work)](https://www.youtube.com/watch?v=Jw9X4HjlFpI) `Jw9X4HjlFpI` | Zeref3DForge | 5:18 | auto | 1096 | NOVÁ `praxe/modularni-kity.md` | „Trim sheet jako systém" (příběh „změňme dřevo", scéna ze dvou textur, kdy trim ne) |
| published | [How The Witcher 3 Built Its Cities \| Environment Breakdown](https://www.youtube.com/watch?v=cCovMWRSL6o) `cCovMWRSL6o` | Next Level Game Art | 20:52 | auto | 3483 | NOVÁ `praxe/modularni-kity.md` | „Beauclair" (orientační body a clony, 500 MB textur, streamování LODů, Umbra, jeden vertex-blend shader na čtvrť s texture arrays, deco balíčky); kurz a partnerský web v Pozn. |
| published | [How 30 Devs Made One of 2026's Best Looking Games \| Mortal Shell 2](https://www.youtube.com/watch?v=SleW5iuwyIA) `SleW5iuwyIA` | Next Level Game Art | 20:41 | auto | 3490 | NOVÁ `praxe/modularni-kity.md` | „Mortal Shell 2" (Nanite a kity, málo tilerů a víc než 25 LUTů, nástroje z Fabu, kompaktní svět, cizí měření Lumenu a VRAM, varování pro absolventy); prodejní čísla v titulcích nečitelná, vynechána; kurz a partner v Pozn. |
| published | [How 007 First Light Is Built Inside the Editor](https://www.youtube.com/watch?v=T4JStuqxUPI) `T4JStuqxUPI` | Next Level Game Art | 14:20 | auto | 2188 | NOVÁ `praxe/env-technika.md` | „007 First Light" (entity, template, brick; trunk-based vývoj a build editoru každých 15–30 min; GI bez HW RT; Smolder s OIT; Houdini nástroje); barel → backlink do `pasti-a-mechaniky` |
| published | [3 Invisible Systems Secretly Running Alan Wake 2](https://www.youtube.com/watch?v=zOlvns5pEZM) `zOlvns5pEZM` | Next Level Game Art | 17:04 | auto | 2517 | NOVÁ `praxe/env-technika.md` | „Alan Wake 2" (spouštěče na zemi, stopy, wind boxy nad SDF, vegetace skinovaná na GPU, meshlety a culling po stupních, mlha přes MBOIT); backlink do `footsteps` |
| published | [Tricks Behind AC Black Flag Resynced's Materials and Tech](https://www.youtube.com/watch?v=MF_wkqanBFI) `MF_wkqanBFI` | Next Level Game Art | 11:22 | auto | 1653 | NOVÁ `praxe/env-technika.md` | „AC Black Flag Resynced" (páry materiálů, obecná knihovna, trimy a mesh decaly, zdi z Houdini simulace, falešné interiéry, vlny u břehu) |

### Dávka 53 — Světlo a materiály · `hotovo`

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [Artist's Guide to Using MegaLights in Unreal Engine 5.8 \| Inside Unreal](https://www.youtube.com/watch?v=Nrb17mtBJPM) `Nrb17mtBJPM` | Unreal Engine | 166:35 | auto | 30920 | NOVÁ `praxe/megalights.md` | NOVÁ kapitola, 5 myšlenek: rozpočet vzorků na pixel (co nahrazuje, cena = rozlišení, demo 200 světel, podmínky, kdy ne) · attenuation radius jako hlavní páka (překryvy, kalibrace, smart light BP, diagnostika) · svítidlo z víc světel (source radius, rect lights, light channels a IES v 5.8, ~30 světel na auto) · slunce bez MegaLights (importance, VSM, měsíc) · expozice, která drží (kalibrace, local exposure, dva modely světla); řečníci jen jako role; Fab showcase v Pozn. |
| published | [How to Create Fake Windows in Unreal Engine 5 \| Fake 3D Interior](https://www.youtube.com/watch?v=OftM6QfMLtk) `OftM6QfMLtk` | Zima Env | 8:07 | auto | 941 | `praxe/materialy.md` | +1 „Falešné okno" (Interior Cubemap, špína a emisiv za static switchem, cube textura ze Scene Capture Cube); spárováno s AC Black Flag v `env-technika` |
| published | [How to Make PSX-Style Fog in Unreal Engine 5](https://www.youtube.com/watch?v=6i5hk_9whpE) `6i5hk_9whpE` | Eremental Studios | 15:14 | auto | 2235 | `praxe/ps1-estetika.md` | +1 „PS1 v enginu" (s `UFX-DwosKUM`): mlha jako post-process materiál (vzdálenost + Perlin šum, Infinite Extent PPV); promo vlastních projektů na Fabu, Gumroad a Discord v Pozn. |
| published | [Pixelated Effect on Any Material in Unreal Engine 5 \| Material Tutorial](https://www.youtube.com/watch?v=UFX-DwosKUM) `UFX-DwosKUM` | Zima Env | 1:39 | auto | 241 | `praxe/ps1-estetika.md` | pixelizace UV (Floor) v myšlence „PS1 v enginu", i pro Niagaru |
| published | [Landscape Lab #01 — The Perfect POM + Contact Shadows Combo in Unreal Engine 5](https://www.youtube.com/watch?v=gxk2ulmlkX8) `gxk2ulmlkX8` | Gatyh Interactive | 20:55 | auto | 4243 | `praxe/landscape-tipy.md` | +1 „Hloubka bez geometrie" (s `c9WhNdNLheY`): near/far tiling, POM node, contact shadows přes pixel depth offset a ShadowPassSwitch; vlastní texture packer a CC0 web v Pozn. |
| published | [NEXT-GEN Real-Time Displacement \| IHP for Unreal Engine](https://www.youtube.com/watch?v=c9WhNdNLheY) `c9WhNdNLheY` | Denizcan Gok | 15:01 | manual | 1721 | `praxe/landscape-tipy.md` | IHP v myšlence „Hloubka bez geometrie": nastavení výškové textury, IHP Standard node, parametry; FLAG: vývojářův vlastní plugin, výkon jen z jeho scény (bez srovnání bez efektu) |

### Dávka 54 — PCG, terén, povrchy a velké světy · `hotovo`

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [Procedural Cities for Tech Artists: Geometry Scripting & PCG \| Unreal Fest Chicago 2026](https://www.youtube.com/watch?v=7uuFPOKIw8I) `7uuFPOKIw8I` | Unreal Engine | 43:43 | auto | 7301 | NOVÁ `praxe/pcg-mesta.md` | NOVÁ kapitola, 5 myšlenek: budova jako věta (panelové kity, grammar string, patra a strany, sklo přes sockety, střechy z Geometry Scriptu, zaoblené nároží) · variabilita z dat (sockety a čtvrti, barvy instancí, presety pod gameplay tagy, OSM) · interiér z bodů (místnosti jako subgrafy, devět uzlů, parallax okna) · blok napřed, silnice potom (block processor, material spline cuts, booleany a vertex color, world tiles, snap na terén, adaptivní panely, značení) · nástroj pro artisty (pluginy, bake v EUW, Run Construction Script on Drag, debug compute meshů, PCG profiler, UX). Řečníci jen jako tým tech artů Lucid Games |
| published | [Volumetric Sampling In PCG Is a LOT More Powerful Than You Think](https://www.youtube.com/watch?v=mgurlPTz__E) `mgurlPTz__E` | Procedural Minds | 21:48 | auto | 4517 | `praxe/pcg-liany.md` | +1 „Podlaha, stěny a strop jedním grafem" (World Volumetric Query, World Raycast, Normal To Density podle směru, Spatial Noise shluky, Copy Points grid, pasti trace complex); Patreon v Pozn. |
| published | [Building Open World Forests: The Fastest Way in UE5](https://www.youtube.com/watch?v=ufZrhbZWPto) `ufZrhbZWPto` | Aziel Arts | 39:52 | auto | 8289 | `praxe/pcg-vegetace.md` | +1 „Les pro otevřený svět" (onload vs. runtime skupina, biome map, hustota a spatial noise, CPU kvůli kolizi a PCG stamp, runtime + partitioned a grid size, contact shadows, spline masky); FLAG: autorův nástroj QuickScatter a akademie |
| published | [Introducing Mesh Terrain: Craft Large Complex Worlds \| Unreal Fest Chicago 2026](https://www.youtube.com/watch?v=QJwTTmNez3k) `QJwTTmNez3k` | Unreal Engine | 47:40 | auto | 7682 | `praxe/mesh-terrain.md` | +2 „Proč trojúhelníky a ne voxely" (pouta height map, proč ne voxely, mesh partition, zdroj → mezivrstva → runtime, transformers a build variants, kolize 59× a −90 %, RVT nestihlo 5.8, výkon na datech Fortnite, experimental → produkce konec 2027) a „Modifikátory v rukou Epicu" (pořadí vrstev, sub-priorita, outliner do bodu, vertex colory → kanály, modifikátor jako komponenta na POI, PCG Mesh Projection Instance Spawner); úvod a warning box aktualizovány |
| published | [Supercharging my procedural mountain forest](https://www.youtube.com/watch?v=ACjlgxRp69c) `ACjlgxRp69c` | runevision | 18:01 | manual | 2355 | `praxe/velke-svety.md` | +1 „Dohled na kilometry" (Burst 3×, LOD vrstvy generování 5×5 s 2× chunky, skirts, LayerProcGen, octahedral impostory se stínem, eroze a sdílený kód CPU/GPU, fixed point a origin shifting v 8 000 km, aerial perspective do bíla); mimo UE, mosty do UE v Pozn. |
| published | [Footstep VFX by Surface Type in Unreal Engine 5 (Niagara)](https://www.youtube.com/watch?v=RsI8O7Guz4s) `RsI8O7Guz4s` | Tank Control Games | 17:57 | auto | 3394 | `praxe/footsteps.md` | +1 „Částice podle povrchu" (trace z chodidla místo kapsle, Select systému podle povrchu, Make Rot from Z, Intensity přes custom HLSL a Map Range podle rychlosti); Pozn.: Manual Release vs. doporučení Epicu (auto release) z `niagara-vykon`, NDC jako škálovatelná verze |
| published | [UE5 Surface Deformation Tutorial \| Real-Time Snow & Ground Depth (Render Target, RVT, VHM)](https://www.youtube.com/watch?v=QWONTiw68OU) `QWONTiw68OU` | Tank Control Games | 28:10 | auto | 5479 | `praxe/footsteps.md` | +1 „Stopy do hloubky" (render target jako plátno, štětec Additive/Unlit, VHM + RVT, WPO podle plátna, přepočet do UV a metrů, kreslení jen při pohybu); zastaralá Pozn. v „Stopy jako decaly" aktualizována |

### Dávka 55 — AI nástroje: MCP, agenti a AI animace · `hotovo`

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [From Words to Worlds: Integrating MCP into the Unreal Editor \| Unreal Fest Chicago 2026](https://www.youtube.com/watch?v=lDf_y-YPELo) `lDf_y-YPELo` | Unreal Engine | 36:40 | auto | 6178 | NOVÁ `praxe/mcp-v-editoru.md` | NOVÁ kapitola, 2 myšlenky z přednášky: asistent, ne zázrak (tři principy, PCG jako prostorový jazyk, tool sets + PCG primitiva + příklady + skills, obývák a město za den, lighting skill se screenshoty, technical artist jako klíč) · vlastní tool set a skill (reflexe → JSON schema/data, UFunctions i v Pythonu, čtyři pravidla tool setu a čtyři pravidla skillu, statické a dynamické příklady). Jména tříd jen mluveně → neuvedena; přednášející jako role |
| published | [Getting Started with MCP in Unreal Engine 5.8 I Epic Games Education Webinar](https://www.youtube.com/watch?v=k0tgmrBuIJc) `k0tgmrBuIJc` | Unreal Engine | 60:52 | auto | 9293 | NOVÁ `praxe/mcp-v-editoru.md` | 2 myšlenky: rozjet MCP (tři pluginy včetně All Tool Sets a Editor Tool Set, Auto Start, client config, agent z kořene projektu, port, troubleshooting, MCP Inspector, limity) · jak s agentem mluvit (konkrétnost, čtyři návyky, kontextové okno a velikost popisů tool setů, harness, tokeny podle plánu, co agent nesvede: HLSL místo uzlů, delaye místo Timeline, build proti Event Ticku). Napětí s trojicí pluginů v `claude-code-ue` v Pozn. |
| published | [Agentic Development in Unreal Engine with Rider \| Unreal Fest Chicago 2026](https://www.youtube.com/watch?v=0C7GjShUnlY) `0C7GjShUnlY` | Unreal Engine | 24:55 | auto | 3026 | NOVÁ `praxe/mcp-v-editoru.md` | 1 myšlenka: agent v IDE (generický agent čte projekt jako text, index a debugger pro agenty, srovnání 5 potomků za ~10 s a 18 assetů za 38 s, kontroly kódu, Rider Kit přes ACP v editoru, vidění a simulace vstupů, výkon indexace a debuggeru); FLAG: prezentace výrobce, popis slibuje víc (GAS, build triage, DataTables), než záznam ukazuje |
| published | [New Absolute King of 3D & Blender - GPT-6 Astra](https://www.youtube.com/watch?v=8MUk-tQTiwE) `8MUk-tQTiwE` | Stefan 3D AI | 14:08 | manual | 2709 | `praxe/claude-code-ue.md` | +1 „MCP místo klikání" (computer use pomalé, MCP dál; postavy z primitiv ne, mesh z 3D AI ano; blocking → detail; rig s IK; auto z výkresů s nesrovnalostmi; jedna scéna z 3D AI, ne procedurální; limity předplatného); FLAG: hype, affiliate Higgsfield, kurzy |
| published | [Unreal Engine’s NEW AI Animation System Is Crazy (UE5)](https://www.youtube.com/watch?v=vksuxAECgI8) `vksuxAECgI8` | Smart Poly | 10:07 | auto | 1888 | `praxe/ai-assety.md` | +1 „Animace z modelu přímo ve hře" (s `6NYC4ryO9ik`, `lj-xPo7ueGA`, `wknRD5g-vvk`): AnimGen sample (NPC styly, celý walk cycle, ~40 stylů), autorova nejistota o tréninku vyvrácená Epicem; kurzy autora v Pozn. |
| published | [Free and Local Real-Time AI Animation - NVIDIA MotionBricks.cpp](https://www.youtube.com/watch?v=lj-xPo7ueGA) `lj-xPo7ueGA` | Stefan 3D AI | 7:19 | manual | 1320 | `praxe/ai-assety.md` | MotionBricks.cpp v myšlence „Animace z modelu přímo ve hře": predikce pohybu místo animačního systému, smart primitives zatím ne, CPU spíš výzkumně, ~30 snímků a škálování na 60; FLAG: sponzor Higgsfield |
| published | [NVIDIA Kimodo Now Runs Without a GPU - Free Local Workflow](https://www.youtube.com/watch?v=wknRD5g-vvk) `wknRD5g-vvk` | Stefan 3D AI | 6:45 | auto | 1275 | `praxe/ai-assety.md` | Kimodo.cpp v myšlence „Animace z modelu přímo ve hře": CPU a 2 GB VRAM, 3 s animace až 5 min, licence koster (SMPL-X ne, SOMA/G1 ano), GLB, retarget přes Mixamo, chybí prsty; autorův kurz v Pozn. |
| published | [Create a FREE 2D Parallax System Using AI ( Game Ready )](https://www.youtube.com/watch?v=4_u5Ues1zPY) `4_u5Ues1zPY` | Iris Ogli - Modeling, AI Animation & Game Assets | 3:46 | manual | 528 | `teorie/2d-vizual.md` | doplněk v „Layering a verticalita": jedna scéna se zamčenou kamerou a horizontem → oddělené vrstvy se stejnou perspektivou → průhledná PNG; promo (prompty na webu kanálu) |
| skip | [World Modeling and Vibe Simulation with Unreal Engine \| Unreal Fest Chicago 2026](https://www.youtube.com/watch?v=v6QujSBg4Xw) `v6QujSBg4Xw` | Unreal Engine | 48:42 | auto | 8925 | — | světové modely a syntetická data pro robotiku (Duality) — mimo gamedev |
| skip | [Getting Started with the Unreal Engine HMI Template and Data Reduction Pipeline](https://www.youtube.com/watch?v=fyjkR6YDjvM) `fyjkR6YDjvM` | Unreal Engine | 42:18 | auto | 6280 | — | automotive HMI šablona (Epic + Qualcomm) — mimo gamedev; s UI souvisí jen vzdáleně (binding signálů na widgety) |

### Dávka 56 — Teorie: příběh, plánování, design a level design · `hotovo`

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| published | [If You Can't Answer These 6 Questions You Don't Have A Story - Glenn Gers](https://www.youtube.com/watch?v=uL0atQFZzL8) `uL0atQFZzL8` | Film Courage | 14:57 | manual | 2677 | `teorie/pribeh-a-postavy.md` | +1 „Šest otázek, bez kterých nemáš příběh" (postava se záměrem a překážkou, šest otázek, konec jako první nový čin, proces po krátkých dávkách, placeholder scéna); Gersův vlastní kanál v Pozn. |
| published | [The Breakdown Method: The Secret to Finishing Your Game](https://www.youtube.com/watch?v=wAe6b3IpSh0) `wAe6b3IpSh0` | Unreal University | 7:51 | auto | 1711 | `teorie/planovani-nastroje.md` | +1 „Hora po kamenech" (proč se hry nedodělávají, rozpad na kusy na jedno sezení, příklad s lodí, týdenní otázka místo vrcholu); FLAG: kurz zdarma 3× |
| published | [5 things I wish I knew before I started Unreal Engine](https://www.youtube.com/watch?v=pMziF4jpejo) `pMziF4jpejo` | Unreal University | 7:02 | auto | 1272 | `teorie/jak-se-ucit-kodovat.md` | doplněk v „Aktivní sledování" (Minute Monkey, chyby jako opakování, hloubka před šířkou, Fab, pravidelnost proti vyhoření); překryv se staršími radami téhož autora v `praxe/editor-tipy` → jen nové důrazy |
| published | [You can create any game mechanic once you understand this](https://www.youtube.com/watch?v=vZkAbeMLcvc) `vZkAbeMLcvc` | PtroDev | 10:54 | auto | 1777 | `teorie/systemy-a-mechaniky.md` | +1 „Pět kostek každé mechaniky" (truhla, dveře, plošina, tlačítko, checkpoint, NPC, kulka, nepřítel, grappling hook; pět otázek); UE a Godot protějšky v Pozn. |
| published | [The infinite potential of Conway's Game Of Life](https://www.youtube.com/watch?v=SQitnzjr8tc) `SQitnzjr8tc` | Ominous Dev | 6:17 | auto | 1160 | `teorie/algoritmy-prehled.md` | doplněk v „Emergence, žíhání a kabinet kuriozit" (von Neumann → Conway, tři pravidla, útvary, Turingova úplnost, víc pravidel = restriktivnější); most do `systemy-a-mechaniky` |
| published | [Spawn Closets in Video Game Level Design](https://www.youtube.com/watch?v=YjZVo8RO0xQ) `YjZVo8RO0xQ` | timdoesleveldesign (TimDoesLevelDesign) | 6:07 | manual | 1097 | `teorie/prostor-a-hranice.md` | +1 „Spawn closet" (rozpočet aktivních nepřátel, Doom, Half-Life 2, Star Wars Outlaws, proč ne spawn z ničeho, Dead Island 2, Far Cry, ARC Raiders) |
| published | [How was Cyberpunk 2077 created?](https://www.youtube.com/watch?v=G_te2IkVVi4) `G_te2IkVVi4` | ByteSeb | 30:04 | auto | 4618 | `teorie/vydani-hry.md` | +1 „Cyberpunk 2077: launch, který se rozbil, a roky oprav" (dvakrát od nuly, engine souběžně, 500 lidí, odklady a crunch, Sony, akcie, opravy až 2.0 a Phantom Liberty, přechod na UE5; řemeslo: urbanistika, kity, diegetický HUD, interiéry, cut content); FLAG: sekundární zdroj se spekulacemi, příběhové spekulace vynechány; backlinky z `ui-ve-svete` a `blockout` |

### Low-priority a skip mimo dávky

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| todo-lp | [Unreal Engine 5.8.2 Beginner Tutorial - UE5 Starter Course 2026#unrealengine5 #megascans #cgi](https://www.youtube.com/watch?v=LqOKsVmy2Rc) `LqOKsVmy2Rc` | Magnet VFX | 67:51 | auto | 10257 | — | LOW-PRIORITY: Magnet VFX, průchod stavbou prostředí 68 min (jako `FAo9nfWYPSE`) |
| todo-lp | [Unreal Engine 5.8 Beginner Tutorial - UE5 Starter Course 2026#unrealengine5 #megascans #cgi](https://www.youtube.com/watch?v=oDXCx2i17DQ) `oDXCx2i17DQ` | Magnet VFX | 67:47 | auto | 9167 | — | LOW-PRIORITY: Magnet VFX, průchod stavbou prostředí a MetaHuman animací 68 min (jako `FAo9nfWYPSE`) |
| todo-lp | [Create Next-Gen Dynamic Environments In Unreal Engine 5 - Shallow Water River, Megaplants & more!](https://www.youtube.com/watch?v=-KMBEjaVp3M) `-KMBEjaVp3M` | pinkpocketTV | 16:00 | auto | 2158 | — | LOW-PRIORITY: začátečnický průchod (shallow water řeka, megaplants) — obsah už mají `interaktivni-voda.md` a `pcg-vegetace.md` |
| skip | [1989 WALK THROUGH FIRE // Synthwave, Cyberpunk, Retrowave](https://www.youtube.com/watch?v=dflqyI2KXp0) `dflqyI2KXp0` | Moebius FM | 125:27 | auto | 150 | — | dvouhodinový synthwave mix bez mluveného slova (přepis = „Heat. Heat.“) |
