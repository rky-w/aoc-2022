
from aocd.models import Puzzle
from string import ascii_letters

puzzle = Puzzle(year=2022, day=3)

pks = puzzle.input_data.splitlines()

vals = dict(zip(ascii_letters, range(1,53)))

scr = 0
for pk in pks:
    sz = int(len(pk)/2)
    c1, c2 = pk[:sz], pk[sz:]
    j = set(c1).intersection(set(c2)).pop()
    scr += vals.get(j)

# Pt 1
print(scr)
