
from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=1)

cals = []
tot = 0
for val in puzzle.input_data.splitlines():
    if val == '':
        cals.append(tot)
        tot = 0
    else:
        tot += int(val)

max(cals)

sum(sorted(cals, reverse=True)[:3])