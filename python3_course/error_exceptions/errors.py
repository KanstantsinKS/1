# SyntaxError
# des func():
#   print("Text")

# NameError
# print(x)

# TypeError
# len(12)
# my_list = []
# print(my_list + "Hello")

# IndexError
# my list = [1, 2]
# print(my_list[4])

# ValueError
# print(int('43'))
# print(int('hi'))
# print(int([43]))

# KeyError
# my_dict = {1: 'apple', 2: 'orange'}
# print(my_dict[3])

# AttributeError
# 'red'.attr()



# Raising Errors

# raise ValueError('My invalid value')
# raise ValueError

# def gat_rainbow_color(color_number):
#     color_number_list = [1, 2, 3]
#     if type(color_number) is not int:
#         raise TypeError(f'Color number must be integer type')
#
#     if color_number not in color_number_list:
#         raise ValueError(f'Color number must be in range of integer from 1 to 7')
#
#     if color_number == 1:
#         print('red')
#     elif color_number == 2:
#         print('orange')
#     elif color_number == 3:
#         print('green')
#
# gat_rainbow_color(1)
# gat_rainbow_color(2)
# gat_rainbow_color("hi")

# def colorize_text(color_number, text):
#     color_number_list = [1, 2, 3]
#     if type(color_number) is not int:
#         raise TypeError(f'Color number must be integer type')
#
#     if color_number not in color_number_list:
#         raise ValueError(f'Color number must be in range of integer from 1 to 7')
#
#     if type(text) is not str:
#         raise TypeError(f'Text must be str type')
#
#     if color_number == 1:
#         print('red')
#     elif color_number == 2:
#         print('orange')
#     elif color_number == 3:
#         print('green')
#
# colorize_text(1, "hi")
# colorize_text(2, "hi")
# colorize_text(2, 2)



# try except

# print('Some code')
# try:
#     print(len(24))
#     print(some_variable)
# except NameError:
#     print('NameError with variable')
# except TypeError:
#     print('TypeError with variable')
# print('Code after error')


# some_dict = {'first_name': 'Jack', 'last_name': 'White', 'age': 24}
# print(some_dict['last_name'])
# # print(some_dict['name'])
#
# def get_dict(dict, key):
#     try:
#         return dict[key]
#     except KeyError:
#         return None
#
# print(get_dict(some_dict, 'age'))
# print(get_dict(some_dict, 'a'))


# else finally

# if we have an error - except block fires and else block doesn't fire
# if we haven't an error - except block doesn't fire and else block fires
# finally block fires anyway
# while True:
#     try:
#         number = input('enter some number ')
#         print(int(number) / 2)
#     except:
#         print("Enter a number")
#     else:
#         print('Good number!')
#         break
#     finally:
#         print('Finally block')
#
# print('code after error handling')


def divide(x, y):
    try:
        print(x / y)
    except ZeroDivisionError as e:
        print('You can\'t divide by zero')
        print(e)
    except TypeError as e:
        print('x, y must be numbers')
        print(e)
    else:
        print('x divided by y')
    finally:
        print('finally block')


divide(3, 4)
print()
divide(3, 0)
print()
divide(3, 'ho')
