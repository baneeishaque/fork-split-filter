# Testing

Twelve tests, run with pytest:

```sh
.venv/bin/pytest -q
```

`pyproject.toml` sets `pythonpath = ["."]` and `testpaths = ["tests"]`, so the suite runs from a
clean checkout with only `textual` and `pytest` installed.

## What the suite covers

| File                     | Tests | Boundary it pins                                                                 |
| ------------------------ | ----- | -------------------------------------------------------------------------------- |
| `tests/test_git_status.py` | 6   | Parsing and classification against raw bytes **and** real repositories            |
| `tests/test_filtering.py`  | 4   | The pure filter: empty query, case folding, rename origin, no-match               |
| `tests/test_app.py`        | 2   | The Textual app: the two pane filters are actually independent                    |

### Parser and repository integration (6)

- `test_parse_untracked_and_staged` — raw NUL-delimited bytes: an untracked record lands in
  unstaged with `untracked=True`; an ordinary record with `x="A"`, `y="."` lands in staged.
- `test_parse_rename_carries_original_path` — a `2` record plus its separate origin token produce
  `display_path == "old.txt -> new.txt"`.
- `test_read_status_classifies_areas` — a real repository: staged modification in staged, untracked
  file in unstaged.
- `test_read_status_file_on_both_sides` — stage a change, then edit the file again: it appears in
  both panes, which is correct, not a bug.
- `test_read_status_rename` — a real `git mv` produces the origin path.
- `test_read_status_conflict_appears_in_both` — a real merge conflict appears in both panes with
  `conflict=True`.

Five of these six build a scratch repository under pytest's `tmp_path` and drive real git
commands; only the two parser tests feed hand-written bytes, and those bytes are literal porcelain
v2 output. The integration tests exist because the format's edge cases (rename tokens, unmerged
records) are exactly where a parser written from memory gets it wrong.

### Filter engine (4)

- Empty or whitespace-only query returns every entry.
- `"APP"` matches both `src/App.tsx` and `tests/app.test.tsx` — case-insensitive substring.
- A query matching only the rename origin still selects the entry.
- A non-matching query returns an empty list.

### Textual app (2)

Both use Textual's own pilot (`app.run_test()`), so they assert on the rendered widget tree — the
number of children in each `ListView` — not on internal state:

- `test_filters_are_independent` — filtering the staged pane to no-match empties only the staged
  list; the unstaged list is untouched, and vice versa. This is the regression test for the whole
  premise of the tool.
- `test_matching_filter_keeps_only_matching_rows` — a matching query narrows the list to the
  matching row and a non-matching query empties it.

## A test-data lesson worth keeping

The first version of the app fixture used `staged_file.txt` and `unstaged_file.txt` and filtered
with `"staged_file"` — which is a **substring of `"unstaged_file.txt"`**. The test failed for the
right reason: the filter is a plain substring match, and the fixture was accidentally
self-overlapping. The fix was renaming the fixture paths, not weakening the assertion. Substring
semantics are a documented product decision (see [`trade-offs.md`](trade-offs.md)); tests should
respect the decision, not route around it.

## What is not covered

- The `say`-based video pipeline is validated by its own `--check` mode, not by pytest.
- Mouse interaction, terminal resizing, and color themes are Textual's tested surface, not ours.
- Stage/unstage actions are exercised manually; the pilot tests cover the list behavior, not the
  git mutation path.
