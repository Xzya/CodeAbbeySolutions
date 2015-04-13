#input
# 29
# 49 1.40
# 92 1.67
# 103 2.21
# 70 1.71
# 67 1.47
# 46 1.96
# 50 1.44
# 71 1.65
# 88 2.10
# 46 1.26
# 115 2.60
# 94 2.22
# 44 1.35
# 60 1.52
# 45 1.54
# 120 2.74
# 111 1.99
# 41 1.21
# 44 1.45
# 53 1.59
# 51 1.73
# 76 2.05
# 102 1.76
# 107 2.31
# 55 1.25
# 43 1.75
# 51 1.30
# 73 2.14
# 57 1.40

def BMI(weight, height):
    return (weight / (height ** 2))

def grade(bmi):
    if bmi < 18.5:
        return "under"
    elif bmi < 25.0:
        return "normal"
    elif bmi < 30.0:
        return "over"
    elif bmi > 30.0:
        return "obese"

n = int(input())

for k in range(0, n):
    line = [float(i) for i in input().split()]
    bmi = BMI(line[0], line[1])
    print(grade(bmi), "", end="")