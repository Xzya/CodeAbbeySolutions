#input
# 28
# 49 31 32 22 38 5 28 9 12 48 1 37 51 24 39 36 30 20 16 17 45 29 43 25 2 50 27 40

suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

n = int(input())

cards = [int(x) for x in input().split()]

for i in range(0, n):
  value = cards[i]
  rank = value % 13
  suit = value // 13
  rank = ranks[rank]
  suit = suits[suit]

  print(rank + "-of-" + suit, "", end="")
