# Bracket-completion! 
from sys import argv

with open(argv[1], 'r') as f:
  chunks = f.read().strip().split('\n')

delim = {
  '(':')',
  '{':'}',
  '[':']',
  '<':'>'
}

points = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137
}

def corrupt(chk: str) -> int:
  stk = []
  for token in chk:
    if token in delim:
      stk.append(token)
    else:
      if delim[stk.pop()] != token:
        return points[token]
  return 0 # no corruption

incomplete = []
score = 0
for chunk in chunks:
  chunk_score = corrupt(chunk)
  # Push zero score to incomplete list for part 2
  if (chunk_score == 0): incomplete.append(chunk)
  score += chunk_score
print("Part 1", score)

# part 2, auto-complete
repair_points = {
  ')': 1,
  ']': 2,
  '}': 3,
  '>': 4
}

def repair(chk: str) -> int:
  stk = []
  for token in chk:
    if token in delim:
      stk.append(token)
    else: # ASSUMING CORRECT TOKEN
      stk.pop()
  # auto-complete
  ending = ''.join(list(map(lambda s: delim[s], stk))[::-1])
  assert(corrupt(chk + ending) == 0)
  # determine score
  score = 0
  for c in ending:
    score = (score*5) + repair_points[c]
  return score

scores = []
for chunk in incomplete:
  scores.append(repair(chunk))
print("Part 2", sorted(scores)[len(scores)//2])