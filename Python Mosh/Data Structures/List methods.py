letters = ['a', 'b', 'c']

# Add
letters.append('d')  # adds an item at the end of the list
letters.insert(0, '_')  # adds an item at a given index
print(letters)

# Remove
letters.pop()  # removes items at the end of the list or a specified index
letters.remove('b')  # removes the first instance of the item in the list
letters.clear()  # deletes the list
# del letters[0:3] # removes a range of items in a list


# finding items
letters.index('a')  # returns the index of the item given
print(letters.count('d'))  # returns the numbers of instances for the item
