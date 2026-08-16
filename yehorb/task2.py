import math

def rectangle(a, b):
    return a * b

def triangle(a, h):
    return a * h / 2

def circle(r):
    return math.pi * r ** 2


print("Choose a shape:")
print("1 - Rectangle")
print("2 - Triangle")
print("3 - Circle")

choice = input("Your choice: ")

if choice == "1":
    print("You chose rectangle")
    a = float(input("What's the first side: "))
    b = float(input("What's the second side: "))
    print(f"The area of rectangle is {rectangle(a, b)}")

elif choice == "2":
    print("You chose triangle")
    a = float(input("What's the side: "))
    h = float(input("What's the height: "))
    print(f"The area of triangle is {triangle(a, h)}")

elif choice == "3":
    print("You chose circle")
    r = float(input("What's the radius: "))
    print(f"The area of circle is {circle(r)}")

else:
    print("Invalid choice")