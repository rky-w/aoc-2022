
from aocd.models import Puzzle
from string import ascii_letters
import re
import os
import time
from pprint import pprint
from copy import deepcopy
from collections import defaultdict
import pandas as pd
import numpy as np

puzzle = Puzzle(year=2022, day=8)

trees = puzzle.input_data.splitlines()

trees = [
    '30373',
    '25512',
    '65332',
    '33549',
    '35390',
]

ta = np.array([list(row) for row in trees], dtype=int)

visarr = np.zeros_like(ta)

for x in range(ta.shape[0]):
    for y in range(ta.shape[1]):
        tree = ta[x, y]
        row=ta[x,:]
        # right
        for i in row[]
        # left
        # down
        # up
        


        print(ta[row, col])