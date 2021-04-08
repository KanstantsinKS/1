# def simple_function():
#     # print('Some code before the old code')
#     print('Simple code')
#     # print('Some code after the old code')
#
# simple_function()
# print()
#
# def decorator_function(original_function):
#     def wrap_function():
#         print('Some code before the old code')
#         original_function()
#         print('Some code after the old code')
#     return wrap_function
#
# # decorated_function = decorator_function(simple_function)
# # decorated_function()
# print()
#
# # @decorator_function
# def simple_function():
#     print('Simple code without decorator')
#
# simple_function()
# print()
#
# @decorator_function
# def simple_function():
#     print('Simple code with decorator ')
#
# simple_function()

# def make_comliment(func):
#     def wrapper(*args, **kwargs):
#         print('Nice to meat you!')
#         func(*args, **kwargs)
#         print('You lock great!')
#     return wrapper
#
#
# @make_comliment  # Wtih decorator
# def ask_name():
#     print('What is your name?')
#
#
# ask_name()
# print()
#
#
# @make_comliment  # Wtih decorator
# def say_name(name):
#     print(f'My name is {name}')
#
#
# say_name('Jack')
# print()
#
#
# @make_comliment
# def order(food, drink):
#     print(f'Give me {food} and {drink}')
#
#
# order('chips', 'cola')
# order(food='chips', drink='cola')



# Wraps decorator
# from functools import wraps
#
# def print_function_data(function):
#     """
#     This is decorator function
#     param function:
#     return:
#     """
#     @wraps(function)
#     def wrapper(*args, **kwargs):
#         print(f'You are using {function.__name__}')
#         print(f'Function documentation {function.__doc__}')
#         return function(*args, **kwargs)
#     return wrapper
#
#
# @print_function_data
# def squres_sum(a, b):
#     """
#     param a: first number
#     param b: second number
#     return: sum of squares a and b: (a * a + b + b)
#     """
#     return f' Sum of squares = {a * a + b + b}'
#
#
# print(squres_sum(2, 3))
# print(squres_sum.__name__)
# print(squres_sum.__doc__)

# from functools import wraps
#
#
# def print_args(function):
#     @wraps(function)
#     def wrapper_function(*args, **kwargs):
#         print(f'Args {args}')
#         print(f'Kwargs {kwargs}')
#         return function(*args, **kwargs)
#     return wrapper_function
#
#
# @print_args
# def function_to_decorate(*args, **kwargs):
#     print('This is a original function text')
#
#
# function_to_decorate('Jack', 'Smith', food='eggs', drink='soda')
