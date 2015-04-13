#input
# 22
# 172 87 19 46558 536 3487 14193 495 16 13633 30 464 3918 21256 2340 45 25538 44 41473 15622 15167 39

def num_of_steps(x):
  counter = 0
  while x != 1:
    if x % 2 == 0:
      x = x / 2
    else:
      x = 3 * x + 1
    counter += 1
  return counter

n = int(input())

for x in input().split():
  print(num_of_steps(int(x)), "", end="")