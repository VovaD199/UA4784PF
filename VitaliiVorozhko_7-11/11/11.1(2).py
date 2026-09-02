def get_day(number):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    if number >= 8:
        raise ValueError("Number must be from 1 to 7")

    if number < 1:
        raise ValueError("Number must be from 1 to 7")

    return days[number]


def main():
    try:
        number = int(input("Enter a number from 1 to 7: "))
        print(get_day(number))

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()