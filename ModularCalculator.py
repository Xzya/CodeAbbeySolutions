#input
# 2288
# * 415
# + 96
# * 625
# * 83
# + 2186
# * 1
# + 2
# + 930
# * 5375
# * 3
# + 99
# + 4162
# * 50
# * 5
# * 277
# * 37
# * 41
# + 4
# * 862
# * 4
# * 76
# + 7
# + 305
# * 4467
# + 1
# + 26
# * 659
# + 8
# + 507
# * 7109
# + 2
# * 268
# + 100
# * 10
# * 989
# * 4
# * 10
# + 43
# * 8
# * 5
# * 7
# + 2
# + 52
# * 8
# * 24
# + 377
# + 6
# + 3
# * 3
# + 302
# % 7846

result = int(input())

next = input()

while next:
  op, n = next.split()

  if op == "+":
    result += int(n)
  elif op == "*":
    result *= int(n)
  elif op == "%":
    result %= int(n)
    break
  next = input()

print(result)