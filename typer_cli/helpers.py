import curses 
from typer_cli.colors import (
    C_BORDER, C_ERR
)

# ── draw helpers ─────────────────────────────────────────────────────────────

def cx(w, n):
    return max(0, (w - n) // 2)


def put(win, y, x, text, cp=0, attr=0):
    try:
        win.addstr(y, x, text, curses.color_pair(cp) | attr)
    except curses.error:
        pass


def putc(win, y, w, text, cp=0, attr=0):
    put(win, y, cx(w, len(text)), text, cp, attr)


def hline(win, y, x, n, cp=C_BORDER):
    put(win, y, x, "-" * n, cp)


def wrap(text, width):
    lines, cur = [], ""
    for word in text.split(" "):
        test = f"{cur} {word}" if cur else word
        if len(test) <= width:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines
# ── error ────────────────────────────────────────────────────────────────────

def error(scr, message):
    _,w = scr.getmaxyx()
    putc(scr, 1, w, message, C_ERR)
