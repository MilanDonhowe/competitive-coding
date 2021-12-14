# Day 14 - Polymers
from sys import argv
from collections import Counter
from copy import deepcopy

with open(argv[1], 'r') as f:
  problem = f.read().split('\n\n')
  template = problem[0]

# Parse recipes
recipes = {}
for [pair, product] in list(map(lambda x: x.split(' -> '), problem[1].strip().split('\n'))):
  recipes[pair] = product

def step(prev_polymer: str) -> str:
  next_polymer = ''
  for i in range(1, len(prev_polymer)):
    next_polymer += prev_polymer[i-1]
    next_polymer += recipes[ prev_polymer[i-1] + prev_polymer[i] ]
  next_polymer += prev_polymer[-1]
  return next_polymer

# Part 1
polymer = template
for _ in range(10):
  polymer = step(polymer)
element_frequency = Counter(polymer).most_common()
print("Part 1", element_frequency[0][1] - element_frequency[-1][1])

# Part 2 - Keep track of polymers, not elements (call back to fish problem)

polymers = []
for i in range(1, len(template)):
  polymers.append(template[i-1] + template[i])
polymers = Counter(polymers)

# keep track of frequencies separately (since polymers alone will double count characters) 
element_frequency = Counter(list(template))

def fast_step(prev_polymers: Counter[str]) -> Counter[str]:
  next_polymers = Counter()
  for polymer in prev_polymers:
    # update number of new polymers
    next_polymers[polymer[0]+recipes[polymer]] += prev_polymers[polymer]
    next_polymers[recipes[polymer]+polymer[1]] += prev_polymers[polymer]
    # update frequencies
    element_frequency[recipes[polymer]] += prev_polymers[polymer]
  return next_polymers

for _ in range(40):
  polymers = fast_step(polymers)

element_frequency = element_frequency.most_common()
print("Part 2", element_frequency[0][1] - element_frequency[-1][1])

