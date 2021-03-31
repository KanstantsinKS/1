# inheritance

class Car:

    wheels_number = 4

    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year
        print('Car is created')

    def drive(self, city):
        print(f'{self.model} is driving to {city}')

    def change_color(self, new_color):
        self.color = new_color


class Truck(Car):

    wheels_number = 6

    def __init__(self, model, color, year):
        Car.__init__(self, model, color, year)
        print('Truck is created')

    def drive(self, city):
        print(f'Truck {self.model} is driving to {city}')

    def load_cargo(self, weight):
        print(f'The cargo is loaded. Weight is {weight} kg')

man_truck = Truck('Man', 'white', 2015)

man_truck.drive('York')
print(man_truck.wheels_number)
man_truck.load_cargo(2000)


# Polimorphism
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError('Class successor must implement this method')


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} is saying woof')


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} is saying meow')


class Fish(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} is saying nothing')


spike = Dog('Spike')
tom = Cat('Tom')
nemo = Fish('Nemo')
pet_list = [spike, tom]

for pet in pet_list:
    pet.speak()

print()


def pet_voice(pet):
    pet.speak()


pet_voice(spike)
pet_voice(tom)
pet_voice(nemo)


class GameCharacter:

    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def speak(self):
        print(f'Hi, my name is {self.name}')


class Villain(GameCharacter):

    def __init__(self, name, health, level):
        GameCharacter.__init__(self, name, health, level)

    def speak(self):
        print(f'Hi, my name is {self.name} and I will kill you')

    def kill(self, target):
        target.health = 0
        print('Bang-bang, now you\'re dead')


gamer = GameCharacter('Mat', 100, 1)
gamer2 = Villain('Tom', 100, 2)

gamer.speak()
gamer2.speak()
print(f'Health {gamer.name} = {gamer.health}')
gamer2.kill(gamer)
print(f'Health {gamer.name} = {gamer.health}')