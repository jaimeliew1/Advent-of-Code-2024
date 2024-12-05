from dataclasses import dataclass

IS_AFTER: dict[int, list[int]] = {}


@dataclass
class Page:
    page: int

    def __lt__(self, other) -> bool:
        if is_after := IS_AFTER.get(self.page):
            return other.page in is_after
        return False


def parse(fn: str) -> list[list[Page]]:
    ordering, manuals = open(fn).read().split("\n\n")
    for l, r in [x.split("|") for x in ordering.split()]:
        IS_AFTER.setdefault(int(l), [int(r)]).append(int(r))

    return [[Page(int(x)) for x in line.split(",")] for line in manuals.split()]


def solve(manuals: list[list[Page]]) -> tuple[int, int]:
    ans1, ans2 = 0, 0
    for manual in manuals:
        if all(manual[i] < manual[i + 1] for i in range(len(manual) - 1)):
            ans1 += manual[len(manual) // 2].page
        else:
            ans2 += sorted(manual)[len(manual) // 2].page
    return ans1, ans2


if __name__ == "__main__":
    print(solve(parse("inputs/day05.txt")))
