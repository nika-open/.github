# Where these images come from

Rendered on 20 November 2026 by [`build.py`](build.py) from the nika.sh brand kit.

| File | Size | Made with |
|---|---|---|
| `banner-dark.png` | 2400 × 840 | headless Chrome, from an SVG composition with the site's Martian Grotesk and Martian Mono (woff2, embedded) |
| `banner-light.png` | 2400 × 840 | the same composition with the light roles |
| `avatar.png` | 1024 × 1024 | `rsvg-convert`: the ice mark `#9fd0ff` on the tile ground `#04050d` |

Sources, quoted rather than redrawn:

- the mark: the path of `public/brand/nika-mark-dark.svg`;
- the lockup: the geometry of `public/brand/nika-logo-dark.svg` (Martian Mono 700 wordmark and its
  `#ff7a3c` dot);
- dark colors: `src/ui/roles.css`; light colors: `src/home/styles/01-foundations.css`;
- words: the nika.sh homepage hero ("Say it once. Keep it as a file.") and its description
  (checked before it runs, run with the model you choose, proven afterwards).

To rebuild, place the two woff2 files from nika.sh `src/ui/fonts/` and the mark SVG beside the
script as it expects (`src/fonts/`, `src/nika-mark-dark.svg`), then run
`python3 -I build.py <that folder>`.
