def divede(a, b):
    assert b != 0, 'b must not equals zero'
    return a / b

print(divede(2, 2))
# print(divede(2, 0))


def multiply_positive_numbers(a, b):
    assert a > 0 and b > 0, 'a and b must be positive'
    print(a * b)

multiply_positive_numbers(2, 5)
# multiply_positive_numbers(3, -3)


def get_access(password):
    pasword_list = [111, 222, 333]
    assert int(password) in pasword_list, 'Password is invalid'
    print('You can make dangerous stuff')

pass_1 = input('Please input the password: ')
get_access(pass_1)


