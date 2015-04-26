#input
# 20
# 61805557897
# 1637677356949
# 1033200463951
# 232022744333
# 3228899709877
# 63969904967
# 31998330919
# 24673399901
# 1361055835961
# 296624456963
# 1125919944761
# 9368798607989
# 2020318785259
# 1369854206401
# 512780553161
# 902986479947
# 617222057527
# 7456259792411
# 1997799802849
# 843168860101

def find_factors(num):
  factors = []
  j = 2
  numm = num
  while True:
    div = numm / j
    if div.is_integer():
      factors.append(j)
      numm = div
      j = 2
      if div == 1:
        break
    else:
      j += 1
  return factors

n = int(input())

for i in range(0, n):
  num = int(input())
  factors = find_factors(num)
  print("*".join([str(x) for x in factors]), "", end="")
