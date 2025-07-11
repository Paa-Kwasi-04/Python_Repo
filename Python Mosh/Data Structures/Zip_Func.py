# zip(*iterables) - -> A zip object yielding tuples until an input is exhausted.
# list(zip('abcdefg', range(3), range(4)))[('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]

# The zip object yields n-length tuples, where n is the number of iterables passed as positional arguments to zip(). The i-th element in every tuple comes from the i-th iterable argument to zip(). This continues until the shortest argument is exhausted. Full name: builtins.zip


list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip(list1, list2)))

# OR
print(list(zip("abc", list1, list2)))  # since it takes any iterable
