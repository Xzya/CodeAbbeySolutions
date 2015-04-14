import math
import operator
import random

class Problem:
  __lengtha = 0
  __lengthb = 0
  __initial_vectora = []
  __initial_vectorb = []

  def getInitialVectorA(self):
    return self.__initial_vectora
  def setInitialVectorA(self,a):
    self.__initial_vectora = a
    self.__lengtha = len(self.__initial_vectora)
  def getInitialVectorB(self):
    return self.__initial_vectorb
  def setInitialVectorB(self,b):
    self.__initial_vectorb = b
    self.__lengthb = len(self.__initial_vectorb)
  def getLengthA(self):
    return self.__lengtha
  def getLengthB(self):
    return self.__lengthb

def distance_between_points(a, b):
  dist = ((b[0] - a[0])**2 + (b[1] - a[1])**2)**.5
  return dist

def calculate_signature(array):
  signature = []
  for i in range(0, len(array)):
    current_vector = array[i]
    distances = []
    for j in range(0, len(array)):
      dist = distance_between_points(current_vector, array[j])
      if dist == 0:
        continue
      distances.append([dist, array[j]])
    distances = sorted(distances, key=operator.itemgetter(0))

    dists = [x[0] for x in distances[:10]]
    points = [x[1] for x in distances[:10]]

    signature.append([current_vector, dists, points])#, distances[:10][1]])
  return signature

def score(a, b):
  if a == b:
    return 0
  else:
    return (a-b)**2

##init problem
problem = Problem()
problem.setInitialVectorA([(-10.1, -20.8), (-16.8, -12.5), (1.0, 26.8), (11.5, 44.7), (-3.8, -47.5), (36.7, -23.1), (-9.5, 19.5), (13.0, -42.1), (-9.9, 42.2), (16.0, 35.5), (-2.2, 47.0), (16.6, -46.3), (1.2, 26.0), (-28.3, -35.3), (-13.7, 42.8), (-28.7, -3.1), (-11.3, 13.3), (33.2, 21.8), (-16.4, 0.4), (8.1, -11.5), (31.3, -34.6), (46.4, 3.5), (5.4, 38.8), (-33.2, -26.2), (-44.6, 15.0), (-6.8, 46.2), (-19.0, 43.7), (9.9, 9.9), (34.5, 8.1), (-14.2, 21.5), (8.3, 42.3), (16.4, 21.7), (9.7, -47.7), (38.7, -25.8), (43.6, 4.1), (22.5, -42.9), (20.6, -32.6), (29.6, -24.3), (12.1, 44.9), (4.3, 27.6), (41.8, 8.2), (-3.0, 42.0), (38.0, -28.2), (41.4, 19.9), (-3.9, 49.5), (-11.5, -22.2), (38.0, -27.8), (30.4, -21.5), (15.5, -5.6), (-42.5, -4.2), (26.7, -16.2), (28.9, -31.5), (27.5, 25.5), (35.6, 29.1), (-0.5, -46.7), (0.9, -39.2), (-9.5, -14.1), (31.5, -26.8), (28.5, 33.8), (-3.5, 45.3), (-28.5, 0.3), (24.5, 40.0), (26.0, 32.2), (27.5, 15.2), (-2.2, 30.8), (16.3, -6.8), (11.1, -39.5), (31.1, -15.0), (8.0, -17.9), (33.3, -31.9), (-9.9, 41.9), (18.0, -23.3), (37.1, 17.0), (6.2, -1.6), (9.6, -9.6), (36.0, 4.8), (-15.5, -23.4), (36.9, -18.2), (19.9, 13.4), (-11.1, 23.8), (35.1, 7.8), (27.9, -9.4), (12.8, 2.9), (9.4, 9.7), (-38.3, 25.8), (16.4, 1.1), (30.3, 17.1), (11.0, 5.7), (-17.9, 39.2), (-25.7, -24.1), (14.4, 17.9), (26.6, -12.7), (-0.8, 16.1), (31.4, -17.4), (-0.7, 29.3), (-44.1, 7.1), (31.4, 18.5), (10.3, -36.9), (-20.3, 23.4), (17.3, -34.9), (43.8, 17.6), (-39.6, -29.1)])
problem.setInitialVectorB([(9.0, -6.8), (37.1, 30.8), (-5.1, -45.3), (20.2, -36.0), (12.1, -15.9), (14.5, -47.8), (16.7, 39.3), (-23.2, 40.4), (44.8, -15.8), (21.2, -26.5), (-46.5, -9.0), (-14.2, -36.8), (-19.1, -42.6), (16.8, -2.8), (23.1, -32.9), (-9.7, 6.2), (1.2, 14.8), (45.9, 13.0), (18.3, 23.5), (24.9, -40.5), (-4.9, -39.5), (6.2, -40.8), (-37.6, -19.0), (29.4, 8.5), (40.8, -1.7), (-43.7, 20.0), (-16.6, -15.9), (8.5, -31.5), (-20.6, -15.0), (27.5, -36.4), (45.5, 20.4), (-5.5, -42.1), (-27.0, 32.8), (-45.5, -6.9), (25.7, 39.6), (36.5, 30.9), (42.9, 12.8), (17.7, 25.6), (8.2, 40.6), (-1.7, 28.1), (14.0, -44.0), (6.5, 23.9), (16.5, 39.0), (19.2, -9.4), (38.8, -12.9), (18.5, -41.2), (21.8, 19.6), (-22.1, 9.2), (39.2, -2.4), (17.0, -6.1), (28.3, -0.5), (38.4, -12.3), (11.7, 12.1), (38.1, -15.9), (-22.4, -41.7), (35.9, 20.7), (-16.1, 39.1), (-10.8, -9.9), (8.0, -15.4), (23.7, 38.8), (17.4, 1.5), (2.5, -21.8), (2.2, -41.2), (-34.6, 15.1), (-37.4, -8.7), (18.5, 20.5), (-10.7, -48.6), (18.1, -38.1), (32.5, 30.4), (22.6, 35.7), (44.3, -20.3), (2.7, 23.4), (28.3, 28.8), (-14.7, -15.4), (-5.5, 47.9), (-46.0, 0.0), (15.2, -16.3), (-22.0, 43.5), (24.0, -30.7), (-30.4, 25.7), (25.5, 42.7), (45.1, -5.9), (17.9, 1.4), (9.5, 45.1), (-18.5, 44.0), (21.3, 41.2), (5.8, -16.3), (-16.4, -4.9), (40.9, 6.3), (-29.9, -10.5), (17.6, -46.5), (44.0, 0.2), (35.8, -2.7), (-44.4, -8.0), (5.8, 19.3), (25.8, 6.1), (-34.9, -34.6), (-20.2, 12.0), (13.6, 41.7), (24.0, -24.3), (19.6, -29.6), (18.3, 19.7)])

##calculate the signatures
# [vector,[signature..], [to_vector..]]
signaturea = calculate_signature(problem.getInitialVectorA())
signatureb = calculate_signature(problem.getInitialVectorB())

# print(signaturea)
# print(signatureb)


##
def compare_signatures(signaturea, signatureb):
  # sig_lista will be X
  sig_lista = signaturea[:]
  # sig_listb will be Y
  sig_listb = signatureb[:]

  whichList = None
  prevWhichList = None
  prev = None
  Bm, Bf = 0, 0
  p = 20
  firstIteration = True
  # while X and Y are not empty

  while len(sig_lista) + len(sig_listb) != 0:
    # Call the element at the front of X x, and the element at the front of Y y.
    # Let z be the smaller of x and y, and set whichList to the ID of the list (X or Y) that z came from.
    if len(sig_lista) > 0:
      x = sig_lista[0]
    else:
      x = float('inf')
    if len(sig_listb) > 0:
      y = sig_listb[0]
    else:
      y = float('inf')

    if x < y:
      z = x
      whichList = sig_lista
    # elif y < x:
    else:
      z = y
      whichList = sig_listb

    # Remove the first element (z) from the list named by whichList.
    del whichList[0]

    # If whichList == prevWhichList (i.e. if the previous smallest number,
    # prev, was also from the same list as z), or if this is the first iteration,
    # then set newBm = min(Bf + p, Bm) + p.
    if whichList == prevWhichList or firstIteration:
      if (firstIteration):
        newBm = min(Bf + p, Bm)
      else:
        newBm = min(Bf + p, Bm) + p
    # Otherwise, it's possible to match z with the previous number written out,
    # so set newBm = Bf + score(z, prev).
    else:
      newBm = Bf + score(z, prev)

    # Set Bf = min(Bf + p, Bm).
    Bf = min(Bf + p, Bm)

    #Set Bm = newBm.
    Bm = newBm

    # Set prev = z and prevWhichList = whichList.
    prev = z
    prevWhichList = whichList

    firstIteration = False

  # If X and Y are both empty, then halt. The final score is min(Bf + p, Bm)
  final_score = min(Bf + p, Bm)
  print(final_score)
  return final_score

def do_compare_signatures(signaturea, signatureb):
  for i in range(0, len(signaturea)):
    for j in range(0, len(signatureb)):
      # [vector,[signature..], [to_vector..]]
      score = compare_signatures(signaturea[i][1][:], signatureb[j][1][:])
      # break


## TEST
a = [10, 20, 30, 40]
b = [11, 18, 41, 50]
c = [20, 30, 40, 10]
compare_signatures(a, b)
compare_signatures(a, a)
compare_signatures(a, c)
##
# do_compare_signatures(signaturea, signatureb)