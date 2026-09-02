import areas

if __name__ == '__main__':
    while True:
        choice = int(input("\nChoose a figure:"
                           "\n1. Rectangle"
                           "\n2. Triangle"
                           "\n3. Circle"
                           "\n0. Exit"
                           "\n\n Your choice: "))

        match choice:
            case 1:
                rectangle_length = float(input("\nEnter the length of the rectangle: "))
                rectangle_width = float(input("Enter the width of the rectangle: "))
                # rectangle_length, rectangle_width = map(float, input("Enter the length and width of the rectangle: ").split())
                print(f"Rectangle area: {areas.rectangle_area(rectangle_length, rectangle_width):.2f}"
                      f"\n=================")

            case 2:
                triangle_base = float(input("\nEnter the base of the triangle: "))
                triangle_height = float(input("Enter the height of the triangle: "))
                # triangle_base, triangle_height = map(float, input("Enter the base and height of the triangle: ").split())
                print(f"Triangle area: {areas.triangle_area(triangle_base, triangle_height):.2f}"
                      f"\n=================")

            case 3:
                circle_radius = float(input("\nEnter the radius of the circle: "))
                print(f"Circle area: {areas.circle_area(circle_radius):.2f}"
                      f"\n=================")

            case 0:
                break

            case _:
                print("Invalid choice")