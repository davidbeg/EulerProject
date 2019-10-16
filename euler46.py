from math import floor, sqrt


def is_prime(x):
    for i in range(2, floor(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


number = 1
primes = [2]
while True:
    number += 2
    if is_prime(number):
        primes.append(number)
        continue
    found = False
    for prime in primes:
        if sqrt((number - prime) / 2) % 1 == 0:
            found = True
            break
    if not found:
        print(number)
        break
