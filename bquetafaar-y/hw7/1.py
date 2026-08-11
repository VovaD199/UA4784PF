def myFunc(x, y):
    '''The function returns the largest number of two given'''
    result = 0
    if x > y:
        result = x
    else:
        result = y
    return result

print(myFunc(int(input()), int(input())))
print(myFunc.__doc__)