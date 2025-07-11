# Default Optional parameter run if no value is not passed to them
# But must be after all required parameters for the function
def increment(number, by=1):
    return number + by


print(increment(2))
