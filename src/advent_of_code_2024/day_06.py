def parse(fn: str) -> dict[complex, str]:
    out = {}
    for i, line in enumerate(open(fn, "r").readlines()):
        for j, c in enumerate(line.strip()):
            out[complex(j, i)] = c
    return out


def get_path(map: dict[complex, str]):
    pos = [k for k, v in map.items() if v == "^"][0]
    dir = -1j
    visited = set([(pos, dir)])
    while obj := map.get(pos + dir):
        if (pos + dir, dir) in visited:
            return set(x[0] for x in visited), True
        if obj in [".", "^"]:
            pos += dir
            visited.add((pos, dir))
        elif obj in ["#"]:
            dir *= 1j

    return set(x[0] for x in visited), False


def solve(map: dict[complex, str]) -> tuple[int, int]:
    visited, _ = get_path(map)
    loops = 0
    for obstacle_pos in visited:
        if map[obstacle_pos] != "^":
            loops += get_path(dict(map) | {obstacle_pos: "#"})[1]

    return len(visited), loops


if __name__ == "__main__":
    print(solve(parse("inputs/day06.txt")))
