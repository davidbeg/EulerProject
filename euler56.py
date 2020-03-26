from itertools import combinations_with_replacement

maxx = 0
for a, b in combinations_with_replacement(range(1, 100), 2):
    maxx = max(maxx, sum([int(c) for c in str(a ** b)]))
    maxx = max(maxx, sum([int(c) for c in str(b ** a)]))
print(maxx)
