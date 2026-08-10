class Human:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return "Hello, my name is " + self.name

    @classmethod
    def species(cls):
        return f"{cls.__name__} представляет вид Homosapiens"
    
    @staticmethod
    def random_message(): 
        return "Hello world, i know OOP"
    
h = Human("Valerii")
print(h.say_hello())        # Hello, my name is Valerii
print(Human.species())      # Human представляет вид Homosapiens
print(Human.random_message())  # Hello world, i know OOP