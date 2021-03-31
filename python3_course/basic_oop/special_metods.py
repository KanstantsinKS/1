# special (magic) methods __method_name__

# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def __str__(self):
#         return self.first_name + " " + self.last_name + " " + str(self.age) + " age"
#
#     def __len__(self):
#         return self.age
#
#     def __del__(self):
#         print(f'Person object with name {self.first_name} is deleted from memory')
#
#     def __add__(self, other):
#         return self.age + other.age
#
# jack = Person('Jack', 'White', 45)
# jane = Person('Jane', 'White', 43)
#
# print(len([1, 2, 3, 4, 5]))
# print(jack)
# print(len(jack))
# # del(jack)
#
# x = 5
# y = 3
# a = '5'
# b = '3'
# print(x + y)
# print(jack + jane)
# print(x.__add__(y))
# print(jack.__add__(jane))


class Chain:
    def __init__(self, number_of_items):
        self.number_of_items = number_of_items

    def __str__(self):
        return f'Chain with {self.number_of_items} items'

    def __len__(self):
        return self.number_of_items

ch = Chain(2)
print(ch)
print(len(ch))


