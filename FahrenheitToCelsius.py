#input
#35 51 236 154 498 410 178 199 436 499 481 237 403 537 435 38 79 106 545 401 477 562 295 41 437 203 514 196 106 392 352 392 411 557 515 308

def fahrenheit_to_celsius(f):
    return ((f - 32.0) * (5.0/9.0))

temps = input().split()

for i in range(1, int(temps[0]) + 1):
    print(round(fahrenheit_to_celsius(int(temps[i]))) ,"", end="")