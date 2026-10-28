# scottsbots

Personal project gallery: one page per project, a short demo clip, and a link to the live app or the code.

Astro 5 (static) + Tailwind 4. Deploys to Vercel.

## Commands

    npm install
    npm run dev       # http://localhost:4321
    npm run build     # -> dist/

## Add or edit a project

One Markdown file per project in `src/content/projects/`. Schema: `src/content.config.ts`.

| Field | Meaning |
|---|---|
| `built` | Repo creation date; cards sort by it |
| `area` | markets / crypto / cards / home / money |
| `link.kind` | `live` (open app) / `code` (public repo) / `soon` (repo going public) / `none` (clip only) |
| `link.note` | Short caveat shown next to the link, e.g. "Login required" |
| `order` | Home page position; projects without one follow, oldest first |
| `featured` | `true` = full-width row on the home page |
| `clip`, `poster` | Paths under `public/clips/`; omit for the "No signal" placeholder |

## Clips

Muted H.264 MP4, kept at the source resolution, in `public/clips/<slug>.mp4` with a
`<slug>.jpg` poster. Cards on the home page show the poster only; the video plays on the project page.
Any aspect ratio works on the project page; cards crop the poster to 16:10 from the top.
