def parse(fn: str) -> tuple[list[int], list[int]]:
    out = [x.split("   ") for x in open(fn).readlines()]
    return [int(x[0]) for x in out], [int(x[1]) for x in out]


def solve(left: list[int], right: list[int]) -> tuple[int, int]:
    part1 = sum(abs(a - b) for a, b in zip(sorted(left), sorted(right)))
    part2 = sum(a * right.count(a) for a in left)
    return part1, part2


if __name__ == "__main__":
    print(solve(*parse("inputs/day01.txt")))
