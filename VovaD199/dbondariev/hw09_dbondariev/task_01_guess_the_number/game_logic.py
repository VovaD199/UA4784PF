from random import randint


MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_ATTEMPTS = 10


def generate_secret_number():
    return randint(MIN_NUMBER, MAX_NUMBER)


def get_hint(secret_number, user_number):
    if user_number < secret_number:
        return "The secret number is greater than your number."

    if user_number > secret_number:
        return "The secret number is less than your number."

    return "Correct"


def is_correct_guess(secret_number, user_number):
    return secret_number == user_number