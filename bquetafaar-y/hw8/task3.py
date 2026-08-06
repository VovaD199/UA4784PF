import main 

request = input("Which figure area you want to calculate? Rectangle, triangle or circle? ")

if request.lower() == "rectangle":
    print("Enter the a and b values:")
    a = int(input())
    b = int(input())
    print(main.rectangle(a, b))
elif request.lower() == "triangle":
    print("Enter the a and h values:")
    a = int(input())
    h = int(input())
    print(main.triangle(a, h))
elif request.lower() == "circle":
    print("Enter the r value:")
    r = int(input())
    print(main.circle(r))
else:
    print("Unknown figure")