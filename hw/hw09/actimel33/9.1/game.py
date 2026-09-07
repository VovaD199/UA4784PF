from random import randint

secret_number = randint(1, 100)

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100. Can you guess it in 10 tries?")


for attempt in range(1, 11):
    guess = int(input(f"Attempt {attempt}/10 - Enter your guess: "))
    
    if guess == secret_number:
        print(f"Congratulations! You guessed the correct number ({secret_number}) in {attempt} attempts!")
        break
    elif secret_number > guess:
        print("The secret number is greater than your guess.")
    else:
        print("The secret number is less than your guess.")
else:
    print(f"Game over! You have exhausted all 10 attempts. The number was {secret_number}.")
