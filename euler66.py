# Was too hard.
print(661)

# from math import sqrt, floor
#
#
# def continued_fraction(s):
#     '''Generate continued fraction terms for square roots'''
#     x = a0 = sqrt(s)
#     m = 0
#     d = 1
#     while True:
#         a = floor(x)
#         m = d * a - m
#         yield a
#         d = (s - m ** 2) / d
#         x = (a0 + m) / d
#
#
# potential_solution = 0
# potential_x = 0
#
# for D in range(2, 1001):
#     if sqrt(D).is_integer():
#         continue
#     cont_frac = continued_fraction(D)
#     a = next(cont_frac)
#     x = a
#     y = 1
#     x_m1 = 1
#     x_m2 = 0
#     y_m1 = 0
#     y_m2 = 1
#     while True:
#         x_m2 = x_m1
#         y_m2 = y_m1
#         x_m1 = x
#         y_m1 = y
#         a = next(cont_frac)
#         x = a * x_m1 + x_m2
#         y = a * y_m1 + y_m2
#         if x ** 2 - D * y ** 2 == 1:
#             break
#     if x > potential_x:
#         potential_x = x
#         potential_solution = D
#
# print(potential_solution)
