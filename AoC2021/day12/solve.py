# Graph path generating problem!

from sys import argv
from typing import Dict, Set
from collections import deque
from copy import deepcopy

with open(argv[1], 'r') as f:
  edges = list(map(lambda ln: ln.split('-'), f.read().strip().split('\n')))

graph = {}
for [a, b] in edges:
  if a not in graph:
    graph[a] = set([b])
  else:
    graph[a].add(b)
  if b not in graph:
    graph[b] = set([a])
  else:
    graph[b].add(a)

# Generate number of paths between start & end where small caves visited at most once
def paths(g: Dict[str, Set[str]]) -> int:
  def r_ways_to_end(node: str, prev_lower: Set[str]) -> int:
    # deep copy to avoid invalid references
    child_cache = deepcopy(prev_lower)
    # if node == end, we found 1 path!
    if (node == 'end'):
      return 1
    # Could we visit this node again?
    if node.islower():
      child_cache.add(node)
    # check # ways to end from this node
    total_ways = 0
    for neighbor in g[node]:
      if neighbor not in child_cache:
        total_ways += r_ways_to_end(neighbor, child_cache)
    return total_ways
  return r_ways_to_end('start', set())

print("Part 1", paths(graph))

# Part 1 rewritten iteratively to help me finish part 2
def paths_p1(g: Dict[str, Set[str]]) -> int:
  id = 0
  #( path so far, id ) 
  pathways = deque([(['start'], id)])
  caches = {id: set()}
  total_paths = 0
  while len(pathways) > 0:
    path, path_id = pathways.pop()
    # thraead exit condition
    if (path[-1] == 'end'):
      # print('->'.join(list(path))) # debug line
      total_paths += 1
      continue
    # check neighbors
    if (path[-1].islower()):
      caches[path_id].add(path[-1])
    for neighbor in g[path[-1]]:
      if neighbor not in caches[path_id]:
        # spawn new process
        id += 1
        pathways.append((path + [neighbor], id))
        caches[id] = deepcopy(caches[path_id])
  return total_paths


# Part 2--now we can visit 1 small cave twice

# I originally tried some recursive formulation, but quickly exceeded python's max recursion depth, so instead
# I tried to unwind the call-stack into an stack data-structure a-la some green-threading library. This is very
# inefficient and took about 10 seconds seconds on my machine to run, which isn't ideal, but it gets the job 
# done for this problem.
def paths_p2(g: Dict[str, Set[str]]) -> int:
  id = 0
  #( path so far, id ) 
  pathways = deque([(['start'], id)])
  caches = {id: {}}
  total_paths = 0
  while len(pathways) > 0:
    path, path_id = pathways.pop()
    # thraead exit condition
    if (path[-1] == 'end'):
      #print('->'.join(list(path))) # debug line, will print out all valid paths found
      total_paths += 1
      continue
    # keep track if we've seen this node before
    if (path[-1].islower()):
      if path[-1] not in caches[path_id]:
        caches[path_id][path[-1]] = 1
      else:
        caches[path_id][path[-1]] += 1
    # check neighbors
    for neighbor in g[path[-1]]:
      if neighbor not in caches[path_id]:
        # spawn new process
        id += 1
        pathways.append((path + [neighbor], id))
        caches[id] = deepcopy(caches[path_id])
      # Make sure to not visit start twice, it will generate invalid paths!
      elif max(caches[path_id].values()) < 2 and neighbor != 'start':
        id += 1
        pathways.append((path + [neighbor], id))
        caches[id] = deepcopy(caches[path_id])

  return total_paths
        

print("Part 2", paths_p2(graph))