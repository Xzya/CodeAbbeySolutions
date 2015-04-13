#input
# 16
# 123 94 6844693
# 954 1034 622102
# 18888535 14158234 45
# 910 462 884898
# 1134 754 755491
# 15420868 6491059 59
# 74720421 45500476 7
# 49 50 12942362
# 6 10 46972114
# 13107511 25187015 9
# 891438 995706 969
# 6 8 66911072
# 47 60 2300029
# 27406390 15311746 19
# 139170 96954 4379
# 2381028 37964645 26

import math

lines = int(input())

for i in range(0, lines):
  (x,y,n) = (int(x) for x in input().split())

  a1 = math.ceil((y * n) / (x + y))
  a2 = math.floor((y * n) / (x + y))

  b1 = math.ceil((x * n) / (x + y))
  b2 = math.floor((x * n) / (x + y))

  a = [a1, a2]
  b = [b1, b2]

  times = []

  for j in a:
    for k in b:
      tx = (x * j)
      ty = (y * k)
      if (j + k >= n):
        times.append(max(tx,ty))

  print(min(times), "", end="")