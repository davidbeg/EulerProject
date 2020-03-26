x = (1, 2)
count = 0
for _ in range(1000):
    # print("%s %s/%s" % (1 + x[0]/x[1], x[0] + x[1], x[1], ))
    if len(str(x[0] + x[1])) > len(str(x[1])):
        count += 1
    x = (x[1], x[0] + 2 * x[1])
print(count)
