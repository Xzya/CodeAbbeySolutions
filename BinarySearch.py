#input
# 6
# 13.11996696 1.02371109 354.04676402 171.87087735
# 7.46092079 0.82115732 183.71069254 -96.13647324
# 4.63852531 1.53642674 1526.35053616 566.44112158
# 16.46624902 0.60180656 783.43162070 813.74420664
# 14.05264517 0.62539978 1590.12082852 -379.45243656
# 3.37169340 1.90896124 1623.24459926 -1321.75145304

import math

def binary_search(a, b, c, d, xmin, xmax):
  if xmax < xmin:
    return None

  x = (xmax + xmin) / 2

  result = check_result(a,b,c,d,x)

  if result > 0.00000001:
    return binary_search(a,b,c,d, xmin, x)
  elif result < -0.00000001:
    return binary_search(a,b,c,d, x, xmax)
  else:
    return x

def check_result(a, b, c, d, x):
  result = a * x + b * (x**3)**.5 - c * math.exp(-x/50) - d
  return result

def solve_equation(a,b,c,d):
  xmax = 100
  xmin = 0
  x = binary_search(a,b,c,d, xmin, xmax)
  return x

def main():
  n = int(input())
  for i in range(0, n):
    (a, b, c, d) = (float(x) for x in input().split())
    x = solve_equation(a, b, c, d)
    print(x, "", end="")

if __name__ == "__main__":
  main()