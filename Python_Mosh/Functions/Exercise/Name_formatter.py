name = input('Enter Full name> ').title().replace(' ', '')
print(name, ':', len(name))

empty_str = ''

for x in name:
    empty_str = x + empty_str

print(empty_str)
