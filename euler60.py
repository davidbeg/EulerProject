from itertools import permutations, combinations
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


def concat(x, y):
    return int(str(x) + str(y))


all_primes.add(2)
for i in range(3, floor(10 ** 4), 2):
    is_prime(i)

combs2 = set()
combs3 = set()
combs4 = set()
combs5 = set()
primes = sorted(list(all_primes.copy()))
print(len(primes))
ii = 1
for comb in combinations(all_primes, 2):
    # if ii % 1000 == 0:
    #     print(ii)
    ii += 1
    if is_prime(concat(comb[0], comb[1])) and is_prime(concat(comb[1], comb[0])):
        combs2.add(comb if comb[1] > comb[0] else (comb[1], comb[0]))


def sorted_tuple(in_list):
    return tuple(sorted(in_list))


print("Stage 2 done")

for prime in primes:
    for comb in combs2:
        if sorted_tuple([comb[0], prime]) in combs2 and sorted_tuple([comb[1], prime]) in combs2:
            combs3.add(sorted_tuple([comb[0], comb[1], prime]))

print("Stage 3 done")

for prime in primes:
    for comb in combs3:
        if sorted_tuple([comb[0], prime]) in combs2 and \
                sorted_tuple([comb[1], prime]) in combs2 and \
                sorted_tuple([comb[2], prime]) in combs2:
            combs4.add(sorted_tuple([comb[0], comb[1], comb[2], prime]))

print("Stage 4 done")


for prime in primes:
    for comb in combs4:
        if sorted_tuple([comb[0], prime]) in combs2 and \
                sorted_tuple([comb[1], prime]) in combs2 and \
                sorted_tuple([comb[2], prime]) in combs2 and \
                sorted_tuple([comb[3], prime]) in combs2:
            combs5.add(sorted_tuple([comb[0], comb[1], comb[2], comb[3], prime]))

print(combs2)
print(combs3)
print(combs4)
print(combs5)
print(len(primes) ** 2)
print(len(combs2))
print(len(combs3))
print(len(combs5))

print("Done")
