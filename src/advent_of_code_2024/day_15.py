directions = {">": 1, "v": 1j, "<": -1, "^": -1j}
neigh_dir = {"[": 1, "]": -1}


def parse_map(map_raw: str) -> dict[complex, str]:
    map = {}
    for i, line in enumerate(map_raw.split("\n")):
        for j, c in enumerate(line):
            map[complex(j, i)] = c
    return map


def parse(fn: str) -> tuple[dict[complex, str], str]:
    map_raw, instructions = open(fn).read().split("\n\n")
    expanded_raw = map_raw.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
    return parse_map(map_raw), parse_map(expanded_raw), instructions.replace("\n", "")


def can_move(pos: complex, dir: complex, map: dict[complex, str], skip=False) -> bool:
    match map[pos + dir]:
        case ".":
            return True
        case "#":
            return False
        case x if x in ["[", "]"] and dir.real == 0 and not skip:
            return can_move(pos + dir, dir, map) & can_move(
                pos + neigh_dir[x], dir, map, skip=True
            )
        case x if x in ["[", "]"] and dir.real != 0:
            return can_move(pos + dir, dir, map)
        case x if skip:
            return can_move(pos + dir, dir, map)
        case "O":
            return can_move(pos + dir, dir, map)


def move(pos: complex, dir: complex, map, skip=False) -> dict[complex, str]:
    if map[pos + dir] != ".":
        move(pos + dir, dir, map)
    map[pos], map[pos + dir] = map[pos + dir], map[pos]

    if (x := map[pos + dir]) in ["[", "]"] and dir.real == 0 and not skip:
        move(pos + neigh_dir[x], dir, map, skip=True)
    return map


def run_sequence(map: dict[complex, str], instructions: str) -> int:
    pos = [k for k, v in map.items() if v == "@"][0]
    for inst in instructions:
        if can_move(pos, dir := directions[inst], map):
            map, pos = move(pos, dir, map), pos + dir

    boxes = [k for k, v in map.items() if v in ["O", "["]]
    return int(sum(b.imag * 100 + b.real for b in boxes))


def solve(map, expanded_map, instructions: str) -> tuple[int, int]:
    return run_sequence(map, instructions), run_sequence(expanded_map, instructions)


if __name__ == "__main__":
    print(solve(*parse("inputs/day15.txt")))
