import os, re
os.system("cls")

password = str(input('Enter password: '))

if re.findall("[A-z][0-9]", password) \
and re.search(r'[@#$]', password) \
and len(password) >= 6 and len(password) <= 16:
    print(True)
else:
    print(False)

