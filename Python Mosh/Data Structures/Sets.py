# it is a collection with no duplicates
# they are unordered
numbers = [1, 1, 2, 3, 4]

first = set(numbers)
second = {1, 4}


# methods
second.add(5)
second.remove(5)
print(len(second))  # etc

# this is the beauty
# since you can perform some maths on them
print(first | second)  # gives the union of the two sets
print(first & second)  # gives the intersection
print(first - second)  # gives the diff btn the sets


print(uniques)
print(second)
