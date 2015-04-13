#input
# 16
# 2 5
# 2 7 9 14 18
# 2 4 8 13 17 20
# 5 10 15 19 22 25
# 5 7 9 13 15
# 2 4 9 13 18
# 3 8 11 14
# 3 6 8 12 17
# 2 7 9 11
# 3 6 8 11 15
# 1 5 10
# 5 10 12 16
# 3 7
# 5 7 9 11
# 3 5 9
# 5 10 15 18 21 24

n = int(input())

for i in range(0, n):
  a = [int(x) for x in input().split()]

  result = 0
  for k in range(0, len(a)):
    result += a[k] **2

  print(result, "", end="")