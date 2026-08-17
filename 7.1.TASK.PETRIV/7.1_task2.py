import math

def area_rectangle():
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Rectangle area:", l * w)

def area_triangle():
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print("Triangle area:", 0.5 * b * h)

def area_circle():
    r = float(input("Enter radius: "))
    print("Circle area:", math.pi * r ** 2)

# Main program
choice = input("Choose shape (1 - Rectangle, 2 - Triangle, 3 - Circle): ")

if choice == "1":
    area_rectangle()
elif choice == "2":
    area_triangle()
elif choice == "3":
    area_circle()
else:
    print("Invalid choice!")
