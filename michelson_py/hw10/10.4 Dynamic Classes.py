def change_class_name(cls, new_name):
    if not new_name.isalnum() or not new_name[0].isupper():
        raise ValueError("Invalid class name")
    
    cls.__name__ = new_name
    return cls