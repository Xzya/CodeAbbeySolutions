#input
# 17
# 9 72 468
# 6 48 150
# 5 0 -45
# 5 20 -25
# 1 6 90
# 3 -6 246
# 2 -12 50
# 2 24 80
# 9 -54 45
# 1 -10 61
# 8 112 520
# 7 -126 1015
# 9 -36 72
# 7 -140 1267
# 2 18 36
# 2 0 2
# 1 -4 5

def find_roots(a,b,c):
  x1 = (-b + (b**2 - 4 * a * c)**.5) / (2 * a)
  x2 = (-b - (b**2 - 4 * a * c)**.5) / (2 * a)

  x1 = prettyfy(x1)
  x2 = prettyfy(x2)

  return (x1,x2)

def prettyfy(c):
  c = complex(c)
  a = int(round(c.real))
  b = c.imag
  if b == 0:
    return a
  else:
    if b < 0:
      num = str(a) + str(b) + 'j'
    else:
      num = str(a) + '+' + str(b) + 'j'
    return complex(num)

n = int(input())

for i in range(0, n):
  (a,b,c) = (int(x) for x in input().split())
  (x1, x2) = find_roots(a,b,c)

  if (i > 0):
    print('; ', end="")
  print(str(x1).strip(')').strip('(').replace('j','i'),str(x2).strip('(').strip(')').replace('j','i'), end="")