#input
# 23
# 9529 2701 7878 7278 3604 5778 2929 6225 9376 5551 6525 4728 5104 9452 6975 3226 3302 4875 7502 4429 4126 4053 2327
import math

def find_fib_until(fib_numbers, num):
  while True:
    a, b = fib_numbers[-2:]
    c = a + b
    fib_numbers.append(c)
    del fib_numbers[0]
    if c > num:
      break

def find_next_fib(fib_numbers):
  for i in range(0, 100):
    a, b = fib_numbers[-2:]
    c = a + b
    fib_numbers.append(c)

def is_fib(x):
  test1 = 5 * (x**2) + 4
  if (test1**.5).is_integer():
    return True
  test2 = 5 * (x**2) - 4
  if (test2**.5).is_integer():
    return True
  return False

def find_position(Fn):
  n = math.log((Fn * math.sqrt(5) + math.sqrt(5 * (Fn*Fn) + 4))/2, (1 + math.sqrt(5))/2)
  print(n)

def fib_index(Fn):
  Fn = float(Fn)
  phi = (1 + math.sqrt(5)) / 2
  x = Fn.__mul__(math.sqrt(5)).__add__((1/2))

  return round(math.log(x) / math.log(phi))

# n = int(input())
# numbers = [int(x) for x in input().split()]

n = 2
numbers = [233328, 433156]

fib_numbers = [0, 1]

for i in range(0, n):
  num = numbers[i]

  j = 1
  while True:
    k = num * j
    if is_fib(k):
      print(k, fib_index(k))
      break
    j += 1

  # found = False
  # fib_numbers = [0, 1]
  # find_fib_until(fib_numbers, num*num)
  # last_index = 2
  # while not found:
  #   find_next_fib(fib_numbers)
  #   for j in range(last_index, len(fib_numbers)):
  #     if fib_numbers[j] % num == 0:
  #       print(j, "", end="")
  #       found = True
  #       break
  #     last_index = j