"""
    Task2. Write a program that calculates the area of a rectangle, triangle and circle (write three functions to calculate the area. And call them in the main program depending on the user's choice).
"""

import math

def ask_for_number(message):
    """Prompt the user for input until a valid number is entered."""

    while True:
        str_input = input(message)

        try:
            return int(str_input)
        except ValueError:
            pass

        try:
            return float(str_input)
        except ValueError:
            pass

        print(f"{str_input} is not a valid number. Try again")


def calculate_rectangle_area(a, b):
    """Calculate the area of a rectangle."""

    return a * b


def calculate_triangle_area(b, h):
    """Calculate the area of a triangle."""

    return b * h / 2


def calculate_circle_area(r):
    """Calculate the area of a circle."""

    return math.pi * r ** 2


def handle_user_prompt():
    """
    Ask the user which shape they want to calculate the area of, 
    gather the required dimensions, and print the resulting area.

    Supported shapes: rectangle, triangle, circle.
    Entering "exit" ends the program.
    """

    shape = input("Enter a shape to calculate its area (rectangle, triangle or circle) or exit to finish: ")
    area = None

    if shape == "rectangle":
       a, b = ask_for_number("Please input a: "), ask_for_number("Please input b: ")
       area = calculate_rectangle_area(a, b)

    elif shape == "triangle":
        b, h = ask_for_number("Please input b: "), ask_for_number("Please input h: ")
        area = calculate_triangle_area(b, h)

    elif shape == "circle":
        r = ask_for_number("Please input r: ")
        area = calculate_circle_area(r)

    elif shape == "exit":
        exit()

    else:
        print(f"{shape} is not supported shape. Please try again: ")

    if area is not None:
        print(f"Area of {shape} is {area}") 

while True:
    handle_user_prompt()