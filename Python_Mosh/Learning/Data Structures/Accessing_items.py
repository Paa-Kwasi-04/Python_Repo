letters = ['a', 'b', 'c', 'd']
print(letters[-1])  # to access items in list
print(letters[0:3])  # slicing like in strings


# Adding steps in slicing
numbers = list(range(21))
print(numbers[::2])
print(numbers[::-2])  # prints the whole list with a step of two in reverse


# modify items
letters[0] = 'A'
print(letters)
