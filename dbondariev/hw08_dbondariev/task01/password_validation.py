import re


def get_password_errors(password, min_length=6, max_length=16, special_chars="$#@"):
    errors = []

    checks = [
        (
            min_length <= len(password) <= max_length,
            f"Password must be {min_length}-{max_length} characters long.",
        ),
        (
            re.search(r"[a-z]", password),
            "Password must include at least one lowercase letter.",
        ),
        (
            re.search(r"[A-Z]", password),
            "Password must include at least one uppercase letter.",
        ),
        (
            re.search(r"[0-9]", password),
            "Password must include at least one digit.",
        ),
        (
            re.search(rf"[{re.escape(special_chars)}]", password),
            f"Password must include at least one special character ({special_chars}).",
        ),
    ]

    for is_valid, error_message in checks:
        if not is_valid:
            errors.append(error_message)

    return errors


def is_valid_password(password, min_length=6, max_length=16, special_chars="$#@"):
    return len(get_password_errors(password, min_length, max_length, special_chars)) == 0