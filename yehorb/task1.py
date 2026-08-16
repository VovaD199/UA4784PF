a = int(input("What's the first number? "))
b = int(input("What's the second number? "))

def largest(a, b):
    """Function to find the largest number"""
    if a > b:
        return a
    else:
        return b

largest(a, b)
print(f"The largest number is {largest(a, b)}")