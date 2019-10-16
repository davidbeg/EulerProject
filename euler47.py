import time
from math import floor, sqrt

primes = [2, 3]


def is_prime(x):
    for i in range(2, floor(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def find_factors(number):
    factors = []
    index = 0
    while number > 1:
        if number % primes[index] == 0:
            factors.append(primes[index])
            while number % primes[index] == 0:
                number /= primes[index]
        index += 1
    return factors


start = time.time()
i = 4
factor_list = [[1], [2], [3], [2]]
while True:
    i += 1
    if is_prime(i):
        primes.append(i)
    factor_list = factor_list[1:] + [find_factors(i)]
    if i % 10000 == 0:
        print(i)
    if all(map(lambda x: len(x) == 4, factor_list)):
        print(i - 3)
        break
end = time.time()
print(end - start)
