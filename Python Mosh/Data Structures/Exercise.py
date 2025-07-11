# write a program to find the most repeated character in the text
from pprint import pprint
sentence = "This is a common interview question".lower


dic_1 = {}

for x in sentence:
    if x not in dic_1:
        dic_1[x] = 1
    else:
        dic_1[x] += 1


print(max(dic_1, key=lambda k: dic_1[k]))
