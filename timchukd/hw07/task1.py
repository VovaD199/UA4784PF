"""
Task1. Write a function that returns the largest number of two numbers
(use DocStrings documentation strings in the function).
"""
def maxNumber(a, b):
    if a > b:
        return a
    else:
        return b


"""
Task2. Write a program that calculates the area of a rectangle, triangle and circle 
(write three functions to calculate the area. 
And call them in the main program depending on the user's choice).
"""
def area_rectangle(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def area_triangle(base, height):
    """Calculate the area of a triangle."""
    return 0.5 * base * height

def area_circle(radius):
    """Calculate the area of a circle."""
    import math
    
    return math.pi * radius ** 2

"""
Task3. Write a function that calculates the number of characters included in
given string
• input: "hello"
• output: f"h":1, "e":1,"":2,"o": 1}
"""
def count_characters(str):
    char_count = {}
    for char in str:
        char_count[char] = char_count.get(char, 0) + 1

    return char_count
