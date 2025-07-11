class Text(str):  # So it inherits fro m string class
    def duplicate(self):  # so this is an additional functionality to str
        return self + self


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


text = Text('Python')
print(text.lower())
print(text.duplicate())
