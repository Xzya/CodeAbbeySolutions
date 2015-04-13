#input
# 637 3371 327 67 924 968 2 6 6 77 5464 21813 70 5 67 74225 46 2 310 6156 50 4 623 87675 1702 3947 4927 9628 7 510 31 65 3321 23993 8406 88 -1

array = [int(x) for x in input().split()]
array.remove(-1)

swaps = 0
for i in range(0, len(array) - 1):
  if array[i] > array[i+1]:
    swaps += 1
    t = array[i]
    array[i] = array[i+1]
    array[i+1] = t

checksum = 0
for num in array:
  checksum += num
  checksum *= 113
checksum %= 10000007

print(swaps, checksum)