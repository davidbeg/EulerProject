from math import floor

best = []
for p in range(4, 1001, 2):
    print(p)
    solutions_for_p = []
    for a in range(1, p - 2):
        for b in range(a, a + floor((p - a) / 2), 1):
            c = p - a - b
            if a ** 2 + b ** 2 == c ** 2:
                solutions_for_p.append((a, b, c))
    if len(solutions_for_p) > len(best):
        best = solutions_for_p

print("p=%d" % sum(best[0]))
print("len(solutions)=%d" % len(best))
print("solutions=%s" % best)
