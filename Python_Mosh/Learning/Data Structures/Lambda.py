# Used as arguments passed to another function
# lambda parameters: return value/Expression

# sorting complex objects
items = [
    ('product1', 10),
    ('product2', 9),
    ('product3', 12)
]


# makes you easily define a function used once as an argument
items.sort(key=lambda item: item[1])
print(items)
