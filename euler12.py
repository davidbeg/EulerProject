def find_factors(n):
    if n == 1:
        return [1]
    factors = [1, n]
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            factors.append(i)
            factors.append(n // i)
        i += 1
    return factors


n = 1
while len(find_factors((1 + n) * n // 2)) < 500:
    n += 1

print(n)
print((1 + n) * n // 2)
