#input
# 32 6
# Castor 551 641
# Procyon -922 -520
# Deneb -459 -741
# Mizar -221 -209
# Mira -34 -614
# Sirius -960 -76
# Alcor -76 339
# Heka 733 631
# Betelgeuse -814 -641
# Nembus -433 -71
# Thabit 53 -6
# Media -493 -567
# Gemma 425 -418
# Yildun -879 463
# Jabbah -135 -903
# Kochab 495 -585
# Bellatrix 738 574
# Diadem -104 -721
# Altair 834 675
# Unuk 70 -200
# Rigel -940 111
# Kastra 724 -15
# Capella -551 456
# Polaris -384 -364
# Zosma 816 183
# Alcyone 565 -131
# Electra -824 -928
# Fomalhaut 302 602
# Albireo -346 423
# Pherkad 64 519
# Lesath 521 -441
# Vega 934 258

import math

def normalize(v):
  length = (v[0]**2 + v[1]**2)**.5
  normalized_v = (v[0]/length, v[1]/length)
  return normalized_v

def cross_product(a, b):
  cp = a[0] * b[1] - b[0] * a[1]
  return abs(cp)

def dot_product(a, b):
  dp = a[0] * b[0] + a[1] * b[1]
  return dp

def rotation_matrix_degree(degree):
  rad = degree * math.pi/180
  R = (normalize((math.cos(rad), -math.sin(rad))), normalize((math.sin(rad), math.cos(rad))))
  return R

def multiply_mv(m, v):
  result = [0,0]
  for i in range(0, 2):
    for j in range(0, 2):
      result[i] += m[i][j] * v[j]
  return tuple(result)

def transform_vector_degree(v, degree):
  R = rotation_matrix_degree(degree)
  mv = multiply_mv(R, v)
  return mv

def sort_by_y_asc(v):
  e = 1
  while e:
    e = 0
    for i in range(0, len(v) - 1):
      if v[i][2] > v[i+1][2]:
        t = v[i]
        v[i] = v[i+1]
        v[i+1] = t
        e = 1
      elif v[i][2] == v[i+1][2]:
        if v[i][1] > v[i+1][1]:
          t = v[i]
          v[i] = v[i+1]
          v[i+1] = t
          e = 1
  return v

(n, angle) = (int(x) for x in input().split())
points = []

for i in range(0, n):
  (name, x, y) = (x for x in input().split())
  x = int(x)
  y = int(y)
  v = transform_vector_degree((x,y), angle)
  v = (round(v[0]), round(v[1]))
  points.append([name, v[0], v[1]])

sorted_points = sort_by_y_asc(points)

for p in sorted_points:
  print(p[0], "", end="")