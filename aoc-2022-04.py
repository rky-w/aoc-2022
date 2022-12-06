
from aocd.models import Puzzle
from string import ascii_letters
import re

puzzle = Puzzle(year=2022, day=4)

prs = puzzle.input_data.splitlines()

n, p = 0, 0
for pr in prs:
    mtc = re.match(r'^(\d+)-(\d+),(\d+)-(\d+)$', pr)
    cd = [int(mtc.group(i)) for i in range(1, 5)]
    n += cd[0] >= cd[2] and cd[1] <= cd[3] or cd[2] >= cd[0] and cd[3] <= cd[1]
    
    s1 = set(range(cd[0], cd[1]+1))
    s2 = set(range(cd[2], cd[3]+1))
    p += len(s1.intersection(s2)) > 0

# Pt 1
print(n)

# Pt 2
print(p)