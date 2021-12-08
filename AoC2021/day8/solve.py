# Ok, LCD display fixer-upper
# my code is in absolute shambles

from sys import argv

with open(argv[1], 'r') as f:
  lcd_signals = list(map(lambda line: line.strip().split('|'), f.readlines()))

# Part 1: count occurences of 1, 4, 7 & 8
length_mapping = {
  1: 2,
  4: 4,
  7: 3,
  8: 7
}
occurences = 0
for signal in lcd_signals:
  for sequence in signal[1].split():
    if len(sequence) in length_mapping.values():
      occurences += 1
print("Part 1", occurences)

# standard signal --> digit codes
standard_mapping = {
  0: set('abcefg'),
  1: set('cf'),
  2: set('acdeg'),
  3: set('acdfg'),
  4: set('bcdf'),
  5: set('abdfg'),
  6: set('abdefg'),
  7: set('acf'),
  8: set('abcdefg'),
  9: set('abcdfg')
}
# Part 2: decode signals
running_sum = 0
for signal in lcd_signals:
  patterns = sorted(signal[0].split(), key=len)
  signal_mapping = dict()
  # Agonizing algorithm to get the proper signal references... there has to be a better way
  # but, this should ultimately get the correct result for any correct input unless my algebra sucks.
  cf = set(patterns[0])
  # Signal in 7's code but not the 1's code is the a segment signal
  signal_mapping['a'] = set(patterns[1]) - cf

  # signals aeg all in 8's code but not in 4's code  
  eg = (set(patterns[9]) - set(patterns[2])) - signal_mapping['a']
  # c appears in one of the 3 5-length codes with eg; f DOES NOT appear with eg in those codes
  for i in patterns[3:6]:
    if eg.issubset(set(i)):
      signal_mapping['f'] = cf - set(i)
      signal_mapping['c'] = cf - signal_mapping['f']
      # We also can get 'd' from this code since full matched pattern is "acdeg" 
      signal_mapping['d'] = (set(i) - (eg | signal_mapping['a'] | signal_mapping['c']))
  # Can now deduce 'b' from 4's code (bcdf)
  signal_mapping['b'] = set(patterns[2]) - (signal_mapping['d'] | cf)
  # Now we can deduce 'g' by using the either of the other 2 5-length signals again
  for i in patterns[3:6]:
    if not eg.issubset(set(i)):
      # either  (a, c, d, f, g) or (a, b, d, f, g)
      signal_mapping['g'] = set(i) - (signal_mapping['a']|signal_mapping['b']|cf|signal_mapping['d'])
      break
  # finally, we get mapping for e
  signal_mapping['e'] = set(patterns[-1]) - (signal_mapping['a']|cf|signal_mapping['g']|signal_mapping['b']|signal_mapping['d'])

  # translation_table, reverse the mapping for making decoding easier
  translation_table = {}
  for k, v in signal_mapping.items():
    translation_table[v.pop()] = k

  digits = ''
  for displayed_digit in signal[1].split():
    sig_set = set()
    for sig_char in displayed_digit:
      sig_set.add(translation_table[sig_char])
    for digit_mapping in standard_mapping.keys():
      if (standard_mapping[digit_mapping] == sig_set):
        digits += str(digit_mapping)
  # Sanity check -- caught bug
  assert(len(digits) == 4)
  running_sum += int(digits)

print("Part 2", running_sum)
