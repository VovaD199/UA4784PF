def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return "even" if age % 2 == 0 else "odd"

try:
    age = int(input("Enter age: "))
    print(f"Age is {check_age(age)}")
except ValueError as e:
    print(f"Error: {e}")


