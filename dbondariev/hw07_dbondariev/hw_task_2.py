import math


def rectangle_area(width, height):
    """Return the area of a rectangle."""
    return width * height


def triangle_area(base, height):
    """Return the area of a triangle."""
    return base * height / 2


def circle_area(radius):
    """Return the area of a circle."""
    return math.pi * radius ** 2


choice = input("Choose shape: rectangle, triangle, circle: ")

match choice:
    case "rectangle":
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        print(rectangle_area(width, height))

    case "triangle":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        print(triangle_area(base, height))

    case "circle":
        radius = float(input("Enter radius: "))
        print(circle_area(radius))

    case _:
        print("Wrong choice")