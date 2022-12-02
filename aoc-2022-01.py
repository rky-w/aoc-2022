
from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=1)
puzzle_data = [int(val) for val in puzzle.input_data.splitlines()]