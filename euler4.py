largest_product = 0


def is_polindrom(x):
    str_x = str(x)
    return str_x == str_x[::-1]


for a1 in range (100, 1000):
    for a2 in range (100, 1000):
        if a2 > a1:
            break
        if is_polindrom(a1 * a2) and a1 * a2 > largest_product:
            largest_product = a1 * a2
print(largest_product)
