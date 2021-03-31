# pi = 'outer pi variable'
#
# def print_pi():
#     pi = 'inner pi vareiable'
#     print(pi)
#
# print(pi)
# print_pi()
#
# # local scope
# pi1 = 'global pi variable'
#
# def inner():
#     pi1 = 'inner pi variable'
#     print(pi1)
#
# inner()
#
# # global scope
# pi2 = 'global pi variable'
#
# def inner1():
#     pi2 = 'inner pi variable'
#     print(pi2)
#
# inner1()
# print(pi2)

# Enclosed Scope
# pi3 = 'global pi variable'
#
# def outer():
#     pi3 = 'outer pi variable'
#     def inner():
#         nonlocal pi3
#         pi3 = 'inner pi variable'
#         print(pi3)
#     inner()
#     print(pi3)
# outer()
# print(pi3)

# built-in Scope
from math import pi
# pi = 'global pi variable'
def outer():
    # pi = 'outer pi variable'
    def inner():
        # pi = 'inner pi variable'
        print(pi)
    inner()

outer()