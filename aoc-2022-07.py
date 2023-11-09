
from aocd.models import Puzzle
from string import ascii_letters
import re
import os
import time
from pprint import pprint
from copy import deepcopy
from collections import defaultdict
from fs.memoryfs import MemoryFS

puzzle = Puzzle(year=2022, day=7)

log = puzzle.input_data.splitlines()

# Class to build image of the file system
class FileSys():
    def __init__(self):
        self.fs = MemoryFS()
        self.cpath = []
        self.dirszs = dict()

    def cd(self, dir):
        if dir == '..':
            self.cpath.pop()
        else:
            self.cpath.append(dir)
            self.fs.makedir('/'.join(self.cpath), recreate=True)
            
    def ls(self, contents):
        dirsize = 0
        for c in contents:
            isdir = re.match(r'^dir ([a-z]+)', c)
            if isdir:
                self.fs.makedir('/'.join(self.cpath + [isdir.group(1)]))
            else:
                dirsize += int(re.match(r'^(\d+)', c).group(1))
        self.fs.writetext('/'.join(self.cpath + [str(dirsize)]),'')
    
    def image(self, log):
        i = 0
        while i < len(log):
            line = log[i]
            # print(f'Logging: {line} (i={i})')
            if re.match(r'^\$ cd', line):
                self.cd(line.split()[2])
                i += 1
            elif re.match(r'^\$ ls', line):
                i += 1
                contents = []
                while re.match('^[^\$].*', log[i]):
                    contents.append(log[i])
                    i += 1
                    if i >= len(log):
                        break
                self.ls(contents)
            else:
                break

    def sizer(self):
        for dir in self.fs.walk.dirs():
            fsizes = 0
            for file in self.fs.walk.files(dir):
                fsizes += int(re.match(r'.*/(\d+)$', file).group(1))
            self.dirszs[dir] = fsizes
    



# Run through the command log to image the file system then get directory sizes
fs = FileSys()
fs.image(log)
fs.sizer()

# Pt 1 answer
print(sum(v for v in fs.dirszs.values() if v < 100000))


# Pt 2
totsize = 0
for file in fs.fs.walk.files():
    totsize += int(re.match(r'.*/(\d+)$', file).group(1))

print(min(dirsz for dirsz in fs.dirszs.values() if dirsz >= (30000000 - (70000000 - totsize))))
