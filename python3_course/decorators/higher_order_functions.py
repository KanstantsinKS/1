# Highter order functions, with accept another functions as arguments

# def product(n, func):
#     result = 1
#     for number in range(1, n):
#         result *= func(number)
#     return result


# def square(x):
#     return x * x


# def cube(x):
#     return x ** 3


# print(product(4, square))
# print(product(4, cube))


# def my_function(a, b, func):
#     result = func([a, b])
#     return result


# print(my_function(2, 3, sum))



# Using nested function

from random import choice

# def colorize(thing):
#     def get_color():
#         colors = ('red', 'green', 'yellow')
#         color = choice(colors)
#         return color

#     result = get_color() + " " + thing
#     return result

# print(colorize('ball'))

# def make_color():
#     def get_color():
#         colors = ('red', 'green', 'yellow')
#         color = choice(colors)
#         return color

#     return get_color

# first_color = make_color()
# print(first_color())
# second_color = make_color()
# print(first_color())
# third_color = make_color()
# print(first_color())


# Inner functions can access outer function scope

# def colorize(thing):
#     def get_color():
#         colors = ('red', 'green', 'yellow')
#         color = choice(colors)
#         return color + " " + thing
#
#     return get_color
#
# print(colorize('apple')())
# colorize_1 = colorize('ball')
# print(colorize_1())