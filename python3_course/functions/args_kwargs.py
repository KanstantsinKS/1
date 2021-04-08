def ten_percent_of_product(x, y):
    return (x * y) * 0.1

print(ten_percent_of_product(10, 20))

def ten_percent_with_args(*args):
    product = 1
    for number in args:
        product = product * number
    return product * 0.1

print(ten_percent_with_args(10, 20, 2, 4))

def ten_percent_of_product_with_args(percent, *args):
    product = 1
    for number in args:
        product = product * number
    return product / 100 * percent

print(ten_percent_of_product_with_args(10, 20, 2, 4))

def func_with_kwargs(**kwargs):
    print(kwargs)
func_with_kwargs(first=1, second=2)

def hello_with_kwargs(**kwargs):
    if "name" in kwargs:
        print(f"Hello! Nice to meet you {kwargs['name']}")
    else:
        print("Hello! What is you name&")

hello_with_kwargs(gender="male", age=24, name="Jack" )


def func_with_args_and_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)
    print(f"I would like to eat a {args[0]} {kwargs['food']}")

func_with_args_and_kwargs('one', 'two', drink='coffe', food='sandwich')


def is_cat_here(*args):
    lower_arg = [str(arg).lower() for arg in list(args)]
    if "cat" in lower_arg:
        return True
    else:
        return False
is_cat_here("At", "at", "dog")


def is_item_here(item, *args):
    if item in args:
        return True
    else:
        return False
is_item_here('sword', 'pen', 'ball', 'sword')


def your_favorite_color(my_color, **kwargs):
        if "color" in kwargs:
            print(f"My favorite color is {my_color}, but {kwargs['color']} is also pretty good!")
        else:
            print(f"My favorite color is {my_color}, what is your favorite color?")
your_favorite_color("red", age="22", color="blue")
