import math

def distance(x1, y1, x2, y2):
    """Return the distance between two points rounded to two decimal places."""
    dx = x2 - x1
    dy = y2 - y1

    result = math.sqrt(dx ** 2 + dy ** 2)

    return round(result, 2)

print(distance(23,52, 92, 22))