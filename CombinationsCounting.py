#input
# 8
# 62 53
# 96 7
# 104 97
# 90 7
# 109 7
# 103 7
# 75 8
# 113 7

def factorial(n):
  if n <= 1:
    return 1
  else:
    return n * factorial(n-1)

def c(n, k):
  result = factorial(n) / (factorial(k) * factorial(n - k))
  return int(result)

n = int(input())
for i in range(0, n):
  (n, k) = (int(x) for x in input().split())
  comb = c(n, k)
  print(comb, "", end="")