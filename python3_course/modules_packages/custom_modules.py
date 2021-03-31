import greetings

greetings.func_hello()
greetings.func_hi()

from greetings import func_hello
func_hello()

color = greetings.get_favorite_color()
number = greetings.get_favorite_number()
print(color, number)
