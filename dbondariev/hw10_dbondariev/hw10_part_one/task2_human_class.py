class Human:
    species = "Homo sapiens"

    def __init__(self, name):
        self.name = name


    def welcome_message(self):
        return f"Welcome {self.name}"


    @classmethod
    def get_species(cls):
        return f"This is species of {cls.species}."


    @staticmethod
    def arbitrary_message():
        return "This is arbitrary message."


human = Human("Dima")
print(human.welcome_message())
print(human.get_species())
print(human.arbitrary_message())
