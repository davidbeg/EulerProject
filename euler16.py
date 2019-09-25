from functools import reduce

o = 2 ** 1000
print(str(1000) + "," + str(reduce(lambda x, y: int(x) + int(y), str(o))) + "\n")

