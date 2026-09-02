#Task 1
class Polygon:
    def __init__(self, sides):
        self.sides = sides


class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(4)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rectangle = Rectangle(5, 10)

print("Number of sides:", rectangle.sides)
print("Rectangle area:", rectangle.area())






#Task 2
class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def get_species(cls):
        return f"It is a species of {cls.species}"

    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message."


human = Human("Vitalii")

human.welcome()
print(Human.get_species())
print(Human.arbitrary_message())








#Task 3
class Employee:
    """Class that represents an employee."""

    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    @classmethod
    def total_employees(cls):
        print(f"Total employees: {cls.employee_count}")

    def employee_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


employee1 = Employee("John", 3000)
employee2 = Employee("Anna", 4000)
employee3 = Employee("Bob", 3500)

employee1.employee_info()
employee2.employee_info()
employee3.employee_info()

Employee.total_employees()

print("Base classes:", Employee.__base__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)