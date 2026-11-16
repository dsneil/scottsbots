# Resume archive

Retired resume copy, kept for rollback and for pulling ideas back in. Live copy lives in
`src/data/resume.ts`; the page is `src/pages/resume.astro` (scottsbots.vercel.app/resume/).

Rollback a whole version: `git checkout <commit> -- src/data/resume.ts`, then build and push.

## 2026-11-16 · Locations and early dates removed (last version with them: `043a0a1`)

- Meta (then "Facebook"): Menlo Park, CA · 2014 – 2021 → now 2013 – 2021, internship moved back under Meta.
- Other: Periscope Capital · 2012 – 2013 (Toronto, ON); BMO Capital Markets · 2012 (Toronto, ON).
- Education: University of Waterloo · 2009 – 2014.

---

## 2026-11-16 · Early roles collapsed into "Other" (last full version: `a640fe9`)

**Product Analyst Intern** · Facebook Groups · 2013 (was under Meta)
- Identified and prioritized growth opportunities for Groups; defined metrics and built pipelines for ongoing analysis.

**Periscope Capital** · Toronto, ON · Investment Assistant / Technical Lead · 2012 – 2013
- Architected and built the internal accounting system; started the move to technology-centric operations.
- Analyzed and improved the automated trading system.

**BMO Capital Markets** · Toronto, ON · Fixed Income / Money Market Trading Analyst · 2012
- Co-developed and released a new money-market trading platform.
- Built the foundation for a real-time system delivering market and trade data to traders.

---

## 2026-11-16 · Since 2022 section removed (last commit with it: `5ff155b`)

| Label | Text |
|---|---|
| Personal projects | Designed, built and shipped 9 tools end to end: market dashboards, Chrome extensions, on-chain analytics and market-data pipelines, several running daily. |
| Contract startup work | Contract ML engineer at VAWN, an AI tool that reads electrical construction drawings. Took fire-alarm detection from nothing to 0.849 F1 on a locked test set and unified panel data across 3 sources. |
| Investing & trading | Invest and trade across stocks, crypto, prediction markets and sealed collectibles, using research tools I built for each market. |
| Social media | Content creation with @fashionbyally (1.5M+ followers across platforms) for brands such as Amazon, Apple, Waymo/Google, Four Seasons and United Airlines. Authored a travel guide that sold hundreds of copies. |

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

- Facebook Videos scale (commit `92a886b`): "…informed changes that helped grow Videos to 5B+ daily views." (5B+ came from the Sept 2015 resume; public reports had 8B by Nov 2015.)
- Tagline years (commit `6814412`): "AI Product Manager and Data Scientist at Meta for 7 years." (7 = 2014–2021 full-time; 8 counts the 2013 internship)
- Personal projects theme (commit `4464c81`): "General theme across projects is finding datasets and YouTube video catalogs and turning them into actionable tools."
- Facebook Videos team growth (commit `605bd5f`): "…as the engineering team grew 4x." (4x was the Sept 2015 resume figure)
- Facebook Videos bullet 2 (commit `58e48bf`): "Defined core metrics, ran A/B test design, evaluation and ship decisions on new Videos products." (trimmed to fit one line)
- Facebook Videos bullet 2 (commit `0fa4ca6`): "Defined core metrics and ran A/B test design, evaluation and ship decisions on new Videos products."
- Facebook Videos bullets 2–4 (commit `affdef4`): "Ran A/B test design, evaluation and ship decisions on new Videos products." / "Scaled analysis capacity via tooling, education and mentoring as the engineering team grew 4x." / "Defined core metrics and validated logging with Data Engineering; built datasets and dashboards." (4th removed)
- Facebook Videos bullets 1–2 (commit `01f874a`): "Through my tenure, led analytics for Performance, Live, Suggested Videos and Facebook Watch." / "Led A/B test design, evaluation and ship decisions on new Videos products; informed changes that helped grow Videos to 10B+ daily views."
- Facebook Videos second bullet (commit `31d92d4`): "Covered Performance, Live, Suggested Videos and Facebook Watch."
- Instagram API bullet (commit `d37d88b`, was first IG bullet): "Handled sensitive analytics projects around the Instagram API through a complex regulatory environment following Cambridge Analytica."
- Ads Optimization variant tried and reverted (commit `3d7a6a0`): "grew revenue and business transactions in Messenger…"; live copy back to "business outcomes".
- Ads Optimization first sentence (commit `815e172`): "grew revenue and adoption by improving ad delivery and models, driving more business outcomes in Messenger."
- Tagline (commit `e8e3caf`, in `src/pages/resume.astro`): "Product manager and data scientist at Meta for 7 years. Self-employed since 2022."
- CTM wording (commit `f4beaab`): Ads Optimization said "future version of CTM ads optimization"; Quality/Integrity ended "in Messenger and Click-to-Message ads."
- Groups intern (commit `44647ff`): "Sized and prioritized growth opportunities for Groups; defined metrics and built pipelines for ongoing analysis."
- Instagram first bullet (removed after `edcfb3e`): "Growth, Insights, API and Discovery."
- AI PM last bullet (removed after `edcfb3e`): "Also covered privacy for Messenger Business AI."
- Job-posting keyword pass (last version before it: `e606aeb`):
  - Videos: "Led experiment design, evaluation and decisions on new Videos products; informed changes that helped grow Videos to 10B+ daily views."
  - Videos: "Worked with Data Engineering on datasets, metrics, logging validation and dashboards."
  - Instagram: "Researched and prioritized projects to help businesses grow on Instagram through improved Insights and account tips."
  - Groups intern: "Identified and prioritized growth opportunities for Groups; defined metrics and built pipelines for ongoing analysis."
- Instagram Core Business (commit `92a886b`): single bullet "Growth, Insights, API and Discovery." before the API / Insights / pipelines bullets were added.
- AI PM quality bullets (commit `2f6bc37`): "Quality/Integrity: reduced bad and policy-violating ads across Messenger and Click-to-Message." and "Lead cross-company work to drive project alignment and consistently reduce bad and policy-violating ad experiences in Messenger and Click-to-Message ads."
- AI PM Growth bullet (commit `e4937d4`): "Growth: increased business outcomes from person-to-business conversations, feeding better models and more valuable conversations."
- Startup consulting (commit `b4a12f7`): "Iterated on the internal data engine (labeling and training tooling) to speed up dataset creation and labeling."
- Personal projects closer (commit `3f3a8ec`): "Common thread: finding datasets and YouTube video catalogs and turning them into actionable tools."
- Facebook Videos bullet (commit `e4d5208`): "Scaled the engineering team’s analysis through tooling, education and mentoring as the team grew 4x."
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
