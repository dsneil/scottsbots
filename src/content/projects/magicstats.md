---
name: MagicStats
built: 2026-10-21
area: cards
tagline: "Price history and scores for sealed Magic: The Gathering products."
stack: [Python, Postgres, Next.js, Drizzle, Recharts]
link: { kind: live, url: "https://magicthestats.vercel.app" }
---
A daily pipeline collects sealed-product prices and card data, builds a catalog,
and scores each set as a long-term hold. The dashboard shows the results.

- Daily price snapshots per product, from several sources merged into one catalog
- Set scores built from price trends and supply events such as reprints
- Runs on a schedule: collect, build the catalog, load prices
