from math import floor, sqrt


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, floor(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


selected = set()
primes = set()
for i in range(10, 10 ** 6):
    if len(selected) == 11:
        break
    good_trucations = []
    test_num = i
    for _ in range(len(str(i))):
        if test_num in primes:
            good_trucations.append(test_num)
        elif is_prime(test_num):
            good_trucations.append(test_num)
            primes.add(test_num)
        else:
            break
        test_num = int(str(test_num)[:-1]) if test_num > 9 else 0
    test_num = i
    for _ in range(len(str(i))):
        if test_num in primes:
            good_trucations.append(test_num)
        elif is_prime(test_num):
            good_trucations.append(test_num)
            primes.add(test_num)
        else:
            break
        test_num = int(str(test_num)[1:]) if test_num > 9 else 0
    if len(good_trucations) == len(str(i)) * 2:
        selected.add(i)


print(selected)
print(sum(selected))
