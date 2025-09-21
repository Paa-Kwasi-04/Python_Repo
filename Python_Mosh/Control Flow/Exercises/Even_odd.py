
while True:
    number = (input('Enter number: '))

    if number.isnumeric():
        number = int(number)
        message = 'Even' if number % 2 == 0 else 'Odd'

        print(f'It is {message}')
    else:
        print(f'{number} is not a number')
        break
