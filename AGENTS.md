# scottsbots

- Astro 5 is pinned on purpose: local Node is 22.22 and Astro 7 needs >=22.23.4.
- Project content lives in `src/content/projects/*.md`. Write copy only from facts in each project's repo; no invented numbers.
- Design tokens are in `src/styles/global.css` (`:root` + dark overrides). The yellow label tape (`.tape`) is the only loud element; keep everything else quiet.
- Check after a change: `npm run build`, then screenshot at 1440px and 390px wide in light and dark mode; `scrollWidth` must equal the viewport width.
