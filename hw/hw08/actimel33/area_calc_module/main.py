import geometry

def main():
    
    choice = input("Enter the number of the figure (1/2/3): ").strip().lower()
    
    if choice in ['1', 'rectangle']:
        a = float(input("Please enter side a: "))
        b = float(input("Please enter side b: "))
        area = geometry.rectangle_area(a, b)
        print(f"Area is: {area}")
        
    elif choice in ['2', 'triangle']:
        h = float(input("Please enter hight h: "))
        a = float(input("Please enter foundation a: "))
        area = geometry.triangle_area(h, a)
        print(f"Triangle square is: {area}")
        
    elif choice in ['3', 'circle']:
        r = float(input("Please enter radius r: "))
        area = geometry.circle_area(r)
        print(f"Circle area is: {area:.4f}")
        
    else:
        print("Error: Wrong figure number.")

if __name__ == "__main__":
    main()