def print_greeting():
    """
    Print text "Hello!"
    return: None
    """
    print("Hello!")
print_greeting()
help(print_greeting)

def print_greeting_with_name(name = "Name"):
    """
    Print text greeting with name
    :param: name
    :return: None
    """
    print(f"Hello {name}!")
print_greeting_with_name("Jack")
print_greeting_with_name()

def sum_of_two_numbers(a = 0, b = 0):
    """
    Function return sum of two addend
    :param a: first addend
    :param b: second addend
    :return: sum of a and b
    """
    return a + b
x = sum_of_two_numbers(1, 5)
print(x)

def greeting_depends_on_gender(name, gender):
    if gender == "male":
        print(f"hello {name}! You look great!")
        return gender
    elif gender == "female":
        print(f"hello {name}! You are so nice!")
        return gender
    else:
        print(f"hello {name}! I've never seen the creature like ypu!")
        return gender

greeting_depends_on_gender("Jack", "male")
greeting_depends_on_gender("Jane", "female")
greeting_depends_on_gender("Ja", "cale")


def cat_voice():
    return "Meow! " * 2
print(cat_voice())
def dog_voice():
    return print("Woof! " * 2)
dog_voice()

def get_voice(text):
    return print(f"{text}!")
get_voice("hi")

def odd_list(a, b):
    list = []
    for i in range(a, b + 1):
        if i % 2 == 1:
            list.append(i)
    return print(list)
odd_list(1, 10)

def odd_list_comprehension(a, b):
    list = [i for i in range(a, b + 1) if i % 2 == 1]
    return print(list)
odd_list_comprehension(1, 6)

def get_odd_number_list(a, b):
    number_list = list(range(a, b + 1))
    odd_number_list = [number for number in number_list if number % 2 == 1]
    return odd_number_list

print(get_odd_number_list(1, 5))