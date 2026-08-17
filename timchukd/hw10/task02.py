"""
Task2. Create a class Human, everyone has a name, 
create a method in the class that displays a welcome message to each person. 
Create a class method in the class that returns information that it is a species of 
"Homosapiens". And in the class create a static method that returns an arbitrary message.
"""

class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Welcome, {self.name}!"

    @classmethod
    def species_info(cls):
        return "We are a species of Homosapiens."

    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message."

human1 = Human("Boby")

print(human1.welcome_message())
print(Human.species_info())
print(Human.arbitrary_message())

"""
dtimchuk@dt hw10 % python task02.py
Welcome, Boby!
We are a species of Homosapiens.
This is an arbitrary message.
"""