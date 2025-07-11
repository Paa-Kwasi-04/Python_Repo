from sys import getsizeof
# So unlike list that are stored  in memory it produces a
# generator object that is iterable and produces
# a new values in each iteration
# and efficient when you want to conserve memory
values = (x * 2 for x in range(1000))

# print(values) # so cant print it out unless through looping

for x in values:
    print(x)

# size of generators
