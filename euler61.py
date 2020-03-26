from math import sqrt


def is_triangle(n):
    return (sqrt(1 + 8 * n) - 1) % 2 == 0


def is_square(n):
    return sqrt(n) % 1 == 0


def is_pentagonal(n):
    return (sqrt(1 + 24 * n) + 1) % 6 == 0


def is_hexagonal(n):
    return (sqrt(1 + 8 * n) + 1) % 4 == 0


def is_heptagonal(n):
    return (sqrt(9 + 40 * n) + 3) % 10 == 0


def is_octagonal(n):
    return (sqrt(4 + 12 * n) + 2) % 6 == 0


def concat(x, y):
    return int("{:02d}".format(x) + "{:02d}".format(y))


type_detectors = [is_triangle, is_square, is_pentagonal, is_hexagonal, is_heptagonal, is_octagonal]
NUMBER_OF_TYPES = 6


def find_next(prefix, types, first_prefix):
    for type_index in range(NUMBER_OF_TYPES):
        if types[type_index]:
            continue
        detector = type_detectors[type_index]
        for suffix in range(10, 100):
            new_number = concat(prefix, suffix)
            if detector(new_number):
                new_types = types[:]
                new_types[type_index] = True
                if all(new_types):
                    if first_prefix == new_number % 100:
                        return [new_number]
                    continue
                num_list = find_next(suffix, new_types, first_prefix)
                if num_list:
                    return [new_number] + num_list

    return None


is_used = [False] * NUMBER_OF_TYPES
for prefix in range(10, 100):
    result = find_next(prefix, is_used, prefix)
    if result:
        print(result)
        print(sum(result))
        break

