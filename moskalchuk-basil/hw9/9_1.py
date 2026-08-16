from random import randint

secret_number = randint(1, 100)

for attempt in range(1, 11):
    
    print(f"Attempt - {attempt}")
    guess = int(input("Enter a number from 1 to 100: "))
    
    
    if guess < secret_number:
        print("The secret number is bigger.")
    elif guess > secret_number:
        print("The secret number is lower.")
    else:
        print("Successful!")
        break

else:
    print(f"You have used all 10 attempts. The number was {secret_number}.")