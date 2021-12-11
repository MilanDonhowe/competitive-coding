# More simulations!!! 🐙🐙🐙🐙
from sys import argv
from typing import List, Tuple

with open(argv[1], 'r') as f:
  init_state = list(map(lambda l: list(map(int, list(l))), f.read().strip().split('\n')))

def in_bounds(x: int, y: int) -> bool:
  return x >= 0 and x < len(init_state[0]) and y >= 0 and y < len(init_state)

def get_neighbors(x: int, y: int) -> List[Tuple[int,int]]:
  return [(x+dx,y+dy) for (dx,dy) in [(1,0), (-1,0), (1,1), (-1,1), (0,1), (0,-1), (1,-1), (-1,-1)] if in_bounds(x+dx, y+dy)]

# move state from one step to the next
def simulate(prev_state: List[List[int]]) -> Tuple[List[List[int]], int]:
  next_state = prev_state
  # first initially increment each octopus's energy level
  flashing_octopuses = []
  # keep flashed octopi in a set so we don't have an octopi flash twice per step
  flashed_octopi = set()
  for y, line in enumerate(next_state):
    for x in range(len(line)):
      next_state[y][x] += 1
      if next_state[y][x] > 9:
        next_state[y][x] = 0
        flashing_octopuses.append((x,y))
        flashed_octopi.add((x,y))

  # Now handle each flash
  while len(flashing_octopuses) > 0:
    x, y = flashing_octopuses.pop()
    # Increase neighbors values
    for (nx, ny) in get_neighbors(x, y):
      if (nx, ny) not in flashed_octopi:
        next_state[ny][nx] += 1
        # if neighbor > 9 now, then it will also flash
        if (next_state[ny][nx] > 9):
          next_state[ny][nx] = 0
          flashing_octopuses.append((nx,ny))
          flashed_octopi.add((nx,ny))
  
  return (next_state, len(flashed_octopi))

# Part 1
flashes = 0
current_state = init_state 
for _ in range(1, 101):
  current_state, step_flashes = simulate(current_state)
  flashes += step_flashes
print("Part 1", flashes)

# ok, just keep flashing until step_flashes == the size of our input grid
steps = 100
while True:
  steps += 1
  current_state, step_flashes = simulate(current_state)
  if step_flashes == (len(init_state) * len(init_state[0])):
    break
print("Part 2", steps)