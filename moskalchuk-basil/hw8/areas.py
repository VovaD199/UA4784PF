from math import pi, pow

def area_of_rectangle(a, b):
    """Calculates are of a rectangle"""
    S = a * b
    return S
    

def area_of_triangle(a, h):
    """Calculates are of a triangle"""
    S = a * h / 2
    return S

def area_of_circle(r):
    """Calculates are of a circle"""
    S = pi * pow(r, 2)    
    return S