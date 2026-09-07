import module


figure = input("Which figure do you want to calculate? ")

if figure == "rectangle":
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    print("Area:", module.rectangle_area(a, b))

elif figure == "triangle":
    h = float(input("Enter height: "))
    a = float(input("Enter base: "))
    print("Area:", module.triangle_area(h, a))

elif figure == "circle":
    r = float(input("Enter radius: "))
    print("Area:", module.circle_area(r))

else:
    print("Unknown figure")