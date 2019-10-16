from itertools import permutations


total = 0
for n in permutations(range(0, 10)):
    number = int(''.join([str(i) for i in n]))
    if number < 10 ** 9:
        continue
    if int(str(number)[1:4]) % 2 != 0:
        continue
    if int(str(number)[2:5]) % 3 != 0:
        continue
    if int(str(number)[3:6]) % 5 != 0:
        continue
    if int(str(number)[4:7]) % 7 != 0:
        continue
    if int(str(number)[5:8]) % 11 != 0:
        continue
    if int(str(number)[6:9]) % 13 != 0:
        continue
    if int(str(number)[7:10]) % 17 != 0:
        continue
    total += number
    print(number)
print(total)
