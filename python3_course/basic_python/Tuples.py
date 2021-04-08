tuple_1 = 1, 2, 3
tuple_2 = ("one", "two")
tuple_3 = (3, 2.3, "three")
print(tuple_1)
print(tuple_2)
print(tuple_3)

print(tuple_3[2])

new_tuple = (tuple_1[0], 3, tuple_1[2])
print(new_tuple)

x = y = z = 12
print(x, y, z)
x, y, z = 12, 13, 14
print(x, y, z)

person_tuple = ("John", "Smith", 1986)
print(person_tuple)
first_name, last_name, year_of_birth = person_tuple
print(first_name, last_name, year_of_birth)

t1 = (1, 2, 3, 1, 5, 9, "hi")
print(t1.count(1))
print(t1.count("hi"))
print(t1.index(5))
print(t1.index(1))

computer_tuple = ("CPU: 2 Ghz", "Core: 8", "RAM: 8192 Gb", "GPU: 2048 Mb", "SSD: 256 Gb", "HDD: 2 Tb")
print(computer_tuple)
cpu, core, ram, gpu, ssd, hdd = computer_tuple
print(cpu, core, ram, gpu, ssd, hdd)
