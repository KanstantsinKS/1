from functools import wraps

# def prohibit_kwargs(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         if kwargs:
#             raise ValueError('OoO Keyword arguments are prohibited OoO')
#         return func(*args, **kwargs)
#     return wrapper
#
#
# def prohibit_int_kwargs(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         for value in args:
#             if type(value) == int:
#                 raise ValueError('Integer arguments are prohibited')
#         for key, value in kwargs.items():
#             if type(value) == int:
#                 raise ValueError('Integer arguments are prohibited')
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @prohibit_int_kwargs
# def print_hello(name):
#     print(f'Hello {name}!')
#
# print_hello('Jack')
# print_hello(name='Jack')
# print_hello(2)


def prohibit_more_than_2_args(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if len(args) >= 3:
            raise ValueError('Function must have less than 3 arguments!')
        else:
            return function(*args, **kwargs)
    return wrapper


@prohibit_more_than_2_args
def some_function(*args, **kwargs):
    print('Hello')


some_function(2, 3, name='Jack')
