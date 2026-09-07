"""
Task 1

Write a game script that randomly generates a number from a range of 1 to 100 and asks the user to guess that number in 10 tries.

The program reads the numbers entered by the user and prompts the user whether the guessed number is greater or less than the number
entered by the user. The game must continue until the user has used 10 attempts and guessed the number.

If the user guessed the number, the program prints a congratulatory message, and if 10 attempts have been exhausted and the user did not
have time to guess the number, then the corresponding message is displayed.

(To perform the task, you need to import the random module, and from it the randint() function.)
"""

from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 100

game_round = 1
score = 0
aim_number = randint(MIN_NUMBER, MAX_NUMBER)


def ask_for_number(message):
    """Prompt the user for input until a valid number is entered."""

    while True:
        str_input = input(message)

        try:
            return int(str_input)
        except ValueError:
            pass

        print(f"{str_input} is not a valid number. Try again")


def handle_attempt(attempt: int):
    global score

    user_input = ask_for_number(f"This is your attempt #{attempt}. What would be your next guess: ")

    if user_input == aim_number:
        score += 10
        print("Congratulations! Your guess was right!")

        return False

    if user_input < aim_number:
       print(f"Too low! {10 - attempt} attempts left.")

       return True

    if user_input > aim_number:
       print(f"Too high! {10 - attempt} attempts left.")

       return True


def handle_game_round():
    global game_round, aim_number

    print(f"This this round #{game_round} and your current score is {score}. Guess a number ({MIN_NUMBER}-{MAX_NUMBER}): ")


    for attempt in range(1, 11):
        if not handle_attempt(attempt):
            break
    else:
        print(f"Sorry, you're out of tries. The number was {aim_number}.")

    game_round += 1
    aim_number = randint(MIN_NUMBER, MAX_NUMBER)



print(f"Welcome to the game!!!")

while True:
    handle_game_round()
