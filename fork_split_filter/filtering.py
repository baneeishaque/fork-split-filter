"""Case-insensitive substring filtering over status entries."""

from __future__ import annotations

from .git_status import Entry


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
