#input
# 16
# 7 l f e f r o v e p r c
# 7 t n q a o w o m p d y
# 8 s t e e n x g u g q s j l
# 9 s n t o g k i s n h q n r i
# 8 c s e g n t u f l i n o a
# 5 e w d e m m t n
# 4 s i a m g d b
# 5 s k a s h n w h
# 6 k a n r k t r e t k
# 7 p i p n s t s r d o e
# 8 p d v e u i b q l r j p c
# 4 d u c j l o b
# 6 i e t r n y y i z w
# 10 m l f n a t o n a y m p b f q e
# 9 b s r t s u b v v r n i s o
# 7 o t i n h u g o r p p

def read_words(filename):
  f = open(filename, 'r')
  words = f.readlines()
  words = [s.strip() for s in words]
  return words

def matching_length_words(length, words):
  found_words = []
  for word in words:
    if len(word) == length:
      found_words.append(word)
  return found_words

def matching_letters_words(letters, words):
  found_words = []
  for word in words:
    count = 0
    temp_letters = letters[:]
    for letter in word:
      if letter in temp_letters:
        count += 1
        temp_letters.remove(letter)
    if count == len(word):
      found_words.append(word)
  return found_words

def main():
  n = int(input())
  words = read_words('words.txt')

  for i in range(n):
    temp = input().split()
    length = int(temp[0])
    letters = temp[1:]
    matching_len_words = matching_length_words(length, words)
    matching_words = matching_letters_words(letters, matching_len_words)
    print(len(matching_words),end=' ')

if __name__ == '__main__':
  main()