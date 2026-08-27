class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Welcome {self.name}!"

    @classmethod
    def type_of_human(cls):
        return f"Human species: {cls.species}"

    @staticmethod
    def arbitrary_message():
        return "Humans have cool brains"

if __name__ == "__main__":
    human = Human("Tom")

    print(human.greet())
    print(Human.type_of_human())
    print(Human.arbitrary_message())
