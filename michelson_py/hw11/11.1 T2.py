days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

try:
    num = int(input("Enter day number: "))
    if 1 <= num <= 7:
        print(days[num])
    else:
        print("Error: Number must be between 1 and 7")
except ValueError:
    print("Error: Invalid input, not a number")