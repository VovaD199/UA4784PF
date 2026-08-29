class Human:
    def __init__(self, name):
        self.name = name

    def message(self):
        print(f'Welcome {self.name}')

    @classmethod
    def class_info(cls):
        return 'it is a species of Homosapiens'

    @staticmethod
    def static_method():
        return f'It is static method'

one = Human('Oleksii')
one.message()
print(Human.class_info())
print(one.static_method())