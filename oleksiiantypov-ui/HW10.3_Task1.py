class Polygon:
    pass

class Rectangle(Polygon):
    def __init__(self, x, y):
        if x > 0 and y > 0:
            self.x = x
            self.y = y
        else:
            print(f'Please enter a valid number.')

    def square(self):
        print(f'Square of rectangle = {self.x * self.y}')


rec1 = Rectangle(2, 3)
rec1.square()