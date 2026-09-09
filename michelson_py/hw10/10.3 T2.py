class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        print(f"Вітаю, {self.name}!")

    @classmethod
    def species_info(cls):
        return "Homosapiens"

    @staticmethod
    def arbitrary_message():
        return "Це довільне статичне повідомлення."

person = Human("Олексій")
person.welcome_message()
print(f"Вид: {Human.species_info()}")
print(Human.arbitrary_message())