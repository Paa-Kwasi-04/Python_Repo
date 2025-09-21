# def map(func: Callable[[_T1], _S], iter1: Iterable[_T1], /) -> Iterator[_S]
# map(func, *iterables) - -> map object which is also an iterable
# Make an iterator that computes the function using
# arguments from each of the iterables.
# Stops when the shortest iterable is exhausted.

items = [
    ('product1', 10),
    ('product2', 9),
    ('product3', 12)
]


prices = list(map(lambda item: item[1], items))
print(prices)

# Eg2

my_pets = ['alfred', 'tabitha', 'william', 'arla']

uppered_pets = list(map(str.upper, my_pets))

print(uppered_pets)
