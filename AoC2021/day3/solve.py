# Day 3

with open('input', 'r') as f:
  codes = f.read().split('\n')[:-1]

# epsilon rate is inverse (NOT op) of gamma rate
counts = [{'1': 0, '0':0} for _ in range(len(codes[0]))]

for code in codes:
  for pos, bit in enumerate(code):
    counts[pos][bit] += 1

gamma_str = ''.join(['1' if count['1'] > count['0'] else '0' for count in counts])
gamma = int(gamma_str, 2)
bitmask = int(''.join(['1' for _ in codes[0]]), 2)
epsilon = ~gamma & bitmask # bitmask to account for 2s complement (python doesn't believe in unsigned ints)
print("part 1 (power consumption)", gamma * epsilon)


# part 2 

# get oxygen
oxygen = codes
for pos in range(0, len(codes[0])):

  one_count = 0
  for i in range(0, len(oxygen)):
    one_count += int(oxygen[i][pos])
  
  criteria_bit = '1' if one_count >= (len(oxygen)-one_count) else '0'

  oxygen = list(filter(lambda o: o[pos] == criteria_bit, oxygen))

  if len(oxygen) == 1:
    break

# get carbon
carbon = codes
for pos in range(0, len(codes[0])):

  one_count = 0
  for i in range(0, len(carbon)):
    one_count += int(carbon[i][pos])
  
  criteria_bit = '0' if one_count >= (len(carbon)-one_count) else '1'

  carbon = list(filter(lambda o: o[pos] == criteria_bit, carbon))

  if len(carbon) == 1:
    break

print('part 2 (life support rating)', int(oxygen[0],2) * int(carbon[0],2))