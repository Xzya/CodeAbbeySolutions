#input
# http://www.shodor.org/interactivate/activities/SimplePlot/
# http://en.wikipedia.org/wiki/Rotation_matrix
# http://reference.wolfram.com/language/ref/RotationMatrix.html
# http://www.wolframalpha.com/input/?i=RotationMatrix%5B90+Degree%5D
# http://www.wolframalpha.com/input/?i=%7B%7B0%2C+-1%7D%2C+%7B1%2C+0%7D%7D+*+%7B1%2C+1%7D
# http://nghiaho.com/?page_id=671
# http://math.stackexchange.com/questions/180418/calculate-rotation-matrix-to-align-vector-a-to-vector-b-in-3d
# after you find the rotation matrix, multiply each vector with the matrix
# calculate the rotation matrix by centroids ?
# dot product gives angle
# cross product gives length?TODO TODO cross product a1a2 b1b2 are actually lengths not points?
# a 8.994117647058818 2.423529411764707
# b 7.9529411764705875 -0.6049019607843146
# |a x b| = a1*b2 - b1*a2 = |-24.7147462514417647991234140715053|
#  a . b = ||a||||b|| cos 0 = a1*b1 + a2*b2 = 70.0636908881199004800230680507528
# if a . b = 0  -> theta = pi/2
# if a . b > 0  -> theta < pi/2
# if a . b < 0  -> theta > pi/2

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

def rotation_matrix(a, b):
  dp = dot_product(a,b)
  cp = cross_product(a,b)

  #(dp, -cp),(cp,dp) ????
  # R = (normalize((dp, cp)), normalize((-cp, dp)))  ##TODO good
  R = (normalize((dp, cp)), normalize((-cp, dp)))

  return R

def multiply_mv(m, v):
  result = [0,0]
  for i in range(0, 2):
    for j in range(0, 2):
      result[i] += m[i][j] * v[j]

  return tuple(result)

def subtract_vectors(a, b):
  result = (b[0] - a[0], b[1] - a[1])
  return result

def add_vectors(a, b):
  result = (a[0] + b[0], a[1] + b[1])
  return result

def transform_vector(v, a, b):
  R = rotation_matrix(a, b)
  # print(R)
  mv = multiply_mv(R, a)
  t = subtract_vectors(mv, b)

  new_mv = multiply_mv(R, v)
  new_v = add_vectors(new_mv, t)

  return new_v

def transform_vector_degree(v, degree):
  R = rotation_matrix_degree(degree)
  mv = multiply_mv(R, v)
  return mv

def calculate_distance(arrays):
  arrays_lengths = (len(arrays[0]), len(arrays[1]))
  index = -1
  if arrays_lengths[0] < arrays_lengths[1]:
    index = 0
  else:
    index = 1
  distance = 0
  for i in range(0, len(arrays[index])):
    # lengtha = dist_to_origin(arrays[0][i])
    # lengthb = dist_to_origin(arrays[1][i])
    # if lengtha > 30 or lengthb > 30:
    #   continue
    distance += ((arrays[1][i][0] - arrays[0][i][0])**2 + (arrays[1][i][1] - arrays[0][i][1])**2)**.5
  return distance

def calculate_distance_points(a, b):
  dist = ((b[0] - a[0])**2 + (b[1] - a[1])**2)**.5
  return dist

def rotation_matrix_degree(degree):
  # rad = (180 * degree) / math.pi
  rad = degree * math.pi/180
  if degree > 0:
    R = (normalize((math.cos(rad), -math.sin(rad))), normalize((math.sin(rad), math.cos(rad))))
  else:
    R = (normalize((math.cos(rad), math.sin(rad))), normalize((-math.sin(rad), math.cos(rad))))
  return R

def find_centroid(a):
  averagex = 0
  averagey = 0
  for i in range(0, len(a)):
    averagex += a[i][0]
    averagey += a[i][1]
  averagex /= len(a)
  averagey /= len(a)
  return (averagex, averagey)

# a = (5.4,38.8)
# b = (28.3,28.8)
# a = (8.994117647058818, 2.423529411764707)
# b = (7.9529411764705875, -0.6049019607843146)
# v = (6.00, 48.00)
# print(transform_vector(v, a, b))

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

# n = []
# sections = []

problem = Problem()
problem.setInitialVectorA([(-10.1, -20.8), (-16.8, -12.5), (1.0, 26.8), (11.5, 44.7), (-3.8, -47.5), (36.7, -23.1), (-9.5, 19.5), (13.0, -42.1), (-9.9, 42.2), (16.0, 35.5), (-2.2, 47.0), (16.6, -46.3), (1.2, 26.0), (-28.3, -35.3), (-13.7, 42.8), (-28.7, -3.1), (-11.3, 13.3), (33.2, 21.8), (-16.4, 0.4), (8.1, -11.5), (31.3, -34.6), (46.4, 3.5), (5.4, 38.8), (-33.2, -26.2), (-44.6, 15.0), (-6.8, 46.2), (-19.0, 43.7), (9.9, 9.9), (34.5, 8.1), (-14.2, 21.5), (8.3, 42.3), (16.4, 21.7), (9.7, -47.7), (38.7, -25.8), (43.6, 4.1), (22.5, -42.9), (20.6, -32.6), (29.6, -24.3), (12.1, 44.9), (4.3, 27.6), (41.8, 8.2), (-3.0, 42.0), (38.0, -28.2), (41.4, 19.9), (-3.9, 49.5), (-11.5, -22.2), (38.0, -27.8), (30.4, -21.5), (15.5, -5.6), (-42.5, -4.2), (26.7, -16.2), (28.9, -31.5), (27.5, 25.5), (35.6, 29.1), (-0.5, -46.7), (0.9, -39.2), (-9.5, -14.1), (31.5, -26.8), (28.5, 33.8), (-3.5, 45.3), (-28.5, 0.3), (24.5, 40.0), (26.0, 32.2), (27.5, 15.2), (-2.2, 30.8), (16.3, -6.8), (11.1, -39.5), (31.1, -15.0), (8.0, -17.9), (33.3, -31.9), (-9.9, 41.9), (18.0, -23.3), (37.1, 17.0), (6.2, -1.6), (9.6, -9.6), (36.0, 4.8), (-15.5, -23.4), (36.9, -18.2), (19.9, 13.4), (-11.1, 23.8), (35.1, 7.8), (27.9, -9.4), (12.8, 2.9), (9.4, 9.7), (-38.3, 25.8), (16.4, 1.1), (30.3, 17.1), (11.0, 5.7), (-17.9, 39.2), (-25.7, -24.1), (14.4, 17.9), (26.6, -12.7), (-0.8, 16.1), (31.4, -17.4), (-0.7, 29.3), (-44.1, 7.1), (31.4, 18.5), (10.3, -36.9), (-20.3, 23.4), (17.3, -34.9), (43.8, 17.6), (-39.6, -29.1)])
problem.setInitialVectorB([(9.0, -6.8), (37.1, 30.8), (-5.1, -45.3), (20.2, -36.0), (12.1, -15.9), (14.5, -47.8), (16.7, 39.3), (-23.2, 40.4), (44.8, -15.8), (21.2, -26.5), (-46.5, -9.0), (-14.2, -36.8), (-19.1, -42.6), (16.8, -2.8), (23.1, -32.9), (-9.7, 6.2), (1.2, 14.8), (45.9, 13.0), (18.3, 23.5), (24.9, -40.5), (-4.9, -39.5), (6.2, -40.8), (-37.6, -19.0), (29.4, 8.5), (40.8, -1.7), (-43.7, 20.0), (-16.6, -15.9), (8.5, -31.5), (-20.6, -15.0), (27.5, -36.4), (45.5, 20.4), (-5.5, -42.1), (-27.0, 32.8), (-45.5, -6.9), (25.7, 39.6), (36.5, 30.9), (42.9, 12.8), (17.7, 25.6), (8.2, 40.6), (-1.7, 28.1), (14.0, -44.0), (6.5, 23.9), (16.5, 39.0), (19.2, -9.4), (38.8, -12.9), (18.5, -41.2), (21.8, 19.6), (-22.1, 9.2), (39.2, -2.4), (17.0, -6.1), (28.3, -0.5), (38.4, -12.3), (11.7, 12.1), (38.1, -15.9), (-22.4, -41.7), (35.9, 20.7), (-16.1, 39.1), (-10.8, -9.9), (8.0, -15.4), (23.7, 38.8), (17.4, 1.5), (2.5, -21.8), (2.2, -41.2), (-34.6, 15.1), (-37.4, -8.7), (18.5, 20.5), (-10.7, -48.6), (18.1, -38.1), (32.5, 30.4), (22.6, 35.7), (44.3, -20.3), (2.7, 23.4), (28.3, 28.8), (-14.7, -15.4), (-5.5, 47.9), (-46.0, 0.0), (15.2, -16.3), (-22.0, 43.5), (24.0, -30.7), (-30.4, 25.7), (25.5, 42.7), (45.1, -5.9), (17.9, 1.4), (9.5, 45.1), (-18.5, 44.0), (21.3, 41.2), (5.8, -16.3), (-16.4, -4.9), (40.9, 6.3), (-29.9, -10.5), (17.6, -46.5), (44.0, 0.2), (35.8, -2.7), (-44.4, -8.0), (5.8, 19.3), (25.8, 6.1), (-34.9, -34.6), (-20.2, 12.0), (13.6, 41.7), (24.0, -24.3), (19.6, -29.6), (18.3, 19.7)])

# n = [102,102]
# sections = [[(-10.1, -20.8), (-16.8, -12.5), (1.0, 26.8), (11.5, 44.7), (-3.8, -47.5), (36.7, -23.1), (-9.5, 19.5), (13.0, -42.1), (-9.9, 42.2), (16.0, 35.5), (-2.2, 47.0), (16.6, -46.3), (1.2, 26.0), (-28.3, -35.3), (-13.7, 42.8), (-28.7, -3.1), (-11.3, 13.3), (33.2, 21.8), (-16.4, 0.4), (8.1, -11.5), (31.3, -34.6), (46.4, 3.5), (5.4, 38.8), (-33.2, -26.2), (-44.6, 15.0), (-6.8, 46.2), (-19.0, 43.7), (9.9, 9.9), (34.5, 8.1), (-14.2, 21.5), (8.3, 42.3), (16.4, 21.7), (9.7, -47.7), (38.7, -25.8), (43.6, 4.1), (22.5, -42.9), (20.6, -32.6), (29.6, -24.3), (12.1, 44.9), (4.3, 27.6), (41.8, 8.2), (-3.0, 42.0), (38.0, -28.2), (41.4, 19.9), (-3.9, 49.5), (-11.5, -22.2), (38.0, -27.8), (30.4, -21.5), (15.5, -5.6), (-42.5, -4.2), (26.7, -16.2), (28.9, -31.5), (27.5, 25.5), (35.6, 29.1), (-0.5, -46.7), (0.9, -39.2), (-9.5, -14.1), (31.5, -26.8), (28.5, 33.8), (-3.5, 45.3), (-28.5, 0.3), (24.5, 40.0), (26.0, 32.2), (27.5, 15.2), (-2.2, 30.8), (16.3, -6.8), (11.1, -39.5), (31.1, -15.0), (8.0, -17.9), (33.3, -31.9), (-9.9, 41.9), (18.0, -23.3), (37.1, 17.0), (6.2, -1.6), (9.6, -9.6), (36.0, 4.8), (-15.5, -23.4), (36.9, -18.2), (19.9, 13.4), (-11.1, 23.8), (35.1, 7.8), (27.9, -9.4), (12.8, 2.9), (9.4, 9.7), (-38.3, 25.8), (16.4, 1.1), (30.3, 17.1), (11.0, 5.7), (-17.9, 39.2), (-25.7, -24.1), (14.4, 17.9), (26.6, -12.7), (-0.8, 16.1), (31.4, -17.4), (-0.7, 29.3), (-44.1, 7.1), (31.4, 18.5), (10.3, -36.9), (-20.3, 23.4), (17.3, -34.9), (43.8, 17.6), (-39.6, -29.1)],[(9.0, -6.8), (37.1, 30.8), (-5.1, -45.3), (20.2, -36.0), (12.1, -15.9), (14.5, -47.8), (16.7, 39.3), (-23.2, 40.4), (44.8, -15.8), (21.2, -26.5), (-46.5, -9.0), (-14.2, -36.8), (-19.1, -42.6), (16.8, -2.8), (23.1, -32.9), (-9.7, 6.2), (1.2, 14.8), (45.9, 13.0), (18.3, 23.5), (24.9, -40.5), (-4.9, -39.5), (6.2, -40.8), (-37.6, -19.0), (29.4, 8.5), (40.8, -1.7), (-43.7, 20.0), (-16.6, -15.9), (8.5, -31.5), (-20.6, -15.0), (27.5, -36.4), (45.5, 20.4), (-5.5, -42.1), (-27.0, 32.8), (-45.5, -6.9), (25.7, 39.6), (36.5, 30.9), (42.9, 12.8), (17.7, 25.6), (8.2, 40.6), (-1.7, 28.1), (14.0, -44.0), (6.5, 23.9), (16.5, 39.0), (19.2, -9.4), (38.8, -12.9), (18.5, -41.2), (21.8, 19.6), (-22.1, 9.2), (39.2, -2.4), (17.0, -6.1), (28.3, -0.5), (38.4, -12.3), (11.7, 12.1), (38.1, -15.9), (-22.4, -41.7), (35.9, 20.7), (-16.1, 39.1), (-10.8, -9.9), (8.0, -15.4), (23.7, 38.8), (17.4, 1.5), (2.5, -21.8), (2.2, -41.2), (-34.6, 15.1), (-37.4, -8.7), (18.5, 20.5), (-10.7, -48.6), (18.1, -38.1), (32.5, 30.4), (22.6, 35.7), (44.3, -20.3), (2.7, 23.4), (28.3, 28.8), (-14.7, -15.4), (-5.5, 47.9), (-46.0, 0.0), (15.2, -16.3), (-22.0, 43.5), (24.0, -30.7), (-30.4, 25.7), (25.5, 42.7), (45.1, -5.9), (17.9, 1.4), (9.5, 45.1), (-18.5, 44.0), (21.3, 41.2), (5.8, -16.3), (-16.4, -4.9), (40.9, 6.3), (-29.9, -10.5), (17.6, -46.5), (44.0, 0.2), (35.8, -2.7), (-44.4, -8.0), (5.8, 19.3), (25.8, 6.1), (-34.9, -34.6), (-20.2, 12.0), (13.6, 41.7), (24.0, -24.3), (19.6, -29.6), (18.3, 19.7)]]

# for i in range(0, 2):
#   maxj = len(sections[i])
#   j = 0
#   while j < maxj:
#     dist = (sections[i][j][0]**2 + sections[i][j][1]**2)**.5
#     if dist > 30:
#       del sections[i][j]
#       j -= 1
#       maxj -= 1
#     j += 1
#
# print(sections[0])
# print(sections[1])

###############################
# for i in range(0, 2):
#   n.append(int(input()))
#
#   section = []
#   for j in range(0, n[i]):
#     (x, y) = (float(x) for x in input().split())
#     # since some points on the edge might be absent,
#     # ignore all points that have a length > 40
#     # if ((x**2 + y**2)**.5 <= 40):
#     section.append((x,y))
#
#   sections.append(section)
################################


# print(len(sections[0]), len(sections[1]))


################################################################
## distance minimization
# calculate sections centroids
# averages = []
# for i in range(0, 2):
#
#   averagex = 0
#   averagey = 0
#
#   for j in range(0, n[i]):
#     averagex += sections[i][j][0]
#     averagey += sections[i][j][1]
#
#   averagex /= len(sections[i])
#   averagey /= len(sections[i])
#
#   averages.append((averagex, averagey))
#   # print(averagex, averagey)
#
# # #align the centroids
# R = rotation_matrix(averages[0], averages[1])
# rotated_vectors = []
# for i in range(0, n[0]):
#   rotated_vectors.append(transform_vector(sections[0][i], averages[0], averages[1]))
#
#
# #distance minimization
# distances = []
# temp_vector = rotated_vectors#sections[0]#rotated_vectors
# for i in range(1, 360):
#   rotated_vector = []
#   for j in range(0, n[0]):
#     rotated_vector.append(transform_vector_degree(temp_vector[j], i))
#
#   distance = calculate_distance((rotated_vector, sections[1]))
#
#   distances.append((i,distance,rotated_vector))
#
#   temp_vector = rotated_vector
#
#
#
# distances = sorted(distances, key=operator.itemgetter(1))
#
# print(distances[0][2])
# for i in range(0, 20):
#   toString = (str(distances[i][2]).replace('[','(')).replace(']',')')
#   print(toString)
#   # print(distances[i][0], distances[i][2])
######################################################################


#####################################################################
#search for shape
# sort the point by distance from origin
def dist_to_origin(a):
  dist = (a[0]**2 + a[1]**2)**.5
  return dist

def find_nearest_neighbors(p, array, num_of_neigh):
  # [[distance, to_point]]
  dist_points = []
  for i in range(0, len(array)):
    dist = calculate_distance_points(p, array[i])
    #if dist is 0 it's the same point, so ignore it
    if (dist == 0):
      continue
    list_entry = [dist, array[i]]
    dist_points.append(list_entry)

  #sort by distance
  dist_points = sorted(dist_points, key=operator.itemgetter(0))
  neighbors = dist_points[:10]
  # print('dist_points', neighbors)
  return  neighbors

def has_similar_neigh(neigha, neighb, tolerance=0.2, min_matches=10):
  matches = 0
  for i in range(0, len(neigha)):
    for j in range(0, len(neighb)):
      # if neighb-telorance <= neigha <= neighb+tolerance
      if neighb[j][0]-tolerance <= neigha[i][0] and neigha[i][0] <= neighb[j][0]+tolerance:
        matches += 1
  if matches >= min_matches:
    return (True, matches)
  return (False, 0)

sorted_by_dist_origina = sorted(problem.getInitialVectorA(), key=dist_to_origin)
sorted_by_dist_originb = sorted(problem.getInitialVectorB(), key=dist_to_origin)
sorted_arrays = [sorted_by_dist_origina, sorted_by_dist_originb]

def already_matched(point, matched_points):
  for m in matched_points:
    if point == m.getPointInA():
      return True
  return False

class Point:
  __x = None
  __y = None
  def setX(self,x):
    self.__x = x
  def setY(self,y):
    self.__y = y
  def setPoint(self,x):
    self.setX(x[0])
    self.setY(x[1])
  def getPoint(self):
    return (self.getX(), self.getY())
  def getX(self):
    return self.__x
  def getY(self):
    return self.__y
  def __init__(self,x,y):
    self.setX(x)
    self.setY(y)

class Match:
  __pointInA = None
  __pointInB = None
  __numOfMatches = 0
  def setPointInA(self, a):
    self.__pointInA = Point(a[0], a[1])
  def setPointInB(self, b):
    self.__pointInB = Point(b[0], b[1])
  def setNumOfMatches(self, n):
    self.__numOfMatches = n
  def getPointInA(self):
    return self.__pointInA
  def getPointInB(self):
    return self.__pointInB
  def getNumOfMatches(self):
    return self.__numOfMatches
  def __init__(self, a, b, numOfMatches):
    self.setPointInA(a)
    self.setPointInB(b)
    self.setNumOfMatches(numOfMatches)

matched_points = []
while len(matched_points) < 5:
  # chose the closest point to the origin as the observed point
  # then find n closest neighbors
  observed_point = sorted_by_dist_origina[random.randint(0, len(sorted_by_dist_origina) - 1)]
  dist = dist_to_origin(observed_point)
  if dist > 30:
    continue
  while already_matched(observed_point, matched_points):
    observed_point = sorted_by_dist_origina[random.randint(0, len(sorted_by_dist_origina) - 1)]
  observed_point_neigh = find_nearest_neighbors(observed_point, sorted_by_dist_origina, 10)

  # now search for points in the other array with the same pattern
  matches = []
  for i in range(0, problem.getLengthB()):
    point = problem.getInitialVectorB()[i]
    point_neigh = find_nearest_neighbors(point, problem.getInitialVectorB(), 20)

    (is_match, number_of_matches) = has_similar_neigh(observed_point_neigh, point_neigh, 0.2, 10)
    if is_match:
      mat = Match(observed_point, point, number_of_matches)
      matches.append(mat)
  #

  if not matches:
    continue

  best_match = sorted(matches, key=lambda x: x.getNumOfMatches())
  matched_points.append(best_match[0])


clustera = [None] * len(matched_points)
clusterb = [None] * len(matched_points)
for i in range(0, len(matched_points)):
  clustera[i] = matched_points[i].getPointInA().getPoint()
  clusterb[i] = matched_points[i].getPointInB().getPoint()
centa = find_centroid(clustera)
centb = find_centroid(clusterb)

## the first match should be the right one
## now calculate the rotation matrix and rotate the vectors
# rotated_vectors = []
# for v in sorted_by_dist_origina:
#   x = transform_vector(v, centa, centb)
#   rotated_vectors.append(x)

for m in matched_points:
  x = transform_vector(m.getPointInA().getPoint(), centa, centb)
  m.setPointInA(x)

matched_points_in_a = []
matched_points_in_b = []
for u in range(0, len(matched_points)):
  matched_points_in_a.append(matched_points[u].getPointInA().getPoint())
  matched_points_in_b.append(matched_points[u].getPointInB().getPoint())

dist = calculate_distance((matched_points_in_a, matched_points_in_b))
print(dist)

# ## the rotation and alignment might be a bit off
# ## we'll brute force by moving it along the axis and then rotate
# ## until it's in the right place
distance = dist
moved_dist = distance
moved_vectors = matched_points_in_a
j = 0
# while j < 1000:
while moved_dist > 2:
  moving = True
  while moving:
    moving = False
    while True:
      ## move right
      new_v = []
      for v in moved_vectors:
        new_v.append(add_vectors(v, (.5,0)))
      new_dist = calculate_distance((new_v, matched_points_in_b))
      if new_dist < moved_dist:
        moved_vectors = new_v
        moved_dist = new_dist
        moving = True
      else:
        break
    while True:
      ## move up
      new_v = []
      for v in moved_vectors:
        new_v.append(add_vectors(v, (0,.5)))
      new_dist = calculate_distance((new_v, matched_points_in_b))
      if new_dist < moved_dist:
        moved_vectors = new_v
        moved_dist = new_dist
        moving = True
      else:
        break
    while True:
      ## move left
      new_v = []
      for v in moved_vectors:
        new_v.append(add_vectors(v, (-.5,0)))
      new_dist = calculate_distance((new_v, matched_points_in_b))
      if new_dist < moved_dist:
        moved_vectors = new_v
        moved_dist = new_dist
        moving = True
      else:
        break
    while True:
      ## move down
      new_v = []
      for v in moved_vectors:
        new_v.append(add_vectors(v, (0,-.5)))
      new_dist = calculate_distance((new_v, matched_points_in_b))
      if new_dist < moved_dist:
        moved_vectors = new_v
        moved_dist = new_dist
        moving = True
      else:
        break

  ## rotate
  k = 0
  while k < 1:
    k = 1
    ## rotate clockwise
    new_v = []
    for v in moved_vectors:
      new_v.append(transform_vector_degree(v, .01))
    new_dist = calculate_distance((new_v, matched_points_in_b))
    if new_dist < moved_dist:
      moved_vectors = new_v
      moved_dist = new_dist
    else:
      break
  k = 0
  while k < 1:
    k = 1
    ## rotate anti-clockwise
    new_v = []
    for v in moved_vectors:
      new_v.append(transform_vector_degree(v, -.01))
    new_dist = calculate_distance((new_v, matched_points_in_b))
    if new_dist < moved_dist:
      moved_vectors = new_v
      moved_dist = new_dist
    else:
      break

  j += 1
  # break

print(moved_vectors)
print(distance,moved_dist)

# temp_points_in_a = [x.getPoint() for x in matched_points_in_a]
centa2 = find_centroid(matched_points_in_a)
centb2 = find_centroid(moved_vectors)

final_vector = []
fine_vector = []
supafine_vector = []
cent_original = find_centroid(problem.getInitialVectorA())
for v in problem.getInitialVectorA():
  fine_vector.append(subtract_vectors(centa, v))

for v in fine_vector:
  supafine_vector.append(transform_vector(v, centa, centb2))

for v in supafine_vector:
  final_vector.append(add_vectors(v, centa))
# for v in problem.getInitialVectorA():
#   final_vector.append(transform_vector(v, centa, centb))

print(calculate_distance((final_vector, problem.getInitialVectorB())))
print(final_vector)


# # ## the rotation and alignment might be a bit off
# # ## we'll brute force by moving it along the axis and then rotate
# # ## until it's in the right place
# distance = calculate_distance((rotated_vectors, sections[1]))
# moved_vectors = rotated_vectors[:]
# moved_dist = distance
# j = 0
# while j < 1000:
# # while moved_dist > 100:
#   moving = True
#   while moving:
#     moving = False
#     while True:
#       ## move right
#       new_v = []
#       for v in moved_vectors:
#         new_v.append(add_vectors(v, (.5,0)))
#       new_dist = calculate_distance((new_v, sections[1]))
#       if new_dist < moved_dist:
#         moved_vectors = new_v
#         moved_dist = new_dist
#         moving = True
#       else:
#         break
#     while True:
#       ## move up
#       new_v = []
#       for v in moved_vectors:
#         new_v.append(add_vectors(v, (0,.5)))
#       new_dist = calculate_distance((new_v, sections[1]))
#       if new_dist < moved_dist:
#         moved_vectors = new_v
#         moved_dist = new_dist
#         moving = True
#       else:
#         break
#     while True:
#       ## move left
#       new_v = []
#       for v in moved_vectors:
#         new_v.append(add_vectors(v, (-.5,0)))
#       new_dist = calculate_distance((new_v, sections[1]))
#       if new_dist < moved_dist:
#         moved_vectors = new_v
#         moved_dist = new_dist
#         moving = True
#       else:
#         break
#     while True:
#       ## move down
#       new_v = []
#       for v in moved_vectors:
#         new_v.append(add_vectors(v, (0,-.5)))
#       new_dist = calculate_distance((new_v, sections[1]))
#       if new_dist < moved_dist:
#         moved_vectors = new_v
#         moved_dist = new_dist
#         moving = True
#       else:
#         break
#
#   ## rotate
#   k = 0
#   while k < 1:
#     k = 1
#     ## rotate clockwise
#     new_v = []
#     for v in moved_vectors:
#       new_v.append(transform_vector_degree(v, .01))
#     new_dist = calculate_distance((new_v, sections[1]))
#     if new_dist < moved_dist:
#       moved_vectors = new_v
#       moved_dist = new_dist
#     else:
#       break
#   k = 0
#   while k < 1:
#     k = 1
#     ## rotate anti-clockwise
#     new_v = []
#     for v in moved_vectors:
#       new_v.append(transform_vector_degree(v, -.01))
#     new_dist = calculate_distance((new_v, sections[1]))
#     if new_dist < moved_dist:
#       moved_vectors = new_v
#       moved_dist = new_dist
#     else:
#       break
#
#   j += 1
#   # break
#
# print(moved_vectors)
# print(distance,moved_dist)















# print("matches", matches)
#
# a = (-3.9, 49.5)
# b = (25.5, 42.7)
#
# ##
# averages = []
# for i in range(0, 2):
#
#   averagex = 0
#   averagey = 0
#
#   for j in range(0, n[i]):
#     averagex += sections[i][j][0]
#     averagey += sections[i][j][1]
#
#   averagex /= len(sections[i])
#   averagey /= len(sections[i])
#
#   averages.append((averagex, averagey))
#   # print(averagex, averagey)
#
# #move centroid to origin
# origin = []
# for i in range(0, n[0]):
#   origin.append(subtract_vectors(averages[0], sections[0][i]))
#
# print("origin", origin)
#
# # #align the centroids
# # R = rotation_matrix(a, b)
# # rotated_vectors = []
# # for i in range(0, n[0]):
# #   rotated_vectors.append(transform_vector(sections[0][i], averages[0], averages[1]))
# ##
#
#
# # transform vectors
# resulted_vectors = []
# for v in origin:
#   resulted_vectors.append(transform_vector(v, a, b))
#
# #move centroid back
# origin = []
# for i in range(0, n[0]):
#   origin.append(add_vectors(averages[0], resulted_vectors[i]))
#
# print(origin)
# ##############################################################################