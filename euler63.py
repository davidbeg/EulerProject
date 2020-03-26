count = 0
for x in range(1, 40):
    for i in range(1, 30):
        if i == len(str(x ** i)):
            print("%d, %d, %d" % (x, i, x ** i))
            count += 1
print(count)

