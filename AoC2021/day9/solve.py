# Lava-cave!
from sys import argv
from collections import deque

with open(argv[1], 'r') as f:
  lavacave = [list(map(int, ls)) for ls in (map(list, f.read().strip().split('\n')))]

def inbounds(x: int, y: int) -> bool:
  return x >= 0 and y >= 0 and y < len(lavacave) and x < len(lavacave[0]) 

risk_level = 0
basins = {}
# Find "low points" defined as points lower than all adjacent points on the map.
for y, row in enumerate(lavacave):
  for x, height in enumerate(row):
    neighbors = [lavacave[y+dy][x+dx] for (dx, dy) in [(-1, 0), (1, 0), (0, 1), (0, -1)] if inbounds(x+dx, y+dy)]
    if height < min(neighbors):
      risk_level += (height + 1)
      basins[(x,y)] = 1 # Keep track of basins for part 2
print("Part 1", risk_level)

# Part 2: Find largest basin!
def model(x, y):
  # Just a BFS until we hit 9 or out-of-bounds
  traversed = set()
  basin_key = (x,y)
  queue = deque([(x,y)])
  while len(queue) > 0:
    x, y = queue.popleft()
    neighbors = [(x+dx, y+dy) for (dx, dy) in [(-1, 0), (1, 0), (0, 1), (0, -1)] if inbounds(x+dx, y+dy) and (x+dx, y+dy) not in traversed]
    for neighbor in neighbors:
      if (lavacave[neighbor[1]][neighbor[0]] != 9):
        queue.append(neighbor)
    traversed.add((x,y))
  basins[basin_key] = len(traversed)

for pit_x, pit_y in basins:
  model(pit_x, pit_y)
product = 1
for i in sorted(basins.values(), reverse=True)[:3]:
  product *= i
print("Part 2", product)
