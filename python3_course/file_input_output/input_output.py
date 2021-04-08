# # Input
# x = input('Input something ')
#
# # Output
# print(f'Output something {x}')

# Open, close file
# lorem_ipsum_text = open('sample.txt', "r")
# for line in lorem_ipsum_text:
#     print(line, end="")
# lorem_ipsum_text.close()

# lorem_ipsum_text = open('sample.txt', "r")
# for line in lorem_ipsum_text:
#     if 'mary' in line.lower():
#         print(line, end="")
# lorem_ipsum_text.close()

# with open('sample.txt', 'r') as lorem_ipsum_text:
#     for line in lorem_ipsum_text:
#         if 'mary' in line.lower():
#             print(line, end="")
#     line = lorem_ipsum_text.readline()
#     while line:
#         print(line, end="")
#         line = lorem_ipsum_text.readline()

# with open('sample.txt', 'r') as lorem_ipsum_text:
#     lines = lorem_ipsum_text.readlines()
# print(lines)
#
# for line in lines[::-1]:
#     print(line, end='')

# with open('sample.txt', 'r') as lorem_ipsum_text:
#     text = lorem_ipsum_text.read()
# print(text)

# Writing in file
# colors_list = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
# with open('rainbow_colors.txt', 'w') as rainbow_colors:
#     for color in colors_list:
#         print(color, file=rainbow_colors)
# rainbow_colors.close()
#
# colors_list_1 = []
# with open('rainbow_colors.txt', 'r') as rainbow_colors:
#     for color in rainbow_colors:
#         colors_list_1.append(color.strip('\n'))
# print(colors_list_1)
# rainbow_colors.close()
#
# with open('rainbow_colors.txt', 'a') as rainbow_colors:
#     print('dark green', file=rainbow_colors)
#     print('dark blue', file=rainbow_colors)
# rainbow_colors.close()
#
# colors_list_1 = []
# with open('rainbow_colors.txt', 'r') as rainbow_colors:
#     for color in rainbow_colors:
#         colors_list_1.append(color.strip('\n'))
# print(colors_list_1)
# rainbow_colors.close()

# # Read and write binary files
# x = 127  # pow(10, 2) pow(10, 1) pow(10, 0)
# print(1 * pow(10, 2) + 2 * pow(10, 1) + 7 * pow(10, 0))
# y = 1035
# print(1 * pow(10, 3) + 0 * pow(10, 2) + 3 * pow(10, 1) + 5 * pow(10, 0))
#
# # pow(2, 2) pow(2, 1) pow(2, 0)
# x = 0b101  # pow(10, 2) pow(10, 1) pow(10, 0)
# print(1 * pow(2, 2) + 0 * pow(2, 1) + 1 * pow(2, 0))
# y = 0b0110
# print(0 * pow(2, 3) + 1 * pow(2, 2) + 1 * pow(2, 1) + 0 * pow(2, 0))
#
# print(x, y)
#
# # 0x11
# z = 0x11
# print(z)
# print(1 * pow(16, 1) + 1 * pow(16, 0))
# z = 0xa1
# print(z)
# print(10 * pow(16, 1) + 1 * pow(16, 0))
# z = 0x2cf1
# print(z)
# print(format(z, '0>42b'))
# print(0b000000000000000000000000000010110011110001)
# print(2 * pow(16, 3) + 12 * pow(16, 2) + 15 * pow(16, 1) + 1 * pow(16, 0))

# # Write binary files
# with open('binary', 'bw') as binary:
#     for number in range(21):
#         binary.write(bytes([number]))
#
# with open('binary', 'bw') as binary:
#     binary.write(bytes(range(21)))
#
# with open('binary', 'br') as binary:
#     for number in binary:
#         print(number)

# # Module pickle
# import pickle
#
# honda = (
#     'Civic',
#     'grey',
#     '2009',
#     (
#         (1, 'James Brown'),
#         (2, 'Jane White'),
#         (3, 'Jake Smith')
#     )
# )
#
# models = ['civic', 'accord', 'pilot']
# owners = ['James Brown', 'Jane White', 'Jake Smith']
#
# with open('honda.pickle', 'wb') as honda_file:
#     pickle.dump(honda, honda_file)
#     pickle.dump(models, honda_file)
#     pickle.dump(owners, honda_file)
#     pickle.dump(9999999, honda_file)
#
# with open('honda.pickle', 'rb') as honda_file:
#     honda_from_file = pickle.load(honda_file)
#     models = pickle.load(honda_file)
#     owners = pickle.load(honda_file)
#     a = pickle.load(honda_file)

# print(honda_from_file)
# model, color, year, owner_list = honda_from_file
# print(model)
# print(color)
# print(year)
# for owner in owner_list:
#     owner_number, owner_name = owner
#     print(owner_number, owner_name)

# print(honda_from_file)
# print(models)
# print(owners)
# print(a)


# Module Shelve
# import shelve

# with shelve.open('shelve_test') as cars:

    # cars['opel'] = 'Germany'
    # cars['ford'] = 'USA'
    # cars['mazda'] = 'Japan'
    # cars['renault'] = 'France'

    # print(cars['ford'])
    # print(cars['renault'])

    # cars["kia"] = "South Korea"

    # for key in cars:
    #     print(key + ":" + cars[key])

    # while True:
    #     key = input('Please enter a car name: ')
    #     if key == 'quit':
    #         break
    #     country = cars.get(key, f"We don't have a {key}")
    #     print(country)

    # while True:
    #     key = input('Please enter a car name: ')
    #     if key == 'quit':
    #         break
    #     if key in cars:
    #         country = cars[key]
    #         print(country)
    #     else:
    #         print(f"We don't have a {key}")

    # ordered_keys_list = list(cars.keys())
    # ordered_keys_list.sort()
    #
    # for key in ordered_keys_list:
    #     print(f'{key} {cars[key]}')

    # for value in cars.values():
    #     print(value)
    # print(cars.values())
    #
    # for key in cars.keys():
    #     print(key)
    # print(cars.keys())
    #
    # for item in cars.items():
    #     print(item)
    # print(cars.items())


# cars = shelve.open('shelve_test1')
#
# cars['opel'] = 'Germany'
# cars['ford'] = 'USA'
# cars['mazda'] = 'Japan'
# cars['renault'] = 'France'
#
# print(cars['ford'])
# print(cars)
# print(type(cars))
# cars.close()

# monday_schedule = ['math', 'python', 'english']
# tuesday_schedule = ['phisics', 'python', 'math']
# wednesday_schedule = ['html', 'python', 'russian']
# thursday_schedule = ['css', 'java', 'english']
# friday_schedule = ['football', 'russian', 'english']

# with shelve.open('schedules', writeback=True) as shedules:
    # shedules['monday_schedule'] = monday_schedule
    # shedules['tuesday_schedule'] = tuesday_schedule
    # shedules['wednesday_schedule'] = wednesday_schedule
    # shedules['thursday_schedule'] = thursday_schedule
    # shedules['friday_schedule'] = friday_schedule

    # shedules['thursday_schedule'].append('swiming')

    # temp_list = shedules['thursday_schedule']
    # temp_list.append('swiming')
    # shedules['thursday_schedule'] = temp_list
    #
    # shedules['wednesday_schedule'].append('running')
    #
    # for key in shedules:
    #     print(key, shedules[key])


# university = shelve.open('university_file')
# university['schedules'] = {
#         'monday_schedule': ['math', 'python', 'english'],
#         'tuesday_schedule': ['phisics', 'python', 'math'],
#         'wednesday_schedule': ['html', 'python', 'russian'],
#         'thursday_schedule': ['css', 'java', 'english'],
#         'friday_schedule': ['football', 'russian', 'english']
# }
# university["tutors"] = {
#         'math': ['Jack White', 'Jane Black'],
#         'pythom': ['Youra', 'Pethya']
# }
#
# print(university['schedules']['wednesday_schedule'])
# print(university['tutors']['math'])
# university.close()