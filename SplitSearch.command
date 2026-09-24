#!/bin/sh
REPO="$(cat "${TMPDIR:-/tmp}/fork-split-filter.repo" 2>/dev/null || pwd)"
exec "/Users/dk/lab-data/fork-split-filter/run.sh" "$REPO"
