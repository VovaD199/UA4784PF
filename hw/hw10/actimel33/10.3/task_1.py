class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print(f"This is a polygon with {self.sides} sides")


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(4)
        self.length = length
        self.width = width

    def area(self):                  # "square" = area of the rectangle
        return self.length * self.width



rect = Rectangle(5, 10)
print("Task 1 - Rectangle area:", rect.area())
rect.display_info()
