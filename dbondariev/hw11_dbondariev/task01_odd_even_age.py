class NegativeAgeError(Exception):
    pass


def check_age(age):
    if age < 0:
        raise NegativeAgeError("Age cannot be negative")

    if age % 2 == 0:
        return "Age is even"

    return "Age is odd"


try:
    user_age = int(input("Enter your age: "))
    result = check_age(user_age)
    print(result)

except NegativeAgeError as error:
    print(error)

except ValueError:
    print("You entered not a number")