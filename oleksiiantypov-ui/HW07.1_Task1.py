def largest_number(a: int, b: int) -> int:
    """
    Function returns largest number
    of two numbers
    """
    return a if a >= b else b

a = input("Enter a = ")
b = input("Enter b = ")
print(largest_number(a, b))
print(largest_number.__doc__)