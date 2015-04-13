#input
# 41 4

def f(n, k):
  if n == 1:
    return 1
  return ((f(n-1, k)+k-1) % n) + 1

(n, k) = (int(x) for x in input().split())
survivor = f(n, k)
print(survivor)