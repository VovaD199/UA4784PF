import re

def class_name_changer(cls, new_name):
    """A decorator to change the name of a class."""
    if not re.match(r'^[A-Z][a-zA-Z0-9_]*$', new_name):
        raise ValueError("Invalid class name")
    cls.__name__ = new_name
    return cls