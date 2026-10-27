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
| `clip`, `poster` | Paths under `public/clips/`; omit for the "Clip coming" placeholder |

## Clips

20–40 s, muted, H.264 MP4 (or WebM), 16:10, 2–4 MB, in `public/clips/<slug>.mp4` with a
`<slug>.jpg` poster. Longer walkthroughs go on YouTube (unlisted).
