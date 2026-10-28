---
name: WalletMatcher
order: 9
built: 2026-07-28
area: crypto
tagline: "Paste a Solana wallet and find the other wallets the same person controls."
stack: [Next.js, Solana RPC]
link: { kind: live, url: "https://wallet-matcher.vercel.app" }
---
Starting from one address, or a set you believe belong together, it walks the
transaction graph and ranks connected wallets by how likely each one is to be a
real person rather than an exchange, program, bot or dust account.

- Two scores per wallet: how strongly it's linked, and how human it looks
- Filters out exchanges, programs and dust before ranking
- Ranking changes are tested against saved runs on known wallet groups
