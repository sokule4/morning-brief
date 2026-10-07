# Sophie's Morning Brief

A private daily news podcast, fully automated.

1. Every morning a Claude scheduled task researches the news and writes
   `episodes/YYYY-MM-DD.md` (rules in `SHOW.md`, word list in `glossary.json`).
2. The push triggers `.github/workflows/publish.yml`, which voices the script
   (free Microsoft neural voice via edge-tts), uploads the MP3 as a GitHub
   release, and updates `docs/feed.xml`.
3. GitHub Pages serves the feed: `https://<user>.github.io/<repo>/feed.xml`.

Change the voice: Settings → Secrets and variables → Actions → Variables →
`TTS_VOICE` (e.g. `en-US-JennyNeural`, `en-US-AriaNeural`, `en-GB-SoniaNeural`).
Re-run a day: Actions → Publish episode → Run workflow → date.
