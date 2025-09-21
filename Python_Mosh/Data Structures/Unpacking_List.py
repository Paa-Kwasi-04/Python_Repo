# numbers = [1, 2, 3]

# instead of
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

# you can unpack lists and even
# tuples and dictionaries by
# first, second, third = numbers  # but should be the same number as the length


# but if you want just like the first two items you can unpack them and pack the rest by
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# first, second, *other = numbers  # same as in xargs in functions

# print(first)
# print(other)


#   if you want the first and last item instead
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first, *other, last = numbers

print(first, last)
print(other)
