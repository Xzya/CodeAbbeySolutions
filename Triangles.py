#input
# 24
# 859 720 747
# 640 1235 333
# 568 1077 2437
# 1849 1034 677
# 258 156 535
# 142 346 115
# 1249 433 844
# 1612 1004 580
# 803 2833 1345
# 958 1157 757
# 244 185 267
# 550 778 301
# 932 602 979
# 566 799 1698
# 1077 1467 632
# 920 868 1739
# 217 111 102
# 915 709 1910
# 1253 829 1287
# 182 134 401
# 431 1478 595
# 564 385 1215
# 176 337 613
# 699 984 500

import math

def find_perimeter(a, b, c):
  return (a + b + c) / 2.0

def find_area(a, b, c):
  p = find_perimeter(a, b, c)
  f = p * (p - a) * (p - b) * (p - c)
  if f < 0:
    return 0
  return math.sqrt(f)

n = int(input())

for i in range(0, n):
  (a, b, c) = (int(x) for x in input().split())
  area = find_area(a, b, c)
  if area > 0.0:
    print(1, "", end="")
  else:
    print(0, "", end="")