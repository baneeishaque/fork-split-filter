"""Tests for porcelain=v2 parsing and repository status reading."""

from __future__ import annotations

import subprocess
from pathlib import Path

from fork_split_filter.git_status import parse_status, read_status


def _git(repo: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True)


def make_repo(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(repo, "init", "-b", "main")
    _git(repo, "config", "user.email", "test@example.com")
    _git(repo, "config", "user.name", "Test User")
    return repo


def test_parse_untracked_and_staged() -> None:
    raw = (
        b"? new.txt\0"
        b"1 A. N... 100644 100644 100644 e69de29bb2d1d6434b8b29ae775ad8c2e48c5391"
        b" e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 staged.txt\0"
    )
    snapshot = parse_status(raw)
    assert [e.path for e in snapshot.staged] == ["staged.txt"]
    assert [e.path for e in snapshot.unstaged] == ["new.txt"]
    assert snapshot.unstaged[0].untracked
    assert not snapshot.staged[0].untracked


def test_parse_rename_carries_original_path() -> None:
    raw = (
        b"2 R. N... 100644 100644 100644 e69de29bb2d1d6434b8b29ae775ad8c2e48c5391"
        b" e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 R100 new.txt\0old.txt\0"
    )
    snapshot = parse_status(raw)
    entry = snapshot.staged[0]
    assert entry.path == "new.txt"
    assert entry.orig_path == "old.txt"
    assert entry.display_path == "old.txt -> new.txt"
    assert snapshot.unstaged == []


def test_read_status_classifies_areas(tmp_path: Path) -> None:
    repo = make_repo(tmp_path)
    (repo / "staged.txt").write_text("one\n")
    (repo / "modified.txt").write_text("one\n")
    _git(repo, "add", "staged.txt", "modified.txt")
    _git(repo, "commit", "-m", "init")
    (repo / "modified.txt").write_text("two\n")
    _git(repo, "add", "modified.txt")
    (repo / "untracked.txt").write_text("new\n")
    snapshot = read_status(repo)
    assert [e.path for e in snapshot.staged] == ["modified.txt"]
    assert [e.path for e in snapshot.unstaged] == ["untracked.txt"]


def test_read_status_file_on_both_sides(tmp_path: Path) -> None:
    repo = make_repo(tmp_path)
    (repo / "file.txt").write_text("one\n")
    _git(repo, "add", "file.txt")
    _git(repo, "commit", "-m", "init")
    (repo / "file.txt").write_text("two\n")
    _git(repo, "add", "file.txt")
    (repo / "file.txt").write_text("three\n")
    snapshot = read_status(repo)
    assert [e.path for e in snapshot.staged] == ["file.txt"]
    assert [e.path for e in snapshot.unstaged] == ["file.txt"]


def test_read_status_rename(tmp_path: Path) -> None:
    repo = make_repo(tmp_path)
    (repo / "old.txt").write_text("x\n" * 10)
    _git(repo, "add", "old.txt")
    _git(repo, "commit", "-m", "init")
    _git(repo, "mv", "old.txt", "new.txt")
    snapshot = read_status(repo)
    entry = snapshot.staged[0]
    assert entry.path == "new.txt"
    assert entry.orig_path == "old.txt"


def test_read_status_conflict_appears_in_both(tmp_path: Path) -> None:
    repo = make_repo(tmp_path)
    (repo / "file.txt").write_text("base\n")
    _git(repo, "add", "file.txt")
    _git(repo, "commit", "-m", "base")
    _git(repo, "checkout", "-b", "other")
    (repo / "file.txt").write_text("other\n")
    _git(repo, "commit", "-am", "other")
    _git(repo, "checkout", "main")
    (repo / "file.txt").write_text("main\n")
    _git(repo, "commit", "-am", "main")
    merge = subprocess.run(["git", "-C", str(repo), "merge", "other"], capture_output=True)
    assert merge.returncode != 0
    snapshot = read_status(repo)
    assert [e.path for e in snapshot.staged] == ["file.txt"]
    assert [e.path for e in snapshot.unstaged] == ["file.txt"]
    assert snapshot.staged[0].conflict
    assert snapshot.unstaged[0].conflict
