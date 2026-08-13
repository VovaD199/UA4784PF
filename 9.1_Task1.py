from random import randint

secret_number = randint(1, 100)
for attempt in range(1, 11):
    guess = int(input("Guess the secret number between 1 and 100(10 attempts): "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the secret number {secret_number} in {attempt} attempts.")
        break
else:
    print(f"Sorry, you've used all your attempts. The secret number was {secret_number}.")

