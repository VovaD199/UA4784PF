from math import pi, pow

#i do not check whether the parameters are valid
def rectangle_area(a:float,b:float):
    return a*b

#my previous implementation of this task used Heron's formula with checking whether
#the triangle with given sides even exists, but in this task the parameters differ
def triangle_area(a:float,h:float):
    return 1/2*a*h

#used pow(), because in the was task explicitly stated to import pow() function from math 
def circle_area(r:float):
    return pi*pow(r,2)