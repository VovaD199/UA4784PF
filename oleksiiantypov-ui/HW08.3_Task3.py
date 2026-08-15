import module

choise = module.func_choise()

while choise not in [1, 2, 3]:
    print("Wrong number. Choose again")
    choise = module.func_choise()

if choise == 1:
    length = int(input("Enter length = "))
    width = int(input("Enter width = "))
    module.area_restangle(length, width)

elif choise == 2:
    height = int(input("Enter height = "))
    base = int(input("Enter base = "))
    module.area_triangle(height, base)
    
else:
    radius = int(input("Enter radius = "))
    module.area_circle(radius)