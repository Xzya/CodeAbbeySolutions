#input
# 15
# 1007 802 9100 7873 9791 193
# 7992 428 4535 7267 7601 505
# 2787 6110 7980 9336 7437 1146
# 7049 4993 7394 2223 9068 3398
# 4496 6074 3051 8247 4641 809
# 2855 5648 1610 1955 3520 1400
# 2148 1512 1828 6682 8779 9429
# 7187 1565 5539 5166 900 2976
# 6312 7949 7969 3706 171 7036
# 7104 4667 3110 154 2913 7750
# 962 5768 3397 2572 7723 6917
# 3972 9870 8429 5799 6552 7207
# 5228 3738 8772 766 8904 9671
# 3741 5216 7620 1709 8921 7791
# 8745 6024 2457 1854 6178 5369

import math

def find_perimeter(a, b, c):
  return (a + b + c) / 2.0

def find_area(a, b, c):
  p = find_perimeter(a, b, c)
  f = p * (p - a) * (p - b) * (p - c)
  if f < 0:
    return 0
  return math.sqrt(f)

def calculate_length(pointa, pointb):
  x = pointa[0] - pointb[0]
  y = pointa[1] - pointb[1]

  return (x*x + y*y)**.5

n = int(input())

for i in range(0, n):
  (x1, y1, x2, y2, x3, y3) = (int(x) for x in input().split())
  pointa, pointb, pointc = [x1, y1], [x2, y2], [x3, y3]

  a = calculate_length(pointa, pointb)
  b = calculate_length(pointb, pointc)
  c = calculate_length(pointa, pointc)

  area = find_area(a, b, c)

  # p = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
  # area = abs(p) / 2

  print(area, "", end="")