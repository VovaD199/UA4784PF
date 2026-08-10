import areas

figure = input("Choose figure: ").lower()
result = None

if figure == "rectangle":
    a = float(input("Введіть сторону a: "))
    b = float(input("Введіть сторону b: "))
    result = areas.area_of_rectangle(a, b)
elif figure == "triangle":
    a = float(input("Введіть сторону a: "))
    h = float(input("Введіть висоту h: "))
    result = areas.area_of_triangle(a, h)
elif figure == "circle":
    r = float(input("Введіть радіус r: "))
    result = areas.area_of_circle(r)
else:
    print("Invalid figure")

if result is not None:
    print(f"Площа фігури = {result}")