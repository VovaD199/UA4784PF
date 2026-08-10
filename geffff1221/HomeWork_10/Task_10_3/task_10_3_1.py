class Polygon:
    def __init__(self, sides):
        self.sides = sides  

    def get_perimeter(self):
        return sum(self.sides)


class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__([width, height, width, height])

    def get_area(self):
        return self.sides[0] * self.sides[1]


rect = Rectangle(8, 16)
print("Площадь прямоугольника:", rect.get_area())
print("Периметр прямоугольника:", rect.get_perimeter())