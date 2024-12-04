def parse(fn: str) -> dict[complex, str]:
    out = {}
    for i, line in enumerate(open(fn, "r").readlines()):
        for j, c in enumerate(line):
            out[complex(j, i)] = c
    return out


def solve(puz: dict[complex, str]) -> tuple[int, int]:
    ans1, ans2 = 0, 0
    for p in puz.keys():
        for dir in [1, 1 + 1j, 1j, -1 + 1j, -1, -1 - 1j, -1j, 1 - 1j]:
            match (puz.get(p), puz.get(p + dir), puz.get(p + 2 * dir), puz.get(p + 3 * dir)):
                case ("X", "M", "A", "S"):
                    ans1 += 1

        if puz[p] == "A":
            match (puz.get(p + 1 + 1j), puz.get(p + 1 - 1j), puz.get(p - 1 - 1j), puz.get(p - 1 + 1j)):
                case (("M", "M", "S", "S") | ("S", "M", "M", "S") | ("S", "S", "M", "M") | ("M", "S", "S", "M")):
                    ans2 += 1

    return ans1, ans2


if __name__ == "__main__":
    print(solve(parse("inputs/day04.txt")))
