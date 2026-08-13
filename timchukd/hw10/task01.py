"""
Task1. Create a polygon class and a rectangle class that inherits from the polygon class and finds
the square of rectangle.
"""

class Polygon:
    pass

class Rectangle(Polygon):
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def square(self):
        return self.lenght * self.width

rectangle = Rectangle(5, 10)

print(f"The square of the rectangle is: {rectangle.square()}")
"""
dtimchuk@dt hw10 % python task01.py
The square of the rectangle is: 50
"""