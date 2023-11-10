
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

trees_test = [
    '30373',
    '25512',
    '65332',
    '33549',
    '35390',
]

ta = np.array([list(row) for row in trees], dtype=int).T
visarr = np.zeros_like(ta)

mx = ta.shape[0]
my = ta.shape[1]

for x in range(ta.shape[0]):
    for y in range(ta.shape[1]):
        tree = ta[x, y]
        col=ta[x,:]
        row=ta[:,y]

        # right
        if tree > np.append(row[0:x], -1).max():
            visarr[x, y] +=1
        # left
        if tree > np.append(row[x+1:mx], -1).max():
            visarr[x, y] += 1
        # down
        if tree > np.append(col[0:y], -1).max():
            visarr[x, y] += 1
        # up
        if tree > np.append(col[y+1:my], -1).max():
            visarr[x, y] += 1


# Pt 1 answer
print((visarr > 0).sum())


# pt 2
def vistrees(line, tree):
    ci = 0
    for t in line:
        ci += 1
        if t >= tree:
            break
    return ci

best_score = 0
for x in range(ta.shape[0]):
    for y in range(ta.shape[1]):
        tree = ta[x, y]
        col=ta[x,:]
        row=ta[:,y]
        rvis = vistrees(row[x+1:mx], tree)
        lvis = vistrees(row[x-1::-1], tree)
        uvis = vistrees(col[y-1::-1], tree)
        dvis = vistrees(col[y+1:my], tree)
        score = rvis * lvis * uvis * dvis
        best_score = max(best_score, score)

# pt 2 answer
print(best_score)