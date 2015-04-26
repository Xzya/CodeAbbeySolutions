#input
# 235 923 2207 6514 865 900 901 260 5403 73 6183 44 888 67 3169 44 401 275 56 1110 7586 32 666 610 83 33 657 284 8542 654 42 73 4618 4417 926 438 7539 3439 334 6266 29 609 1333 6955 2459 158 445 4853 8804 4245 4798 4903

import random

class Pack:
  if __name__ == '__main__':
    ranks = ['A',2,3,4,5,6,7,8,9,'T','J','Q','K']
    suits = ['C','D','H','S']
    cards = []
    for s in suits:
      for r in ranks:
        cards.append(str(s) + str(r))
    random_numbers = [int(x) for x in input().split()]
    for i in range(0, len(cards)):
      r = random_numbers[i] % 52
      temp = cards[i]
      cards[i] = cards[r]
      cards[r] = temp
    print(' '.join(cards))