from password_validation import get_password_errors


password = input("Enter password: ")

errors = get_password_errors(password)

if errors:
    print("Password is invalid:")
    for error in errors:
        print("-", error)
else:
    print("Password is valid")