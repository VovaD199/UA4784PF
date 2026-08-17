import re

password = input()

low_letter = re.search(r"[a-z]", password)
capital_letter = re.search(r"[A-Z]", password)
digit = re.search(r"[0-9]", password)
special = re.search(r"[$#@]", password)

if 6 <= len(password) <= 16 and low_letter and capital_letter and digit and special:
    print("Password is valid")
else:
    print("Password is not valid")