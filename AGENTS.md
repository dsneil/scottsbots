# scottsbots

- Astro 5 is pinned on purpose: local Node is 22.22 and Astro 7 needs >=22.23.4.
- Project content lives in `src/content/projects/*.md`. Write copy only from facts in each project's repo; no invented numbers.
- Design: minimal retro-robotic. Tokens in `src/styles/global.css` (`:root` + dark overrides). Monospace only (IBM Plex Mono); square-dot Doto (`.dot`, ROND 0) for the name plate and unit names. No rounded corners, shadows or heavy display type; 1px square rules; the red `.led` is the only color.
- Check after a change: `npm run build`, then screenshot at 1440px and 390px wide in light and dark mode; `scrollWidth` must equal the viewport width.
- Resume: copy in `src/data/resume.ts`, page `src/pages/resume.astro`. After any resume change run `python3 scripts/resume-pdf.py` (dev server on :4321) and commit `public/Scott-Neil-Resume.pdf` with it; the Download link serves that file. PDF must stay 1 page. Archive replaced copy in `docs/resume-archive.md`.
