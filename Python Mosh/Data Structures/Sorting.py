# sorting list
numbers = [3, 51, 2, 8, 6]
numbers.sort()  # modifies the list
numbers.sort(reverse=True)  # reverses it
# OR
# just returns a new sorted object in this case a list
numbers = sorted(numbers, reverse=True)


# sorting complex objects
items = [
    ('product1', 10),
    ('product2', 9),
    ('product3', 12)
]

# cant sort complex object so therefore
# the key function in Python's sorted() method specifies the criteria for sorting.
# It takes a function that is applied to each element in the iterable,
# and sorting is then performed based on the returned values.


def sort_item(item):  # function that creates the criteria for sorting
    return item[1]


items.sort(key=sort_item)
print(items)
