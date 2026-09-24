# LinkedIn posts

Two posts, 2–3 days apart, both funnelling to the Medium article. Plain text with the link in the
first comment — LinkedIn rewards text posts over link posts.

## Post 1 — the hook (day 1)

> Every git client has one search box for two lists, and I finally got tired of it.
>
> You type `src/` to find the file you want to stage. You stage it. You switch to the unstaged
> list and the filter is gone, so you type it again.
>
> The staged list answers "what am I about to commit?" The unstaged list answers "what is still
> floating around?" Two different questions — one answer box.
>
> Fork has no plugin API for pane-level UI, so I built the missing piece as a companion: a small
> terminal app, launched from Fork's context menu, with one independent search field per pane.
>
> • 383 lines of Python, 4 modules, 12 tests green
> • Parses `git status --porcelain=v2 -z`, not scraped human output — renames, conflicts, untracked files all explicit
> • A pure filter function, so the two panes cannot drift
> • Zero modifications to Fork
>
> The full system design — including the refresh race I found in smoke testing and the trade-offs
> I accepted — is in the article below.
>
> If you have ever retyped the same filter twice in one commit, this one is for you.
>
> #Git #DeveloperTools #Python #SoftwareEngineering #OpenSource

**First comment:** `One search box, two panes — full write-up: https://medium.com/@baneeishaque/fork-split-filter-system-design?utm_source=linkedin&utm_medium=social&utm_campaign=fork-split-filter-medium`

## Post 2 — the engineering story (day 3–4)

> The most useful bug I fixed this month was a race I never saw in a test.
>
> The tool re-reads `git status` on a 2-second interval, on every keystroke, and on demand. Those
> triggers overlap. Each refresh does read → filter → clear → repopulate — and two interleaved
> refreshes can render duplicated or stale rows.
>
> The fix was one `asyncio.Lock` around the whole refresh, so a single snapshot feeds both panes
> and the previous selection survives. The race window was tiny. The fix was cheap. Write the lock
> before you see the bug.
>
> Two more decisions that paid off:
>
> 1. Parse `git status --porcelain=v2 -z`, not human output. Stable fields, explicit rename and
>    conflict records, NUL delimiters — a filename with a space or a newline cannot break the
>    framing.
>
> 2. Keep the filter pure: entries + query in, entries out. Four of twelve tests call it directly,
>    and the two panes call the same function, so they cannot drift.
>
> The article breaks down the full architecture, the porcelain v2 edge cases, and the trade-offs I
> documented instead of hiding.
>
> #SoftwareEngineering #Git #Testing #Python #DeveloperTools

**First comment:** `Architecture + trade-offs: https://medium.com/@baneeishaque/fork-split-filter-system-design?utm_source=linkedin&utm_medium=social&utm_campaign=fork-split-filter-medium`

## Posting notes

- Post 1 between 08:00–10:00 on a Tuesday–Thursday; Post 2 the same slot 2–3 days later.
- Attach one image per post: Post 1 → the two-pane app with different filters active
  (`shot-two-panes.png`); Post 2 → the green pytest run (`shot-tests.png`) or a code shot of
  `refresh_lists`.
- Do not edit a post in the first hour; edits suppress reach.
- Reply to every comment in the first two hours — that is where the distribution comes from.
