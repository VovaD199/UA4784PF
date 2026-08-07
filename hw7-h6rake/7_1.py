import math
import os

#Task1
a=10
b=100
def large_num_short(a,b):
    """Returns the largest number."""  # <-- ДобавилиDocString по условию задачи
    return max(a,b)
print(large_num_short(a,b))
input("Press Enter to go to the task 2")
os.system('cls')

#Task2
def area_rectangle(width,height):
    return width*height
def area_triangle(base,height):
    return 0.5*base*height
def area_circle(radius):
    return math.pi*(radius**2)
def calcarea():
    print("Choose a shape to calculate its area:")
    print("1.Rectangle")
    print("2.Triangle")
    print("3.Circle")
    choice=input("Enter the number of your choice (1-3): ")
    if choice=='1':
        a=float(input("Enter the width of the rectangle: "))
        b=float(input("Enter the height of the rectangle: "))
        print(f"The area of the rectangle is: {area_rectangle(a, b):.2f}")
    elif choice=='2':
        a=float(input("Enter the base of the triangle: "))
        b=float(input("Enter the height of the triangle: "))
        print(f"The area of the triangle is: {area_triangle(a, b):.2f}")
    elif choice=='3':
        a=float(input("Enter the radius of the circle: "))
        print(f"The area of the circle is: {area_circle(a):.2f}")
    else:
        print("Invalid choice! Please run the program again and select 1, 2, or 3.")
calcarea()
input("Press Enter to go to the task 3")
os.system('cls')

#Task3
def count_characters(text):
    answer={}
    for char in text:
        if char not in answer:
            answer[char]=text.count(char)
    return answer
input_string=input("Enter a string to count the characters: ")
output_dict=count_characters(input_string)

print(f"Input: {input_string}")
print(f"Output: {output_dict}")
input_string=input("Press Enter to close")