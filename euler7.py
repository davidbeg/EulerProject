from euler3 import is_prime

number = 2
count = 1

while count < 10001:
    number += 1
    if is_prime(number):
        count += 1
print(number)
