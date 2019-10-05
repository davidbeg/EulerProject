from functools import reduce


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(a, b):
    return a * b / gcd(a, b)


noms = []
for nom in range(10, 100):
    for denom in range(nom + 1, 100):
        for i in range(1, 10):
            str_i = str(i)
            if str_i in str(nom) and str_i in str(denom) and \
                    int(str(nom).replace(str_i, "", 1)) * denom == int(str(denom).replace(str_i, "", 1)) * nom:
                print("%d/%d" % (nom, denom))
                noms.append(denom)

print(reduce(lcm, [4, 13, 5, 2]))
