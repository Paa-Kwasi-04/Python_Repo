def calculate_xfactor(age):
    if age <= 0:
        raise ValueError('crazy chale')
    return 10/age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)

# Only raise exceptions if you really have to for code performance sake
