'''Task2. Write a program that calculates the area of a rectangle, triangle and circle
(write three functions to calculate the area. And call them in the main program depending
on the user's choice).'''
choice = input("Choose rectangle, triangle or circle: ")
def rectangle_area(a, b):
    return a * b
def triangle_area(a, b):
    return a * b/2
def circle_area(radius):
    return 3.14 * radius**2
if choice == "rectangle":
    a=float(input("Enter length of rectangle: "))
    b=float(input("Enter height of rectangle: "))
    print("Area of rectangle: ", rectangle_area(a, b))
elif choice == "triangle":
    a=float(input('enter the 1st leg of triangle: '))
    b=float(input('enter the 2nd leg of triangle: '))
    print("Area of triangle: ", triangle_area(a, b))
elif choice == "circle":
    radius=float(input('enter the radius of circle: '))
    print("Area of circle: ", circle_area(radius))
else:
    print("Invalid choice")