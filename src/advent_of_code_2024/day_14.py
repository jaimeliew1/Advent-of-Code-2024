import re

XLIM, YLIM = 101, 103


def parse(fn: str) -> tuple[list[complex], ...]:
    pos, vels = [], []
    for line in open(fn, "r").readlines():
        ints = [int(x) for x in re.findall(r"([-]?\d+)", line)]
        pos.append((ints[0], ints[1]))
        vels.append((ints[2], ints[3]))
    return pos, vels


def safety_factor(pos) -> int:
    a = sum(x < XLIM // 2 and y < YLIM // 2 for x, y in pos)
    b = sum(x > XLIM // 2 and y < YLIM // 2 for x, y in pos)
    c = sum(x > XLIM // 2 and y > YLIM // 2 for x, y in pos)
    d = sum(x < XLIM // 2 and y > YLIM // 2 for x, y in pos)
    return a * b * c * d


def iterate(pos, vels, n=1) -> list[tuple[int]]:
    out = []
    for (x, y), (dx, dy) in zip(pos, vels):
        out.append(((x + n * dx) % XLIM, (y + n * dy) % YLIM))
    return out


def solve(pos, vels) -> tuple[int, int]:
    for i in range(100000):
        if i == 100:
            part1 = safety_factor(pos)
        if safety_factor(pos) < 33000000:
            return part1, i
        pos = iterate(pos, vels)


if __name__ == "__main__":
    print(solve(*parse("inputs/day14.txt")))
