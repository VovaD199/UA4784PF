import math


# Task 1
def max_of_two(first_number, second_number):
    """
    Returns the larger of two numbers.

    Args:
        first_number: The first number to compare.
        second_number: The second number to compare.

    Returns:
        The maximum value between the two input numbers.
    """
    if first_number >= second_number:
        return first_number

    return second_number


# Task 2
def rectangle_area(length, width):
    return length * width


def triangle_area(height, base):
    return (height * base) / 2


def circle_area(radius):
    return math.pi * radius ** 2


def area_calculator():
    print("Welcome to the calculator!")

    while True:
        print(
            "\n======================================"
            "\n1. Calculate the area of a rectangle"
            "\n2. Calculate the area of a triangle"
            "\n3. Calculate the area of a circle"
            "\n0. Exit"
        )

        choice = input("\nYour choice: ")

        match choice:
            case "1":
                length = float(input("Write length of the rectangle: "))
                width = float(input("Write width of the rectangle: "))
                print(
                    f"The area of the rectangle: "
                    f"{rectangle_area(length, width):.2f}"
                )

            case "2":
                height = float(input("Write height of the triangle: "))
                base = float(input("Write base of the triangle: "))
                print(
                    f"The area of the triangle: "
                    f"{triangle_area(height, base):.2f}"
                )

            case "3":
                radius = float(input("Write radius of the circle: "))
                print(
                    f"The area of the circle: "
                    f"{circle_area(radius):.2f}"
                )

            case "0":
                break

            case _:
                print("Please enter one of the following options!")


# Task 3
def count_characters(string):
    characters = {}

    for character in string:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1

    return characters