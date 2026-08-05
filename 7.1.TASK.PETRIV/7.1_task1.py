num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def largest_number_of_two_numbers(num1, num2):
    """Calculates the largest 
    number between two numbers"""
    if num1 > num2:
        return num1
    else:
        return num2

print(largest_number_of_two_numbers(num1, num2))