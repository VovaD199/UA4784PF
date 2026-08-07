def check_password_validity_basic(password: str) -> bool:
    """
        args: string
        return: boolean

        This programm check if password strong enough to use.
    """
    if not (6 <= len(password) <= 16):
        return False

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    special_chars = "$#@"

    # Scan each character in the password
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    # Password is valid only if all flags are True
    return has_lower and has_upper and has_digit and has_special

user_password = input("Enter a password to check: ")