rainbow_colors = {"red", "orange", "yellow", "green", "blue", "indigo", "violet"}
print(rainbow_colors)
print(type(rainbow_colors))

empty_set = set()
print(empty_set)
print(type(empty_set))

number_list = [1, 2, 3, 36]
text_tuple = {"sfds", "hi", "hello", "hi", "hi"}
set_from_list = set(number_list)
set_from_tuple = set(text_tuple)

print(set_from_list)
print(type(set_from_list))
print(set_from_tuple)
print(type(set_from_tuple))

set_from_list.add(777)
set_from_tuple.add("me")

print(set_from_list)
print(set_from_tuple)


set_from_list.pop()
print(set_from_list)
set_from_list.remove(36)
print(set_from_list)
set_from_list.discard(7)
print(set_from_list)
set_from_list.clear()
print(set_from_list)


some_text = "Hi, my name is Petr"
some_set = set(some_text)  # create set
x = some_set  # assign value set to variable
print("Variable x have a value -", x)
print("Variable x have -", type(x))

letters_set = set('Создайте множество при помощи функции set() '
                  'из текста, чтобы получить уникальные символы, '
                  'содержащиеся в тексте.')
print(letters_set)
print(type(letters_set))