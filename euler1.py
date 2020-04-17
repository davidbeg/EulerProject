x = sum([[1, i * 2, 1] for i in range(1, 34)], [])
numerator = 1
denom = x.pop()
while x:
    numerator, denom = denom, denom * x.pop() + numerator
print(sum([int(x) for x in str(denom * 2 + numerator)]))
