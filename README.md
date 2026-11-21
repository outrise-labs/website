# Outrise website

Landing page for Outrise, a company building AI-agent products for people and businesses.

The page content is in Portuguese (pt-PT).

## Stack

- Static pages with inline CSS and JavaScript: `index.html` (Portuguese) and `en/index.html` (English), plus the privacy pages.
- The pages are generated from `tools/src.html` by `tools/build.py`, which fills in the logo path, translates the English page and writes the privacy pages. Run `python3 build.py [supabase_url] [publishable_key]` inside `tools/` and copy the output to the root.
- [three.js](https://threejs.org/) r128, loaded from cdnjs, renders the dot-grid visuals: the particle orbit in the hero and the diagonal light in the "Como trabalhamos" section.
- Outrise Sans, the brand typeface, self-hosted from `fonts/`. It is a modified version of [Albert Sans](https://github.com/usted/Albert-Sans) under the SIL Open Font License (`fonts/OFL.txt`).
- Geist Mono for labels, loaded from Google Fonts.

## Local development

Open `index.html` in a browser, or serve the folder:

```bash
python3 -m http.server 8000
```

Then open <http://localhost:8000>.

## Deployment

The site is plain static files, so any static host works.

On Vercel, import the repository and keep the defaults: framework preset "Other", no build command, output directory at the repository root.

## Project structure

```
.
├── index.html          # Portuguese page
├── en/index.html       # English page
├── privacidade.html    # privacy policy (pt)
├── en/privacy.html     # privacy policy (en)
├── favicon.svg, favicon-32.png, apple-touch-icon.png
├── fonts/              # Outrise Sans (woff2) and its license
├── media/              # brand film, poster, subtitles and sharing images
├── tools/              # page source and build script
└── README.md
```

## Contributing

- Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/), written in English in the imperative mood, for example `feat: add pricing section` or `fix: correct logo dot colour on hover`.
- Keep `main` deployable. Use short-lived branches and pull requests for anything larger than a typo.

## Status

- Copy is a draft.
- `ola@outrise.technology` forwards to the founder's inbox (Spaceship email forwarding).
- The waitlist form opens a pre-filled email until a Supabase project is connected; `build.py` takes its URL and publishable key.
- Visits are counted with Vercel Web Analytics (cookie-free).
- The figures in the bento tiles ("128" tasks, the agent log) are illustrative and labelled as examples on the page.

## License

Copyright © 2026 Outrise. All rights reserved, except the fonts in `fonts/`, which are licensed under the SIL Open Font License 1.1.
