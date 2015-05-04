#input
# ;>;<>;<>-<>;<[->++<][->+<]>:<:>;<;[->+>+<<]>>[-<<+>>]<<[->+<];>++++<>;<>;<>;<>;<+:>-:<;[->+>+<<]>>[-<<+>>]<<>-<>;<>:<>;<>:<[->+>++<<];+:>-:<:[>+<-]>++++<>:<>:<[->+>++<<]>-<[->++<][->+<]>-<:[->+<]+:>-:<:>:
# 7 14 11 4 2 7 7 10 12 17 5 2 11 14 2

class Brainfuck:
  def __init__(self):
    self.stack = [0] * 100
    self.pointer = 0

  def set_script(self, script):
    self.script = script

  def resize_stack(self):
    for i in range(0, len(self.stack)):
      self.stack.append(0)

  def set_input(self,inp):
    self.inp = inp.split()

  def interpret_token(self,t):
    if t == '+':
      self.stack[self.pointer] += 1
    elif t == '-':
      self.stack[self.pointer] -= 1
    elif t == ':':
      print(self.stack[self.pointer], end=' ')
    elif t == ';':
      self.stack[self.pointer] = int(self.inp.pop(0))
    elif t == '>':
      self.pointer += 1
      if self.pointer >= len(self.stack) - 1:
        self.resize_stack()
    elif t == '<':
      self.pointer -= 1
      if self.pointer < 0:
        raise IndexError('Error: Data pointer is decremented below zero with "<" operation')

  def interpret(self,script):
    i = 0
    while i < len(script):
      t = script[i]
      if t == '[':
        while True:
          if self.stack[self.pointer] != 0:
            result = self.interpret(script[i+1:])
            if result != None:
              end_index = script.index(result)
            else:
              break
          else:
            if end_index != None:
              i = end_index
              end_index = None
            else:
              j = i
              while script[j] != ']':
                j += 1
              i = j
            break
      elif t == ']':
        return script[i:]
      else:
        self.interpret_token(t)
      i += 1

def main():
  bf = Brainfuck()
  script = input()
  bf.set_input(input())
  bf.interpret(script)

if __name__ == '__main__':
  main()