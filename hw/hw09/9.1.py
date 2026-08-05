from random import randint
def play_guess(n_attempts_:int=10,min_:int=1,max_:int=100) -> tuple[bool,int]:
    to_guess = randint(min_,max_)
    for i in range(n_attempts_):
        #this should've been put in try catch block, but we haven't gone through them yet
        guess = int(input(f"Attempts counter: {n_attempts_-i}\nEnter your guess btw {min_} and {max_} included: "))
        if guess == to_guess:
            return (True,i+1)
        correction = "That's not quite right, the number to guess is"
        correction = correction + f' smaller than {guess}' if to_guess < guess else correction + f' larger than {guess}'
        print('\n\n' + correction + '\n\n')
    return (False,n_attempts_)

if __name__ == "__main__":
    res,n = play_guess()
    if res:
        print(f"Congrats!!! You've successfully managed to guess the number in only {n} attempts!")
    else:
        print("*sad trombone plays*")
