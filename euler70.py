from functools import reduce
from itertools import permutations, combinations
from math import floor, sqrt


def is_prime(x):
    for i in range(2, floor(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def next_prime():
    yield 2
    x = 3
    while True:
        while not is_prime(x):
            x += 2
        yield x
        x += 2


def binary_search(array, x, lo=0, hi=None):
    if hi is None:
        hi = len(array)
    while lo < hi:
        mid = (lo+hi)//2
        midval = array[mid]
        if midval > x:
            lo = mid+1
        elif midval < x:
            hi = mid
        else:
            return mid
    return mid


prime_gen = next_prime()
first_primes = []
while True:
    next_p = next(prime_gen)
    if next_p > 10 ** 6:
        break
    first_primes.append(next_p)
first_primes = first_primes[::-1]
best_candidate = 0
best_xy = 0
best_score = 3 # we know we can do better

for x in first_primes:
    new_index = binary_search(first_primes, (10 ** 7) / x)
    for y in first_primes[new_index:]:
        candidate = x * y
        if candidate >= 10 ** 7:
            continue
        relatives_len = candidate - x - y + 1
        score = candidate / relatives_len
        if sorted(str(candidate)) == sorted(str(relatives_len)):
            if score < best_score:
                best_score, best_candidate, best_xy = score, candidate, (x, y)

print(best_candidate)
print(best_score)
print(best_xy)


