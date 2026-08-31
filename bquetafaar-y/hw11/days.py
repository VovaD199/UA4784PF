days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

try:
    number = int(input("Give us the number of specific day: "))
    display_the_day = lambda number: days[number - 1]
    if number >= 8 or number <= 0:
        raise ValueError("Damn, you entered something too tough!")
    print(display_the_day(number))
except ValueError as error:
    raise error