# Resume session handoff (updated 2026-11-21)

Self-contained: the new session runs on a different computer (Mac) with no Claude memory, no
`~/.claude` files and no Windows/WSL paths. Everything it needs is in this repo or below.

Paste the prompt below into a new Claude Code session started in the `scottsbots` repo root.
Companion doc for the job search: `resume/HANDOFF-scottsbots-resume.md` in the private
`dsneil/JobSearch` repo (overlaps this one; `src/data/resume.ts` wins any conflict).

---

You are continuing work on my resume, which lives on my personal site **scottsbots**. Earlier sessions on another computer did the work; this prompt is the full context. Read the files under "Read first" before changing anything.

## Project

| Item | Value |
|---|---|
| Repo | github.com/dsneil/scottsbots (**public**: never commit secrets or private contact data) |
| Stack | Astro 5.18 (pinned on purpose: Astro 7 needs Node ≥22.23.4) + Tailwind 4, static |
| Hosting | Vercel project `scottsbots`, git-linked: push to `main` auto-deploys |
| Domain | https://scottsbots.xyz (live 2026-11-16). www 308 → apex. scottsbots.vercel.app also works. Use scottsbots.xyz in all copy. scottsbots.io has no DNS; scottsbots.com is someone else's site. |
| DNS | GoDaddy: `A @ 216.150.1.1`, `A @ 216.150.16.1`, `CNAME www ffe2cdc60d038931.vercel-dns-016.com`. Ask before changing DNS or Vercel domain settings. |
| Resume page | https://scottsbots.xyz/resume/ |
| Resume PDF | https://scottsbots.xyz/Scott-Neil-Resume.pdf, served from `public/Scott-Neil-Resume.pdf` |

## Setup on a new machine

Node 22 (Astro 5 is pinned), Python 3.

```bash
git clone https://github.com/dsneil/scottsbots.git && cd scottsbots
npm install
pip3 install playwright && python3 -m playwright install chromium
```

Optional: clone `dsneil/JobSearch` next to it (same parent folder). The export script then also copies the PDF to `../JobSearch/resume/`; without it the script skips the copy.

## Read first

| File | Role |
|---|---|
| `AGENTS.md` | Repo rules: design tokens, check procedure, resume PDF rule |
| `src/data/resume.ts` | All resume copy: constants (LinkedIn, `CONTACT_EMAIL`, `PDF_PATH`, `SITE_HOST`), `INLINE_LINKS` (bullet text that renders as a link), `EXPERIENCE`, `EDUCATION`. Source of truth for current wording. |
| `src/pages/resume.astro` | Header (name, tagline, links), Experience, Education. Tagline is hard-coded here. Print styles via Tailwind `print:` variants + scoped `<style>`. |
| `src/styles/global.css` | Print block: black on white, html 10px, `@page` 14 mm margins |
| `docs/resume-archive.md` | Every retired line with its rollback commit, plus an Idea bank of sourced facts not on the page |
| `scripts/resume-pdf.py` | Exports /resume/ (print media, US Letter) to `public/Scott-Neil-Resume.pdf`. Prints page count + links; exits nonzero if not 1 page. Needs the dev server on :4321. |

## Loop for every resume change

1. Archive the replaced text in `docs/resume-archive.md` ("Earlier one-liners", newest first) with the last commit that had it.
2. Edit `src/data/resume.ts` (or `resume.astro` for header/tagline/layout).
3. `npm run build 2>&1 | grep -E 'page\(s\) built|rror'`
4. Start the dev server in the background if not running: `npx astro dev --port 4321`. Then `python3 scripts/resume-pdf.py`; it must print `1 page(s)`.
5. Layout changes: no horizontal overflow (`scrollWidth` == viewport) at 1440 and 390 px, light and dark (Playwright).
6. Commit (include `public/Scott-Neil-Resume.pdf`), push to `main`.
7. Confirm live: poll `curl -s https://scottsbots.xyz/resume/ | grep -c '<new phrase>'` (up to 20 tries, 10 s apart).
8. Show me `public/Scott-Neil-Resume.pdf` in the side panel.

## Constraints

- PDF must stay **1 page**; about 1 line of headroom. A bullet that wraps one extra line can push it to 2 pages. Measure line counts (li height minus padding, divided by line-height) and offer me trims rather than choosing words yourself.
- Use my wording nearly verbatim. Only fix tense/apostrophes/typos, and flag each fix in the reply.
- No invented numbers. Sources: LinkedIn (I paste screenshots; LinkedIn blocks fetching), my 2015 resume (facts already pulled into the archive's Idea bank), project repos, public stats.
- Public contact = LinkedIn + Contact mailto (address in `resume.ts`). No phone number anywhere. Use no other email of mine.
- Do not open personal HR documents (offer letters, exit packets, performance reviews, visa files).
- Never print or commit secrets; ask before reading any `.env*` file.
- Reply style: terse, result first, tables for results, decisions as interactive multiple-choice questions.

## Current state (all committed and pushed)

- Header (web): name (Doto, `clamp(2.1rem,7vw,3.8rem)`), tagline "AI Product Manager and Data Scientist at Meta for 8 years. Self-employed since 2022.", links LinkedIn ↗ · Contact ✉ · Download PDF ↓ (web only).
- Header (PDF): LinkedIn ↗ · Contact ✉ · Website ↗ (print only). Contact in the PDF is a clickable mailto; the address isn't printed.
- Sections: Self-employed 2022 – Present (Social media, Startup consulting, Trading & crypto, Personal projects); Meta 2013 – 2021 (AI Product Manager · Messenger Business AI; Data Scientist, Analytics · Instagram Core Business; Data Scientist, Analytics · Facebook Videos; Product Analyst Intern · Facebook Groups); Other (Periscope Capital, BMO Capital Markets); Education (University of Waterloo, BASc Systems Design Engineering).
- Inline links: `scottsbots.xyz` → site, `@fashionbyally` → Instagram.

## Decisions already made (don't relitigate)

| Decision | Reason |
|---|---|
| "partner", not "wife" | Targeting tech jobs |
| Click-to-Message spelled out on first use, then "CTM" | My request |
| "business outcomes" kept ("business transactions" tried, reverted) | My request |
| Tagline says 8 years | Counts the 2013 internship |
| Videos: 10B+ daily views; eng team "grew over 5x" | My figures |
| Instagram API bullet short, no Cambridge Analytica mention | My wording |
| Locations and pre-Meta dates removed; early roles collapsed into "Other" | Space and relevance |
| Download link hidden in print | A download link inside the PDF is circular |

## Research done (reuse, don't redo)

- Data science job-posting keyword pass, already applied: north-star/guardrail metrics, A/B test design and ship decisions, partnering with Product/Eng, opportunity sizing, pipelines/self-serve dashboards, influencing leadership. Unused: tools list (SQL, Python, Hive, Tableau).
- Public stats used: Facebook video 8B daily views (Nov 2015); Instagram business profiles 15M → 25M in 2017.

## Rest of the site (not resume)

- Design: minimal retro-robotic. Monospace only (IBM Plex Mono); square-dot Doto for the name plate and unit names. No rounded corners, shadows, bubbles or heavy display type ("Claude-like" was rejected). Details in `AGENTS.md`.
- Project pages: `src/content/projects/*.md`; copy only from facts in each project's repo.
- Clips: keep source resolution (no downscaling); re-encode muted H.264 CRF 20. Home page shows poster stills only; video plays only on the project page.
- Parked: WalletMatcher (wallet-matcher.vercel.app) returns `RPC 429: Too Many Requests` within ~5 s with UI defaults. HYPOTHESIS: the RPC provider refuses JSON-RPC batch payloads with HTTP 429; `isBatchRefusal` in the WalletMatcher repo's `lib/solana/rpc.ts` only treats 403/413 as a refusal, so it throws instead of falling back to single calls. Unconfirmed. Its app link was removed from the site (card reads "No public link"); no clip until fixed.
- Parked: Wallet Tracker demo clip; I will record it or send screenshots.

Start by reading the files above and showing me the current PDF. Then wait for my edits.
