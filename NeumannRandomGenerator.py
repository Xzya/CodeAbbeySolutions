#input
# 12
# 8090 2968 6239 4655 7581 4410 2312 5929 7019 1855 6186 4514

n = int(input())

numbers = input().split()

for i in range(0, n):
  num = int(numbers[i])
  num_set = []
  iterations = 0
  while True:
    if num not in num_set:
      num_set.append(num)
    else:
      break

    num **= 2
    num = str(num)

    if len(num) < 8:
      for j in range(8 - len(num)):
        num = "0" + num
    num = int(num[2:-2])

    iterations += 1

  print(iterations, "", end="")