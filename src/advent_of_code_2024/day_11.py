from functools import cache


def parse(fn: str) -> list[int]:
    return list(map(int, open(fn).read().split()))


@cache
def stone_count(val: int, cycles: int) -> int:
    match val, cycles:
        case _, 0:
            return 1
        case 0, _:
            return stone_count(1, cycles - 1)
        case x, _ if ((d := len(val_str := str(x))) % 2) == 0:
            return stone_count(int(val_str[: d // 2]), cycles - 1) + stone_count(int(val_str[d // 2 :]), cycles - 1)
        case x:
            return stone_count(val * 2024, cycles - 1)


def solve(stones: list[int]) -> tuple[int, int]:
    return (
        sum(stone_count(x, 25) for x in stones),
        sum(stone_count(x, 75) for x in stones),
    )


if __name__ == "__main__":
    print(solve(parse("inputs/day11.txt")))
