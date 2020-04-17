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


prime_gen = next_prime()
first_primes = []
for i in range(12):
    first_primes.append(next(prime_gen))

best_candidate = 0
best_score = 0
for i in range(7, 10):
    print("Combining %d primes" % i)
    for a in combinations(first_primes, i):
        candidate = reduce(lambda x, y: x * y, a)
        if candidate > 10 ** 6:
            continue
        potential_relative_primes = set(range(1, candidate))
        relative_primes = set()
        for f in potential_relative_primes:
            division_result = [f % factor for factor in a]
            if 0 not in division_result:
                relative_primes.add(f)
        score = candidate / len(relative_primes)
        if score > best_score:
            best_score, best_candidate = score, candidate
print(best_candidate)
print(best_score)


