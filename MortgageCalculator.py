##input
# 3800000 5 108
##answer
# 43766

def binary_search(P, R, L, xmin, xmax):
  if xmax <= xmin:
    return None

  x = (xmax + xmin) / 2

  newP = P
  for i in range(0, L):
    temp = (x - (newP * (R/12/100)))
    newP -= temp

  if newP < -1e-7:
    return binary_search(P, R, L, xmin, x)
  elif newP > 1e-7:
    return binary_search(P, R, L, x, xmax)
  else:
    return x

def main():
  (P, R, L) = (int(x) for x in input().split())

  M = binary_search(P, R, L, 0, P/2)
  print(round(M))

if __name__ == '__main__':
    main()
