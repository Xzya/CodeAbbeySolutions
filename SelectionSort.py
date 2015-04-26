#input
# 120
# 55 21 102 38 114 63 131 194 198 115 48 108 80 170 12 37 74 47 154 157 6 188 191 8 61 179 155 60 111 138 132 41 152 46 104 84 40 88 10 78 59 22 69 86 26 75 17 2 135 195 106 95 109 62 145 124 141 143 151 70 173 136 42 67 118 162 119 98 79 77 93 185 171 3 24 107 64 146 32 153 43 174 113 13 110 35 121 164 72 85 148 120 156 94 27 30 33 183 76 101 68 103 168 105 90 54 126 50 193 92 178 57 51 130 182 5 71 66 122 18

def selection_sort(array):
  bound = len(array)-1
  while bound > 0:
    max_num = max(array[:bound+1])
    max_index = array.index(max_num)
    print(max_index, "", end="")

    temp = array[bound]
    array[bound] = max_num
    array[max_index] = temp

    bound -= 1
  return array

n = int(input())
array =[int(x) for x in input().split()]
sorted_array = selection_sort(array)

# print(array)