x = [1,2,3,4,5]

y = [x.copy()] * 5
z = [x.copy() for i in range(5)]
print(x)
y[0][0] = 100
z[0][0] = 100
print(y)
print(z)
print(y == z)
