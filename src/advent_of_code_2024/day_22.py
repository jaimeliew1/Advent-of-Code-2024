from collections import Counter, deque
from functools import cache


def parse(fn: str) -> list[int]:
    return [int(x) for x in open(fn).readlines()]


@cache
def next_number(w: int) -> int:
    x = ((w * 64) ^ w) % 16777216
    y = ((x // 32) ^ x) % 16777216
    return ((y * 2048) ^ y) % 16777216


def solve(initial: dict[complex, str]) -> tuple[int, int]:
    banana_count, ans1 = Counter(), 0
    for x in initial:
        seq = deque(maxlen=4)
        this_count = Counter()
        for _ in range(2000):
            x2 = next_number(x)
            seq.append((x2 % 10) - (x % 10))
            if len(seq) == 4 and tuple(seq) not in this_count:
                this_count[tuple(seq)] += x2 % 10
            x = x2
        banana_count += this_count
        ans1 += x

    return ans1, banana_count.most_common(1)[0][1]


if __name__ == "__main__":
    print(solve(parse("inputs/day22.txt")))
