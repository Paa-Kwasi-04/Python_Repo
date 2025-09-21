# is a collection of key value pairs

# point = {}  # empty dictionary
point = {'x': 1, 'y': 2}
# point = dic(x=1, y=2)


# Accessing values in a dictionary
print(point['x'])

# changing values of keys
point['x'] = 10

# adding new keys
point['z'] = 20

# deleting keys
# del point['x']

# to get values of keys and returns a 0 if not in dictionary
print(point.get("a", 0))

# looping over dictionary
for key, value in point.items:
    print(key, value)
