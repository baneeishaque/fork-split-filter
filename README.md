# fork-split-filter

Companion TUI for the [Fork](https://git-fork.com/) git client on macOS: staged and unstaged changes side by
side, each pane with its **own search field** (Fork itself only offers a single shared filter).

## Usage

```sh
/Users/dk/lab-data/fork-split-filter/run.sh [/path/to/repo]
```

In Fork: repository context menu -> **Split Search (Staged/Unstaged)** (installed as a Fork Custom Command).

## Keys

| Key | Action |
| :--- | :--- |
| `tab` / `shift+tab` | move focus (filter fields and lists) |
| `up` / `down` | move selection in the focused list |
| `s` | stage selected file (Unstaged pane) |
| `u` | unstage selected file (Staged pane) |
| `o` | open in VS Code |
| `r` | reveal in Finder |
| `c` | copy absolute path |
| `R` | refresh now |
| `q` | quit |

## Development

```sh
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python textual pytest
.venv/bin/pytest -q
.venv/bin/python -m fork_split_filter --dump /path/to/repo
```
