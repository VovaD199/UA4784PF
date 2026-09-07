from random import randint

number = randint(1, 100)

for attempt in range(1, 11):
    guess = int(input(f"Attempt {attempt}/10. Guess the number: "))

    if guess == number:
        print(f"Congratulations! You guessed the number in {attempt} attempts!")
        break
    elif guess < number:
        print("The guessed number is greater.")
    else:
        print("The guessed number is less.")
else:
    print(f"You lost! You used all 10 attempts. The number was {number}.")