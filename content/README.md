# Content kit

Everything needed to present this project: a standalone Medium deep dive with its own
cross-platform funnel, and a scripted multilingual video pipeline.

## Asset map

| File / directory                              | Platform            | Format                                      | Length           |
| --------------------------------------------- | ------------------- | ------------------------------------------- | ---------------- |
| [`funnel-medium/`](funnel-medium/README.md)   | Medium + social     | Funnel to the Medium deep dive (9 assets)   | ~2,000 words     |
| [`youtube/`](youtube/)                        | YouTube             | Full video pipeline (37 locales)            | ~2.5 minutes     |

The funnel kit is the publishing front door: the [Medium article](funnel-medium/medium-article.md)
carries the full system design, and every social asset drives traffic to it. The
[YouTube pipeline](youtube/README.md) is the same discipline applied again — one source of truth,
deterministic stages, and artifacts you can verify.

## Publishing order

1. **Publish the Medium article first** — every asset links to it, so it must resolve before
   anything else goes out.
2. **Community blog post** the same day (the soft-launch companion; it links to the Medium piece
   as "the full write-up").
3. **LinkedIn post 1** the next morning; post 2 two to three days later.
4. **X thread** the same day as LinkedIn post 1, a few hours later.
5. **Reels + Instagram carousel + Snapchat** midweek, all in one push — the short-form video drives
   the most cold traffic.
6. **Facebook** the day after the short-form push.
7. **WhatsApp developer groups** last and least often — treat it as a favour to communities, not a
   broadcast channel.
8. **YouTube video** whenever the multilingual cut is ready; it is the only asset that shows all
   37 locales in one artifact.

## Conventions

- **Repo URL** used throughout:
  `https://github.com/baneeishaque-ompventure/fork-split-filter`. If the published URL differs,
  find-and-replace before posting.
- **Medium URL placeholder** used throughout:
  `https://medium.com/@baneeishaque/fork-split-filter-system-design`. If the published URL
  differs, find-and-replace it in every file under [`funnel-medium/`](funnel-medium/README.md)
  **before** posting anything.
- **UTM tags**: append
  `?utm_source=<platform>&utm_medium=social&utm_campaign=fork-split-filter-medium` to Medium links.
  The community blog post uses `utm_source=community-blog&utm_medium=referral`.
- **Verified numbers** quoted in the kit (2 panes, 383 lines of application code, 220 lines of
  tests, 12 tests, 12 video scenes, 37 subtitle languages, 20 narration tracks) come from the
  repository itself; re-check against `.venv/bin/pytest -q` and
  `content/youtube/scenes.json` before posting if the project changes.
- **Screenshots** for carousel/short-form assets: Fork's single shared filter box
  (`shot-fork-filter.png`), the two-pane app with different filters active (`shot-two-panes.png`),
  the green pytest run (`shot-tests.png`), and the master MKV track list (`shot-tracks.png`).

## Video pipeline (YouTube)

`youtube/` contains a scripted pipeline rather than a finished upload:

- `translations/<locale>.json` — per-locale slide titles and narrations (37 files; the
  community-reviewable layer).
- `build-scenes.py` — owns scene order, on-screen code, the locale roster, and voices; assembles
  `scenes.json`.
- `scenes.json` — generated single source of truth consumed by the renderer and builder.
- `render-slides.mjs` — renders slide images with headless Chromium (per-script fonts, RTL,
  Nastaliq line boxes).
- `build-video.py` — generates narration with macOS `say`, assembles per-locale videos, muxes the
  master multi-audio MKV (20 audio + 37 subtitle tracks), and exports subtitles.
- `subtitles/` — generated SRT/VTT files for all 37 locales, committed as deliverables.
- `metadata.md` — titles, descriptions, tags, and chapters per locale.

See [`youtube/README.md`](youtube/README.md) for the full pipeline, the locale roster, and the 17
subtitle-only locales.
