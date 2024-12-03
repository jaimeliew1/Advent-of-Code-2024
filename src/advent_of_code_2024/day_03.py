import re


def mult_sum(x):
    return sum(int(a) * int(b) for a, b in re.findall(r"mul\((\d+),(\d+)\)", x))


def solve(program: str) -> tuple[int, int]:
    ans2 = 0
    for i, group in enumerate(program.split("don't()")):
        if i != 0 and "do()" not in group:
            continue
        if i != 0:
            group = group.split("do()", maxsplit=1)[-1]
        ans2 += mult_sum(group)

    return mult_sum(program), ans2


if __name__ == "__main__":
    print(solve(open("inputs/day03.txt").read()))
