from calcfunctions import *
selectvar=input("Enter the shape you want to calculate the area for (r-rectangle,t-triangle,c-circle): ")
match selectvar:
    case "r":
        l=float(input("Enter the length of the rectangle: "))
        w=float(input("Enter the width of the rectangle: "))
        print("The area of the rectangle is: ",rectangle(l,w))
    case "t":
        b=float(input("Enter the base of the triangle: "))
        h=float(input("Enter the height of the triangle: "))
        print("The area of the triangle is: ",triangle(b,h))
    case "c":
        r=float(input("Enter the radius of the circle: "))
        print("The area of the circle is: ",circle(r))
    case _:
        print("Invalid input")
