# Crab-based optimization problem
from sys import argv
from collections import Counter
from typing import Tuple

with open(argv[1], 'r') as f:
  crabs = Counter(map(int, f.read().split(',')))
  max_pos = max(crabs)
  crabs = crabs.items()

# At pos = 0 the cost to get to zero is its position
minimal_cost = sum(map(lambda c: c[0]*c[1], crabs))

def cost(crab_tuple: Tuple[int, int], destination: int) -> int:
  origin, n = crab_tuple
  return abs(destination - origin) * n

for pos in range(1, max_pos+1):
  minimal_cost = min(sum(map(lambda c: cost(c, pos), crabs)), minimal_cost)
print("Part 1", minimal_cost)

def inc_cost(crab_tuple: Tuple[int, int], destination: int) -> int:
  origin, num_crab = crab_tuple
  n = abs(destination - origin)
  return ((n*(n+1)) // 2) * num_crab

minimal_cost = sum(map(lambda c: inc_cost(c, 0), crabs))
for pos in range(1, max_pos+1):
  minimal_cost = min(sum(map(lambda c: inc_cost(c, pos), crabs)), minimal_cost)
print("Part 2", minimal_cost)
