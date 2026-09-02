from random import randint

number = randint(1, 100)
attempts = 0

while attempts < 10:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess == number:
        print("You guessed the number!")
        break
    elif guess < number:
        print("The number is greater.")
    else:
        print("The number is less.")
else:
    print("You used all 10 attempts. The number was", number)