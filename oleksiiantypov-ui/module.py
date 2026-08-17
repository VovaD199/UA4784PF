from math import pow, pi

def area_triangle(b, h):
    print(f"Area of triangle = {h * b *0.5}")

def area_circle(r):
    print(f"Area of circle = {pi * pow(r, 2)}")

def area_restangle(a, b):
    print(f"Area of rectangle = {a * b}")

def func_choise():
    choise = int(input("Print 1 if you need calculete the area of rectangle \n" \
      "Print 2 if you need calculete the area of triangle \n" \
      "Print 3 if you need calculete the area of circle \n" ))
    return(choise)