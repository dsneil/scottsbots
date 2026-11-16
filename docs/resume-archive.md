# Resume archive

Retired resume copy, kept for rollback and for pulling ideas back in. Live copy lives in
`src/data/resume.ts`; the page is `src/pages/resume.astro` (scottsbots.vercel.app/resume/).

Rollback a whole version: `git checkout <commit> -- src/data/resume.ts`, then build and push.

---

## 2026-11-16 · Self-employed, role-by-role version (commit `98d5157`)

Replaced by the four-bullet Self-employed section (Social media, Trading/crypto, Startup
consulting, Personal projects).

### Self-employed · 2022 – Present

**Contract ML Engineer** · VAWN · AI electrical blueprint analysis · 2026
- Built fire-alarm device detection on construction drawings from zero: dataset, three model generations, tiled inference, false-positive filtering and the production pipeline. Locked-test F1 0.849; an unseen project scored 41 of 43 devices with zero false positives.
- Unified panels detected from single-line diagrams, schedule tables and floor plans into one record with per-field source authority. Breaker extraction rose from 0.596 to 0.872; every cross-source disagreement is logged as one of 19 issue types.
- Built labeling tools (template-match proposals, legend viewer, one-click box correction) that cut cross-class false positives from 54 per run to 0.
- Shipped chat answers that jump to the referenced panel on the drawing, and an upload flow that runs only the disciplines requested. 381 commits.

**Personal projects** · scottsbots · 2022 – Present
- MagicStats: daily pipeline over 243 sealed Magic sets and 3,100+ products from 6 sources, plus LLM extraction of 7,100 market calls from 700+ videos.
- BiKnow: real-time tracker of 1,000+ curated Solana wallets processing thousands of transactions a day; WalletMatcher clusters wallets the same person controls.
- PolyHolders and fomo Wallet Matcher: Chrome extensions that surface who holds each side of a Polymarket bet and the real wallets behind fomo traders.

**Investing & trading** · 2022 – Present
- ScottStats: real-time charting and breakout alerts over custom universes, including 500+ AI stocks across 20+ subsectors.
- Distilled a breakout strategy from a transcribed playlist of trading videos, with every rule cited to a quote and timestamp, then backtested and ported it into ScottStats.
- CMR Scorecard: turned 500+ market videos and reports into calls plotted on their charts.

**Social media** · @fashionbyally · 2022 – Present
- Work with my wife (@fashionbyally, 1.5M+ followers across platforms) on content creation: strategy, video concepting, videography and photography.
- Partnered with global brands including Amazon, Apple, Waymo/Google, Air France and Four Seasons Hotels.
- Authored a travel guide that sold hundreds of copies and drove thousands of newsletter subscribers.

### Since 2022 summary rows (unchanged at time of archive)

| Label | Text |
|---|---|
| Personal projects | Designed, built and shipped 9 tools end to end: market dashboards, Chrome extensions, on-chain analytics and market-data pipelines, several running daily. |
| Contract startup work | Contract ML engineer at VAWN, an AI tool that reads electrical construction drawings. Took fire-alarm detection from nothing to 0.849 F1 on a locked test set and unified panel data across 3 sources. |
| Investing & trading | Invest and trade across stocks, crypto, prediction markets and sealed collectibles, using research tools I built for each market. |
| Social media | Content creation with @fashionbyally (1.5M+ followers across platforms) for brands including Amazon, Apple, Waymo/Google, Air France and Four Seasons. Authored a travel guide that sold hundreds of copies. |

---

## Earlier one-liners

- Brand list (commit `1c3a54d`): "Partnered with global brands including Amazon, Apple, Waymo/Google, Air France and Four Seasons Hotels." Summary row: "…for brands including Amazon, Apple, Waymo/Google, Air France and Four Seasons."
- Social media & publishing (commit `c8ebcd2`): "Co-authored a travel guide that sold hundreds of copies, and gave away thousands of copies of free info products."
- Facebook role dates were briefly year-only (`e38e995`), reverted to month + year (`a3d1b50`).

## Idea bank

Facts with sources, not on the page right now:

- VAWN legend detection: legend pages found on 19/29 → 27/29 projects; fleet 92/137 → 130/137 (source: `Documents/PROJECTS/SCOTT-CONTRIBUTIONS-LINKEDIN.md`).
- VAWN fire-alarm dataset: 59 pages / 2,266 annotations; unseen holdout 41/43 devices, 0 false positives.
- VAWN labeling: precision 0.20 → 0.94 at equal recall; legend → plan cold start 16/18 smoke detectors from one exemplar.
- VAWN ground-truth migration: 393 tables / 55 projects / 1,179 breaker rows verified.
- Facebook Videos (2015 resume): team grew 4x; worked with Data Eng on datasets, metrics, logging validation, dashboards.
- Periscope Capital: architected internal accounting system (C#, SQL Server).
- Skura Corporation, Software Developer, May–Aug 2011 (2015 resume; not on LinkedIn screenshot).
- Waterloo projects: Adaptive Traffic Control (4th-year design), Divie asset-division tool.
