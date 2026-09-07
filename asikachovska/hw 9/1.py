from random import randint
number = randint(1, 100)
for i in range(0, 10):
    usernum = int(input('take guess!'))

    if usernum == number:
        print('you guessed right, congrats!')
        break
    elif usernum > number and usernum <= 100:
        print('too high')
    elif usernum < number and usernum >= 1:
        print('too low')
    else:
        print('wrong guess, the number should be between 1 and 100')
    if i == 9:
        print('you lose')