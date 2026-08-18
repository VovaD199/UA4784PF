import random

MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_ATTEMPTS = 10


def read_guess(attempts_left: int) -> int:
    """Keep asking until the user types a valid integer (doesn't burn an attempt)."""
    while True:
        raw = input(f"({attempts_left} attempts left) Enter your guess: ").strip()
        try:
            return int(raw)
        except ValueError:
            print(f"'{raw}' is not a whole number, try again.")


def play_round(secret: int) -> bool:
    """Runs the game loop, returns True if the player wins."""
    for attempt_number in range(1, MAX_ATTEMPTS + 1):
        attempts_left = MAX_ATTEMPTS - attempt_number + 1
        guess = read_guess(attempts_left)

        if guess == secret:
            print(f"🎉 Correct! You nailed it in {attempt_number} attempt(s).")
            return True

        direction = "higher" if guess < secret else "lower"
        print(f"Nope. The secret number is {direction} than {guess}.")

    return False


def main():
    print(f"I'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}.")
    print(f"You have {MAX_ATTEMPTS} attempts to guess it.\n")

    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)

    if not play_round(secret_number):
        print(f"💀 Out of attempts! The number was {secret_number}.")


if __name__ == "__main__":
    main()
