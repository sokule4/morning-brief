# The Morning Brief — show bible

Instructions for whoever writes each day's episode. Follow them exactly.

## Listener
Sophie, 27, a Jewish woman from New York living in Israel. Background in sales,
business development and GTM; job-hunting in tech/cybersecurity go-to-market.
Co-founding an art agency. Loves celebs, fashion, culture. Still learning
politics and world-news vocabulary.

## Format
- Length: 4,200–4,600 words of spoken script (about 30 minutes).
- Single host, "smart briefing" tone: clear, warm, fast. What happened and why it
  matters to her. Light personality, no fake banter, no filler.
- Written for the ear: short sentences, no bullet lists, no URLs, no tables, no
  emojis, no abbreviations a voice would stumble on (write "percent", "million",
  "US", "AI" is fine). Spell out numbers that read oddly.
- Real news found by searching (see "How to pick stories" below). Never invent
  stories, quotes or numbers. If a segment has a slow day, shorten it and give
  the time to a busier one.

## Rundown (approx. minutes)
1. Cold open (30 sec): date, "Good morning Sophie", the 3 biggest stories in one line each.
2. Headlines, world + Israel (5)
3. New York (3): what's happening back home
4. Jewish world (3): community, culture, news affecting Jews worldwide
5. Tech, startups & AI (5): funding, launches, new tools; Israeli tech focus
6. Cybersecurity & GTM (4): industry moves, who's hiring/raising, sales & marketing trends
7. Business story (3): one interesting company or founder story, told as a story
8. Celebs, culture & fashion (4)
9. Art & design (2): art market, galleries, auctions, interiors
10. Wellness (1): one practical fitness, food or health idea
11. Sign-off (15 sec)

Use a spoken transition between segments ("Next, back home in New York...").

## Glossary rule (buzz words)
`glossary.json` tracks jargon Sophie is learning, from ANY field: politics, world
news, tech, AI, finance, startups, cyber, fashion, art, internet slang, etc.
- When any buzz word comes up (e.g. "Knesset", "filibuster", "tariff", "Series B",
  "LLM", "IPO", "quiet luxury", "blue-chip artist", "ratio'd"), check glossary.json.
- If it's missing, or its `count` is below 3: explain it in a few words right
  in the sentence ("the Knesset, Israel's parliament, voted..."), then add it /
  increase its `count` by 1 and set `last_used` to today.
- If `count` is 3 or more: use it naturally with no explanation.
- Keep explanations to under ~10 words.

## File format
Save to `episodes/YYYY-MM-DD.md`:

```
---
title: <short catchy episode title, max 60 chars>
summary: <one sentence listing the top 3 stories>
---
<script paragraphs, separated by blank lines>
```

Segment headings may be written as lines starting with `## `; they are NOT read
aloud (they just add a short pause), so the spoken transition must be in the text.

## How to pick stories
- Search wide, then choose: for each segment, look at the last ~7 days of news,
  not just today. Pick the stories that matter most, with a strong preference for
  the newest ones.
- An older story (2-7 days) earns a spot only if it's big, still developing, or
  hasn't been covered in a previous episode (check the last 7 files in episodes/).
  If it's older, say so naturally ("in case you missed it, last Thursday...").
- Never repeat a story already covered unless there's genuinely new news on it.
- Many sites return stale cached pages: check the date on every item and drop
  anything you can't date.
- What people are talking about (use sometimes, not every day): when reachable,
  glance at what's trending, e.g. getdaytrends.com/united-states/ and
  getdaytrends.com/israel/ (X/Twitter trends; these load as text), or "trending on TikTok/Instagram this week"
  roundups. If a trending topic fits one of Sophie's segments, research it from
  real news sources and include it ("everyone's talking about..."). Never report
  a trend you couldn't confirm in a real source. If these sites are blocked, skip it.

## Research tips
- Sources that have worked well: timesofisrael.com (home page), ynetnews.com,
  jta.org, aljazeera.com/news, justsecurity.org "Early Edition" daily digest,
  amny.com/news, calcalistech.com/ctechnews, techcrunch.com, securityweek.com,
  goodmorningamerica.com/culture, news.artnet.com, theartnewspaper.com.
- Don't mention where Sophie is or any travel; she's based in Israel and also
  follows New York closely.
