---
name: ScottStats
built: 2026-01-26
area: markets
tagline: "My trading dashboard — stock and crypto breakouts, refreshed every few minutes."
stack: [React, Vercel Functions, Turso, QStash, ECharts]
link: { kind: live, url: "https://scott-stats.vercel.app" }
clip: /clips/scottstats.mp4
poster: /clips/scottstats.jpg
---
A scanner and charting app built around one swing-trading strategy. Quotes and
candles refresh every 3 minutes during the US session and less often overnight,
pulling from Yahoo Finance, Hyperliquid, CoinGecko and FRED.

- Flags breakout setups and logs every signal so they can be reviewed later
- Watchlists by sector: software, space, robotics, consumer and more
- Macro panel built from FRED series such as M2 money supply
- Indicator logic is checked against a separate Python reference implementation
