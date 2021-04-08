number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in number_list:
    print("Number - " + str(number))

for number in number_list:
    if number % 2 == 0:
        print(f"Number {number} is even")
    else:
        print(f"Number {number} is odd")

greeting = "Hello Python"
for letter in greeting:
    if letter != "o":
        print(letter)

tuple_list = [("a", "b"), ("c", "d"), ("e", "f")]
for item in tuple_list:
    print(item)
for letter_1, letter_2 in tuple_list:
    print(letter_1, letter_2)
for letter_1, letter_2 in tuple_list:
    print(letter_1)

tuple_list_1 = [("a", "b", 1), ("c", "d", 4), ("e", "f", 5)]
for letter_1, letter_2, number in tuple_list_1:
    print(letter_1, letter_2, number)

dictionary = {"key1": "value1", "key2": "value2", "key3": "value3"}
for item in dictionary:
    print(item)
for item in dictionary.items():
    print(item)
for item in dictionary.keys():
    print(item)
for item in dictionary.values():
    print(item)

for key, value in dictionary.items():
    print(key, value)

for x in range(5):
    print(x)

sum = 0
for i in range(10, 31):
    if i % 2 == 0:
        sum += i
print(sum)


for x in range(int(input("Enter number: "))):
    print("Hello")