import bisect
for i in range(30):
    print(i * (3 * i - 1) // 2, (i + 1) * (3 * i + 2) // 2)
from bisect import bisect_left


def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

SIZE = 100000

numbers = list()
numberss = set()
best = (0, 10**8)
for i in range(1, SIZE):
    numbers.append(i * (3 * i - 1) // 2)
    numberss.add(i * (3 * i - 1) // 2)
numbers = sorted(numbers)
for i in range(1, SIZE - 1):
    if not i % 100:
        print(i)
    for j in range(i):
        if numbers[j] - numbers[i] >= best[1] - best[0]:
            continue
        try:
            index(numbers, numbers[i] + numbers[j])
            index(numbers, numbers[i] - numbers[j])
        except ValueError:
            continue
        best = (numbers[i], numbers[j])
        print(best)

print(best)