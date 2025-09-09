from random import randint


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
    guess: int = int(input(f'Enter a number btn ({first},{last}):'))
    return guess


def main():
    """
    Run the number guessing game.

    The player is prompted to guess a randomly generated number within a user-defined range.
    The game continues until the player guesses correctly and chooses to stop.

    Returns
    -------
    None
    """
    first: int = int(input('Enter starting number: '))
    last: int = int(input('Enter ending number: '))
    while True:
        computer: int = computer_number(first, last)
        player: int = player_guess(first, last)

        while player != computer:
            if player > computer:
                print(f'{player} is too high guess again')
                player: int = player_guess(first, last)
            else:
                print(f'{player} is too low guess again')
                player: int = player_guess(first, last)

        if player == computer:
            print(f'your guess of {player} is right')
        ans: str = input('Would you play again (y/n): ').lower().strip()
        if ans == 'n':
            break


if '__name__' == '__main__':
    main()
    print('Thanks for playing')
