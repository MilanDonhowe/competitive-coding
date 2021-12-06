# Fish simulation
from collections import Counter
from sys import argv
with open(argv[1], 'r') as f:
  fishes = Counter(map(int, f.read().strip().split(',')))
state = [fishes[s] for s in range(9)]

def simulate(start_state: list[int], n: int) -> int:
  current_state = start_state
  for _ in range(n):
    new_state = [0 for __ in  range(9)]
    # Spawn new fish
    new_state[8] = current_state[0]
    # Age older child fish
    new_state[7] = current_state[8]
    # Move parent fish to timer = 6
    new_state[6] = current_state[0]
    # Also age children to adult
    new_state[6] += current_state[7]
    # age other fish
    for state_num in range(5, -1, -1):
      new_state[state_num] = current_state[state_num+1]
    # update state
    current_state = new_state
 
  return sum(current_state)

print('part 1:', simulate(state, 80))
print('part 2:', simulate(state, 256))