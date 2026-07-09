# KICKOFF — first Claude Code session (Phase 0)

Start by reading `AGENTS.md`. This file is the concrete assignment for the scaffold-verification phase; the checklist lives in `agent_docs/roadmap.md` → Phase 0. Work through it top to bottom, follow `agent_docs/workflow.md` for the loop, and tick roadmap checkboxes as you go.

## Context you need

- This repo skeleton was produced in a chat session from 5 pilot videos. The pilot chapters in `docs/` are **done content** — do not rewrite them; your job is to make the machinery around them run.
- Raw pilot transcripts exist only on the user's machine (a local `pilot/` folder). They are **not** in the repo and must never be committed (see the licensing block in `AGENTS.md`).
- Credit blocks in pilot chapters contain `<!-- TODO: credit z info.json -->` placeholders — the pilot was fetched before `--write-info-json` was added to the pipeline. Filling them is part of this phase.

## Tasks

1. **Git + hygiene.** `git init` if needed; verify `.gitignore` matches the boundaries in `AGENTS.md` (`transcripts/`, `transcripts_clean/`, `inbox/`, `pilot/`, `site/`). Move any local `pilot/` raw files under `transcripts/<id>/…` (they stay untracked either way).
2. **Local build.** `pip install mkdocs-material` (pipx also fine). `mkdocs build --strict` must pass. Then `mkdocs serve` and eyeball: light palette, working nav, search returns Czech content, hover tooltips appear on terms (e.g. „Nanite" in the Mesh Terrain chapter). Fix what's broken; broken internal links are the most likely failure.
3. **Pipeline end-to-end.** Set the real `PLAYLIST_URL` in `scripts/fetch_transcripts.sh`. Run it — `scripts/fetched.txt` is empty, so the 5 pilot videos re-fetch **with** `info.json` this time. Then `python3 scripts/clean_transcripts.py transcripts transcripts_clean`. If the playlist is large, that's fine — this run doubles as the Phase 2 full fetch; mind YouTube 429s (the script sleeps 1 s between requests; if throttled, wait and re-run — the archive makes it resumable).
4. **Fill credits.** For each pilot video id (`ySZynbrqMRM`, `6SYX17NzNqE`, `rCd36pNqCeo`, `De2fXs2JZxw`, `JzQrUAVPmr4`): read `channel` + `channel_url` from its `info.json` and replace the `TODO` placeholders in the matching chapters. Exact names from metadata only — never guess attribution.
5. **Site config.** Replace `REPLACE_GITHUB_USERNAME` in `mkdocs.yml` with the real GitHub username once the remote repo exists.
6. **Deploy.** Push to GitHub, enable Pages (Settings → Pages → Source: **GitHub Actions** — the workflow builds with `--strict` and publishes via the native Pages artifact flow; no `gh-pages` branch is involved). Verify the workflow is green and the site is live; paste the URL into `README.md`.
7. **Log + propose.** Dev log entry per protocol; tick Phase 0 boxes in `agent_docs/roadmap.md`; propose a commit message (the user commits). Point to the next step (Phase 1 — user review of pilot chapters).

## Done means

- `mkdocs build --strict` green locally and in CI; site live on Pages.
- Zero `TODO: credit` placeholders left in `docs/`.
- `transcripts/` populated + gitignored; `scripts/fetched.txt` committed with the fetched ids.
- Dev log entry written; roadmap updated.
