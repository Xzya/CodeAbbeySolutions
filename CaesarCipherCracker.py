#input
# 5
# DANA ZEAO EJ IU XKOOKI PQNJO WHH WNKQJZ XQP ZKAO JKP IKRA CNAAJBEAHZO WNA CKJA JKS
# NF RNFL NF YLVAT VG VF OYNPX NAQ JUVGR NAQ ERQ NYY BIRE VS OYBBQ OR GUR CEVPR BS GUR NQZVENYGL
# OP TPPOFS TQPLFO UIBO CSPLFO GPVS TDPSF BOE TFWFO ZFBST BHP UP VT JO PMEFO TUPSJFT
# YWHHAZ EP PDA NEOEJC OQJ EJ WJYEAJP LANOEW PDANA SWO W GEJC SDK SWJPO PK HERA BKNARAN
# PX VTEE AXK MAX PHFTG PAH WBW GHM VTKX LMHGX PTEEL WH GHM T IKBLHG FTDX

#generates a new dict ratated by k palces
def generate_dict(alphabet, k):
  dict = {}
  for i in range(0, len(alphabet)):
    dict[alphabet[(i+k) % len(alphabet)]] = alphabet[i]
  return dict

#calculates the letter frequency for given sentence
def calculate_letter_freq(sentence, alphabet):
  freq = [0] * len(alphabet)
  for i in range(0, len(alphabet)):
    freq[i] = sentence.count(alphabet[i]) / len(sentence) * 100
  return freq

#calculates the difference in distribution between found distribution
#and ideal distribution
def distribution_difference(freq, ideal_letter_distribution):
  diff = []
  for i in range(0, len(freq)):
    diff.append(freq[i] - ideal_letter_distribution[i])
  return diff

#decipheres a given sentence, returns the rotation k
def decipher(sentence, alphabet, ideal_letter_distribution):
  k = 0
  deciphered_sentences = []
  differences = []
  for i in range(0, 25):
    deciphered = ""
    dict = generate_dict(alphabet, k)
    k += 1

    for c in sentence:
      if c != ' ':
        deciphered += dict[c]
      else:
        deciphered += c
    deciphered_sentences.append(deciphered)

    freq = calculate_letter_freq(deciphered, alphabet)
    diff = distribution_difference(freq, ideal_letter_distribution)
    diff = [x**2 for x in diff]
    differences.append(diff)

  averages = []
  for i in range(0, len(differences)):
    diff_sum = sum(differences[i])
    average = diff_sum / len(differences[i])
    averages.append(average)

  min_average_index = 0
  for i in range(0, len(averages)):
    if averages[i] < averages[min_average_index]:
      min_average_index = i

  return deciphered_sentences, min_average_index


alphabet = [c for c in 'abcdefghijklmnopqrstuvwxyz'.upper()]
ideal_letter_distribution = [8.1, 1.5, 2.8, 4.3, 13.0, 2.2, 2.0, 6.1, 7.0, 0.15, 0.77, 7.0, 2.4,
        6.8, 7.5, 1.9, 0.095, 6.0, 6.3, 9.1, 2.8, 0.98, 2.4, 0.15, 2.0, 0.074]

n = int(input())

for i in range(0, n):
  sentence = input()

  deciphered_sentences, k = decipher(sentence, alphabet, ideal_letter_distribution)

  print(' '.join((deciphered_sentences[k].split())[:3]), k, "", end="")