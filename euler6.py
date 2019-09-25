
n = 100
print(sum([x * y for x in range(n + 1) for y in range(n + 1)]) - sum([x ** 2 for x in range(n+1)]))
