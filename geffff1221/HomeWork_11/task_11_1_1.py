class MyErrorClass(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


def process_age(age):
    if age <= 0:
        raise MyErrorClass("You write incorrect age")
    elif age % 2 == 0:
        return "Even"
    else:
        return "Odd"


age = int(input("Please, write age: "))

try:
    print(process_age(age)) 
except MyErrorClass as e:
    print(e)