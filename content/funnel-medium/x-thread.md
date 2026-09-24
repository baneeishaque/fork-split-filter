# X / Twitter thread

10 posts. Post 1 is the hook; the link lands in the final post (keep it out of the opener so the
algorithm does not down-rank the thread). Keep every post under 280 characters.

***

**1/10**
Every git client has one search box for two lists.

You filter staged. You switch to unstaged. The filter is gone. You type it again.

Fork has no plugin API, so I built the missing piece: one filter per pane. 🧵

**2/10**
It is called fork-split-filter.

A small terminal app launched from Fork's context menu: both panes side by side, each with its own search field.

383 lines of Python. 12 tests green. MIT.

**3/10**
The architecture rule: one-way knowledge flow.

`git status --porcelain=v2 -z → parser → filter engine → Textual TUI`

Nothing imports backwards. The parser owns the format, the filter owns "matches", the app owns the terminal.

**4/10**
Parse the machine format, not the text.

`--porcelain=v2 -z` gives stable fields and explicit rename/conflict records.

NUL delimiters mean no filename can break the framing — not spaces, not quotes.

**5/10**
Classification is four lines:

```python
if entry.x != ".": staged.append(entry)
if entry.y != ".": unstaged.append(entry)
```

A file edited after staging has both — so it appears in both panes. That's the truth, not a bug.

**6/10**
A filter should be a pure function.

entries + query in, entries out. No widget access, no git calls.

Four of the twelve tests call it directly. The panes cannot drift: same function, different queries.

**7/10**
The race I found in smoke testing:

Refreshes fire on a 2s interval, on every keystroke, and on demand. Interleave two and you can render stale rows.

Fix: one `asyncio.Lock` around the whole refresh. Write the lock before you see the bug.

**8/10**
The test-data lesson:

A fixture had `staged_file.txt` and `unstaged_file.txt`. The test filtered for `staged_file` — a substring of `unstaged_file.txt`.

It failed for the right reason. Fix the fixture, not the assertion.

**9/10**
The meta-proof:

The project's video pipeline narrates its own walkthrough in 20 languages.

Subtitles ship in 37 — Malayalam, Tamil, Kannada, Bengali, Gujarati, Urdu, Sindhi, Sanskrit, and more.

The system describes itself.

**10/10**
Full write-up — system design, porcelain v2 edge cases, testing strategy, and the trade-offs I accepted:

<https://medium.com/@baneeishaque/fork-split-filter-system-design?utm_source=x&utm_medium=social&utm_campaign=fork-split-filter-medium>

Code + docs (MIT):
github.com/baneeishaque-ompventure/fork-split-filter

If it saves you a retyped filter, a repost helps. 🙏

***

## Posting notes

- Post the thread 2–3 hours after the LinkedIn post goes live; do not run them simultaneously.
- Attach the two-pane screenshot to post 1 and the pytest output to post 7.
- Quote-post your own post 1 the next morning with the article link for a second wave.
