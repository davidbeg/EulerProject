from itertools import permutations
from math import floor, sqrt


def is_prime(x):
    for i in range(2, floor(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


for n in permutations(range(7, 0, -1)):
    number = int(''.join([str(i) for i in n]))
    if is_prime(number):
        print(number)
        break

