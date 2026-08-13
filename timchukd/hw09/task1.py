"""
Task 1. Write a game script that randomly generates a number from a range of
1 to 100 and asks the user to guess that number in 10 tries. The program reads the numbers entered by the user and prompts the user whether the guessed number is greater or less than the number entered by the user. The game must continue until the user has used 10 attempts and guessed the number. If the user guessed the number, the program prints a congratulatory message, and if 10 attempts have been exhausted and the user did not have time to guess the number, then the corresponding message is
displayed.
(to perform the task, you need to import the random module,
softserve
and from it the randint() function)
"""

from random import randint

number = randint(1, 100)

for attempt in range(1, 11):
    guess = int(input(f"Attempt {attempt}/10. Guess the number: "))

    if guess == number:
        print(f"Congratulations! You guessed the number in {attempt} attempts!")
        break
    elif guess < number:
        print("The number is greater.")
    else:
        print("The number is less.")
else:
    print(f"Sorry! You didn't guess the number. It was {number}.")