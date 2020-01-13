from random import random

memo = {}


def fact_aux(n):
    return 1 if n < 2 else n * fact_aux(n - 1)


def fact(n):
    try:
        return memo[n]
    except KeyError:
        memo[n] = fact_aux(n)
        return memo[n]


def nCr(n, r):
    return fact(n) // (fact(r) * fact(n - r))


count = 0
for n in range(1, 101):
    for r in range(1, 101):
        if nCr(n, r) > 10 ** 6:
            count += 2 * (n // 2 - r + 1)
            if n % 2 == 0:
                count -= 1
            break

print(count)
print("All")
