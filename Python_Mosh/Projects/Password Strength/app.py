import re

def password_strength(password:str):
    password_strength_dict:dict = {
        0:'Very Weak',
        1:'Very Weak',
        2:'Weak',
        3:'Medium',
        4:'Strong',
        5:'Very Strong',
    }
    strength:int = 0
    length_of_password = len(password)

    
    
    if length_of_password >= 8:
        strength += 1
    if re.search(r'[0-9]',password):
        strength += 1
    if re.search(r'[A-Z]',password):
        strength += 1
    if re.search(r'[a-z]',password):
        strength += 1
    if re.search(r"[@_!#$%^&*()<>?/\|}{~:]",password):
        strength += 1

    return password_strength_dict[strength]



def main():
    password:str = input('Enter a password: ').strip()
    pass_strength = password_strength(password)

    print(f'Your password is {pass_strength}')

if __name__ == '__main__':
    main()
