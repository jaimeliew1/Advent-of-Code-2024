"""
Notes:
- The A register is better interpreted as several 8-bit bytes.
- The right-most bytes determine the right-most 8-bit output values.
- To generate its own source code (i.e. a quine), work out the left-most values
of A first, which determine the right-most value of the program.
- Can be solved recursively.
- There may be multiple candidates which produce the same output at each
recursion. record all candidates. Finally, return the minimum candidate for the
full program.
"""

from rich import print


def parse(fn: str) -> tuple[list[int], int, int, int]:
    register_raw, prog_raw = open(fn).read().split("\n\n")
    A, B, C = [int(x.split(":")[1]) for x in register_raw.split("\n")]
    return list(map(int, prog_raw.split(":")[1].split(","))), A, B, C


def compute(prog: list[int], A: int, B: int, C: int) -> list[int]:
    def combo(x):
        match x:
            case 4:
                return A
            case 5:
                return B
            case 6:
                return C
            case 7:
                raise ValueError
            case x:
                return x

    cursor = 0
    out = []
    while cursor < len(prog):
        match prog[cursor], prog[cursor + 1]:
            case 0, x:
                A = A // 2 ** combo(x)
            case 1, x:
                B ^= x
            case 2, x:
                B = combo(x) % 8
            case 3, x if A != 0:
                cursor = x
                continue
            case 4, _:
                B = B ^ C
            case 5, x:
                out.append(combo(x) % 8)
            case 6, x:
                B = A // 2 ** combo(x)
            case 7, x:
                C = A // 2 ** combo(x)
        cursor += 2

    return out


def quine(prog: list[int], full_prog: list[int]) -> list[int]:
    if len(prog) == 0:
        return [0]
    candidates = []
    for a in quine(prog[1:], full_prog):
        for _a in range(8):
            if compute(full_prog, a * 8 + _a, 0, 0) == prog:
                candidates.append(a * 8 + _a)
    return candidates


def solve(prog: list[int], A: int, B: int, C: int) -> tuple[str, int]:
    part1 = compute(prog, A, B, C)
    return ",".join(str(x) for x in part1), min(quine(prog, prog))


if __name__ == "__main__":
    print(solve(*parse("inputs/day17.txt")))
