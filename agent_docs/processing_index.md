# Processing Index

Per-video status tracker for the whole playlist — created in the Phase 2 taxonomy. **Update the status column whenever a video is processed.** Chapter slugs are working titles for grouping; final chapter names/files are decided at synthesis time. Téma tree **approved by user 2026-07-09** (incl. „Rešerše: slovanská mytologie" and the skip/low-priority flags); re-assigning individual videos later is cheap (nav-only change).

Legend: status `todo / drafted / published / skip` · track `manual / auto / —` (— = no English subtitle track, "bez přepisu") · slova = word count of the cleaned transcript.

**Stats:** 210 videos (31 Teorie, 179 Praxe) · 138 published (pilot + batch 1–13) · 7 bez přepisu · 5 skip (news/promo) + 2 low-priority (beginner courses).

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
| todo | [I Recreated Fall Guy's Hex-A-Gone Game Using PCG. Here's How I Did It!](https://www.youtube.com/watch?v=G5eXYvFbMko) `G5eXYvFbMko` | Procedural Minds | 25:23 | auto | 5807 | `pcg-pripadovky` | Hex-A-Gone |
| todo | [Spawn Vines On Any Mesh With A Single Click Using PCG Mode in UE5.7](https://www.youtube.com/watch?v=rYLF1up8sc8) `rYLF1up8sc8` | Procedural Minds | 26:27 | auto | 6701 | `pcg-vegetace` | liány na mesh |
| todo | [Spawn Hanging PCG Vines And More Using This Simple Setup](https://www.youtube.com/watch?v=5bbKHksth9Q) `5bbKHksth9Q` | Procedural Minds | 25:18 | auto | 6205 | `pcg-vegetace` | visící liány |
| todo | [SpeedTree to Nanite foliage with Wind! Unreal Engine 5.7](https://www.youtube.com/watch?v=67-W5lCSD_0) `67-W5lCSD_0` | lumpy668 | 16:30 | — | — | `pcg-vegetace` | bez přepisu |
| todo | [Everything You Need to Know About Procedural Vegetation in UE5.8 #tutorial #unrealengine #procedural](https://www.youtube.com/watch?v=DvBECqijNDg) `DvBECqijNDg` | PolyBoost | 14:09 | auto | 1042 | `pcg-vegetace` |  |
| todo | [How to integrate PCG with landscape layers in Unreal engine 5 - Part 2](https://www.youtube.com/watch?v=hEHF0x22LpY) `hEHF0x22LpY` | Rbnks | 9:50 | auto | 1610 | `pcg-vegetace` | landscape layers |
| todo | [Unreal Engine 5.7 - Procedural Vegetation - Build Your Own Forest - Tutorial (Part 1/2)](https://www.youtube.com/watch?v=o-kMXZX_oK8) `o-kMXZX_oK8` | Unreal - X - Tutorials | 9:04 | auto | 1235 | `pcg-vegetace` | les 1/2 |
| todo | [Create a PCG forest with the new Megaplants and Collision in Unreal Engine 5](https://www.youtube.com/watch?v=ryb0sb2SQ-U) `ryb0sb2SQ-U` | Rbnks | 8:25 | auto | 1249 | `pcg-vegetace` | Megaplants |
| todo | [Unreal Engine 5.7 - Create Forest Clearings & Paths With PCG - Tutorial](https://www.youtube.com/watch?v=8UxAmQfIj5s) `8UxAmQfIj5s` | Unreal - X - Tutorials | 8:20 | auto | 1102 | `pcg-vegetace` | mýtiny a cesty |
| todo | [Unreal Engine 5.7 - PCG Vegatation - Build Your Own Forest - Tutorial (Part 2/2)](https://www.youtube.com/watch?v=4TZG9fBEiR0) `4TZG9fBEiR0` | Unreal - X - Tutorials | 6:20 | auto | 829 | `pcg-vegetace` | les 2/2 |
| todo | [Unreal Engine 5.7 - How To Add Collision To PCG Wind Trees - Tutorial](https://www.youtube.com/watch?v=Ag6r2YNtSe0) `Ag6r2YNtSe0` | Unreal - X - Tutorials | 4:42 | auto | 619 | `pcg-vegetace` | kolize větrných stromů |
| todo | [Unreal Engine 5.7 - Procedural Vegetation Pine Trees - Quick Tip](https://www.youtube.com/watch?v=Wqmr0bSR99U) `Wqmr0bSR99U` | Unreal - X - Tutorials | 1:26 | auto | 173 | `pcg-vegetace` | quick tip |
| skip | [SpeedTree 10 to Unreal Engine 5 with Wind Animation (Udemy Course)](https://www.youtube.com/watch?v=Kke6IaV7dc0) `Kke6IaV7dc0` | BlenderToUnreal | 1:23 | auto | 151 | `pcg-vegetace` | promo kurzu (1:23) — přeskočit? |
| todo | [Unreal Engine 5.7 - Procedural Vegetation - Distance Wind Fix - QuickTip](https://www.youtube.com/watch?v=X_83dlYoZ7w) `X_83dlYoZ7w` | Unreal - X - Tutorials | 0:57 | auto | 120 | `pcg-vegetace` | quick tip |
| published | [Add Scattering To The PCG Mode Brush To Simulate Actual Painting](https://www.youtube.com/watch?v=AYulmKtqhLM) `AYulmKtqhLM` | Procedural Minds | 24:29 | auto | 5953 | `pcg-zaklady` | brush scattering |
| published | [How To Use the NEW UE5.7 PCG Mode, and Tips To Make It MORE Powerful!](https://www.youtube.com/watch?v=IPwVOhvQ2bo) `IPwVOhvQ2bo` | Procedural Minds | 23:29 | auto | 5451 | `pcg-zaklady` | PCG mode 5.7 (2 myšlenky) |
| published | [Precise Cutouts Using Collisions in UE5 PCG, And More Tips and Tricks](https://www.youtube.com/watch?v=-G14-4m4-LA) `-G14-4m4-LA` | Procedural Minds | 16:02 | auto | 3812 | `pcg-zaklady` | cutouts |
| published | [UE5.7 Just Upgraded PCG! Here’s How to Use the New Editor Tools](https://www.youtube.com/watch?v=fjuCUJ1r-Wk) `fjuCUJ1r-Wk` | All things GAME! | 15:03 | auto | 1585 | `pcg-zaklady` |  |

### Prostředí a environment art · `P-ENV` (11)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| todo | [This Developer Recreated San Francisco 1:1 in Unreal Engine 5](https://www.youtube.com/watch?v=TBGPbs9yjMM) `TBGPbs9yjMM` | Gorka Games | 36:19 | auto | 6875 | `env-breakdowny` | San Francisco 1:1 |
| todo | [How 4 Artists Built a AAA World](https://www.youtube.com/watch?v=a78WoZeZGqI) `a78WoZeZGqI` | Next Level Game Art | 21:53 | auto | 3678 | `env-breakdowny` |  |
| todo | [Why Resident Evil Requiem Looks So Real \| Graphics Breakdown](https://www.youtube.com/watch?v=utYMtJwGxiM) `utYMtJwGxiM` | Next Level Game Art | 17:33 | auto | 2201 | `env-breakdowny` | RE Requiem |
| todo | [The ''Fake'' Geometry of Crimson Desert: How it Really Works](https://www.youtube.com/watch?v=44PT8XRZRGA) `44PT8XRZRGA` | Next Level Game Art | 13:30 | auto | 2025 | `env-breakdowny` | Crimson Desert |
| todo | [The Environment Art Tricks Behind TLOU Part 1](https://www.youtube.com/watch?v=EJcqhvylH50) `EJcqhvylH50` | Next Level Game Art | 10:15 | auto | 1709 | `env-breakdowny` | TLOU |
| todo | [How Crimson Desert Fakes Realism (It’s Genius)](https://www.youtube.com/watch?v=TUAyiCswYt4) `TUAyiCswYt4` | Next Level Game Art | 9:48 | auto | 1587 | `env-breakdowny` | Crimson Desert |
| todo | [Forest Path Environment in UE5 \| Step-by-Step Tutorial](https://www.youtube.com/watch?v=WrjgH4sRja8) `WrjgH4sRja8` | Hoj Dee Studio | 131:44 | auto | 11297 | `env-tvorba` | 132 min |
| todo | [How to create Cinematic dark Forest scene in Unreal Engine 5.5.4 \| Full Tutorial](https://www.youtube.com/watch?v=Eh8QgGhjxyg) `Eh8QgGhjxyg` | World Of VFX | 16:47 | auto | 3302 | `env-tvorba` | temný les |
| todo | [Use this Technique to take your Environments to the next Level](https://www.youtube.com/watch?v=R9yr1ksLlmY) `R9yr1ksLlmY` | UNF Games | 14:54 | auto | 2282 | `env-tvorba` |  |
| todo | [Unreal Engine 5.7 - Forest Atmosphere: Dynamic Audio & Falling Leaves - Tutorial](https://www.youtube.com/watch?v=ItHOm_BJpCM) `ItHOm_BJpCM` | Unreal - X - Tutorials | 14:20 | auto | 1839 | `env-tvorba` | audio + padající listí |
| skip | [DASH 1.12 - IMPROVED UE5 WORLD BUILDING TOOLS](https://www.youtube.com/watch?v=ZvTJBAkx_lY) `ZvTJBAkx_lY` | Polygonflow Dash | 6:40 | auto | 671 | `nastroje-treti-strany` | changelog nástroje — přeskočit? |

### Materiály a VFX · `P-MAT` (6)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| todo | [Smart Master Material Workflow in Unreal Engine 5 #tutorial  #unrealengine #substance_painter](https://www.youtube.com/watch?v=xLlFljzdLF4) `xLlFljzdLF4` | PolyBoost | 15:34 | auto | 918 | `master-materialy` |  |
| todo | [Easy Nanite Displacement in UE5 - Create Stunning Detail](https://www.youtube.com/watch?v=pLl25FaqCiI) `pLl25FaqCiI` | duongunreal | 30:09 | manual | 585 | `nanite-displacement` |  |
| todo | [Unreal Engine 5.4 Preview Nanite Cliff Tessellation RTX 4090](https://www.youtube.com/watch?v=CdyLdkRmFA0) `CdyLdkRmFA0` | Gorka Games | 2:19 | auto | 432 | `nanite-displacement` | preview (2:19) |
| todo | [How To Create A Procedural Decay System - Unreal Engine 5 Material Tutorial](https://www.youtube.com/watch?v=OCgrHAHKmuM) `OCgrHAHKmuM` | Pitchfork Academy | 85:23 | auto | 13694 | `proceduralni-materialy` | 85 min |
| todo | [Stop Stretching Textures in UE5 #unrealengine #gamedev #indiedev](https://www.youtube.com/watch?v=kJgRLfyqjL0) `kJgRLfyqjL0` | Matt Aspland | 0:32 | auto | 107 | `textury-tipy` | short |
| todo | [How To Use Toon Shading New In UE5.8 - Unreal Engine 5.8 Materials Tutorial](https://www.youtube.com/watch?v=iMJJYXHMw4o) `iMJJYXHMw4o` | Pitchfork Academy | 31:15 | auto | 5671 | `toon-shading` |  |

### Osvětlení a atmosféra · `P-LIGHT` (6)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| todo | [Recreating Silent Hill 2 Fog in Unreal Engine 5](https://www.youtube.com/watch?v=96sheL5UqJQ) `96sheL5UqJQ` | Dallas Drapeau | 36:10 | auto | 4985 | `atmosfera-mlha` | Silent Hill 2 |
| todo | [Realistic and Physical Lighting in UE5: The PBL Workflow](https://www.youtube.com/watch?v=GsE0mDtxtiQ) `GsE0mDtxtiQ` | arthur tasquin | 28:39 | manual | 5022 | `fyzikalni-osvetleni` |  |
| todo | [Create a horror lighting in Unreal Engine.](https://www.youtube.com/watch?v=0w3SBb5ktlg) `0w3SBb5ktlg` | Karim aboushousha | 16:12 | auto | 1793 | `hororove-osvetleni` |  |
| todo | [How to make a simple night scene in Unreal Engine 5](https://www.youtube.com/watch?v=YHhRTjD_P2A) `YHhRTjD_P2A` | UE5 Poseidon | 8:28 | auto | 958 | `nocni-scena` |  |
| todo | [Game Dev Secrets: How does light work? #indiegamedev #indiedev](https://www.youtube.com/watch?v=rzm8v5gx7l0) `rzm8v5gx7l0` | Inbound Shovel | 1:00 | auto | 254 | `osvetleni-zaklady` | short |
| todo | [UE5 Lighting Tricks You Need to Know](https://www.youtube.com/watch?v=9PFrFDjVXHM) `9PFrFDjVXHM` | Sergey Maryshev | 0:51 | manual | 142 | `osvetleni-zaklady` | short |

### Rendering a optimalizace · `P-PERF` (7)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| todo | [DLSS 4.5 Setup Guide for UE 5.7 Projects](https://www.youtube.com/watch?v=y80hX4IlzmI) `y80hX4IlzmI` | DK 3D | 25:10 | auto | 3078 | `dlss` |  |
| todo | [How to use Nanite Voxelization (like in the Witcher Demo)](https://www.youtube.com/watch?v=q2T4ni7UPfI) `q2T4ni7UPfI` | DK 3D | 11:25 | auto | 1467 | `nanite` | voxelizace |
| todo | [LOD or Nanite in UE5? \| Unreal Engine 5 Optimization Tutorial for Beginners](https://www.youtube.com/watch?v=-FmFOiqTO-8) `-FmFOiqTO-8` | Sergey Maryshev | 8:58 | manual | 1569 | `nanite` | LOD vs Nanite |
| todo | [Foliage Optimization Done Right (UE 5.7)](https://www.youtube.com/watch?v=QvE_EUuGFm4) `QvE_EUuGFm4` | Dallas Drapeau | 54:47 | auto | 8236 | `optimalizace-foliage` |  |
| todo | [Why your levels are Slow in Unreal Engine 5](https://www.youtube.com/watch?v=4fjTSbDaeYQ) `4fjTSbDaeYQ` | Taken Grace | 34:16 | auto | 7923 | `optimalizace-levelu` |  |
| todo | [Stop Shipping 4K Textures — Right-Size Everything in UE5 (Surface Forge)](https://www.youtube.com/watch?v=WnHgLJcmhTM) `WnHgLJcmhTM` | Arghanion's Puzzlebox | 20:14 | auto | 4092 | `textury-optimalizace` |  |
| todo | [Virtual Textures vs Atlases: The Truth about UE5 Optimization](https://www.youtube.com/watch?v=_fUzAKlxiQg) `_fUzAKlxiQg` | Sergey Maryshev | 7:42 | manual | 1386 | `textury-optimalizace` | virtual textures |

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
| todo | [AI Animation Just Got a Revolution — NVIDIA Kimodo](https://www.youtube.com/watch?v=CVA4jGHAbnA) `CVA4jGHAbnA` | Stefan 3D AI | 6:47 | manual | 1211 | `ai-animace` | NVIDIA Kimodo |
| todo | [From AI to Metahuman - Best New UE 5.8 Workflow for Custom Character](https://www.youtube.com/watch?v=4w7oA4oJMqs) `4w7oA4oJMqs` | Stefan 3D AI | 28:22 | manual | 5415 | `ai-assets` | → MetaHuman |
| todo | [I Built a Modular Character with AI (Full Workflow)](https://www.youtube.com/watch?v=gZIxrX1n2D4) `gZIxrX1n2D4` | Stefan 3D AI | 26:54 | manual | 5047 | `ai-assets` | modulární postava |
| todo | [Claude Took Over ComfyUI + Blender: Here's What Happened](https://www.youtube.com/watch?v=KdYv_TT-ZnQ) `KdYv_TT-ZnQ` | PixelArtistry | 23:07 | auto | 4860 | `ai-assets` | ComfyUI+Blender |
| todo | [From AI to Playable 3D Character in Unreal Engine](https://www.youtube.com/watch?v=k1xBERhXtHA) `k1xBERhXtHA` | Stefan 3D AI | 22:04 | manual | 4195 | `ai-assets` |  |
| todo | [Next-Gen 3D AI Is Here (5-Second Game-Ready Models)](https://www.youtube.com/watch?v=mXjUz3viYmQ) `mXjUz3viYmQ` | Stefan 3D AI | 19:48 | manual | 3282 | `ai-assets` |  |
| todo | [Complete Free AI Workflow for Game-Ready 3D Characters](https://www.youtube.com/watch?v=TkP-_LyacMI) `TkP-_LyacMI` | Stefan 3D AI | 12:09 | manual | 2316 | `ai-assets` |  |
| todo | [Make infinite characters in the SAME style!](https://www.youtube.com/watch?v=LcJQQwltQ2Q) `LcJQQwltQ2Q` | PixelLab | 11:06 | auto | 1744 | `ai-assets` | konzistentní styl |
| todo | [From Dialogue to Action: Create Scene-Aware AI Characters That Act AND React \| Convai Unreal Engine](https://www.youtube.com/watch?v=lB5_KRWdg_w) `lB5_KRWdg_w` | Convai | 5:20 | auto | 889 | `ai-npc-dialogy` | produktové demo (Convai) |
| todo | [I Built My Dream Game in 72 Hours — Assets by AI, Gameplay by Claude Code](https://www.youtube.com/watch?v=k9cbm5jSOxk) `k9cbm5jSOxk` | Stefan 3D AI | 35:14 | manual | 5619 | `claude-code-ue` | hra za 72 h |
| todo | [Claude Code Took Over Unreal Engine 5 and Built a Game](https://www.youtube.com/watch?v=iRcrZjOt5H8) `iRcrZjOt5H8` | Stefan 3D AI | 16:45 | manual | 3136 | `claude-code-ue` |  |
| todo | [NEW Unreal Engine 5.8 MCP Tutorial (QuickStart Guide)](https://www.youtube.com/watch?v=PqrKqhkj3gQ) `PqrKqhkj3gQ` | Smart Poly | 12:21 | auto | 2579 | `claude-code-ue` | MCP |
| todo | [This AI builds blueprints for you in Unreal Engine](https://www.youtube.com/watch?v=Kzy7isA2xO0) `Kzy7isA2xO0` | TUF | 7:42 | auto | 1048 | `claude-code-ue` | AI staví blueprinty |
| todo | [How to Setup Claude Code in Unreal Engine 5.8 (Easy)](https://www.youtube.com/watch?v=0tzXVwDxzt8) `0tzXVwDxzt8` | Unreal University  | 5:51 | auto | 1066 | `claude-code-ue` | setup |

### Editor a workflow · `P-EDITOR` (12)

| status | video | kanál | délka | track | slova | kapitola (slug) | pozn. |
|---|---|---|---|---|---|---|---|
| todo | [5 Years Of Unreal Engine Experience In 9 Minutes](https://www.youtube.com/watch?v=BHY46bPmsXY) `BHY46bPmsXY` | Unreal University  | 9:14 | auto | 1805 | `editor-tipy` | 5 let zkušeností |
| todo | [UE5 for Beginners: 5 Tips I Wish I Knew Sooner](https://www.youtube.com/watch?v=jxEfh8_zfdk) `jxEfh8_zfdk` | Sergey Maryshev | 0:48 | manual | 148 | `editor-tipy` | short |
| todo | [Change Your Mesh's Pivot Point in the Engine! #unrealengine5 #modelingmode #pivot #ue5 #blender](https://www.youtube.com/watch?v=f50yoTWThnw) `f50yoTWThnw` | Druid Mechanics | 0:41 | auto | 192 | `editor-tipy` | short |
| todo | [The Secret 3D Box-Select Tool in UE5! 🤯 #unrealengine #indiedev #gamedev](https://www.youtube.com/watch?v=HprvvfEzrNI) `HprvvfEzrNI` | Matt Aspland | 0:30 | auto | 100 | `editor-tipy` | short |
| todo | [Stop Deleting Blueprint Nodes Like This! #unrealengine #gamedev #indiedev](https://www.youtube.com/watch?v=Pt1tFh4UqJk) `Pt1tFh4UqJk` | Matt Aspland | 0:28 | auto | 98 | `editor-tipy` | short |
| published | [Select EVERY Copy of an Asset Instantly in UE5! 🤯 #unrealengine #gamedev #indiedev](https://www.youtube.com/watch?v=De2fXs2JZxw) `De2fXs2JZxw` | Matt Aspland | 0:27 | auto | 102 | `praxe/editor-tipy.md` |  |
| todo | [5 Unreal Engine Tricks Every Beginner Misses #unrealengine #indiedev #gamedev](https://www.youtube.com/watch?v=kSHz_V79eCk) `kSHz_V79eCk` | Matt Aspland | 0:26 | auto | 81 | `editor-tipy` | short |
| todo | [The Secret to Realistic Level Design in UE5 #unrealengine #gamedev #indiedev](https://www.youtube.com/watch?v=qo-LYeeKMr4) `qo-LYeeKMr4` | Matt Aspland | 0:26 | auto | 88 | `editor-tipy` | short — physics placement |
| todo | [How To Fix Editor Lag In 30 Seconds! #unrealengine5 #indiedev](https://www.youtube.com/watch?v=U0nC8-882a0) `U0nC8-882a0` | Matt Aspland | 0:22 | auto | 73 | `editor-tipy` | short |
| todo | [Unreal Engine 5.7.1 Beginner Tutorial - UE5 Starter Course 2026#unrealengine5  #megascans #cgi](https://www.youtube.com/watch?v=0yBSEiMldo0) `0yBSEiMldo0` | Magnet VFX | 97:40 | auto | 13268 | `kurzy` | kurz pro začátečníky (98 min) — nízká priorita |
| skip | [Unreal Engine 5.8 JUST DROPPED (Mesh Terrain, Control Rig, Physics, AI)](https://www.youtube.com/watch?v=sDLYd2keSwA) `sDLYd2keSwA` | Proj Prod | 12:44 | manual | 2188 | `novinky` | novinkové video — přeskočit? |
| skip | [Unreal Engine 5.8 Feature Highlights](https://www.youtube.com/watch?v=ExFF5gXVhDU) `ExFF5gXVhDU` | Unreal Engine | 3:26 | manual | 359 | `novinky` | novinkové video — přeskočit? |
