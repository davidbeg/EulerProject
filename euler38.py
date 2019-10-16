def is_9_pandigital(n):
    if len(n) != 9:
        return False
    for i in range(1, 10):
        if not str(i) in n:
            return False
    return True

largest = (0, 123456789)
for i in range(1, 10 ** 5):
    concat_prod = ""
    for j in range(1, 10):
        concat_prod += str(i * j)
        if len(concat_prod) >= 9:
            break
    if not is_9_pandigital(concat_prod):
        continue
    if int(concat_prod) > largest[1]:
        largest = (i, int(concat_prod))

print(largest)


