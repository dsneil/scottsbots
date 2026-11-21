# Resume session handoff (2026-11-20)

Paste the prompt below into a new Claude Code session started in `~/Projects/scottsbots`.

---

You are continuing work on my resume, which lives on my personal site **scottsbots** (Astro 5 + Tailwind 4, `~/Projects/scottsbots`, public repo `dsneil/scottsbots`, Vercel; push to `main` auto-deploys). Live: https://scottsbots.xyz/resume/ (www 308s to apex; scottsbots.vercel.app also works). Use scottsbots.xyz everywhere. scottsbots.io has no DNS; scottsbots.com is someone else's site.

## Read first

| File | Role |
|---|---|
| `src/data/resume.ts` | All resume copy: constants (LinkedIn, `CONTACT_EMAIL`, `PDF_PATH`, `SITE_HOST`), `INLINE_LINKS` map (text in bullets that renders as a link), `EXPERIENCE`, `EDUCATION`. Source of truth for current wording. |
| `src/pages/resume.astro` | Page: header (name, tagline, links), Experience, Education. Tagline is hard-coded here. Print styles via Tailwind `print:` variants + scoped `<style>`. |
| `src/styles/global.css` | Print block: black on white, html 10px, `@page` 14mm margins. |
| `docs/resume-archive.md` | Every retired line with its rollback commit, plus an Idea bank of sourced facts not on the page. |
| `scripts/resume-pdf.py` | Exports /resume/ (print media, US Letter) to `public/Scott-Neil-Resume.pdf` and copies it to `~/Projects/JobSearch/resume/Scott-Neil-Resume.pdf`. Prints page count + links; exits nonzero if not 1 page. Needs dev server on :4321. |
| `public/Scott-Neil-Resume.pdf` | Served at https://scottsbots.xyz/Scott-Neil-Resume.pdf by the web Download link. |
| `AGENTS.md` | Repo rules (resume rule on line 7; overflow-check rule). |

## Loop for every resume change

1. Archive the replaced text in `docs/resume-archive.md` ("Earlier one-liners", newest first) with the last commit that had it.
2. Edit `src/data/resume.ts` (or `resume.astro` for header/tagline/layout).
3. `npm run build 2>&1 | grep -E 'page\(s\) built|rror'`
4. Dev server: `npx astro dev --port 4321` (start it in the background if not running), then `python3 scripts/resume-pdf.py`. Must print `1 page(s)`.
5. Layout changes: check no horizontal overflow (scrollWidth == viewport) at 1440 and 390 px, light and dark (Playwright).
6. Commit (include `public/Scott-Neil-Resume.pdf`), push to `main`.
7. Poll https://scottsbots.xyz/resume/ until the change is live.
8. Show `~/Projects/JobSearch/resume/Scott-Neil-Resume.pdf` in the side panel.

## Constraints

- PDF must stay **1 page**. About 1 line of headroom. A bullet that wraps one extra line can push it to 2 pages; measure line counts (li height minus padding, divided by line-height) and offer trims.
- Use my wording nearly verbatim. Only fix tense/apostrophes/typos, and flag each fix in the reply.
- No invented numbers. Sources: LinkedIn (I supply screenshots; LinkedIn can't be fetched), the 2015 resume, project repos, public stats.
- Public contact = LinkedIn + Contact mailto `workwithscottn@gmail.com`. No phone number anywhere. Do not use any other email of mine.
- Do not open personal HR documents (offer letters, exit packets, performance reviews, visa files).
- Never print or commit secrets.

## Current state (all committed and pushed)

- Header (web): name (Doto, `clamp(2.1rem,7vw,3.8rem)`), tagline "AI Product Manager and Data Scientist at Meta for 8 years. Self-employed since 2022.", links LinkedIn ↗ · Contact ✉ · Download PDF ↓ (web only).
- Header (PDF): LinkedIn ↗ · Contact ✉ · Website ↗ (print only). Contact in the PDF is a clickable mailto; the address isn't printed.
- Sections: Self-employed 2022 – Present (Social media, Startup consulting, Trading & crypto, Personal projects); Meta 2013 – 2021 (AI Product Manager · Messenger Business AI; Data Scientist, Analytics · Instagram Core Business; Data Scientist, Analytics · Facebook Videos; Product Analyst Intern · Facebook Groups); Other (Periscope Capital, BMO Capital Markets); Education (University of Waterloo, BASc Systems Design Engineering).
- Inline links: `scottsbots.xyz` → site, `@fashionbyally` → Instagram.

## Decisions already made (don't relitigate)

| Decision | Reason |
|---|---|
| "partner", not "wife" | Targeting tech jobs |
| Click-to-Message spelled out on first use, then "CTM" | User request |
| Tagline says 8 years | Counts the 2013 internship |
| Videos: 10B+ daily views; eng team "grew over 5x" | User figures |
| Locations and early dates removed; early roles collapsed into "Other" | Space and relevance |
| Download link hidden in print | A download link inside the PDF is circular |
| Name heading reduced | User request |

## Research done (reuse, don't redo)

- Data science job-posting keyword pass, already applied: north-star/guardrail metrics, A/B test design and ship decisions, partnering with Product/Eng, opportunity sizing, pipelines/self-serve dashboards, influencing leadership. Unused: tools list (SQL, Python, Hive, Tableau).
- Public stats used: Facebook video 8B daily views (Nov 2015); Instagram business profiles 15M → 25M in 2017.

## Parked (not resume)

- WalletMatcher on the site returns RPC 429. Hypothesis is in memory `scottsbots-site.md`. Ask before reading env files.
- Some project clips are missing; the user will supply the Wallet Tracker clip.

Start by reading the files above and showing me the current PDF. Then wait for my edits.
