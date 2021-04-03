from time import time
from functools import wraps

# def speed_test(function):
#     @wraps(function)
#     def wrapper(*args, **kwargs):
#         start_time = time()
#         result = function(*args, **kwargs)
#         end_time = time() - start_time
#         print(f'Time of code execution {end_time}')
#         return result
#     return wrapper
#
#
# @speed_test
# def sum_with_list():
#     return sum([number for number in range(1000000)])
#
#
# @speed_test
# def sum_with_gen():
#     return sum(number for number in range(1000000))
#
#
# @speed_test
# def product(range_value):
#     result = 1
#     for number in range(1, range_value):
#         result *= number
#     return result
#
#
# print(sum_with_list())
# print(sum_with_gen())
# print(product(100000))

from functools import wraps


def hello_from_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        string = function(*args, **kwargs)
        print(str(string) + ' Hello from decorator!')
    return wrapper


@hello_from_decorator
def hello_function():
    return 'Text of origin function +'


hello_function()




