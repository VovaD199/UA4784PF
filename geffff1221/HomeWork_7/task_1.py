num_1 = input("Enter the first number: ")
num_2 = input("Enter the second number: ")

def max_digit(num_1, num_2):
    if num_1 > num_2:
        return num_1
    elif num_1 == num_2:
        return "Both numbers are equal."
    else:
        return num_2


print("The maximum digit is:", max_digit(num_1, num_2))