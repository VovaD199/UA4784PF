import random

secret = random.randint(1, 100)
guessed = False

for attempt in range(1, 11):
    print(f"Attempt {attempt}/10")

    guess = int(input("Enter your guess: "))

    if guess == secret:
        print("Congratulations!")
        guessed = True
        break
    elif guess < secret:
        print("The secret number is greater.")
    else:
        print("The secret number is lower.")

if not guessed:
    print(f"You lost! The secret number was {secret}.")