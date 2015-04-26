#input
# 15
# 2 4 3 6 7 9 1 5 8
# 9 3 7 8 6 1 5 2 4
# 1 4 9 5 6 3 2 8 7
# 1 6 8 3 4 2 9 7 5
# 7 4 6 5 1 9 3 8 2
# 8 1 7 5 6 3 9 2 4
# 2 4 3 9 7 8 5 1 6
# 6 3 1 9 2 7 4 5 8
# 1 4 7 6 8 9 5 3 2
# 7 9 1 8 5 6 3 2 4
# 1 3 9 6 8 2 5 7 4
# 8 5 4 6 3 7 2 1 9
# 7 2 4 5 8 1 9 3 6
# 5 2 6 1 8 4 9 3 7
# 4 8 5 3 2 6 1 7 9

class Game:
  board = []

  def initialize(self):
    self.board = []
    for i in range(0, 3):
      self.board.append([None, None, None])

  def mark(self, pos, p):
    self.board[pos // 3][pos % 3] = p

  def is_game_over(self):
    ##check rows
    for i in range(0, 3):
      if (self.board[i][0] == None):
        continue
      if (self.board[i][0] == self.board[i][1]
        and self.board[i][1] == self.board[i][2]):
        return True
    ##check columns
    for i in range(0, 3):
      if (self.board[0][i] == None):
        continue
      if (self.board[0][i] == self.board[1][i]
        and self.board[1][i] == self.board[2][i]):
        return True
    ##check diagonals
    if self.board[1][1] == None:
      return False
    if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
      return True
    if self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2]:
      return True
    return False

game = Game()

n = int(input())

for i in range(0, n):
  game.initialize()
  moves = [int(x) for x in input().split()]

  for j in range(0, len(moves)):
    player = None
    if j % 2 == 0:
      player = 'x'
    else:
      player = 'o'

    game.mark(moves[j] - 1, player)
    if game.is_game_over():
      print(str(j+1), "", end="")
      break
    if j == len(moves) - 1:
      print(0, "", end="")