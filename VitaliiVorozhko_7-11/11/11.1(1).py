class NegativeAgeError(Exception):
    pass


def check_age(age):
    if age < 0:
        raise NegativeAgeError("Age cannot be negative")

    if age % 2 == 0:
        print(f"Age {age} is even")
    else:
        print(f"Age {age} is odd")


def main():
    try:
        age = int(input("Enter your age: "))
        check_age(age)

    except NegativeAgeError as error:
        print(f"Error: {error}")

    except ValueError:
        print("Error: you must enter a number")


if __name__ == "__main__":
    main()