# Folding paper
from sys import argv
from typing import Set, Tuple

with open(argv[1], 'r') as f:
  dots, folds = f.read().split('\n\n')
  dots = list(map(lambda x: x.split(','), dots.strip().split('\n')))
  paper = set()
  max_x = 0
  max_y = 0
  for [dot_x, dot_y] in dots:
    paper.add((int(dot_x), int(dot_y)))
    max_x = max(int(dot_x), max_x)
    max_y = max(int(dot_y), max_y)
  instructions = list(map(lambda x: x[11:].split('='), folds.strip().split('\n')))

def perform_fold(mode: str, degree: int, paper: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
  # For each fold, a point a (x, y) will either:
  # A -- be unchanged if it's in the fold boundary
  # B -- have a coordinate (x, y) transformed to (x, degree - (y - degree)) or (degree - (x - degree), y)
  # C -- be discarded if it's on the fold-line.
  folded_paper = set()
  for dot in paper:
    fold_x, fold_y = dot
    if mode == 'x':
      if fold_x == degree:
        continue
      if fold_x > degree:
        fold_x = degree - (fold_x - degree)
    if mode == 'y':
      if fold_y == degree:
        continue
      if fold_y > degree:
        fold_y = degree - (fold_y - degree)
    folded_paper.add((fold_x, fold_y))
  return folded_paper

move1_mode, move1_degree = instructions[0]
print('Part 1', len(perform_fold(move1_mode, int(move1_degree), paper)), 'dots')

# Part 2
def display_points(points: Set[Tuple[int, int]]) -> None:
  rows = 0
  cols = 0
  for (x, y) in points:
    cols = max(cols, x)
    rows = max(rows, y)
  board = [[' ' for _ in range(cols+1)] for __ in range(rows+1)]
  for (x, y) in points:
    board[y][x] = '#'
  for row in board:
    print(''.join(row))

for [mode, degree] in instructions:
  paper = perform_fold(mode, int(degree), paper)
print('Part 2')
display_points(paper)
