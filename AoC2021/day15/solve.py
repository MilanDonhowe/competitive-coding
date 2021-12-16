# Optimal path in 2D maze
from sys import argv
from typing import Tuple, List
from math import floor

with open(argv[1], 'r') as f:
  grid = list(map(lambda ln: list(map(int, list(ln))), f.read().strip().split('\n')))

# Assuming square input
assert(len(grid) == len(grid[0]))
GRID_SIZE = len(grid)

# helpful functions
def inbounds(x: int, y: int) -> bool:
  return -1 < x < GRID_SIZE and -1 < y < GRID_SIZE

def gen_neighbors(pos: Tuple[int, int]) -> List[Tuple[int, int]]:
  x, y = pos
  return [(x+dx,y+dy) for (dx, dy) in [(1,0), (0,1), (-1,0), (0,-1)] if inbounds(x+dx, y+dy)]

# Just Dijkstra's algorithm with a min-heap.

class MinHeap:
  """Min Heap, top element always smallest"""
  def __init__(self):
    self.heap = []

  def add(self, val, weight):
    self.heap.append((val, weight))
    self.organize()
  
  def pop(self):
    #print(self.heap)
    #input()
    # edge case when heap has 1 item
    if len(self.heap) == 1:
      return self.heap.pop()

    # heap organization rules
    val = self.heap[0]
    self.heap[0] = self.heap[-1]
    self.heap = self.heap[:-1]  
    self.organize()

    return val

  def largest_child_index(self, index):
    candidates = []
    if (index*2 + 1 < len(self.heap)):
      candidates.append(index*2 + 1)
    if (index*2 + 2 < len(self.heap)):
      candidates.append(index*2 + 2)
    
    max_index = sorted(candidates, key=lambda ind: self.heap[ind][1])
    if len(max_index) == 0:
      return -1
    return max_index[0]
  
  def organize(self):
    node = 0
    child_index = self.largest_child_index(node)
    if (child_index == -1): return

    while self.heap[node][1] > self.heap[child_index][1]:
      # swap child & parent
      self.heap[node], self.heap[child_index] = self.heap[child_index], self.heap[node]
      node = child_index
      child_index = self.largest_child_index(node)
      if (child_index == -1):
        break

TABLE = {}
for y in range(0, GRID_SIZE):
  for x in range(0, GRID_SIZE):
    TABLE[(x,y)] = float('inf')
TABLE[(0,0)] = 0
UN_QUEUED = set(TABLE.keys()) - {(0,0)}

Q = MinHeap()
# Add edge & it's current weight :D (why did I have to write a heap for this???)
Q.add((0,0), 0)

while len(Q.heap) > 0:
  # Grab lowest unvisited node
  node, _weight = Q.pop()
  # Check each edge of this node
  neighbors = gen_neighbors(node)

  for (nx, ny) in neighbors:
    # update lower edges
    if TABLE[node] + grid[ny][nx] < TABLE[(nx,ny)]:
      TABLE[(nx,ny)] = TABLE[node] + grid[ny][nx]
    # add neighbor to bucket Q
    if (nx,ny) in UN_QUEUED:
      UN_QUEUED.remove((nx,ny))
      Q.add((nx,ny), TABLE[(nx,ny)])

print("Part 1", TABLE[(GRID_SIZE-1, GRID_SIZE-1)])

# Part 2:


def inbounds_p2(x: int, y: int) -> bool:
  return -1 < x < GRID_SIZE*5 and -1 < y < GRID_SIZE*5

def gen_neighbors_p2(pos: Tuple[int, int]) -> List[Tuple[int, int]]:
  x, y = pos
  return [(x+dx,y+dy) for (dx, dy) in [(1,0), (0,1), (-1,0), (0,-1)] if inbounds_p2(x+dx, y+dy)]

# Ok, expanding the entire graph is going to take up too much memory, let's fake it.
def weight(x, y):
  if (inbounds(x,y)):
    return grid[y][x]
  adjusted = (grid[y % GRID_SIZE][x % GRID_SIZE] + floor(x / GRID_SIZE) + floor(y / GRID_SIZE))
  if adjusted > 9:
    return (adjusted % 10) + 1
  return adjusted

# Now just copy-paste part 1 with some minor changes
TABLE = {}
for y in range(0, GRID_SIZE*5):
  for x in range(0, GRID_SIZE*5):
    TABLE[(x,y)] = float('inf')
TABLE[(0,0)] = 0
UN_QUEUED = set(TABLE.keys()) - {(0,0)}

Q = MinHeap()
# Add edge & it's current weight :D (why did I have to write a heap for this???)
Q.add((0,0), 0)

while len(Q.heap) > 0:
  # Grab lowest unvisited node
  node, _weight = Q.pop()
  # Check each edge of this node
  neighbors = gen_neighbors_p2(node)

  for (nx, ny) in neighbors:
    # update lower edges
    if TABLE[node] + weight(nx, ny) < TABLE[(nx,ny)]:
      TABLE[(nx,ny)] = TABLE[node] + weight(nx, ny)
    # add neighbor to bucket Q
    if (nx,ny) in UN_QUEUED:
      UN_QUEUED.remove((nx,ny))
      Q.add((nx,ny), TABLE[(nx,ny)])

print("Part 2", TABLE[(GRID_SIZE*5-1, GRID_SIZE*5-1)])