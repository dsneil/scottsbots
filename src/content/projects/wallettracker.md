---
name: BiKnow
order: 2
built: 2026-08-13
area: crypto
tagline: "Realtime blockchain transaction tracker for curated set of 1000+ wallets, processing thousands of txns/day."
stack: [Next.js, Supabase Realtime, Helius webhooks, Tailwind]
link: { kind: live, url: "https://wallettrackerapp.vercel.app", note: Login required }
---
Add wallets to a watchlist and their on-chain activity shows up in a live feed
without reloading. Solana arrives via Helius webhooks; EVM chains are polled.

- Live feed filtered by wallet or transaction type
- Token view: who in the watchlist holds, bought or sold each token, down to single trades
- Labels and tags for every wallet; the webhook updates itself when the list changes
