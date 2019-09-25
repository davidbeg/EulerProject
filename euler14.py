def step(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1


mem = dict()
for i in range(1, 10**6):
    mem[i] = 0
    count = 0
    n = i
    while n != 1:
        if n in mem and mem[n] != 0:
            mem[i] = mem[n]
            break
        n = step(n)
        count += 1
    mem[i] = count + mem[i]

print(max(mem.items(), key=lambda x: x[1]))

