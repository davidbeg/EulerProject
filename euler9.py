from math import sqrt

a, b, c = 1, 1, 1
while c < 1000:
    b = 1
    while c > b:
        a = 1000 - b - c
        if a ** 2 + b ** 2 == c ** 2 and b > 1000 - b - c > 0:
            print("a: %d, b: %d, c: %d" % (a, b, c))
            print(a* b* c)
        b += 1
    c += 1
