#input
# 7 1
# BT FBTZ BT MZJOH DBSUIBHF NVTU CF EFTUSPZFE.
# HJWF ZPVS SPPLT CVU OPU EJMBSBN HSFFOGJFMET BSF HPOF OPX.
# UIBU BMM NFO BSF DSFBUFE FRVBM XIP XBOUT UP MJWF GPSFWFS NFU B XPNBO BU UIF XFMM.
# BSF XPOEFST NBOZ UPME.
# B EBZ BU UIF SBDFT UIF TFDSFU PG IFBUIFS BMF JO BODJFOU QFSTJB UIFSF XBT B LJOH.
# GPVS TDPSF BOE TFWFO ZFBST BHP.
# MPWFTU UIPV NF QFUFS B OJHIU BU UIF PQFSB.

alphabet = [c for c in 'abcdefghijklmnopqrstuvwxyz'.upper()]
(n, k) = (int(x) for x in input().split())

dict = {}

for i in range(0, len(alphabet)):
  dict[alphabet[(i+k) % len(alphabet)]] = alphabet[i]

for i in range(0, n):
  sentence = input()

  ciphered = ''
  for c in sentence:
    if c != ' ' and c != '.':
      ciphered += dict[c]
    else:
      ciphered += c

  print(ciphered, "", end="")