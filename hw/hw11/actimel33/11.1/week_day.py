"""
Program that analyzes the entered number and, depending on the number,
gives the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.).
Take into account cases of entering numbers from 8 and more, as well as cases of entering
non-numerical data.
"""

import calendar


class InvalidDayNumberError(Exception):
    """Raised when the day number is outside the range 1-7."""


def process_weekday(day_number: int) -> str:
    """Return the name of the weekday by its number."""
    if not 1 <= day_number <= 7:
        raise InvalidDayNumberError("Day number must be between 1 and 7.")

    return calendar.day_name[day_number - 1]


def main():
    """Get the day number from the user and handle exceptions."""
    try:
        day_number = int(input("Please enter a weekday number (1-7): "))
        print(f"The day of the week is {process_weekday(day_number)}.")

    except ValueError:
        print("Invalid input. Please enter a number.")

    except InvalidDayNumberError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()