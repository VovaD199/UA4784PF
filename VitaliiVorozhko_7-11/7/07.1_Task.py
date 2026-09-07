#Task 1
def max_number(a, b):
    """Return the largest of two numbers."""
    if a > b:
        return a
    else:
        return b



#Task 2
import math

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def area_circle(radius):
    return math.pi * radius ** 2

choice = input("Choose a shape: rectangle, triangle or circle: ")

if choice == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print(area_rectangle(length, width))

elif choice == "triangle":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print(area_triangle(base, height))

elif choice == "circle":
    radius = float(input("Enter radius: "))
    print(area_circle(radius))



#Task 3
def count_characters(text):
    char_count = {}

    for char in text:
        char_count[char] = char_count.get(char, 0) + 1

    return char_count