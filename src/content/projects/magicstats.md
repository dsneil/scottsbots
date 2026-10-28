---
name: MagicStats
order: 4
built: 2026-10-21
area: cards
tagline: "Price history, sales data, and market depth on all sealed Magic sets. Sentiment analysis from 500+ videos."
stack: [Python, Postgres, Next.js, Drizzle, Recharts]
link: { kind: live, url: "https://magicthestats.vercel.app" }
clip: /clips/magicstats.mp4
poster: /clips/magicstats.jpg
---
A daily pipeline extracts sealed product prices and card data, including sales,
market depth, price changes, and inventory, to better understand the sealed
market. 700+ AlphaInvestments69 videos covering 3 years of market analysis were
also extracted for sentiment and qualitative insights.

- Daily pipeline tracks 243 sets and 3,100+ products, building history on key market metrics from 6 sources
- Ongoing analysis of AlphaInvestments69 YouTube videos: 3 years of sealed-market commentary, 7,100 extracted calls
- In progress: a scoring mechanism to read market trends and inform purchase decisions
