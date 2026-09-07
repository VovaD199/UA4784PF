"""
Task2. Write a Python program to check the validity of a password (input from users).

Validation:
    - At least 1 letter between [a-z] and 1 letter between [A-Z].
    - At least 1 number between [0-9].
    - At least 1 character from [$#@].
    - Minimum length 6 characters.
    - Maximum length 16 characters.
"""

import re


def validate_password(password_str: str):
    validation_reg_ex = (
        r"^(?=.*[$#@])(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])[0-9A-Za-z$#@]{6,16}$"
    )

    return bool(re.fullmatch(validation_reg_ex, password_str))


# The set of test below was created with Claude

# --- Valid passwords ---
assert validate_password("Abcde1$") == True  # meets all rules
assert validate_password("Aa1#bc") == True  # exactly 6 chars (min length)
assert validate_password("Aa1#bcdefghijklm") == True  # exactly 16 chars (max length)
assert validate_password("Passw0rd@") == True  # typical good password
assert validate_password("Xy9$Zz") == True  # minimal valid combo

# --- Missing lowercase ---
assert validate_password("ABCDE1$") == False

# --- Missing uppercase ---
assert validate_password("abcde1$") == False

# --- Missing digit ---
assert validate_password("Abcdef$") == False

# --- Missing special character ---
assert validate_password("Abcdef1") == False

# --- Too short ---
assert validate_password("Ab1$") == False  # 4 characters
assert validate_password("Ab1#c") == False  # 5 characters

# --- Too long ---
assert validate_password("Aa1#bcdefghijklmno") == False  # 18 characters

# --- Wrong special character (not in $#@) ---
assert validate_password("Abcde1!") == False
assert validate_password("Abcde1%") == False

# --- Empty / edge inputs ---
assert validate_password("") == False
assert validate_password("      ") == False

# --- Multiple failures at once ---
assert validate_password("abc") == False
assert validate_password("ABCDEFGH") == False

# --- Boundary: exactly at length limit but missing a rule ---
assert validate_password("abcdef") == False


user_input: str = input("Please provide a password: ")

print(
    "The password is valid"
    if validate_password(user_input)
    else "The password is not valid"
)
