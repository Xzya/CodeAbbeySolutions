#input
# 8
# 25 11 41
# 16 12 76
# 24 8 83
# 13 1 60
# 24 10 41
# 5 13 89
# 15 18 17
# 15 3 57

n = int(input())

for i in range(0, n):
  (a, b, k) = (int(x) for x in input().split())
  result = 0
  for j in range(0, k):
    result += a + (j * b)
  print(result, "", end="")