from types import MappingProxyType
import random
from enum import Enum

class GameState(Enum):
    Start = 0
    Terminated = 1
    Lost = 2



def balance_input_validation():
    while True:
        try:
            balance:str = input('Enter your starting balance: $ ')

            if balance.isalpha() or (not balance):
                raise ValueError('Please enter a valid number.')
            if int(balance) <= 0:
                raise ValueError('Balance must be a positive number.')
            return int(balance)

        except ValueError as e:
            print(e)

def bet_amount_input_validation(balance):

    while True:
        try:
            bet_amount:str = input('Enter your bet amount: $ ')

            if bet_amount.isalpha() or (not bet_amount):
                raise ValueError('Please enter a valid number for the bet amount.')
            if int(bet_amount) <= 0 or int(bet_amount) > balance:
                raise ValueError(f'Invalid bet amount. You can bet btn $1 and ${balance}.')
            return int(bet_amount)
        except ValueError as e:
            print(e)



def if_won(rand_fruits,bet_amount):
    print('|'.join(rand_fruits))
    amount_won = 0

    # if all(i == rand_fruits[0] for i in rand_fruits):  alternative
    #     print('You won!')
    # else:
    #     print('You lost!')

    if len(set(rand_fruits)) <= 1:  # checks if all fruits match
        amount_won = 10*bet_amount
        print(f'You won ${amount_won}!')

    elif len(rand_fruits) != len(set(rand_fruits)):   #checks if at least two fruits match ie If lengths are different, a duplicate exists
        amount_won = 2*bet_amount
        print(f'You won ${amount_won}!')
    else:
        print('You lost')

    return amount_won

def main():

    NUMBER_TO_SELECT:int = 3
    current_balance = 0
    state:GameState = GameState.Start

    # makes the dictionary immutable in runtime, cos i this case i am using the unicodes fo the emojis
    EMOJIS_UNICODE = MappingProxyType({    
        'strawberry': "\U0001F353",
        'banana': "\U0001F34C",
        'red_apple': "\U0001F34E",
        'water_melon': "\U0001F349",
        'cherries': "\U0001F352"
    })

    balance:int = balance_input_validation()
    current_balance += balance
    

    print('Welcome to the Slot Machine Game !')
    print(f'You start with a balance of {balance}')

    while True:
        
        print(f'Current balance: ${current_balance}')
        bet_amount:int = bet_amount_input_validation(balance)

        if bet_amount:
            current_balance -= bet_amount
        

        rand_fruits = random.sample(list(EMOJIS_UNICODE.values()),k = NUMBER_TO_SELECT)
        amount_won = if_won(rand_fruits,bet_amount)

        if amount_won:
            current_balance += amount_won

        if current_balance <= 0:
            state = GameState.Lost
            break
        
        play_again = input('Do you want to play again? (y/n): ').lower().strip()

        if play_again != 'y':
            state = GameState.Terminated
            break
        
    if state == GameState.Lost:
        print(f'Current balance: {current_balance}.\n You are out of money! Game Over.')
    else:
        print(f'Thanks for playing!')




if __name__ == '__main__':
    main()