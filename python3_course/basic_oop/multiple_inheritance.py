class Swimable:
    def __init__(self, name):
        print('Init() of Swimable()')
        self.name = name

    def greeting(self):
        print(f'Hello! My name is {self.name} and I can swim')

    def swim(self):
        print('I\'m swiming')


class Walkable:
    def __init__(self, name):
        print('Init() of Walkable()')
        self.name = name

    def greeting(self):
        print(f'Hello! My name is {self.name} and I can walk')

    def walk(self):
        print('I\'m walking')


class Flyable:
    def __init__(self, name):
        print('Init() of Flyable()')
        self.name = name

    def greeting(self):
        print(f'Hello! My name is {self.name} and I can fly')

    def fly(self):
        print('I\'m flying')


class GameCharacter(Swimable, Walkable, Flyable):
    def __init__(self, name):
        print('Init() of GameCharacter()')
        self.name = name
        Swimable.__init__(self, name)
        Walkable.__init__(self, name)
        Flyable.__init__(self, name)

    def greeting(self):
        print(f'Hello! My name is {self.name} and I can swim, walk and fly')


james = GameCharacter('James')
james.greeting()
james.swim()
james.walk()
james.fly()

# print(isinstance(james, Walkable))
# print(isinstance(james, Swimable))
# print(isinstance(james, Flyable))
# print(isinstance(james, GameCharacter))
# print(isinstance(james, object))
