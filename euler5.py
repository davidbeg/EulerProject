import time
from collections import Counter
from functools import reduce
from math import sqrt, floor


def is_prime(x):
    for i in range(2, floor(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def find_factors(number):
    factors = []
    factor = 2
    while number > 1:
        if number % factor == 0:
            factors += [factor]
            number /= factor
        else:
            factor += 1
    return factors


def way2():
    factors = Counter([])
    for n in range(2, 21):
        factors |= Counter(find_factors(n))
    print(reduce(lambda x, y: x * (y ** factors[y]), factors, 1))


def is_divisible(number):
    for divisor in range(1, 21):
        if number % divisor != 0:
            return False
    return True


def way1():
    smallest_number = 0

    while True:
        smallest_number += 1
        # if smallest_number % 100000 == 0:
        #     print(smallest_number)
        if is_divisible(smallest_number):
            print(smallest_number)
            break


start_time = time.time()
print("Way 1:")
way1()
print("Time elapsed: " + str(time.time() - start_time))

start_time = time.time()
print("Way 2:")
way2()
print("Time elapsed: " + str(time.time() - start_time))
