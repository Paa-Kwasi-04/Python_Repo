numbers_string = input('Enter string of numbers to be added> ')
sum = 0

for x in numbers_string:
    if x not in [',', ' ']:
        sum += int(x)

print(sum)
