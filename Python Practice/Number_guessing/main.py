"""
Number Guessing Game
-------------------
A simple game where players try to guess a randomly generated number within a specified range.
The game keeps track of high scores using a CSV file.

Functions
---------
csv_read()
    Read the scores database from a CSV file.

score_ranking()
    Get the highest scoring player from the records.

csv_write(Name, Score)
    Write a new score entry to the records CSV file.

computer_number(first, last)
    Generate a random number within specified bounds.

player_guess(first, last)
    Get and validate player's number guess.

main(limit, count, first, last)
    Run the main game loop.
"""
from random import randint
import pandas as pd
import os
FILEPATH = 'Number_guessing/Records.csv'

def csv_read() -> pd.DataFrame:
    """
    Read the game records from CSV file.

    Returns
    -------
    pd.DataFrame
        DataFrame containing player names and scores.
    """
    db = pd.read_csv(FILEPATH)
    return db


def score_ranking() -> pd.Series:
    """
    Get the highest scoring player (lowest number of attempts).

    Returns
    -------
    tuple
        Name and score of the highest scoring player.
    """
    db = csv_read()
    high_score = db[db['Score'] == db['Score'].min()]
    high_score = db[db['Score'] == db['Score'].min()]
    names = high_score['Name'].tolist()  # Convert to list
    score = high_score['Score'].iloc[0]  # Get first score as int
    return name, score                   # tuple of (str, int)


def csv_write(Name: str, Score: int) -> None:
    """
    Write a new score entry to the records file.

    Parameters
    ----------
    Name : str
        Player's name
    Score : int
        Number of attempts taken

    Returns
    -------
    None
    """
    
    # Check if file exists
    file_exists = os.path.isfile(FILEPATH)
    
    dbw = pd.DataFrame({'Name': [Name], 'Score': [Score]})
    
    if not file_exists:
        # Create new file with headers
        dbw.to_csv(FILEPATH, index=False)
    else:
        # Append to existing file without headers
        dbw.to_csv(FILEPATH, mode='a', index=False, header=False)


def computer_number(first, last) -> int:
    """
    Generate a random integer between two bounds.

    Parameters
    ----------
    first : int
        The lower bound of the range (inclusive).
    last : int
        The upper bound of the range (inclusive).

    Returns
    -------
    int
        A random integer between `first` and `last`.
    """
    number: int = randint(first, last)
    return number


def player_guess(first, last) -> int:
    """
    Prompt the player to guess a number within a specified range.

    Parameters
    ----------
    first : int
        The lower bound of the range (inclusive).
    last : int
        The upper bound of the range (inclusive).

    Returns
    -------
    int
        The player's guessed number.
    """
    while True:
        try:
            guess: int = int(input(f'Enter a number btn ({first},{last}):'))
            if first <= guess <= last:
                return guess
            raise ValueError(f'Number should be btn ({first},{last})')
        except Exception as e:
            print(e)
            continue


def main(limit: int, count: int, first: int, last: int) -> tuple:
    """
    Run the main game loop.

    Parameters
    ----------
    limit : int
        Maximum number of attempts allowed
    count : int
        Current attempt counter
    first : int
        Lower bound of number range
    last : int
        Upper bound of number range

    Returns
    -------
    tuple
        (final_count, success_flag)
        final_count : int
            Total number of attempts used
        success_flag : bool
            True if player won, False if exceeded limit
    """
    while True:
        computer: int = computer_number(first, last)
        player: int = player_guess(first, last)

        while (player != computer):
            if count == limit:
                return count, False
            if player > computer:
                print(f'{player} is too high guess again')
                player: int = player_guess(first, last)
            else:
                print(f'{player} is too low guess again')
                player: int = player_guess(first, last)
            count += 1

        if player == computer:
            print(f'your guess of {player} is right')

        ans: str = input('Would you play again (y/n): ').lower().strip()
        if ans == 'n':
            return count, True




if __name__ == '__main__':
    limit: int = 20
    count: int = 1
    name: str = input(f'Enter your name: ').strip().capitalize()
    count = main(limit, count, first=1, last=100)
    if not count[1]:
        print(f'You have exceeded your limit of {count[0]} tries')
    else:
        print('Thanks for playing\n')
    csv_write(name, count[0])
    ranking = score_ranking()
    if isinstance(ranking[0], list):
        names_str = ', '.join(ranking[0])
        print(f'Leader Board\nTop Scorers: {names_str}, Score: {ranking[1]}')




