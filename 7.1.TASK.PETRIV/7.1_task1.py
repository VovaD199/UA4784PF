num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def largest_number_of_two_numbers(num1, num2):
    """Calculate the largest of two numbers."""
    if num1 > num2:
        return num1
    return num2

print(largest_number_of_two_numbers(num1, num2))
