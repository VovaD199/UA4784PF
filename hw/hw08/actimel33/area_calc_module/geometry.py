from math import pi, pow

def rectangle_area(a: float, b: float) -> float:
    """Calculates the area of the rectangle S = a * b"""
    return a * b

def triangle_area(h: float, a: float) -> float:
    """Calculates the area of the triangle S = 0.5 * h * a"""
    return 0.5 * h * a

def circle_area(r: float) -> float:
    """Calculates the area of the square S = pi * r^2 with the help pow()"""
    return pi * pow(r, 2)