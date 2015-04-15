import math
import copy

def distance_between_points(a, b):
  dist = ((b[0] - a[0])**2 + (b[1] - a[1])**2)**.5
  return dist

n0 = 94
n1=92
xy0 = [[-47.5, -10.4],[19.1, 25.9],[18.9, -10.4],[-2.1, -47.6],[41.8, -12.1],[-15.7, 12.1],[-11.0, -0.6],[-15.6, -7.6],[14.9, 43.5],[16.6, 0.1],[3.6, -33.5],[-14.2, 20.8],[17.8, -29.8],[-2.2, -12.8],[44.6, 19.7],[17.9, -41.3],[24.6, 37.0],[43.9, 14.5],[23.8, 19.6],[-4.2, -40.5],[32.0, 17.2],[22.6, -26.9],[9.9, -33.4],[-13.6, 6.6],[48.5, -3.5],[-9.9, -39.9],[-28.2, 20.7],[7.1, 15.5],[-36.2, -29.9],[-18.2, 11.1],[-1.2, -13.7],[9.3, 9.3],[39.2, 15.8],[-5.2, -16.2],[-34.9, 5.0],[-13.4, -31.8],[24.7, -29.1],[1.4, 24.0],[-24.4, 18.0],[11.9, -29.1],[36.3, 18.6],[30.3, 38.4],[4.8, -20.5],[-46.8, 12.1],[-44.2, -6.0],[-1.4, -39.7],[-1.0, -13.7],[13.3, 23.6],[37.4, -7.0],[-22.3, 37.8],[17.6, -3.3],[35.0, -9.1],[-44.5, 13.1],[-5.1, 19.7],[-12.1, 1.7],[-30.9, -1.9],[-19.4, -15.0],[10.8, 31.9],[19.7, 3.1],[29.9, -16.6],[31.7, -26.8],[38.1, 30.2],[3.5, 25.1],[-14.8, 19.6],[2.1, 29.0],[-9.6, -32.9],[24.8, 4.9],[-2.2, -24.7],[-4.3, -37.4],[-3.0, 37.4],[-34.0, -21.2],[-18.4, 34.6],[9.3, -45.2],[-21.1, -10.3],[-19.8, 29.1],[31.3, 37.7],[27.2, 19.3],[-1.6, -45.6],[35.3, -23.5],[-39.9, -19.8],[-3.8, 40.6],[-15.7, 12.5],[-0.8, -16.3],[-5.1, 13.1],[-13.8, -25.7],[43.8, 5.6],[9.2, 38.6],[42.2, 0.2],[-10.0, -48.6],[14.1, -6.5],[34.6, -26.8],[11.1, -6.7],[-6.1, 25.1],[-38.3, 8.1]]
xy1 = [[-14.8, 10.9],[18.8, -0.1],[-11.3, 5.7],[-19.7, 6.9],[-11.5, -16.7],[-45.4, -15.3],[6.0, -46.9],[-24.1, -26.3],[30.2, 27.4],[21.4, -27.2],[12.1, -36.1],[23.8, -38.7],[41.5, 5.3],[-8.7, 25.5],[36.6, -5.9],[43.7, -14.6],[-9.7, -8.6],[34.7, -19.3],[-15.5, 19.3],[21.4, 3.9],[34.0, 29.8],[6.5, 19.5],[28.2, -21.7],[13.4, -41.8],[-25.9, -6.9],[37.5, 27.8],[18.1, 44.7],[-43.0, -19.9],[-15.7, 18.0],[2.4, -31.6],[9.6, -37.6],[15.4, -28.8],[43.6, -11.2],[4.6, -10.2],[-8.8, 38.2],[8.7, -34.6],[-4.7, 14.1],[-1.7, 31.3],[0.6, 27.9],[26.3, 13.7],[-1.2, 26.3],[32.1, -17.7],[15.5, 32.6],[-14.4, -12.6],[22.3, -22.5],[7.0, 48.5],[-6.4, 20.5],[-42.9, 4.2],[-23.0, 31.6],[-24.6, 14.0],[-30.2, -26.5],[-29.0, 15.7],[6.0, 36.3],[44.3, 13.5],[-27.6, 33.7],[13.4, -43.9],[10.5, 28.9],[47.0, 1.4],[10.2, 14.0],[13.3, -15.9],[-3.4, -25.6],[-14.7, 10.5],[21.6, 27.6],[21.8, 10.6],[-37.8, -14.2],[7.6, -21.8],[-8.6, 1.3],[6.8, -13.3],[40.9, -15.3],[-10.3, 41.1],[6.0, -10.8],[-1.5, -31.4],[-35.6, 1.0],[2.5, -14.3],[24.4, -2.6],[-24.1, -35.3],[-29.9, -34.7],[15.9, -1.0],[19.5, 7.0],[44.5, 19.1],[39.7, 2.7],[2.7, 42.4],[-23.0, 25.9],[25.0, 28.2],[31.2, -32.8],[3.9, -38.4],[-44.8, 2.7],[-39.9, -19.3],[-7.0, -0.6],[5.8, -10.9],[-44.5, 19.9],[-31.5, -1.2]]
temp1 = [-47.5, -10.4, 19.1, 25.9, 18.9, -10.4, -2.1, -47.6, 41.8, -12.1, -15.7, 12.1, -11.0, -0.6, -15.6, -7.6, 14.9, 43.5, 16.6, 0.1, 3.6, -33.5, -14.2, 20.8, 17.8, -29.8, -2.2, -12.8, 44.6, 19.7, 17.9, -41.3, 24.6, 37.0, 43.9, 14.5, 23.8, 19.6, -4.2, -40.5, 32.0, 17.2, 22.6, -26.9, 9.9, -33.4, -13.6, 6.6, 48.5, -3.5, -9.9, -39.9, -28.2, 20.7, 7.1, 15.5, -36.2, -29.9, -18.2, 11.1, -1.2, -13.7, 9.3, 9.3, 39.2, 15.8, -5.2, -16.2, -34.9, 5.0, -13.4, -31.8, 24.7, -29.1, 1.4, 24.0, -24.4, 18.0, 11.9, -29.1, 36.3, 18.6, 30.3, 38.4, 4.8, -20.5, -46.8, 12.1, -44.2, -6.0, -1.4, -39.7, -1.0, -13.7, 13.3, 23.6, 37.4, -7.0, -22.3, 37.8, 17.6, -3.3, 35.0, -9.1, -44.5, 13.1, -5.1, 19.7, -12.1, 1.7, -30.9, -1.9, -19.4, -15.0, 10.8, 31.9, 19.7, 3.1, 29.9, -16.6, 31.7, -26.8, 38.1, 30.2, 3.5, 25.1, -14.8, 19.6, 2.1, 29.0, -9.6, -32.9, 24.8, 4.9, -2.2, -24.7, -4.3, -37.4, -3.0, 37.4, -34.0, -21.2, -18.4, 34.6, 9.3, -45.2, -21.1, -10.3, -19.8, 29.1, 31.3, 37.7, 27.2, 19.3, -1.6, -45.6, 35.3, -23.5, -39.9, -19.8, -3.8, 40.6, -15.7, 12.5, -0.8, -16.3, -5.1, 13.1, -13.8, -25.7, 43.8, 5.6, 9.2, 38.6, 42.2, 0.2, -10.0, -48.6, 14.1, -6.5, 34.6, -26.8, 11.1, -6.7, -6.1, 25.1, -38.3, 8.1]
temp2 = [-14.8, 10.9, 18.8, -0.1, -11.3, 5.7, -19.7, 6.9, -11.5, -16.7, -45.4, -15.3, 6.0, -46.9, -24.1, -26.3, 30.2, 27.4, 21.4, -27.2, 12.1, -36.1, 23.8, -38.7, 41.5, 5.3, -8.7, 25.5, 36.6, -5.9, 43.7, -14.6, -9.7, -8.6, 34.7, -19.3, -15.5, 19.3, 21.4, 3.9, 34.0, 29.8, 6.5, 19.5, 28.2, -21.7, 13.4, -41.8, -25.9, -6.9, 37.5, 27.8, 18.1, 44.7, -43.0, -19.9, -15.7, 18.0, 2.4, -31.6, 9.6, -37.6, 15.4, -28.8, 43.6, -11.2, 4.6, -10.2, -8.8, 38.2, 8.7, -34.6, -4.7, 14.1, -1.7, 31.3, 0.6, 27.9, 26.3, 13.7, -1.2, 26.3, 32.1, -17.7, 15.5, 32.6, -14.4, -12.6, 22.3, -22.5, 7.0, 48.5, -6.4, 20.5, -42.9, 4.2, -23.0, 31.6, -24.6, 14.0, -30.2, -26.5, -29.0, 15.7, 6.0, 36.3, 44.3, 13.5, -27.6, 33.7, 13.4, -43.9, 10.5, 28.9, 47.0, 1.4, 10.2, 14.0, 13.3, -15.9, -3.4, -25.6, -14.7, 10.5, 21.6, 27.6, 21.8, 10.6, -37.8, -14.2, 7.6, -21.8, -8.6, 1.3, 6.8, -13.3, 40.9, -15.3, -10.3, 41.1, 6.0, -10.8, -1.5, -31.4, -35.6, 1.0, 2.5, -14.3, 24.4, -2.6, -24.1, -35.3, -29.9, -34.7, 15.9, -1.0, 19.5, 7.0, 44.5, 19.1, 39.7, 2.7, 2.7, 42.4, -23.0, 25.9, 25.0, 28.2, 31.2, -32.8, 3.9, -38.4, -44.8, 2.7, -39.9, -19.3, -7.0, -0.6, 5.8, -10.9, -44.5, 19.9, -31.5, -1.2]

## uncomment this to take input from keyboard
# temp1 = []
# temp2 = []
# n0 = int(input())
# xy0 = []
# for i in range(0, n0):
#   (x,y) = (float(x) for x in input().split())
#   xy0.append([x,y])
#   temp1.append(x)
#   temp1.append(y)
# n1 = int(input())
# xy1 = []
# for i in range(0, n1):
#   (x,y) = (float(x) for x in input().split())
#   xy1.append([x,y])
#   temp2.append(x)
#   temp2.append(y)

##-------------------------------------------------------------------------------------
class Dist:
  ix = None
  d = None
  def __init__(self):
    pass

class Cluster:
  x = None
  y = None
  iy = None
  err = None
  ix = []
  d = []
  def __init__(self):
    pass

max_r = 5.0
max_err = 0.2
max_rr = max_r**2
max_errr = max_err**2
ix0 = [None] * n0
ix1 = [None] * n1
wi0, wi1 = None, None
cl0 = []
cl1 = []
txy1 = [[None for j in range(2)] for i in range(n1)]
##--------------------------------------------------------------------------------------

def atanxy(x, y):
  pi = math.pi
  pi2 = 2 * math.pi
  sx, sy, a = None, None, None
  _zero = 1.0e-30
  sx = 0;
  if x < -_zero:
    sx = -1
  if x > +_zero:
    sx = +1
  sy = 0
  if y < -_zero:
    sy = -1
  if y > +_zero:
    sy = +1
  if sy == 0 and sx == 0:
    return 0
  if sx == 0 and sy > 0:
    return 0.5 * pi
  if sx == 0 and sy < 0:
    return 1.5 * pi
  if sy == 0 and sx > 0:
    return 0
  if sy == 0 and sx < 0:
    return pi
  a = y/x
  if a < 0:
    a = -a
  a = math.atan(a)
  if x > 0 and y > 0:
    a = a
  if x < 0 and y > 0:
    a = pi-a
  if x < 0 and y < 0:
    a = pi + a
  if x > 0 and y < 0:
    a = pi2 - a
  return a

def compute():
  i0,i1,e,f = None, None, None, None
  a,x,y = None, None, None
  ## original indexes (to keep track)
  for e in range(0, n0):
    ix0[e] = e
  for e in range(0, n1):
    ix1[e] = e
  ## sort xy0[] by x asc
  e = 1
  while e:
    e = 0
    i0 = 0
    for i1 in range(1, n0):
      if xy0[i0][0] > xy0[i1][0]:
        e = ix0[i0]
        ix0[i0] = ix0[i1]
        ix0[i1] = e
        e = 1
        a = xy0[i0][0]
        xy0[i0][0] = xy0[i1][0]
        xy0[i1][0] = a
        a = xy0[i0][1]
        xy0[i0][1] = xy0[i1][1]
        xy0[i1][1] = a
      i0 += 1
  ## sort xy1[] by x asc
  e = 1
  while e:
    e = 0
    i0 = 0
    for i1 in range(1, n1):
      if xy1[i0][0] > xy1[i1][0]:
        e = ix1[i0]
        ix1[i0] = ix1[i1]
        ix1[i1] = e
        e = 1
        a = xy1[i0][0]
        xy1[i0][0] = xy1[i1][0]
        xy1[i1][0] = a
        a = xy1[i0][1]
        xy1[i0][1] = xy1[i1][1]
        xy1[i1][1] = a
      i0 += 1
  ##----------------------
  d = Dist()
  c = Cluster()
  pc, pd = None, None
  dist = []

  ## find star clusters in xy0[]
  cl0 = []
  for i0 in range(0, n0):
    dist = []
    for i1 in range(i0+1, n0):
      if abs(xy0[i0][0] - xy0[i1][0]) > max_r:
        break
      x = xy0[i0][0] - xy0[i1][0]
      x *= x
      y = xy0[i0][1] - xy0[i1][1]
      y *= y
      a = x + y

      if a <= max_rr:
        d.ix = i1
        d.d = a
        dist.append(copy.copy(d))
    if len(dist) >= 2:
      c.ix = []
      c.err = -1.0
      c.ix.append(copy.copy(i0))
      for i1 in range(0, len(dist)):
        c.ix.append(copy.copy(dist[i1].ix))
      c.iy = -1 #??????????????????????
      c.x = xy0[i0][0]
      for i1 in range(0, len(dist)):
        c.x += xy0[dist[i1].ix][0]
      c.x /= len(dist) + 1 #???????????????????
      c.y = xy0[i0][1]
      for i1 in range(0, len(dist)):
        c.y += xy0[dist[i1].ix][1]
      c.y /= len(dist) + 1 #???????????????????????

      e = 1
      for i1 in range(0, len(cl0)):
        # pc = cl0[i1]
        x = c.x - cl0[i1].x
        x *= x
        y = c.y - cl0[i1].y
        y *= y
        a = x + y
        if a < max_rr:
          cl0[i1].x = 0.5 * (cl0[i1].x + c.x)
          cl0[i1].y = 0.5 * (cl0[i1].y + c.y)
          for e in range(0, len(c.ix)):
            for f in range(0, len(cl0[i1].ix)):
              if cl0[i1].ix[f] == c.ix[e]:
                f = -1
                break
            if f >= 0:
              cl0[i1].ix.append(copy.copy(c.ix[e]))
          e = 0
          break
      if e:
        cl0.append(copy.copy(c))
  ## full recompute clusters
  pc = cl0
  for f in range(0, len(cl0)):
    pc[f].x = 0.0
    for i1 in range(0, len(pc[f].ix)):
      pc[f].x += xy0[pc[f].ix[i1]][0]
    pc[f].x /= len(pc[f].ix) #??????????????
    pc[f].y = 0.0
    for i1 in range(0, len(pc[f].ix)):
      pc[f].y += xy0[pc[f].ix[i1]][1]
    pc[f].y /= len(pc[f].ix) #??????????????

    ## distances
    pc[f].d = []
    for i0 in range(0, len(pc[f].ix)):
      for i1 in range(i0+1, len(pc[f].ix)):
        x = xy0[pc[f].ix[i1]][0] - xy0[pc[f].ix[i0]][0]
        x *= x
        y = xy0[pc[f].ix[i1]][1] - xy0[pc[f].ix[i0]][1]
        y *= y
        pc[f].d.append(copy.copy(math.sqrt(x + y)))
    ## sort by distance asc
    e = 1
    while e:
      e = 0
      i0 = 0
      for i1 in range(1, len(pc[f].d)):
        if pc[f].d[i0] > pc[f].d[i1]:
          a = pc[f].d[i0]
          pc[f].d[i0] = pc[f].d[i1]
          pc[f].d[i1] = a
          e = 1
        i0 += 1
  ## find star clusters in xy1[]
  cl1 = []
  for i0 in range(0, n1):
    dist = []
    for i1 in range(i0+1, n1):
      if abs(xy1[i0][0] - xy1[i1][0]) > max_r:
        break
      x = xy1[i0][0] - xy1[i1][0]
      x *= x
      y = xy1[i0][1] - xy1[i1][1]
      y *= y
      a = x + y

      if a <= max_rr:
        d.ix = i1
        d.d = a
        dist.append(copy.copy(d))
    if len(dist) >= 2:
      c.ix = []
      c.err = -1.0
      c.ix.append(copy.copy(i0))
      for i1 in range(0, len(dist)):
        c.ix.append(copy.copy(dist[i1].ix))
      c.iy = -1 # ???????????????????
      c.x = xy1[i0][0]
      for i1 in range(0, len(dist)):
        c.x += xy1[dist[i1].ix][0]
      c.x /= len(dist) + 1 # ??????????????
      c.y = xy1[i0][1]
      for i1 in range(0, len(dist)):
        c.y += xy1[dist[i1].ix][1]
      c.y /= len(dist) + 1 # ??????????????

      e = 1
      for i1 in range(0, len(cl1)):
        pc = cl1[i1]
        x = c.x - pc.x
        x *= x
        y = c.y - pc.y
        y *= y
        a = x + y
        if a < max_rr:
          pc.x = 0.5 * (pc.x + c.x)
          pc.y = 0.5 * (pc.y + c.y)
          for e in range(0, len(c.ix)):
            for f in range(0, len(pc.ix)):
              if pc.ix[f] == c.ix[e]:
                f = -1
                break
            if f >= 0:
              pc.ix.append(copy.copy(c.ix[e]))
          e = 0
          break
      if e:
        cl1.append(copy.copy(c))
  ## full recompute clusters
  pc = cl1
  for f in range(0, len(cl1)):
    pc[f].x = 0.0
    for i1 in range(0, len(pc[f].ix)):
      pc[f].x += xy1[pc[f].ix[i1]][0]
    pc[f].x /= len(pc[f].ix) #?????????????
    pc[f].y = 0.0
    for i1 in range(0, len(pc[f].ix)):
      pc[f].y += xy1[pc[f].ix[i1]][1]
    pc[f].y /= len(pc[f].ix) # ?????????????

    ## distances
    pc[f].d = []
    for i0 in range(0, len(pc[f].ix)):
      for i1 in range(i0+1, len(pc[f].ix)):
        x = xy1[pc[f].ix[i1]][0] - xy1[pc[f].ix[i0]][0]
        x *= x
        y = xy1[pc[f].ix[i1]][1] - xy1[pc[f].ix[i0]][1]
        y *= y
        pc[f].d.append(math.sqrt(x + y))
    ## sort by distance asc
    e = 1
    while e:
      e = 0
      i0 = 0
      for i1 in range(1, len(pc[f].d)):
        if pc[f].d[i0] > pc[f].d[i1]:
          a = pc[f].d[i0]
          pc[f].d[i0] = pc[f].d[i1]
          pc[f].d[i1] = a
          e = 1

        i0 += 1
  ## find matches
  pc = cl0
  for i0 in range(0,len(cl0)):
    if pc[i0].iy < 0:
      e = -1
      x = 0.0
      pd = cl1
      for i1 in range(0, len(cl1)):
        if len(pc[i0].d) == len(pd[i1].d):
          y = 0.0
          for f in range(0, len(pc[i0].d)):
            y += abs(pc[i0].d[f] - pd[i1].d[f])
          if e < 0 or x > y:
            e = i1
            x = y
      x /= len(pc[i0].d)
      if e >= 0 and x < max_err:
        if cl1[e].iy >= 0:
          cl0[cl1[e].iy].iy = -1
        pc[i0].iy = e
        cl1[e].iy = i0
        pc[i0].err = x
        cl1[e].err = x

  ## compute transform
  tx0 = 0.0
  tx1 = 0.0
  ty0 = 0.0
  ty1 = 0.0
  tc = 1.0
  ts = 0.0
  i0 = -1
  i1 = -1

  pc = cl0
  f = 0
  for e in range(0, len(cl0)):
    if pc[e].iy >= 0:
      if f == 0:
        i0 = e
      if f == 1:
        i1 = e
        break
      f += 1
  if (i1 >= 0):
    pc = cl0[i0]
    pd = cl0[i1]
    tx1 = pc.x
    ty1 = pc.y
    a = atanxy(pd.x - pc.x, pd.y - pc.y)
    pc = cl1[pc.iy]
    pd = cl1[pd.iy]
    tx0 = pc.x
    ty0 = pc.y
    a -= atanxy(pd.x - pc.x, pd.y - pc.y)
    tc = math.cos(a)
    ts = math.sin(a)
  ## transform xy1 -. txy1 (in xy0 coordinate system
  for i1 in range(0, n1):
    x = xy1[i1][0] - tx0
    y = xy1[i1][1] - ty0
    txy1[i1][0] = x * tc - y * ts + tx1
    txy1[i1][1] = x * ts + y * tc + ty1

  ## sort txy1[] by x asc (after transfrm)
  e = 1
  while e:
    e = 0
    i0 = 0
    for i1 in range(1, n1):
      if txy1[i0][0] > txy1[i1][0]:
        e = ix1[i0]
        ix1[i0] = ix1[i1]
        ix1[i1] = e
        e = 1
        a = txy1[i0][0]
        txy1[i0][0] = txy1[i1][0]
        txy1[i1][0] = a
        a = txy1[i0][1]
        txy1[i0][1] = txy1[i1][1]
        txy1[i1][1] = a
      i0 += 1
  ## find match between xy0,txy1 (this can be speeded up by exploiting sorted order)
  ix01 = [0 for i in range(n0)]
  ix10 = [0 for i in range(n1)]
  for i0 in range(0, n0):
    ix01[i0] = -1
  for i1 in range(0, n1):
    ix10[i1] = -1
  for i0 in range(0, n0):
    a = -1.0
    for i1 in range(0, n1):
      x = xy0[i0][0] - txy1[i1][0]
      x *= x
      y = xy0[i0][1] - txy1[i1][1]
      y *= y
      x += y
      if x < max_errr:
        if a < 0.0 or a > x:
          a = x
          ix01[i0] = i1
          ix10[i1] = i0
  ## find the closest stars from unmatched stars
  a = -1.0
  wi0 = -1
  wi1 = -1
  for i0 in range(0, n0):
    if ix01[i0] < 0:
      for i1 in range(0, n1):
        if ix10[i1] < 0:
          x = xy0[i0][0] - txy1[i1][0]
          x *= x
          y = xy0[i0][1] - txy1[i1][1]
          y *= y
          x += y
          if wi0 < 0 or a > x:
            a = x
            wi0 = i0
            wi1 = i1

  # print(xy0[wi0][0], xy0[wi0][1])
  # print(txy1[wi1][0], txy1[wi1][1])

  print(ix0[wi0], ix1[wi1])

compute()