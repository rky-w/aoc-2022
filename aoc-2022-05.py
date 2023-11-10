
from aocd.models import Puzzle
from string import ascii_letters
import re
from pprint import pprint
from copy import deepcopy

puzzle = Puzzle(year=2022, day=5)

inp = puzzle.input_data.splitlines()


# Parse puzzle input into stacks, indexes, and patterns
stks = []
pats = []
for r in inp:
    if re.match(r'^[\s\d]+$', r):
        idxs = r
    elif re.match(r'^move', r):
        mt = re.match(r'^move (\d+) from (\d+) to (\d+)$', r)
        pats.append((int(mt.group(1)), int(mt.group(2)), int(mt.group(3))))
    elif r != '':
        stks.append(r)


# Convert stacks to lists (last value as top of stack)
i = 0
stkl = []
idxl = []
for p in idxs:
    if p != ' ':
        nl = []
        for r in stks:
            if r[i] != ' ':
                nl.insert(0, r[i])
        stkl.append(nl)
        idxl.append(p)
    i += 1


# Function to move boxes
def mover(pats, stkl, pt2=False):
    stk = deepcopy(stkl)
    for ptn in pats:
        if pt2:
            stk[ptn[2]-1].extend(stk[ptn[1]-1][-ptn[0]:])
            stk[ptn[1]-1] = stk[ptn[1]-1][:-ptn[0]]
        else:
            for i in range(ptn[0]):
                stk[ptn[2]-1].append(stk[ptn[1]-1].pop())
    return(''.join(l[-1] for l in stk))


# Pt 1
print(mover(pats, stkl))

# Pt 2
print(mover(pats, stkl, pt2=True))