import sys

from blessings import Terminal

ESCAPE_CODE_MARGIN_BUFFER = 18


def write_over_live_message(str_to_write: str, term: Terminal):
    write_over_line(str_to_write, 2, term)


def write_over_progress_bar(green_pct: float, red_pct: float, term: Terminal):
    num_green_bars = int(green_pct * term.width)
    num_red_bars = int(red_pct * term.width)

    # Deal with rounding, converting to int could leave us with 1 bar less, so make it green
    if term.width - num_green_bars - num_red_bars == 1:
        num_green_bars += 1

    bar = term.green("█" * num_green_bars) + term.red("█" * num_red_bars)
    write_over_line(bar, 1, term)


def write_over_line(str_to_write: str, offset_from_bottom: int, term: Terminal):
    with term.location(0, term.height - offset_from_bottom):
        right_margin = max(0, term.width - len(str_to_write) + ESCAPE_CODE_MARGIN_BUFFER) * " "
        print(f"{str_to_write}{right_margin}")
        sys.stdout.flush()
