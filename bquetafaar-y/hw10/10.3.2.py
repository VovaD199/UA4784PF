class Human:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        print(f"Hello {self.name}")

    @classmethod
    def species(cls):
        return "Homosapiens"

    @staticmethod
    def arb():
        return "an ode to locksmiths"

person = Human("Yaromyr")

person.greeting()

print(person.species())

print(person.arb())