import math

def rectangle(x,y):
    '''Calculates the rectangles area'''
    result = x*y
    return result

def triangle(a, h):
    '''Calculates the triangles area'''
    result = a*h/2
    return result

def circle(r):
    '''Calculates the circles area'''
    result = r**2*math.pi
    return result

request = input("What kind of figure area you want to calculate? Rectangle, triangle or circle?")

if request.lower() == "rectangle":
    print("Enter the x and y values:")
    x = int(input())
    y = int(input())
    print(rectangle(x, y))

elif request.lower() == "triangle":
    print("Enter the a and h values:")
    a = int(input())
    h = int(input())
    print(triangle(a, h))

elif request.lower() == "circle":
    print("Enter the r value:")
    r = int(input())
    print(circle(r))

else:
    print("Unknown figure")

          