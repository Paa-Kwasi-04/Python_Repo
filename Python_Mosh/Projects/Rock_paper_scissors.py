import random as r

Rock = 'r'
Paper = 'p'
Scissors = 's'
emojis = {Rock: 'Rock', Paper: 'Paper', Scissors: 'Scissors'}
choices = tuple(emojis.keys())


def get_user_input():
    while True:
        user_choice = input('Rock,paper or scissors? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid choice')


def print_choice(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')


def result(user_choice, computer):
    if user_choice == computer:
        print('Tie!')
    elif (
        (user_choice == Rock and computer == Scissors) or
        (user_choice == Scissors and computer == Paper) or
            (user_choice == Paper and computer == Rock)):
        print('You win')
    else:
        print('You lose')


def play_game():
    while True:

        user_choice = get_user_input()

        computer = r.choice(choices)

        print_choice(user_choice, computer)

        result(user_choice, computer)

        should_continue = input('Continue? (y/n): ').lower()
        if should_continue == 'n':
            print('Thanks for playing!')
            break


play_game()
