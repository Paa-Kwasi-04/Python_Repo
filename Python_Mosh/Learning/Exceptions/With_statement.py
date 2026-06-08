# The with statement in Python simplifies resource management
#  and exception handling by ensuring proper acquisition and
#  release of resources like files, network connections, and
#  database connections. It replaces try-except-finally blocks
# and enhances readability by reducing boilerplate code. The with
# statement is commonly used for file handling, as it ensures automatic
# file closure after operations are completed. Context managers manage
#  resource allocation and deallocation using
#  two special methods: __enter__() and __exit__().
#  Multiple contexts can be used in a single with statement by separating
# them with commas. Context managers define the runtime context to be established
#  when executing a with statement, implementing two methods: __enter__() and __exit__().

try:
    with open('app.py') as file, open('new.py') as target:  # we are focusing on with
        print('File opened')

    age = int(input('Age: '))
    xfactor = 10/age

except (ValueError, ZeroDivisionError) as ex:

    print('You didn\'t enter a valid age')
    print(f'Error: {ex}')

else:
    print('No exceptions were thrown')
