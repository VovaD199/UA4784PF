import math

def area_rectangle(w, h):
    return w * h

def area_triangle(b, h):
    return 0.5 * b * h

def area_circle(r):
    return math.pi * r**2

choice = input("1 - Прямокутник, 2 - Трикутник, 3 - Коло: ")

if choice == "1":
    print("Площа:", area_rectangle(float(input("Ширина: ")), float(input("Висота: "))))
   
elif choice == "2":
    print("Площа:",area_triangle(float(input("Основа: ")), float(input("Висота: "))))
    
elif choice == "3":
    print("Площа:", area_circle(float(input("Радіус: "))))
else:
    print("Невідомий вибір")

