# One search box, two panes: the system design behind a small git companion

*Fork has one filter shared by staged and unstaged changes. A 383-line Python TUI gives each pane
its own — and the interesting part is everything around the filter.*

***

Every git client has the same small papercut, and after a while you stop noticing it: there is one
search box for two lists.

You type `src/` to find the file you want to stage. You stage it, switch to the unstaged list, and
the filter is still `src/` — or worse, it is not, and you type it again. The staged list and the
unstaged list answer two different questions ("what am I about to commit?" and "what is still
floating around?"), but the UI makes them share one answer. It is not a bug in any client. It is a
missing feature everyone has learned to live around.

I use [Fork](https://git-fork.com/) on macOS, and it has exactly this papercut. There is no plugin
API for pane-level UI, so waiting for the feature means waiting on a roadmap. Instead I built the
missing piece as a companion: **fork-split-filter**, a small terminal app that shows staged and
unstaged changes side by side, each pane with its **own** search field, launched from Fork's
repository context menu.

**Repository: [github.com/baneeishaque-ompventure/fork-split-filter](https://github.com/baneeishaque-ompventure/fork-split-filter)**

Stack: Python 3.12, [Textual](https://textual.textualize.io/), pytest. The application is 383
lines across four modules; the tests are another 220 lines. It is MIT-licensed, and every claim
below is enforced by the suite.

## One refresh, one pipeline

The most common failure mode in small tools is bidirectional knowledge: the UI knows how to parse
git, the parser knows what the UI wants to render, and every new feature touches both. Bugs live
in the seams.

This project enforces a single direction. Every refresh flows through four stages, and nothing
imports backwards:

```text
git status --porcelain=v2 -z  →  parser  →  filter engine  →  Textual TUI
```

- **`git_status.py`** runs git and owns the format: raw NUL-delimited bytes in, a typed
  `StatusSnapshot` out. It is the only module that knows what porcelain v2 looks like.
- **`filtering.py`** owns one pure function: entries plus a query in, matching entries out. It is
  the only module that knows what "matches" means.
- **`app.py`** owns the terminal: two panes, a refresh loop, keyboard actions. It is the only
  module that knows Textual exists.
- **`__main__.py`** owns the entry point: launch the TUI, or `--dump` the parsed lists for
  scripting.

The payoff is a boring, reviewable change checklist. "Search rename origins too" is a one-function
change in `filtering.py` with a unit test. "Handle unmerged entries" is a one-branch change in
`git_status.py` with an integration test. Neither can leak into the other, because neither knows
the other exists.

## Parse the format, not the text

The naive way to build this tool is to shell out to `git status` and scrape the human output. That
works until a filename contains a space, a quote, or a newline — or until the user's locale
changes the column headers. Human formats are for humans.

`git status --porcelain=v2 -z` is git's machine format, and three properties make it the right
contract:

- **Stable field order.** Every ordinary entry starts with its status characters and ends with the
  path — no prefix text to strip, no column positions to count.
- **Unambiguous semantics.** Renames carry a similarity score and the original path as a separate
  NUL token. Unmerged entries have their own record type. Untracked and ignored files are marked
  explicitly. Nothing has to be inferred.
- **NUL delimiters.** Paths containing spaces, quotes, or newlines cannot break the framing; the
  raw output is split on `\0`, and non-UTF-8 path bytes survive via `surrogateescape`.

Classification is then four lines of policy:

```python
def _classify(entry: Entry, staged: list[Entry], unstaged: list[Entry]) -> None:
    if entry.x != ".":
        staged.append(entry)
    if entry.y != ".":
        unstaged.append(entry)
```

A file edited after being staged has both an `x` and a `y` status — so it appears in **both**
panes. That is not a bug to deduplicate away; it is the truth. The staged pane shows what a commit
would record; the unstaged pane shows what is still changing. An unmerged path appears in both
panes with a `UU` tag for the same reason: it is genuinely both.

## A filter is a pure function

Filtering is deliberately not a UI concern:

```python
def filter_entries(entries: list[Entry], query: str) -> list[Entry]:
    """Return entries whose path (or rename origin) contains `query`, ignoring case."""
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

Entries and a string go in; entries come out. No widget access, no git calls, no state. Three
things fall out of that purity:

1. **The filter is testable without a terminal.** Four of the twelve tests call this function
   directly — empty query, case folding, rename origin, no match.
2. **The two panes cannot drift.** They call the same function with different queries; there is no
   second code path to keep in sync.
3. **Rename origins are searchable.** Typing `old_name` finds a file renamed to `new_name.py`,
   because the filter checks both sides of the rename. This is the kind of detail that makes a
   filter feel trustworthy.

It is a plain substring match, case-insensitive, and that is a decision, not a shortcut. Fuzzy
matching forgives typos but makes results harder to predict; regex is powerful but turns a
five-second interaction into a syntax exercise. In a tool you use mid-commit, predictability wins.

## Refresh without races

The app re-reads git status on three triggers: a 2-second interval, every keystroke in either
filter, and `R` on demand. Those triggers overlap — type fast while the interval fires and you
have two refreshes in flight.

Each refresh does read → filter → `clear()` → `extend()`. Interleave two of those and you can
render duplicated or stale rows. The fix is one lock:

```python
async def refresh_lists(self) -> None:
    """Re-read git status and repopulate both panes from their own filters."""
    async with self._refresh_lock:
        ...
```

Now every refresh is atomic with respect to the UI: one snapshot is read, both panes are
repopulated from that single snapshot, and the previous selection index is restored when it still
exists. Git failures do not kill the app either — a failed `git status` switches the subtitle to
`<repo> - git error` and raises one notification per failure streak, keeping the last good
snapshot until the next success.

This race was found in manual smoke-testing, not by a failing test. It is in this article because
that is what actually happens when a tool grows triggers: the concurrency is real, the window is
small, and the fix is cheap. Write the lock before you see the bug.

## The test suite is the specification

Twelve tests, run with pytest:

- **6 parser and repository tests.** Two feed literal porcelain v2 bytes (untracked + staged,
  rename tokens). Four build real scratch repositories under pytest's `tmp_path` and drive real
  git: area classification, a file on both sides, `git mv`, and a real merge conflict.
- **4 filter tests.** Empty query, case-insensitive substring, rename-origin match, no match.
- **2 Textual pilot tests.** Textual's own `run_test()` pilot drives the real widget tree: the
  panes' filters are independent, and a matching query narrows a list to exactly the matching row.

The integration tests exist because the format's edge cases — rename tokens, unmerged records —
are exactly where a parser written from memory gets it wrong. Feeding real git output through real
git commands is the difference between "the parser handles renames" and "the parser handles the
rename record I remembered."

One test-data lesson is worth repeating. The app fixture originally used `staged_file.txt` and
`unstaged_file.txt`, and a test filtered for `staged_file` — which is a **substring of
`unstaged_file.txt`**. The test failed for the right reason: the filter is a plain substring
match, and the fixture was accidentally self-overlapping. The fix was renaming the fixture, not
weakening the assertion. When a test and a documented product decision disagree, the test is
usually the thing that is wrong.

## The trade-offs, honestly

Every architecture is a set of accepted costs. These are mine:

| Decision                       | You gain                                                                  | You pay                                                     |
| ------------------------------ | ------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Standalone companion app       | Ships today; no vendor roadmap dependency                                 | A terminal window beside Fork, not inside it                |
| Shell out to `git`             | The installed git is the source of truth; porcelain v2 is stable          | One process per refresh; no in-process object database      |
| Snapshot polling (2 s)         | Trivial, safe on huge repositories                                        | Up to 2 s staleness; `R` exists for impatience              |
| Porcelain v2 over v1           | Unambiguous renames, conflicts, untracked; NUL-safe paths                 | Requires git ≥ 2.11 (2016)                                  |
| Plain substring filter         | Predictable; one line of logic; trivial to test                           | No typo tolerance; no regex power users                     |
| Textual (Python)               | Fast to build; testable via pilot; runs anywhere Python runs              | Heavier than a native pane; needs a terminal                |
| Keyboard-first, macOS-leaning  | Stage/unstage without leaving the keyboard                                | `open -R`, `pbcopy`, and VS Code lookups are macOS-flavoured |

None of these are universal answers. They are *recorded* answers — each one lives in
[`docs/trade-offs.md`](https://github.com/baneeishaque-ompventure/fork-split-filter/blob/main/docs/trade-offs.md)
with its alternative, so the next engineer can disagree on purpose instead of by accident.

## Results

- Two panes, two independent filters, launched from Fork's context menu without touching Fork
  itself
- 383 lines of application code; 220 lines of tests; 12 tests green
- Real git semantics: renames with origins, files on both sides, unmerged conflicts, untracked
  files
- Keyboard-first staging: `s` and `u` in the pane you are looking at, plus open, reveal, copy, and
  refresh
- Zero modifications to Fork; the integration is a Custom Command and a shell script

And the meta-proof: the project's video pipeline narrates its walkthrough in 20 languages and
ships subtitles in **37** — including Malayalam, Tamil, Kannada, Bengali, Gujarati, Punjabi, Odia,
Assamese, Urdu, Sindhi, Sanskrit, Nepali, Konkani, Maithili, Bodo, Dogri, Manipuri, Santali, and
Kashmiri. The system the video describes is the system that produced the video.

## Steal this

The repository is public and MIT-licensed, with the architecture guide, per-decision trade-off
notes, and the test suite next to the code:

**Repository: [github.com/baneeishaque-ompventure/fork-split-filter](https://github.com/baneeishaque-ompventure/fork-split-filter)**

If you take one thing from this article, take the pipeline rule: parse the machine format, keep
the filter pure, serialize the refresh — and write the test that fails when someone reverses the
decision. The missing feature is the easy part. The seams are what decide whether it survives its
first real repository.

***

*If this saved you from retyping the same filter twice, star the repository — it is how other
engineers find it.*
