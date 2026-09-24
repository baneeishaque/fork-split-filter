# WhatsApp — developer groups

Messages for git / Fork / developer-tooling community groups. Share **once per group**, ideally
after asking an admin. The goal is a useful artifact, not a broadcast; the etiquette notes below
are part of the deliverable.

## Short version (default)

> Hi all 👋 I wrote up how I built the git filter Fork doesn't have: staged and unstaged side by
> side, each pane with its own search field, launched from Fork's context menu.
>
> The interesting parts aren't the UI: parsing `git status --porcelain=v2 -z` instead of human
> output, a pure filter function, and the refresh race I found in smoke testing (12 tests green,
> 383 lines of Python).
>
> Full article: <https://medium.com/@baneeishaque/fork-split-filter-system-design?utm_source=whatsapp&utm_medium=social&utm_campaign=fork-split-filter-medium>
>
> Code is MIT on GitHub if you want to steal the architecture. Happy to answer questions here.

## Longer version (groups that welcome detail)

> Sharing something I wish I'd found two years ago.
>
> Every git client has one search box shared by the staged and unstaged lists — so you filter,
> stage, switch panes, and retype. I built a small companion app that gives each pane its own
> filter, launched from Fork's repository context menu (no plugin API needed).
>
> The interesting part isn't the UI:
>
> • one-way architecture: `porcelain=v2 -z → parser → filter engine → TUI`, nothing imports backwards
> • machine format, not scraped text: explicit rename/conflict/untracked records, NUL-delimited paths
> • a pure filter function — entries + query in, entries out — so the two panes cannot drift
> • refreshes serialized with an `asyncio.Lock`, because the interval, keystrokes, and manual refresh overlap
> • 12 tests: literal porcelain bytes, real scratch repos, and Textual pilot tests
>
> I wrote the full system design, including the trade-offs I accepted, here:
> <https://medium.com/@baneeishaque/fork-split-filter-system-design?utm_source=whatsapp&utm_medium=social&utm_campaign=fork-split-filter-medium>
>
> Repo (MIT): github.com/baneeishaque-ompventure/fork-split-filter

## Etiquette

- Ask an admin before posting in moderated groups; "sharing a write-up I made" gets a warmer
  reception than a silent drop.
- Share once per group. Do not repost in the same group when engagement is low; the article is
  evergreen.
- Answer questions in the group instead of DMing links.
- If the group has a "share your projects" day or thread, use it — and drop the longer version
  there.
