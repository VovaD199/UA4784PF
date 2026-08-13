'''task 1'''
def largest_number(a,b):
    if a > b:
        return a
    else:
        return b
print(largest_number(30, 100))


'''task2'''

import maths

def area_rectangle(a, b):
    return a * b

def area_(c, h):
    return (c * h) / 2

def area_circle(radius):
    return math.pi * radius ** 2

choice = input(" Виберіть фігуру (rectangle, triangle, circle): ")

if choice == "rectangle":
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    print(area_rectangle(a, b))

elif choice == "triangle":
    c = float(input("Enter c: "))
    h = float(input("Enter h: "))
    print(area_triangle(c, h))

elif choice == "circle":
    radius = float(input("Enter radius: "))
    print(area_circle(radius))

else:
    print("Unknown shape")


'''task3'''
def count_characters(text):
    result = {}

    for char in text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result


print(count_characters("hello"))
