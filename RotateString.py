#input
# 11
# -2 yecezfzlauaifiy
# -7 pjwjscdtaivraoodlhietd
# 6 ilbfnwuwmijpbeq
# 4 abqdnylslolyqke
# -3 ifivdseequedwefghsitf
# -1 csohemzmrbbvugzeaihq
# 1 kavefyyxbstjwycdrefgyl
# 3 iewbsnlsdjycjpeuc
# 1 pwttoamgajmznda
# -6 stqkwzaavehiyxytl
# -1 biaoboruocdawtlmnghcdpl

n = int(input())

for i in range(0, n):
  (k, s) = (input().split())
  k = int(k)

  s = s[k:] + s[:k]

  print(s, "", end="")