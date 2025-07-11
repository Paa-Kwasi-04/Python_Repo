class Instructor:
    # class object variable
    Cash = 0

    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.Follower = 0
        self.follower_name = []

    def display(self, subject: str):
        print(f'Hi I am {self.name}\nI teach {subject.capitalize()}')

    def update_follower(self, follower: str):
        self.Follower += 1
        self.follower_name.append(follower)


inst_1 = Instructor('kwasi', 'Tse addo')
inst_1.display('python')
for i in range(5):
    inst_1.update_follower(input('Enter follower name: '))
print(inst_1.Follower)
print(inst_1.follower_name)
