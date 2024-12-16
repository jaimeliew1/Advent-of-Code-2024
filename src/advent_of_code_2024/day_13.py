import re


def buttons_opt(x1, y1, x2, y2, x_target, y_target) -> int:
    det = x1 * y2 - x2 * y1

    a = (x_target * y2 - y_target * x2) // det
    b = (-x_target * y1 + y_target * x1) // det
    valid = (a * x1 + b * x2 == x_target) and (a * y1 + b * y2 == y_target)
    return 3 * a + b if valid else 0


def parse(fn: str) -> list[tuple[int, ...]]:
    out = []
    for block in open(fn, "r").read().split("\n\n"):
        out.append(tuple(int(x) for x in re.findall(r"(\d+)", block.replace("\n", ""))))
    return out


def solve(machines: list[tuple[int, ...]]) -> tuple[int, int]:
    part1, part2 = 0, 0
    for x1, y1, x2, y2, x_target, y_target in machines:
        part1 += buttons_opt(x1, y1, x2, y2, x_target, y_target)
        part2 += buttons_opt(
            x1, y1, x2, y2, x_target + 10000000000000, y_target + 10000000000000
        )
    return part1, part2


if __name__ == "__main__":
    print(solve(parse("inputs/day13.txt")))
