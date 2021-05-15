class Rectangle:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        if type(length) and type(width) and type(height) not in [int, float] or length < 0 or width < 0 or height < 0:
            raise ValueError


    # def show(self):
    #     print(f'Hello {self.length} {self.width} {self.height}')
    def volume_calculation(self):
        try:
            return self.length * self.width * self.height
        except ValueError:
            print('loser entered wrong type')

    

c = Rectangle(1, 3, 10)

print(c.volume_calculation())
