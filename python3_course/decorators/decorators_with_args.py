from functools import wraps
from time import sleep

# def check_if_first_arg_is(value):
#     def inner_decorator(function):
#         @wraps(function)
#         def wrapper(*args, **kwargs):
#             if args and args[0] != value:
#                 print(f'First argument has to be {value}')
#             return function(*args, **kwargs)
#         return wrapper
#     return inner_decorator
#
#
# @check_if_first_arg_is('red')
# def print_rainbow_colors(*colors):
#     print(colors)
#
#
# @check_if_first_arg_is(7)
# def multiply_7(a, b):
#     print(a * b)
#
#
# print_rainbow_colors('red', 'orange', 'yellow', 'green')
# print_rainbow_colors('orange', 'yellow', 'red', 'green')
# multiply_7(7, 2)
# multiply_7(5, 7)


# def enforce(*types):
#     def inner_decorator(function):
#         @wraps(function)
#         def wrapper(*args, **kwargs):
#             new_args = []
#             for a, t in zip(args, types):
#                 new_args.append(t(a))
#             return function(*new_args, **kwargs)
#         return wrapper
#     return inner_decorator
#
#
# @enforce(str, int)
# def print_text_n_times(text, n):
#     for number in range(n):
#         print(text)
#
#
# print_text_n_times('hi', '3')
# print_text_n_times('hello', 3)


from functools import wraps
from time import sleep


def wait(n):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func(*args,**kwargs)
            sleep(n)
            print(f"There was a pause {n} seconds before execution {func.__name__}")
        return wrapper
    return inner_dec


@wait(3)
def print_text(text):
    print(text)


print_text('Hello')


from functools import wraps
from time import sleep


