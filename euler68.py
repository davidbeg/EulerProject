from itertools import combinations, permutations
from time import sleep

SIZE = 5
NUMBERS = list(range(1, SIZE * 2 + 1))[::-1]
inner = [0] * SIZE
outer = [0] * SIZE
assigned = [False] * SIZE


def test_circle():
    group_sums = [0] * SIZE
    value = ""
    for group_index in range(SIZE):
        values = [outer[group_index], inner[group_index], inner[(group_index + 1) % SIZE]]
        value += str(outer[group_index]) + str(inner[group_index]) + str(inner[(group_index + 1) % SIZE])
        group_sums[group_index] = sum(values) if all(values) else 0
    is_gon = len(set([num for num in group_sums if num])) == 1
    if is_gon:
        return value
    return None


biggest = 0
for i in permutations(NUMBERS, 5):
    outer = i
    if min(outer) != outer[0]:
        continue
    for j in permutations([x for x in NUMBERS if x not in i]):
        inner = j
        result = test_circle()
        if result and len(result) == 16 and int(result) > biggest:
            biggest = int(result)
            print(outer)
            print(inner)
            print(biggest)
            # exit()

