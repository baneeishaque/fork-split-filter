"""Textual pilot test: the two pane filters are independent."""

from __future__ import annotations

import asyncio
import subprocess
from pathlib import Path

from textual.widgets import ListView

from fork_split_filter.app import ForkSplitFilterApp


def _git(repo: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True)


def _make_repo(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(repo, "init", "-b", "main")
    _git(repo, "config", "user.email", "test@example.com")
    _git(repo, "config", "user.name", "Test User")
    (repo / "staged_file.txt").write_text("s\n")
    (repo / "unstaged_file.txt").write_text("u\n")
    _git(repo, "add", "staged_file.txt")
    return repo


def test_filters_are_independent(tmp_path: Path) -> None:
    repo = _make_repo(tmp_path)

    async def scenario() -> None:
        app = ForkSplitFilterApp(repo)
        async with app.run_test() as pilot:
            await pilot.pause()
            staged_list = app.query_one("#staged-list", ListView)
            unstaged_list = app.query_one("#unstaged-list", ListView)
            assert len(staged_list.children) == 1
            assert len(unstaged_list.children) == 1

            await app.set_filter("staged", "no-match-zzz")
            await pilot.pause()
            assert len(staged_list.children) == 0
            assert len(unstaged_list.children) == 1

            await app.set_filter("staged", "")
            await app.set_filter("unstaged", "no-match-zzz")
            await pilot.pause()
            assert len(staged_list.children) == 1
            assert len(unstaged_list.children) == 0

            await app.set_filter("unstaged", "")
            await pilot.pause()
            assert len(staged_list.children) == 1
            assert len(unstaged_list.children) == 1

    asyncio.run(scenario())


def test_matching_filter_keeps_only_matching_rows(tmp_path: Path) -> None:
    repo = _make_repo(tmp_path)
    (repo / "other_file.txt").write_text("o\n")

    async def scenario() -> None:
        app = ForkSplitFilterApp(repo)
        async with app.run_test() as pilot:
            await pilot.pause()
            unstaged_list = app.query_one("#unstaged-list", ListView)
            assert len(unstaged_list.children) == 2
            await app.set_filter("unstaged", "unstaged_file")
            await pilot.pause()
            assert len(unstaged_list.children) == 1
            await app.set_filter("unstaged", "other_file")
            await pilot.pause()
            assert len(unstaged_list.children) == 1
            await app.set_filter("unstaged", "zzz-no-match")
            await pilot.pause()
            assert len(unstaged_list.children) == 0

    asyncio.run(scenario())
