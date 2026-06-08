print('Press 0 to Exit\n')
while True:
    number = int(input('Enter a number> '))

    if number >= 1:

        for x in range(2, number):
            if number % x == 0:
                prime = False
                break
        else:  # since it runs true and doesn't break it means it is prime so the else block
            prime = True

        if prime:
            print(f'{number} is prime')
        else:
            print(f'{number} is not prime')

    elif number == 0:
        break

    else:
        print(f'{number} is not a positive integer')


print('Program Ended')
