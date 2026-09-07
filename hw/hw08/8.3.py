import area_calculator as ac

def calculate_area(choice:str)->float|None:
    if choice == 'r':
        a = float(input('Enter first side of the rectangle: '))
        b = float(input('Enter second side of the rectangle: '))

        #len may be 0 (the area of such object will not be very informative though), but not negative
        if a*b<0:
            return None
        #neither of the parameters are negative:
        return ac.rectangle_area(a,b)
    if choice == 't':
        a = float(input('Enter the length of one side of the triangle: '))
                                   #might be my rough translation
        h = float(input('Enter the height of the triangle'))
        if a*h<0:
            return None
        return ac.triangle_area(a,h)
    if choice == 'c':
        r = float(input('Enter radius of the circle: '))
        if r<0:
            return None
        return ac.circle_area(r)
    return None   


if __name__ == "__main__":
    choice = input("Bonjour! Please, select the object you want calculate the area for:\n" \
                "\t'r' -- rectrangle\n" \
                "\t't' -- triangle\n" \
                "\t'c' -- circle\n")
    result = calculate_area(choice)
    if result != None:
        print(f'The area of the picked object is {result:.2f}!!!')
    else:
        print('Try better)')