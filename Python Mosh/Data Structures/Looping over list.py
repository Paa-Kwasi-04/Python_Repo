letters = ['a', 'b', 'c']


# enumerate returns both the index and its item as a tuple which you can unpack
for index, letter in enumerate(letters):
    print(index, letter)
