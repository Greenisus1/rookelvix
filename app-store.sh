#!/bin/bash
# pi-app-store: 1
# pi-app-store-category: games
set -eu
cd -- "$(dirname -- "$0")"
case "${1:-}" in
  install) python3 -m venv .venv; .venv/bin/python -m pip install -r requirements.txt; .venv/bin/python -m py_compile rookelvix.py terminal_ui.py ;;
  run) test -x .venv/bin/python || { echo "Run install first."; exit 1; }; exec .venv/bin/python rookelvix.py ;;
  *) echo 'Use: bash app-store.sh install OR bash app-store.sh run'; exit 1 ;;
esac
