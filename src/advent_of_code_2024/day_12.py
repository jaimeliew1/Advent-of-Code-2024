def parse(fn: str) -> dict[complex, str]:
    out = {}
    for i, line in enumerate(open(fn, "r").readlines()):
        for j, c in enumerate(line.strip()):
            out[complex(j, i)] = c
    return out


def solve(map: dict[complex, str]) -> tuple[int, int]:
    garden_price = 0
    unvisited = set(map.keys())
    while unvisited:
        letter = map[_pos := unvisited.pop()]
        next_in_block, area, perim = set([_pos]), 0, 0

        while next_in_block:
            pos = next_in_block.pop()
            neighbors = [
                pos + dir for dir in [1, 1j, -1, -1j] if map.get(pos + dir) == letter
            ]

            area, perim = area + 1, perim + 4 - len(neighbors)
            next_in_block.update([x for x in neighbors if x in unvisited])
            unvisited.discard(pos)
        garden_price += area * perim
    return garden_price, 0


if __name__ == "__main__":
    print(solve(parse("inputs/day12.txt")))
