#input
# 10
# 124514 129254 122893 177259 135118 153744 173358 120627 199128 151979

def generate_primes(max_num_of_primes):
  primes = []
  i = 3
  # for i in range(3, 200000, 2):
  while len(primes) < max_num_of_primes:
    isPrime = True
    for p in primes:
      if p * p > i:
        break
      remainder = i % p
      if remainder == 0:
        isPrime = False
        break
    if not isPrime:
      i += 2
      continue
    else:
      primes.append(i)
    i += 2
  primes.insert(0, 2)
  primes.insert(0, 1)
  return primes

n = int(input())
indices = [int(x) for x in input().split()]

primes = generate_primes(max(indices))

for i in indices:
  print(primes[i], "", end="")