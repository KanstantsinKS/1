for x in range(3, 11, 2):
    print(x)

print(range(5))
print(list(range(5)))

letter_index = 0
my_string = "asdgre"
for letter in my_string:
    print(f"{letter} is at index {letter_index}")
    letter_index += 1

for item in enumerate(my_string):
    print(item)

for index, letter in enumerate(my_string):
    print(f"{letter} is at index {index}")

print("a" in "Jack")

letter_list = ["a", "b", "c", "d"]
print(1 in letter_list)
print("d" in letter_list)

dict_1 = {1: "a", 2: "b", 3: "c"}
print(1 in dict_1)
print("c" in dict_1)
print("c" in dict_1.values())

print(min(1.1, 12, 0.325, 5))
print(max(1.1, 12, 0.325, 5))

num_list = [12, 43, 125, 666]
print(max(num_list))

for letter in "Hello":
    print(ord(letter))

from random import shuffle
shuffle(num_list)
print(num_list)

from random import randint
print(randint(1, 20))
