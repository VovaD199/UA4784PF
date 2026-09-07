import area_calculator

def main():
    print("Оберіть фігуру для обчислення площі:")
    print("1 — Прямокутник")
    print("2 — Трикутник")
    print("3 — Коло")
    
    choice = input("Введіть номер фігури (1, 2 або 3): ").strip()

    if choice == "1":
        a = float(input("Введіть сторону a: "))
        b = float(input("Введіть сторону b: "))
        print(f"Площа прямокутника: {area_calculator.rectangle_area(a, b)}")
    elif choice == "2":
        a = float(input("Введіть основу a: "))
        h = float(input("Введіть висоту h: "))
        print(f"Площа трикутника: {area_calculator.triangle_area(a, h)}")
    elif choice == "3":
        r = float(input("Введіть радіус r: "))
        print(f"Площа кола: {area_calculator.circle_area(r)}")
    else:
        print("Некоректний вибір.")

if __name__ == "__main__":
    main()