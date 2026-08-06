#dynamic classes

import re
def class_name_changer(cls, new_name):
    if not new_name:
        raise Error
                   #^[^A-Z] starts with anything but uppercase alphabetical
                   #(?=[^A-Za-z0-9]) -- lookahead to check whether either non-alphabetical symbols or digits are present
    if re.findall("^[^A-Z]|(?=[^A-Za-z0-9])",new_name): #basically, if the response is non-empty
                                                        #then new_name does not meet requirements
        raise Error
    cls.__name__ = new_name
