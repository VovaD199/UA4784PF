import math
from typing import Literal

def get_largest(number1, number2):
    """
    Args:
        number1: number
        number2: number
    Returns:
        number1 if it is greater then number2 or wise verse
    """
   
    if number1 > number2:
        return number1

    return number2

area_functions_map = {
    'rectangle': lambda a, b: a * b,
     'triangle': lambda a, b, c: (
        lambda p: math.sqrt(p * (p - a) * (p - b) * (p - c))
    )((a + b + c) / 2),
    'circle': lambda r: math.pi * r ** 2
} 

def calc_area(figure: Literal['rectangle', 'triangle', 'circle'], *args: float):
     """
    Args:
        figure: 'rectangle' or 'triangle' or 'circle'
        args: number
    Returns:
        calculated area
    """

    func = area_functions_map.get(figure)

    if func is None:
        return 'Not acceptable!'

    try:
        return func(*args)
    except Exception:
        return 'Not acceptable!'


def char_count_in(text):
     """
    Args:
        text: string
    Returns:
        dictionary

    Function count times each char in text
    """
    result = {}
    for char in text:
        counter = text.count(char)
        result[char] = counter
    
    return result