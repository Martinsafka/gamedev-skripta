#!/usr/bin/env bash
# Incremental transcript fetch for the study playlists.
#
# Downloads English subtitle tracks + metadata (info.json) for every video
# in PLAYLIST_URLS that has not been fetched before. Already-fetched video ids
# are tracked in scripts/fetched.txt (--download-archive), so re-running after
# extending a playlist downloads only the new videos.
#
# Layout produced:  transcripts/<video_id>/<title>.<lang>.srt + <title>.info.json
# transcripts/ is gitignored — raw transcripts must never be committed/published.
#
# Usage:  ./scripts/fetch_transcripts.sh
# Then:   python3 scripts/clean_transcripts.py transcripts transcripts_clean
set -euo pipefail

PLAYLIST_URLS=(
  "https://www.youtube.com/playlist?list=PL-qhg2vVw8lw3mBg_K_EtS7MGcua86kru"  # hlavní studijní playlist (210+)
  "https://www.youtube.com/playlist?list=PLfwSSaFKkCXc"                       # Gamedev-music (hudba a zvuk)
)

yt-dlp \
  --skip-download \
  --write-subs --write-auto-subs \
  --sub-langs "en.*" \
  --convert-subs srt \
  --write-info-json \
  --download-archive scripts/fetched.txt \
  --force-write-archive \
  --ignore-errors \
  --sleep-requests 1 \
  -o "transcripts/%(id)s/%(title)s.%(ext)s" \
  "${PLAYLIST_URLS[@]}"
