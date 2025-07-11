# def filter(function: None, iterable: Iterable[Optional[_T]], /) -> Iterator[_T]
# def filter(function: Callable[[_T], Any], iterable: Iterable[_T], /) -> Iterator[_T]


# filter(function or None, iterable) - -> filter object

# Return an iterator yielding those items of iterable for which function(item)
# is true. If function is None, return the items that are true.

items = [
    ('product1', 10),
    ('product2', 9),
    ('product3', 12)
]


# so filters the items list for those whose price is 10 and above
filtered_list = list(filter(lambda item: item[1] >= 10, items))
print(filtered_list)


# Eg 2
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]


def is_A_student(score):
    return score > 75


over_75 = list(filter(is_A_student, scores))

print(over_75)
