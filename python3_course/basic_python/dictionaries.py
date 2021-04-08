car_prices = {"Opel": 5000, "Toyota": 7000, "BMV": 10000}
print(car_prices)
print(f"BMV price -", car_prices["BMV"])
car_prices["Mazda"] = 4000
car_prices["Opel"] = 2000
print(car_prices)

del car_prices["Toyota"]
print(car_prices)

car_prices.clear()
print(car_prices)


person = {
    "first name": "Jack",
    "last name": "Brown",
    "age": 43,
    "hobbies": ["football", "singing"],
    "children": {"son": "Michael", "daughter": "Pamela"}
}

print(person["age"])
print(person["hobbies"])
hobbies = person["hobbies"]
print(hobbies[1])
print(person["hobbies"][1])
print(person["children"]["son"])

person["car"] = "Mazda"
print(person)
person["hobbies"][0] = "games"
person["hobbies"].append("basketball")
print(person)

print(person.keys())
print(person.values())
print(person.items())


dictionary = {
    "name": "Jack",
    "age": 23,
    "car": "BMW"
}
print(dictionary["name"])

computer_dictionary = {
    "CPU": "2 Ghz",
    "core": 8,
    "RAM": "8192 Gb",
    "GPU": "2048 Mb",
    "SSD": "256 Gb",
    "HDD": "2 Tb"
}
print(computer_dictionary)