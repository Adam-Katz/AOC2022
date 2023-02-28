from dataclasses import dataclass

RAW = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

@dataclass
class Elf:
    foods: list[int]

    def cals(self) -> int:
        return sum(self.foods)

def parse(raw) -> list[Elf]:
    return [Elf([int(x) for x in lines.split()]) for lines in raw.strip().split("\n\n")]

with open('day01.txt', 'r') as f:
    elves = parse(f.read())
print('Task #1')
print(max(elf.cals() for elf in elves))
print('Task #2')
print(sum(sorted([elf.cals() for elf in elves], reverse=True)[:3]))