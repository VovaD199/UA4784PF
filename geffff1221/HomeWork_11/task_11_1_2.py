days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

class CustomError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

def day_of_the_weekcalculations():
    day_of_the_week = int(input("Enter a number from 1 to 7: "))
    if day_of_the_week < 1 or day_of_the_week > 7:
        raise CustomError("Error: Please enter a number between 1 and 7.")
    return days_list[day_of_the_week - 1]

def main():
    try:
        result = day_of_the_weekcalculations()
        print(f"The day of the week is: {result}")
    except ValueError:
        print(CustomError("Error: Please enter a valid number."))
    except CustomError as e:
        print(e)
    
if __name__ == "__main__":
    main()
    