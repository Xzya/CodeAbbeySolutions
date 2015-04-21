#input
# 1732 13
# 7830 2356 7261 2736 7682 0832 3207 2608 0672 7312 6087 1235 7250

(number, n)  = (x for x in input().split())
n = int(n)

guesses = input().split()

for i in range(0, n):
  guess = guesses[i]

  a = 0
  b = 0
  for c in guess:
    if c in number:
      if guess.index(c) == number.index(c):
        a += 1
      else:
        b +=1

  print(str(a) + "-" + str(b), "", end="")