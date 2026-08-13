def get_day_of_week(num):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }

    try:
        return days[num]
    except KeyError:
        return "There is no day for this number"


try:
    number = int(input("Enter number from 1 to 7: "))
    result = get_day_of_week(number)
    print(result)

except ValueError:
    print("You entered not a number")