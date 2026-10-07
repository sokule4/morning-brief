"""Turn an episode script into an MP3 and refresh the podcast feed.

Usage: python scripts/build.py episodes/2026-10-07.md
Env:   GITHUB_REPOSITORY (owner/repo), TTS_VOICE (optional)
"""
import asyncio, json, os, re, sys, datetime, html
from email.utils import format_datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
OUT = ROOT / "out"
VOICE = os.environ.get("TTS_VOICE", "en-US-AvaMultilingualNeural")
RATE = os.environ.get("TTS_RATE", "+5%")
KEEP = 30  # episodes kept in the feed
SHOW_TITLE = "Sophie's Morning Brief"
SHOW_DESC = "A daily 30-minute news briefing made just for Sophie."


def parse(md_path):
    text = Path(md_path).read_text(encoding="utf-8")
    meta = {}
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"')
        text = text[m.end():]
    chunks = []
    for para in re.split(r"\n\s*\n", text):
        p = para.strip()
        if not p:
            continue
        if p.startswith("#"):
            chunks.append(None)  # pause marker
            continue
        p = re.sub(r"[*_`>]", "", p)
        p = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", p)
        p = re.sub(r"\s+", " ", p)
        chunks.append(p)
    return meta, chunks


async def tts(text, path):
    import edge_tts
    for attempt in range(5):
        try:
            await edge_tts.Communicate(text, VOICE, rate=RATE).save(str(path))
            if path.stat().st_size > 0:
                return
        except Exception as e:  # network hiccups
            print(f"  retry {attempt + 1}: {e}")
            await asyncio.sleep(3 * (attempt + 1))
    raise RuntimeError(f"TTS failed for: {text[:60]}")


def make_audio(chunks, mp3_path):
    import subprocess
    work = OUT / "parts"
    work.mkdir(parents=True, exist_ok=True)
    for f in work.glob("*"):
        f.unlink()
    silence = work / "pause.mp3"
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "lavfi", "-i",
                    "anullsrc=r=24000:cl=mono", "-t", "1.2", "-q:a", "9", str(silence)], check=True)
    parts = []
    for i, c in enumerate(chunks):
        if c is None:
            parts.append(silence)
            continue
        p = work / f"{i:04d}.mp3"
        print(f"  voicing part {i + 1}/{len(chunks)}")
        asyncio.run(tts(c, p))
        parts.append(p)
    listfile = work / "list.txt"
    listfile.write_text("".join(f"file '{p.resolve()}'\n" for p in parts))
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0",
                    "-i", str(listfile), "-ac", "1", "-ar", "24000", "-b:a", "48k",
                    str(mp3_path)], check=True)


def duration(mp3_path):
    from mutagen.mp3 import MP3
    return int(MP3(str(mp3_path)).info.length)


def write_feed(episodes, repo):
    owner, name = repo.split("/")
    site = f"https://{owner.lower()}.github.io/{name}/"
    items = []
    for ep in episodes:
        d = datetime.datetime.fromisoformat(ep["date"]).replace(
            hour=5, tzinfo=datetime.timezone.utc)
        items.append(f"""    <item>
      <title>{html.escape(ep['title'])}</title>
      <description>{html.escape(ep['summary'])}</description>
      <pubDate>{format_datetime(d)}</pubDate>
      <guid isPermaLink="false">{ep['date']}</guid>
      <enclosure url="{ep['url']}" length="{ep['bytes']}" type="audio/mpeg"/>
      <itunes:duration>{ep['seconds']}</itunes:duration>
      <itunes:explicit>false</itunes:explicit>
    </item>""")
    feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
  <channel>
    <title>{SHOW_TITLE}</title>
    <link>{site}</link>
    <description>{SHOW_DESC}</description>
    <language>en-us</language>
    <itunes:author>Claude</itunes:author>
    <itunes:image href="{site}cover.jpg"/>
    <itunes:explicit>false</itunes:explicit>
    <itunes:block>Yes</itunes:block>
{chr(10).join(items)}
  </channel>
</rss>
"""
    (DOCS / "feed.xml").write_text(feed, encoding="utf-8")


def main(md_path, audio=True):
    repo = os.environ.get("GITHUB_REPOSITORY", "owner/morning-brief")
    date = Path(md_path).stem
    meta, chunks = parse(md_path)
    OUT.mkdir(exist_ok=True)
    mp3 = OUT / f"{date}.mp3"
    if audio:
        make_audio(chunks, mp3)
    episodes = json.loads((DOCS / "episodes.json").read_text())
    episodes = [e for e in episodes if e["date"] != date]
    episodes.append({
        "date": date,
        "title": meta.get("title", f"Morning Brief {date}"),
        "summary": meta.get("summary", ""),
        "url": f"https://github.com/{repo}/releases/download/ep-{date}/{date}.mp3",
        "bytes": mp3.stat().st_size,
        "seconds": duration(mp3),
    })
    episodes.sort(key=lambda e: e["date"], reverse=True)
    dropped = episodes[KEEP:]
    episodes = episodes[:KEEP]
    (DOCS / "episodes.json").write_text(json.dumps(episodes, indent=2))
    (OUT / "dropped.txt").write_text("\n".join(e["date"] for e in dropped))
    write_feed(episodes, repo)
    print(f"Built {mp3} ({episodes[0]['seconds'] // 60} min)")


if __name__ == "__main__":
    main(sys.argv[1], audio="--no-audio" not in sys.argv)
