from math import floor, sqrt


def find_factors(number):
    factors = [1]
    for factor in range(2, floor(sqrt(number))):
        if number % factor == 0:
            factors += [factor, number // factor]
    return factors


print(sum([i for i in range(1, 10000) if i == sum(find_factors(sum(find_factors(i)))) and i != sum(find_factors(i))]))
print(([i for i in range(1, 10000) if i == sum(find_factors(sum(find_factors(i)))) and i != sum(find_factors(i))]))
