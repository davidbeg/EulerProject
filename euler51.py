from itertools import permutations
from math import floor, sqrt

all_primes = set()
not_primes = set()

def is_prime(x):
    if x in all_primes:
        return True
    if x in not_primes:
        return False
    for i in range(2, floor(sqrt(x)) + 1):
        if x % i == 0:
            not_primes.add(x)
            return False
    all_primes.add(x)
    return True


def next_prime(x):
    x += 2
    while not is_prime(x):
        x += 2
    return x


n = 101


def is_same_length(x):
    global n
    return len(str(x)) == len(str(n))


def filter_family(candidates):
    # candidates = list(filter(is_same_length, candidates))
    new_family = []
    misses = 0
    for candidate in candidates:
        if is_prime(candidate):
            new_family.append(candidate)
        else:
            misses += 1
            if misses == 3:
                return new_family
    return new_family


digits = [str(i) for i in range(10)]


def add_candidates():
    candidates = []
    for d in digits:
        candidates.append(int(''.join([d if permutation[i] else num_str[i] for i in range(num_len)])))
    return candidates


while True:
    num_str = str(n)
    num_len = len(num_str)
    for replaced_digits_count in range(1, num_len - 1):
        for permutation in set(permutations([1] * replaced_digits_count + [0] * (num_len - replaced_digits_count))):
            family_candidates = add_candidates()
            family = filter_family(family_candidates)
            if len(family) == 8:
                # print(permutation)
                print(family)
                exit()

    n += 2
