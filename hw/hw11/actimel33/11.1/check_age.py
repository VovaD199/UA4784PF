"""
A program that prompts the user to enter their age, and then displays a message
stating whether the age is even or odd. The program must provide the ability to
enter a negative number, and in this case generate an exception. The master code
should call a function that processes the information entered.
"""


def prompt_age():
    """
    Prompts the user age.
    """
    user_input = input("Enter your age positive or negative")

    return user_input


def process_age(age):
    """
    Processes the age to determine if it is even or odd.
    Generates a ValueError exception if the age is negative.
    """

    if age < 0:
        raise ValueError("Age cannot be negative!")

    if age % 2 == 0:
        return "even"
    else:
        return "odd"


def main():
    """
    Master code that prompts the user and handles exceptions.
    """

    try:
        user_input = prompt_age()
        age = int(user_input)

        result = process_age(age)

        print(f"The age entered is {result}.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
