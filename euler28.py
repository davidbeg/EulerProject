total = 1
number = 1
layer = 2
while layer * 2 - 1 <= 1001:
    length = 2 * (layer - 1)
    for _ in range(4):
        number += length
        total += number
    layer += 1

print(total)
