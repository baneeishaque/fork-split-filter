# Trade-offs

Every architecture is a set of accepted costs. This file records the decisions behind
`fork-split-filter`, what each one buys, and what it costs — so the next engineer can disagree on
purpose instead of by accident.

| Decision                        | You gain                                                                 | You pay                                                             |
| ------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| Standalone companion app        | Ships today, no dependency on a vendor's roadmap                          | Lives in a terminal beside Fork, not inside it                      |
| Shell out to `git`              | The installed git is the source of truth; porcelain v2 is a stable contract | One process per refresh; no in-process object database              |
| Snapshot polling (2 s)          | Trivial, safe on huge repositories                                        | Up to 2 s staleness; `R` exists for impatience                      |
| Porcelain v2 over v1            | Unambiguous renames, conflicts, untracked; NUL-safe paths                 | Requires git ≥ 2.11 (2016)                                          |
| Plain substring filter          | Predictable; one line of logic; trivial to test                           | No typo tolerance; no regex power users                             |
| Textual (Python)                | Fast to build; testable via pilot; runs anywhere Python runs              | Heavier than a native pane; needs a terminal emulator               |
| Keyboard-first, macOS-leaning   | Stage/unstage without leaving the keyboard                                | `open -R`, `pbcopy`, and VS Code lookups are macOS-flavoured        |
| Unmerged entries in both panes  | Conflicts are visible wherever you look                                   | Deliberate double-listing that looks like a bug until you read this |

## Standalone app instead of a Fork plugin

Fork does not expose a plugin API for pane-level UI, so there is no supported way to put a second
filter box inside its changes view. The alternative — wait for a vendor feature or patch a
closed-source binary — was rejected: the companion app ships today and keeps working across Fork
updates. The cost is honest: it is a second window, not an integrated pane. If Fork ever ships
independent pane filters, this tool becomes a two-minute install of the real thing.

## Shelling out to git instead of libgit2

`git status --porcelain=v2` is a documented, stable, machine-readable contract, and the git
binary is already installed on every machine that has Fork. A binding (pygit2/libgit2) would keep
everything in-process and remove the subprocess per refresh, but it re-implements repository
discovery, config resolution, and index semantics — and drifts from the git version the user
actually runs. For a tool whose whole job is to report what git thinks, asking git is the feature,
not the shortcut.

## Snapshot polling instead of a filesystem watcher

A file watcher would refresh the instant something changes, but it would need recursive watches
over the whole working tree (`.git` included) and a debounce policy for build output. The polling
loop re-reads status every two seconds and on every keystroke; on repositories large enough for
that to matter, `git status` itself is the bottleneck and a watcher would not fix it. The escape
hatch is `R`.

## Substring filter instead of fuzzy or regex

The filter answers one question: "which paths contain this text?" It is case-insensitive and it
also searches rename origins, so `old_name` finds a rename to `new_name.py`. Fuzzy matching would
be friendlier to typos and regex would be more powerful, but both make the two panes harder to
reason about when they show different results. Predictability wins in a tool you use while
composing a commit.

## Textual instead of curses or a web UI

Textual gives a real widget tree, a test pilot, and modern terminal rendering (mouse, colors,
async) without hand-rolling curses. A web UI would be prettier but would add a server, a browser
tab, and a build step to a tool that should be one keystroke from Fork. The cost is a Python
runtime and a dependency on Textual's release cadence — acceptable for a developer-local tool.

## macOS-leaning actions

`open -R`, `pbcopy`, and the `code-insiders`/`code` lookups target the author's daily environment.
The core (parsing, filtering, stage/unstage) is portable, and the platform-specific actions
degrade to a notification when the tool is missing. Porting them is a per-platform branch, not a
redesign — recorded here so a Linux or Windows contributor knows the seam is intentional.
