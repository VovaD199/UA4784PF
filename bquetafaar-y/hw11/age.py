def check_age(age):
    if age % 2 == 0:
        return f"Your age,{age}, is even."
    else:
        return f"Your age,{age}, is odd."
    
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("You entered a negative number")
    check_age(age)
except ValueError as error:
    raise error