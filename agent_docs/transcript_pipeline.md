# Transcript Pipeline

How raw material gets into the repo. Authoritative for `scripts/` behavior and the `transcripts*/` layout.

## Fetch (incremental)

`scripts/fetch_transcripts.sh` — edit `PLAYLIST_URL` once, then run from repo root. Requires `yt-dlp` + `ffmpeg` (`brew install yt-dlp ffmpeg`).

What the flags do and why:

- `--skip-download` — subtitles + metadata only, never video files.
- `--write-subs --write-auto-subs --sub-langs "en.*"` — manual tracks when creators uploaded them, auto captions as fallback. Manual > auto in quality (punctuation, correct terms).
- `--convert-subs srt` — normalize to SRT (needs ffmpeg).
- `--write-info-json` — per-video metadata; **the credit source** (`channel`, `channel_url`, `title`, `webpage_url`, `duration`).
- `--download-archive scripts/fetched.txt` — **the incremental core.** yt-dlp records each processed video id and skips it on re-runs; extending the playlist and re-running fetches only the delta. `--force-write-archive` makes this work with `--skip-download`.
- `--ignore-errors` — one broken/region-locked video must not kill a 200-video run.
- `--sleep-requests 1` — spacing against YouTube's HTTP 429 rate limiting.
- `-o "transcripts/%(id)s/%(title)s.%(ext)s"` — folder per **video id** (stable key; titles can change, ids can't). Files inside carry the human-readable title.

Known follow-up: if fetches start failing wholesale after a YouTube-side change, `brew upgrade yt-dlp` first.

## Clean

`python3 scripts/clean_transcripts.py transcripts transcripts_clean`

- **Track selection per video** (since 2026-10-10 driven by `info.json`): a **manual** English track listed under `subtitles` (`en`, then regional `en-GB`/`en-US`) > auto **`en-orig`** (original ASR; `en-US-orig` for an English dub of a foreign video) > auto `en`. A manual track that runs well past the video's duration belongs to another video and is rejected. The chosen track is recorded in the output header. Without info.json the old file-name heuristic applies.
- **Trap: auto `en` is no longer a copy of `en-orig`.** Up to the third wave the two were identical (447/447 old videos clean to the same paragraphs and timestamps). In the fourth wave 10 of 54 English videos had an auto `en` that is a **machine retranslation from one of YouTube's auto-dubbed audio tracks** — readable but garbled („game tag", „snippet" for fragment, „card" for map). Hence `en-orig` first.
- **Trap: `en-xx` tracks are not regional subs.** When a creator uploads manual subs in other languages, YouTube offers machine translations of each back into English (`en-de`, `en-pl`, `en-en`…), and `--sub-langs "en.*"` downloads them all. The pre-2026-10-10 heuristic took any `en-<letters>` file for a regional manual track and so sometimes cleaned a retranslation instead of the original (10 videos, see dev_log 2026-10-10). The same multilingual videos also multiply subtitle requests and are the main trigger of HTTP 429 during a fetch.
- **Rolling-window dedupe:** YouTube auto-captions repeat the previous cue's tail in every cue; the script strips the overlap.
- Strips HTML entities (`&nbsp;`), inline tags, and noise markers (`[Music]`, `[Applause]`).
- Joins cues into paragraphs (new paragraph on ≥8 s silence or ≥45 s length) and prefixes each with `[M:SS | t=SECONDSs]` — the `t=` value plugs directly into deep links (`&t=273s`).
- Output: `transcripts_clean/<video_id>.txt` with a metadata header (source file, track type).

## Quality expectations for synthesis

- **Auto captions have no punctuation and garble terminology phonetically** ("teslation", "rogike", "windarching"). Fix from context; when a term is genuinely undecipherable, mark `[nesrozumitelné]` rather than inventing.
- Manual tracks may contain gaps (creators sometimes skip music/sponsor segments) — a mid-sentence jump in the transcript is a track gap, not a cleaning bug.
- A video with **no English track at all** yields only `info.json`. It still enters the processing index (source of title/URL) flagged `bez přepisu`; it can be covered from the author's summary or skipped, per user decision.

## Boundaries

- `transcripts/`, `transcripts_clean/` are **gitignored** — raw and cleaned transcripts are the creators' content and never enter the public repo. `scripts/fetched.txt` (bare video ids) **is committed** — it's the incremental state.
- Pilot material lives in the same structure (`transcripts/<id>/…`); there is no special pilot folder in the repo.
