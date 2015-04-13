#input
# 13
# 19443 576
# 6001842 911503
# 4067 1248
# 6121885 186
# -410349 4955307
# 5375848 874
# 2770998 256
# 18765 1284
# 5813 1630
# 8212240 77
# 293304 -4580549
# 7956897 3420372
# 6775023 846

n = int(input())

for k in range(0, n):
    num = None
    for i in input().split():
        if not(num):
            num = float(i)
            continue
        num /= float(i)
    print(round(num)," ", end="")