number_list = [32, 21, 48, 34.56]
print(number_list)
some_list = [12, 35.334, "hello"]
print(some_list)
print(len(some_list))
print(some_list[1])

another_list = some_list[:2]
print(another_list)
some_list[2] = "hi"
print(some_list)

new_list = some_list + another_list
print(new_list)
new_list.append("new item")
print(new_list)

# added items
new_list.insert(0, "start")
new_list.insert(2, 13)
print(new_list)

# removing items
new_list.pop(-1)
new_list.pop(0)
new_list.pop(-3)
print(new_list)

deleted_item = new_list.pop()
print(new_list)
print(deleted_item)

deleted_item = new_list.remove(12)
print(new_list)
print(deleted_item)

number_list = [45, 12, 3, -455, 22]
letter_list = ["s", "w", "t", "a"]

print(number_list)
print(letter_list)

x = number_list.sort()
y = letter_list.sort()

print(number_list)
print(letter_list)
print(x)
print(y)

letter_list.sort()
new_letter_list = letter_list
print(new_letter_list)

number_list.append(letter_list)
print(number_list)
number_list.reverse()
letter_list.reverse()
print(number_list)
print(letter_list)


new_list = [3, 2.2, "abc", True]
print(new_list)
new_short_list = new_list[:3]
print(new_short_list)