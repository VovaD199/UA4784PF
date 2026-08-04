import re

def validity(password):
    print("Password should contain:\
              At least 1 letter between [a-z] and 1 letter between [A-Z].\
              At least 1 number between 10-9].\
              At least 1 character from [$#@]\
              Minimum length 6 characters.\
              Maximum length 16 characters.")
    if (
    len(password) >= 6
    and len(password) <= 16
    and re.search(r"[$#@]", password)
    and re.search(r"[0-9]", password)
    and re.search(r"[a-z]", password)
    and re.search(r"[A-Z]", password)
):
       return True
    else:
        return False
print(validity("DAun223@"))