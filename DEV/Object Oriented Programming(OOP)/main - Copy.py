class Instructor:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.followers = 0


inst = Instructor('kwasi', 'tse Addo')
inst_1 = Instructor('Kwaku', 'Osu')
inst_2 = Instructor('kesse', 'Nungua')
print(inst.name)
print(inst.followers)
# task of a constructor is to initialize
# the attributes of the class while creating the objects of the class
