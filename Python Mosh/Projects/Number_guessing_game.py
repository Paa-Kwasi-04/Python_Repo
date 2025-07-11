import random as r

random_number = r.randint(1, 100)

while True:

    choice = input('Guess the number between 1 and 100: ')

    if choice.isnumeric():
        if int(choice) == random_number:
            print('Congratulations! You guessed the number')
            break

        elif int(choice) != random_number:
            if int(choice) > random_number:
                print('Too high!')
            else:
                print('Too low!')

    else:
        print('Please enter a valid number')


# Mosh used try and except instead which is way better
