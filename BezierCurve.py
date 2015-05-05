## input
# 4 40
# 501 458
# 36 485
# 492 746
# 889 512
## answer
# 501 458 467 461 437 464 410 468 386 473 366 478 348 484 334 491 323 498 314 505 308 513 305 520 305 528 307 536 311 544 317 552 326 559 337 566 349 573 364 580 380 586 398 591 417 596 438 600 460 604 484 606 509 608 534 609 561 608 588 607 617 604 646 600 675 594 705 588 735 579 766 569 797 558 828 544 858 529 889 512

def calc_segments(points):
  segments = []
  for i in range(len(points) - 1):
    x = points[i+1][0] - points[i][0]
    y = points[i+1][1] - points[i][1]
    segments.append((x,y))
  return segments

def calc_curve(points, n):
  delta_alpha = 1 / (n - 1)
  alpha = 0
  points_on_curve = [points[0]]
  for i in range(1, n):
    alpha += delta_alpha
    segments = calc_segments(points)
    temp_points = points[:]
    while len(temp_points) > 1:
      intermediate_segments = []
      for j in range(0, len(segments)):
        x = temp_points[j][0] + segments[j][0] * alpha
        y = temp_points[j][1] + segments[j][1] * alpha
        intermediate_segments.append((x,y))
      segments = calc_segments(intermediate_segments)
      temp_points = intermediate_segments[:]
    points_on_curve.append((round(temp_points[0][0]), round(temp_points[0][1])))
  return points_on_curve

def main():
  (m,n) = (int(x) for x in input().split())
  initial = []
  for i in range(m):
    (x,y) = (int(z) for z in input().split())
    initial.append((x,y))
  points_on_curve = calc_curve(initial, n)

  for point in points_on_curve:
    print(point[0],point[1], end=' ')

if __name__ == '__main__':
    main()