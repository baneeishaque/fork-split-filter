# Architecture

The application is a one-way pipeline. Every refresh moves in the same direction, and nothing
imports backwards:

```text
git status --porcelain=v2 -z --untracked-files=all
        │  subprocess, NUL-delimited bytes
        ▼
git_status.parse_status()   →   StatusSnapshot { staged: [Entry], unstaged: [Entry] }
        ▼
filtering.filter_entries(entries, query)      ← one call per pane, each with its own query
        ▼
app.ForkSplitFilterApp (Textual)              → two panes, live refresh, keyboard actions
```

## Modules

| Module                        | Owns                                                                             |
| ----------------------------- | -------------------------------------------------------------------------------- |
| `fork_split_filter/git_status.py` | Running git, parsing porcelain v2, the `Entry`/`StatusSnapshot` models, branch name |
| `fork_split_filter/filtering.py`  | The pure, case-insensitive substring filter over entries                          |
| `fork_split_filter/app.py`        | The Textual application: two panes, refresh loop, stage/unstage and file actions  |
| `fork_split_filter/__main__.py`   | The CLI: launch the TUI, or `--dump` the parsed lists for scripting               |

## Why porcelain v2, NUL-delimited

`git status --porcelain=v2 -z` is git's machine format, not a human format that happens to be
parseable. Three properties matter here:

- **Stable field order.** Every ordinary entry starts with its status characters, and the path is
  always the last field — no locale-dependent prefix text to strip.
- **Unambiguous semantics.** Renames carry a similarity score and the original path as a separate
  NUL token; unmerged entries have their own record type; untracked and ignored files are marked
  explicitly. The parser never has to guess from column positions.
- **NUL delimiters.** Paths containing spaces, quotes, or newlines cannot break the framing. The
  raw output is split on `\0` and decoded with `surrogateescape`, so even non-UTF-8 path bytes
  survive the round trip.

The parser classifies each record into the two lists that drive the UI:

```python
def _classify(entry: Entry, staged: list[Entry], unstaged: list[Entry]) -> None:
    if entry.x != ".":
        staged.append(entry)
    if entry.y != ".":
        unstaged.append(entry)
```

A path edited after being staged (`x != "."` **and** `y != "."`) intentionally appears in both
panes, and an unmerged path appears in both with a `UU` tag. That is the point of the tool: the
two panes answer two different questions, so a path can legitimately answer both.

## The filter engine is pure

Filtering is deliberately not a UI concern. `filter_entries` takes a list of entries and a query,
and returns the matching entries — nothing else:

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

Two consequences: the filter can be tested without a terminal (four of the twelve tests do exactly
that), and both panes are guaranteed to behave identically because they call the same function
with different queries.

## The refresh loop

The app re-reads git status on a 2-second interval, on every keystroke in either filter, and on
demand via `R`. Those triggers can overlap, so refreshes are serialized with one lock:

```python
async def refresh_lists(self) -> None:
    """Re-read git status and repopulate both panes from their own filters."""
    async with self._refresh_lock:
        ...
```

Without the lock, two overlapping refreshes could interleave `clear()`/`extend()` calls and
render duplicated or stale rows. The lock makes each refresh atomic with respect to the UI: the
snapshot is read once, both panes are repopulated from that single snapshot, and the previous
selection index is restored afterwards when it still exists.

Git failures do not kill the app. A failed `git status` switches the subtitle to
`<repo> - git error` and raises one notification per failure streak — the panes keep the last
good snapshot until the next successful refresh.

## Actions

| Action              | Implementation                                              |
| ------------------- | ----------------------------------------------------------- |
| Stage selected      | `git add -- <path>` from the Unstaged pane                  |
| Unstage selected    | `git restore --staged -- <path>`, falling back to `git reset -q -- <path>` |
| Open in editor      | `code-insiders -g` or `code -g`, whichever exists on PATH    |
| Reveal in Finder    | `open -R`                                                    |
| Copy absolute path  | `pbcopy`                                                     |
| Refresh / quit      | `R` / `q`                                                    |

Stage and unstage are pane-aware: pressing `s` while the Staged pane is focused warns instead of
silently doing nothing, because "stage what is already staged" is almost always a mis-press.

## Launching from Fork

Fork has no plugin API for pane-level UI, but it does support Custom Commands. The repository
ships `SplitSearch.command` (a macOS double-clickable wrapper) and `run.sh`; the Fork custom
command runs the wrapper with the selected repository, and the app opens in a terminal window
beside Fork with the repository path already bound. See the [`README.md`](../README.md) for the
install steps.
