from math import sqrt


def is_triangle(n):
    ''' n(n+1)/2 ==> 0.5n2 + 0.5n'''
    return (-0.5 + sqrt(0.25 + 2*n)) % 1 == 0


def is_hexagonal(n):
    ''' n(2n-1) ==> 2n2 - n'''
    return (1 + sqrt(1 + 8*n)) % 4 == 0

i = 165
while True:
    i += 1
    new_number = i * (3 * i - 1) / 2
    if is_hexagonal(new_number) and is_triangle(new_number):
        print(i)
        print(new_number)
        break
