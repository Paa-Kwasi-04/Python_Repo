import random as r
count = 0

while True:
    choice = input('Roll the dice? (y/n):').lower()
    if choice == 'y':
        count += 1
        print((r.randint(1, 6), r.randint(1, 6)))

    elif choice == 'n':
        print('Thanks for playing!')
        break

    else:
        print('Invalid choice!')

print(f'You rolled the dice {count} number of times')
