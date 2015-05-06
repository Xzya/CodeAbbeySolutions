#input
# 8
# 13607226
# 13418686
# 23033462
# 18703162
# 19858310
# 24212456
# 22221554
# 18708494
#answer
# 31933179393025 31741201048489 91485035577961 60020114980225 67820973151801 100589526301489 84822350109025 62240186670025

def calculate(s):
  for a in range(2, s):
    if ((s * s - 2 * s * a) % (2 * s - 2 * a)) == 0:
      b = (s * s - 2 * s * a) // (2 * s - 2 * a)
      c = (s - a - b)
      return (a,b,c)
  return 0

def main():
  n = int(input())
  for i in range(0, n):
    s = int(input())
    (a,b,c) = calculate(s)
    print(c*c, end=' ')

if __name__ == '__main__':
    main()
