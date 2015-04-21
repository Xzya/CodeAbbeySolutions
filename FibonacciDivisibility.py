#input
# 23
# 9529 2701 7878 7278 3604 5778 2929 6225 9376 5551 6525 4728 5104 9452 6975 3226 3302 4875 7502 4429 4126 4053 2327

def find_next_fib(fib_numbers):
  for i in range(0, 10):
    a, b = fib_numbers[-2:]
    c = a + b
    fib_numbers.append(c)

n = int(input())
numbers = [int(x) for x in input().split()]
fib_numbers = [0, 1]

for i in range(0, n):
  num = numbers[i]

  found = False
  last_index = 2
  while not found:
    find_next_fib(fib_numbers)
    for j in range(last_index, len(fib_numbers)):
      if fib_numbers[j] % num == 0:
        print(j, "", end="")
        found = True
        break
      last_index = j