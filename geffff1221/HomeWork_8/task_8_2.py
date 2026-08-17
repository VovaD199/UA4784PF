import re

password = input("Enter your password: ")

correct_password = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,16}$'

if re.match(correct_password, password):
    print("Password is valid.")
else:
    print("Password is invalid.")