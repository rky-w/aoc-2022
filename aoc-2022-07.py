
from aocd.models import Puzzle
from string import ascii_letters
import re
from pprint import pprint
from copy import deepcopy
from collections import defaultdict

puzzle = Puzzle(year=2022, day=7)

log = puzzle.input_data.splitlines()

log = [
'$ cd /',
'$ ls',
'dir a',
'14848514 b.txt',
'8504156 c.dat',
'dir d',
'$ cd a',
'$ ls',
'dir e',
'29116 f',
'2557 g',
'62596 h.lst',
'$ cd e',
'$ ls',
'584 i',
'$ cd ..',
'$ cd ..',
'$ cd d',
'$ ls',
'4060174 j',
'8033020 d.log',
'5626152 d.ext',
'7214296 k'
]


# Class to build image of the file system
class FileSys:
    def __init__(self):
        self.cwd = '/'
        self.diridx = defaultdict(set)
        self.parents = defaultdict(set)
        self.fileidx = defaultdict(set)

    def cd(self, path):
        if path == '..':
            self.cwd = list(self.parents[self.cwd])[0]
        else:
            self.parents[path].add(self.cwd)
            self.cwd = path

    def ls(self, contents):
        for c in contents:
            res = re.match(r'^dir ([a-z]+)', c)
            if res:
                self.mkdir(res.group(1))
            else:
                self.touch(c)

    def mkdir(self, dirname):
        self.diridx[self.cwd].add(dirname)

    def touch(self, filename):
        self.fileidx[self.cwd].add(filename)

    def sizer(self):
        pass
        for loc in self.fileidx:
            for file in loc:
                res = re.match(r'^(\d+) (.*)$', file)
                if res:
                    res.group(1)


# Run through the commands to image the file system
fs = FileSys()
i = 0
while i < len(log):
    line = log[i]
    print(f'Logging: {line} (i={i})')
    if re.match(r'^\$ cd', line):
        fs.cd(line.split()[2])
        i += 1
    elif re.match(r'^\$ ls', line):
        i += 1
        contents = []
        while re.match('^[^\$].*', log[i]):
            contents.append(log[i])
            i += 1
            if i >= len(log):
                break
        fs.ls(contents)
    else:
        break
    fs.diridx
    fs.fileidx
    fs.parents
    fs.cwd
    print('---------')
    

# YOU ARE HERE
# Develop the sizer function to sum up file sizes within each directory