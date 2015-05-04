#input
# 27
# 90 17
# 67 76
# 21 22
# 28 66
# 58 33
# 47 25
# 40 48
# 22 21
# 11 15
# 57 64
# 65 76
# 38 36
# 88 19
# 70 25
# 52 27
# 77 51
# 34 53
# 37 46
# 66 56
# 21 34
# 79 59
# 50 29
# 17 62
# 41 18
# 68 88
# 73 42
# 73 20

def chance_for_a_to_win(pa,pb):
  return sum(((1-pa)*(1-pb))**(n-1) * (pa) for n in range(1,100)) + 1e-7
# or
def chance_for_a_to_win2(pa,pb):
  return pa/(1-(1-pa)*(1-pb))

def main():
  n = int(input())
  for i in range(0,n):
    (pA, pB) = (int(x) for x in input().split())
    chance = chance_for_a_to_win2(pA/100,pB/100)
    print(round(chance*100),end=' ')

if __name__ == '__main__':
  main()