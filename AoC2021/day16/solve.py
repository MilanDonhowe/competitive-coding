# BITS Packet Decoding

from os import read
from sys import argv
from math import log2
from functools import reduce

with open(argv[1], 'r') as f:
  stream = f.read().strip()

# 1. decode hex into continuous string of 1s and 0s
stream = list(map(lambda d: bin(int(d, 16))[2:], list(stream)))
stream = list(map(lambda b: '0'*(4-len(b))+b, stream))
stream = ''.join(stream)

class Packet():
  def __init__(self, version=None, type_id=None, length_type_id=None, length=0, literal=None, bit_size=0):
    # standard header
    self.type_id = type_id
    self.version = version
    # operator specific headers
    self.length_type_id = length_type_id
    self.length = length
    self.packets = [] # sub packets
    # literal specific
    self.literal = literal
    # all packets
    self.bit_size = bit_size # = to total bit size or just header size w/o children
  
  # Size of this packet & its sub packets
  def get_bit_size(self):
    if (self.literal != None):
      return self.bit_size
    return self.bit_size + sum([s.get_bit_size() for s in self.packets])

  def add_literal(self, literal, version, type_id):
    self.literals.append((literal, version, type_id))

  def add_packet(self, packet):
    self.packets.append(packet)

  # are we done reading our child packets?
  def done(self):
    # if type_id is 1, length references number of child-packets
    if self.length_type_id == '1':
      if len(self.packets) < self.length:
        return False
    if self.length_type_id == '0':
      if sum([s.get_bit_size() for s in self.packets]) < self.length:
        return False
    return True


def init_decoder(stream:str):
  decode_ptr = 0
  def read(n: int) -> str:
    nonlocal decode_ptr
    if (decode_ptr+n > len(stream)):
      raise IndexError(f'bruh what the heck, decoder freeze @ {decode_ptr+n} >= {len(stream)}')
    val = stream[decode_ptr:decode_ptr+n]
    decode_ptr += n
    return val
  def peek() -> str:
    return stream[decode_ptr]
  return read, peek

def decode_packets(stream: str):
  read_stream, peek_stream = init_decoder(stream)
  parentPacket = Packet(length_type_id='1', length=1, version='0')
  packet_stk = [parentPacket]

  while len(packet_stk) != 0:
    curr_packet = packet_stk.pop()    
    # no more reading to do
    if (curr_packet.done()):
      continue
    # otherwise, push this packet back onto the stack
    # for future completion
    packet_stk.append(curr_packet)

    # Now let's parse the next packet in stream
    new_packet = Packet()
    # read standard header
    new_packet.version = read_stream(3)
    new_packet.type_id = read_stream(3)

    # Literal specific (read bits)
    if new_packet.type_id == '100':
      # add literal type
      bits_read = 6
      literal = ''
      # read at least next 5 bits
      while peek_stream() != '0':
        bits_read += 5
        # discard leading bit
        literal += read_stream(5)[1:]
      # read final 5 bits
      literal += read_stream(5)[1:]
      bits_read += 5
      # discard padding zeros
      bit_check = (bits_read - 6) - ((bits_read - 6) // 5) # if not mulitple of 4, we have to kill padding bits 
      while (bit_check % 4 != 0):
        bits_read += 1
        bit_check += 1
        assert(read_stream(1) == '0')
      new_packet.bit_size = bits_read
      new_packet.literal = int(literal, 2)
      # finally add literal to parent packet
      curr_packet.add_packet(new_packet)
    # Operator packet parsing
    else:
      new_packet.bit_size = 7
      new_packet.length_type_id = read_stream(1)
      # num packets
      if (new_packet.length_type_id == '1'):
        new_packet.length = int(read_stream(11), 2)
        new_packet.bit_size += 11
      # num bits
      else:
        new_packet.length = int(read_stream(15), 2)
        new_packet.bit_size += 15
      # now add as a child to current packet
      curr_packet.add_packet(new_packet)
      # push to stack so we process this packet next
      packet_stk.append(new_packet)
  return parentPacket

# Part 1, parse the packet stream
root = decode_packets(stream)

# sanity check / debug function
def printTree(pckt):
  print(f"HEADER: Type: {pckt.type_id}, Version: {int(pckt.version, 2)}, LENGTH_TYPE: {pckt.length_type_id}")
  if pckt.literal != None:
    print(f"Literal Value: {pckt.literal}")
  for child in pckt.packets:
    printTree(child)

def versionSum(pckt):
  if len(pckt.packets) == 0:
    return int(pckt.version, 2)
  intermediate = sum([versionSum(child) for child in pckt.packets])
  return intermediate + int(pckt.version, 2)

print("Part 1", versionSum(root))

# part 2: evaluate

def evaluateTree(node):
  if (type(node) == int):
    return node
  if node.type_id == '100':
    return node.literal
  # sum
  elif node.type_id == '000':
    return sum([evaluateTree(p) for p in node.packets])
  # product
  elif node.type_id == '001':
    if len(node.packets) == 1:
      return evaluateTree(node.packets[0])
    return reduce(lambda a,b: evaluateTree(a)*evaluateTree(b), node.packets)
  # min
  elif node.type_id == '010':
    return min([evaluateTree(p) for p in node.packets])
  # max
  elif node.type_id == '011':
    return max([evaluateTree(p) for p in node.packets])
  # greater than
  elif node.type_id == '101':
    return 1 if evaluateTree(node.packets[0]) > evaluateTree(node.packets[1]) else 0
  # less than
  elif node.type_id == '110':
    return 1 if evaluateTree(node.packets[0]) < evaluateTree(node.packets[1]) else 0
  # equal to
  elif node.type_id == '111':
    return 1 if evaluateTree(node.packets[0]) == evaluateTree(node.packets[1]) else 0
  else:
    raise ValueError(f'Invalid Type Id: \"{node.type_id}\"')

# unpack my parent packet I added in my decoder function
root = root.packets[0]
print("Part 2", evaluateTree(root))