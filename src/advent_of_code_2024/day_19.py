from functools import cache


def parse(fn: str):
    towels, patterns = open(fn).read().split("\n\n")
    return towels.split(", "), patterns.split()


def solve(towels: list[str], patterns: list[str]) -> tuple[int, int]:
    @cache
    def count_combos(pattern: str) -> int:
        count = 0
        for towel in towels:
            if not pattern.startswith(towel):
                continue
            elif towel == pattern:
                count += 1
            elif c := count_combos(pattern[len(towel) :]):
                count += c
        return count

    combos = [count_combos(x) for x in patterns]
    return sum(x > 0 for x in combos), sum(combos)


if __name__ == "__main__":
    print(solve(*parse("inputs/day19.txt")))
