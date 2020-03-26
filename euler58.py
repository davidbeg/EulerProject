import math


def is_prime(x):
    for i in range(2, math.floor(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


x = 1
total = 1
iteration = 1
primes = 0
while primes / total >= (.1 if x > 1 else 0):
    for _ in range(4):
        x += 2 * iteration
        if is_prime(x):
            primes += 1
    total += 4
    iteration += 1
print(iteration)
print(iteration * 2 - 1)
