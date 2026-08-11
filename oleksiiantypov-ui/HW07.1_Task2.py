
import math
import os

os.system("cls")

def area_restangle(a, b):
    print(f"Area of rectangle = {a * b}")

def area_triangle(b, h):
    print(f"Area of triangle = {h * b / 2}")

def area_circle(r):
    print(f"Area of circle = {math.pi * r**2}")

def func_choise():
    choise = int(input("Print 1 if you need calculete the area of rectangle \n" \
      "Print 2 if you need calculete the area of triangle \n" \
      "Print 3 if you need calculete the area of circle \n" ))
    return(choise)

choise = func_choise()

while choise not in [1, 2, 3]:
    print("Wrong number. Choose again")
    choise = func_choise()

if choise == 1:
    length = int(input("Enter length = "))
    width = int(input("Enter width = "))
    area_restangle(length, width)

elif choise == 2:
    height = int(input("Enter height = "))
    base = int(input("Enter base = "))
    area_triangle(height, base)
    
else:
    radius = int(input("Enter radius = "))
    area_circle(radius)

