class Employee:
    """This class represents an employee."""

    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def display_employee_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def display_employee_count(cls):
        print(f"Total number of employees: {cls.employee_count}")


employee1 = Employee("John", 3000)
employee2 = Employee("Anna", 4000)

employee1.display_employee_info()
employee2.display_employee_info()

Employee.display_employee_count()

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)