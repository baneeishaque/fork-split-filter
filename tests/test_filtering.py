"""Tests for the case-insensitive substring filter."""

from __future__ import annotations

from fork_split_filter.filtering import filter_entries
from fork_split_filter.git_status import Entry


def _entry(path: str, orig: str | None = None) -> Entry:
    return Entry(path=path, x="M", y=".", orig_path=orig)


def test_empty_query_returns_all() -> None:
    entries = [_entry("a.py"), _entry("b.py")]
    assert filter_entries(entries, "") == entries
    assert filter_entries(entries, "   ") == entries


def test_case_insensitive_substring() -> None:
    entries = [_entry("src/App.tsx"), _entry("tests/app.test.tsx"), _entry("docs/readme.md")]
    matched = [e.path for e in filter_entries(entries, "APP")]
    assert matched == ["src/App.tsx", "tests/app.test.tsx"]


def test_matches_rename_original_path() -> None:
    entries = [_entry("new_name.py", orig="old_name.py"), _entry("other.py")]
    matched = [e.path for e in filter_entries(entries, "old_name")]
    assert matched == ["new_name.py"]


def test_no_match_returns_empty() -> None:
    entries = [_entry("a.py")]
    assert filter_entries(entries, "zzz") == []
