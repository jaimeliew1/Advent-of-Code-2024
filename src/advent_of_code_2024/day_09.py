from dataclasses import dataclass
from itertools import batched
import copy


@dataclass
class Block:
    loc: int
    length: int
    ID: int = None

    def checksum(self) -> int:
        return sum((self.loc + i) * self.ID for i in range(self.length))

    def expand(self) -> list["Block"]:
        return [Block(self.loc + i, 1, self.ID) for i in range(self.length)]


def parse(fn: str) -> list[Block]:
    data, empty, loc = [], [], 0
    for id, (a, b) in enumerate(batched(map(int, open(fn).read() + "0"), 2)):
        data.append(Block(loc, a, id))
        empty.append(Block(loc + a, b))
        loc += a + b
    return data, empty


def defrag_checksum(_data: list[Block], _empty: list[Block]) -> int:
    data, empty, idx_end = copy.deepcopy(_data), copy.deepcopy(_empty), len(_data) - 1
    while idx_end > 0:
        for idx_gap, gap in enumerate(empty):
            if gap.loc >= data[idx_end].loc:
                break
            if gap.length >= data[idx_end].length:
                data[idx_end].loc = gap.loc
                empty[idx_gap].loc += data[idx_end].length
                empty[idx_gap].length -= data[idx_end].length
                if empty[idx_gap].length == 0:
                    empty.pop(idx_gap)
                break
        idx_end -= 1
    return sum(x.checksum() for x in data)


def solve(data: list[Block], empty: list[Block]) -> tuple[int, int]:
    expanded = sum([x.expand() for x in data], [])
    return defrag_checksum(expanded, empty), defrag_checksum(data, empty)


if __name__ == "__main__":
    print(solve(*parse("inputs/day09.txt")))
