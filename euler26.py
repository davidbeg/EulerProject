def find_cycle(d):
    digits = "1."
    enumerators = dict()
    residual = 1
    while True:
        if residual in enumerators:
            break
        if residual == 0:
            print(digits)
            return
        enumerators[residual % d] = digits
        jumps = 0
        while residual < d:
            jumps += 1
            residual *= 10
        digits += "0" * (jumps - len(str(residual // d))) + str(residual // d)
        residual = residual % d
    index = len(enumerators[residual % d])
    print("'%4d' %s(%s)" % (len(digits[index:]), digits[:index], digits[index:]))


for i in range(1, 1000):
    print("%d: " % i, end="")
    find_cycle(i)

