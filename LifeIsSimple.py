#input
# X------
# XXXX---
# XX--XX-
# X--XXXX
# -X--X-X

def print_grid(grid):
  for r in grid:
    for c in r:
      if c == 0:
        print('-',end="")
      if c == 1:
        print('X', end="")
    print()

def num_of_neighbors(grid, i, j):
  num = 0
  imin = i - 1 if i > 0 else i
  imax = i + 1 if i < len(grid) - 1 else i
  jmin = j - 1 if j > 0 else j
  jmax = j + 1 if j < len(grid) - 1 else j
  for k in range(imin, imax+1):
    for l in range(jmin, jmax+1):
      if k == i and l == j:
        continue
      num += grid[k][l]
  return num

def next_step(grid):
  dead = []
  born = []
  alive = 0
  for i in range(0, len(grid)):
    for j in range(0, len(grid[0])):
      if grid[i][j] == 0:
        if num_of_neighbors(grid, i, j) == 3:
          born.append([i,j])
      if grid[i][j] == 1:
        alive += 1
        neigh = num_of_neighbors(grid, i, j)
        if neigh < 2 or neigh > 3:
          dead.append([i,j])
  for x in dead:
    grid[x[0]][x[1]] = 0
  for y in born:
    grid[y[0]][y[1]] = 1
  alive = alive - len(dead) + len(born)
  return alive

grid = [([0 for x in range(20)]) for y in range(20)]

for i in range(len(grid)//4, len(grid)//4 + 5):
  row = input()
  for j in range(0, 7):
    if row[j] == '-':
      continue
    elif row[j] == 'X':
      grid[i][j+len(grid)//4] = 1

for i in range(0, 5):
  alive = next_step(grid)
  print(alive, '', end='')