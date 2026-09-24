"""Parse `git status --porcelain=v2 -z` into staged and unstaged entry lists."""

from __future__ import annotations

import subprocess
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Entry:
    """One changed path with its staged (X) and unstaged (Y) status characters."""

    path: str
    x: str
    y: str
    orig_path: str | None = None
    untracked: bool = False
    conflict: bool = False

    @property
    def display_path(self) -> str:
        """`orig -> new` for renames, plain path otherwise."""
        if self.orig_path:
            return f"{self.orig_path} -> {self.path}"
        return self.path


@dataclass
class StatusSnapshot:
    """Changed paths split by staging area."""

    staged: list[Entry] = field(default_factory=list)
    unstaged: list[Entry] = field(default_factory=list)


def _classify(entry: Entry, staged: list[Entry], unstaged: list[Entry]) -> None:
    if entry.x != ".":
        staged.append(entry)
    if entry.y != ".":
        unstaged.append(entry)


def parse_status(raw: bytes) -> StatusSnapshot:
    """Parse raw NUL-separated porcelain=v2 output into a snapshot."""
    tokens = raw.split(b"\0")
    snapshot = StatusSnapshot()
    index = 0
    while index < len(tokens):
        token = tokens[index]
        index += 1
        if not token:
            continue
        kind = token[:1]
        if kind == b"1":
            parts = token.decode("utf-8", "surrogateescape").split(" ", 8)
            if len(parts) < 9:
                continue
            xy, path = parts[1], parts[8]
            _classify(Entry(path=path, x=xy[0], y=xy[1]), snapshot.staged, snapshot.unstaged)
        elif kind == b"2":
            parts = token.decode("utf-8", "surrogateescape").split(" ", 9)
            if len(parts) < 10:
                continue
            xy, path = parts[1], parts[9]
            orig_path = None
            if index < len(tokens):
                orig_path = tokens[index].decode("utf-8", "surrogateescape") or None
                index += 1
            entry = Entry(path=path, x=xy[0], y=xy[1], orig_path=orig_path)
            _classify(entry, snapshot.staged, snapshot.unstaged)
        elif kind == b"u":
            parts = token.decode("utf-8", "surrogateescape").split(" ", 10)
            if len(parts) < 11:
                continue
            xy, path = parts[1], parts[10]
            entry = Entry(path=path, x=xy[0], y=xy[1], conflict=True)
            snapshot.staged.append(entry)
            snapshot.unstaged.append(entry)
        elif kind == b"?":
            path = token[2:].decode("utf-8", "surrogateescape")
            snapshot.unstaged.append(Entry(path=path, x="?", y="?", untracked=True))
        elif kind == b"!":
            continue
    return snapshot


def read_status(repo: Path) -> StatusSnapshot:
    """Run git status in `repo` and return the parsed snapshot."""
    proc = subprocess.run(
        ["git", "-C", str(repo), "status", "--porcelain=v2", "-z", "--untracked-files=all"],
        check=True,
        capture_output=True,
    )
    return parse_status(proc.stdout)


def current_branch(repo: Path) -> str:
    """Short branch name, or a detached-HEAD marker, or `(no branch)`."""
    proc = subprocess.run(
        ["git", "-C", str(repo), "symbolic-ref", "--short", "-q", "HEAD"],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode == 0 and proc.stdout.strip():
        return proc.stdout.strip()
    proc = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "--short", "HEAD"],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode == 0 and proc.stdout.strip():
        return f"detached@{proc.stdout.strip()}"
    return "(no branch)"
