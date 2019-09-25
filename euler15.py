mem = dict()


def find_path(point):
    global mem
    if point in mem:
        return mem[point]
    if point[0] < 0 or point[1] < 0:
        return 0
    if point == (0, 0):
        return 1
    else:
        mem[point] = find_path((point[0] - 1, point[1])) + find_path((point[0], point[1] - 1))
        return mem[point]


print(find_path((20, 20)))
