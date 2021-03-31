x = 1
y = 2

print(x > 1)
print(y > 1)
print()

# and, or, not
print(x > 1 and y > 1)
print(x >= 1 and y > 1)
print()

print(x > 1 or y > 1)
print(x > 1 or y < 1)
print()

print(not x > 1)
print(not y > 1)
print()

print(True and True)
print(True or True)
print(not True)
print()

print(False and False)
print(False or False)
print(not False)
print()

print(True and False)
print(True or False)
print()
print()

name = "John"
age = 18
is_marred = False

if age >= 18 and not is_marred:
    print(f"Hello {name}! You can find a girl of your dream here!")
else:
    print(f"Sorry, you can't do this.")
print()
print()

# if, elif, else
x = 2

if x > 3:
    print("x > 3")
elif x < 3:
    print("x < 3")
    print("Good")
else:
    print("x = 3")
print()

day_time = "afternoon"

if day_time == "morning":
    print("Monster wakes up")
elif day_time == "afternoon":
    print("Monster is walking")
elif day_time == "evening":
    print("Monster is eating")
elif day_time == "night":
    print("Monster is sleppeng")
else:
    print("Monster is doing something")
print()

x = 45
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")


lucky_number = int(input("Enter any number: "))
if lucky_number == 7:
    print("7 is a lucky number! Today is your lucky day!")
else:
    print("Thank you! Have a nice day!")

number = int(input("Enter an integer number: "))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
