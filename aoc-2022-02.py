
from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=2)


rnds = puzzle.input_data.splitlines()

pts = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
wins = ('C X', 'A Y', 'B Z')
drws = ('A X', 'B Y', 'C Z')


def scorer(rnds):
    score = 0
    for rnd in rnds:
        if rnd in wins or (len(rnd) > 3 and rnd[4] == 'Z'):
            score += 6
        elif rnd in drws or (len(rnd) > 3 and rnd[4] == 'Y'):
            score += 3
        score += pts.get(rnd[2])
    return(score)

# Pt 1
print(scorer(rnds))

# Pt 2
towin = {'A': 'B', 'B': 'C', 'C': 'A'}
tolse = {'A': 'C', 'B': 'A', 'C': 'B'}

newscore = 0
for rnd in rnds:
    if rnd[2] == 'Z':
        p = towin.get(rnd[0])
    elif rnd[2] == 'Y':
        p = rnd[0]
    else:
        p = tolse.get(rnd[0])
    newrnd = f'{rnd[0]} {p} {rnd[2]}'
    newscore += scorer([newrnd])

print(newscore)