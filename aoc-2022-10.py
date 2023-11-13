
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

puzzle = Puzzle(year=2022, day=10)

prog = puzzle.input_data.splitlines()


class Circuit():
    def __init__(self, prog):
        self.prog = prog.copy()
        self.cycle = 0
        self.X = 1
        self.addx_n = 0
        self.sig = 0
        self.disp = ''

    def draw(self):
        if (self.X - 1) <= (
            (self.cycle - (((self.cycle-1) // 40) * 40)) - 1
            ) <= (self.X + 1):
            self.disp += '#'
        else:
            self.disp += '.'
        if self.cycle  == ((self.cycle // 40) * 40):
            self.disp += '\n'
    
    def run(self):
        while c.prog:
            self.cycle += 1
            cmd = self.prog[0]
            self.draw()

            if (self.cycle  == ((self.cycle - 20) // 40) * 40 + 20):
                self.sig += self.cycle * self.X
            if cmd == 'noop':
                self.prog.pop(0)
            else:
                if self.addx_n > 0:
                    task, val = cmd.split(' ')
                    self.X += int(val)
                    self.prog.pop(0)
                    self.addx_n = 0
                else:
                    self.addx_n += 1

c = Circuit(prog)
c.run()

# Pt 1 answer
print(c.sig)

# Pt 2
print(c.disp)
