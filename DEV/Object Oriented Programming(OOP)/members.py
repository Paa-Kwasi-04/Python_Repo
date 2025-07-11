class Box:
    # class variables / members
    box_type = 'packaging carton'
    color = 'brown'

    def __init__(self, side_a: int, side_b: int):
        self.side_a = side_a
        self.side_b = side_b

    def __str__(self):
        return f'side A:{self.side_a}, side B:{self.side_b}'


b1 = Box(3, 4)
print(b1)
print(Box.color)
