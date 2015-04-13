#input
# 19
# 945 426 679 891 378 483 281 141 97 233 848 333 579 639 794 531 46 739 190

n = int(input())

initial_array = [int(x) for x in input().split()]
sorted_array = initial_array[:]

done = False
while not done:
  done = True
  for i in range(0, len(sorted_array) - 1):
    if sorted_array[i] > sorted_array[i+1]:
      done = False
      t = sorted_array[i]
      sorted_array[i] = sorted_array[i+1]
      sorted_array[i+1] = t

for x in sorted_array:
  print(initial_array.index(x) + 1, "", end="")