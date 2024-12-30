def parse(fn: str) -> list[int]:
    init_raw, connections_raw = open(fn).read().split("\n\n")
    init = {}
    for y in init_raw.split("\n"):
        x1, x2 = y.split(":")
        init[x1] = int(x2)

    connections = []
    for line in connections_raw.split("\n"):
        x = line.split()
        connections.append((x[0], x[1], x[2], x[4]))

    return init, connections


def solve(state: dict[int], connections: list[tuple]) -> tuple[int, int]:
    while len(connections) > 0:
        A, gate, B, out = connections.pop(0)
        if A in state and B in state:
            match gate:
                case "AND":
                    state[out] = state[A] & state[B]
                case "OR":
                    state[out] = state[A] | state[B]
                case "XOR":
                    state[out] = state[A] ^ state[B]
        else:
            connections.append((A, gate, B, out))

    bits = [v for k, v in sorted(state.items()) if k.startswith("z")]
    val = sum(b * 2**n for n, b in enumerate(bits))

    return val, 0


if __name__ == "__main__":
    print(solve(*parse("inputs/day24.txt")))
