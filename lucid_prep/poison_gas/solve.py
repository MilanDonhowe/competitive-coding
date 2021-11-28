
with open("test", "r") as f:
  problem_input = f.read().split('\n')

CaveData = problem_input[1:]

# Algo:
# Iterate horizontall across cave, each time we hit a second wall, reset accumulator
# and add to sum

total_gas = 0

