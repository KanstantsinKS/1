nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 0]]
print(nested_list)
print(len(nested_list))
print(len(nested_list[2]))
print(len(nested_list[-1]))
print(nested_list[1][1])
print(nested_list[-2][-2])
print(nested_list[1][-2])
print(nested_list[-2][1])

for inner_list in nested_list:
    print(inner_list)

for inner_list in nested_list:
    for number in inner_list:
        print(number)
print()
print()

[[print(number) for number in inner_list] for inner_list in nested_list]

