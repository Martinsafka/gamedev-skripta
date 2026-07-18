# Processing Index

Per-video status tracker for the whole playlist — created in the Phase 2 taxonomy. **Update the status column whenever a video is processed.** Chapter slugs are working titles for grouping; final chapter names/files are decided at synthesis time. Téma tree **approved by user 2026-07-09** (incl. „Rešerše: slovanská mytologie" and the skip/low-priority flags); re-assigning individual videos later is cheap (nav-only change).

Legend: status `todo / drafted / published / skip` · track `manual / auto / —` (— = no English subtitle track, "bez přepisu") · slova = word count of the cleaned transcript.

**Stats (hlavní playlist):** 210 videos (31 Teorie, 179 Praxe) · 202 published (pilot + batch 1–19) · 7 bez přepisu · 5 skip (news/promo) + 2 low-priority (beginner courses). **Phase 3 komplet — zbývá: 2 low-priority kurzy + 1 CS video (čeká na cs-subtitle pipeline).**

**Phase 7 (samostatný playlist „Gamedev-music"):** 17 videí, **všech 17 published** v dokumentu „Hudba a zvuk" (tabulka na konci souboru).

**Druhá vlna hlavního playlistu (+116 videí, staženo 2026-07-17):** taxonomie **schválena 2026-07-18** — kompletní tabulky v sekci „Druhá vlna" na konci souboru; tam běží i statusy dávek (20–30). Rozložení: 86 Teorie (z toho 6 nových témat) · 27 Praxe · 3 Hudba; ~512k slov přepisů; 2 bez přepisu; 2 nové low-priority beginner kurzy. **Strom schválen uživatelem 2026-07-18.** Stav: **38/116 published (dávky 20–22)**, 76 todo + 2 todo-lp. T-DESIGN split proveden: nav téma „Design do hloubky" (obtiznost, systemy-a-mechaniky, ludonarativni-soulad; dávkou 23 přibudou zanry, engineering-experiences, pripadovky-designu, horor-design, kamera).

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
| published | [From AI to Metahuman - Best New UE 5.8 Workflow for Custom Character](https://www.youtube.com/watch?v=4w7oA4oJMqs) `4w7oA4oJMqs` | Stefan 3D AI | 28:22 | manual | 5415 | `ai-assety` | → MetaHuman 5.8 |
| published | [I Built a Modular Character with AI (Full Workflow)](https://www.youtube.com/watch?v=gZIxrX1n2D4) `gZIxrX1n2D4` | Stefan 3D AI | 26:54 | manual | 5047 | `ai-assety` | modulární postava |
| published | [Claude Took Over ComfyUI + Blender: Here's What Happened](https://www.youtube.com/watch?v=KdYv_TT-ZnQ) `KdYv_TT-ZnQ` | PixelArtistry | 23:07 | auto | 4860 | `claude-code-ue` | ComfyUI+Blender; slug → claude-code-ue |
| published | [From AI to Playable 3D Character in Unreal Engine](https://www.youtube.com/watch?v=k1xBERhXtHA) `k1xBERhXtHA` | Stefan 3D AI | 22:04 | manual | 4195 | `ai-assety` | hratelná postava tandem |
| published | [Next-Gen 3D AI Is Here (5-Second Game-Ready Models)](https://www.youtube.com/watch?v=mXjUz3viYmQ) `mXjUz3viYmQ` | Stefan 3D AI | 19:48 | manual | 3282 | `ai-assety` | Tripo vs Hunyuan vs Rodin |
| published | [Complete Free AI Workflow for Game-Ready 3D Characters](https://www.youtube.com/watch?v=TkP-_LyacMI) `TkP-_LyacMI` | Stefan 3D AI | 12:09 | manual | 2316 | `ai-assety` | free pipeline |
| published | [Make infinite characters in the SAME style!](https://www.youtube.com/watch?v=LcJQQwltQ2Q) `LcJQQwltQ2Q` | PixelLab | 11:06 | auto | 1744 | `ai-assety` | 2D styl konzistence (PixelLab) |
| published | [From Dialogue to Action: Create Scene-Aware AI Characters That Act AND React \| Convai Unreal Engine](https://www.youtube.com/watch?v=lB5_KRWdg_w) `lB5_KRWdg_w` | Convai | 5:20 | auto | 889 | `claude-code-ue` | produkt Convai; slug → claude-code-ue |
| published | [I Built My Dream Game in 72 Hours — Assets by AI, Gameplay by Claude Code](https://www.youtube.com/watch?v=k9cbm5jSOxk) `k9cbm5jSOxk` | Stefan 3D AI | 35:14 | manual | 5619 | `claude-code-ue` | hra za 72 h (capstone) |
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
| skip | [Unreal Engine 5.8 Feature Highlights](https://www.youtube.com/watch?v=ExFF5gXVhDU) `ExFF5gXVhDU` | Unreal Engine | 3:26 | manual | 359 | `novinky` | novinkové video — přeskočit? |

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

## Druhá vlna hlavního playlistu (+116) · Phase 8 _(strom schválen 2026-07-18; dávky 20–22 published)_

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
| todo | [What Do "Professional" Game Design Documents Look Like? 📜](https://www.youtube.com/watch?v=fk-rQlrNYZ8) `fk-rQlrNYZ8` | Indie Game Clinic | 41:21 | auto | 7826 | `teorie/gdd.md` | jak vypadají profesionální GDD |
| todo | [Game Design Documents - a Minimalist Approach 🧘🏽](https://www.youtube.com/watch?v=uBxYGFRi-S4) `uBxYGFRi-S4` | Indie Game Clinic | 37:44 | manual | 7296 | `teorie/gdd.md` | minimalistický přístup; cross-link zápisek gdd-review |
| todo | [How to find amazing game ideas](https://www.youtube.com/watch?v=0m60QbT85Tc) `0m60QbT85Tc` | Game Maker's Toolkit | 27:09 | manual | 4856 | `teorie/napad.md` | rozšíření (GMTK) |
| todo | [The Secret to GOOD Game Ideas 💡 [Practical Ideation Methods Explained]](https://www.youtube.com/watch?v=LMOCQNcMleg) `LMOCQNcMleg` | Indie Game Clinic | 24:29 | auto | 4622 | `teorie/napad.md` | rozšíření (IGC ideation) |
| todo | [Manage Your GameDev Projects with Trello/Kanban](https://www.youtube.com/watch?v=-SqcrlAarGo) `-SqcrlAarGo` | Indie Game Clinic | 22:33 | auto | 4741 | `teorie/planovani-nastroje.md` | Trello/Kanban |
| todo | [The ULTIMATE Playtest Guide](https://www.youtube.com/watch?v=zXNRJuc48Ek) `zXNRJuc48Ek` | Indie Game Clinic | 39:27 | auto | 7549 | `teorie/playtesting.md` | pozn. sponzor GameMaker segment |
| todo | [GameDev as an Iterative Spiral](https://www.youtube.com/watch?v=9L6XX9kDQyA) `9L6XX9kDQyA` | Indie Game Clinic | 12:30 | auto | 2656 | `teorie/prototypovani.md` | rozšíření: iterační spirála |
| todo | [9 Months of Dev… Pivot or Perish?](https://www.youtube.com/watch?v=CbWpsNs7nrg) `CbWpsNs7nrg` | Indie Game Clinic | 28:57 | auto | 6003 | `teorie/scope.md` | pivot po 9 měsících |
| todo | [Stopping Scope Creep without Crushing Creativity (Stream Highlights)](https://www.youtube.com/watch?v=Xyl3tsZx4wQ) `Xyl3tsZx4wQ` | Indie Game Clinic | 10:02 | auto | 2113 | `teorie/scope.md` | rozšíření: scope creep |
| todo | [How I Made A Steam Game In Only 1 Month](https://www.youtube.com/watch?v=7naIKclU1A4) `7naIKclU1A4` | Zoteling | 6:53 | auto | 1470 | `teorie/scope.md` | devlog: hra za měsíc |
| todo | [How To Make Small Games \| Indie Game Dev Tutorial](https://www.youtube.com/watch?v=U-j91fw648Q) `U-j91fw648Q` | RETRODEAD | 5:27 | auto | 1399 | `teorie/scope.md` | malé hry |

### Základy designu · `T-DESIGN` (+18)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| todo | [Tynan Sylvester - Designing Games, A Guide to Engineering Experiences (GDL ep07)](https://www.youtube.com/watch?v=RFSxLRBht14) `RFSxLRBht14` | Indie Game Clinic | 95:02 | auto | 20346 | `teorie/engineering-experiences.md` | Tynan Sylvester — kniha Designing Games (95 min) |
| published | [INDIE Game DevLog - Why GOOD Combat Is So HARD To Make (June 2026)](https://www.youtube.com/watch?v=NYqyAL7FKYg) `NYqyAL7FKYg` | SILKROAD Project | 15:20 | manual | 2843 | `teorie/game-feel.md` | devlog: proč je dobrý combat těžký · dávka 22 |
| published | [10 Ways to Improve Game Feel](https://www.youtube.com/watch?v=qCj9CZoAvFY) `qCj9CZoAvFY` | Design Diary | 10:37 | auto | 2078 | `teorie/game-feel.md` | rozšíření: 10 způsobů · dávka 22 |
| todo | [How To Create A Horror Game That SCARES](https://www.youtube.com/watch?v=JVTWbRMHYeY) `JVTWbRMHYeY` | Devilish Inks | 37:17 | auto | 8040 | `teorie/horor-design.md` | jak vyvolat strach |
| todo | [How Metroidvania Cameras are Shockingly Different than Platformer Cameras](https://www.youtube.com/watch?v=drbatB2KWlo) `drbatB2KWlo` | Inbound Shovel | 20:33 | auto | 4929 | `teorie/kamera.md` | metroidvania vs. platformer kamery |
| published | [LUDOTHEMATICS: Harmony and Dissonance in Game Design](https://www.youtube.com/watch?v=uG-RPNilP-8) `uG-RPNilP-8` | Indie Game Clinic | 39:24 | auto | 7769 | `teorie/ludonarativni-soulad.md` | ludothematics: harmonie a disonance · dávka 22 |
| published | [Challenge & Difficulty in Game Design](https://www.youtube.com/watch?v=FLCet4Z7zew) `FLCet4Z7zew` | Indie Game Clinic | 49:58 | auto | 9741 | `teorie/obtiznost.md` | challenge & difficulty (IGC, 50 min) · dávka 22 |
| published | [This Puzzle Platformer Has a Unique Approach to Difficulty [Octojump]](https://www.youtube.com/watch?v=IcSD7w-fdJ8) `IcSD7w-fdJ8` | Indie Game Clinic | 6:28 | auto | 1172 | `teorie/obtiznost.md` | případovka Octojump · dávka 22 |
| todo | [Indie Soulsborne "Fade: The First Chapter" - Game Design Deep-Dive](https://www.youtube.com/watch?v=cIi-mgZUELE) `cIi-mgZUELE` | Indie Game Clinic | 28:09 | auto | 4574 | `teorie/pripadovky-designu.md` | soulsborne Fade deep-dive |
| todo | [I Played 150 of Your Games; Common Problems (and Solutions!)](https://www.youtube.com/watch?v=8bYnlOE_pl0) `8bYnlOE_pl0` | Indie Game Clinic | 21:26 | manual | 4078 | `teorie/pripadovky-designu.md` | 150 her — časté problémy |
| published | [Game Mechanics & Systems Thinking](https://www.youtube.com/watch?v=nkLmjJK3vOw) `nkLmjJK3vOw` | Indie Game Clinic | 40:49 | auto | 7443 | `teorie/systemy-a-mechaniky.md` | cross-link smycky-a-retezce · dávka 22 |
| published | [What is Fun? A Game Design Introduction](https://www.youtube.com/watch?v=56ENqlUST9U) `56ENqlUST9U` | Indie Game Clinic | 31:10 | manual | 4766 | `teorie/zabava.md` | rozšíření: What is Fun (IGC) · dávka 22 |
| published | [Game Design Theory: A Guided Tour](https://www.youtube.com/watch?v=TATKLd1Q6ho) `TATKLd1Q6ho` | Indie Game Clinic | 31:14 | auto | 5423 | `teorie/zaklady.md` | přehled teorií designu (IGC) · dávka 22 |
| published | [How To Think Like A Game Designer](https://www.youtube.com/watch?v=iIOIT3dCy5w) `iIOIT3dCy5w` | Game Maker's Toolkit | 13:06 | manual | 2245 | `teorie/zaklady.md` | rozšíření (GMTK) · dávka 22 |
| published | [The 10 Basic Principles of Game Design Every Indie Dev Should Know](https://www.youtube.com/watch?v=5Fk7p-f2ymY) `5Fk7p-f2ymY` | NOBL Games | 12:18 | auto | 1822 | `teorie/zaklady.md` | 10 principů · dávka 22 |
| todo | [Game Genres - a Design Perspective](https://www.youtube.com/watch?v=3KJbYdNP5js) `3KJbYdNP5js` | Indie Game Clinic | 38:00 | auto | 7937 | `teorie/zanry.md` | žánry očima designu |
| todo | [Indie Game Genres & Subtractive Design](https://www.youtube.com/watch?v=RkcmljWlvrs) `RkcmljWlvrs` | Indie Game Clinic | 21:41 | manual | 3713 | `teorie/zanry.md` | subtraktivní design |
| todo | [Become a Game Dev NECROMANCER!!!](https://www.youtube.com/watch?v=nN5VEvl9fik) `nN5VEvl9fik` | Indie Game Clinic | 16:03 | auto | 3179 | `teorie/zanry.md` | mrtvé žánry (nekromancie) |

### Level design · `T-LEVEL` (+4)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| todo | [Level Design Approaches for Solo Devs](https://www.youtube.com/watch?v=OLXn6YYAk7M) `OLXn6YYAk7M` | Indie Game Clinic | 20:45 | auto | 4162 | `teorie/level-design-solo.md` | přístupy pro sólo vývojáře |
| todo | [Game vs Level Design [explained with Golf and Robots]](https://www.youtube.com/watch?v=R7N1XUKL5JE) `R7N1XUKL5JE` | Indie Game Clinic | 19:40 | auto | 3301 | `teorie/level-design-solo.md` | game design vs. level design |
| todo | [Creating an In-Game Level Editor \| Indie Devlog #9](https://www.youtube.com/watch?v=nAXMHOWliAA) `nAXMHOWliAA` | Game Endeavor | 8:12 | manual | 2063 | `teorie/nastroje-na-levely.md` | devlog in-game editor; tenké — merge kandidát |
| todo | [Environmental Storytelling Explained [Stray, Gone Home, Amnesia, Unpacking, Minit]](https://www.youtube.com/watch?v=sSFs61IF2Rs) `sSFs61IF2Rs` | Indie Game Clinic | 23:06 | auto | 4568 | `teorie/prostor-vypravi.md` | environmental storytelling; cross-link env-breakdowny |

### Vydání a marketing · `T-MARKET` (+6)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| todo | [Game Marketing Advice with Chris Z](https://www.youtube.com/watch?v=O7GoWKwEwIk) `O7GoWKwEwIk` | Indie Game Clinic | 49:07 | auto | 10853 | `teorie/co-prodava.md` | rozšíření: rozhovor Chris Z (49 min) |
| todo | [What Makes a Successful Game?](https://www.youtube.com/watch?v=nO9HMnuZO78) `nO9HMnuZO78` | Indie Game Clinic | 11:23 | auto | 2507 | `teorie/co-prodava.md` | rozšíření: co dělá hru úspěšnou |
| todo | [Roasting Steam Pages with a Marketing Expert](https://www.youtube.com/watch?v=8gY9SU9ShOw) `8gY9SU9ShOw` | Indie Game Clinic | 68:45 | auto | 14515 | `teorie/steam-stranka.md` | rozšíření: roasting s marketérem (69 min) |
| todo | [How To Write Marketing Copy For Your Game](https://www.youtube.com/watch?v=m5X_ZYXVpQE) `m5X_ZYXVpQE` | Indie Game Clinic | 24:59 | auto | 5246 | `teorie/steam-stranka.md` | rozšíření: marketingová copy |
| todo | [What nobody tells you about releasing a game on Steam...](https://www.youtube.com/watch?v=uQnIkK6BOLQ) `uQnIkK6BOLQ` | BiteMe Games | 21:34 | auto | 4874 | `teorie/vydani-hry.md` | co nikdo neřekne o vydání na Steamu |
| todo | [Most Steam Demos Suck; Here's Why](https://www.youtube.com/watch?v=1vtqBTX2Lzc) `1vtqBTX2Lzc` | Indie Game Clinic | 18:35 | auto | 3540 | `teorie/vydani-hry.md` | proč většina dem nefunguje |

### Byznys, data a kariéra · `T-BIZ` (+6) ⭐ NOVÉ TÉMA

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| todo | [I Analysed 62,000 Indie Developers. Here's What Actually Predicts Success](https://www.youtube.com/watch?v=WueQ75GP1wc) `WueQ75GP1wc` | Game Oracle | 16:07 | auto | 2660 | `teorie/data-o-uspechu.md` | 62k vývojářů — co predikuje úspěch |
| todo | [I Scraped the Entire Steam Catalog, Here’s the Data](https://www.youtube.com/watch?v=qiNv3qv-YbU) `qiNv3qv-YbU` | Newbie Indie Game Dev | 11:28 | manual | 2101 | `teorie/data-o-uspechu.md` | scrape celého Steam katalogu |
| todo | [Ultimate gamedev funding tierlist](https://www.youtube.com/watch?v=qjyPRnzlx8A) `qjyPRnzlx8A` | BiteMe Games | 40:06 | auto | 9139 | `teorie/financovani.md` | tierlist zdrojů financování (40 min) |
| todo | [How To Make Indie Games In 2026 w/ Jonathan Blow — Full Time Game Dev Podcast Ep. 061](https://www.youtube.com/watch?v=yNdRv5LFuQk) `yNdRv5LFuQk` | Thomas Brush | 96:41 | auto | 20137 | `teorie/indie-kariera.md` | podcast Jonathan Blow (97 min) |
| todo | [When is an Indie Game Not an Indie Game?](https://www.youtube.com/watch?v=CyX41iR08Pc) `CyX41iR08Pc` | Indie Game Clinic | 9:58 | auto | 2040 | `teorie/indie-kariera.md` | kdy indie není indie |
| todo | [How BiteMe Games Survived 4 Years Without a Viral Game](https://www.youtube.com/watch?v=KehpqxUfz60) `KehpqxUfz60` | Dev Dream Pod with Blake Gocey | 103:20 | auto | 22461 | `teorie/prezit-jako-studio.md` | podcast BiteMe 4 roky (103 min) |

### Herní umění a vizuál · `T-ART` (+13) ⭐ NOVÉ TÉMA

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| todo | [How we made our Isometric Game Art! ★ \|\| GOLEMBERT Devlog #12](https://www.youtube.com/watch?v=UYBzqCldDDI) `UYBzqCldDDI` | Studio Firlefanz | 9:25 | auto | 1646 | `teorie/2d-perspektivy.md` | isometrická grafika (devlog); tenké — merge kandidát |
| todo | [So You Wanna Make Games?? \| Episode 10: Game Design](https://www.youtube.com/watch?v=yYYtBFSxoCg) `yYYtBFSxoCg` | Riot Games | 14:50 | manual | 2649 | `teorie/art-pipeline.md` | Riot E10: game design (pro artisty; en-cs track!) |
| todo | [So You Wanna Make Games?? \| Episode 2: Concept Art](https://www.youtube.com/watch?v=FqX-UMVTLHI) `FqX-UMVTLHI` | Riot Games | 12:39 | manual | 2069 | `teorie/art-pipeline.md` | Riot E2: concept art |
| todo | [So You Wanna Make Games?? \| Episode 3: Character Art](https://www.youtube.com/watch?v=PfpE5dNTWeI) `PfpE5dNTWeI` | Riot Games | 12:10 | manual | 1969 | `teorie/art-pipeline.md` | Riot E3: character art |
| todo | [So You Wanna Make Games?? \| Episode 5: Technical Art](https://www.youtube.com/watch?v=kr7XYXMM7-U) `kr7XYXMM7-U` | Riot Games | 12:44 | manual | 1885 | `teorie/art-pipeline.md` | Riot E5: technical art |
| todo | [So You Wanna Make Games?? \| Episode 4: Environment Art](https://www.youtube.com/watch?v=37LVhP15zGw) `37LVhP15zGw` | Riot Games | 12:54 | manual | 1858 | `teorie/art-pipeline.md` | Riot E4: environment art |
| todo | [So You Wanna Make Games?? \| Episode 6: Character Animation](https://www.youtube.com/watch?v=VmNUAX2V8JQ) `VmNUAX2V8JQ` | Riot Games | 13:11 | manual | 1840 | `teorie/art-pipeline.md` | Riot E6: character animation |
| todo | [So You Wanna Make Games?? \| Episode 1: Intro to Game Art](https://www.youtube.com/watch?v=RqRoXLLwJ8g) `RqRoXLLwJ8g` | Riot Games | 11:28 | manual | 1817 | `teorie/art-pipeline.md` | Riot E1: intro to game art |
| todo | [So You Wanna Make Games?? \| Episode 9: User Interface Design](https://www.youtube.com/watch?v=sc3h5JXtIzw) `sc3h5JXtIzw` | Riot Games | 12:29 | manual | 1776 | `teorie/art-pipeline.md` | Riot E9: UI design |
| todo | [So You Wanna Make Games?? \| Episode 7: Game VFX](https://www.youtube.com/watch?v=3QKK2o5rWSQ) `3QKK2o5rWSQ` | Riot Games | 11:50 | manual | 1750 | `teorie/art-pipeline.md` | Riot E7: game VFX |
| todo | [Typography Basics Every Game Dev Should Know](https://www.youtube.com/watch?v=QuNNdPrVMm0) `QuNNdPrVMm0` | Indie Game Clinic | 40:08 | auto | 8060 | `teorie/typografie.md` | typografie pro vývojáře (40 min) |
| todo | [Visual Communication: Why Game Art Matters](https://www.youtube.com/watch?v=SV1BBtD3hY4) `SV1BBtD3hY4` | Indie Game Clinic | 20:49 | manual | 3673 | `teorie/vizualni-komunikace.md` | proč na artu záleží |
| todo | [You Don't Need to Be an Artist to Make Great Game Art](https://www.youtube.com/watch?v=3eg5Lp3pGNk) `3eg5Lp3pGNk` | TechDad Impact | 13:36 | manual | 2665 | `teorie/vizualni-komunikace.md` | nemusíš být umělec |

### Blueprint architektura a organizace projektu · `P-BP` (+6)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| todo | [Why Dependencies are Bad and How To Avoid Them In Unreal Engine \| UE5 Mediator Pattern Explained](https://www.youtube.com/watch?v=y4fE2JdFdvY) `y4fE2JdFdvY` | Ali Elzoheiry | 26:39 | auto | 4490 | `praxe/komunikace-blueprintu.md` | rozšíření: mediator pattern |
| todo | [Why Use "Interfaces" & "Event Dispatchers" in Unreal Engine \| UE5 Explained](https://www.youtube.com/watch?v=EQfml2D9hwE) `EQfml2D9hwE` | Ali Elzoheiry | 21:54 | auto | 4020 | `praxe/komunikace-blueprintu.md` | rozšíření: proč interfaces/dispatchery |
| todo | [The Most Common Mistake Beginners Make in Unreal Engine \| UE5 Observer Pattern Explained](https://www.youtube.com/watch?v=YFtLd-bKl-U) `YFtLd-bKl-U` | Ali Elzoheiry | 12:17 | auto | 2190 | `praxe/komunikace-blueprintu.md` | rozšíření: observer pattern |
| todo | [The Power of Git in Unreal Engine: a Step-by-Step Guide \| UE5](https://www.youtube.com/watch?v=zf_44hN4Lkg) `zf_44hN4Lkg` | Ali Elzoheiry | 18:48 | auto | 3494 | `praxe/organizace-projektu.md` | rozšíření: Git v UE |
| todo | [Understanding "Components" in Unreal Engine \| UE5 Explained](https://www.youtube.com/watch?v=xo0sbSeWKe4) `xo0sbSeWKe4` | Ali Elzoheiry | 28:11 | auto | 5326 | `praxe/principy-architektury.md` | rozšíření: komponenty |
| todo | [The ultimate guide \| How to Save & Load your unreal engine 5 game \| ue5](https://www.youtube.com/watch?v=H6rqJbwjRIk) `H6rqJbwjRIk` | Ali Elzoheiry | 49:59 | auto | 8148 | `praxe/ukladani.md` | rozšíření: ultimate save/load guide (50 min) |

### AI a chování NPC · `P-AI-NPC` (+2)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| todo | [UE5 AI Sight Detection & Chasing With Behaviour Trees!](https://www.youtube.com/watch?v=JF5hIBcycPc) `JF5hIBcycPc` | Matt Aspland | 14:51 | auto | 3191 | `praxe/ai-vnimani.md` | rozšíření: sight + behavior tree chase |
| todo | [What is Utility AI? \| Smarter AI Design in Unreal Engine 5](https://www.youtube.com/watch?v=LF81fxuQeF8) `LF81fxuQeF8` | D3kryption | 18:40 | auto | 4042 | `praxe/ai-zaklady.md` | rozšíření: Utility AI |

### Motion Matching a GASP · `P-ANIM` (+1)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| todo | [EASY Directional Hit Reactions in Unreal Engine 5 (Using Choosers)](https://www.youtube.com/watch?v=d6icw1-KPwI) `d6icw1-KPwI` | Tank Control Games | 20:48 | auto | 4375 | `praxe/mm-systemy.md` | rozšíření: hit reactions přes choosery |

### Animace: nástroje a mocap · `P-ANIMTOOLS` (+1)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| todo | [New FREE Animation Tool in Unreal Engine 5.8 \| (S.A.M) Solo Animation Mode](https://www.youtube.com/watch?v=-mcMxpVmnAM) `-mcMxpVmnAM` | Proj Prod | 12:42 | auto | 2343 | `praxe/animace-nastroje.md` | rozšíření: SAM (Solo Animation Mode) 5.8 |

### Pohyb postavy (locomotion) · `P-MOVE` (+1)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| todo | [I Created THE LAST OF US PART - 2 Style Wall Detection System \| And It's AMAZING 😎\| UE 5.8](https://www.youtube.com/watch?v=EL4s7sHAFV8) `EL4s7sHAFV8` | Hydra | 12:08 | auto | 1126 | `praxe/parkour-vault.md` | rozšíření: TLOU2 wall detection 5.8 |

### MetaHuman · `P-MH` (+1)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| todo | [UE 5.8 - Any Mesh To MetaHuman - Tutorial](https://www.youtube.com/watch?v=ZmiTuYglaRI) `ZmiTuYglaRI` | Unreal - X - Tutorials | 13:58 | auto | 1714 | `praxe/metahuman.md` | rozšíření: any mesh → MetaHuman 5.8 |

### Osvětlení a atmosféra · `P-LIGHT` (+3)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| todo | [Understanding Expanse for Unreal Engine \| Complete Beginner Tutorial](https://www.youtube.com/watch?v=rky_GNM0EZs) `rky_GNM0EZs` | SARKAMARI | 23:44 | auto | 3435 | `praxe/osvetleni.md` | rozšíření: Expanse — volumetrická obloha (EVDB) |
| todo | [Lighting Hacks Got My Project Featured on Unreal Engine 5 Page 😯 \| Tips & Tricks You Should Know](https://www.youtube.com/watch?v=H2Jfs7nDKh0) `H2Jfs7nDKh0` | Karim Yasser | 15:22 | manual | 2484 | `praxe/osvetleni.md` | rozšíření: lighting hacky |
| todo | [How I Made My Horror Game Look 10x Better \| DEVLOG](https://www.youtube.com/watch?v=D4n7BeKNOtg) `D4n7BeKNOtg` | AkulDev | 8:30 | auto | 1954 | `praxe/osvetleni.md` | devlog horor vzhled; naváže na entry o hororu ve vrstvách |

### Materiály a VFX · `P-MAT` (+1)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| todo | [VFX Texture Creation: The ULTIMATE guide](https://www.youtube.com/watch?v=dMthnzpR-eU) `dMthnzpR-eU` | Le Lu | 28:46 | auto | 4089 | `praxe/materialy.md` | rozšíření: VFX textury (29 min) |

### Prostředí a environment art · `P-ENV` (+1)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| todo | [How Naughty Dog Automates AAA Art (TLOU Part 1)](https://www.youtube.com/watch?v=dqfvgA7oKC4) `dqfvgA7oKC4` | Next Level Game Art | 11:42 | auto | 1922 | `praxe/env-breakdowny.md` | rozšíření: Naughty Dog shader pipeline (TLOU už v kapitole) |

### Rendering a optimalizace · `P-PERF` (+1)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| todo | [Game Dev Secrets: Multithreaded Optimization! #indiegamedev #gamedev](https://www.youtube.com/watch?v=44hfu7ELgVc) `44hfu7ELgVc` | Inbound Shovel | 1:46 | auto | 480 | `praxe/optimalizace.md` | short 1:46 — multithreading; drobnost/Pozn. |

### AI nástroje ve vývoji · `P-AITOOLS` (+2)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| todo | [NVIDIA ARDY: The Real-Time Leap in AI Animation (Open-Source)](https://www.youtube.com/watch?v=xLf27GC0-hE) `xLf27GC0-hE` | Stefan 3D AI | 6:18 | manual | 1158 | `praxe/ai-assety.md` | rozšíření: NVIDIA ARDY — AI animace real-time |
| todo | [Claude And New UE 5.8 MCP is Crazy Good (But I made it better)](https://www.youtube.com/watch?v=I5WLl4MdK28) `I5WLl4MdK28` | Stefan 3D AI | 16:46 | manual | 3263 | `praxe/claude-code-ue.md` | rozšíření: MCP v UE 5.8 (Stefan 3D AI) |

### Editor a workflow · `P-EDITOR` (+3)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| todo | [The Best Way To Learn Unreal Engine in 2026!](https://www.youtube.com/watch?v=Nn9F341Vwy0) `Nn9F341Vwy0` | Unreal University | 11:02 | auto | 2295 | `praxe/editor-tipy.md` | rozšíření: jak se učit UE (2026) |
| todo-lp | [Unreal Engine 5 \| Blueprint For Beginners (2026)](https://www.youtube.com/watch?v=c6qW2NP8TP4) `c6qW2NP8TP4` | Smart Poly | 159:31 | manual | 29574 | — | LOW-PRIORITY: beginner kurz 160 min (jako dB-pS8PHALY) |
| todo-lp | [Unreal Engine 5.8 Beginner Tutorial - UE5 Starter Course 2026#unrealengine5  #megascans #cgi](https://www.youtube.com/watch?v=FAo9nfWYPSE) `FAo9nfWYPSE` | Magnet VFX | 88:12 | auto | 11655 | — | LOW-PRIORITY: starter kurz 88 min |

### Tvorba assetů mimo engine (Blender) · `P-ASSET` (+4) ⭐ NOVÉ TÉMA

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| todo | [Turn Any Photo into a Game Asset (Fast & Easy Blender Tutorial)](https://www.youtube.com/watch?v=ZR_X2OhsteQ) `ZR_X2OhsteQ` | Grant Abbitt (Gabbitt) | 22:21 | auto | 5301 | `praxe/foto-do-assetu.md` | Blender: fotka → herní asset |
| todo | [How to make PS1 style models in Blender \| Part 1: Textures and UV Mapping \| Tutorial](https://www.youtube.com/watch?v=8--xYWCY_bc) `8--xYWCY_bc` | hacktic | 4:33 | auto | 1005 | `praxe/ps1-estetika.md` | Blender: PS1 modely, textury/UV |
| todo | [How to make PS1 Graphics in 4 minutes](https://www.youtube.com/watch?v=A25NTdPGNaw) `A25NTdPGNaw` | binbun3D | 3:49 | auto | 631 | `praxe/ps1-estetika.md` | PS1 grafika ve 4 minutách (Blender) |
| todo | [Environment in PS1 style. (Blender Timelapse)](https://www.youtube.com/watch?v=d9GUXlnwRGk) `d9GUXlnwRGk` | Summer 85 | 7:03 | — | — | `praxe/ps1-estetika.md` | bez přepisu — timelapse; krýt z popisu |

### Hudba a zvuk (rozšíření dokumentu) · `H-EXT` (+3)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| todo | [Making an Indie Pop Banger from Scratch w/ Lyncs (Cook Up)](https://www.youtube.com/watch?v=X6RMUest2sw) `X6RMUest2sw` | Splice | 18:58 | auto | 1418 | `hudba/aranz.md` | rozšíření: cook-up Splice — track od nuly v praxi |
| todo | [The most insane sound design tool nobody's heard of (is free)](https://www.youtube.com/watch?v=TGczsxuAm1I) `TGczsxuAm1I` | mylarmelodies | 14:50 | manual | 2028 | `hudba/nastroje-zdarma-a-game-jam.md` | rozšíření: CDP (alt. synteza-zvuku) |
| todo | [How to Make a 3D Sound in Unreal Engine 5](https://www.youtube.com/watch?v=dttUv6--1nA) `dttUv6--1nA` | Gorka Games | 3:43 | auto | 572 | `hudba/sound-design-ve-hre.md` | rozšíření: 3D zvuk v UE |
