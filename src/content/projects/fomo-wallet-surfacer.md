---
name: fomo Wallet Matcher
order: 5
built: 2026-08-17
area: crypto
tagline: "A Chrome extension that shows the real wallets behind fomo traders."
stack: [JavaScript, Chrome Extension MV3, Chainbase, Helius, Blockscout]
link: { kind: none, note: Private extension }
clip: /clips/fomo-wallet-surfacer.mp4
poster: /clips/fomo-wallet-surfacer.jpg
---

fomo is a popular social trading app, but it intentionally obfuscates each trader's address.
Knowing the exact wallet address is useful for my analysis, understanding and tracking. It is
possible to do manually, but this tool automatically looks at on-chain data to identify and
surface each trader's associated wallet addresses.

- Looks at on-chain data around token holdings, bridge transactions and funding events to link wallet addresses across chains to trader profiles
- Surfaces wallets in place for quicker analysis and tracking
- Fuzzy matches are surfaced to the user to select the correct pairing
