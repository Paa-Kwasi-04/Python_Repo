word = input('Enter any word> ').strip().lower()

empty_str = ''

for x in word:
    empty_str = x + empty_str

empty_str = empty_str.strip()
# print(empty_str)

if word == empty_str:
    print('It\'s a Palindrome')

else:
    print('It\'s not a Palindrome')


print(empty_str)
