from advent_of_code_2024.utils import print_complex_map


def parse(fn: str) -> tuple[dict[complex, str], str]:
    map_raw, instructions = open(fn).read().split("\n\n")
    map = {}
    for i, line in enumerate(map_raw.split("\n")):
        for j, c in enumerate(line):
            map[complex(j, i)] = c
    return map, instructions.replace("\n", "")


directions = {">": 1, "v": 1j, "<": -1, "^": -1j}


def move(inst: str, map: dict[complex, str]) -> dict[complex, str]:
    pos = [k for k, v in map.items() if v == "@"][0]
    dir = directions[inst]
    next_vacant = pos

    while (v := map[next_vacant]) in ["@", "O"]:
        next_vacant += dir
    if v == "#":
        return map

    buffer = "."
    while pos != next_vacant:
        buffer, map[pos] = map[pos], buffer
        pos += dir
    map[pos] = buffer
    return map


def GPS(map: dict[complex, str]) -> int:
    boxes = [k for k, v in map.items() if v == "O"]
    return int(sum(b.imag * 100 + b.real for b in boxes))


def solve(map: dict[complex, str], instructions: str) -> tuple[int, int]:
    print_complex_map(map)
    for inst in instructions:
        map = move(inst, map)
    return GPS(map), 0


if __name__ == "__main__":
    print(solve(*parse("inputs/day15.txt")))
