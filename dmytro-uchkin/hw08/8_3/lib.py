from math import pi, pow


def calculate_rectangle_area(a, b):
    """Calculate the area of a rectangle."""

    return a * b


def calculate_triangle_area(b, h):
    """Calculate the area of a triangle."""

    return b * h / 2


def calculate_circle_area(r):
    """Calculate the area of a circle."""

    return pi * pow(r, 2)
