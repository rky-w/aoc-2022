
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

puzzle = Puzzle(year=2022, day=9)

motions = puzzle.input_data.splitlines()

motions_test = [
    'R 4',
    'U 4',
    'L 3',
    'D 1',
    'R 4',
    'D 1',
    'L 5',
    'R 2',
]

motions_test2 = [
    'R 5',
    'U 8',
    'L 8',
    'D 3',
    'R 17',
    'D 10',
    'L 25',
    'U 20',
]


class Ropes():
    def __init__(self, ntails=1):
        self.h = np.array([0,0])
        self.t = [np.array([0,0]) for i in range(ntails + 1)]
        self.thist = list()

    def mvh(self, dir):
        if dir=='R':
            self.t[0][0] += 1
        elif dir=='L':
            self.t[0][0] -= 1
        elif dir=='U':
            self.t[0][1] += 1
        else:
            self.t[0][1] -= 1
        
    def mvt(self, h, t):
        diffx, diffy = h[0] - t[0], h[1] - t[1]
        if abs(h - t).sum() > 2:
            t[0] += diffx // abs(diffx)
            t[1] += diffy // abs(diffy)
        elif abs(diffx) > 1:
            t[0] += diffx // 2
        elif abs(diffy) > 1:
            t[1] += diffy // 2
        return t

    def move(self, motions):
        for motion in motions:
            dir, nc = motion.split(' ')
            steps = int(nc)
            for step in range(steps):
                self.mvh(dir)
                for i in range(1, len(self.t)):
                    self.t[i] = self.mvt(self.t[i-1], self.t[i])
                self.thist.append(str(self.t[i]))
    
    def npositions(self):
        return len(set(self.thist))

r = Ropes()
r.move(motions)

# Pt 1 answer
r.npositions()

# Pt 2 answer
r9 = Ropes(9)
r9.move(motions)
r9.npositions()