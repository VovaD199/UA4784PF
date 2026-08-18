class Animal:
    def __init__(self, name, species, number_of_legs):
        self.name = name
        self.species = species
        self.number_of_legs = number_of_legs
    def make_sound(self):
            pass

class Mammal(Animal):
    def make_sound(self):
         return "Roar"
    def give_birth(self):
         pass
class Bird(Animal):
     def make_sound(self):
        return "Squawk"
     def lay_eggs(self):
          pass

class Reptile(Animal):
     def make_sound(self):
        return "Hiss"
     def shed_skin(self):
          pass

animals = [Mammal("Lion", "Mammal", 4), Bird("Falcon", "Bird", 2), Reptile("Python", "Reptile", 4)]
for animal in animals:
    print(animal.make_sound())