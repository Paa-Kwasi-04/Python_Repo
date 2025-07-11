# types of functions
# All functions return none unless you decide to return something
# 1. Perform a task: gets prints to terminal
def greet(first_name, last_name):
    print(f'Hi {first_name} {last_name}')
    print('Welcome aboard')


greet('Paa', 'Kwasi')


# 2. Return a value: and do whatever we want with it
def get_greeting(name):
    return f'Hi {name}'


message = get_greeting('Paa Kwasi')
