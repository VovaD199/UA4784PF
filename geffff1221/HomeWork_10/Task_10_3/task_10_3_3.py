class Employee:
    """A class representing a company employee."""
    count = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1
        
    @classmethod
    def get_count(cls):
        return cls.count
    
    def display_info(self):
        return f"Employee Name: {self.name}, Salary: {self.salary}"
    
emp1 = Employee("Иван", 50000)
emp2 = Employee("Анна", 60000)

print(emp1.display_info())
print(emp2.display_info())
print(f"Total employees: {Employee.get_count()}")

print("\n--- Служебная информация о классе ---")
print("__bases__:", Employee.__bases__)
print("__dict__:", Employee.__dict__)
print("__name__:", Employee.__name__)
print("__module__:", Employee.__module__)
print("__doc__:", Employee.__doc__)