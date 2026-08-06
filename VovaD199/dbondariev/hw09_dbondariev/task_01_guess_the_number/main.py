from game_logic import (
    MIN_NUMBER,
    MAX_NUMBER,
    MAX_ATTEMPTS,
    generate_secret_number,
    get_hint,
    is_correct_guess,
)


def get_user_guess(attempt):
    while True:
        user_input = input(f"Attempt {attempt}. Enter your guess: ")

        try:
            user_number = int(user_input)
        except ValueError:
            print("Please enter a valid integer number.")
            continue

        if MIN_NUMBER <= user_number <= MAX_NUMBER:
            return user_number

        print(f"Please enter a number from {MIN_NUMBER} to {MAX_NUMBER}.")


def play_game():
    secret_number = generate_secret_number()

    print(f"Guess the number from {MIN_NUMBER} to {MAX_NUMBER}.")
    print(f"You have {MAX_ATTEMPTS} attempts.")

    for attempt in range(1, MAX_ATTEMPTS + 1):
        user_number = get_user_guess(attempt)

        if is_correct_guess(secret_number, user_number):
            print("Congratulations! You guessed the number!")
            print(f"You used {attempt} attempt(s).")
            break

        hint = get_hint(secret_number, user_number)
        print(hint)

    else:
        print("You used all attempts.")
        print(f"The secret number was: {secret_number}")


play_game()