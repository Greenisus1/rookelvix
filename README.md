# Rookelvix

Offline terminal chess against a simple opponent. Version 1.0.1. Original terminal artwork; no account, desktop or telemetry. No assets or names taken from other games.

## Install and run

    bash app-store.sh install
    bash app-store.sh run

Python3.8+ with curses, pip and venv support. `install` creates .venv and downloads pinned chess 1.11.2 from PyPI. On DietPi, install python3-venv if venv creation reports it missing. Nothing changes system Python packages. Network required only for dependency installation. No arbitrary moving-main installer. GPL3-or-later code uses GPL3-or-later chess library; library not bundled. No strong engine dependency.

You play White. Type legal coordinate moves such as e2e4, then Enter. Promotions need a suffix such as a7a8q. Q quits with empty input, R restarts with empty input; Backspace edits. Uppercase white pieces, lowercase black. Full standard legal moves handled by chess library (castling, en passant, promotion, check, mate and draws). Draws are automatically accepted as soon as claimable. AI is a one-ply material/check/mate picker with random ties, not a strong chess engine. No chess clock, multiplayer, undo, saves or opening book.

Interactive curses terminal at least 68x18. Too-small windows show a resize notice and retain/pause the game. Terminal default, no GUI and no desktop requirement. R with --seed restarts the same seeded sequence, otherwise a fresh random board. For a non-interactive snapshot, use:

    .venv/bin/python rookelvix.py --seed 42 --demo

For tests:

    .venv/bin/python -m unittest -v

10 core tests plus actual Linux PTY visual/input smoke. Linux tested; physical Raspberry Pi and non-Linux untested. Without curses the interactive game is unavailable. No paid features. games category marker line3; older stores still list/launch it. GPL3-or-later; see LICENSE.txt. Dependency sources: https://pypi.org/project/chess/ and https://python-chess.readthedocs.io/en/latest/ .

1.0.1: terminal initialization failure returns error status rather than false success. Move input limited to coordinate/promotion characters and five characters; invalid input still checked by legal-move library. Core game rules unchanged.

Fullscreen update: Store interactive launch uses terminal-sized board cells or wrapped full-terminal utility input/results with PgUp/PgDn scrolling. Original core rules and direct CLI commands remain unchanged. Ctrl+C cancels utility entry, result Enter returns; no new dependency downloads. Linux PTY resize/restoration checked; physical Pi untested.
