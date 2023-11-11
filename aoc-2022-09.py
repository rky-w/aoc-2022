
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

class Ropes():
    def __init__(self):
        self.h = np.array([0,0])
        self.t = np.array([0,0])
        self.thist = list()

    def mvh(self, dir):
        if dir=='R':
            self.h[0] += 1
        elif dir=='L':
            self.h[0] -= 1
        elif dir=='U':
            self.h[1] += 1
        else:
            self.h[1] -= 1
        
    def mvt(self):
        diffx, diffy = self.h[0] - self.t[0], self.h[1] - self.t[1]
        if abs(self.h - self.t).sum() > 2:
            self.t[0] += diffx // abs(diffx)
            self.t[1] += diffy // abs(diffy)
        elif abs(diffx) > 1:
            self.t[0] += diffx // 2
        elif abs(diffy) > 1:
            self.t[1] += diffy // 2

    def move(self, motions):
        for motion in motions:
            dir, nc = motion.split(' ')
            steps = int(nc)
            for step in range(steps):
                self.mvh(dir)
                self.mvt()
                self.thist.append(str(self.t))
    
    def npositions(self):
        return len(set(self.thist))


r = Ropes()
r.move(motions)

# Pt 1 answer
r.npositions()
