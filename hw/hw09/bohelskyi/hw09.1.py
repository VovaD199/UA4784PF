from random import randint

if __name__ == '__main__':
    answer = randint(1, 100)
    for _ in range(10):
        guess = int(input("Take guess: "))
        if guess == answer:
            print("You guessed right!")
            break
        elif guess > answer:
            print("You guessed too high!")
        else:
            print("You guessed too low!")
    else: print("You loser!")