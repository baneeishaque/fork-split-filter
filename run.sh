#!/bin/sh
set -eu
DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
REPO="$(CDPATH= cd -- "${1:-$PWD}" && pwd)"
cd "$DIR"
exec ./.venv/bin/python -m fork_split_filter "$REPO"
