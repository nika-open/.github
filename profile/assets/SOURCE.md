# Where these images come from

Rendered on 26 November 2026 in the style of [nika.sh](https://nika.sh): its three faces, its
roles in the dark and the light theme, its mark and its blue file. Only rendered pixels are
published here: no face, no site source and no logo file.

| File | Size | What it is |
|---|---|---|
| `hero-{dark,light}.gif`, `hero-{dark,light}.webp` | 1280 × 640, a loop of 12 s | "Say it once. Keep it as a file." beside the story of one file: a request, the file, its inspection, its run and its record |
| `hero-{dark,light}.png` | 2560 × 1280 | the still of that loop, for readers who ask for reduced motion |
| `steps-{dark,light}.gif`, `steps-{dark,light}.webp` | 1280 × 400, a loop of 7.2 s | the four moves and the command of each |
| `steps-{dark,light}.png` | 2560 × 800 | the still of that loop |
| `family-{dark,light}.png` | 2560 × 988 | the repositories, by what each one is for |
| `banner-<repository>-{dark,light}.gif`, `.webp` | 1280 × 400, a loop of 7 s | one per repository, shown at the top of its README: its promise in its own words, beside the first commands that README teaches |
| `banner-<repository>-{dark,light}.png` | 2560 × 800 | the still of that loop |
| `avatar.png` | 1024 × 1024 | the ice mark `#9fd0ff` on the tile ground `#04050d` |

## What the hero shows

Every line in the hero's panel is read from recorded output of `nika 0.125.2` on the example
`social-repurpose.nika` that ships with the engine:

```sh
nika check social-repurpose.nika
nika run social-repurpose.nika --model mock/echo
nika trace verify
```

The run is an offline rehearsal: a mock model echoes the prompt, so no key is used and no model
answers. The picture says so. A count of verbs, providers or tools is never drawn in a picture,
because it changes with the language.

## What a banner shows

A banner shows only what its reader types or writes: commands, a few lines of a file, or the steps
of a contribution. It shows no output, no version and no count, so it does not age with a release.
Its words come from the bold line that opens the repository's README.

## The name

The name is the mark and the word `nika`, as the site's header writes it. The mark keeps its own
tone: ice on a dark ground, ink on a light one.

## Addresses

Pages name a picture by its raw address followed by `?v=` and the first twelve characters of the
file's SHA-256. GitHub caches a picture by its address, so a picture that changes gets a new one.
