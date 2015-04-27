#input
# 8
# recaps
# traipse
# persist
# reaps
# crates
# parroted
# trashed
# enlists

def open_file():
  f = open('words.txt', 'r')
  return f

def is_anagram(word, other):
  if len(word) != len(other):
    return False
  if word == other:
    return False
  for c in word:
    if word.count(c) != other.count(c):
      return False
  return True

if __name__ == '__main__':
  f = open_file()
  n = int(input())
  for i in range(n):
    word = input()
    num_of_anagrams = 0
    f.seek(0)
    w = f.readline().strip()
    while w:
      if is_anagram(word, w):
        num_of_anagrams += 1
      w = f.readline().strip()
    print(num_of_anagrams, '', end="")