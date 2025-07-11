import random
import string

print(random.random())  # generates random values from 0 to 1
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4]))
print(random.choices([1, 2, 3, 4], k=2))
print(random.choices('abcdefghi', k=4))

# join method
print(''.join(random.choices('abcdefghi', k=4)))
print(','.join(random.choices('abcdefghi', k=4)))


# string module

# print((string.ascii_letters), (string.digits))

# generates a random password
print(''.join(random.choices(string.ascii_letters+string.digits, k=4)))

numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)
