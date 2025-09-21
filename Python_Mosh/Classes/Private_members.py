
class TagCloud:

    def __init__(self):
        self.__tags = {}  # the __prefix makes this attribute private and inaccessible by users

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
# this method gives you a list of the attributes in the class and you can still access private attributes with that
print(cloud.__dict__)

cloud.add('python')
cloud.add('python')
cloud.add('python')
print(cloud['python'])
print(len(cloud))

cloud['python'] = 10
print(cloud['python'])
