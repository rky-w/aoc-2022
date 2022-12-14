
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
        self.fileszs = defaultdict(set)
        self.dirszs = defaultdict(set)

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

    # Recursion through tree to add sum of files in child dirs
    def _sizer(self, node):
        if not self.diridx.get(node):
            return list(self.fileszs.get(node))[0]
        else:
            return list(self.fileszs.get(node))[0] + sum(self._sizer(child) for child in self.diridx.get(node))

    def sizer(self):
        # Get totals within directories
        for dir, contents in self.fileidx.items():
            totsz = 0
            for file in contents:
                totsz += int(re.match(r'^(\d+)', file).group(1))
            self.fileszs[dir].add(totsz)
        
        # Do this for all directories (nodes)
        for dir in self.fileszs.keys():
            self.dirszs[dir].add(self._sizer(dir))




# Run through the commands to image the file system
fs = FileSys()
i = 0
while i < len(log):
    line = log[i]
    # print(f'Logging: {line} (i={i})')
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
    

# Run the sizer
fs.sizer()

# Pt 1 answer
print(sum(list(v)[0] for v in fs.dirszs.values() if list(v)[0] < 100000))

