from math import floor, sqrt


def is_prime(x):
    for i in range(2, floor(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


selected = set()
primes = set()
for i in range(2, 10 ** 6):
    good_permutations = []
    test_num = i
    for _ in range(len(str(i))):
        if test_num in primes or is_prime(test_num):
            good_permutations.append(test_num)
            primes.add(test_num)
        s = str(test_num)
        test_num = int(s[-1] + s[:-1])
    if len(good_permutations) == len(str(i)):
        selected.add(i)


print(selected)
print(len(selected))
