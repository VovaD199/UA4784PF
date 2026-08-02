import re


def get_password_errors(password):
    errors = []

    checks = [
        (
            6 <= len(password) <= 16,
            "Password must be 6-16 characters long.",
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
            re.search(r"[$#@]", password),
            "Password must include at least one special character ($#@).",
        ),
    ]

    for is_valid, error_message in checks:
        if not is_valid:
            errors.append(error_message)

    return errors


def is_valid_password(password):
    return len(get_password_errors(password)) == 0