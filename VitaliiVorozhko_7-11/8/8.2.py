import password_checker

SPECIAL_SYMBOLS = "$#@"
MIN_LENGTH = 6
MAX_LENGTH = 16

while True:
    password = input("Enter your password: ")

    if password_checker.passwordcheck(
        password,
        SPECIAL_SYMBOLS,
        MIN_LENGTH,
        MAX_LENGTH
    ):
        print("Password is valid!")
        break

    print("Password is invalid. Please try again.")