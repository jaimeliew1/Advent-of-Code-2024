from itertools import combinations


def parse(fn: str) -> dict[str, list[complex]]:
    out = {}
    for i, line in enumerate(open(fn, "r").readlines()):
        for j, c in enumerate(line.strip()):
            out.setdefault(c, []).append(complex(j, i))
    del out["."]
    return out


def count_antinodes(antennas: dict[str, list[complex]], multiples: int) -> int:
    antinodes = []
    for _frequency, locations in antennas.items():
        for a, b in combinations(locations, r=2):
            for m in multiples:
                antinodes.extend([a + m * (a - b), b + m * (b - a)])
    return sum((0 <= x.real < 50) & (0 <= x.imag < 50) for x in set(antinodes))


def solve(antennas: dict[str, list[complex]]) -> tuple[int, int]:
    return count_antinodes(antennas, [1]), count_antinodes(antennas, range(50))


if __name__ == "__main__":
    print(solve(parse("inputs/day08.txt")))
