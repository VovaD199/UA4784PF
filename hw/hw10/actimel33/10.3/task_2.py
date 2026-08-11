class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def species(cls):
        return "Homosapiens"

    @staticmethod
    def arbitrary_message():
        return "This is a static message"



person = Human("Alice")
person.welcome()
print("Species:", Human.species())
print("Static message:", Human.arbitrary_message())