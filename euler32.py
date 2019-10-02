products = set()
pandigital = set(range(1, 10))
for i in range(1, 10 ** 5):
    j = 1
    all_digits = str(i) + str(j) + str(i*j)
    while len(all_digits) < 10:
        if "0" not in all_digits and len(set([c for c in all_digits])) == 9:
            products.add(i * j)
        j += 1
        all_digits = str(i) + str(j) + str(i*j)

print(products)
print(sum(products))
