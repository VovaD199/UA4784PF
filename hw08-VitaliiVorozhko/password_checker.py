def passwordcheck(password, special_symbols="$#@", min_length=6, max_length=16):
    if not min_length <= len(password) <= max_length:
        return False

    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in special_symbols for char in password)

    return has_lower and has_upper and has_digit and has_special