#input
# Stand at the pole with the plaque START
# go 420 feet by azimuth 13
# go 160 feet by azimuth 330
# go 140 feet by azimuth 358
# go 200 feet by azimuth 316
# go 500 feet by azimuth 17
# go 80 feet by azimuth 58
# go 20 feet by azimuth 3
# go 400 feet by azimuth 75
# go 360 feet by azimuth 31
# go 120 feet by azimuth 3
# go 400 feet by azimuth 282
# go 500 feet by azimuth 316
# go 460 feet by azimuth 306
# go 300 feet by azimuth 3
# go 420 feet by azimuth 286
# Dig here!
#answer
# -835 3033

import math
import re

def get_coords(start_x, start_y, length, angle):
  x = start_x + length * math.cos(math.radians(angle))
  y = start_y + length * math.sin(math.radians(angle))
  return (x,y)

def azimuth_to_degrees(azimuth):
  degrees = (90 - azimuth) % 360
  return degrees

def main():
  input()
  line = input()
  (x,y) = (0,0)
  while line != 'Dig here!':
    match = re.findall('\d+', line)
    (length,azimuth) = (int(z) for z in match)
    (x,y) = get_coords(x,y,length,azimuth_to_degrees(azimuth))
    line = input()
  print(round(x),round(y))

if __name__ == '__main__':
    main()
