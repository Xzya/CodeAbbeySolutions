#input
# 2 4 4 2
# 2 2 2 2
# 2 2 2 2
# 4 2 2 4
# R R R D L R U D U

class Tile:
  value = 0
  alreadyStacked = False
  def __init__(self, _value=0):
    self.value = _value

class Game:
  board = []

  def up(self):
    for i in range(0, 4):
      for j in range(0, 4):
        if self.board[i][j].value != 0:
          k = i
          while k > 0:
            tile = self.board[k][j]
            if self.board[k-1][j].value == 0:
              self.board[k-1][j] = tile
              self.board[k][j] = Tile()
            elif self.board[k-1][j].value == tile.value and not self.board[k-1][j].alreadyStacked and not self.board[k][j].alreadyStacked:
              self.board[k-1][j].value = tile.value * 2
              self.board[k-1][j].alreadyStacked = True
              self.board[k][j] = Tile()
            k -= 1
    self.resetStacks()

  def down(self):
    for i in range(3, -1, -1):
      for j in range(3, -1, -1):
        if self.board[i][j].value != 0:
          k = i
          while k < 3:
            tile = self.board[k][j]
            if self.board[k+1][j].value == 0:
              self.board[k+1][j] = tile
              self.board[k][j] = Tile()
            elif self.board[k+1][j].value == tile.value and not self.board[k+1][j].alreadyStacked and not self.board[k][j].alreadyStacked:
              self.board[k+1][j].value = tile.value * 2
              self.board[k+1][j].alreadyStacked = True
              self.board[k][j] = Tile()
            k += 1
    self.resetStacks()

  def right(self):
    for j in range(3, -1, -1):
      for i in range(3, -1, -1):
        if self.board[i][j].value != 0:
          k = j
          while k < 3:
            tile = self.board[i][k]
            if self.board[i][k+1].value == 0:
              self.board[i][k+1] = tile
              self.board[i][k] = Tile()
            elif self.board[i][k+1].value == tile.value and not self.board[i][k+1].alreadyStacked and not self.board[i][k].alreadyStacked:
              self.board[i][k+1].value = tile.value * 2
              self.board[i][k+1].alreadyStacked = True
              self.board[i][k] = Tile()
            k += 1
    self.resetStacks()

  def left(self):
    for j in range(0, 4):
      for i in range(0, 4):
        if self.board[i][j].value != 0:
          k = j
          while k > 0:
            tile = self.board[i][k]
            if self.board[i][k-1].value == 0:
              self.board[i][k-1] = tile
              self.board[i][k] = Tile()
            elif self.board[i][k-1].value == tile.value and not self.board[i][k-1].alreadyStacked and not self.board[i][k].alreadyStacked:
              self.board[i][k-1].value = tile.value * 2
              self.board[i][k-1].alreadyStacked = True
              self.board[i][k] = Tile()
            k -= 1
    self.resetStacks()

  def resetStacks(self):
    for i in self.board:
      for j in i:
        j.alreadyStacked = False

  def printBoard(self):
    for i in range(0, 4):
      for j in range(0, 4):
        print(self.board[i][j].value, "", end="")
      print()
    print()

  def countValues(self):
    values = {2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0, 512:0, 1024:0, 2048:0}
    for i in self.board:
      for j in i:
        if j.value in values:
          values[j.value] += 1
    sortedKeys = sorted(values.keys())

    for k in range(len(sortedKeys)-1, 0, -1):
      if values[sortedKeys[k]] == 0:
        del sortedKeys[k]
      else:
        break

    for k in range(0, len(sortedKeys)):
      print(values[sortedKeys[k]], "", end="")

  def solve(self):
    temp_board = []
    for i in range(0, 4):
      row = [Tile(int(x)) for x in input().split()]
      temp_board.append(row)
    self.board = temp_board

    instructions = input().split()
    for i in instructions:
      if i == 'U':
        self.up()
      elif i == 'D':
        self.down()
      elif i == 'R':
        self.right()
      elif i == 'L':
        self.left()

    self.countValues()

game = Game()
game.solve()