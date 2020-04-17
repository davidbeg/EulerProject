from math import floor


def do_step(n, top, bottom):
    multiplier = top
    top, bottom = -bottom, n - bottom ** 2
    bottom //= multiplier
    added = 0
    while top - bottom > -(n ** 0.5):
        added += 1
        top -= bottom
    return added, top, bottom


def calculate_series(n):
    a0 = floor(n ** 0.5)
    memory = set()
    series = []
    added, top, bottom = do_step(n, 1, -a0)
    while not (added, top, bottom) in memory:
        series.append(added)
        memory.add((added, top, bottom))
        added, top, bottom = do_step(n, bottom, top)
    print("√%d = [%d; %s], period=%d" % (n, a0, tuple(series), len(series)))
    return len(series) % 2 == 1


odds = 0
for i in range(2, 10 ** 4 + 1):
    if i ** 0.5 % 1 == 0:
        continue
    if calculate_series(i):
        odds += 1
print(odds)
