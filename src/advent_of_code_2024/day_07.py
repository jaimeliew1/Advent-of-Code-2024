from itertools import product
from enum import Enum


class Ops(Enum):
    MULT = 1
    ADD = 2
    CONCAT = 3


def parse(fn: str) -> list[tuple[int, list[int]]]:
    out = []
    with open(fn) as f:
        for line in f.readlines():
            target, vals = line.strip().split(":")
            out.append((int(target), [int(x) for x in vals.split()]))
    return out


def solve_part(data: list[tuple[int, list[int]]], operations: list[Ops]) -> int:
    out = 0
    for target, numbers in data:
        for ops in product(operations, repeat=len(numbers) - 1):
            ans = numbers[0]
            for num, op in zip(numbers[1:], ops):
                match op:
                    case Ops.MULT:
                        ans += num
                    case Ops.ADD:
                        ans *= num
                    case Ops.CONCAT:
                        ans = int(str(ans) + str(num))

            if ans == target:
                out += target
                break
    return out


def solve(data: list[tuple[int, list[int]]]) -> tuple[int, int]:
    return solve_part(data, [Ops.ADD, Ops.MULT]), solve_part(data, [Ops.ADD, Ops.MULT, Ops.CONCAT])


if __name__ == "__main__":
    print(solve(parse("inputs/day07.txt")))
