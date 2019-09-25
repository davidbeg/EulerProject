from math import floor, sqrt


def find_factors(number):
    factors = set([1])
    for factor in range(2, floor(sqrt(number)) + 1):
        if number % factor == 0:
            factors.add(factor)
            factors.add(number // factor)
    return factors

print("stage 1")
abundants = []
for i in range(1, 28123):
    if sum(find_factors(i)) > i:
        abundants.append(i)
print("stage 2")

sums = {i for i in range(28124)}
for i in abundants:
    for j in abundants:
        if i + j < 28124 and i + j in sums:
            sums.remove(i + j)
print("stage 3")

total = 0
print(sum(sums))
