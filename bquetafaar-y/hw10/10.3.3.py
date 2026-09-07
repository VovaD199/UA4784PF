class Employee:
    counter = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1

    @classmethod
    def employeesCount(cls):
        print(cls.counter)

    def employeeInfo(self):
        print(self.name)
        print(self.salary)

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)