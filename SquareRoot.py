#input
# 10
# 98 6
# 5476 10
# 18 12
# 21 9
# 41 11
# 77463 6
# 803 13
# 277 3
# 91029 7
# 149 11

n = int(input())

for i in range(0, n):
  (v, steps) = (int(x) for x in input().split())

  r = 1
  for j in range(0, steps):
    d = v / r
    r = (r + d) / 2

  print(r, "", end="")