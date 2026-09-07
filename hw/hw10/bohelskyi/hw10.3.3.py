class Employee:
    """Class representing an employee."""
    number_of_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.number_of_employees += 1

    @classmethod
    def get_employee_count(cls):
        return cls.number_of_employees

    def employee_info(self):
        return f"Name: {self.name}, Salary: {self.salary}"


if __name__ == "__main__":
    employee_1 = Employee("John Doe", 1500)
    employee_2 = Employee("Jane Doe", 2000)

    print(employee_1.employee_info())
    print(employee_2.employee_info())
    print(f"Total employees: {Employee.get_employee_count()}")

    print(f"Employee.__base__: {Employee.__base__}")
    print(f"Employee.__dict__: {Employee.__dict__}")
    print(f"Employee.__name__: {Employee.__name__}")
    print(f"Employee.__module__: {Employee.__module__}")
    print(f"Employee.__doc__: {Employee.__doc__}")
