import math


def rectangle_area(length, width):
    return length * width


def triangle_area(base, height):
    return 0.5 * base * height


def circle_area(radius):
    return math.pi * radius ** 2


choice = input("Choose figure: rectangle, triangle or circle: ")

if choice == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print(rectangle_area(length, width))

elif choice == "triangle":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print(triangle_area(base, height))

elif choice == "circle":
    radius = float(input("Enter radius: "))
    print(circle_area(radius))