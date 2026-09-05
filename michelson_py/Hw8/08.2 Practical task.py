import re

def check_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[$#@]", password):
        return False
    return True

password = input("Enter password: ")
if check_password(password):
    print("Valid Password")
else:
    print("Invalid Password")