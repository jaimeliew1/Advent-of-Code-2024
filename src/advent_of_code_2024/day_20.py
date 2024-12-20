def parse(fn: str) -> dict[complex, str]:
    out = {}
    for j, line in enumerate(open(fn).readlines()):
        for i, c in enumerate(line.strip()):
            out[complex(i, j)] = c
    return out


def solve(map: dict[complex, str]) -> tuple[int, int]:
    start = [k for k, v in map.items() if v == "S"][0]
    end = [k for k, v in map.items() if v == "E"][0]

    path, pos = {end: 0}, end
    while pos != start:
        for dir in [1, -1, 1j, -1j]:
            if map[pos + dir] != "#" and (pos + dir not in path):
                path[pos + dir] = path[pos] + 1
                pos = pos + dir

    part1, part2 = 0, 0
    for pos, dist in path.items():
        for cheat in path:
            d = abs(cheat.real - pos.real) + abs(cheat.imag - pos.imag)
            if d == 2:
                part1 += dist - d - path[cheat] >= 100
            if d <= 20:
                part2 += dist - d - path[cheat] >= 100

    return part1, part2


if __name__ == "__main__":
    print(solve(parse("inputs/day20.txt")))
