---
name: Fomo Wallet Surfacer
built: 2026-08-17
area: crypto
tagline: "A Chrome extension that shows the real wallets behind fomo traders."
stack: [JavaScript, Chrome Extension MV3, Chainbase, Helius, Blockscout]
link: { kind: none, note: Private extension }
clip: /clips/fomo-wallet-surfacer.mp4
poster: /clips/fomo-wallet-surfacer.jpg
---
fomo shows each holder's handle and balance but never their wallet address. The
extension recovers it by matching each holder's balance against the token's real
on-chain holder list, then adds a copy button next to the name.

- Copy buttons on the token holders list, the top traders list and trader profiles
- Solana and EVM wallets linked per trader; one EVM match covers Base, BNB, Ethereum and Robinhood Chain
- Abstains instead of guessing: when a balance fits more than one wallet, it shows the shortlist
- Caches every match, so each token's holder list is looked up once
