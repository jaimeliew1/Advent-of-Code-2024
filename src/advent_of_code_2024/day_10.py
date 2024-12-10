from collections import Counter


def parse(fn: str) -> dict[complex, int]:
    out = {}
    for i, line in enumerate(open(fn, "r").readlines()):
        for j, c in enumerate(line.strip()):
            out[complex(j, i)] = int(c)
    return out


def solve(map: dict[complex, int]) -> tuple[int, int]:
    def DFS(start: complex) -> Counter:
        out = Counter()
        for dir in [1, 1j, -1, -1j]:
            match map.get(start + dir):
                case 9 if map[start] == 8:
                    out[start + dir] += 1
                case x if x == map[start] + 1:
                    out += DFS(start + dir)
        return out

    part1, part2 = 0, 0
    for trailhead in (k for k, v in map.items() if v == 0):
        peaks = DFS(trailhead)
        part1 += len(peaks)
        part2 += sum(peaks.values())

    return part1, part2


if __name__ == "__main__":
    print(solve(parse("inputs/day10.txt")))
