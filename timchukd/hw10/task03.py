"""
Task3. Create an employee class. Each employee has characteristics such as name and salary. 
The class should have a counter that calculates the total number of employees, 
as well as a method that prints the total number of employees and a method that displays information
about each employee in particular, namely the name and salary. 
In addition to creating a class, display information about the base classes from 
which the employee class is inherited (_base_), the class namespace (_dict__), 
the class name (name_), the module name in which the class is defined (module__), 
the documentation bar (_doc__)
"""

class Employee:
    employee_counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_counter += 1

    @classmethod
    def print_employee_count(cls):
        print(f"Total employees: {cls.counter}")

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

employee1 = Employee("Tom", 50000)
employee2 = Employee("Boby", 60000)

print(f"Base classes: {Employee.__bases__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation: {Employee.__doc__}")
print(f"Total employees: {Employee.employee_counter}")

"""
dtimchuk@dt hw10 % python task03.py
Base classes: (<class 'object'>,)
Class namespace: {'__module__': '__main__', 'employee_counter': 2, '__init__': <function Employee.__init__ at 0x1028816c0>, 'print_employee_count': <classmethod(<function Employee.print_employee_count at 0x1028819e0>)>, 'display_info': <function Employee.display_info at 0x102881a80>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}
Class name: Employee
Module name: __main__
Documentation: None
Total employees: 2
"""