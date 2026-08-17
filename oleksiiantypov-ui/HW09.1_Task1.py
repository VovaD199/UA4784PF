from random import randint
import os
os.system("cls")


if __name__ == '__main__':
    attempts = 1
    win = False
    number = randint(1, 100)

    print('You have 10 attempts. Try to guess number. Good luck!')

    while attempts <= 10 and win == False:
        itemp = int(input(f'Attemp: {attempts}. Enter number from 1 to 100: '))
        if number == itemp:
            win = True
            print('You win')
        elif number > itemp:
            print('Greater')
            attempts += 1
        elif number < itemp:
            print('Less')
            attempts += 1

    print(f'You lose. The number was {number}' if win == False else '')

        
