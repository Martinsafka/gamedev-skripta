#!/usr/bin/env python3
"""Clean YouTube SRT/VTT transcripts into plain text with paragraph timestamps.

YouTube auto-captions use a "rolling window": each cue repeats the tail of the
previous one. This script deduplicates the overlap, strips HTML entities and
noise markers ([Music], [Applause], ...), joins cues into readable paragraphs,
and prefixes each paragraph with a timestamp usable for deep links
(https://www.youtube.com/watch?v=ID&t=SECONDSs).

Usage:
    python3 scripts/clean_transcripts.py <input_dir> <output_dir>

<input_dir> is scanned for per-video folders (named by video id) containing
.srt/.vtt files — the layout produced by scripts/fetch_transcripts.sh.
For each video the best available track is chosen:
    manual subs (e.g. en-GB, or en differing from en-orig) > auto captions.
Output: <output_dir>/<video_id>.txt
"""
import html
import re
import sys
from pathlib import Path

NOISE_RE = re.compile(r"\[(?:Music|Applause|Laughter|music|applause|laughter)\]")


def parse_timestamp(ts: str) -> int:
    """HH:MM:SS,mmm or HH:MM:SS.mmm -> whole seconds."""
    ts = ts.replace(",", ".").strip()
    h, m, s = ts.split(":")
    return int(int(h) * 3600 + int(m) * 60 + float(s))


def parse_srt_or_vtt(path: Path):
    """Return a list of (start_seconds, text) cue tuples."""
    content = path.read_text(encoding="utf-8", errors="replace")
    content = re.sub(r"^WEBVTT.*?\n\n", "", content, flags=re.DOTALL)
    content = re.sub(r"<[^>]+>", "", content)  # inline tags <c>, <00:00:00.000>
    content = re.sub(r"align:start position:\d+%", "", content)
    content = html.unescape(content)  # &nbsp; &amp; ...
    content = content.replace("\u00a0", " ")  # non-breaking spaces from &nbsp;
    content = NOISE_RE.sub("", content)

    cues = []
    ts_re = re.compile(
        r"(\d{1,2}:\d{2}:\d{2}[.,]\d{3})\s*-->\s*(\d{1,2}:\d{2}:\d{2}[.,]\d{3})"
    )
    for block in re.split(r"\n\s*\n", content):
        lines = [l.strip() for l in block.strip().split("\n") if l.strip()]
        if not lines:
            continue
        start = None
        text_lines = []
        for line in lines:
            m = ts_re.search(line)
            if m:
                start = parse_timestamp(m.group(1))
            elif re.fullmatch(r"\d+", line):
                continue  # SRT sequence number
            else:
                text_lines.append(line)
        if start is not None and text_lines:
            text = re.sub(r"\s+", " ", " ".join(text_lines)).strip()
            if text:
                cues.append((start, text))
    return cues


def dedupe_rolling(cues):
    """Remove the rolling-window overlap of YouTube auto-captions."""
    result = []
    prev_text = ""
    for start, text in cues:
        t = text.strip()
        if not t or t == prev_text:
            continue
        overlap = 0
        for i in range(min(len(prev_text), len(t)), 0, -1):
            if prev_text.endswith(t[:i]):
                overlap = i
                break
        new_part = t[overlap:].strip()
        if new_part:
            result.append((start, new_part))
        prev_text = t
    return result


def to_paragraphs(cues, gap_seconds=8, max_par_seconds=45):
    """Join cues into paragraphs; break on silence gaps or after max length."""
    if not cues:
        return []
    paragraphs = []
    cur_start, cur_texts, last_ts = cues[0][0], [cues[0][1]], cues[0][0]
    for start, text in cues[1:]:
        if (start - last_ts > gap_seconds) or (start - cur_start > max_par_seconds):
            paragraphs.append((cur_start, " ".join(cur_texts)))
            cur_start, cur_texts = start, [text]
        else:
            cur_texts.append(text)
        last_ts = start
    paragraphs.append((cur_start, " ".join(cur_texts)))
    return paragraphs


def fmt_ts(seconds: int) -> str:
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def choose_best_track(vid_dir: Path):
    """Prefer manual subtitles over auto captions.

    Heuristic: any regional variant (en-GB, en-US...) is manual; a plain `en`
    that differs in size from `en-orig` is manual; otherwise fall back to
    whatever exists (`en`, then `en-orig`).
    """
    files = [f for f in vid_dir.iterdir() if f.suffix in (".srt", ".vtt")]
    regional = [f for f in files if re.search(r"\.en-(?!orig)[A-Za-z]+\.(srt|vtt)$", f.name)]
    en_plain = [f for f in files if re.search(r"\.en\.(srt|vtt)$", f.name)]
    en_orig = [f for f in files if re.search(r"\.en-orig\.(srt|vtt)$", f.name)]
    if regional:
        return regional[0], "manual (regional track)"
    if en_plain and en_orig and en_plain[0].stat().st_size != en_orig[0].stat().st_size:
        return en_plain[0], "manual (differs from -orig)"
    if en_plain:
        return en_plain[0], "auto or manual (single en track)"
    if en_orig:
        return en_orig[0], "auto captions"
    return None, "no usable track"


def process(path: Path, out_dir: Path, video_id: str, source_note: str):
    cues = dedupe_rolling(parse_srt_or_vtt(path))
    paragraphs = to_paragraphs(cues)
    out = out_dir / f"{video_id}.txt"
    with out.open("w", encoding="utf-8") as f:
        f.write(f"# {path.stem}\n# video_id: {video_id}\n")
        f.write(f"# source_file: {path.name}\n# track: {source_note}\n\n")
        for start, text in paragraphs:
            f.write(f"[{fmt_ts(start)} | t={start}s] {text}\n\n")
    words = sum(len(t.split()) for _, t in paragraphs)
    print(f"{video_id}: {len(paragraphs)} paragraphs, ~{words} words ({source_note}) -> {out}")


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    in_dir, out_dir = Path(sys.argv[1]), Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)
    for vid_dir in sorted(p for p in in_dir.iterdir() if p.is_dir()):
        chosen, note = choose_best_track(vid_dir)
        if chosen:
            process(chosen, out_dir, vid_dir.name, note)
        else:
            print(f"{vid_dir.name}: SKIPPED — {note}")


if __name__ == "__main__":
    main()
