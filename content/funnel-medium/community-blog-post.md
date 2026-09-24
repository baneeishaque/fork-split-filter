# Community blog post

Companion post for community platforms (dev.to, Hashnode, a company blog, or a community
newsletter). Warmer and shorter than the Medium deep dive; it tells the story and hands the reader
off to the article.

***

## I built the git filter Fork forgot: one search box per pane

Every git client has one search box for two lists, and I finally got tired of it.

The papercut: you type `src/` to find the file you want to stage. You stage it. You switch to the
unstaged list and the filter is either gone or wrong, so you type it again. The staged list
answers "what am I about to commit?" and the unstaged list answers "what is still floating
around?" — two different questions sharing one answer box. It is not a bug in Fork, or in any
other client. It is a missing feature everyone has learned to live around.

I use [Fork](https://git-fork.com/) on macOS and it has exactly this papercut. Fork has no plugin
API for pane-level UI, so I built the missing piece as a companion instead: a small terminal app
that shows staged and unstaged changes side by side, **each pane with its own search field**,
launched straight from Fork's repository context menu.

It is called **fork-split-filter**, it is 383 lines of Python across four modules, it is
MIT-licensed, and it has 12 tests. Here is what building it taught me.

### 1. Parse the machine format, not the text

The naive version shells out to `git status` and scrapes the human output. That works until a
filename contains a space, a quote, or a newline — or until a locale changes the column headers.
Human formats are for humans.

`git status --porcelain=v2 -z` is git's machine format: stable field order, explicit records for
renames (with the original path as a separate token), conflicts, and untracked files, and NUL
delimiters so no path can break the framing. The parser splits on `\0` and decodes with
`surrogateescape`, so even non-UTF-8 path bytes survive. The classification policy is four lines:

```python
def _classify(entry: Entry, staged: list[Entry], unstaged: list[Entry]) -> None:
    if entry.x != ".":
        staged.append(entry)
    if entry.y != ".":
        unstaged.append(entry)
```

A file edited after staging has both an `x` and a `y` status, so it appears in **both** panes.
That is not a bug to deduplicate away — it is the truth. The staged pane shows what a commit
would record; the unstaged pane shows what is still changing.

### 2. A filter should be a pure function

Filtering is deliberately not a UI concern. Entries and a string go in; entries come out:

```python
def filter_entries(entries: list[Entry], query: str) -> list[Entry]:
    needle = query.strip().lower()
    if not needle:
        return list(entries)
    return [
        entry
        for entry in entries
        if needle in entry.path.lower()
        or (entry.orig_path is not None and needle in entry.orig_path.lower())
    ]
```

No widget access, no git calls, no state. Four of the twelve tests call this function directly,
the two panes cannot drift because they call the same function with different queries, and typing
`old_name` finds a file renamed to `new_name.py` because the filter checks both sides of the
rename.

It is a plain substring match, case-insensitive — a decision, not a shortcut. Fuzzy matching
forgives typos but makes results harder to predict; regex is powerful but turns a five-second
interaction into a syntax exercise. In a tool you use mid-commit, predictability wins.

### 3. Refresh triggers overlap; serialize them

The app re-reads git status on a 2-second interval, on every keystroke in either filter, and on
demand. Those triggers overlap — type fast while the interval fires and two refreshes are in
flight. Each refresh does read → filter → `clear()` → `extend()`; interleave two and you can
render duplicated or stale rows.

The fix is one `asyncio.Lock` around the whole refresh. Now one snapshot is read, both panes are
repopulated from it, and the previous selection is restored. I found this in manual smoke-testing,
not from a failing test — which is exactly why it is in this post. Write the lock before you see
the bug.

### 4. When a test and a decision disagree, the test is usually wrong

The app fixture originally used `staged_file.txt` and `unstaged_file.txt`, and a test filtered for
`staged_file` — which is a **substring of `unstaged_file.txt`**. The test failed for the right
reason: the filter is a plain substring match and the fixture was accidentally self-overlapping.
The fix was renaming the fixture, not weakening the assertion.

### The trade-offs nobody puts in the README

Every architecture is a set of costs you accept. The project documents its own:

| Decision                 | You gain                                                      | You pay                                        |
| ------------------------ | ------------------------------------------------------------- | ---------------------------------------------- |
| Standalone companion app | Ships today; no vendor roadmap dependency                     | A terminal window beside Fork, not inside it   |
| Shell out to `git`       | The installed git is the source of truth                      | One process per refresh                        |
| Snapshot polling (2 s)   | Trivial, safe on huge repositories                            | Up to 2 s staleness                            |
| Plain substring filter   | Predictable; one line of logic                                | No typo tolerance                              |
| Textual (Python)         | Testable via pilot; runs anywhere Python runs                 | Heavier than a native pane                     |

### The meta-proof

The best part of this project is that it describes itself the same way twice. The repository
includes a scripted video pipeline that narrates the walkthrough in 20 languages and ships
subtitles in 37 — including Malayalam, Tamil, Kannada, Bengali, Gujarati, Punjabi, Odia, Assamese,
Urdu, Sindhi, Sanskrit, Nepali, Konkani, Maithili, Bodo, Dogri, Manipuri, Santali, and Kashmiri.
One source of truth, deterministic stages, artifacts you can verify. The app filters two panes;
the video about the app renders itself in thirty-seven locales.

### What to do with this

The full write-up — system design, the exact architecture, the testing strategy, and every
trade-off — is on Medium:

> [One search box, two panes: the system design behind a small git companion](https://medium.com/@baneeishaque/fork-split-filter-system-design?utm_source=community-blog&utm_medium=referral)

And the code is here, with the reasoning written next to it:

**Repository: [github.com/baneeishaque-ompventure/fork-split-filter](https://github.com/baneeishaque-ompventure/fork-split-filter)**

If you only take one thing: parse the machine format, keep the filter pure, serialize the refresh
— and write the test that fails when someone reverses the decision. The missing feature is the
easy part. The seams are what decide whether it survives its first real repository.
