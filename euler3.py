import math


def is_prime(x):
    for i in range(2, math.floor(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

if __name__ == '__main__':
    limit = 600851475143
    x = math.floor(math.sqrt(limit))
    while limit % x != 0 or not is_prime(x):
        x -= 1
    print(x)

