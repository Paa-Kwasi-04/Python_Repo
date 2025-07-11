# *args produces a tuple which is iterable
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


multiply(2, 3, 4, 5)


# **args produces a dictionary which is iterable
def save_user(**user):
    print(user['name'])


save_user(id=1, name='John', age=22)
