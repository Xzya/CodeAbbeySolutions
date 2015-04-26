#input
# 124
# 87 18 168 66 69 123 44 164 139 184 105 96 111 74 108 104 110 76 165 180 187 53 55 9 125 84 177 89 122 71 175 140 40 42 163 86 173 102 78 197 181 151 85 62 50 103 97 28 6 5 94 183 70 116 131 79 196 68 179 49 133 194 37 34 11 114 138 72 119 33 56 178 14 109 189 171 195 150 126 128 35 59 100 43 159 92 144 31 17 160 63 155 51 27 65 176 191 20 93 21 188 23 162 77 127 60 158 29 149 199 145 25 113 192 57 61 198 182 152 120 13 47 41 166

def binary_search(array, t):
  xmin = 0
  xmax = len(array)
  index = binary_search_r(array, t, 0, xmin, xmax)
  return index

def binary_search_r(array, t, lastIndex, xmin, xmax):
  x = int(xmin + ((xmax - xmin) // 2))
  if lastIndex == x:
    return lastIndex

  lastIndex = x
  if t > array[x]:
    return binary_search_r(array, t, lastIndex, xmin, x)
  elif t < array[x]:
    return binary_search_r(array, t, lastIndex, x, xmax)
  else:
    return x

def insertion_sort(array):
  sort = [array[0]]
  shifted = []
  for i in range(1, len(array)):
    t = array[i]
    #check to see if t is higher than the last element in the sorted array
    if t >= sort[-1]:
      sort.append(t)
      continue
    # index = binary_search(sort, t)
    for j in range(0, len(sort)):
      if t < sort[j]:
        index = j
        break
    sort = sort[:index+1] + sort[index:]
    sort[index] = t
  return shifted
  # return sort

n = int(input())
array = [int(x) for x in input().split()]
sorted_array = insertion_sort(array)
print(" ".join([str(x) for x in sorted_array]))