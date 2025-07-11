import string
from random import choices, choice, shuffle


def generate_password(length, Uppercase_letters, numbers, special_characters):

    # Initialize an empty string for the password
    password = ""
    if Uppercase_letters == 'y':
        password += choice(string.ascii_uppercase)
    if numbers == 'y':
        password += choice(string.digits)
    if special_characters == 'y':
        password += choice(string.punctuation)

    len_pass = len(password)

    # Fill the rest of the password with random characters
    # from the allowed character set

    # Initialize the character set with lowercase letters
    # and add other characters based on user input
    pass_initial = [x for x in string.ascii_lowercase]
    if Uppercase_letters == 'y':
        pass_initial += choices(string.ascii_uppercase)

    if numbers == 'y':
        pass_initial += choices(string.digits)

    if special_characters == 'y':
        pass_initial += choices(string.punctuation)

    pass_list = choices(pass_initial, k=(length - len_pass))
    shuffle(pass_list)

    return ''.join(pass_list) + password


def get_password_length():
    while True:
        try:
            length = int(input("Enter password length: "))
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            return length
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    length = get_password_length()
    Uppercase_letters = input("Include uppercase letters? (y/n): ").lower()
    numbers = input("Include numbers? (y/n): ").lower()
    special_characters = input("Include special characters? (y/n): ").lower()

    password = generate_password(
        length, Uppercase_letters, numbers, special_characters)
    print(f"Generated password: {password}")


if __name__ == "__main__":
    main()
# This code generates a password based on user input for length and character types.
