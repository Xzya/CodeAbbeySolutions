#input
# 69 237 245 22 97 105 68 243 232 209 177 72 161 199 237 218 206 122 209 100 79 226 195 202 160 238 106 99 118 57 68 68 53 65 240 230 160 99 208 64 118 210 232 244 119 178 69 224 146 87 104 237 232 204 227 75 65 162 90 75 64 133 75 225 238 160 204 54 14 196 121 78 72 240 89 237 145 108 244 179 102 54 32 160 53 82 160 248 238 180 72 66 253 113 103 78 121 237 116 160 46

def decode(seq):
  if len(seq) == 8:
    seq = '0b' + seq[1:]
  char = chr(int(seq,2))
  return char

encoded_sequence = [int(x) for x in input().split()]

for c in encoded_sequence:
  binc = (bin(c))[2:]
  num_of_bits = binc.count('1')

  if num_of_bits % 2 == 0:
    decoded_character = decode(binc)
    print(decoded_character, end="")