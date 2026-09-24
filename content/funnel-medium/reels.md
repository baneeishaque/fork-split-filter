# Reels / Shorts / TikTok — three scripts

Three short-form scripts, 30–45 seconds each, all pointing at the Medium article (link in bio; on
Shorts, put the article link in the description).

## Reel 1 — "The filter your git client forgot" (35 s)

| Time      | Visual                                                            | VO / caption                                                                  |
| --------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| 0:00–0:04 | One filter box in a git client; staged/unstaged panes switching    | "Every git client has one search box for two lists."                          |
| 0:04–0:10 | Typing `src/`, staging a file, switching panes, retyping          | "You filter, stage, switch panes — and type the same thing again."            |
| 0:10–0:17 | Split screen: the two panes with different queries active          | "So I built a companion app: staged and unstaged side by side, each with its own filter." |
| 0:17–0:25 | Zoom on the Fork context menu → app opens in a terminal            | "It launches from Fork's context menu. No plugin API, no modifications."      |
| 0:25–0:32 | Pytest output: 12 passed                                           | "Twelve tests, real repositories, 383 lines of Python."                       |
| 0:32–0:35 | End card: "Full write-up — link in bio"                            | —                                                                             |

## Reel 2 — "Parse the machine format" (40 s)

| Time      | Visual                                                            | VO / caption                                                                 |
| --------- | ----------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| 0:00–0:05 | Scraping `git status` human output; a filename with a space breaks it | "The naive version scrapes human output. A filename with a space breaks it." |
| 0:05–0:12 | Zoom: `git status --porcelain=v2 -z`                              | "Git has a machine format. Stable fields, explicit records, NUL delimiters."  |
| 0:12–0:20 | Code: rename record + origin token; conflict record; `?` untracked | "Renames carry their origin path. Conflicts and untracked files have their own records." |
| 0:20–0:30 | Code: `if entry.x != ".": staged.append(entry)`                    | "A file edited after staging appears in both panes — because it really is both." |
| 0:30–0:37 | Code: `filter_entries` — pure function                             | "The filter is pure: entries plus a query in, entries out. The panes can't drift." |
| 0:37–0:40 | End card: "Full write-up — link in bio"                            | —                                                                            |

## Reel 3 — "The video that describes itself" (45 s)

| Time      | Visual                                                            | VO / caption                                                                 |
| --------- | ----------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| 0:00–0:06 | Master MKV track list scrolling: 20 audio + 37 subtitle tracks     | "This project's video narrates itself in 20 languages."                       |
| 0:06–0:14 | Subtitle files grid: ml, ta, kn, bn, gu, pa, ur, sd, sa…          | "…and ships subtitles in 37 — including Malayalam, Tamil, Kannada, Bengali, Urdu, Sindhi, and Sanskrit." |
| 0:14–0:22 | `scenes.json` on one side, generated `script.md` on the other      | "One source of truth. Every locale's script generated from the same file."    |
| 0:22–0:32 | Screen recording: the two panes filtering independently            | "The app itself gives each git pane its own filter — with 12 tests."          |
| 0:32–0:40 | Repo page + docs folder                                            | "Architecture, trade-offs, and the test suite — all public, MIT."             |
| 0:40–0:45 | End card: "Full write-up — link in bio"                            | —                                                                             |

## Production notes

- 9:16 vertical; burn captions; assume muted autoplay.
- Code shots: dark terminal background, monospace, one highlighted line at a time, 2–3 seconds per
  shot maximum.
- Reuse the same footage library across all three reels (screen recordings of the two panes,
  terminal output, track lists) — only the script changes.
- Publish Reel 1 first; if it performs, follow with 2 and 3 in the same week.
