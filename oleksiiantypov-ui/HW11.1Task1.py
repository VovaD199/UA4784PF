# Task 1

def check_odd_even(num):
    if num % 2 == 0:
        return 'Entered age is even'
    else:
        return 'Entered age is odd'

def check_if_negative(age):
    if age < 0:
        return ValueError(f'Error: Negative number')
    else:
        return check_odd_even(age)

if __name__ == '__main__':
    age = int(input("Enter an age: "))
    print(check_if_negative(age))

# Task 2
def check_week_day(number): 
    match number:
        case 1: 
            return 'Monday'
        case 2:
            return 'Tuesday'
        case 3:
            return 'Wednesday'
        case 4:
            return 'Thursday'
        case 5:
            return 'Friday'
        case 6:
            return 'Saturday'
        case 7:
            return 'Sunday'

def check_number():
    try:
        number = int(input('Enter a number from 1 to 7: '))
    except ValueError as e:
        return f'Error: {e}'
    else:
        if number <= 0 or number > 7 :
            return ValueError(f'Error: {number} is not from 1 to 7')
        else:
            return check_week_day(number)
        
if __name__ == '__main__':
    print(check_number())

        
    