sum = 0
x1 = 0
x2 = 1
while x2 < 4 * 10 ** 6:
    if x2 % 2 != 0:
        sum += x2
    x1, x2 = x2, x1 + x2
print(x2)
print(sum)