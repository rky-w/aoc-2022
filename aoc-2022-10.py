
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

prog = [
    'noop',
    'addx 3',
    'addx -5',
]

prog = [
    'addx 15',  
    'addx -11', 
    'addx 6',   
    'addx -3',  
    'addx 5',   
    'addx -1',  
    'addx -8',  
    'addx 13',  
    'addx 4',   
    'noop', 
    'addx -1',  
    'addx 5',   
    'addx -1',  
    'addx 5',   
    'addx -1',  
    'addx 5',   
    'addx -1',  
    'addx 5',   
    'addx -1',  
    'addx -35', 
    'addx 1',   
    'addx 24',  
    'addx -19', 
    'addx 1',   
    'addx 16',  
    'addx -11', 
    'noop', 
    'noop', 
    'addx 21',  
    'addx -15', 
    'noop', 
    'noop', 
    'addx -3',  
    'addx 9',   
    'addx 1',   
    'addx -3',  
    'addx 8',   
    'addx 1',   
    'addx 5',   
    'noop', 
    'noop', 
    'noop', 
    'noop', 
    'noop', 
    'addx -36', 
    'noop', 
    'addx 1',   
    'addx 7',   
    'noop', 
    'noop', 
    'noop', 
    'addx 2',   
    'addx 6',   
    'noop', 
    'noop', 
    'noop', 
    'noop', 
    'noop', 
    'addx 1',   
    'noop', 
    'noop', 
    'addx 7',   
    'addx 1',   
    'noop', 
    'addx -13', 
    'addx 13',  
    'addx 7',   
    'noop', 
    'addx 1',   
    'addx -33', 
    'noop', 
    'noop', 
    'noop', 
    'addx 2',   
    'noop', 
    'noop', 
    'noop', 
    'addx 8',   
    'noop', 
    'addx -1',  
    'addx 2',   
    'addx 1',   
    'noop', 
    'addx 17',  
    'addx -9',  
    'addx 1',   
    'addx 1',   
    'addx -3',  
    'addx 11',  
    'noop', 
    'noop', 
    'addx 1',   
    'noop', 
    'addx 1',   
    'noop', 
    'noop', 
    'addx -13', 
    'addx -19', 
    'addx 1',   
    'addx 3',   
    'addx 26',  
    'addx -30', 
    'addx 12',  
    'addx -1',  
    'addx 3',   
    'addx 1',   
    'noop', 
    'noop', 
    'noop', 
    'addx -9',  
    'addx 18',  
    'addx 1',   
    'addx 2',   
    'noop', 
    'noop', 
    'addx 9',   
    'noop', 
    'noop', 
    'noop', 
    'addx -1',  
    'addx 2',   
    'addx -37', 
    'addx 1',   
    'addx 3',   
    'noop', 
    'addx 15',  
    'addx -21', 
    'addx 22',  
    'addx -6',  
    'addx 1',   
    'noop', 
    'addx 2',   
    'addx 1',   
    'noop', 
    'addx -10', 
    'noop', 
    'noop', 
    'addx 20',  
    'addx 1',   
    'addx 2',   
    'addx 2',   
    'addx -6',  
    'addx -11', 
    'noop', 
    'noop', 
    'noop', 
]

class Circuit():
    def __init__(self, prog):
        self.prog = prog.copy()
        self.cycle = 0
        self.X = 1
        self.addx_n = 0
        self.sig = 0
    
    def run(self):
        while c.prog:
            self.cycle += 1
            cmd = self.prog[0]
            # print()
            # print('cycle: ', self.cycle)
            # print('cmd: ', cmd)
            # print('X: ', self.X)
            if (self.cycle  == ((self.cycle - 20) // 40) * 40 + 20):
                self.sig += self.cycle * self.X
            if self.cycle >= 220:
                break
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

