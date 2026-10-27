---
name: PolyStats
built: 2026-02-03
area: markets
tagline: "A Chrome extension that shows who is holding each side of a Polymarket bet."
stack: [TypeScript, Chrome Extension MV3, Goldsky subgraphs, IndexedDB]
link: { kind: soon }
---
Polymarket shows prices and an order book but not who holds the positions. This
extension adds a Holders panel to every market page, styled to match the site.

- Top YES and NO holders with position size in USDC
- Average entry price for each holder, from Polymarket's public PnL subgraph
- Hover a holder to see their profile and stats
- Private wallet tags, stored only in your browser
