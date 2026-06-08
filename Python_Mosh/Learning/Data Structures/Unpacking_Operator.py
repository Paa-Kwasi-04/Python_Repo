# unpacks any iterable ie lists, tuples, dictionary,range, strings etc

numbers = [1, 2, 3]
print(*numbers)  # unpacks the list


# another application
values = [*range(5), *"Hello"]
print(values)

# Eg3
first = [1, 2]
second = [3]
combined = [*first, 'a', *second, *'']
print(combined)


# Unpacking Dictionaries
_1dict = dict(x=1)
_2dict = dict(x=1, y=2)
combine = {**_1dict, **_2dict, 'z': 1}
print(combine)
