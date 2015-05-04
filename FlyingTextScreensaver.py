#input
# 40 18 7

class ScreenSaver():
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.x = 0
    self.y = 0
    self.left = False
    self.right = True
    self.up = False
    self.down = True

  def setText(self,text):
    self.text = text
    self.length = len(text)

  def update(self):
    if self.left:
      self.go_left()
    elif self.right:
      self.go_right()
    if self.up:
      self.go_up()
    elif self.down:
      self.go_down()

  def go_left(self):
    if self.x - 1 >= 0:
      self.x -= 1
    else:
      self.left = False
      self.right = True
      self.go_right()

  def go_right(self):
    if self.x + self.length < self.width:
      self.x += 1
    else:
      self.left = True
      self.right = False
      self.go_left()

  def go_up(self):
    if self.y - 1 >= 0:
      self.y -= 1
    else:
      self.up = False
      self.down = True
      self.go_down()

  def go_down(self):
    if self.y + 1 < self.height:
      self.y += 1
    else:
      self.up = True
      self.down = False
      self.go_up()

  def print(self):
    i = 0
    print('{}'.format('#' * (self.width + 2)))
    while i < self.height:
      if i == self.y:
        print('#{}{}{}#'.format(' ' * self.x, self.text, ' ' * (self.width - self.length - self.x)))
      else:
        print('#{}#'.format(' ' * self.width))
      i += 1
    print('{}'.format('#' * (self.width + 2)))

def main():
  (width, height, length) = (int(x) for x in input().split())

  ss = ScreenSaver(width, height)
  ss.setText('@' * length)

  for i in range(101):
    print(ss.x, ss.y, end=' ')
    ss.update()

if __name__ == '__main__':
  main()