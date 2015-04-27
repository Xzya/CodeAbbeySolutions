#input
# 125
# 166 110 40 46 91 169 42 183 53 84 133 102 23 62 66 123 72 185 199 78 132 188 9 50 164 112 192 190 134 197 170 114 180 125 71 11 8 74 20 103 101 141 65 6 162 73 4 181 81 64 85 55 17 5 59 142 126 191 116 179 98 115 14 96 3 135 130 163 1 43 12 95 159 99 22 51 118 86 68 106 148 10 108 60 36 161 38 111 94 44 104 39 80 152 93 34 138 143 193 165 124 47 13 160 63 158 75 49 24 145 52 83 140 56 41 120 67 151 7 129 156 119 195 19 149

def quicksort(array, left, right):
  pivot_pos = partition(array, left, right)
  if pivot_pos - left > 1:
    quicksort(array, left, pivot_pos - 1)
  if right - pivot_pos > 1:
    quicksort(array, pivot_pos + 1, right)

def partition(array, left, right):
  print(str(left) + "-" + str(right), "", end="")
  lt = left
  rt = right
  dir = 'left'
  pivot = array[left]
  while lt < rt:
    if dir == 'left':
      if array[rt] > pivot:
        rt = rt - 1
      else:
        array[lt] = array[rt]
        lt = lt + 1
        dir = 'right'
    else:
      if array[lt] < pivot:
        lt = lt + 1
      else:
        array[rt] = array[lt]
        rt = rt - 1
        dir = 'left'
  array[lt] = pivot
  return lt

n = int(input())
array = [int(x) for x in input().split()]
quicksort(array, 0, len(array)-1)