class Polygon:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Rectangle(Polygon):
    def area(self):
        return self.width * self.height


rectangle = Rectangle(5, 5)
print(rectangle.area())
