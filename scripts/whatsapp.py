"""Send the day's recap to Sophie on WhatsApp via CallMeBot (free, personal use).

Needs repo secrets WHATSAPP_PHONE (e.g. +9725xxxxxxx) and CALLMEBOT_APIKEY.
Silently skips if they're missing.
"""
import json, os, sys, time, urllib.parse, urllib.request
from pathlib import Path

phone = os.environ.get("WHATSAPP_PHONE", "").strip()
key = os.environ.get("CALLMEBOT_APIKEY", "").strip()
if not phone or not key:
    print("WhatsApp not configured; skipping.")
    sys.exit(0)

date = sys.argv[1]
ep = next(e for e in json.load(open("docs/episodes.json")) if e["date"] == date)
recap_file = Path(f"episodes/{date}.recap.txt")
body = recap_file.read_text(encoding="utf-8").strip() if recap_file.exists() else ep["summary"]
mins = round(ep["seconds"] / 60)
text = (f"*🎙️ Morning Brief · {date}*\n*{ep['title']}*  ({mins} min)\n\n{body}\n\n"
        f"▶️ It's in your podcast app now.")

url = ("https://api.callmebot.com/whatsapp.php?" +
       urllib.parse.urlencode({"phone": phone, "text": text, "apikey": key}))
for attempt in range(3):
    try:
        with urllib.request.urlopen(url, timeout=60) as r:
            out = r.read().decode("utf-8", "replace")
        print(r.status, out[:300])
        if r.status == 200:
            break
    except Exception as e:
        print("retry:", e)
    time.sleep(20)
