from math import floor, sqrt


def is_prime(x):
    for i in range(2, floor(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


for i in range(1001, 10000, 2):
    if not is_prime(i):
        continue
    for j in range(2, (10000 - i) // 2 + 1, 2):
        if is_prime(i + j) and is_prime(i + 2 * j):
            if sorted(str(i)) == sorted(str(i + j)) == sorted(str(i + 2 * j)):
                print(i, i + j, i + 2 * j)
