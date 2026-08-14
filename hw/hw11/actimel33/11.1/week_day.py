"""
Program that analyzes the entered number and, depending on the number,
gives the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.).
Take into account cases of entering numbers from 8 and more, as well as cases of entering
non-numerical data.
"""

import calendar


class InvalidDayNumberError(Exception):
    """Exception raised when the entered number is outside the 1 to 7 range."""

    def __init__(self, message="Number must be between 1 and 7."):
        super().__init__(message)


def process_weekday(day_number):
    """
    Processes the week day and returns its name.
    Generates an exception if the day_number is an impropriate.
    """
    if 1 <= day_number <= 7:
        return calendar.day_name[day_number - 1]
    else:
        raise InvalidDayNumberError(
            "Invalid day number. Please enter a number between 1 and 7."
        )


def main():
    """
    Master code that prompts the number and handles exceptions.
    """
    try:
        user_input = input("Please enter a weekday number (1-7): ")
        day_number = int(user_input)

        result = process_weekday(day_number)

        print(f"The day of the week is {result}.")

    except ValueError as e:
        print(f"Invalid input!!! Please enter numerical data only. Error: {e}")
    except InvalidDayNumberError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
