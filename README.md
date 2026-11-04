# Sophie's Morning Brief

A private daily news podcast, fully automated.

1. Every morning a Claude scheduled task researches the news and writes two
   episodes: the ~20-minute Morning Brief `episodes/YYYY-MM-DD.md` and the
   ~10-minute Cyber Brief `episodes/YYYY-MM-DD-cyber.md` (rules in `SHOW.md`,
   word list in `glossary.json`), each with a `.recap.txt` for WhatsApp.
2. The push triggers `.github/workflows/publish.yml`, which voices both scripts
   (free Microsoft neural voice via edge-tts), uploads the MP3 as a GitHub
   release, updates `docs/feed.xml` and sends one WhatsApp recap for the day.
3. GitHub Pages serves the feed: `https://<user>.github.io/<repo>/feed.xml`.

Change the voice: Settings → Secrets and variables → Actions → Variables →
`TTS_VOICE` (e.g. `en-US-JennyNeural`, `en-US-AriaNeural`, `en-GB-SoniaNeural`).
Re-run a day (both episodes): Actions → Publish episode → Run workflow → date.
