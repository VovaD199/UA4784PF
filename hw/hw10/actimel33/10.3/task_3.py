class Employee:
    """Employee class that stores name and salary of workers."""
    count: int = 0                       # class variable - total number of employees

    def __init__(self, name: str, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    @classmethod
    def total_employees(cls) -> None:
        print(f"Total number of employees: {cls.count}")

    def display_info(self) -> None:
        print(f"Name: {self.name}, Salary: {self.salary}")



emp1 = Employee("John", 50000)
emp2 = Employee("Jane", 60000)
emp3 = Employee("Bob", 55000)

Employee.total_employees()
emp1.display_info()
emp2.display_info()
emp3.display_info()


print("__bases__  :", Employee.__bases__)
print("__dict__   :", Employee.__dict__)
print("__name__   :", Employee.__name__)
print("__module__ :", Employee.__module__)
print("__doc__    :", Employee.__doc__)
