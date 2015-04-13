#input
# 28
# RP PP RR PS RP
# PR PP SR PS SS RR RS RP
# PR SP PR RS RP PP RS
# RP PS PS PR SS RR PP PR SP SP RR PR PS PS SP
# RS PS RR PR RP PR RS SR SR RR PP PP SR RS RP
# RR RR RR SP PR RP RR PP SP PS RR RS SP
# SS RP RP PP SS RR RP PS SP RR RS SR RS RS SS PS
# SR SP SR RP RP SS SP PP SS SS SS SS RP
# SR PP RP PP RP SS SR PP RR RP
# RR SS RP SR RP RP SS PP RR SS SP PR SS PR RS SR RP
# PR SS PR SS SS PP RP RS
# PR PP RS PR SP
# RR PP RR RP RR RR RS PR RS RP RP RS
# RR SR SR PS PR RP PP SS SS SP PR SR
# PP SS PR RP SR RS SR PS
# SR SS SP SS RR SR PR PR
# RP RR RS PP SR PP SS PR PR SR SP PR PP SP
# SP RP PP PP RS PR PS RR PR SP RS
# SR PR PP SP RR SP SR RP PR
# SS SS RR RS SP PR RP SP RR RS RP PS RS
# PR PP SR PS RP
# SR SR PR SR PR PP SS RP
# RP SS PR PP RS PP RS RP PP RP PP SS SP PP PR
# SP SS RR RP PS RS RS
# PP SS RR RR SS SP RR SR RR RS RR SS PP RP PR
# RP RS SP SS PS PS SS SR SS RS RR PS
# RS RS RS SP RS PP SR RP SS PP SP
# PP RP SS PS RP RS PR PR RR PS SP SP

def convert_sign(s):
  if (s == 'R'):
    return 0
  elif (s == 'P'):
    return 1
  else:
    return 2

def winner(seq):
  a = convert_sign(seq[0])
  b = convert_sign(seq[1])

  res = (a - b + 3) % 3

  if res == 0:
    return -1
  elif res == 1:
    return 0
  else:
    return 1

def check_winner(s):
  player = [0,0]

  for i in range(0, len(s)):
    win = winner(s[i])
    if win != -1:
      player[win] += 1

  if player[0] > player[1]:
    return 0
  elif player[0] < player[1]:
    return 1
  else:
    return -1

def main():
  n = int(input())
  for i in range(0, n):
    seq = input().split()

    winner = check_winner(seq)

    if winner == -1:
      return

    print(winner + 1, "", end="")

if __name__ == "__main__":
  main()