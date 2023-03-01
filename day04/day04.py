from dataclasses import dataclass

RAW = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


@dataclass
class Elf:
    lo: int
    hi: int

    @staticmethod
    def parse(s: str) -> "Elf":
        return Elf(*[int(x) for x in s.split("-")])


def fully_contained(elf1: Elf, elf2: Elf) -> bool:
    if (
        (elf1.lo >= elf2.lo and elf1.hi <= elf2.hi)
        or elf2.lo >= elf1.lo
        and elf2.hi <= elf1.hi
    ):
        return True
    return False


def overlap(elf1: Elf, elf2: Elf) -> bool:
    if ((elf1.lo <= elf2.lo <= elf1.hi) or (elf1.lo <= elf2.hi <= elf1.hi)) or (
        (elf2.lo <= elf1.lo <= elf2.hi) or (elf2.lo <= elf1.hi <= elf2.hi)
    ):
        return True
    return False


def parse(raw: str) -> list[list[Elf, Elf]]:
    return [[Elf.parse(x) for x in line.split(",")] for line in raw.strip().split()]


pair_list = parse(RAW)
assert sum(fully_contained(*x) for x in pair_list) == 2
print("Task #1")
puzzle_input = parse(open("day04.txt").read())
print(sum(fully_contained(*x) for x in puzzle_input))

print("Task #2")
assert sum(overlap(*x) for x in pair_list) == 4
print(sum(overlap(*x) for x in puzzle_input))
