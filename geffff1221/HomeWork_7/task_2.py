figure = int(input("Choose the number that corresponds to the shape:\n"
                   "1. Rectangle\n"
                   "2. Triangle (base and height)\n"
                   "3. Triangle (three sides) Note: any two sides must sum to more than the third\n"
                   "4. Circle.\n"
                   "Enter your choice: "))


if figure == 1:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

elif figure == 2:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))

elif figure == 3:
    side_a = float(input("Enter the length of side a: "))
    side_b = float(input("Enter the length of side b: "))
    side_c = float(input("Enter the length of side c: "))
elif figure == 4:
    radius = float(input("Enter the radius of the circle: "))
else:
    print("Invalid choice. Please select a valid option.")
    
def calculate_area_rectangle(length, width):
    return length * width

def calculate_area_triangle_base_height(base, height):
    return 0.5 * base * height

def calculate_area_triangle_sides(side_a, side_b, side_c):
    # Проверка неравенства треугольника
    if (side_a + side_b <= side_c or 
        side_a + side_c <= side_b or 
        side_b + side_c <= side_a):
        print("Error: A triangle with these sides does not exist")
        return None
    
    s = (side_a + side_b + side_c) / 2
    return (s * (s - side_a) * (s - side_b) * (s - side_c)) ** 0.5

def calculate_area_circle(radius):
    
    return 3.14159265359 * radius ** 2

if figure == 1:
    print("The area of the rectangle is:", calculate_area_rectangle(length, width))
elif figure == 2:
    print("The area of the triangle is:", calculate_area_triangle_base_height(base, height))
elif figure == 3:
    print("The area of the triangle is:", calculate_area_triangle_sides(side_a, side_b, side_c))
elif figure == 4:
    print("The area of the circle is:", calculate_area_circle(radius))