"""CLI entry point: launch the TUI, or `--dump` the parsed lists."""

from __future__ import annotations

import argparse
from pathlib import Path

from .git_status import current_branch, read_status


def _dump(repo: Path) -> int:
    snapshot = read_status(repo)
    print(f"repo: {repo}")
    print(f"branch: {current_branch(repo)}")
    print("staged:")
    for entry in snapshot.staged:
        print(f"  {entry.display_path}")
    print("unstaged:")
    for entry in snapshot.unstaged:
        print(f"  {entry.display_path}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="fork_split_filter",
        description="Independent staged/unstaged search for git repositories.",
    )
    parser.add_argument("repo", nargs="?", default=".", help="Git repository path (default: current directory)")
    parser.add_argument("--dump", action="store_true", help="Print parsed staged/unstaged lists and exit")
    args = parser.parse_args(argv)
    repo = Path(args.repo).expanduser().resolve()
    if args.dump:
        return _dump(repo)
    from .app import ForkSplitFilterApp

    ForkSplitFilterApp(repo).run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
