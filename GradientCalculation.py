#input
# 13 0.3 0.7 6
# 0.1 0.3
# -0.9 -0.4
# -0.4 0.1
# 0.4 -0.6
# 0.3 0.8
# 0.9 0.6
# -0.8 -0.4
# 0.7 -1
# 0.1 -0.7
# -1 -0.6
# 0.4 0.3
# 0.7 -0.9
# 0.7 -0.5

import math

def f(x,y, a,b,c):
  result = (x - a)**2 + (y - b)**2 + c * math.exp(-(x + a)**2 - (y + b)**2)
  return result

def g(x,y,dt, a,b,c):
  x0 = (f(x+dt,y, a,b,c) - f(x,y, a,b,c)) / dt
  y0 = (f(x, y+dt, a,b,c) - f(x,y, a,b,c)) / dt
  return [x0, y0]

def raising_direction(x,y):
  return round(math.degrees(math.atan2(y, x)))

def descent_direction(x,y):
  return 180 + round(math.degrees(math.atan2(y, x)))

inp = input().split()
n = int(inp[0])
(a, b, c) = (float(x) for x in inp[1:])

for i in range(0, n):
  (x, y) = (float(x) for x in input().split())
  gradient = g(x,y,1e-9,a,b,c)
  slope = descent_direction(gradient[0], gradient[1])

  print(slope, "", end="")