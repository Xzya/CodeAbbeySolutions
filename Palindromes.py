#input
# 15
# EveIoaeie-Xwi-xg, kk G X iwxeiea-o i ve
# Zr M cksznun z-skymrz
# Zy-Rl z, C, dcul R Y-z
# Ibov-kfxuy Ssyux-fk vobi
# Yiyay, Wo, e Tejleuooziizo Ou Elj-Eteowy Ay iy
# Uj-Oco-i, Eno yllyo Neiocqj u
# Hmipeahybcyoyamuwsydy-s Wumayfycbyh-Ae Pimh
# Idvkegabzyfa I-Yycgw wgcyyi, Afyzbaoekvdi
# Xlrgoijvlauvfy, D-cp, Pc dyuvu, A-Lvjiogr, Lx
# Rfdauupu, w npipnwu-Puu-a, Dfy
# Ojyyfzlqxgi, pazmzapigxqlzfyyzo
# Bydz, jsjot Itojsjzdy-B
# Eacv u at E-ae Ta-u, vca, e
# Gnj, Tjwuvmryuvayucmomcuyavutrmvuwjtjng
# Ibi, Tuainniaut-Ibi

punctuation = [' ', '.', ',', '?', '!', '-']
n = int(input())

for i in range(0, n):
  sentence = input().lower()
  for p in punctuation:
    sentence = sentence.replace(p, "")
  reversed_sentence = sentence[::-1]
  is_palindrome = None
  if sentence == reversed_sentence:
    is_palindrome = "Y"
  else:
    is_palindrome = "N"
  print(is_palindrome, "", end="")