import curses
from typer_cli.themes import THEMES, THEME_NAMES

# ── colors ───────────────────────────────────────────────────────────────────

C_DIM = 1
C_OK = 2
C_ERR = 3
C_CURSOR = 4
C_ACCENT = 5
C_STAT = 6
C_TITLE = 7
C_BORDER = 8
C_GOOD = 9
C_BAD = 10
C_HINT = 11


def init_colors(theme_name="default"):
    curses.start_color()
    curses.use_default_colors()
    theme = THEMES.get(theme_name, THEMES["default"])
    for pair_id, (fg, bg) in theme.items():
        curses.init_pair(pair_id, fg, bg)

