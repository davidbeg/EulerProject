from euler3 import is_prime

total = 2
for i in range(3, 2 * (10 ** 6), 2):
    if is_prime(i):
        total += i

print(total)
