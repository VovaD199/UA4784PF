"""
Task2.
Write a Python program to check the validity of a password (input from users).
Validation :
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
"""

import re

def password_check(passwd):
    if len(passwd) < 6 or len(passwd) > 16:
        return False
    if not re.search("[a-z]", passwd):
        return False
    if not re.search("[A-Z]", passwd):
        return False
    if not re.search("[0-9]", passwd):
        return False
    if not re.search("[$#@]", passwd):
        return False
    return True