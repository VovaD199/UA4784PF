"""
Task 3.

Write a program that calculates the area of a rectangle S = a*b, the area of a triangle S = 0.5*h*a, and the area of a circle S = pi*r**2.

This module must be used in another module in which we ask the user the area of which figure he wants to calculate.

Note:

To perform the task, you need to import the math module, and from it the pow() function and the value of the variable pi, and module,
which contains three functions for finding areas, into the main program.

The basic logic of the program is executed in the main module.
"""

from lib import calculate_rectangle_area, calculate_triangle_area, calculate_circle_area


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