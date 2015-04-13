#input
# 37
# 7 3599 83815 51913477 10565410 26 1447 2246 166 6 159071 459 429789 123255 143059893 47012 78641 17171 1437 170043 1761720 178 102 62 215393582 36209 3216809 10405 510805 272 234 242276 32012517 39 6841 2497 1745343

def wsd(digits):
    sum = 0
    for i in range(0, len(digits)):
        sum += int(digits[i]) * (i+1)
    return sum

n = int(input())

digits = [i for i in input().split()]

for k in range(0, n):
    print(wsd(digits[k]), "", end="")