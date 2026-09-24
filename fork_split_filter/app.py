"""Textual TUI: two panes, each with its own search field."""

from __future__ import annotations

import asyncio
import shutil
import subprocess
from pathlib import Path

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.widgets import Footer, Header, Input, Label, ListItem, ListView

from .filtering import filter_entries
from .git_status import Entry, current_branch, read_status


class FileItem(ListItem):
    """A selectable changed-file row carrying its Entry."""

    def __init__(self, entry: Entry, tag: str) -> None:
        super().__init__(Label(f"[{tag}] {entry.display_path}"))
        self.entry = entry


class ForkSplitFilterApp(App[None]):
    """Staged/unstaged lists with independent filters, bound to one repo."""

    CSS = """
    #panes { height: 1fr; }
    .pane { width: 1fr; border: round $primary; }
    .pane-title { padding: 0 1; background: $panel; text-style: bold; }
    .filter { margin: 0 1; }
    ListView { height: 1fr; }
    """

    BINDINGS = [
        Binding("s", "stage", "Stage"),
        Binding("u", "unstage", "Unstage"),
        Binding("o", "open_in_editor", "Open"),
        Binding("r", "reveal", "Reveal"),
        Binding("c", "copy_path", "Copy path"),
        Binding("R", "refresh", "Refresh"),
        Binding("q", "quit", "Quit"),
    ]

    def __init__(self, repo: Path) -> None:
        super().__init__()
        self.repo = repo
        self._error_shown = False
        self._refresh_lock = asyncio.Lock()

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Horizontal(id="panes"):
            with Vertical(classes="pane"):
                yield Label("Staged", id="staged-title", classes="pane-title")
                yield Input(placeholder="Filter staged...", id="staged-filter", classes="filter")
                yield ListView(id="staged-list")
            with Vertical(classes="pane"):
                yield Label("Unstaged", id="unstaged-title", classes="pane-title")
                yield Input(placeholder="Filter unstaged...", id="unstaged-filter", classes="filter")
                yield ListView(id="unstaged-list")
        yield Footer()

    async def on_mount(self) -> None:
        self.title = "Fork Split Filter"
        self.sub_title = str(self.repo)
        await self.refresh_lists()
        self.set_interval(2.0, self.refresh_lists)

    async def on_input_changed(self, event: Input.Changed) -> None:
        await self.refresh_lists()

    async def set_filter(self, pane: str, text: str) -> None:
        """Set one pane's filter programmatically (used by tests)."""
        self.query_one(f"#{pane}-filter", Input).value = text
        await self.refresh_lists()

    async def refresh_lists(self) -> None:
        """Re-read git status and repopulate both panes from their own filters."""
        async with self._refresh_lock:
            try:
                snapshot = read_status(self.repo)
                branch = current_branch(self.repo)
            except (subprocess.CalledProcessError, FileNotFoundError) as exc:
                self.sub_title = f"{self.repo} - git error"
                if not self._error_shown:
                    self.notify(f"git status failed: {exc}", severity="error")
                    self._error_shown = True
                return
            self._error_shown = False
            self.sub_title = f"{self.repo}  ({branch})"
            staged_query = self.query_one("#staged-filter", Input).value
            unstaged_query = self.query_one("#unstaged-filter", Input).value
            await self._populate("staged", snapshot.staged, staged_query)
            await self._populate("unstaged", snapshot.unstaged, unstaged_query)

    async def _populate(self, pane: str, entries: list[Entry], query: str) -> None:
        list_view = self.query_one(f"#{pane}-list", ListView)
        title = self.query_one(f"#{pane}-title", Label)
        previous = list_view.index
        visible = filter_entries(entries, query)
        total = len(entries)
        shown = len(visible)
        label = pane.capitalize()
        title.update(f"{label} ({shown}/{total})" if shown != total else f"{label} ({total})")
        await list_view.clear()
        items: list[ListItem] = []
        for entry in visible:
            if entry.conflict:
                tag = "UU"
            elif pane == "unstaged" and entry.untracked:
                tag = "??"
            else:
                tag = entry.x if pane == "staged" else entry.y
            items.append(FileItem(entry, tag))
        await list_view.extend(items)
        if previous is not None and previous < len(list_view.children):
            list_view.index = previous

    def _active_list(self) -> ListView | None:
        focused = self.focused
        if isinstance(focused, ListView):
            return focused
        if isinstance(focused, Input) and focused.id and focused.id.endswith("-filter"):
            pane = focused.id.removesuffix("-filter")
            return self.query_one(f"#{pane}-list", ListView)
        return None

    def _selected_item(self) -> tuple[ListView, FileItem] | None:
        list_view = self._active_list()
        if list_view is None:
            return None
        child = list_view.highlighted_child
        if not isinstance(child, FileItem):
            return None
        return list_view, child

    def _selected_path(self) -> Path | None:
        selected = self._selected_item()
        if selected is None:
            return None
        return self.repo / selected[1].entry.path

    async def action_stage(self) -> None:
        await self._mutate_selected("stage")

    async def action_unstage(self) -> None:
        await self._mutate_selected("unstage")

    async def _mutate_selected(self, mode: str) -> None:
        selected = self._selected_item()
        if selected is None:
            self.notify("No file selected", severity="warning")
            return
        list_view, item = selected
        pane = (list_view.id or "").removesuffix("-list")
        if mode == "stage" and pane != "unstaged":
            self.notify("Select a file in the Unstaged pane to stage it", severity="warning")
            return
        if mode == "unstage" and pane != "staged":
            self.notify("Select a file in the Staged pane to unstage it", severity="warning")
            return
        path = item.entry.path
        args = ["add", "--", path] if mode == "stage" else ["restore", "--staged", "--", path]
        try:
            subprocess.run(["git", "-C", str(self.repo), *args], check=True, capture_output=True)
        except subprocess.CalledProcessError as exc:
            if mode == "unstage":
                fallback = subprocess.run(
                    ["git", "-C", str(self.repo), "reset", "-q", "--", path],
                    capture_output=True,
                )
                if fallback.returncode == 0:
                    await self.refresh_lists()
                    return
            detail = exc.stderr.decode("utf-8", "replace").strip() or str(exc)
            self.notify(f"git {args[0]} failed: {detail}", severity="error")
            return
        await self.refresh_lists()

    def action_open_in_editor(self) -> None:
        path = self._selected_path()
        if path is None:
            self.notify("No file selected", severity="warning")
            return
        for editor in ("code-insiders", "code"):
            if shutil.which(editor):
                subprocess.Popen([editor, "-g", str(path)])
                return
        self.notify("Neither `code-insiders` nor `code` found on PATH", severity="error")

    def action_reveal(self) -> None:
        path = self._selected_path()
        if path is not None:
            subprocess.Popen(["open", "-R", str(path)])

    def action_copy_path(self) -> None:
        path = self._selected_path()
        if path is not None:
            subprocess.run(["pbcopy"], input=str(path).encode(), check=False)
            self.notify(f"Copied: {path}")

    async def action_refresh(self) -> None:
        await self.refresh_lists()
