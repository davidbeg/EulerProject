from math import floor, sqrt

MILLION = 10 ** 6


def is_prime(x):
    for i in range(2, floor(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def next_prime(x):
    x += 2
    while not is_prime(x):
        x += 2
    return x


all_primes = [2, 3]
total = 5

while total <= MILLION:
    all_primes.append(next_prime(all_primes[-1]))
    total += all_primes[-1]

max_size = len(all_primes)
options = [all_primes]
found = False
while not found:
    for sequence in options:
        if is_prime(sum(sequence)):
            print(sequence)
            print("SUM=%d" % sum(sequence))
            print(len(sequence))
            found = True
            break
    max_size -= 1
    if next_prime(all_primes[-1]) + sum(all_primes[-max_size:]) < MILLION:
        all_primes.append(next_prime(all_primes[-1]))
    options = [all_primes[i: i + max_size] for i in range(len(all_primes) - max_size + 1)]

