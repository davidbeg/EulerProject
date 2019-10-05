import math

for i in range(10 ** 8):
    if i == sum([math.factorial(int(x)) for x in str(i)]):
        print(i)