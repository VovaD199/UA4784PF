from random import randint

secret_number = randint(1, 100)

for attempt in range(10):
    guess = int(input("Guess the number from 1 to 100: "))

    if guess == secret_number:
        print("Congratulations! You guessed the number!")
        break
    elif guess < secret_number:
        print("The number is greater.")
    else:
        print("The number is less.")
else:
    print("You have used all 10 attempts. The number was:", secret_number)