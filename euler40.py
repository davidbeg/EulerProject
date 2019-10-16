x = ""
for i in range(1, 2 * (10 ** 5)):
    x += str(i)
result = 1
for i in range(7):
    result *= int(x[10 ** i - 1])
print(result)
