# Facebook post

One post for a developer group or your page. Conversational, no jargon walls. The link goes in the
first comment (Facebook also suppresses link posts).

***

**Post text:**

I finally got tired of a papercut I'd had for years: every git client has one search box shared by
the staged and unstaged lists.

You type `src/` to find the file you want to stage. You stage it. You switch to the unstaged list
and the filter is gone — so you type it again. The staged list answers "what am I about to
commit?" and the unstaged list answers "what is still floating around?" Two different questions,
one answer box.

Fork has no plugin API for pane-level UI, so I built the missing piece as a companion app: staged
and unstaged changes side by side, each pane with its own search field, launched from Fork's
repository context menu.

The parts I'm most proud of:

- 383 lines of Python, 12 tests green, MIT-licensed
- Parses `git status --porcelain=v2 -z` — renames, conflicts, and untracked files handled
  explicitly, not scraped from human output
- A pure filter function, so the two panes cannot drift
- Zero modifications to Fork — the integration is a Custom Command and a script

I wrote the whole story — architecture, testing, and the trade-offs I accepted — as an article.
It's a good read if you've ever shipped a developer tool of your own.

Link in the first comment. 👇

**First comment:** `One search box, two panes — full write-up: https://medium.com/@baneeishaque/fork-split-filter-system-design?utm_source=facebook&utm_medium=social&utm_campaign=fork-split-filter-medium`

## Posting notes

- Post in developer groups only where self-promotion is allowed; read the rules first.
- One image: the two-pane app with different filters active (`shot-two-panes.png`).
- Reply to questions with specifics — "how does it parse git status?" is the conversation to lean
  into, not the star count.
