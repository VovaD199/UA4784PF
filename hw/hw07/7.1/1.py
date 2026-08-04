def largest_of_two(num1:float,num2:float) -> float:
    """Function that returns the largest of two numbers.

    Arguments: 
        num1 (float): first number.
        num2 (float): second number.
        
    Returns:
        max(num1,num2) (float)
    """
    return num1 if num1>num2 else num2

print(largest_of_two.__doc__)