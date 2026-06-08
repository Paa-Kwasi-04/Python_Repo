# these are like data structures  in python eg list
# where you can define your own data structure and its methods

class TagCloud:

    def __init__(self):
        # making our custom container of dictionary type but given it additional functionality
        self.tags = {}  # so we defined the attribute without asking the user

    def add(self, tag):  # this method requires an input tag
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    # defines how to get an element from the container instance
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    # defines how to set new values for instances
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    # defines how to get length of instances of your class
    def __len__(self):  # doesn't require any info from the user
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()

cloud.add('python')
cloud.add('python')
cloud.add('python')
print(cloud['python'])
print(len(cloud))

cloud['python'] = 10
print(cloud.tags)
