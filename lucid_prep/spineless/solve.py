from collections import OrderedDict

class Record(object):
  def __init__(self):
    self.y = 0
    self.n = 0
    self.a = 0
  def add(self, code):
    if code == 'yes':
      self.y += 1
    elif code == 'no':
      self.n +=1
    elif code == 'unsure':
      self.a += 1

  def vote(self):
    #print(f"y:{self.y}, n:{self.n}, a:{self.a}")
    self.n *= 2
    if self.n > self.y:
      return 'no'
    if self.y > self.n:
      return 'yes'
    return 'abstain'

with open("test2.txt") as f:
  content = f.read().split('\n')

# Alright, let's store the issues as tuples
# (yes, no, abstain)
record = OrderedDict()
total_polls = int(content[0])

for issue in content[1:total_polls+1]:
  record[issue] = Record()

for vote in content[2 + total_polls:]:
  if (len(vote.split(' ')) < 2): continue
  issue, choice = vote.split(' ')
  record[issue].add(choice)

for issue in record.keys():
  print(f'{issue} {record[issue].vote()}')