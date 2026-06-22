from pathlib import Path
import random
from enum import Enum


class GameStatus(Enum):
    LOST = 0
    WON = 1



def read_words():

    script_dir = Path(__file__).parent

    file_path = script_dir / 'word.txt'
    try:
        with open(file_path,'r') as word_file:
            words = word_file.readlines()

            if not words:
                raise ValueError(f'Empty {file_path} document')

        stripped_words = [word.strip() for word in words]
    except FileNotFoundError:
        return False, f'Error: The file {file_path} was not found.'
    except ValueError as e:
        return False, e

    return True, stripped_words

def random_word(words:list):
    chosen_word = random.choice(words)

    return chosen_word



def word_guessing(chosen_word:str)->GameStatus:

    number_of_attempts:int = 6 
    used_letters = []
    word_so_far = ['_' for i in chosen_word]
    

    while True:
        try:
            letter:str = input('Enter a letter: ').strip().lower()
            

            if not letter:
                raise ValueError('Input is empty')
            if len(letter) > 1:
                raise ValueError('Enter only one letter')
            if not letter.isalpha():
                raise ValueError('Enter only letters from a to z')


            if letter in chosen_word:

                if letter not in used_letters:
                    used_letters.append(letter)
                    #number_of_attempts -= 1
                else:
                    raise ValueError('You already guessed that letter')

                print('Good guess')
                for index,x in enumerate(chosen_word):
                    if letter == x:
                        word_so_far[index] = letter
                
            else:
                print('Wrong guess')
                number_of_attempts -= 1

            print(''.join(word_so_far))

            if '_' not in word_so_far:
                if ''.join(word_so_far) == chosen_word:
                    status:GameStatus = GameStatus.WON
                    return status


            if number_of_attempts == 0:
                status:GameStatus = GameStatus.LOST
                return status

            print(''.join(word_so_far))
            
                 
        except ValueError as e:
            print(e)





def main():
    try:
        state, words = read_words()

        if state:
            rand_word:str = random_word(words)
            status:GameStatus = word_guessing(rand_word)

            if status == GameStatus.WON:
                print('You have won the game')
            elif status == GameStatus.LOST:
                print(f'Game Over! The word was {rand_word}')
        else:
            raise ValueError(words)
    except KeyboardInterrupt:
        print('\nGame interrupted by user. Goodbye!')
    except ValueError as e:
        print(e)

    

if __name__ == '__main__':
    main()