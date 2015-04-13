#input
# 23
# 430 5468 7002 92223 32896 7143 5 7 631791901 707188 63404 7373174 975230312 7909405 45 35 50416821 224836766 43 71 6162421 7896153 10

n = int(input())

numbers = [int(x) for x in input().split()]
result = 0
for num in numbers:
  result += num
  result *= 113
result %= 10000007

print(result)