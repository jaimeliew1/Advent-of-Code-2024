"""
Fetches all available puzzle input files and saves it to the "inputs folder".
Requires aocd to be setup with your session ID.
"""

from pathlib import Path

import aocd
from rich import print

SAVEDIR = Path(__file__).parent.parent.parent / "inputs"
SAVEDIR.mkdir(exist_ok=True, parents=True)


def fetch():
    for day in range(1, 26):
        fn = SAVEDIR / f"day{day:02}.txt"

        if fn.exists():
            print(f"day{day:02} data already fetched.")
            continue

        print(f"fetching data for day{day:02}...")

        try:
            data = aocd.get_data(day=day, year=2024)
        except aocd.exceptions.PuzzleLockedError:
            print(f"day{day:02} is not available yet. Exiting")
            break

        print(f"saving to {fn}.")
        with open(fn, "w") as f:
            f.write(data)


if __name__ == "__main__":
    fetch()
