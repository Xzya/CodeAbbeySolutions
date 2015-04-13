#input
# 19
# 6486 5922
# 3648 760
# 2376 1936
# 2697 1271
# 6020 6440
# 3385 48
# 59 1640
# 9 35
# 1581 1147
# 2106 2028
# 318 10
# 8362 6546
# 660 2700
# 865 5748
# 1479 3567
# 3198 1950
# 10 8
# 81 425
# 27 62

def find_gcd(a, b):
  gcd = None
  while a != 0 and b != 0:
    if a > b:
      a %= b
    else:
      b %= a

    if a == 0:
      gcd = b
    elif b == 0:
      gcd = a
  return gcd

def find_lcd(gcd, a, b):
  return ((a * b) // gcd)

n = int(input())

for i in range(0, n):
  (a, b) = (int(x) for x in input().split())

  gcd = find_gcd(a, b)
  lcd = find_lcd(gcd, a, b)

  print("(" + str(gcd), str(lcd) + ")", "", end="")