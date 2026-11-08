# The Morning Brief — show bible

Instructions for whoever writes each day's episode. Follow them exactly.

## Listener
Sophie, 27, a Jewish woman from New York living in Israel. Her background is
MARKETING (about 5 years, incl. growth marketing at a cybersecurity startup), not
sales. Job-hunting in tech/cybersecurity marketing / go-to-market roles. Never
describe her as a salesperson; frame career takeaways from a marketer's angle.
Co-founding an art agency. Loves celebs, fashion, culture. Still learning
politics and world-news vocabulary.

## Format
ONE episode a day, about 30 minutes, live by 8:00 Israel time, in two parts:
- **Part 1: Sophie's interests** (~20 minutes, 2,700–2,900 words of spoken
  script): Israeli and world politics and news, pop culture, travel, and
  anything trending. No cybersecurity deals, funding or hires here.
- **Part 2: Cyber Watch** (~10 minutes, 1,300–1,500 words): cyber funding,
  acquisitions, executive hires and how cyber companies market and sell. This is
  for her job search (see "Part 2: Cyber Watch" below).
- Total about 4,200 words. Both parts live in the same script file.
- Single host, "smart briefing" tone: clear, warm, fast. What happened and why it
  matters to her. Light personality, no fake banter, no filler.
- Written for the ear: short sentences, no bullet lists, no URLs, no tables, no
  emojis, no abbreviations a voice would stumble on (write "percent", "million",
  "US", "AI" is fine). Spell out numbers that read oddly.
- Real news only, found by searching (see "How to pick stories" below). Check the
  date of every item. Never invent stories, quotes, facts or numbers. If a segment
  has a slow day, shorten it and give the time to a busier one. Never pad.

## Depth: explain, don't just report (IMPORTANT)
Sophie wants to actually understand each story, not just hear that it happened.
Prefer fewer stories told properly over many stories in one line each.
- Every company: say what it does in plain words, how big/known it is, and
  where it's based, the first time it's mentioned ("Wiz, the Israeli cloud
  security company Google bought for 32 billion dollars").
- Every person: their role AND what that role means ("the CRO, chief revenue
  officer, the executive in charge of sales"; "the attorney general, the
  government's top lawyer, who in Israel is independent from the ministers").
  Spell out every job-title acronym (CEO, CMO, CISO, VP, etc.) until the glossary
  says she knows it.
- Conflicts, protests, riots, strikes, wars, political fights: always cover
  WHO is involved, WHAT happened, HOW it started (the trigger), WHY (the deeper
  background: the history, the grievance, what each side wants), and WHAT'S NEXT.
  Give each side's view fairly. This usually takes 6-10 sentences, not 2.
- Numbers need context: is 50 million dollars big for this kind of company?
  Is this poll a change from last week?
- After the main facts of a big story, add one line on why it matters to Sophie
  or to Israel/New York.

## Part 1: Sophie's interests (rundown, approx. minutes)
1. Cold open (30 sec): date, "Good morning Sophie", the 3 biggest stories of the
   day in one line each (from either part).
2. Israel news & politics (6): government, elections, security, the economy,
   society. Explain the background (see Depth).
3. World news & politics (5): the biggest international stories, US politics
   included; explain who, what, why.
4. Pop culture (4): celebrities, entertainment, fashion, music, TV and film.
5. Travel (2): one destination, trend or practical travel story (new routes from
   Tel Aviv, festivals, a great city break, travel deals and rules).
6. Trending (2): what people are talking about online this week (see "What
   people are talking about" below), confirmed in real news sources.
7. Bridge (10 sec): "Now, Part 2, your Cyber Watch."

Use a spoken transition between segments ("Next, around the world...").

## Part 2: Cyber Watch (rundown, ~10 minutes)
Sophie's daily cyber watch, the part she relies on for her job search. Focus on
the last ~48 hours (since the previous episode); older items only if they haven't
been covered in the last 7 days of episodes. Israeli and Israel-founded companies
first. Cyber deals and hires appear ONLY in Part 2, never in Part 1.
1. Funding & acquisitions (~3.5 min): cybersecurity rounds from pre-seed to late
   stage, companies coming out of stealth with funding, and acquisitions. For each:
   what the company does in plain words, round and amount, lead investor, and
   whether that's big for its stage. Merge the same round reported by several
   outlets into one story.
2. Executive hires (~2.5 min): new CMOs, VPs/Heads of Marketing and other marketing
   leaders first, then CEOs, CROs, GTM, Sales and Partnerships leaders at cyber
   companies; big hiring pushes (a new Israel office) and notable layoffs. Say where
   the person came from when it's reported.
3. How cyber companies market and sell (~2.5 min): campaigns, events, positioning
   shifts, pricing and packaging, partnerships and channels, AI in go-to-market.
   Explain what they did and why it works or doesn't, from a marketer's angle.
4. Worth a look for you (~1.5 min): 1–3 items from today that could mean a
   marketing or GTM role for Sophie (e.g. a Seed–Series B Israeli company that
   just raised, or a new CMO likely to build a team), and why in a sentence or two.
5. Sign-off (10 sec).
Skip product launches, vulnerability/breach news and opinion pieces in Part 2. On
a slow cyber day, Part 2 can be shorter (even 6–7 minutes); never pad.

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
Save the whole episode (both parts) to `episodes/YYYY-MM-DD.md`:

```
---
title: <short catchy episode title, max 60 chars>
summary: <one sentence listing the top 3 stories>
---
<script paragraphs, separated by blank lines>
```

Segment headings may be written as lines starting with `## ` (e.g. `## Part 2:
Cyber Watch`); they are NOT read aloud (they just add a short pause), so the
spoken transition must be in the text. No recap files.
When checking for repeats, read every script from the last 7 days: before
2026-11-09 some days were split into `YYYY-MM-DD.md` + `YYYY-MM-DD-cyber.md`.

## How to pick stories
- Search wide, then choose: for each segment, look at the last ~7 days of news,
  not just today. Pick the stories that matter most, with a strong preference for
  the newest ones.
- An older story (2-7 days) earns a spot only if it's big, still developing, or
  hasn't been covered in the last 7 days of episodes.
  If it's older, say so naturally ("in case you missed it, last Thursday...").
- Never repeat a story covered in the last 7 days unless there's genuinely new news on it.
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
  amny.com/news, calcalistech.com/ctechnews, techcrunch.com, securityweek.com (incl. its funding
  and "people on the move" roundups), globes.co.il/en, geektime.com, siliconangle.com,
  PR Newswire / Business Wire press releases,
  goodmorningamerica.com/culture, news.artnet.com, theartnewspaper.com.
- Don't mention where Sophie is or her own trips; she's based in Israel and also
  follows New York closely.
