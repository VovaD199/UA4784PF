#Passwordcheck main
import password_check as pc

special_symbols = "$#@"
minlen = 6
maxlen = 16
while True:
    passwd = input("Bonjour! Enter your password:" \
    "\n\thint: password should contain:" \
    "\n\t\tat least one lowercase alphabetical letter"\
    "\n\t\tat least one uppercase alphabetical letter" \
    "\n\t\tat least one digit" \
    f"\n\t\tat least one of special symbols ({special_symbols})"\
    f"\n\t\tbe at least {minlen} and utmost {maxlen} symbols long"\
    "\nenter: ")

    if pc.passwordcheck(passwd,special_symbols,minlen,maxlen):
        print("Congratulations, the password satisfies all of the requirements!!!")
        break
    print("oops, passwrod too bad, need better")
