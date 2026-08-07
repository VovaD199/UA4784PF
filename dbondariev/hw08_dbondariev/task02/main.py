from areas import rectangle_area, triangle_area, circle_area


figure = input("Choose figure: rectangle, triangle, or circle: ").lower()

match figure:
    case "rectangle":
        a = float(input("Enter rectangle side a: "))
        b = float(input("Enter rectangle side b: "))

        result = rectangle_area(a, b)
        print("Rectangle area:", result)

    case "triangle":
        a = float(input("Enter triangle base a: "))
        h = float(input("Enter triangle height h: "))

        result = triangle_area(a, h)
        print("Triangle area:", result)

    case "circle":
        r = float(input("Enter circle radius r: "))

        result = circle_area(r)
        print("Circle area:", result)

    case _:
        print("Unknown figure")