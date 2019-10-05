import binascii

sum = 0
for i in range(1, 10 ** 6):
    binary_str = "{0:b}".format(i)
    if binary_str == binary_str[::-1] and str(i) == str(i)[::-1]:
        sum += i

print(sum)
