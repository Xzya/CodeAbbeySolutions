#input
# 20
# 18 7 1 8 11 6 5 4 13 20 2 16 9 10 19 14 12 17 15 3

n = int(input())

array = [int(x) for x in input().split()]

passes = 0
swaps = 0
done = False
while not done:
  done = True
  passes += 1
  for i in range(0, n - 1):
    if array[i] > array[i+1]:
      done = False
      swaps += 1
      t = array[i]
      array[i] = array[i+1]
      array[i+1] = t

print(passes, swaps)