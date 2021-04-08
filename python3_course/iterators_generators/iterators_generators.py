# Iterate

# number_list = [1, 2, 3, 4, 5]
#
# for number in number_list:
#     print(number)
#
# for letter in 'my string':
#     print(letter)

# # Iterators

# number_list_iterator = iter(number_list)
# print(type(number_list_iterator))
#
# string_iterator = iter('my string')
# print(type(string_iterator))

# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())

# print(next(number_list_iterator))

# def my_for_loop(iterable):
#     iterator = iter(iterable)
#     print(iterator.__next__())
#     print(next(iterator))
#
# my_for_loop('hello')


# def my_for_loop(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(next(iterator))
#         except StopIteration:
#             print("Iter finished")
#             break
#
# my_for_loop('hello')
# my_for_loop((1, 2, 3))

# Custom Iterable

# class MyRange:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.current = start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current < self.end:
#             number = self.current
#             self.current += 1
#             return number
#         raise  StopIteration
#
# first_range = MyRange(1, 10)
# iter(first_range)
# for number in first_range:
#     print(number)


# Generators
# All Generators are Iterators
# Generators can be created with generator functions
# Generatorr can be created with generator expressions

# def my_func(x):
#     return x

# print(my_func(4))

# def count_up_to(x):
#     count = 1
#     while count <= x:
#         yield count
#         count += 1

# print(count_up_to(4))
# counter = count_up_to(4)
# print(counter.__next__())
# print(counter.__next__())
# print(next(counter))
# print(next(counter))

# for number in count_up_to(10):
#     print(number)

# counter = count_up_to(10)

# for number in counter:
#     print(number)

# counter.__next__()
# counter.__next__()
# for number in counter:
#     print(number)

# counter = list(count_up_to(10))
# print(counter)


# def get_week_day():
#     week_day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
#     for day in week_day:
#         yield day

# current_day = get_week_day()

# print(current_day.__next__())  # 'Sunday'
# print(current_day.__next__())  # 'Monday'
# print(current_day.__next__())  # 'Tuesday'
# print(current_day.__next__())  # 'Wednesday'
# print(current_day.__next__())  # 'Thursday'
# print(current_day.__next__())  # 'Friday'
# print(current_day.__next__())  # 'Saturday'


# def even_odd():
#     for i in range(0, 4):
#         if i % 2 == 0:
#             yield i, 'even'
#         else:
#             yield i, 'odd'

# even_odd_generator = even_odd()
# print(next(even_odd_generator)) # 'even'
# print(next(even_odd_generator)) # 'odd'
# print(next(even_odd_generator)) # 'even'
# print(next(even_odd_generator)) # 'odd'


# Infinite process

# def create_patterns():
#     max_pattern_number = 100
#     patterns = ('first', 'second', 'third', 'forth')
#     i = 0
#     result_list = []
#     while len(result_list) < max_pattern_number:
#         if i >= len(patterns):
#             i = 0
#         result_list.append(patterns[i])
#         i += 1
#     return result_list
#
# print(create_patterns())

# def get_corrent_pattern():
#     patterns = ('first', 'second', 'third', 'forth')
#     i = 0
#     while True:
#         if i >= len(patterns):
#             i = 0
#         yield patterns[i]
#         i += 1

# corrent_pattern = get_corrent_pattern()
# print(next(corrent_pattern))
# print(next(corrent_pattern))
# print(next(corrent_pattern))
# print(next(corrent_pattern))
# print(next(corrent_pattern))


# def square_of_integer_numbers():
#     number = 1
#     while True:
#         yield number ** 2
#         number += 1

# integer_square_generator = square_of_integer_numbers()

# print(next(integer_square_generator)) # 1
# print(next(integer_square_generator)) # 4
# print(next(integer_square_generator)) # 9
# print(next(integer_square_generator)) # 16


# Generator expressions

# def get_number_from_range():
#     for number in range(10):
#         yield number

# counter = get_number_from_range()
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# counter1 = (number for number in range(10))
# print(next(counter1))
# print(next(counter1))
# print(next(counter1))
# print(next(counter1))
# print(next(counter1))

# counter2 = [number for number in range(10)]

# print(counter)
# print(counter1)
# print(counter2)


