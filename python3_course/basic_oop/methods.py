class Car:

    wheels_number = 4

    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

    def drive(self, city):
        print(f'{self.model} is driving to {city}')

    def change_color(self, new_color):
        self.color = new_color

opel_car = Car('Opel', 'grey', 1998)
mazda_car = Car('Mazda', 'red', 2000)

opel_car.drive('London')
mazda_car.drive('York')

print(mazda_car.color)
mazda_car.change_color("blue")
print(mazda_car.color)


class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def get_area(self):
        return self.pi * (self.radius ** 2)

circle_1 = Circle()
print(circle_1.get_area())
circle_2 = Circle(3)
print(circle_2.get_area())


class BankAccount:

    balance = 0.0

    def __init__(self, client_id, client_first_name, client_last_name):
        self.client_id = client_id
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name

    def add(self, sum):
        self.balance += sum
        return self.balance

    def withdraw(self, sum):
        self.balance -= sum
        return self.balance

person = BankAccount("001", "Jack", "Smith")
print(f'Balance {person.client_first_name} {person.client_last_name} ID {person.client_id} - {person.add(200)} $')
print(f'Balance {person.client_first_name} {person.client_last_name} ID {person.client_id} - {person.withdraw(50)} $')


class Gamer:

    active_gamers = 0

    @classmethod
    def get_active_gamers(cls):
        return Gamer.active_gamers

    @classmethod
    def gamer_from_string(cls, data_string):
        nickname, age, level, points = data_string.split(',')
        return cls(nickname, age, level, points)


    def __init__(self, nickname, age, level, points):
        self.nickname = nickname
        self.age = age
        self.level = level
        self.points = points
        Gamer.active_gamers += 1

    def get_nickname(self):
        return self.nickname

    def get_age(self):
        return self.age

    def get_level(self):
        return self.level

    def get_points(self):
        return self.points

    def is_adult(self):
        return self.age >= 18

    def get_adult_level(self):
        if self.is_adult():
            print('You can go to adult level')
        else:
            print('You can\'t go to adult level')

    def logout(self):
        Gamer.active_gamers -= 1


print(Gamer.active_gamers)
gamer_1 = Gamer("Nick", 23, 5, 13)
print(Gamer.active_gamers)
gamer_2 = Gamer('Pol', 15, 10, 23)
print(Gamer.active_gamers)

print(gamer_1.get_age())
gamer_1.get_adult_level()

print(gamer_2.get_age())
gamer_2.get_adult_level()

print(Gamer.active_gamers)

gamer_2.logout()
print(Gamer.get_active_gamers())

jack = Gamer.gamer_from_string('Jack, 34, 2, 15')
jane = Gamer.gamer_from_string('Jane, 24, 3, 5')
print(jack.get_age())
print(jane.get_level())
print(Gamer.active_gamers)