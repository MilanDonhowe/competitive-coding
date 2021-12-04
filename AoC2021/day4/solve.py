# Day 4: Bingo! 

with open('input', 'r') as f:
  problem = f.readlines()

marked_numbers = list(map(int, problem[0].strip().split(',')))

# determines if board wins for a set of called numbers 
def doesBoardWin(board, num_set):
  truth_board = [[False for _ in range(len(board))] for _ in range(len(board))]
  for row in range(len(board)):
    for col in range(len(board)):
      if board[row][col] in num_set:
        truth_board[row][col] = True  
  # shout out to https://stackoverflow.com/a/34386518/8638218 for matrix transpose 1 liner
  if (any([all(row) for row in truth_board]) or any([all(col) for col in zip(*truth_board)])):
    # return sum of unmarked nums
    unmarked_sum = 0
    for row in range(len(board)):
      for col in range(len(board)):
        if truth_board[row][col] == False:
          unmarked_sum += board[row][col]
    return unmarked_sum
  return 0

# parse out boards
boards = [[]]

for ln in problem[2:]:
  if ln == '\n':
    boards.append([])
    continue
  boards[-1].append(list(map(int, filter(lambda x: len(x.strip()) > 0, ln.strip().split(' ')))))

def part1():
  called_marked_numbers = set()
  for num in marked_numbers:
    called_marked_numbers.add(num)
    for board in boards:
      if (unmarked_sum := doesBoardWin(board, called_marked_numbers)) > 0:
        print(num, unmarked_sum)
        return num * unmarked_sum
  return 'ERROR'
print("Part 1", part1())

# Part 2 - find last winning board
def part2(b):
  called_marked_numbers = set()
  boards = b
  last_winning_board = None
  for num in marked_numbers:
    called_marked_numbers.add(num)
    losers = []
    for bd in boards:
      if doesBoardWin(bd, called_marked_numbers) == 0:
        losers.append(bd)
      else:
        last_winning_board = (doesBoardWin(bd, called_marked_numbers) , num)
    boards = losers
    if len(boards) == 0:
      break
  return last_winning_board[0] * last_winning_board[1]
print("Part 2", part2(boards))