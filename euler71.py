from math import ceil, floor


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


lowest = 3, 7
lowest_score = 0
for d in range(8, 10 ** 6 + 1):
    n = d * (3 / 7)
    if n % 1 == 0:
        n -= 1
    else:
        n = floor(n)
    if gcd(n, d) != 1:
        # n += 1
        continue
    if n / d > lowest_score:
        lowest = n, d
        lowest_score = n / d
print(lowest)
print(lowest_score)
print(lowest_score - 3 / 7)
