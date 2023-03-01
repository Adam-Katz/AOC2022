from enum import Enum

RAW = """A Y
B X
C Z
"""


class Rps(Enum):
    ROCK = 1
    PAPER = 2
    SCISSSORS = 3

    @staticmethod
    def parse(s: str) -> "Rps":
        if s in ("A", "X"):
            return Rps.ROCK
        elif s in ("B", "Y"):
            return Rps.PAPER
        elif s in ("C", "Z"):
            return Rps.SCISSSORS
        else:
            raise ValueError("bad choice!")


def parse(raw: str) -> list[list[Rps]]:
    return [[Rps.parse(x) for x in line.split()] for line in raw.strip().splitlines()]


def score(opponent: Rps, me: Rps) -> int:
    if opponent == me:
        return 3 + me.value
    if (
        (opponent == Rps.ROCK and me == Rps.SCISSSORS)
        or (opponent == Rps.PAPER and me == Rps.ROCK)
        or (opponent == Rps.SCISSSORS and me == Rps.PAPER)
    ):
        return 0 + me.value
    return 6 + me.value


def score2(opponent: Rps, directions: Rps) -> int:
    if directions == Rps.ROCK:
        match opponent:
            case Rps.ROCK:
                me = Rps.SCISSSORS
            case Rps.PAPER:
                me = Rps.ROCK
            case Rps.SCISSSORS:
                me = Rps.PAPER
    elif directions == Rps.PAPER:
        me = opponent
    else:
        match opponent:
            case Rps.ROCK:
                me = Rps.PAPER
            case Rps.PAPER:
                me = Rps.SCISSSORS
            case Rps.SCISSSORS:
                me = Rps.ROCK
    return score(opponent, me)


with open("day02.txt") as f:
    RAW2 = f.read()

print("Task #1")
assert sum(score(*x) for x in parse(RAW)) == 15
print(sum(score(*x) for x in parse(RAW2)))
print("Task #2")
assert sum(score2(*x) for x in parse(RAW)) == 12
print(sum(score2(*x) for x in parse(RAW2)))
