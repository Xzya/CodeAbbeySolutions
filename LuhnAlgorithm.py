#input
# 45
# 2457936494652626
# 97?4007043638635
# 1383223592?19814
# 9395692538403002
# 405462418?345881
# 9472573944710938
# 43?3987686879416
# 2168466840113397
# ?599469437091510
# 5958352483344315
# 2642476956082118
# 6473415214792624
# 28127311?5484100
# 9227858484323065
# 71738796155953?1
# ?339050987742616
# 8490248467735171
# 8213172347506405
# 6098933888371907
# 4241754159?11181
# 5534314125571464
# 2?25405427772498
# 7388680925755520
# 20035408?2444772
# 1618393556438909
# 1?41890293636382
# 54926582329?0325
# 6635430790034167
# 2105674206038953
# 9002545672047379
# 1975?60161120392
# 44?7150269128544
# 6873597103826488
# 31?5462150267707
# 99815398?5769563
# 8852439461195853
# 50?4168617952405
# 6175588802114733
# 7809398653901945
# 7266231702578582
# 5917970014697137
# 4143254325523211
# 6055195471726484
# 9770745295817222
# 5373564995382308

def checksum(num):
  i = len(num) - 1
  second = False
  csum = 0
  while i >= 0:
    if second:
      temp = int(num[i]) * 2
      if temp > 9:
        temp -= 9
      csum += temp
    else:
      csum += int(num[i])
    second = not second
    i -= 1
  return csum

def is_valid(csum):
  if csum % 10 == 0:
    return True
  return False

def find_valid_card_number(num):
  if num.count('?') > 0:
    i = 0
    while i < 10:
      temp_num = num[:]
      temp_num = temp_num.replace('?', str(i))
      csum = checksum(temp_num)
      if is_valid(csum):
        return temp_num
      else:
        i += 1
  else:
    i = 0
    while i < len(num) - 1:
      temp_num = list(num[:])
      t = temp_num[i]
      temp_num[i] = temp_num[i+1]
      temp_num[i+1] = t
      csum = checksum(temp_num)
      if is_valid(csum):
        return ''.join(temp_num)
      else:
        i += 1

def main():
  n = int(input())
  for i in range(n):
    card = input()
    fixed_num = find_valid_card_number(card)
    print(fixed_num, end=' ')

if __name__ == '__main__':
  main()
