from decimal import *
getcontext().prec = 28


def find_max_geo_sum(n):
    biggest = 0
    best_l = []
    while n >= 1:
        visited = set()
        for i in range(int(n) - 1, 1, -1):
            # if i in visited:
            #     continue
            # visited.add(i)
            l, temp_sum = find_sum_with_first_two(i, n, visited)
            if temp_sum + n > biggest and len(l) > 2:
                biggest = temp_sum + n
                best_l = l
        n -= 1
    print([round(num) for num in best_l])


def find_sum_with_first_two(i, n, visited):
    temp_sum = 0
    progression = n / i
    x = Decimal(i)
    l = [n]
    while (abs(x % 1) < Decimal(1) / (10 ** 10) or abs(x % 1 - 1) < Decimal(1) / (10 ** 10)) and x >= 1:
        if int(x) in visited:
            break
        visited.add(x)
        temp_sum += x
        l.append(x)
        x = x / Decimal(progression)
    return l, temp_sum


find_max_geo_sum(4)
find_max_geo_sum(10)
find_max_geo_sum(12)
find_max_geo_sum(1000)
find_max_geo_sum(Decimal(5 * 10 ** 3))
