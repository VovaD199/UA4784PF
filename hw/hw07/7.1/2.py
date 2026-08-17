from math import pi,sqrt
def calculate_area(choice:str)->float|None:
    if choice == 'r':
        a = float(input('Enter first side of the rectangle: '))
        b = float(input('Enter second side of the rectangle: '))
        return calculate_rectangle_area(a,b)
    if choice == 't':
        a = float(input('Enter first side of the triangle: '))
        b = float(input('Enter second side of the triangle: '))
        c = float(input('Enter second side of the triangle: '))
        if not check_triangle(a,b,c):
            print("WRONG TRIANGLE!!!")
            return None
        return calculate_triangle_area(a,b,c)
    if choice == 'c':
        r = float(input('Enter radius of the circle: '))
        return calculate_cirle_area(r)
    return None               

def check_triangle(a:float,b:float,c:float)->bool:
    return a<b+c and b<a+c and c<a+b
def calculate_triangle_area(a:float, b:float,c:float)->float:
    half_per = (a+b+c)/2
    return sqrt(half_per*(half_per-a)*(half_per-b)*(half_per-c))

def calculate_rectangle_area(a:float,b:float)->float:
    return a*b

def calculate_cirle_area(r:float)->float:
    return pi*r**2

choice = input("Bonjour! Please, select the object you want calculate the area for:\n" \
               "\t'r' -- rectrangle\n" \
               "\t't' -- triangle\n" \
               "\t'c' -- circle\n")
result = calculate_area(choice)
if result != None:
    print(f'The area of the picked object is {result:.2f}!!!')
else:
    print('Try better)')