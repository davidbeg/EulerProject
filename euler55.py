count = 0
for ii in range(1, 10 ** 4):
    i = ii + int(str(ii)[::-1])
    found = False
    for _ in range(51):
        if str(i) == (str(i))[::-1]:
            found = True
            break
        i += int(str(i)[::-1])
    if not found:
        print(ii)
        count += 1
print(count)
