---
name: BiKnow
order: 4
built: 2026-08-13
area: crypto
tagline: "Live trades from a watchlist of Solana and EVM wallets, as they happen."
stack: [Next.js, Supabase Realtime, Helius webhooks, Tailwind]
link: { kind: live, url: "https://wallettrackerapp.vercel.app", note: Login required }
---
Add wallets to a watchlist and their on-chain activity shows up in a live feed
without reloading. Solana arrives via Helius webhooks; EVM chains are polled.

- Live feed filtered by wallet or transaction type
- Token view: who in the watchlist holds, bought or sold each token, down to single trades
- Labels and tags for every wallet; the webhook updates itself when the list changes
