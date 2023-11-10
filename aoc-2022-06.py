
from aocd.models import Puzzle
from string import ascii_letters
import re
from pprint import pprint
from copy import deepcopy

puzzle = Puzzle(year=2022, day=6)

buf = puzzle.input_data.splitlines()[0]

def getmarker(buf, n=4):
    i = 0
    while i < len(buf):
        p = buf[i:i+n]
        if len(set(p)) == n:
            break
        i += 1
    return(i+n)

# Pt 1
print(getmarker(buf))

# Pt 2
print(getmarker(buf, n=14))