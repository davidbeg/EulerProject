from euler3 import is_prime

largest_n = 0
largest_a = 0
largest_b = 0
for a in range(-999, 1000):
    if a % 2 == 0:
        continue
    for b in range(-999, 1001, 2):
        n = 0
        quad = n ** 2 + a * n + b
        while quad > 0 and is_prime(quad):
            n += 1
            quad = n ** 2 + a * n + b
        if n > largest_n:
            largest_n, largest_a, largest_b = n, a, b
print(largest_a)
print(largest_b)
print(largest_n)
