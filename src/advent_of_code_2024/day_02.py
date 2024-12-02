import numpy as np


def parse(fn: str) -> list[list[int]]:
    return [[int(x) for x in report.split()] for report in open(fn).readlines()]


def is_safe(rep: list[int]) -> bool:
    diff = np.diff(rep)
    return all((diff >= 1) & (diff <= 3)) or all((diff <= -1) & (diff >= -3))


def solve(reports: list[list[int]]) -> tuple[int, int]:
    ans1 = sum(is_safe(rep) for rep in reports)

    ans2 = 0
    for rep in reports:
        variations = [rep]
        for i in range(len(rep)):
            variations.append([x for idx, x in enumerate(rep) if idx != i])
        ans2 += any(is_safe(x) for x in variations)

    return ans1, ans2


if __name__ == "__main__":
    print(solve(parse("inputs/day02.txt")))
