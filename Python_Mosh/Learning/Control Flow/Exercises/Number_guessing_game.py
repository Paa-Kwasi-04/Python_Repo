from random import randint

Random_number = randint(1, 10)
# print(Random_number)
count = 0

while True:

    count += 1
    Guess = int(input('Guess a number btn 1 and 10> '))

    if Guess == Random_number:
        print(f'You Won after {count} tries' if count >
              1 else f'You Won after {count} try')
        break

    print('Wrong \nTry Again')
