
# try except block works like the for else block
try:
    file = open('app.py')
    age = int(input('Age: '))
    xfactor = 10/age
# Takes your thrown exception error message and stores it in the variable ex
except (ValueError, ZeroDivisionError) as ex:

    print('You didn\'t enter a valid age')
    print(f'Error: {ex}')

else:  # executed when no exceptions are thrown
    print('No exceptions were thrown')
finally:
    file.close()  # Code that always executes, regardless of whether an exception occurred or not
