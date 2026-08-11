def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

print(greet("Johnny"))
print(greet("Alice"))
