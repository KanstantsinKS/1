greeting = "Hello!"
letter_list = []
for letter in greeting:
    letter_list.append(letter)
print(letter_list)

letter_list1 = [letter for letter in greeting]
print(letter_list1)

number_list = [number for number in "01234565789"]
print(number_list)

number_list_1 = [num for num in range(0, 10)]
print(number_list_1)

number_list_2 = [num ** 2 for num in range(0, 10)]
print(number_list_2)

number_list_3 = [-((num - 3) / 2) ** 2 for num in range(0, 10)]
print(number_list_3)

number_list_4 = [6, 43, -2, 11, 0, -55, -12, 3, 345]
new_list = [num for num in number_list_4 if num > 0]
print(new_list)

new_list_1 = ["+" if num > 0 else "-" if num < 0 else "zero" for num in number_list_4]
print(new_list_1)

# Из исходного списка greetings = ['hello', 'hi', 'hey', 'hola'] создайте новый список содержащий вторую
# букву из # каждой # строки исходного списка. Выведите новый список на печать.
# Решите задание двумя способами - при помощи List Comprehension и без него.
greetings = ['hello', 'hi', 'hey', 'hola']
new_greetings = []
for letter in greetings:
    new_greetings.append(letter[1])
print(new_greetings)

new_greeting = [letter[1] for letter in greetings]
print(new_greeting)

# With List Comprehension
greetings = ['hello', 'hi', 'hey', 'hola']
letter_list = [greeting[1] for greeting in greetings]
print(letter_list)

# Without List Comprehension
greetings = ['hello', 'hi', 'hey', 'hola']
letter_list = []
for greeting in greetings:
    letter_list.append(greeting[1])
print(letter_list)




# Из исходного списка digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] создайте новый список содержащий нечетные
# числа исходного списка. Выведите новый список на печать.
# Решите задание двумя способами - при помощи List Comprehension и без него.

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_digits = []
for num in digits:
    if num % 2 == 1:
        new_digits.append(num)
print(new_digits)

new_digit = [num for num in digits if num % 2 == 1]
print(new_digit)