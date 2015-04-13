#input
# 20
# 425 1020 1171
# 984 287 1025
# 264 77 275
# 840 350 910
# 435 232 493
# 1320 704 1496
# 320 240 400
# 329 1128 1208
# 295 708 821
# 240 450 564
# 915 488 1121
# 364 273 490
# 427 1464 1525
# 112 210 236
# 1176 343 1183
# 204 153 284
# 75 100 125
# 60 25 64
# 1176 343 1234
# 276 368 471

import math

n = int(input())

angles = []
for i in range(0, n):
  (a, b, c) = (int(x) for x in input().split())
  pyth = math.sqrt(a**2 + b**2)

  angle = None
  if pyth == c:
    angle = 'R'
  elif pyth > c:
    angle = 'A'
  elif pyth < c:
    angle = 'O'
  angles.append(angle)

print(' '.join(angles))