from string import ascii_lowercase, ascii_uppercase

RAW = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

letter_score = "0" + ascii_lowercase + ascii_uppercase


def find_odd(line: str) -> str:
    length = len(line)
    a = set(line[: length // 2])
    b = set(line[length // 2 :])
    return (a.intersection(b)).pop()


def score(s: str) -> int:
    return letter_score.find(s)


def find_common(bags: list[str]) -> str:
    a, b, c = bags
    return ((set(a).intersection(set(b))).intersection(set(c))).pop()


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i : i + n]


print("Task #1")
assert sum(score(find_odd(x)) for x in RAW.splitlines()) == 157
with open("day03.txt") as f:
    RAW2 = f.read()
print(sum(score(find_odd(x)) for x in RAW2.splitlines()))

print("Task #2")
bag_list = RAW.strip().split()
scores = []
for chunk in chunks(bag_list, 3):
    scores.append(score(find_common(chunk)))
assert sum(scores) == 70
scores = []
for chunk in chunks(RAW2.strip().split(), 3):
    scores.append(score(find_common(chunk)))
print(sum(scores))
