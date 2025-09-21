

for x in range(1, 51):
    if x % 3 == 0 and x % 5 == 0:  # Since it is short circuit in nature
        print('FizzBuzz', x)
    elif x % 3 == 0:
        print('Fizz', x)
    elif x % 5 == 0:
        print('Buzz', x)
