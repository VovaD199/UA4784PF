import re

SMALL_LETTER_PATTERN = re.compile(r"[a-z]")
CAPITAL_LETTER_PATTERN = re.compile(r"[A-Z]")
NUMBER_PATTERN = re.compile(r"[0-9]")
SPECIAL_CHARACTER_PATTERN = re.compile(r"[$#@]")


# explicitly declared regex patterns for better readability and reuse
def compiled_pattern_password_validator(password):
    return bool(
        SMALL_LETTER_PATTERN.search(password)
        and CAPITAL_LETTER_PATTERN.search(password)
        and NUMBER_PATTERN.search(password)
        and SPECIAL_CHARACTER_PATTERN.search(password)
        and 6 <= len(password) <= 16
    )


# implementation without precompiled patterns
def simple_password_validator(password):
    return bool(
        re.search(r"[a-z]", password)
        and re.search(r"[A-Z]", password)
        and re.search(r"[0-9]", password)
        and re.search(r"[$#@]", password)
        and 6 <= len(password) <= 16
    )


# implementation with a single regex
def single_regex_password_validator(password):
    return bool(
        re.search(
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,16}$",
            password,
        )
    )


if __name__ == "__main__":
    password = input("Enter password to check: ")

    print(f"Password validation with precompiled patterns: {compiled_pattern_password_validator(password)}")
    print(f"Password validation with simple pattern compilation: {simple_password_validator(password)}")
    print(f"Password validation with oneline pattern compilation: {single_regex_password_validator(password)}")