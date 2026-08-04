def checkpass(password):
    islegit=true
    nums='0123456789'
    symbols = "$#@"
    alphabet="abcdefghijklmnopqrstuvwxyz"
    if len(password)<6 or len(password)>16:
        islegit=False
    if not any(char in alphabet for char in password):
        islegit=False
    if not any(char in alphabet.upper() for char in password):
        islegit=False
    if not any(char in nums for char in password):
        islegit=False
    if not any(char in symbols for char in password):
        islegit=False
    if islegit:
        print("Password is valid")
    else:
        print("Password is invalid")
passwd=input("Enter your password: ")
checkpass(passwd)