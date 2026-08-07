from formulas import *


def main():
    print("Which figure's area do you want to calculate?")
    print("1 - Rectangle")
    print("2 - Triangle")
    print("3 - Circle")

    choice = input("Enter the figure number: ")

    if choice == "1":
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        print(f"Rectangle area: {rectangle_area(a, b)}")

    elif choice == "2":
        a = float(input("Enter base a: "))
        h = float(input("Enter height h: "))
        print(f"Triangle area: {triangle_area(a, h)}")

    elif choice == "3":
        r = float(input("Enter radius r: "))
        print(f"Circle area: {circle_area(r)}")

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()