'''Task1. Write a function that returns the largest number of two numbers
 (use DocStrings documentation strings in the function).'''
def largest_number(a,b):
    '''Return the largest number between two numbers.'''
    return a if a > b else b
print(largest_number(30,20))